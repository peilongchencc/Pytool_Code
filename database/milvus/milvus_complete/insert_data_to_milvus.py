from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
import torch
import numpy as np
from transformers import ElectraModel, ElectraTokenizer
import time
from tqdm import tqdm
lines = []
with open("new_现代汉语常用词汇.txt", "r", encoding='utf-8')as f:
    for line in f.readlines():
        lines.append(line.strip('\n'))
    f.close()
start_time = time.time()
connections.connect(host='localhost', port='19530')

def create_milvus_collection(collection_name, dim):
    if utility.has_collection(collection_name):
        utility.drop_collection(collection_name)
    
    fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=False),
            FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=500),   
            FieldSchema(name="text_vector", dtype=DataType.FLOAT_VECTOR, dim=dim),
    ]
    schema = CollectionSchema(fields=fields, description='search text')
    collection = Collection(name=collection_name, schema=schema)
    
    index_params = {
        'metric_type': "COSINE",
        'index_type': "HNSW",
        'params': {"nlist": 1024, 'efConstruction': 10, 'M':60} # 'params': {"nlist": 1024, 'index_file_size': 1}
    }
    collection.create_index(field_name='text_vector', index_params=index_params)
    return collection

collection = create_milvus_collection('search_article_in_medium', 312)

from transformers import BertTokenizer, AlbertModel
tokenizer = BertTokenizer.from_pretrained("clue/albert_chinese_tiny")
model = AlbertModel.from_pretrained("clue/albert_chinese_tiny")

batch_size = 128
num_texts = len(lines)
vectors = []
array_dict = {}
count = 0

for i in tqdm(range(0, num_texts, batch_size)):

    batch_texts = lines[i:i + batch_size]
    ids = np.arange(i, min(i + batch_size, num_texts)).tolist()
    encoded_texts = tokenizer(batch_texts, return_tensors='pt', padding=True)
    with torch.no_grad():
        last_hidden_state = model(**encoded_texts).last_hidden_state
        attention_mask = encoded_texts["attention_mask"] 
        last_hidden_state = last_hidden_state * attention_mask.unsqueeze(-1)
        sum_hidden_state = last_hidden_state.sum(dim=1).squeeze()
        output = sum_hidden_state / attention_mask.sum(dim=1, keepdim=True)
        output = output.numpy()
    output = output / np.linalg.norm(output, axis=1, keepdims=True).tolist()
    collection.insert([ids, batch_texts, output.tolist()])

    array_dict[str(count)] = output
    count += 1
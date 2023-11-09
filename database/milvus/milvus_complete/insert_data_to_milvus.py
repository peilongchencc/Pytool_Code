from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
import torch
import numpy as np
import time
from tqdm import tqdm
from transformers import BertTokenizer, AlbertModel

def load_data_file(file_path):
    """加载文本数据
    Args:
        file_path:文本路径
    Return: 
        lines:文本数据
    """
    lines = []
    with open(file_path, "r", encoding='utf-8')as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
        f.close()
    return lines

def create_connection():
    """建立milvus连接(milvus默认为连接池形式)
    """
    print(f"\n创建Milvus连接...")
    connections.connect(host='localhost', port='19530')
    print(f"\n当前所连接数据库中含有的集合为:")
    print(utility.list_collections())   # 返回值为集合名(str)组成的list

def create_milvus_collection(collection_name, dim):
    """创建milvus集合
    Args:
        collection_name: 集合名称
        dim: 词向量字段的维度
    Return:
        collection: 创建的milvus集合
    """
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
        'params': {"nlist": 1024, 'efConstruction': 10, 'M':60}
    }
    collection.create_index(field_name='text_vector', index_params=index_params)
    return collection

class Convert_Batch_Text_2_Vector:
    """将文本以batch方式转为词向量,注意以batch方向转词向量需要消除padding的影响
    """
    tokenizer = BertTokenizer.from_pretrained("clue/albert_chinese_tiny")
    model = AlbertModel.from_pretrained("clue/albert_chinese_tiny")
    
    def __init__(self):
        pass
    def convert_batch_to_embed(self, text_data, batch_size, collection):
        """将文本以batch方式转为词向量
        Args:
            text_data: 待转化的文本,数据类型要求为list
            batch_size: batch大小
            collection: 准备插入的milvus集合
        Return:
            None: 由于执行的是插入操作,无返回值
        """
        # 获取待转化文本的长度，用于做batch切分
        num_texts = len(text_data)
        print(f"\n开始进行词向量批量转化，并按批次写入Milvus的{collection.name}集合中---\n")
        # 记录词向量转化开始时间
        start_time = time.time() 
        for i in tqdm(range(0, num_texts, batch_size)):
            batch_texts = text_data[i:i + batch_size]
            ids = np.arange(i, min(i + batch_size, num_texts)).tolist()
            encoded_texts = self.tokenizer(batch_texts, return_tensors='pt', padding=True)
            with torch.no_grad():
                # 通过模型获取文本的隐藏状态
                last_hidden_state = self.model(**encoded_texts).last_hidden_state
                # 获取注意力掩码
                attention_mask = encoded_texts["attention_mask"]
                # 将隐藏状态与注意力掩码相乘，用于消除padding的影响
                last_hidden_state = last_hidden_state * attention_mask.unsqueeze(-1)
                # 对隐藏状态求和，用于获得整个文本的表示
                sum_hidden_state = last_hidden_state.sum(dim=1).squeeze()
                # 通过注意力掩码的和进行归一化
                output = sum_hidden_state / attention_mask.sum(dim=1, keepdim=True)
                # 转化为numpy数组
                output = output.numpy()
            # 归一化输出向量，以便向量的模长为1
            output = output / np.linalg.norm(output, axis=1, keepdims=True).tolist()
            collection.insert([ids, batch_texts, output.tolist()])
        end_time = time.time()
        total_time = end_time - start_time
        print("*" * 30)
        print(f"恭喜🎉,数据已全部写入Milvus的{collection.name}集合中,共耗时{total_time}s。")
        print("*" * 30)

if __name__ == '__main__':
    # 加载数据
    file_path = "new_现代汉语常用词汇.txt"
    text_data = load_data_file(file_path)
    
    # 建立milvus连接
    create_connection()
    
    # 创建milvus集合
    milvus_collection = create_milvus_collection('search_article_in_medium', 312)
    
    # 词向量转化类的实例化
    albert_embed_model = Convert_Batch_Text_2_Vector()
    
    # 将文本数据转化为词向量，并以batch形式写入milvus集合
    albert_embed_model.convert_batch_to_embed(text_data, 128, milvus_collection)
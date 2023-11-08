## 利用Milvus向量数据库返回相似数据
- [利用Milvus向量数据库返回相似数据](#利用milvus向量数据库返回相似数据)
- [模型选择：](#模型选择)
- [程序运行方式：](#程序运行方式)
- [存储时索引构造解释:](#存储时索引构造解释)
- [词向量构造解释:](#词向量构造解释)

## 模型选择：

模型名称: `clue/albert_chinese_tiny`，可以通过下方链接下载:<br>

```txt
https://huggingface.co/clue/albert_chinese_tiny
```

## 程序运行方式：

1. 下载或将`clue/albert_chinese_tiny`文件移动到当前目录；

2. 运行`insert_data_to_milvus.py`文件；

3. 运行`sanic_milvus.py`文件；

4. 打开postman，选择POST模式，输入类似以下的URL；

URL: `http://8.140.203.xxx:8848/vector_similarity`<br>

5. 选择`Body`选项，自定义Value传入，点击Send即可。

Key|Value|Description
---|---|---
usr_input | 教师 | 

返回内容如下:<br>

> distance为相似度度量; fields为自定义的返回字段;

```json
{
    "相似度计算的结果为：": {
        "结果1": {
            "id": 161872,
            "distance": 1.0000001192092896,
            "fields": {
                "id": 161872,
                "text": "教师"
            }
        },
        "结果2": {
            "id": 161804,
            "distance": 0.9283397197723389,
            "fields": {
                "id": 161804,
                "text": "教学"
            }
        },
        "结果3": {
            "id": 28946,
            "distance": 0.9250288009643555,
            "fields": {
                "id": 28946,
                "text": "任课教师"
            }
        }
    }
}
```

❤️❤️❤️经测试:我的Milvus中存储了34万条向量数据(312维)，检索一条数据的耗时为2.7ms。<br>

## 存储时索引构造解释:

```python
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
        'params': {"nlist": 1024, 'efConstruction': 10, 'M':60}
    }
    collection.create_index(field_name='text_vector', index_params=index_params)
    return collection
```

1. `metric_type`: 定义用于向量搜索时计算向量之间相似度的度量类型。在这个例子中使用的是 "COSINE"，表示使用余弦相似度作为向量之间相似度的度量。余弦相似度是衡量两个向量方向上相似程度的一个度量标准，它的值域从-1（完全不同）到1（完全相同），其中0通常表示两个向量是正交的，即独立无关。

2. `index_type`: 指定用于集合中的向量字段的索引类型。在这个例子中，使用的是 "HNSW"，Hierarchical Navigable Small World（分层可导航小世界图），这是一种图的近似最近邻搜索算法，它在大规模和高维数据集上提供了高效的搜索性能。

3. `params`: 这是一个字典，包含用于构建索引时的额外参数。在这个例子中，有三个参数：
   - `nlist`: 表示在索引中划分的聚类的数量，这个参数对于索引的质量和搜索性能都有影响。
   - `efConstruction`: 是构建时的大小，这个参数决定了索引构建过程中的精度和性能。通常更高的 `efConstruction` 值会提高索引的质量，但同时会增加构建索引的时间和资源消耗。
   - `M`: 与 `HNSW` 索引相关的参数，它定义了图中节点的最大出度，也就是每个元素将连接多少个邻居。`M` 越大，构建索引的时间越长，但搜索的准确性可能会提高。

最后，`create_index` 方法是用来在集合的 `text_vector` 字段上创建指定类型的索引，以便更高效地执行搜索操作。<br>

## 词向量构造解释:

我的词向量构造较为复杂，具体代码如下:<br>

```python
# 使用tokenizer将文本编码
encoded_texts = tokenizer(batch_texts, return_tensors='pt', padding=True)
with torch.no_grad():
    # 通过模型获取文本的隐藏状态
    last_hidden_state = model(**encoded_texts).last_hidden_state
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
```

你可能会想，或着你可能在其他地方见到过，类似下面这种简单的写法:<br>

```python
# 使用tokenizer将文本编码
encoded_texts = tokenizer(batch_texts, return_tensors='pt', padding=True)
with torch.no_grad():
    output = model(**encoded_texts).last_hidden_state.mean(dim=1).squeeze().numpy()
```

**🚀🚀🚀你也许会想，为什么不用这种简单的写法呢？**<br>

是的，你可以使用这种方法直接获取每个文本的平均词向量表示。这行代码将完成以下几个步骤：<br>

1. `model(**encoded_texts).last_hidden_state`：这会通过模型获得每个token的词向量表示。`last_hidden_state` 是模型最后一层的输出，它包含了每个token的隐藏状态。

2. `.mean(dim=1)`：这个操作会在第一个维度（即sequence长度的维度）上计算平均值，因此对于每个文本，它会将所有token的词向量进行平均，这样就得到了单个向量表示整个文本的平均隐藏状态。这忽略了不同词语的重要性可能不同，并假设所有词语都同等重要。

3. `.squeeze()`：如果维度中有任何单维度，则此操作会移除它们。比如，如果维度是`(batch_size, 1, hidden_size)`，它会变成`(batch_size, hidden_size)`。

4. `.numpy()`：这将把结果从PyTorch张量转换为NumPy数组，方便后续处理或存储。

🚨🚨🚨但是，使用`.mean()`函数有一个缺点：**它会对所有tokens的向量进行平均，包括那些填充的tokens（即[PAD] tokens）。**这可能会稀释实际有意义词汇的表示，尤其是在处理长度不一的句子时。如果你想要一个更加精确的文本表示，那么应该只对实际的词汇（而非填充的部分）计算平均值或者其他形式的聚合。<br>

🌿🌿🌿在之前的代码中，笔者通过乘以`attention_mask`来确保只有非填充tokens被考虑在内，这样可以获得更加准确的文本表示。<br>

**如果你决定使用`.mean()`，请确保你的数据集中大部分文本的长度相近，这样填充对于结果的影响才不会太大。** 如果文本长度相差很大，就应该采用类似之前代码中的加权平均，这样对于不同长度的文本都能获得较为准确的表示。<br>
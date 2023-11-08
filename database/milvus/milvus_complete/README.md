## 利用Milvus向量数据库返回相似数据

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
# Example

## 文件介绍：

文件名|用途|备注
---|---|---
db_config.py | 配置文件 | 
empty_mongodb.py | 清空mongodb中数据 | 注意修改集合名称
fetch_from_mongodb.py | 从mongodb获取数据 | 
insert_to_mongodb.py | 向mongodb存储数据 | 
mongodb_id.json | 记录向mongodb存储数据的id | 通过id从MongoDB检索，速度最快，注意修改键名
mongodb_utils.py | 函数文件 | 包括：连接池建立，存储、获取函数构建

## 文件运行顺序：
1. 检查db_config.py文件。

2. 清空mongodb中数据。(可选)

```bash
python empty_mongodb.py
```

3. 向mongodb存储数据。

```bash
python insert_to_mongodb.py
```

4. 从mongodb获取数据。

```bash
python fetch_from_mongodb.py
```

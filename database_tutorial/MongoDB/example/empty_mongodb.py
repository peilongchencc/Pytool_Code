import pymongo
from db_config import Mongodb_Server_Config

# 连接到 MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")

# 选择你要清空数据的数据库和集合
db = client[Mongodb_Server_Config['mongodb_database']]
collection = db[Mongodb_Server_Config['mongodb_collection']]

# 使用 delete_many 方法删除集合中的所有文档
result = collection.delete_many({})

# 打印删除的文档数量
print(f"删除了 {result.deleted_count} 个文档")

# 关闭 MongoDB 连接
client.close()
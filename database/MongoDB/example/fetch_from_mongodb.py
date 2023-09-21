from mongodb_utils import fetch_onedata_from_mongodb
from db_config import Mongodb_Server_Config, Mongodb_Id_Path
from bson import ObjectId
import time
import json

start_time = time.time() 
# 获取mongodb集合信息
collection_name = Mongodb_Server_Config['mongodb_collection']
# 打开JSON文件并加载内容
with open(Mongodb_Id_Path, 'r') as file:
    data = json.load(file)

# 将str转为ObjectId
financial_mongo_id = ObjectId(data["financial"])
sale_mongo_id = ObjectId(data["sale"])

# 从mongodb获取数据
mongo_query = {"_id": financial_mongo_id}
data = fetch_onedata_from_mongodb(mongo_query, collection_name)
# 获取的数据类似{'_id': ObjectId('650c0126e3075b37f6a43bfb'), 'name': 'John', 'age': 30, 'score': {'chinese': 87, 'math': 99, 'english': 92}}
# 可以使用以下指令去除，也可以不去除，毕竟是字典。
# del data['_id']
# print(data)
print(type(data)) # <class 'dict'>
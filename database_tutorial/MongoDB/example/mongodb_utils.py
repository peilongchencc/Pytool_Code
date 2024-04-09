from pymongo import MongoClient
from pymongo import uri_parser
from db_config import Mongodb_Server_Config
import json

# 构建MongoDB连接URI
mongodb_uri = f"mongodb://{Mongodb_Server_Config['mongodb_host']}:{Mongodb_Server_Config['mongodb_port']}/{Mongodb_Server_Config['mongodb_database']}"

# 解析URI，获取连接池配置
parsed_uri = uri_parser.parse_uri(mongodb_uri)

# 创建MongoDB连接池
client_pool = MongoClient(mongodb_uri, maxPoolSize=5)   # 指定连接池大小为5，根据需要进行调整

# collection_name = Mongodb_Server_Config['mongodb_collection']

# 在需要的地方获取连接
def get_mongodb_connection():
    return client_pool.get_database()

def insert_onedata_to_mongodb(document, collection_name, file_name=None, key_name=None):
    """单个文档插入mongodb
    
    Args:
        document (dict): 要插入mongodb的字典
        collection_name (str): mongodb中的集合名称
        file_name (str): 用于将生成的mongodb索引id存储，便于之后检索。
    
    Returns:
        None
        
    Notes:
        不需要手动关闭mongodb连接,mongodb连接池会自动管理连接的生命周期
    """
    # 从mongodb连接池获取一个连接
    mongo_db = get_mongodb_connection()
    # 选择一个集合（类似于关系型数据库中的表）
    collection = mongo_db[collection_name]
    result = collection.insert_one(document)
    print(f"Inserted document with id: {result.inserted_id}")

    if file_name is not None:
        # 打开JSON文件并加载内容
        with open(file_name, 'r') as file:
            data = json.load(file)

        # 更新JSON对象中的数据
        data[key_name] = str(result.inserted_id) # 将 `ObjectId` 转换为字符串形式

        # 将更新后的数据写回JSON文件
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)  # indent参数用于格式化输出，可选

        print("JSON文件已更新。")
    

# 示例函数，从MongoDB获取数据
def fetch_onedata_from_mongodb(mongo_query, collection_name):
    """从mongodb获取数据
    
    Args:
        mongo_query (dict): mongodb的检索条件
        collection_name (str): mongodb中的集合名称
    
    Returns:
        result (dict): 从mongodb获取数据
        
    Notes:
        不需要手动关闭mongodb连接,mongodb连接池会自动管理连接的生命周期
    """
    # 从mongodb连接池获取一个连接
    mongo_db = get_mongodb_connection()
    # 选择一个集合（类似于关系型数据库中的表）
    collection = mongo_db[collection_name]
    result = collection.find_one(mongo_query)
    return result
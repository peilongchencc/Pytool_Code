import redis
import pickle

# 连接到Redis
r = redis.Redis(host='localhost', port=6379, db=0)

######################################################################
# 运行 r.get("xxx") 的文件才需要导入类的定义，所以本文件不需要导入类的定义。
######################################################################

def get_classOfclass_data():
    print("--执行get_redis_function.py文件--")
    # 从Redis获取
    serialized_data_from_redis = r.get('my_classOfclass')
    # 反序列化
    deserialized_data = pickle.loads(serialized_data_from_redis)
    print("从Redis获取数据成功，类的属性为：")
    print(deserialized_data.name)                   # 输出：instance_a
    print(deserialized_data.b_obj.name)             # 输出：instance_b
    print(deserialized_data.b_obj.c_obj.name)       # 输出：instance_c

import redis
import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

# 创建一个 Python 对象
tmp_data = {
    1: MyClass("销售"),
    2: MyClass("理财"),
    3: MyClass("保险")
}


# 创建Redis客户端连接
# redis_client = redis.Redis(host='localhost', port=6379, db=0) # 以序号指定Redis中的数据库，可以不用。没写密码是因为我本地redis没有设置密码。
redis_client = redis.Redis(host='localhost', port=6379)

# 将类对象序列化为字节流，然后存入Redis
my_object_bytes = pickle.dumps(tmp_data)
redis_client.set('my_object', my_object_bytes)

# 从Redis中提取对象，然后将字节流反序列化为类对象；
my_object_bytes = redis_client.get('my_object')
my_object = pickle.loads(my_object_bytes)

# 打印提取到的对象的值
print(my_object[1])
print(my_object[1].value)
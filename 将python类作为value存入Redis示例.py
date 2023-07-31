import redis
import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

# 创建Redis客户端连接
redis_client = redis.Redis(host='localhost', port=6379)

# 将对象存入Redis
my_object = MyClass(42)
my_object_bytes = pickle.dumps(my_object)
redis_client.set('my_object', my_object_bytes)

# 从Redis中提取对象
my_object_bytes = redis_client.get('my_object')
my_object = pickle.loads(my_object_bytes)

# 打印提取到的对象的值
print(my_object.value)
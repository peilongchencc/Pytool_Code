import redis
import pickle

# 连接到Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# 定义类
class C:
    def __init__(self, name):
        self.name = name

class B:
    def __init__(self, name, c_obj):
        self.name = name
        self.c_obj = c_obj

class A:
    def __init__(self, name, b_obj):
        self.name = name
        self.b_obj = b_obj

# 实例化类，类互相嵌套
c_instance = C('instance_c')
b_instance = B('instance_b', c_instance)
a_instance = A('instance_a', b_instance)

# 将对象序列化
serialized_data = pickle.dumps(a_instance)

# 存入Redis
r.set('my_classOfclass', serialized_data)

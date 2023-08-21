import redis
import pickle

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

data = {"key1": "value1",
        "key2": "value2",
        "key3": "value3"}
data = pickle.dumps(data)
# 使用hmset命令将字典存储为一个哈希
r.set("my_dict", data)

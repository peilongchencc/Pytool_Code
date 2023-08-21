import redis
import pickle

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 获取存储在哈希中的全部键值对
result = r.get("my_dict")
result = pickle.loads(result)
print(result)

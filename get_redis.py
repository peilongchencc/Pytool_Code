import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 获取存储在哈希中的全部键值对
result = r.get("my_str")                        # b'Hello, world!'
decoded_result = result.decode()                # 等同于 result.decode("utf-8")；
print(decoded_result)                           # Hello, world!
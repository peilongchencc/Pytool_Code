# 将dict存入 Redis；

import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

data = "Hello, world!"

# 使用hmset命令将字典存储为一个哈希
r.set("my_str", data)

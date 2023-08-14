import redis
import json

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)
# 将数据存入redis

redis_key = "your_data_key"
data = {"id":33,
        "name":"Tom",
        "score":"97"}

r.set(redis_key,json.dumps(data))
r.expire(redis_key, 608400)    # 设置存储时间为7天+1小时；

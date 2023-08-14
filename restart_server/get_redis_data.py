import redis
import json

# 创建Redis连接
r = redis.Redis(host='localhost',password='', port=6379, db=0)  # 密码没有设置，所以这里用的空。


res = json.loads(r.get("your_data_key"))    # 利用存入Redis中的key取值；
print(res)
print(type(res))
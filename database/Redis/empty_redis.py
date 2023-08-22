# 清空Redis中的数据，慎重操作！
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)
# 清空redis
r.flushall()
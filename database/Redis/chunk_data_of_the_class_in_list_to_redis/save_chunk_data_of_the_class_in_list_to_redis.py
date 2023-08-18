import pickle
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

class Car:
    def __init__(self, make, model, year):
        self.make = make    # 汽车厂商；
        self.model = model  # 汽车型号；
        self.year = year    # 汽车出厂年份；

# 数据都是捏造的；
data_list = [Car("长城","t1","2000"),Car("长城","t2","2001"),Car("奥迪","a6","2010"),Car("奥迪","a8","2014"),Car("奥迪","a10","2016")]
# print(data_list)
# print(len(data_list))

# 将数据长度存入Redis
r.set("data_list_length",len(data_list))

business_name = 'traffic'   # 每个 chunk 的 redis-key 前缀；

#######################################
# 将数据按照 n 个为一组进行存储；
#######################################
chunk_size = 2

if len(data_list) != 0:
    # 将 data_list 拆分为多个 chunks
    # chunks = [[<__main__.Car object1>,<__main__.Car object2>],    # n个元素为一个list；
    #           [<__main__.Car object3>,<__main__.Car object4>]]
    #           [<__main__.Car object5>]]
    chunks = [data_list[i:i+chunk_size] for i in range(0, len(data_list), chunk_size)]

    for i, chunk in enumerate(chunks):
        # 为每个 chunk 创建一个 Redis 键
        data_list_rediskey = business_name + "_data_list_" + str(i)

        # 将 chunk 存入 Redis
        r.set(data_list_rediskey, pickle.dumps(chunk))    # 非必要不要使用pickle或json序列化与反序列化，非常耗时；
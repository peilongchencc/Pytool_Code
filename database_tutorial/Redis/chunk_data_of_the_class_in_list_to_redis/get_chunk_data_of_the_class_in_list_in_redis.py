import pickle
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 存入Redis的内容如果是类，必须将类也导入；如果是类A中使用了类B，需要将类A和类B都导入。
# 可以使用 from ... import classA, classB 的形式；
class Car:
    def __init__(self, make, model, year):
        self.make = make    # 汽车厂商；
        self.model = model  # 汽车型号；
        self.year = year    # 汽车出厂年份；


business_name = 'traffic'
chunk_size = 2

# 从Redis获取数据长度
data_list_length = int(r.get('data_list_length'))
print(f'data_list_length的值为：{data_list_length}')

# 获取 Redis 中存储的 chunk 数量
num_chunks = (data_list_length + chunk_size - 1) // chunk_size
print(f'num_chunks的值为：{num_chunks}')

# 恢复data_list
restored_data_list = []

for i in range(num_chunks):
    # 获取 Redis 键
    data_list_rediskey = business_name + "_data_list_" + str(i)

    # 从 Redis 中获取 chunk
    chunk = r.get(data_list_rediskey)

    # 如果 chunk 存在，则进行反序列化并添加到复原的列表中
    if chunk:
        restored_chunk = pickle.loads(chunk)         # 非必要不要使用pickle或json序列化与反序列化，非常耗时；
        restored_data_list.extend(restored_chunk)

# 打印复原后的 tmp_QA_list
print(restored_data_list)
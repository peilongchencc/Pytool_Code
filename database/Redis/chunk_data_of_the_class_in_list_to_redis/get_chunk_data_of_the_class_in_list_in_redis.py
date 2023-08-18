import pickle
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

business_name = 'traffic'
chunk_size = 10

# 从Redis获取数据长度
data_list_length = int(r.get('data_list_length'))

# 获取 Redis 中存储的 chunk 数量
num_chunks = (data_list_length + chunk_size - 1) // chunk_size

# 恢复data_list
restored_data_list = []

for i in range(num_chunks):
    # 获取 Redis 键
    data_list_rediskey = business_name + "_data_list_" + str(i)

    # 从 Redis 中获取 chunk
    chunk = r.get(data_list_rediskey)

    # 如果 chunk 存在，则进行反序列化并添加到复原的列表中
    if chunk:
        restored_chunk = pickle.loads(chunk)
        restored_data_list.extend(restored_chunk)

# 打印复原后的 tmp_QA_list
print(restored_data_list)
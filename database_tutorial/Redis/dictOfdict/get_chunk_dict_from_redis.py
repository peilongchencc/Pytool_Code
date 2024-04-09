################################################
# 从redis获取分段存储的字典嵌套字典结构，然后反序列化。
################################################
import redis
import pickle

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

CHUNK_SIZE = 2  # 选择一个合适的大小

data_length = r.llen("data_length")

reconstructed_data = {}
chunk_count = (data_length + CHUNK_SIZE - 1) // CHUNK_SIZE

for i in range(chunk_count):
    chunk_data = pickle.loads(r.get(f'data_chunk_{i}'))
    reconstructed_data.update(chunk_data)
    
print(reconstructed_data)
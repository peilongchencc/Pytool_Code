#########################
# 分段存储字典嵌套字典
#########################
import redis
import pickle

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

data = {'-2': {'text': {}, 'list': {}}, '-3': {'text': {}, 'list': {}}, 'WJT-4-20220208-1': {'text': {'减': ['减', '减仓', '减持', '割肉', '卖', '卖了', '赎回了', '卖出了', '赎出了', '卖掉了', '减仓了', '减了', '减持了', '取出了', '取了', '卖出', '卖掉', '取', '取出', '赎出', '赎回'], '三佳': ['三佳', '组合三佳', '货币三佳'], '到': ['到', '到账'], '资金': ['资金', '钱']}, 'list': {}}}


CHUNK_SIZE = 2  # 选择一个合适的大小
keys = list(data.keys())
print(type(keys))
print(keys)

r.delete("data_length")   # 删除之前的键，避免采用数据插入的方式。
r.lpush("data_length", *keys)

for i in range(0, len(keys), CHUNK_SIZE):
    chunk = {key: data[key] for key in keys[i:i+CHUNK_SIZE]}
    r.set(f'data_chunk_{i // CHUNK_SIZE}', pickle.dumps(chunk))
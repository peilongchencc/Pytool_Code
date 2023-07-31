import redis
import json

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 存储数据
data = {
    1: "financial_new",
    2: "sale",
    3: "insurance",
    4: "other"
}
r.set("systemid_2_dataname", json.dumps(data))  # redis只能存字符串，其他类型需要用json.dumps转换；

# 获取数据并解析
result = r.get("systemid_2_dataname")
parsed_result = json.loads(result)

# 将字符串转换回数字类型
parsed_result = {int(k): v for k, v in parsed_result.items()}

# 打印结果
print(parsed_result)

# 常用 Redis 指令：
# redis-cli          # 终端连接到 Redis；
# KEYS *             # 返回当前数据库中所有的键列表;
# GET "my_object"    # 获取键对应的值;
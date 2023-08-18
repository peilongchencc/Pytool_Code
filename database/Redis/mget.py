import redis

# 假设你已经连接到了Redis数据库
r = redis.Redis(host='localhost', port=6379)


import time
start_time = time.time() 

# 生成键名列表
keys = ['financial_tmp_QA_list_'+str(i) for i in range(100)]

# 一次性获取多个键的值
values = r.mget(keys)

# 将获取的值组成一个list
result = list(values)

end_time = time.time() 
execution_time = end_time - start_time 
print(f"执行时间为：{execution_time} 秒")
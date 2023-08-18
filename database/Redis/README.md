# Redis

## 测试 Redis 连接：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)
```

## 使用python代码清空Redis
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)
# 清空redis
r.flushall()
```

## 数字存入redis与提取：
### 整数：
注意：在Redis中，set命令只能存储字符串值。即使你尝试将数字、列表、字典等非字符串类型的数据存储为值，Redis也会将其视为字符串进行存储，其实是字节形式。<br>
```python
import pickle
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)
# 存入Redis
r.set("number",123)

# 从Redis取出数据
res = int(r.get("number"))
print(res)          # 123
print(type(res))    # <class 'int'>
```
从Redis取出数据要注意数据类型的转化，以上述代码举例，`r.get("number")` 获取的结果为：`b'123'`，类型为：`<class 'bytes'>`。<br>

### 浮点数：
```python
import pickle
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)
# 存入Redis
r.set("number",123.4)

# 从Redis取出数据
res = float(r.get("number"))
print(res)          # 123.4
print(type(res))    # <class 'float'>
```
与从Redis取出整数相同，要注意数据类型的转化，以上述代码举例，`r.get("number")` 获取的结果为：`b'123.4'`，类型为：`<class 'bytes'>`。<br>
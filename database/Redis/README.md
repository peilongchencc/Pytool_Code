# Redis
本文分两部分，前文介绍Redis一下基础使用，后文介绍各文件及文件夹作用。<br>

## Ubuntu 18.04安装Redis：
1. 更新软件包列表：
```shell
sudo apt update
```

2. 安装Redis服务器：
```shell
sudo apt install redis-server
```
安装完成后，Redis服务器将自动启动，此时终端即可使用 redis-cli 指令。（ Redis 的安装真的很简单🤭）<br>
<br>

## 终端Redis常用指令：
**开启/关闭 Redis 服务:**
```shell
redis-server          # 开启 Redis 服务；
redis-cli shutdown    # 关闭 Redis 服务；
```

**查看 Redis 版本：**
可通过下列2种方法中的任何一种方法查看 Redis 版本：<br>
1. 终端查看：

终端输入下列指令即可查看到 Redis 版本信息：<br>
```shell
redis-server --version
```
注意⚠️：Ubuntu 18.04 只提供Redis 4.0.9版本的安装。<br>

2. 进入 Redis 数据库内部查看：
- 打开终端并输入:
```shell
redis-cli
```
此时会显示 `127.0.0.1:6379>` ，这表示你已经进入了 Redis 数据库。<br>

- 在 `127.0.0.1:6379>` 后输入： 
```shell
INFO SERVER
```
显示的内容为 Redis 服务器的信息，包括版本号。退出操作很多，包括输入 `exit`、`quit` 或 按 `Ctrl+c`。<br>

**查看存入 Redis 中的数据：**
注意⚠️：如果数据是以 byte(字节) 存入的 Redis，使用GET指令无法看到真实数据；<br>
```shell
redis-cli          # 终端连接到 Redis；
KEYS *             # 返回当前数据库中所有的键列表;
GET "my_object"    # 获取键对应的值;
```

**清空 Redis 数据：**
> 如果Redis关闭了，所有数据都会被清空，无论是否设置了过期时间。当Redis重新启动时，它将是一个空的数据库，之前存储的数据将会丢失。

终端输入 `redis-cli` 进入Redis数据库，然后输入：<br>
```shell
FLUSHALL    # "清除全部"
```
这个命令将删除所有数据库中的数据，包括所有的键、值、过期时间以及配置信息。🚨🚨🚨请谨慎使用该命令，因为删除的数据无法恢复。<br>

可以设置数据的过期时间，如果不是自己本地的 Redis，自己可以随意改动，最好不要使用此命令。<br>

## python 安装 Redis 库：
安装了Redis库才能使用python与Redis库连接，否则只能使用终端连接。<br>
```shell
pip install redis
```

## 测试 Redis 连接：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)
```

## 使用python代码清空 Redis 中的数据：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)
# 清空redis
r.flushall()
```

## 字符串存入 Redis 与提取：
注意⚠️⚠️⚠️：从Redis获取到的数据类型均为 byte(字节)，需要进行转换为自己需要的形式，例如使用 Redis 自带的 decode() 方法，将数据转换为str。<br>

### 使用 set 将字符串存入 Redis：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

data = "Hello, world!"

# 使用set命令将字符串存储
r.set("my_str", data)
```

### 使用 get 从 Redis 取出 字符串 数据：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 获取存储在Redis中的字符串
result = r.get("my_str")                        # b'Hello, world!'
decoded_result = result.decode()                # 等同于 result.decode("utf-8")；
print(decoded_result)                           # Hello, world!
```

### Redis 中 decode 函数解释：
```python
(method) def decode(
    encoding: str = "utf-8",
    errors: str = "strict"
) -> str
```
`decode` 方法默认将数据转化为 `str`。<br>


## 数字存入 Redis 与提取：
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

## dict存入 Redis 与取出：
### 使用 hmset 将 dict 存入 Redis：
使用 `hmset` 会遇到提示 `DeprecationWarning: Redis.hmset() is deprecated. Use Redis.hset() instead.`，不影响使用，Ubuntu 18.04 只提供Redis 4.0.9版本的安装。<br>
```python
# 将dict存入 Redis；

import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

data = {"key1": "value1",
        "key2": "value2",
        "key3": "value3"}

# 使用hmset命令将字典存储为一个哈希
r.hmset("my_dict", data)
```

### 使用 hgetall 从 Redis 取出 dict 数据：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 获取存储在哈希中的全部键值对
result = r.hgetall("my_dict")       
print(result)                           # {b'key1': b'value1', b'key2': b'value2', b'key3': b'value3'}

restore_data = {}
for key, value in result.items():
    restore_data[key.decode()] = value.decode()

print(restore_data)                     # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```


## 文件介绍：
chunk_data_of_the_class_in_list_to_redis: 将python类组成的列表按照chunk分段存入Redis，再从Redis中取出还原列表。<br>
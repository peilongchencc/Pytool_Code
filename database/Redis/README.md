# Redis
Redis是一个开源的高性能键值对存储数据库，它主要用于缓存、消息队列、实时分析、排行榜和会话管理等场景。<br>

Redis具有快速、可靠、灵活、可扩展的特点，支持多种数据结构（字符串、哈希、列表、集合、有序集合等）。<br>

将 python 与 Redis 结合可实现数据的快速加载(〽️**因为数据就在缓存中**〽️)，避免重复读取，从而提升项目的整体运行速度。<br>

本文分两部分，前半部分介绍 Redis 基础使用，后半部分介绍当前目录下各文件及文件夹作用。<br>

## Ubuntu 18.04 安装 Redis 步骤：
1.更新软件包列表：
```shell
sudo apt update
```

2.安装Redis服务器：
```shell
sudo apt install redis-server
```
安装完成后，Redis服务器将自动启动，此时终端即可使用 redis-cli 指令。（ Redis 的安装真的很简单🤭）<br>
<br>

## 终端Redis常用指令：
### 开启/关闭 Redis 服务:
```shell
redis-server          # 开启 Redis 服务；
redis-cli shutdown    # 关闭 Redis 服务；
```

### 查看 Redis 版本：
可通过下列2种方法中的任何一种方法查看 Redis 版本：<br>
#### 终端查看：

终端输入下列指令即可查看到 Redis 版本信息：<br>
```shell
redis-server --version
```
注意⚠️：Ubuntu 18.04 只提供Redis 4.0.9版本的安装。<br>
<br>

#### 进入 Redis 数据库内部查看：
1.打开终端并输入以下指令:
```shell
redis-cli
```
此时会显示 `127.0.0.1:6379>` ，这表示你已经进入了 Redis 数据库。<br>

2.在 `127.0.0.1:6379>` 后输入： 
```shell
INFO SERVER
```
显示的内容为 Redis 服务器的信息，包括版本号。退出操作很多，包括输入 `exit`、`quit` 或 按 `Ctrl+c`。<br>
<br>

### 查看存入 Redis 中的数据：
注意⚠️：如果数据是以 byte(字节) 存入的 Redis，使用GET指令无法看到真实数据；<br>
```shell
redis-cli          # 终端连接到 Redis；
KEYS *             # 返回当前数据库中所有的键列表;
GET "my_object"    # 获取键对应的值;
```

### 清空 Redis 中的数据：
> 如果Redis关闭了，所有数据都会被清空，无论是否设置了过期时间。当Redis重新启动时，它将是一个空的数据库，之前存储的数据将会丢失。

终端输入 `redis-cli` 进入Redis数据库，然后输入：<br>
```shell
FLUSHALL    # "清除全部"
```
这个命令将删除所有数据库中的数据，包括所有的键、值、过期时间以及配置信息。🚨🚨🚨请谨慎使用该命令，因为删除的数据无法恢复。<br>

可以设置数据的过期时间，如果不是自己本地的 Redis，自己可以随意改动，最好不要使用此命令。<br>
<br>

## Redis 在 python 的应用：

### python 安装 Redis 库：
安装了Redis库才能使用python与Redis库连接，否则只能使用终端连接。<br>
```shell
pip install redis
```

### 测试 Redis 连接：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)
```

### 使用python代码清空 Redis 中的数据：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)
# 清空redis
r.flushall()
```

### 字符串存入 Redis 与提取：
注意⚠️⚠️⚠️：从Redis获取到的数据类型均为 byte(字节)，需要进行转换为自己需要的形式，例如使用 Redis 自带的 decode() 方法，将数据转换为str。<br>

#### 使用 set 将字符串存入 Redis：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

data = "Hello, world!"

# 使用set命令将字符串存储
r.set("my_str", data)
```

#### 使用 get 从 Redis 取出 字符串 数据：
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


### 数字存入 Redis 与提取：
#### 整数：
注意：在Redis中，set命令只能存储字符串值。即使你尝试将数字、列表、字典等非字符串类型的数据存储为值，Redis也会将其视为字符串进行存储，其实是字节形式。<br>
```python
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

#### 浮点数：
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

### List 存入 Redis 与取出：
Redis 提供的将 List 数据存入 Redis 的方法有2种:<br>
使用 `lpush(key, value1, value2, ...)` 方法将一个或多个值从左侧插入到列表中，创建一个列表。<br>
使用 `rpush(key, value1, value2, ...)` 方法将一个或多个值从右侧插入到列表中，创建一个列表。<br>
#### 使用 lpush/rpush 将list存入Redis：
下面演示如何使用 `lpush` 存入 Redis 与取出数据，`rpush` 操作类似，举一反三即可：<br>
```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
key = 'my_list'
values = ['apple', 1, 'orange']
r.lpush(key, *values)

# 或者可以使用 rpush 方法
# r.rpush(key, *values)
```
🔆🔆🔆从左侧插入可能不符合大部分人的习惯，改为 `rpush` 即可。

当你的 `values=[]` 使用上述代码会出错，需要改为以下形式：<br>
```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
key = 'my_list'
values = ['apple', 1, 'orange']
for i in values:
    r.lpush(key, i)

# 或者可以使用 rpush 方法
# r.rpush(key, *values)
```
#### 使用 lrange 依靠索引将list从Redis取出：
```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
key = 'my_list'
# 按索引取出所需内容，lrange方法的索引是必填项
res = r.lrange(key,0,-1)        
print(type(res))                # <class 'list'>
print(res)                      # [b'orange', b'1', b'apple']

# 复原list
restored_list = [x.decode() for x in res]
print(type(restored_list))      # <class 'list'>
print(restored_list)            # ['orange', '1', 'apple']
```
🔆🔆🔆从取出的结果我们可以看出，元素确实是按照左侧插入的方式构建的列表。另外：解码要注意转换为自己需要的格式，Redis统一按照字节的方式存储。


### dict存入 Redis 与取出：
Redis 使用 `hmset` 存储含多个键值对的字典，‼️‼️注意 `hmset` 只能存储标准的字典，即 `key` 和 `value` 都是字符串的字典‼️‼️。如果是字典嵌套字典，或字典嵌套列表等结构，无法使用 `hmset` 方法存储，需要使用 `pickle` 或 `json`。
#### 使用 hmset 将 dict 存入 Redis：
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

#### 使用 hgetall 从 Redis 取出 dict 数据：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 获取存储在哈希中的全部键值对
result = r.hgetall("my_dict")       
print(result)                           # {b'key1': b'value1', b'key2': b'value2', b'key3': b'value3'}
print('直接从 Redis 获取的数据：')
print(result[b'key1'])                  # b'value1'，不加b会报错；
print(type(result[b'key1']))            # <class 'bytes'>
print()

"""
想要恢复为原来的数据模样，需要加入 decode() 方法。
"""

# 恢复数据
restore_data = {}
for key, value in result.items():
    restore_data[key.decode()] = value.decode()

print('恢复后的数据：')
print(restore_data)                     # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(restore_data['key1'])             # value1
print(type(restore_data['key1']))       # <class 'str'>
```

### dict存入 Redis 与取出--pickle：
在Python中，pickle.dumps()函数用于将对象**序列化**为字节流（即将对象转换为可传输或存储的格式），而pickle.loads()函数用于将序列化的字节流**反序列化**为原始对象。<br>

pickle适用于将各种内容存入 Redis，但需要考虑序列化和反序列化消耗的时间。json 方法的序列化与反序列化操作与 pickle 相同，将下列代码中的 pickle 替换为 json 即可。<br>

🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀<br>
`pickle` 适用于各种数据结构，包括类套字典、类套类、类套类套类、字典、列表、字符串。但数据结构越复杂，序列化与反序列化的时间开销越大。<br>

一般来说，`pickle` 适用的数据类型最多，`json` 次之，Redis 自带的方法只能处理特定结构。<br>

**时间消耗：** 以字典的存储与提取为例，小数据量三种方法的时间开销差别不大，数据量极大时，`(hmset/hgetall+decode)`消耗的时间最少，`json`次之，`pickle`最长。<br>
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀<br>

#### 使用 pickle.dumps 配合 set 将 dict 存入 Redis：
```python
import redis
import pickle

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

data = {"key1": "value1",
        "key2": "value2",
        "key3": "value3"}

# 将data序列化为字节流(bytes)
data = pickle.dumps(data)
# 使用set命令将data存入redis
r.set("my_dict", data)
```

#### 使用 pickle.loads 配合 get 从 Redis 取出 dict 数据：
```python
import redis
import pickle

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 获取存储在哈希中的全部键值对
result = r.get("my_dict")
result = pickle.loads(result)
print(result)   # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```
🚨使用 `pickle` 一定要注意时间开销！<br>

### class 存入 Redis 与取出：
Redis 无法直接存储 python 的类，需要借助 `pickle` 或 `json` 进行序列化和反序列化才能存储和提取数据。<br>

#### 使用 pickle.dumps 配合 set 将 class 存入 Redis：
```python
import redis
import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 将对象存入Redis
my_object = MyClass(42)
my_object_bytes = pickle.dumps(my_object)
r.set('my_object', my_object_bytes)
```

#### 使用 pickle.loads 配合 get 将 class 从 Redis 取出：
将 class 从 Redis 取出时必须确保在调用 `r.get('xxx')` 时已经导入了相关类的定义。如果存入的数据很复杂，比如 `类套类套类`，需要将对应类的定义都导入。可以采用在文件中写入类的完整定义，也可以采用 `from xxx import classA, classB, classC` 的形式。【可参考 classOfclass 文件中的内容】<br>
```python
import redis
import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

# 创建Redis客户端连接
r = redis.Redis(host='localhost', port=6379)

# 从Redis中提取对象
my_object_bytes = r.get('my_object')
my_object = pickle.loads(my_object_bytes)

# 打印提取到的对象的值
print(my_object.value)  # 42
```
🚨使用 `pickle` 存储的数据越复杂，耗时越多，解析时花费的时间也越多！<br>

如果你对 `pickle` 参与其中的作用还不是很了解，可以试着运行下面的代码：<br>
```python
import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

# 序列化后的数据，其实是 MyClass(42)。
serialized_data = b"\x80\x04\x95)\x00\x00\x00\x00\x00\x00\x00\x8c\b__main__\x94\x8c\aMyClass\x94\x93\x94)\x81\x94}\x94\x8c\x05value\x94K*sb."

my_object = pickle.loads(serialized_data)       
print(type(my_object))                          # # <class '__main__.MyClass'>
print(my_object)                                # <__main__.MyClass object at 0x7f4973e73c10>
print(my_object.value)                          # 42
```

## Redis--大量键值对获取：
当数据量特别大时，多次使用 `get` 方法与 Redis 连接、获取值的时间开销就会显得很高，此时使用 `mget` 和 `pipeline` 方法是一种更优的选择，两者都可以用于一次获取多个键的值。<br>
### 场景描述：
我Redis中的键名与下面的写法类似，但数据量很大。我是否能一次从redis中取100条，这100条组成一个list。<br>
financial_list_0<br>
financial_list_1<br>
financial_list_2<br>
financial_list_3<br>
financial_list_4<br>
financial_list_5<br>
financial_list_6<br>
### mget 方法：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 生成键名列表
keys = ['financial_list_'+str(i) for i in range(100)]

# 一次性获取多个键的值
values = r.mget(keys)

# 将获取的值组成一个list
result = list(values)
```

### pipeline 方法：
```python
import redis

# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

# 构建 pipeline 方法
pipeline = r.pipeline()

# 将需要获取的内容存储到 pipeline 中
for i in range(100):
    pipeline.get('financial_list_'+str(i))

# 执行 pipeline，一次性获取所有内容
results = pipeline.execute()
```
单个结果可采用 `results[0]`、`results[1]`、`results[2]` 的方式获取，数据的顺序与存入 `pipeline` 中的顺序相同。数据如果需要转换，按照自己的数据格式转换即可。<br>

### mget 与 pipeline 的选择：
在 Redis 中，`mget` 和 `pipeline` 方法都可以用于一次获取多个键的值。<br>

`mget` 适用于少量键的情况，`pipeline` 方法适用于大量键的情况。<br>

通常，在少量键的情况下，两种方法的性能差异可能不明显。当需要获取大量键的值时，使用 `pipeline` 方法会比使用 `mget` 方法更快。<br>

需要注意的是，使用 `pipeline` 方法虽然可以提高性能，但是它的实际效果取决于你的具体使用情况，包括网络延迟、数据量大小以及Redis服务器的性能等因素。因此，在选择使用哪种方法时，建议根据具体情况进行测试和评估。<br>

## 文件介绍：
**chunk_data_of_the_class_in_list_to_redis:** 将python类组成的列表按照chunk分段存入Redis，再从Redis中取出还原列表。<br>

**classOfclass:** 展示 `类嵌套类嵌套类` 型数据的存储。<br>

**dictOfdict:** 利用 `pickle` 分段存储字典嵌套字典结构。<br>

**empty_redis.py:** 清空Redis中的数据，慎重操作！<br>

**if_conditions_to_redis.py:**<br>
应用场景：将满足不同 `if` 条件的值按照顺序存入 redis。<br>
代码含义：将20以内满足不同 `if` 条件的值按照顺序存入 redis。<br>




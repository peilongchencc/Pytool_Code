# Redis
Redis是一个开源的高性能键值对存储数据库，它主要用于缓存、消息队列、实时分析、排行榜和会话管理等场景。<br>

Redis具有快速、可靠、灵活、可扩展的特点，支持多种数据结构（字符串、哈希、列表、集合、有序集合等）。<br>

将 python 与 Redis 结合可实现数据的快速加载(〽️**因为数据就在缓存中**〽️)，避免重复读取，从而提升项目的整体运行速度。<br>

本文分两部分，前半部分介绍 Redis 基础使用，后半部分介绍当前目录下各文件及文件夹作用。<br>
- [Redis](#redis)
  - [Ubuntu 18.04 安装 Redis 步骤：](#ubuntu-1804-安装-redis-步骤)
  - [终端Redis常用指令：](#终端redis常用指令)
    - [开启/关闭 Redis 服务:](#开启关闭-redis-服务)
    - [查看 Redis 版本：](#查看-redis-版本)
      - [终端查看：](#终端查看)
      - [进入 Redis 数据库内部查看：](#进入-redis-数据库内部查看)
    - [查看存入 Redis 中的数据：](#查看存入-redis-中的数据)
    - [清空 Redis 中的数据：](#清空-redis-中的数据)
  - [Redis 在 python 的应用：](#redis-在-python-的应用)
    - [python 安装 Redis 库：](#python-安装-redis-库)
    - [测试 Redis 连接：](#测试-redis-连接)
    - [使用python代码清空 Redis 中的数据：](#使用python代码清空-redis-中的数据)
    - [字符串存入 Redis 与提取：](#字符串存入-redis-与提取)
      - [使用 set 将字符串存入 Redis：](#使用-set-将字符串存入-redis)
      - [redis设置过期时间：](#redis设置过期时间)
      - [使用 get 从 Redis 取出 字符串 数据：](#使用-get-从-redis-取出-字符串-数据)
    - [Redis设置默认返回值：](#redis设置默认返回值)
    - [Redis 中 decode 函数解释：](#redis-中-decode-函数解释)
    - [数字存入 Redis 与提取：](#数字存入-redis-与提取)
      - [整数：](#整数)
      - [浮点数：](#浮点数)
    - [List 存入 Redis 与取出：](#list-存入-redis-与取出)
      - [使用 lpush/rpush 将list存入Redis：](#使用-lpushrpush-将list存入redis)
      - [使用 lrange 依靠索引将list从Redis取出：](#使用-lrange-依靠索引将list从redis取出)
    - [dict存入 Redis 与取出：](#dict存入-redis-与取出)
      - [使用 hmset 将 dict 存入 Redis：](#使用-hmset-将-dict-存入-redis)
      - [使用 hgetall 从 Redis 取出 dict 数据：](#使用-hgetall-从-redis-取出-dict-数据)
    - [dict存入 Redis 与取出--pickle：](#dict存入-redis-与取出--pickle)
      - [使用 pickle.dumps 配合 set 将 dict 存入 Redis：](#使用-pickledumps-配合-set-将-dict-存入-redis)
      - [使用 pickle.loads 配合 get 从 Redis 取出 dict 数据：](#使用-pickleloads-配合-get-从-redis-取出-dict-数据)
    - [class 存入 Redis 与取出：](#class-存入-redis-与取出)
      - [使用 pickle.dumps 配合 set 将 class 存入 Redis：](#使用-pickledumps-配合-set-将-class-存入-redis)
      - [使用 pickle.loads 配合 get 将 class 从 Redis 取出：](#使用-pickleloads-配合-get-将-class-从-redis-取出)
  - [Redis--大量键值对获取：](#redis--大量键值对获取)
    - [场景描述：](#场景描述)
    - [mget 方法：](#mget-方法)
    - [pipeline 方法：](#pipeline-方法)
    - [pipeline完整示例：](#pipeline完整示例)
    - [mget 与 pipeline 的选择：](#mget-与-pipeline-的选择)
    - [Redis的pipeline设置默认返回值：](#redis的pipeline设置默认返回值)
  - [Redis连接池的使用：](#redis连接池的使用)
    - [Redis连接池示例：](#redis连接池示例)
    - [特别声明：](#特别声明)
    - [整体结构：](#整体结构)
    - [Redis连接池使用pipeline:](#redis连接池使用pipeline)
  - [文件介绍：](#文件介绍)

## Ubuntu 18.04 安装 Redis 步骤：

1. 更新软件包列表：

```bash
sudo apt update
```

2. 安装Redis服务器：

```bash
sudo apt install redis-server
```

安装完成后，Redis服务器将自动启动，此时终端即可使用 redis-cli 指令。（ Redis 的安装真的很简单🤭）<br>
<br>

## 终端Redis常用指令：

### 开启/关闭 Redis 服务:

如果你想要启动Redis数据库，请使用下列指令：<br>

```bash
redis-server
```

如果你想要关闭Redis数据库，请使用下列指令：<br>

```bash
redis-cli shutdown
```

⚠️注意：因Redis数据为缓存型数据，重新启动Redis数据库会导致Redis中的数据清空。<br>

### 查看 Redis 版本：

可通过下列2种方法中的任何一种方法查看 Redis 版本：<br>

#### 终端查看：

终端输入下列指令即可查看到 Redis 版本信息：<br>

```bash
redis-server --version
```

注意⚠️：Ubuntu 18.04 只提供Redis 4.0.9版本的安装。<br>
<br>

#### 进入 Redis 数据库内部查看：

1. 打开终端并输入以下指令:

```bash
redis-cli
```

此时会显示 `127.0.0.1:6379>` ，这表示你已经进入了 Redis 数据库。<br>

2. 账号验证：

如果你的Redis没有设置密码，可以跳过这一节内容。😀😀😀<br>

如果你的Redis设置了密码，输入Redis指令会遇到下列提示：<br>

```log
(error) NOAUTH Authentication required.
```

仿照下列指令进行权限验证即可，假设你Redis的密码为`Flameaway3.`，在 `127.0.0.1:6379>` 后输入：<br>

```bash
AUTH Flameaway3.
```

3. 在 `127.0.0.1:6379>` 后输入： 

```bash
INFO SERVER
```

显示的内容为 Redis 服务器的信息，包括版本号。<br>
<br>

退出Redis命令行界面的操作很多，包括输入 `exit`、`quit` 或按 `Ctrl+c`。<br>
<br>

### 查看存入 Redis 中的数据：

注意⚠️：如果数据是以 byte(字节) 存入的 Redis，使用GET指令无法看到真实数据；<br>

```bash
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
redis_conn = redis.Redis(host='localhost', port=6379)
```

### 使用python代码清空 Redis 中的数据：
```python
import redis

# 连接到Redis
redis_conn = redis.Redis(host='localhost', port=6379)
# 清空redis
redis_conn.flushall()
```

### 字符串存入 Redis 与提取：
注意⚠️⚠️⚠️：从Redis获取到的数据类型均为 byte(字节)，需要进行转换为自己需要的形式，例如使用 Redis 自带的 decode() 方法，将数据转换为str。<br>

#### 使用 set 将字符串存入 Redis：
```python
import redis

# 连接到Redis
redis_conn = redis.Redis(host='localhost', port=6379)

data = "Hello, world!"

# 使用set命令将字符串存储
redis_conn.set("my_str", data)
```

#### redis设置过期时间：
redis通过`expire`设置过期时间，该参数以秒为单位：<br>

```python
import redis

# 连接到Redis
redis_conn = redis.Redis(host='localhost', port=6379)

data = "Hello, world!"

# 使用set命令将字符串存储
redis_conn.set("my_str", data)
redis_conn.expire("my_str", 7*24*60*60)    # 设置存储时间为7天；
```

#### 使用 get 从 Redis 取出 字符串 数据：

```python
import redis

# 连接到Redis
redis_conn = redis.Redis(host='localhost', port=6379)

# 获取存储在Redis中的字符串
result = redis_conn.get("my_str")                        # b'Hello, world!'
decoded_result = result.decode()                # 等同于 result.decode("utf-8")；
print(decoded_result)                           # Hello, world!
```

### Redis设置默认返回值：

当使用 `get` 从redis获取数据时，如果你的数据过期🥶🥶🥶，或者你查询的 `key` 输入错误🙈🙈🙈，此时会返回 `None`，有可能对后续代码产生影响，所以当从redis获取内容时，设置一个默认值是非常有必要的一件事。<br>

```python
import redis

# 创建一个Redis连接
redis_conn = redis.Redis(host='localhost', port=6379, db=0)
# 清空redis
# redis_conn.flushall()

# 指定键名
key = 'my_key'

# 尝试从Redis中获取数据，如果不存在则返回默认值
data = redis_conn.get(key) or 'default_value'

print(data)
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
redis_conn = redis.Redis(host='localhost', port=6379)
# 存入Redis
redis_conn.set("number",123)

# 从Redis取出数据
res = int(redis_conn.get("number"))
print(res)          # 123
print(type(res))    # <class 'int'>
```
从Redis取出数据要注意数据类型的转化，以上述代码举例，`redis_conn.get("number")` 获取的结果为：`b'123'`，类型为：`<class 'bytes'>`。<br>

#### 浮点数：
```python
import pickle
import redis

# 连接到Redis
redis_conn = redis.Redis(host='localhost', port=6379)
# 存入Redis
redis_conn.set("number",123.4)

# 从Redis取出数据
res = float(redis_conn.get("number"))
print(res)          # 123.4
print(type(res))    # <class 'float'>
```
与从Redis取出整数相同，要注意数据类型的转化，以上述代码举例，`redis_conn.get("number")` 获取的结果为：`b'123.4'`，类型为：`<class 'bytes'>`。<br>

### List 存入 Redis 与取出：
Redis 提供的将 List 数据存入 Redis 的方法有2种:<br>
使用 `lpush(key, value1, value2, ...)` 方法将一个或多个值从左侧插入到列表中，创建一个列表。<br>
使用 `rpush(key, value1, value2, ...)` 方法将一个或多个值从右侧插入到列表中，创建一个列表。<br>
#### 使用 lpush/rpush 将list存入Redis：
下面演示如何使用 `lpush` 存入 Redis 与取出数据，`rpush` 操作类似，举一反三即可：<br>
```python
import redis

redis_conn = redis.Redis(host='localhost', port=6379, db=0)
key = 'my_list'
values = ['apple', 1, 'orange']
redis_conn.lpush(key, *values)

# 或者可以使用 rpush 方法
# redis_conn.rpush(key, *values)
```
🔆🔆🔆从左侧插入可能不符合大部分人的习惯，改为 `rpush` 即可。

当你的 `values=[]` 使用上述代码会出错，需要改为以下形式：<br>
```python
import redis

redis_conn = redis.Redis(host='localhost', port=6379, db=0)
key = 'my_list'
values = ['apple', 1, 'orange']
for i in values:
    redis_conn.lpush(key, i)

# 或者可以使用 rpush 方法
# redis_conn.rpush(key, *values)
```
#### 使用 lrange 依靠索引将list从Redis取出：
```python
import redis

redis_conn = redis.Redis(host='localhost', port=6379, db=0)
key = 'my_list'
# 按索引取出所需内容，lrange方法的索引是必填项
res = redis_conn.lrange(key,0,-1)        
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
redis_conn = redis.Redis(host='localhost', port=6379)

data = {"key1": "value1",
        "key2": "value2",
        "key3": "value3"}

# 使用hmset命令将字典存储为一个哈希
redis_conn.hmset("my_dict", data)
```

#### 使用 hgetall 从 Redis 取出 dict 数据：
```python
import redis

# 连接到Redis
redis_conn = redis.Redis(host='localhost', port=6379)

# 获取存储在哈希中的全部键值对
result = redis_conn.hgetall("my_dict")       
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
redis_conn = redis.Redis(host='localhost', port=6379)

data = {"key1": "value1",
        "key2": "value2",
        "key3": "value3"}

# 将data序列化为字节流(bytes)
data = pickle.dumps(data)
# 使用set命令将data存入redis
redis_conn.set("my_dict", data)
```

#### 使用 pickle.loads 配合 get 从 Redis 取出 dict 数据：
```python
import redis
import pickle

# 连接到Redis
redis_conn = redis.Redis(host='localhost', port=6379)

# 获取存储在哈希中的全部键值对
result = redis_conn.get("my_dict")
result = pickle.loads(result)
print(result)   # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```
🚨使用 `pickle` 一定要注意时间开销！<br>

### class 存入 Redis 与取出：
Redis 无法直接存储 python 的类，需要借助 `pickle` 或 `json` 进行序列化和反序列化才能存储和提取数据。<br>
‼️‼️‼️‼️注意，python 类对象无法截断存入 Redis，即使强行将 `pickle.dumps()` 后的字节流截断存入 Redis，从 Redis 将截断的字节流取出后，也无法复原数据。<br>

#### 使用 pickle.dumps 配合 set 将 class 存入 Redis：
```python
import redis
import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

# 连接到Redis
redis_conn = redis.Redis(host='localhost', port=6379)

# 将对象存入Redis
my_object = MyClass(42)
my_object_bytes = pickle.dumps(my_object)
redis_conn.set('my_object', my_object_bytes)
```

#### 使用 pickle.loads 配合 get 将 class 从 Redis 取出：
将 class 从 Redis 取出时必须确保在调用 `redis_conn.get('xxx')` 时已经导入了相关类的定义。如果存入的数据很复杂，比如 `类套类套类`，需要将对应类的定义都导入。可以采用在文件中写入类的完整定义，也可以采用 `from xxx import classA, classB, classC` 的形式。【可参考 classOfclass 文件中的内容】<br>
```python
import redis
import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

# 创建Redis客户端连接
redis_conn = redis.Redis(host='localhost', port=6379)

# 从Redis中提取对象
my_object_bytes = redis_conn.get('my_object')
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
redis_conn = redis.Redis(host='localhost', port=6379)

# 生成键名列表
keys = ['financial_list_'+str(i) for i in range(100)]

# 一次性获取多个键的值
values = redis_conn.mget(keys)

# 将获取的值组成一个list
result = list(values)
```

### pipeline 方法：
```python
import redis

# 连接到Redis
redis_conn = redis.Redis(host='localhost', port=6379)

# 构建 pipeline 方法
pipeline = redis_conn.pipeline()

# 将需要获取的内容存储到 pipeline 中
for i in range(100):
    pipeline.get('financial_list_'+str(i))

# 执行 pipeline，一次性获取所有内容
results = pipeline.execute()
```
单个结果可采用 `results[0]`、`results[1]`、`results[2]` 的方式获取，数据的顺序与存入 `pipeline` 中的顺序相同。数据如果需要转换，按照自己的数据格式转换即可。<br>

### pipeline完整示例：
数据写入：<br>
```python
import redis

# 建立到Redis服务器的连接
redis_conn = redis.Redis(host='localhost', port=6379, db=0)

# 创建一个Pipeline对象
pipeline = redis_conn.pipeline()

# 在Pipeline中添加多个SET命令
pipeline.set('key1', 'value1')
pipeline.set('key2', 'value2')
pipeline.set('key3', 'value3')

# 执行Pipeline中的所有命令
pipeline.execute()
```
数据获取：<br>
```python
import redis

# 建立到Redis服务器的连接
redis_conn = redis.Redis(host='localhost', port=6379, db=0)

# 创建一个Pipeline对象
pipeline = redis_conn.pipeline()

# 在Pipeline中添加多个SET命令
pipeline.get('key1')
pipeline.get('key2')
pipeline.get('key3')

# 执行Pipeline中的所有命令
result = pipeline.execute()
for i in result:
    print(i.decode())
```
终端效果：<br>
```log
value1
value2
value3
```

### mget 与 pipeline 的选择：
在 Redis 中，`mget` 和 `pipeline` 方法都可以用于一次获取多个键的值。<br>

`mget` 适用于少量键的情况，`pipeline` 方法适用于大量键的情况。<br>

通常，在少量键的情况下，两种方法的性能差异可能不明显。当需要获取大量键的值时，使用 `pipeline` 方法会比使用 `mget` 方法更快。<br>

需要注意的是，使用 `pipeline` 方法虽然可以提高性能，但是它的实际效果取决于你的具体使用情况，包括网络延迟、数据量大小以及Redis服务器的性能等因素。因此，在选择使用哪种方法时，建议根据具体情况进行测试和评估。<br>
<br>

### Redis的pipeline设置默认返回值：
与单个`get`获取数据时的默认值设置不同，在使用 Redis Pipeline 执行多个命令时，要设置默认值并获取多个键的数据，需要在执行命令后对 `result` 列表进行处理。<br>

以下是如何设置默认值并获取多个键的数据的代码示例：<br>

```python
import redis

# 建立到 Redis 服务器的连接
redis_conn = redis.Redis(host='localhost', port=6379, db=0)

# 创建一个 Pipeline 对象
pipe = redis_conn.pipeline()

# 在 Pipeline 中添加多个 GET 命令
pipe.get('key1')
pipe.get('key2')
pipe.get('key3')

# 执行 Pipeline 中的所有命令
result = pipe.execute()

# 处理结果并设置默认值
default_value = 'default_value'
data = []

for value in result:
    if value is None:
        data.append(default_value)
    else:
        data.append(value)

# data 列表包含了获取的数据或默认值
print(data)
```
<br>

## Redis连接池的使用：
使用连接池的方式相较于在每个需要Redis连接的地方直接创建连接（如使用`redis.Redis(host='localhost', port=6379)`）有几个主要好处：<br>

**资源重用和管理**：连接池会管理连接的创建、重用和释放，确保连接得到充分重用，而不是频繁地创建和断开连接。这有助于降低资源消耗和提高性能，尤其在高并发环境下。<br>

**性能优化**：连接池可以显著提高应用程序的性能，因为它减少了每次操作的连接建立和断开开销。连接池内的连接可以被多次复用，从而减少了网络通信的开销。<br>

**并发处理**：连接池是线程安全的，这意味着多个线程可以安全地共享同一个连接池，而不会引发竞态条件或其他并发问题。这是多线程或多进程应用程序中使用连接池的一个重要优势。<br>

**可维护性和可扩展性**：将连接池的配置封装在一个独立的模块中（如`redis_utils.py`），可以提高代码的可维护性。如果以后需要更改连接配置，你只需修改一个地方，而不是在整个代码库中查找和修改所有连接的地方。<br>

总的来说，连接池提供了一种更加灵活、高效和可维护的方式来处理与Redis的连接。它是在生产环境中使用Redis的推荐做法之一，可以帮助你更好地管理和优化与Redis的通信。<br>

### Redis连接池示例：
Redis连接池通常用于项目中多个文件需要从redis获取数据的情况，以下是一个示例，展示如何在多个文件中使用Redis：<br>

假设你的项目结构如下：<br>

```
project/
    └── config/
        ├── redis_config.py
    └── utils/
        ├── redis_utils.py
    └── main.py
```

`redis_config.py` 文件包含Redis连接配置：<br>

```python
# config/redis_config.py

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
```

`redis_utils.py` 文件包含与Redis操作相关的工具函数，并使用连接池：<br>

```python
# utils/redis_utils.py

import redis
from project.config.redis_config import REDIS_HOST, REDIS_PORT, REDIS_DB

# 创建Redis连接池
pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

# 获取Redis连接
def get_redis_connection():
    return redis.Redis(connection_pool=pool)

# 从Redis中获取数据的示例函数
def get_data_from_redis(key):
    redis_conn = get_redis_connection()
    data = redis_conn.get(key)
    return data
```

在 `main.py` 文件中使用上述工具函数：<br>

```python
# main.py

from project.utils.redis_utils import get_data_from_redis

def main():
    key = 'your_key'
    data = get_data_from_redis(key)
    if data:
        print(f'Data from Redis: {data.decode("utf-8")}')
    else:
        print('Data not found in Redis.')

if __name__ == '__main__':
    main()
```

这样，你可以在多个文件中使用相同的连接池来处理Redis操作，而不必在每个文件中单独创建连接。此外，你可以在其他文件中导入 `redis_utils.py` 中的工具函数来执行Redis操作。这种方式可以提高代码的可维护性和重用性。<br>

### 特别声明：
使用连接池的方式，每次调用 `get_redis_connection()` 函数时，都会获取一个从连接池中分配的连接。🤭🤭🤭这并不会导致每次都创建一个新的连接，而是会重复使用已经建立的连接，从而减少连接和断开连接的开销。‼️‼️‼️‼️<br>

所以，每次调用 `get_redis_connection()` 函数都会返回一个已经存在的连接，而不是创建一个新的连接。<br>

这样，你可以在多个文件和函数中重复使用相同的连接池，从而降低了与Redis的连接开销。连接池会管理连接的生命周期，包括连接的创建、释放和重用。这有助于提高你的应用程序的性能和效率。<br>

### 整体结构：
如果你想在一个文件中测试Redis连接池效果，可以直接使用下列代码：<br>
> 注意将代码中的 `key = 'your_key'` 修改为自己存入redis中的key。

```python
import redis

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = '' # 这里为空，笔者没有设置密码

# 创建Redis连接池
pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)

# 获取Redis连接
def get_redis_connection():
    return redis.Redis(connection_pool=pool)

# 从Redis中获取数据的示例函数
def get_data_from_redis(key):
    redis_conn = get_redis_connection()
    data = redis_conn.get(key)
    return data

def main():
    key = 'your_key'
    data = get_data_from_redis(key)
    if data:
        print(f'Data from Redis: {data.decode("utf-8")}')
    else:
        print('Data not found in Redis.')

if __name__ == '__main__':
    main()
```

### Redis连接池使用pipeline:
使用连接池的方式也支持Redis的pipeline操作，在使用连接池的情况下，你可以像以下代码这样使用Redis的pipeline：<br>

```python
import redis
from project.utils.redis_utils import get_redis_connection

# 获取Redis连接
redis_conn = get_redis_connection()

# 创建pipeline对象
pipeline = redis_conn.pipeline()

# 向pipeline中添加多个命令
pipeline.set('key1', 'value1')
pipeline.set('key2', 'value2')

# 执行pipeline中的命令
results = pipeline.execute()

# 打印结果
for result in results:
    print(result)
```

上述示例中，我们首先从连接池中获取一个Redis连接，然后创建了一个pipeline对象，将多个命令添加到pipeline中，最后通过`pipeline.execute()`一次性发送并执行这些命令。这样，你可以充分利用Redis的pipeline功能，减少了多次网络通信的开销。<br>

使用连接池的方式并不影响Redis的pipeline操作，你可以在代码中方便地组织和执行pipeline中的多个命令。这有助于提高与Redis的通信效率。<br>

## 文件介绍：
**chunk_data_of_the_class_in_list_to_redis:** 将python类组成的列表按照chunk分段存入Redis，再从Redis中取出还原列表。<br>

**classOfclass:** 展示 `类嵌套类嵌套类` 型数据的存储。<br>

**dictOfdict:** 利用 `pickle` 分段存储字典嵌套字典结构。<br>

**empty_redis.py:** 清空Redis中的数据，慎重操作！<br>

**if_conditions_to_redis.py:**<br>
应用场景：将满足不同 `if` 条件的值按照顺序存入 redis。<br>
代码含义：将20以内满足不同 `if` 条件的值按照顺序存入 redis。<br>




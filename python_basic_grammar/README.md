# Python Basci Grammar
介绍 python 基本语法、常见函数的使用与笔者常用的感觉非常方便的python库。python 类由于其复杂性，单独创建一个文件夹讲解。<br>

## pip 查看某个库的版本：
假设你要查询 `pandas` 库的详细信息：<br>
```shell
pip show pandas
```
如果你已经安装了这个库，将显示类似下面的信息：<br>
```txt
(nudge_new) root@iZ2zea5v77oawjy2qz7c20Z:/data/Pytool_Code# pip show pandas
Name: pandas
Version: 1.5.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: The Pandas Development Team
Author-email: pandas-dev@python.org
License: BSD-3-Clause
Location: /root/anaconda3/envs/nudge_new/lib/python3.10/site-packages
Requires: numpy, python-dateutil, pytz
Required-by: 
```
了解相信的信息有时很有用，例如可以根据 `Home-page` 的链接访问原网页，查询该库的更多细节。尤其是对于用户较少的某些库，例如 `snowflake-id`。


## 字典(dict):
python中字典支持以数字作为键，但不推荐这种写法，毕竟我们也代码要考虑可读性，单纯的数字作为 `key` 自己或同时并不能看出代码的含义。<br>
```python
dictionary = {1: "financial", 2: "sale", 3: "insurance"}    # python中字典支持以数字作为键；
print(dictionary)
print(dictionary[1])    # 调用的时候也以数字的方式调用，如果写为 print(dictionary['1']) 会报错。
print(dictionary[2])
```

### 查看字典中是否有某个key及该key对应的值：
如果不确定字典中是否有某个key，需要用 `get()` 函数进行判断，不能用 `if item["key_name"]:` 的方式判断，如果字典中没有 `"key_name"` 这个键，使用 `if item["key_name"]:` 运行代码会报错。<br>
```python
data = [{"name":"Tom(汤姆)","score":"640(720)"}, {"name":"Spike(斯派克)"},{"name":"Jerry(杰瑞)","score":"700(720)"}]

for item in data:
    if item.get("score"):
        name = item["name"]
        score = item["score"]
        print(f"{name}的考试成绩为:{score}")    # f-string 不支持 f"...{item["name"]}..." 写法。
    else:
        name = item["name"]
        print(f"没有查询到{name}的考试成绩，TA可能缺考了。")
```

## import 导入时文件顺序解析：
项目有入口文件和工具文件之分，我们经常从入口文件引入工具文件中的部分内容，很多人很迷惑import导入文件的流程，这里借助 `jieba` 和 `python类` 梳理一下 `import` 时代码读取流程。<br>
假设我们现在有两个文件 入口文件`main.py` 和 工具文件`tools.py`，具体内容如下：<br>
```python
# tools.py
import time
import jieba
print('This is the start of tools.py')

current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class Segment:
    # 模拟根据用户的登录id、user_name、text，返回附加时间的分词结果。
    def __init__(self,id,name) -> None:
        self.id = id
        self.name = name
        self.date = current_time
    
    def split_words(self,text):
        result = jieba.lcut(text)
        return f'{self.date}：用户{self.id}，{self.name}先生/女士您好，您的分词结果是：{result}'

print('This is the end of tools.py')
```

```python
# main.py
from tools import Segment
text = '长江市市长江大桥。'

# 模拟用户登录
personal_information = Segment('007','peilongchencc')
# 模拟获取到用户输入文本
res = personal_information.split_words(text)    # 执行分词方法
print(res)
```

输出：<br>
```txt
This is the start of tools.py
This is the end of tools.py
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 0.706 seconds.
Prefix dict has been built successfully.
2023-07-28 17:01:32：用户007，peilongchencc先生/女士您好，您的分词结果是：['长江', '市市', '长江大桥', '。']
```
从输出可以看出，`from tools import Segment` 会将导入文件的所有内容都执行一遍，`函数、类`是因为没有调用所以没有执行。当运行到 `personal_information.split_words(text)` 才真正执行了类 `Segment` 中的函数。<br>

笔者讲这个的原因是：希望大家不要随意在工具文件中写可执行内容，很容易重复调用，产生无用的开销。尤其是文件中有 python类，不要在定义类的文件中就把类实例化了。可能有部分人觉得这样便于维护，调用方便(只需要`from ... import ...`)，但这会增加共同维护项目仓库人员的负担，会增大内存、CPU开销，因为只要调用这个文件就会自动实例化一次对应的类。除非这个文件中你只写了一个类，或是专门用于各种类实例化的文件，但这种方式显然不可能。所以最好的方式依旧是在该实例化的地方实例化，至于维护问题，采用 `from config import ...` 这种方式维护即可。 ❌❌❌<br>

## open() 函数：
Python 的内建函数 `open()` 函数用于打开文件，常搭配 `read()`, `readline()` 和 `readlines()` 方法来读取文件内容。<br>

`read()`: 一次性读取所有内容为字符串。可通过添加 `size` 参数控制读取的字节，例如 `file.read(100)` 表示读取前100个字节的内容。<br>
`readline()`: 每次调用，读取文件的下一行。通常用于逐行读取大文件，这样可以不必一次性加载整个文件到内存。<br>
`readlines()`: 读取整个文件并返回一个包含文件每一行的列表。虽然这个方法很方便，但如果文件很大，一次性加载所有行到一个列表可能会消耗大量内存。<br>

现在以读取 `test.txt` 文件为例，讲解三种读取方式的不同。`test.txt`文件内容如下：<br>
```txt
黄鹤楼送孟浩然之广陵
    唐·李白
故人西辞黄鹤楼，烟花三月下扬州。
孤帆远影碧空尽，唯见长江天际流。
```
### read():
```python
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
```
`python read_file.py` 运行结果如下，以😲😲😲字符串形式😲😲😲一次性返回所有内容：<br>
```shell
黄鹤楼送孟浩然之广陵
    唐·李白
故人西辞黄鹤楼，烟花三月下扬州。
孤帆远影碧空尽，唯见长江天际流。
```

### readline():
```python
with open("test.txt", "r") as file:
    line = file.readline()
    while line:                     # 当line存在时，读取下一行
        print(line, end='')         # end='' 用来避免重复的换行
        line = file.readline()
```
`line` 第一次调用 `print` 的结果为 "黄鹤楼送孟浩然之广陵"，`line` 第二次调用 `print` 的结果为 "    唐·李白"，每次返回一行内容。<br>

### readlines():
```python
with open("test.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')  # end='' 用来避免重复的换行
```
`lines` 的结果如下：<br>
```shell
['黄鹤楼送孟浩然之广陵\n', '    唐·李白\n', '故人西辞黄鹤楼，烟花三月下扬州。\n', '孤帆远影碧空尽，唯见长江天际流。']
```
所以要进行 `for循环` 遍历，同时控制 `end` 才能复原数据。<br>
<br>

## join() 函数：
在Python中，`join()` 函数是用于将序列中的元素连接为一个字符串的方法。它可以将一个可迭代对象（比如列表、元组、字符串等）中的元素以🌵**指定的分隔符**🌵连接起来，生成一个新的字符串。<br>

☪️**可迭代对象的要求：** 必须每一项都是字符串类型。如果不是，可以借助列表推导式或 `map()` 函数将每一项元素都转为字符串类型，再执行 `json()` 函数。接下来看几个例子：<br>

将列表中每个元素以 `-` 进行连接，拼接为字符串：<br>
```python
information = ['O', 'l', 'd', ':', '1', '8']
# 分隔符
separator = '-'
result = separator.join(information)
print(result)   # O-l-d-:-1-8
```

不要分隔符，将列表中每个元素进行连接，拼接为字符串：<br>
```python
information = ['O', 'l', 'd', ':', '1', '8']
# 分隔符
separator = ''
result = separator.join(information)
print(result)   # Old:18
```

‼️如果列表中某个元素不是字符串，会报错：<br>
```python
information = ['O', 'l', 'd', ':', 1, '8']
# 分隔符
separator = '-'
result = separator.join(information)
print(result)   # TypeError: sequence item 4: expected str instance, int found
```

可采用列表推导式，先将列表中的每一项转为字符串，再执行 `json` 函数：<br>
```python
information = ['O', 'l', 'd', ':', 1, '8']
# 分隔符
separator = '-'
result = separator.join([str(i) for i in information])
print(result)   # O-l-d-:-1-8
```

也可以采用 `map` 函数：<br>
```python
information = ['O', 'l', 'd', ':', 1, '8']
# 分隔符
separator = '-'
result = separator.join(map(str, information))
print(result)   # O-l-d-:-1-8
```

## 常见库解释：
### flask
介绍Python Web应用程序框架Flask的安装和使用。<br>

### nginx:
以Nginx在反向代理方面的应用为切入，介绍Nginx的安装和使用。<br>

### time
time库是Python标准库中的一个模块，它提供了处理时间的功能。time 文件夹下是一些常见的time库的用法。<br>
**Ps1**:文章中的时间如果格式化，统一转化为 2022-01-01 12:05:44 形式，原因为：该时间格式可以直接写入mysql，在实际操作中非常方便。<br>
**Ps2**:文章中使用的都是 `time` 模块中的用法，并没有使用利用 `datetime` 等其他时间模块，这样做的好处是：在项目中使用统一的时间获取方式。<br>
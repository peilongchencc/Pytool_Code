# time
time库是Python标准库中的一个模块，它提供了处理时间的功能。下面是一些常见的time库的用法：<br>

**Ps1**：`time`库的结果以**秒**为单位，请不要记错。🚨🚨🚨<br>
**Ps2**：文章中的时间如果格式化，统一转化为 2022-01-01 12:05:44 形式，原因为：该时间格式可以直接写入mysql，在实际操作中非常方便。<br>
**Ps3**：文章中使用的都是 `time` 模块中的用法，并没有使用利用 `datetime` 等其他时间模块，这样做的好处是：在项目中使用统一的时间获取方式。<br>
- [time](#time)
  - [获取当前时间的时间戳：](#获取当前时间的时间戳)
  - [获取指定时间的时间戳：](#获取指定时间的时间戳)
  - [根据时间戳，将时间格式化：](#根据时间戳将时间格式化)
  - [获取当前时间的年份、月份、日期等信息：](#获取当前时间的年份月份日期等信息)
  - [延时执行程序：](#延时执行程序)
  - [获取程序执行时间：](#获取程序执行时间)
  - [通过装饰器计算程序执行时间：](#通过装饰器计算程序执行时间)
    - [计算函数执行时间：](#计算函数执行时间)
    - [计算类中函数执行时间：](#计算类中函数执行时间)
    - [计算类实例(内置文本处理方法)执行时间：](#计算类实例内置文本处理方法执行时间)

## 获取当前时间的时间戳：
```python
import time

current_time = time.time()  # 返回一个浮点数，表示当前时间距离1970年1月1日00:00:00的秒数。
print(current_time)
```
注意⚠️：time.time() 函数返回的是当前时间的时间戳，无法直接返回指定时间的时间戳。要获取指定时间的时间戳，需要借助其他时间模块来实现。

## 获取指定时间的时间戳：
假设指定的时间为：2022-01-01 12:05:44
```python
import time

date_string = "2022-01-01 12:05:44"
timestamp = time.mktime(time.strptime(date_string, "%Y-%m-%d %H:%M:%S"))

print(timestamp)    # 1641009944.0
```
`time.strptime()` 函数用于将字符串时间转换为 **时间元组** 。时间元组包含了年、月、日、时、分、秒等时间信息。<br>
`'%Y-%m-%d %H:%M:%S'` 指定了字符串时间的格式，与字符串时间的实际格式相匹配。<br>
`time.mktime()` 函数用于将时间元组转换为对应的时间戳。<br>

## 根据时间戳，将时间格式化：
```python
import time

timestamp = 1641009944.0
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print(formatted_time)   # 2022-01-01 12:05:44
```

`time.localtime()` 用于将时间戳转化为 struct_time 的时间元组形式。用法如下：<br>
```python
import time

timestamp = 1641009944.0
res = time.localtime(timestamp)
print(res)
# 输出：
# time.struct_time(tm_year=2022, tm_mon=1, tm_mday=1, tm_hour=12, tm_min=5, tm_sec=44, tm_wday=5, tm_yday=1, tm_isdst=0)
```

如果时间戳通过 `time.time()` 获取，则表示 **根据时间戳，将当前时间格式化：**<br>
```python
import time
timestamp = time.time()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print(formatted_time)   # 2023-08-15 11:29:22
```

也可以使用更简单的形式，当 `time.localtime()` 无参数时，默认获取的就是当前时间的元组形式。<br>
```python
import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 输出格式为：
# 2023-08-15 10:18:14
```

## 获取当前时间的年份、月份、日期等信息：
`time.localtime()` 将时间戳转化为了 struct_time 的时间元组形式，可以通过 `struct_time` 的key获取对应的年份、月份、日期。<br>
```python
import time

current_time = time.localtime()
print(current_time)     
# time.struct_time(tm_year=2023, tm_mon=8, tm_mday=15, tm_hour=11, tm_min=36, tm_sec=29, tm_wday=1, tm_yday=227, tm_isdst=0)

year = current_time.tm_year
month = current_time.tm_mon
day = current_time.tm_mday
print(year, month, day) # 2023 8 15
```

## 延时执行程序：
```python
import time

print("Start")
time.sleep(2)   # 程序延时2秒后再执行下方的print("End")。
print("End")
```

## 获取程序执行时间：
🚨🚨🚨如果你想查看某部分代码的时间，最好单独测试，不要整个项目一起查看。服务器性能、服务器负载不平衡都会影响你的时间。如果你是使用 `postman` 测试远程服务器部署的代码，更可能由于网络延迟导致每次测试的时间不一致。<br>
```python
import time
start_time = time.time() 
"""
这里执行自己的代码 
"""
end_time = time.time() 
execution_time = end_time - start_time 
print(f"执行时间为：{execution_time} 秒")
```

## 通过装饰器计算程序执行时间：
工作中，笔者经常感到一直写 `start_time` 和 `end_time` 计算程序的执行时间很累，尤其是需要计算时间的函数特别多时。所以就有了想以最简单方式实现程序时间计算的想法，于是就有了时间装饰器。你在工作中也可以直接复用下列代码：<br>
> 如果不了解装饰器是什么，可以去我的python_basic_grammer部分查看相关内容。

```python
import time

# 定义timing_decorator装饰器
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()              # 起始时间
        result = func(*args, **kwargs)        # 函数执行，函数有多个返回值依旧可以执行
        end_time = time.time()                # 结束时间
        elapsed_time = end_time - start_time  # 计算耗时
        
        # 根据不同情况获取名称
        # 对于函数来说，使用 `func.__name__` 可以获得函数名称；但对于类的实例，需要使用 `func.__class__.__name__` 来获得实例对应的类的名称。
        func_name = getattr(func, "__name__", None) or func.__class__.__name__
        
        print(f"Function {func_name} took {elapsed_time:.6f} seconds to execute.")
        return result
    return wrapper
```
使用方法很简单，我分别介绍一下计算函数、类方法、类实例(内置文本处理方法)耗时，跨文件导入的使用方式。<br>

### 计算函数执行时间：
与常规装饰器的使用方法相同，通过在需要计算函数的上方添加 `@timing_decorator` 即可～<br>

代码示例：<br>
```python
import time

# 定义timing_decorator装饰器
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()              # 起始时间
        result = func(*args, **kwargs)        # 函数执行，函数有多个返回值依旧可以执行
        end_time = time.time()                # 结束时间
        elapsed_time = end_time - start_time  # 计算耗时
        
        # 根据不同情况获取名称
        # 对于函数来说，使用 `func.__name__` 可以获得函数名称；但对于类的实例，需要使用 `func.__class__.__name__` 来获得实例对应的类的名称。
        func_name = getattr(func, "__name__", None) or func.__class__.__name__
        
        print(f"Function {func_name} took {elapsed_time:.6f} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def fullwidth_to_halfwidth(input_str):
    halfwidth_str = ""
    for char in input_str:
        char_code = ord(char)
        # 处理全角空格
        if char_code == 12288:
            halfwidth_str += " "
        # 处理全角中文字符
        elif 65281 <= char_code <= 65374:
            halfwidth_str += chr(char_code - 65248)
        else:
            halfwidth_str += char
    return halfwidth_str

# 示例用法
input_str = "Ｈｅｌｌｏ，这是一个示例字符串！"
halfwidth_result = fullwidth_to_halfwidth(input_str)
print(halfwidth_result)

# 这个函数会将输入字符串中的全角字符转换为半角字符，包括中文字符。请注意，这个函数只处理了常见的全角字符范围，如果需要支持更多字符范围，可能需要进一步扩展。
```
终端效果：<br>
```log
Function fullwidth_to_halfwidth took 0.000012 seconds to execute.
Hello,这是一个示例字符串!
```

### 计算类中函数执行时间：
计算类中函数执行时间的方式与计算函数执行时间的方式相同～🥴🥴🥴<br>
```python
import jieba
import time

# 定义timing_decorator装饰器
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()              # 起始时间
        result = func(*args, **kwargs)        # 函数执行，函数有多个返回值依旧可以执行
        end_time = time.time()                # 结束时间
        elapsed_time = end_time - start_time  # 计算耗时
        
        # 根据不同情况获取名称
        # 对于函数来说，使用 `func.__name__` 可以获得函数名称；但对于类的实例，需要使用 `func.__class__.__name__` 来获得实例对应的类的名称。
        func_name = getattr(func, "__name__", None) or func.__class__.__name__
        
        print(f"Function {func_name} took {elapsed_time:.6f} seconds to execute.")
        return result
    return wrapper

# 格式化当前时间为 "2023-09-12 15:19:00" 类型
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class Segment:
    # 模拟根据用户的登录id、user_name、text，返回附加时间的分词结果。
    def __init__(self,id,name) -> None:
        self.id = id
        self.name = name
        self.date = current_time
    
    @timing_decorator
    def split_words(self,text):
        result = jieba.lcut(text)
        return f'{self.date}：用户{self.id}，{self.name}先生/女士您好，您的分词结果是：{result}'


text = '长江市市长江大桥。'

# 模拟用户登录
personal_information = Segment('007','peilongchencc')
# 模拟获取到用户输入文本
res = personal_information.split_words(text)    # 执行分词方法
print(res)
```

终端效果：<br>
```log
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 1.248 seconds.
Prefix dict has been built successfully.
Function split_words took 1.248072 seconds to execute.
2023-09-12 15:19:00：用户007，peilongchencc先生/女士您好，您的分词结果是：['长江', '市市', '长江大桥', '。']
```
🚨🚨🚨注意观察终端内容，**分词模型的导入就花费了1.248s**，所以 `split_words` 其实基本没有花费时间。<br>

### 计算类实例(内置文本处理方法)执行时间：
以 `hanlp.pipeline` 为例：<br>
```python
import hanlp
import time

# 定义timing_decorator装饰器
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()              # 起始时间
        result = func(*args, **kwargs)        # 函数执行，函数有多个返回值依旧可以执行
        end_time = time.time()                # 结束时间
        elapsed_time = end_time - start_time  # 计算耗时
        
        # 根据不同情况获取名称
        # 对于函数来说，使用 `func.__name__` 可以获得函数名称；但对于类的实例，需要使用 `func.__class__.__name__` 来获得实例对应的类的名称。
        func_name = getattr(func, "__name__", None) or func.__class__.__name__
        
        print(f"Function {func_name} took {elapsed_time:.6f} seconds to execute.")
        return result
    return wrapper

HanLP = hanlp.pipeline() \
    .append(timing_decorator(hanlp.load('CTB9_TOK_ELECTRA_SMALL')), output_key='tok') \
    .append(timing_decorator(hanlp.load('CTB9_POS_ELECTRA_SMALL')), output_key='pos') \
    .append(timing_decorator(hanlp.load('MSRA_NER_ELECTRA_SMALL_ZH')), output_key='ner', input_key='tok') \
    .append(timing_decorator(hanlp.load('CTB9_DEP_ELECTRA_SMALL', conll=False)), output_key='dep', input_key='tok') \
    .append(timing_decorator(hanlp.load('CTB9_CON_ELECTRA_SMALL')), output_key='con', input_key='tok')

doc = HanLP(['急性肠胃炎要如何治疗？', '盛剑环境的股价太高了。'])
print(doc)
```
终端效果：<br>
```log
Function TransformerTaggingTokenizer took 0.033004 seconds to execute.
Function TransformerTagger took 0.030062 seconds to execute.
Function TransformerNamedEntityRecognizer took 0.035365 seconds to execute.
Function BiaffineDependencyParser took 0.035167 seconds to execute.
Function CRFConstituencyParser took 0.064560 seconds to execute.
```
🚨🚨🚨注意：对于类的实例，`func.__class__.__name__` 获取的是实例对应的类的名称。<br>
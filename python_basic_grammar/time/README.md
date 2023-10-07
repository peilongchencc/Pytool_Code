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
    - [计算python类中函数执行时间：](#计算python类中函数执行时间)
    - [计算类实例(内置文本处理方法)执行时间：](#计算类实例内置文本处理方法执行时间)
    - [跨文件导入：](#跨文件导入)
    - [timing\_decorator与staticmethod联合使用：](#timing_decorator与staticmethod联合使用)
  - [异步函数与时间装饰器：](#异步函数与时间装饰器)
    - [错误示例一：](#错误示例一)
    - [错误示例二：](#错误示例二)
    - [正确示例：](#正确示例)

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

### 计算python类中函数执行时间：
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

### 跨文件导入：
跨文件导入这部分内容其实没什么好讲的🫠🫠🫠完全跟正常的 `import` 语句一样。<br>

假设你在一个文件(例如命名为`execute_time.py`)中定义了 `timing_decorator` ：<br>
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
在其他需要使用此装饰器的文件中，正常使用 `import` 语句导入并应用它即可：<br>
```python
from execute_time import timing_decorator

@timing_decorator
def add(a,b):
    res = a+b
    return res

result = add(3,1)
print(result)
```
终端效果：<br>
```log
Function add took 0.000001 seconds to execute.
4
```

### timing_decorator与staticmethod联合使用：
现在，我们讲一个稍显复杂的情况，如果你想在一个静态方法(`staticmethod`)上使用这个装饰器，你应该怎么做呢？`timing_decorator` 和 `staticmethod` 都是装饰器，能连用吗？<br>

如果你有这个疑问，可以查看下列代码：<br>
```python
class MyClass:
    
    @staticmethod
    @timing_decorator
    def my_static_method(x, y):
        # ... method body ...
```

当有多个装饰器时，一定要注意装饰器的顺序。💦💦💦**首先应用的装饰器是最接近方法定义的那个，然后是其上方的装饰器**🐳🐳🐳。<br>

在这个例子中，首先`timing_decorator`被应用于`my_static_method`，然后`staticmethod`装饰器被应用于已经被`timing_decorator`装饰过的`my_static_method`。<br>

这样，当你调用静态方法时，会首先执行`timing_decorator`中的逻辑，然后执行实际的静态方法，最后输出方法的执行时间。<br>
<br>

## 异步函数与时间装饰器：

前面看了那么多例子，你一定有种在需要的位置都用 `time()` 函数计算耗时的冲动。这是好事，可以让你更好把握程序响应时间，但如果你想计算异步函数的耗时，可能和你想的方式有点不一样。<br>

### 错误示例一：

看了上面的介绍，如果你直接采用类似以下的方式计算异步函数耗时，那就错了：<br>

```python
from sanic import Sanic
from sanic.response import json
import jieba
import time

app = Sanic("SEGMENT-API")

@app.route("/segment", methods=["POST"])
async def segment(request):
    start_time = time.time()  # 记录开始
    text = request.form.get("user_input")
    if not text:
        return json({"Error": "Missing 'user_input' parameter"}, status=400)

    segment_text = jieba.lcut(text)
    end_time = time.time()    # 记录结束时间
    elapsed_time = end_time - start_time  # 计算耗时
    print(f"Function segment took {elapsed_time:.6f} seconds to execute.")
    return json({"程序的分词结果为：": segment_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8848)
```

### 错误示例二：

```python
from sanic import Sanic
from sanic.response import json
import jieba
import time

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

app = Sanic("SEGMENT-API")

@app.route("/segment", methods=["POST"])
@timing_decorator
async def segment(request):
    text = request.form.get("user_input")
    if not text:
        return json({"Error": "Missing 'user_input' parameter"}, status=400)

    segment_text = jieba.lcut(text)
    return json({"程序的分词结果为：": segment_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8848)
```

‼️‼️‼️上面的两种写法都是典型的错误写法，代码中`segment`函数使用`async def`定义，因此是异步函数。<br>

在异步函数内部使用`time.time()`来计算执行时间时，可能会受到事件循环的影响。**异步函数的执行时间不会等待所有异步任务完成，而是会立即返回**，因此计时会不准确。<br>

即使使用了装饰器写法，但如果没有对异步函数进行特殊处理，依旧计时会不准确。🚨🚨🚨<br>

### 正确示例：

正确写法是：利用`await`关键字等待异步任务完成，将异步任务包含其中。代码示例如下：<br>

```python
from sanic import Sanic
from sanic.response import json
import jieba
import time

# 定义timing_decorator装饰器
def timing_decorator(func):
    async def wrapper(request, *args, **kwargs):
        start_time = time.time()  # 记录函数开始执行的时间
        result = await func(request, *args, **kwargs)  # 执行被装饰的函数(异步函数)
        end_time = time.time()  # 记录函数执行结束的时间
        elapsed_time = end_time - start_time  # 计算函数执行的总时间

        # 获取函数的名称，如果无法获取名称，则使用类的名称
        func_name = getattr(func, "__name__", None) or func.__class__.__name__

        # 输出函数名称和执行时间
        print(f"Function {func_name} took {elapsed_time:.6f} seconds to execute.")

        return result  # 返回被装饰函数的结果

    return wrapper  # 返回包装函数，用于替代原始函数

app = Sanic("SEGMENT-API")

@app.route("/segment", methods=["POST"])
@timing_decorator
async def segment(request):
    text = request.form.get("user_input")
    if not text:
        return json({"Error": "Missing 'user_input' parameter"}, status=400)

    segment_text = jieba.lcut(text)
    return json({"程序的分词结果为：": segment_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8848)
```

理解 `timing_decorator` 装饰器函数中的异步操作需要对 Python 的异步编程有一些基本的了解。💦💦💦<br>

在 Python 中，异步编程是一种并发的编程方式，它允许你在一个程序中同时执行多个任务而不会阻塞主线程。异步操作通常用于处理 I/O 密集型任务，如网络请求或文件操作，以充分利用等待 I/O 操作完成的时间。<br>

在 Sanic 中，请求处理函数通常是异步函数，因为它们可能需要等待客户端请求的数据或执行一些异步操作。因此，`timing_decorator` 装饰器函数也需要是一个异步函数，以便能够包装和测量这些异步请求处理函数的执行时间。<br>

下面是 `timing_decorator` 装饰器函数中异步操作的关键点解释：<br>

1. `async def wrapper(request, *args, **kwargs)`：这是装饰器内部的包装函数，它使用 `async def` 定义，表示这是一个异步函数。异步函数可以包含 `await` 关键字，允许在执行期间等待异步操作完成而不会阻塞整个程序。

2. `result = await func(request, *args, **kwargs)`：这一行代码调用了被装饰的原始函数 `func`，并使用 `await` 关键字等待其执行完成。`await` 的作用是在函数执行到这一行时，暂停执行，允许其他任务或异步操作继续执行。一旦 `func` 完成执行，它会恢复执行 `wrapper` 函数后面的代码。这是异步操作的核心概念，它使得程序能够高效地利用等待时间来执行其他任务。

3. 异步函数的特点：异步函数可以在等待 I/O 操作（如文件读写、网络请求等）时释放控制权，让事件循环（Event Loop）去处理其他任务。这样可以避免线程或进程阻塞，提高程序的并发性能。

总之，异步操作允许你在等待某些任务完成时执行其他任务，而不会阻塞整个程序。<br>

在 `timing_decorator` 装饰器函数中，我们将其定义为异步函数以适应可能是异步的请求处理函数，并使用 `await` 来等待请求处理函数的执行，确保测量整个请求的执行时间。这样，即使请求处理函数可能涉及异步操作，我们仍然可以准确测量其执行时间。<br>
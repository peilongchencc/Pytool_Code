# Loguru
Loguru 是一个简单而方便的日志库，用于在 Python 项目中记录和处理日志。相较于 python 自带的 logging 库，优势在于配置简单。<br>
- [Loguru](#loguru)
  - [loguru 的安装：](#loguru-的安装)
  - [简单使用：](#简单使用)
  - [格式化log信息：](#格式化log信息)
  - [log信息输出至log文件：](#log信息输出至log文件)
  - [logger.add() 方法解析：](#loggeradd-方法解析)
    - [rotation(轮转):](#rotation轮转)
    - [filter：](#filter)
    - [compression:](#compression)
  - [复杂示例：](#复杂示例)
  - [项目中loguru使用示例:](#项目中loguru使用示例)

## loguru 的安装：
```shell
pip install loguru
```

## 简单使用：
```python
from loguru import logger

logger.debug('This is debug information')
logger.info('This is info information')
logger.warning('This is warn information')
logger.error('This is error information')
```
logger 中不同 `level` 的日志信息颜色是不一样的，终端效果是彩色的，我这里因为是 Markdown 格式，所以不显示颜色。具体终端显示的信息如下：<br>
```shell
2023-08-22 17:22:59.696 | DEBUG    | __main__:<module>:4 - This is debug information
2023-08-22 17:22:59.697 | INFO     | __main__:<module>:5 - This is info information
2023-08-22 17:22:59.697 | INFO     | __main__:<module>:7 - This is nlp-server info information
2023-08-22 17:22:59.697 | WARNING  | __main__:<module>:8 - This is warn information
2023-08-22 17:22:59.697 | ERROR    | __main__:<module>:9 - This is error information
```

## 格式化log信息：
logger 支持 `f-string` 形式格式化log信息。<br>
```python
from loguru import logger
message = "nlp-server"
logger.info(f'这里是 {message} info 信息。')
```
终端效果：<br>
```shell
2023-08-22 17:39:31.796 | INFO     | __main__:<module>:3 - 这里是 nlp-server info 信息。
```

## log信息输出至log文件：
通过在 `logger.add()` 方法中添加文件名或文件路径即可实现。<br>
```python
from loguru import logger
logger.add("runtime.log")   # 追加形式写入

logger.info('This is info information')
```
注意⚠️：这种方式会将 `log` 信息同时在终端和 `log` 文件输出。<br>

如果只想要在 `log` 文件输出，需要在 `logger.add()` 方法前添加以下代码：
```python
# 关闭控制台输出
logger.remove(handler_id=None)
```
完整代码：<br>
```python
from loguru import logger
# 关闭控制台输出
logger.remove(handler_id=None)
logger.add("runtime.log")   # 追加形式写入

logger.info('This is info information')
```

## logger.add() 方法解析：
前面简单讲了一下 `logger.add()` 的使用，其实 `logger.add()` 功能非常强大，loguru 比 python 自带的 logging 库方便就体现于此。<br>

### rotation(轮转):
`rotation` 参数的作用是设置创建新日志文件的条件，可选项为 **"文件大小"** 和 **"时间"**。🚼🚼🚼无法同时实现控制时间和文件大小，如果要同时实现这两个功能需要配合 logging 库。<br>

下面以 "当文件大小达到 10 KB时，创建一个新log文件，文件名是 run+当时的时间。" 为例，讲解一下 `rotation` 的用法：<br>
```python
import time
from loguru import logger
# 关闭控制台输出
logger.remove(handler_id=None)
timestamp = time.time()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

# "10 KB"太小了，可以改为 "500 MB" 、 "1 GB" 或 "10 days"
logger.add(f'run_{current_time}.log', rotation="10 KB")

logger.debug('your log message.')
```
`rotation` 参数的可选项是多样的，支持各种字符串，例如："500 MB" 、 "1 GB" 、 "10 days" 、"Tuesday" 、"1 week" 或 "18:16"(表示每天的18:16创建新的日志文件)。<br>

`rotation` 好像不能太具体的指定时间，比如 "每周二凌晨1点" 轮转日志文件(也可能是我对 `rotation` 的了解不深)。<br>

`rotation` 无法直接指定 "每周二凌晨1点" 没有关系，我们可以采用多个方法配合的方式实现。让 `rotation="1 week"` ，然后用 `crontab` 起一个定时任务，每周二凌晨1点触发日志创建也可实现这个功能。<br>

`rotation` 参数的最小值和最大值取决于文件系统的限制以及具体的操作系统。在 loguru 的文档中并没有明确指定最小值和最大值的具体数值。通常来说，最小值可能为1字节或0字节，表示每次写入日志都会轮转文件，而最大值可能在几GB到几TB之间。<br>

### filter：
`filter` 参数用于指定一个🔶**自定义**🔶的过滤器函数，用于决定哪些日志消息应该被传入日志文件中。<br>

下面是一个示例，演示如何使用filter参数来过滤日志消息：<br>
```python
import loguru

def custom_filter(record):
    # 只将level为INFO的日志消息传入runtime.log文件
    return record["level"].name == "INFO"

loguru.logger.add("runtime.log", filter=custom_filter)
loguru.logger.info("This is an INFO message")
loguru.logger.debug("This is a DEBUG message")
```
运行上述代码，终端会完整显示所有日志信息，但 `runtime.log` 文件中只有 `info` 的日志信息。<br>

构建自定义过滤器函数时，需要注意：<br>

过滤器函数是一个可以接受一个日志记录器对象以及一个日志记录记录对象作为参数的函数。它应该返回一个布尔值，指示该日志消息是否应该被传入日志文件中。如果返回 `True` ，表示该日志消息应该被传入日志文件中；如果返回 `False`，表示该日志消息应该被忽略。<br>

### compression:
当log文件达到 `rotation` 设置的条件后，将log文件压缩为 `zip` 格式。使用 `unzip` 解压缩后依旧是 `run_xxx.log` 文件。<br>
```python
import time
from loguru import logger
# 关闭控制台输出
logger.remove(handler_id=None)
timestamp = time.time()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

# "10 KB"太小了，可以改为 "500 MB" 、 "1 GB" 或 "10 days"
logger.add(f'run_{current_time}.log', rotation="10 KB", compression='zip')
for i in range (500):
    logger.debug(f'your log{i} message.')
```

## 复杂示例：

```python
from loguru import logger
# 关闭控制台输出
logger.remove(handler_id=None)
# 设置生成日志文件，utf-8编码，每天0点切割，zip压缩，保留3天，异步写入
logger.add(sink='test.log', level="INFO", rotation='00:00', retention='3 days', compression='zip', encoding='utf-8', enqueue=True)  
```


```python
(method) def add(
    sink: str | PathLikeStr,
    *,
    level: str | int = ...,
    format: str | FormatFunction = ...,
    filter: str | FilterFunction | FilterDict | None = ...,
    colorize: bool | None = ...,
    serialize: bool = ...,
    backtrace: bool = ...,
    diagnose: bool = ...,
    enqueue: bool = ...,
    catch: bool = ...,
    rotation: str | int | time | timedelta | RotationFunction | None = ...,
    retention: str | int | timedelta | RetentionFunction | None = ...,
    compression: str | CompressionFunction | None = ...,
    delay: bool = ...,
    watch: bool = ...,
    mode: str = ...,
    buffering: int = ...,
    encoding: str = ...,
    **kwargs: Any
) -> int
```


## 项目中loguru使用示例:

一个项目中要保证日志的格式统一,合理的做法是在程序的入口文件( `main.py` )中设置日志格式,其他文件中直接使用`logger.info()`等方法来记录日志即可,这样输出的日志格式都是统一的。<br>

例如,入口文件( `main.py` ):<br>

```python
# main.py
import os
from loguru import logger
from module_1 import some_function
from module_2 import another_function

# 设置日志
logger.remove()
logger.add("loguru_test.log", rotation="1 GB", backtrace=True, diagnose=True, format="{time} {level} {message}")

def main_function():
    # 获取当前文件的文件名
    current_file_name = os.path.basename(__file__)
    logger.info(f"主程序文件名为:{current_file_name}")

if __name__ == '__main__':
    main_function()
    some_function()
    another_function()
```

其他模块或文件,例如 `module_1.py`:<br>

```python
# module1.py
import os
from loguru import logger

def some_function():
    # 获取当前文件的文件名
    current_file_name = os.path.basename(__file__)
    logger.info(f"模块1文件名为:{current_file_name}")
```

其他模块或文件,例如 `module_2.py`:<br>

```python
# module2.py
import os
from loguru import logger

def another_function():
    # 获取当前文件的文件名
    current_file_name = os.path.basename(__file__)
    logger.info(f"模块2文件名为:{current_file_name}")
```

`python main.py` 运行入口文件后,会自动根据路径创建 `loguru_test.log` 文件,然后将log信息添加到其中。<br>

如果`loguru_test.log` 文件已经存在,会以追加形式将log信息添加到其中。<br>

❤️这样做可以确保整个项目中的日志记录器是一致的,同时避免了在每个文件中都重复设置日志。<br>

`loguru_test.log` 文件中内容如下:<br>

```log
2024-04-11T11:00:09.327469+0800 INFO 主程序文件名为:main.py
2024-04-11T11:00:09.327596+0800 INFO 模块1文件名为:module_1.py
2024-04-11T11:00:09.327681+0800 INFO 模块2文件名为:module_2.py
2024-04-11T11:02:02.553378+0800 INFO 主程序文件名为:main.py
2024-04-11T11:02:02.553503+0800 INFO 模块1文件名为:module_1.py
2024-04-11T11:02:02.553574+0800 INFO 模块2文件名为:module_2.py
```
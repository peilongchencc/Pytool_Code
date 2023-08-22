# Loguru
Loguru 是一个简单而方便的日志库，用于在 Python 项目中记录和处理日志。相较于 python 自带的 logging 库，优势在于配置简单。<br>

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

logger默认有控制台输出，即sys.stderr，想要只输出到文本而不输出到控制台，需要关闭sys.stderr。<br>

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
前面简单讲了一下 `logger.add()` 的使用，其实 `logger.add()` 功能非常强大，loguru 比 python 自带的 logging 库方便就体现于此。




## 复杂示例：
```python
from loguru import logger
# 关闭控制台输出
logger.remove(handler_id=None)
# 设置生成日志文件，utf-8编码，每天0点切割，zip压缩，保留3天，异步写入
logger.add(sink='test.log', level=”INFO”, rotation=’00:00′, retention=’3 days’, compression=’zip’, encoding=’utf-8′, enqueue=True)  
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
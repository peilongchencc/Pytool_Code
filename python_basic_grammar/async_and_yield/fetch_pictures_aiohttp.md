# 利用图片链接将图片下载到本地:
- [利用图片链接将图片下载到本地:](#利用图片链接将图片下载到本地)
  - [使用`requests`同步下载图片:](#使用requests同步下载图片)
  - [使用`aiohttp`异步下载图片:](#使用aiohttp异步下载图片)
    - [`asyncio.gather` 用法介绍:](#asynciogather-用法介绍)
    - [基本用法](#基本用法)
    - [示例代码](#示例代码)
    - [特点](#特点)
    - [注意事项](#注意事项)
    - [`asyncio.gather`中`return_exceptions=True`的作用是什么？](#asynciogather中return_exceptionstrue的作用是什么)
    - [`asyncio.gather(*tasks)`中 `*tasks` 是什么用法？](#asynciogathertasks中-tasks-是什么用法)
    - [python根据文件路径删除指定文件:](#python根据文件路径删除指定文件)
      - [场景模拟:](#场景模拟)
      - [解决方案:](#解决方案)

## 使用`requests`同步下载图片:

首先确保你已经安装了requests库。如果没有安装，可以通过运行 `pip install requests` 来安装。<br>

```python
import requests

# 图片的URL
url = "https://xxxxxx.com/pic/2024-02-22/be0c6836-6bc2-4dc1-bf0d-cf88029c522c.png?Expires=4862173056&OSSAccessKeyId=LTAI4Fqnoczaf1rSV6Vd7sLe&Signature=9YYZgqhN6eSuoQUrWhUndD40pSU%3D"

# 发起GET请求下载图片
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 将内容写入文件
    with open("downloaded_image.png", "wb") as file:
        file.write(response.content)
    print("图片下载成功")
else:
    print("下载失败，状态码：", response.status_code)
```

这段代码首先发送一个GET请求到提供的URL，然后检查HTTP响应状态码是否为200（表示请求成功）。如果请求成功，代码会读取响应的内容（即图片的二进制数据）并将其写入到当前目录下的一个文件中。这里，图片被保存为downloaded_image.png。<br>

请注意，由于笔者主要使用异步操作，对于同步操作，这里只写出简单示例，相关完整版功能请参考 `aiohttp` 异步示例。<br>


## 使用`aiohttp`异步下载图片:

可以使用 `aiohttp` 来异步下载图片。以下是一个简单的示例，说明如何使用 `aiohttp` 来下载图片并保存到本地。请确保你已经安装了 `aiohttp`。如果没有安装，可以通过运行 `pip install aiohttp` 来安装它。<br>

代码中使用 `aiofiles` 异步写文件，需要安装 `aiofiles` 。如果没有安装，可以通过运行 `pip install aiofiles` 来安装。<br>

```python
"""
@author:PeilongChen(peilongchencc@163.com)
@description:这个脚本首先定义了一个异步函数 `download_image`，它接受图片的 URL 列表进行遍历，使用 `aiohttp.ClientSession()` 异步发送 HTTP GET 请求获取图片，然后利用 `aiofiles.open` 异步写入文件，这样可以在不阻塞主线程的情况下下载并保存图片，图片的文件名从 URL 中获取。
"""
import os
import aiohttp
import asyncio
import aiofiles
from urllib.parse import urlparse, parse_qs

async def download_image(url):
    # 解析 URL 获取文件名
    parsed_url = urlparse(url)
    if "filePath" in parse_qs(parsed_url.query):
        # 如果是查询参数中包含文件路径，则从查询参数中提取文件名
        file_path = parse_qs(parsed_url.query)["filePath"][0]
        filename = file_path.split('/')[-1]
    else:
        # 否则，从 URL 路径中直接提取文件名
        filename = parsed_url.path.split('/')[-1]
    
    # 定义文件保存路径
    save_path = f"ocr_pictures/{filename}"
    # 获取给定路径中的路径名，例如对于 f"ocr_pictures/{filename}" 会返回 "ocr_pictures"
    save_dir = os.path.dirname(save_path)

    # 检查保存路径是否存在，不存在则创建
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                # 使用 aiofiles 异步写文件，需要安装 aiofiles
                # 如果没有安装，可以通过运行 pip install aiofiles 来安装
                async with aiofiles.open(save_path, mode='wb') as f:
                    await f.write(await response.read())
                    print(f"图片已保存到 {save_path}")

async def main(urls):
    tasks = [download_image(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        "https://xxxxxx.com/pic/2024-02-22/be0c6836-6bc2-4dc1-bf0d-cf88029c522c.png?Expires=4862173056&OSSAccessKeyId=LTAI4Fqnoczaf1rSV6Vd7sLe&Signature=9YYZgqhN6eSuoQUrWhUndD40pSU%3D",
        "https://xxxxxx.com.cn/user/file/download/?filePath=/positionimages/202401/20240112102706-1.jpg"
    ]

    # 运行异步任务
    asyncio.run(main(urls))
```

在这个代码版本中，所有的函数定义和导入都放在脚本的顶部，而将实际执行的代码放在了 `if __name__ == "__main__":` 块内。这样，当你直接运行这个脚本时，它会执行异步下载任务；而如果你从另一个脚本中导入这个脚本中的函数，那些执行代码就不会被运行，避免了不必要的执行和潜在的错误。

### `asyncio.gather` 用法介绍:

`asyncio.gather(*tasks)` 是 Python 异步编程中的一个重要功能，用于并发运行多个异步任务。这个函数主要的作用是聚合多个异步操作，让它们并发执行，从而提高程序的执行效率。当你有多个异步操作需要同时执行时，使用 `asyncio.gather` 可以非常方便地处理这些操作。<br>

### 基本用法

基本上，你会将多个协程（coroutines）作为参数传递给 `asyncio.gather`，它会并发运行这些协程，并等待所有协程完成。它返回一个单一的协程（一个 `Future` 对象），这个 `Future` 对象在所有传递给 `gather` 的协程完成时完成。<br>

### 示例代码

```python
import asyncio

async def task1():
    # 模拟异步操作
    print('Task 1 is running')
    await asyncio.sleep(1)  # 模拟 IO 操作
    return 'Result of Task 1'

async def task2():
    print('Task 2 is running')
    await asyncio.sleep(2)  # 模拟 IO 操作
    return 'Result of Task 2'

async def main():
    # 使用 asyncio.gather 并发运行 task1 和 task2
    results = await asyncio.gather(task1(), task2())
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
```

终端显示:<br>

```txt
Task 1 is running
Task 2 is running
['Result of Task 1', 'Result of Task 2']
```

在这个例子中，`task1` 和 `task2` 会并发执行。`asyncio.gather(task1(), task2())` 调用将等待这两个任务都完成，然后返回一个包含所有结果的列表。<br>

### 特点

- **并发执行**：传递给 `gather` 的任务会并发执行，这可以显著减少总的运行时间，特别是在涉及到 IO 等待的情况下。
- **灵活性**：`gather` 允许你同时等待多个异步操作，无论它们的执行时间如何，这对于优化程序性能非常有用。
- **结果聚合**：`gather` 返回的是一个包含所有任务结果的列表（按传入顺序），这使得处理多个异步操作的结果变得非常方便。

### 注意事项

- 使用 `gather` 时，如果其中一个任务失败（抛出异常），`gather` 默认会取消所有其他任务。你可以通过设置 `return_exceptions=True` 来改变这个行为，这样的话，结果列表中将包含成功的结果和异常对象。
- 由于 `gather` 并发执行任务，所以 **任务之间的执行顺序是不确定的** 🐳🐳🐳。如果任务之间有依赖关系，需要其他方式来管理这些依赖，或者单独处理依赖任务。


### `asyncio.gather`中`return_exceptions=True`的作用是什么？

在 `asyncio.gather(*tasks, return_exceptions=True)` 中，`return_exceptions=True` 参数的作用是控制 `asyncio.gather` 函数在遇到异常时的行为。<br>

默认情况下，`return_exceptions` 参数为 `False`，这意味着当 `gather` 中的任何一个任务抛出异常时，`asyncio.gather` 会立即取消所有其他任务，并将该异常向上抛出至调用者。这种行为对于某些情况下希望快速失败并处理异常的场景是有用的。<br>

然而，当 `return_exceptions=True` 时，`gather` 的行为会有所不同：<br>

- 如果任务成功完成，它们的结果会被正常返回。

- 如果任务抛出异常，`gather` 不会抛出异常并中止其他任务。相反，它会捕获异常，并在结果列表中，对应位置返回这个异常对象。

这样做的好处是，即使某些任务失败，你也可以获取所有任务的结果（无论是成功的结果还是异常），然后在所有任务都完成后统一处理这些结果或异常。这对于并发执行多个任务并希望独立处理每个任务的结果或异常的场景非常有用。<br>

例如，你可以遍历 `gather` 返回的结果列表，检查每个元素是否是异常实例，如果是，则处理异常；如果不是，则处理正常的结果。这提供了一种灵活的方式来处理并发任务中的错误情况，而不是让单一的异常中断所有操作。<br>


### `asyncio.gather(*tasks)`中 `*tasks` 是什么用法？

在 Python 中，`*` 符号用在函数调用时，表示将可迭代对象（如列表、元组等）"展开"，使其元素成为函数的位置参数。在 `asyncio.gather(*tasks)` 调用中，`*tasks` 就是利用了这一特性。<br>

使用 `*` 符号可以将 `tasks` 列表中的每个元素（即每个异步任务）"展开"，作为独立的参数传递给 `asyncio.gather`。<br>

这样，如果你的 `tasks` 列表中有三个任务，`asyncio.gather(*tasks)` 就相当于 `asyncio.gather(task1, task2, task3)`，其中 `task1, task2, task3` 是列表中的三个元素。<br>

这种用法使得函数调用非常灵活，特别是当你事先不知道有多少个参数需要传递给函数时。通过将参数组织在列表或元组中，然后在函数调用时使用 `*` 符号展开，可以动态地调整传递给函数的参数数量。<br>

### python根据文件路径删除指定文件:

#### 场景模拟:

我的文件保存路径为 "ocr_pictures/20240112102706-1.jpg"，我在代码的OCR服务执行完毕后想要删除这个文件，应该怎么做呢？<br>

#### 解决方案:

你可以使用`os`模块来删除文件。首先，需要导入`os`模块，然后使用`os.remove()`函数来删除指定的文件。这里是一个示例代码，展示如何删除你提到的文件：<br>

```python
import os

# 文件路径
file_path = "ocr_pictures/20240112102706-1.jpg"

# 检查文件是否存在
if os.path.exists(file_path):
    # 删除文件
    os.remove(file_path)
    print("文件已删除。")
else:
    print("找不到文件，无法删除。")
```

这段代码首先检查文件是否存在，如果存在，则使用`os.remove()`函数删除该文件。这样做的好处是避免在文件不存在时尝试删除文件，从而引发异常。如果文件不存在，它会打印一条消息说找不到文件。这种做法可以确保代码的健壮性。<br>
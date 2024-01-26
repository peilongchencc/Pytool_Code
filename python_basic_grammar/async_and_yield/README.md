# async 和 yield
- [async 和 yield](#async-和-yield)
  - [I/O 操作介绍:](#io-操作介绍)
  - [异步编程:](#异步编程)
    - [基本概念](#基本概念)
    - [示例](#示例)
      - [步骤 1: 引入必要的库](#步骤-1-引入必要的库)
      - [步骤 2: 定义异步函数](#步骤-2-定义异步函数)
      - [步骤 3: 创建主要的异步函数](#步骤-3-创建主要的异步函数)
      - [步骤 4: 运行事件循环](#步骤-4-运行事件循环)
    - [完整代码](#完整代码)
  - [yield生成器的多种返回格式:](#yield生成器的多种返回格式)
    - [生成器的常规使用:](#生成器的常规使用)
    - [将生成器的所有结果收集到一个列表中并返回:](#将生成器的所有结果收集到一个列表中并返回)
    - [返回最后一个生成的结果:](#返回最后一个生成的结果)
  - [异步调用大模型接口返回答案示例:](#异步调用大模型接口返回答案示例)
    - [情况描述:](#情况描述)
    - [解决方案:](#解决方案)
    - [数据串扰问题:](#数据串扰问题)
    - [数据串扰问题解答:](#数据串扰问题解答)
    - [工具函数和sanic路由不在同一个文件时的代码改动:](#工具函数和sanic路由不在同一个文件时的代码改动)

## I/O 操作介绍:

I/O 是 "Input/Output" 的缩写，I/O 操作即输入/输出操作，是计算机程序与外界（例如用户、文件系统、网络等）进行数据交换的过程。这个术语通常用于描述两种主要类型的操作：<br>

1. **文件 I/O**：这涉及到读写文件系统上的文件。例如，当你的程序从硬盘上的文件中读取数据，或者向文件写入数据时，这就是文件 I/O 操作。这些操作通常涉及等待磁盘驱动器或者固态硬盘完成数据的读取或写入，这可能需要相对较长的时间。

2. **网络 I/O**：这指的是通过网络发送和接收数据。例如，当你的程序向服务器发送请求或从服务器接收数据时，这就是网络 I/O 操作。网络 I/O 通常涉及等待网络延迟和数据传输，这也可能是一个耗时的过程。

I/O 操作通常是计算机程序中较慢的部分，因为它们依赖于外部系统（如硬盘、网络设备等），这些系统的速度通常比 CPU 和内存慢得多。**这就是为什么在进行 I/O 操作时，常常会使用异步编程技术。**异步编程允许程序在等待 I/O 操作完成时继续执行其他任务，从而提高程序的整体效率和响应性。🫠🫠🫠<br>


## 异步编程:

Python中的异步编程是一种编程范式，它允许程序在等待某些操作（如I/O操作）完成时继续执行其他任务。这在处理大量并发连接或高延迟操作时特别有用。Python从3.5版本开始引入了`async`和`await`关键字，使异步编程变得更加简单和直观。<br>

### 基本概念

1. **协程（Coroutine）**: 使用`async def`定义的函数。这种函数在调用时不会立即执行，而是返回一个协程对象。

2. **事件循环（Event Loop）**: 管理并分配执行异步任务的机制。事件循环在后台运行，按照任务的就绪状态进行调度。

3. **`await`**: 用于暂停协程的执行，直到等待的协程完成。在`await`之后的代码，只有在`await`的协程完成后才会执行。

### 示例

让我们通过一个简单的例子来理解这些概念：假设我们要异步地获取多个网页的内容。<br>

#### 步骤 1: 引入必要的库

```python
import asyncio
import aiohttp
```

这里，`asyncio`是Python标准库中的异步I/O框架，`aiohttp`是一个支持异步请求的HTTP客户端。<br>

#### 步骤 2: 定义异步函数

```python
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
```

这个`fetch`函数是一个协程，它异步地获取给定URL的内容。<br>

#### 步骤 3: 创建主要的异步函数

```python
async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```

`main`函数也是一个协程，它创建了多个`fetch`协程的任务，并且使用`asyncio.gather`来并发地运行它们。<br>

#### 步骤 4: 运行事件循环

```python
urls = ["https://www.example.com", "https://www.example.org"]
result = asyncio.run(main(urls))
print(result)
```

这里使用`asyncio.run()`来运行主协程`main`。它会创建事件循环，运行协程，直到协程完成。<br>

### 完整代码

```python
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

urls = ["https://www.example.com", "https://www.example.org"]
result = asyncio.run(main(urls))
print(result)
```

这个例子展示了Python异步编程的基本结构和步骤。你可以根据自己的需要修改这个例子，以适应不同的异步编程场景。<br>


## yield生成器的多种返回格式:

### 生成器的常规使用:

```python
def squares_generator(n):
    for i in range(n):
        yield i ** 2

if __name__ == "__main__":
    # 遍历生成器
    for square in squares_generator(5):
        print(square)
```

终端输出:<br>

```txt
0
1
4
9
16
```

### 将生成器的所有结果收集到一个列表中并返回:

```python
def squares_generator(n):
    for i in range(n):
        yield i ** 2

def all_squares(n):
    """将生成器的所有结果收集到一个列表中并返回
    """
    return list(squares_generator(n))

if __name__ == "__main__":
    res = all_squares(6)
    print(type(res))
    print(res)
```

终端输出:<br>

```txt
<class 'list'>
[0, 1, 4, 9, 16, 25]
```

### 返回最后一个生成的结果:

```python
def squares_generator(n):
    for i in range(n):
        yield i ** 2

def last_square(n):
    """遍历生成器生成的所有结果，并在每次迭代中更新 last 变量。最后，函数会返回最后一个生成的结果
    """
    last = None
    for square in squares_generator(n):
        last = square
    return last

if __name__ == "__main__":
    res = last_square(6)
    print(type(res))
    print(res)
```

终端输出:<br>

```txt
<class 'int'>
25
```

## 异步调用大模型接口返回答案示例:

### 情况描述:

我使用的python，我的函数如下，函数中需要调用大模型接口，大模型接口支持的并行数为5。当前我使用的request的post方式连接的大模型接口，我是不是应该将`request`改为`aiohttp`的post方式？我这个函数也需要写成异步的形式吗？我使用的sanic，sanic的`/answer`路由会调用我这个函数，sanic应该怎样调用这个函数呢？<br>

### 解决方案:

你的函数 `con_aichatbot` 用于连接一个大型模型的API，并通过HTTP POST请求发送数据。目前，你使用的是 `requests` 库，这是一个同步的HTTP客户端。当你的应用程序需要处理并发请求时，特别是当你需要同时向大模型接口发送多个请求时，使用异步的HTTP客户端会更有效，比如 `aiohttp`。<br>

由于大模型接口支持的并行数为5，你确实可以考虑将 `requests` 改为 `aiohttp`。`aiohttp` 是基于异步I/O的，这意味着在等待HTTP响应时，你的程序可以继续执行其他任务。这在处理多个并行请求时特别有用。<br>

同时，你的函数也需要改写为异步的形式。这样，你可以在函数内部使用 `await` 关键字调用异步的HTTP请求，而不会阻塞整个程序的运行。<br>

另外，你提到你使用的是 Sanic，这是一个异步的Web框架。在 Sanic 中调用异步函数非常简单。你只需要在定义路由处理函数时添加 `async` 关键字，然后在其中使用 `await` 调用你的异步函数。这样，Sanic 可以在处理请求时保持其异步特性。<br>

修改后的函数和Sanic路由调用示例如下：<br>

```python
import aiohttp
import json

async def con_aichatbot(access_token=None, channel_id=None, sign=None, timestamp=None, user_input=None):
    if access_token and channel_id and sign and timestamp and user_input:
        data = {
            # ... 同之前的data定义
        }
        url = (
            # ... 同之前的url定义
        )
        headers = {
            # ... 同之前的headers定义
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data, headers=headers) as response:
                    response.raise_for_status()
                    complete_output = None
                    async for line in response.content:
                        line = line.decode('utf-8')
                        # ... 同之前的处理逻辑
        except Exception as e:
            print("连接大模型时出错：", e)
        
        return complete_output

# 在Sanic中使用该函数
from sanic import Sanic, response

app = Sanic("MyApp")

@app.route("/answer", methods=['POST'])
async def answer(request):
    data = request.json
    # 假设data包含了所需的所有参数
    output = await con_aichatbot(
        access_token=data.get("access_token"),
        channel_id=data.get("channel_id"),
        # ... 其他参数
    )
    return response.json({"reply": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

这里有几点需要注意：<br>

1. `aiohttp.ClientSession()` 用于创建一个异步HTTP会话。

2. 使用 `async with` 语法确保资源被正确地管理和释放。

3. `await` 用于等待异步操作完成。

4. 在Sanic中定义路由时使用 `async` 和 `await` 以保持异步性。

### 数据串扰问题:

使用你的代码，多个用户同时请求，不会出现用户A的问题返回的是用户B的答案吧，不会串了吧？<br>

### 数据串扰问题解答:

使用我提供的代码，多个用户同时发送请求时，不会发生用户A的问题得到用户B答案的情况。这是因为每个请求都是独立处理的，每个请求都会创建自己的异步上下文并执行。这就是异步编程的优势之一：**即使在并发请求的情况下，也能保持每个请求的数据隔离。**<br>

在异步编程中，每当一个新的请求到达，Sanic 会为这个请求创建一个新的协程（coroutine）。每个协程都是独立的，并且拥有自己的局部变量和状态。因此，即使有多个请求并发执行，它们各自的数据（如请求参数、局部变量等）也是相互隔离的。<br>

在你的应用场景中，当 `con_aichatbot` 函数被调用时，它会处理传入的参数（例如 `access_token`、`channel_id`、`sign`、`timestamp` 和 `user_input`），这些参数都是请求特有的。因此，每个请求都会根据其特定的输入处理并生成独立的输出。<br>

总之，在你的使用场景中，使用异步编程和 Sanic 框架，可以确保即使在高并发的情况下，每个用户的请求都是独立处理的，不会发生数据串扰的问题。<br>

### 工具函数和sanic路由不在同一个文件时的代码改动:

如果你的函数和 Sanic 路由不在同一个文件中，你可以通过导入模块的方式来使用这些函数。这是 Python 中常见的做法，可以帮助你组织和模块化代码。以下是一个简单的示例，展示了如何在不同的文件中定义函数和路由，并将它们整合在一起。<br>

假设你有两个文件：一个是包含 `con_aichatbot` 函数的文件（我们称之为 `aichatbot.py`），另一个是定义 Sanic 应用和路由的文件（我们称之为 `app.py`）。<br>

1. **aichatbot.py**:

```python
# 异步函数定义
async def con_aichatbot(access_token=None, channel_id=None, sign=None, timestamp=None, user_input=None):
    # ... 函数实现 ...
```

2. **app.py**:

```python
from sanic import Sanic, response
# 从其他文件导入异步函数
from aichatbot import con_aichatbot

app = Sanic("MyApp")

@app.route("/answer", methods=['POST'])
async def answer(request):
    data = request.json
    # 调用异步函数
    output = await con_aichatbot(
        access_token=data.get("access_token"),
        channel_id=data.get("channel_id"),
        # ... 其他参数 ...
    )
    return response.json({"reply": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

在这个例子中，`aichatbot.py` 包含了你的异步函数 `con_aichatbot`，而 `app.py` 包含了 Sanic 应用和路由的定义。你可以在 `app.py` 中通过 `from aichatbot import con_aichatbot` 来导入 `aichatbot.py` 中定义的函数。<br>

这种组织方式不仅有助于保持代码的清晰和模块化，而且也确保了不同文件中的代码可以相互调用。当你的项目规模增长时，这种模块化的方法特别有用。<br>
# yield

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

### 追问:

使用你的代码，多个用户同时请求，不会出现用户A的问题返回的是用户B的答案吧，不会串了吧？<br>

### 解答:

使用我提供的代码，多个用户同时发送请求时，不会发生用户A的问题得到用户B答案的情况。这是因为每个请求都是独立处理的，每个请求都会创建自己的异步上下文并执行。这就是异步编程的优势之一：**即使在并发请求的情况下，也能保持每个请求的数据隔离。**<br>

在异步编程中，每当一个新的请求到达，Sanic 会为这个请求创建一个新的协程（coroutine）。每个协程都是独立的，并且拥有自己的局部变量和状态。因此，即使有多个请求并发执行，它们各自的数据（如请求参数、局部变量等）也是相互隔离的。<br>

在你的应用场景中，当 `con_aichatbot` 函数被调用时，它会处理传入的参数（例如 `access_token`、`channel_id`、`sign`、`timestamp` 和 `user_input`），这些参数都是请求特有的。因此，每个请求都会根据其特定的输入处理并生成独立的输出。<br>

总之，在你的使用场景中，使用异步编程和 Sanic 框架，可以确保即使在高并发的情况下，每个用户的请求都是独立处理的，不会发生数据串扰的问题。<br>
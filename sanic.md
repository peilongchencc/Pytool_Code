# Sanic:
- [Sanic:](#sanic)
  - [Background tasks(后台任务):](#background-tasks后台任务)
    - [Creating Tasks(创建任务):](#creating-tasks创建任务)
    - [Adding tasks before `app.run`(在 `app.run` 之前添加任务):](#adding-tasks-before-apprun在-apprun-之前添加任务)
    - [Named tasks(为tasks命名):](#named-tasks为tasks命名)
  - [Websockets:](#websockets)
  - [Websockets与get、post方法的区别:](#websockets与getpost方法的区别)
    - [Websockets介绍:](#websockets介绍)
    - [Routing(路由):](#routing路由)
    - [Handler(处理器):](#handler处理器)
    - [Configuration(配置):](#configuration配置)

## Background tasks(后台任务):

### Creating Tasks(创建任务):

It is often desirable(向往的；希望) and very convenient to make usage of [tasks](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task) in async Python. <br>

在异步 Python 中，通常希望并且非常方便地使用tasks。<br>

Sanic provides a convenient method to add tasks to the currently **running** loop. It is somewhat(有些；稍微) similar to `asyncio.create_task`. <br>

Sanic 提供了一种便捷的方法来将任务添加到当前**运行**的循环中。这与 `asyncio.create_task` 类似。

For adding tasks before the 'App' loop is running, see next section.<br>

如果要在 'App' 循环开始之前添加任务，请参阅下一节。<br>

```python
async def notify_server_started_after_five_seconds():
    await asyncio.sleep(5)
    print('Server successfully started!')   # 服务器成功启动！

app.add_task(notify_server_started_after_five_seconds())
```

Sanic will attempt to automatically inject the app, passing it as an argument to the task.<br>

> “Inject” 是一个动词，意思是向某物中注入或注射某种物质或信息。在上下文中，它指的是将应用程序作为参数传递给任务，类似于将某种信息或功能注入到任务中。

Sanic 将其(后台要启动的程序)作为参数传递给任务(task)，然后将尝试将 `add_task` 部分自动注入应用程序。<br>

```python
async def auto_inject(app): # "auto inject" 表示自动注入;
    await asyncio.sleep(5)
    print(app.name)

app.add_task(auto_inject)
```

Or you can pass the app argument explicitly.<br>

或者您可以显式地传递 app 参数。<br>

```python
async def explicit_inject(app): # "explicit inject" 表示明确注入;
    await asyncio.sleep(5)
    print(app.name)

app.add_task(explicit_inject(app))
```

### Adding tasks before `app.run`(在 `app.run` 之前添加任务):

It is possible to add background tasks before the App is run ie.(也就是说) before `app.run`. <br>

> "ie." 是拉丁语 "id est" 的缩写，意思是 "即" 或 "也就是说"。在英文中，它常用于解释或澄清前面提到的内容。

在 App 运行之前，即在 `app.run` 之前添加后台任务是可能的。<br>

🚨🚨🚨To add a task before the App is run, it is recommended to not pass the coroutine(协程) object (ie. one created by calling the `async` callable), but instead just pass the callable and Sanic will create the coroutine(协程) object on **each worker**.<br>

🚨🚨🚨要在 App 运行之前添加task，建议不要传递协程对象（即通过调用 `async` 可调用函数创建的对象），而是只传递可调用对象，Sanic 将在 **每个工作进程** 上创建协程对象。<br>

> 也就是说我们自己不要创建协程，Sanic会帮我们创建。

Note: the tasks that are added such are run as `before_server_start` jobs and thus run on every worker (and not in the main process).<br>

注意：这样添加的tasks将作为 `before_server_start` 任务运行，因此会在每个工作进程上运行（而不是在主进程中）。<br>

This has certain consequences(结果;后果;影响), please read [this comment on this issue](https://github.com/sanic-org/sanic/issues/2139) for further details.<br>

这会带来一些后果，请阅读关于此问题的评论以获取更多详细信息。<br>

To add work on the main process, consider adding work to `@app.main_process_start`. Note: the workers won't start until this work is completed.<br>

要在主进程上添加工作，请考虑添加到 `@app.main_process_start`。注意：工作进程在完成此工作之前不会启动。<br>

Example to add a task before `app.run`:<br>

```python
async def slow_work():
   ...

async def even_slower(num):
   ...

app = Sanic(...)
app.add_task(slow_work) # Note: we are passing the callable and not coroutine object ...
app.add_task(even_slower(10)) # ... or we can call the function and pass the coroutine.
app.run(...)
```

### Named tasks(为tasks命名):

When creating a task, you can ask Sanic to keep track of it for you by providing a `name`.<br>

创建tasks时，您可以要求 Sanic 通过提供一个 `name` 来为您跟踪它。<br>

```python
app.add_task(slow_work, name="slow_task")
```

You can now retrieve(检索) that task instance from anywhere in your application using `get_task`.<br>

您现在可以在应用程序的任何地方使用 `get_task` 来检索该任务实例。<br>

```python
task = app.get_task("slow_task")
```

If that task needs to be cancelled(取消), you can do that with `cancel_task`. Make sure that you `await` it.<br>

如果需要取消该task，您可以使用 `cancel_task` 来执行。确保您 `await` 它。<br>

```python
await app.cancel_task("slow_task")
```

All registered(注册的) tasks can be found in the `app.tasks` property(属性). <br>

所有注册的tasks都可以在 `app.tasks` 属性中找到。<br>

✅To prevent(防止) cancelled tasks from filling up, you may want to run `app.purge_tasks` that will clear out any completed or cancelled tasks.<br>

✅为了防止取消的任务填满，您可能希望运行 `app.purge_tasks`，它将清除任何已完成或已取消的任务。<br>

```python
app.purge_tasks()
```

This pattern can be particularly(特别地;特别显著;特别适用) useful with `websockets`:<br>

这种模式在使用 `websockets` 时尤其有用：<br>

```python
async def receiver(ws):
    while True:
        message = await ws.recv()
        if not message:
            break
        print(f"Received: {message}")

@app.websocket("/feed")
async def feed(request, ws):
    task_name = f"receiver:{request.id}"
    request.app.add_task(receiver(ws), name=task_name)
    try:
        while True:
            await request.app.event("my.custom.event")
            await ws.send("A message")
    finally:
        # When the websocket closes, let's cleanup the task
        # 当 WebSocket 关闭时，让我们清理任务
        await request.app.cancel_task(task_name)
        request.app.purge_tasks()
```

## Websockets:

## Websockets与get、post方法的区别:

Sanic 是一个异步框架，用于构建高效的 Web 应用和服务。它支持异步处理请求，这意味着它可以处理大量的并发连接。你提到的 GET 和 POST 是 HTTP 请求的方法，而 WebSockets 是一个不同的协议，用于实现双向通信。以下是 GET、POST 和 WebSockets 之间的主要区别：<br>

1. **GET 和 POST：**
   - **使用场景**：GET 和 POST 都是 HTTP 协议支持的请求方法，主要用于客户端和服务器之间的单向通信。GET 通常用于请求数据，而 POST 通常用于提交数据。
   - **数据传输**：GET 请求通过 URL 传输数据，因此数据大小有限，且数据可见。POST 请求通过请求体传输数据，可以发送更大量的数据，且数据不在 URL 中显示。
   - **安全性**：POST 比 GET 更安全，因为 GET 请求的数据可以在 URL 中看到，而 POST 请求的数据则包含在请求体中。
   - **幂等性**：GET 请求应该是幂等的，意味着多次执行相同的 GET 请求应该返回相同的结果，而不会改变服务器的状态。POST 请求可以改变服务器的状态，例如，通过提交表单来添加或修改数据。

2. **WebSockets：**
   - **使用场景**：WebSockets 是一种不同于 HTTP 的协议，支持在客户端和服务器之间建立一个持久的、全双工的通信通道。这意味着服务器可以直接向客户端发送消息，而不需要客户端先发送请求。
   - **数据传输**：WebSockets 允许数据在一个持续开放的连接上双向传输，适用于需要实时数据更新的应用，如在线游戏、聊天应用等。
   - **性能**：由于 WebSockets 减少了建立连接的开销（握手之后可以保持连接开放），对于实时通信来说，它比轮询（客户端定期发送 HTTP 请求以获取更新）更高效。
   - **兼容性**：虽然现代浏览器普遍支持 WebSockets，但在某些受限环境下（如某些企业防火墙），WebSocket 连接可能会被阻塞。

总结来说，GET 和 POST 是构建 Web 应用时用于单向通信的基本工具，而 WebSockets 提供了一种高效的方式来实现服务器和客户端之间的实时、双向通信。使用 Sanic 时，你可以根据应用的具体需求选择合适的通信机制。<br>

关于 **"服务器可以直接向客户端发送消息，而不需要客户端先发送请求。"** 的解释:<br>

这句话的意思是，在使用 WebSockets 时，服务器有能力主动向客户端发送信息，而不是传统的 HTTP 请求模式（比如 GET 和 POST），在这种模式下，只有客户端能发起请求，服务器只能响应客户端的请求。<br>

在 GET 或 POST 请求中，交互流程通常是这样的：<br>

1. 客户端向服务器发送一个请求（无论是请求数据还是提交数据）。
2. 服务器接收到请求后，处理这个请求，并将结果返回给客户端。

这种模式被称为“请求-响应模式”，客户端必须先发起请求，服务器才能响应。这种通信是单向的，即服务器不能主动发送信息给客户端，它必须等待客户端的请求。<br>

而 WebSockets 协议则提供了一种“全双工”通信方式，意味着一旦建立了 WebSocket 连接，客户端和服务器就可以在这个连接上自由地、实时地互相发送数据，不需要请求-响应模式。这就允许了如下的交互流程：<br>

1. 客户端与服务器通过握手建立 WebSocket 连接。
2. 一旦连接建立，服务器可以在任何时候主动发送数据给客户端，无需等待客户端的请求。同样，客户端也可以随时发送数据给服务器。
3. 这个连接会保持开放状态，直到客户端或服务器决定关闭它。

这种机制特别适合需要实时数据更新的应用，例如在线聊天应用、多玩家在线游戏、实时交易平台等，因为它们需要服务器能够实时、主动地推送更新给客户端，而不是依赖客户端定期发起请求来检查更新。使用 WebSockets，可以减少网络延迟，提高应用的响应速度和交互体验。<br>


### Websockets介绍:

Sanic provides an easy to use abstraction on top of [websockets](https://websockets.readthedocs.io/en/stable/).<br>

Sanic 在 WebSockets 上提供了一个易于使用的抽象层。<br>

### Routing(路由):

Websocket handlers can be hooked up to the router similar to regular handlers.<br>

> "hooked" 在这个上下文中的意思是将某物连接或附着到另一物上。在软件开发和编程中，"hooked up" 常用来描述将一个组件、模块、函数或处理程序与系统的其他部分相连接或集成的过程。所以，在提到 WebSocket 处理程序可以被 "hooked up" 到路由器上时，意思是 WebSocket 处理程序可以被设置或配置为与路由器相连，从而使它们能够处理通过路由器转发的 WebSocket 请求。

WebSocket 处理程序可以像常规处理程序一样挂接到路由器上。<br>

下列两份代码实现了相同的功能，都是在使用 Sanic 框架为 WebSocket 创建路由。它们定义了一个名为 `feed` 的异步函数，这个函数接收一个 `Request` 对象和一个 `Websocket` 对象作为参数。不过，它们采用了不同的方式来将这个函数与一个 WebSocket 路径 `/feed` 关联起来。<br>

1. 第一份代码直接使用 Sanic 应用对象的 `add_websocket_route` 方法。这种方法显式地将 `feed` 函数和路径 `/feed` 关联起来作为 WebSocket 路由。这是一种更明确、手动的方式来添加 WebSocket 路由。

```python
from sanic import Request, Websocket

async def feed(request: Request, ws: Websocket):
    pass

app.add_websocket_route(feed, "/feed")
```

2. 第二份代码使用了一个装饰器 `@app.websocket("/feed")` 来实现相同的效果。装饰器是 Python 中的一个功能强大的特性，它允许你修改或增强函数的行为。在这里，`@app.websocket("/feed")` 装饰器自动将 `feed` 函数与路径 `/feed` 关联，作为 WebSocket 路由。这种方式更加简洁，并且在视觉上更容易理解函数的用途。

```python
from sanic import Request, Websocket

@app.websocket("/feed")
async def feed(request: Request, ws: Websocket):
    pass
```

总的来说，两种方式都是有效的，选择哪一种主要取决于个人喜好或项目规范。使用装饰器的方式通常代码更简洁、更符合 Python 的风格，而直接使用方法添加路由可能在某些情况下给你更多的控制力和灵活性。<br>

### Handler(处理器):

Typically, a websocket handler will want to hold open a loop.<br>

通常，一个 WebSocket 处理器会希望保持一个循环开启状态。

It can then use the `send()` and `recv()` methods on the second object injected into the handler.<br>

然后，它可以使用注入到处理器中的第二个对象的 `send()` 和 `recv()` 方法。<br>

> 🔥🔥🔥"第二对象" 指的就是 `ws: Websocket`。

This example is a simple endpoint that echos back to the client messages that it receives.<br>

这个例子是一个简单的端点，它将接收到的消息回显给客户端。<br>

```python
from sanic import Request, Websocket

@app.websocket("/feed")
async def feed(request: Request, ws: Websocket):
    while True:
        data = "hello!"
        print("Sending: " + data)
        await ws.send(data)
        data = await ws.recv()
        print("Received: " + data)
```

You can simplify your loop by just iterating over the `Websocket` object in a for loop.<br>

您可以通过在 for 循环中迭代 `Websocket` 对象来简化您的循环。<br>

```python
from sanic import Request, Websocket

@app.websocket("/feed")
async def feed(request: Request, ws: Websocket):
    async for msg in ws:
        await ws.send(msg)
```

### Configuration(配置):

See configuration section for more details, however the defaults are shown below.<br>

详细信息请参见配置部分，不过默认配置如下所示。<br>

```conf
app.config.WEBSOCKET_MAX_SIZE = 2 ** 20
app.config.WEBSOCKET_PING_INTERVAL = 20
app.config.WEBSOCKET_PING_TIMEOUT = 20
```

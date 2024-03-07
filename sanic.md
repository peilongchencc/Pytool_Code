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


请将下列内容翻译为地道的中文：
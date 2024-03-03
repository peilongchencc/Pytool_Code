# asyncio — Asynchronous I/O(异步 I/O)
- [asyncio — Asynchronous I/O(异步 I/O)](#asyncio--asynchronous-io异步-io)
  - [部分代码后台执行，避免程序整体耗时:](#部分代码后台执行避免程序整体耗时)
  - [High-level APIs-Runners:](#high-level-apis-runners)
    - [Running an asyncio Program(运行一个 asyncio 程序):](#running-an-asyncio-program运行一个-asyncio-程序)
    - [Runner context manager(运行器上下文管理器):](#runner-context-manager运行器上下文管理器)
    - [Handling Keyboard Interruption(处理键盘中断):](#handling-keyboard-interruption处理键盘中断)
  - [Coroutines and Tasks(协程与任务):](#coroutines-and-tasks协程与任务)
    - [Coroutines(协程):](#coroutines协程)
  - [asyncio--单线程:](#asyncio--单线程)
  - [进程、线程、协程的关系:](#进程线程协程的关系)
    - [进程：杀毒软件](#进程杀毒软件)
    - [线程：扫描任务](#线程扫描任务)
    - [协程：扫描文件](#协程扫描文件)
    - [总结](#总结)
  - [并发需求是否使用 asyncio 的考量:](#并发需求是否使用-asyncio-的考量)
    - [I/O 密集型 vs CPU 密集型任务](#io-密集型-vs-cpu-密集型任务)
    - [程序的复杂性和团队熟悉度](#程序的复杂性和团队熟悉度)
    - [结论](#结论)

> "asynchronous"是一个形容词，用于描述不同时发生、不同步进行的事件或过程。在计算机科学和编程领域，特别是在讨论I/O（输入/输出）操作或程序执行时，"asynchronous"指的是程序在等待某个长时间操作（如网络请求或文件读写）完成时，能够继续执行其他任务，而不是停下来等待该操作完成。这种方式与同步（synchronous）操作相对，后者在等待过程中会阻塞程序的进一步执行直到操作完成。异步操作能够提高程序的效率和响应性，特别是在处理I/O密集型任务时。

python asyncio 官网链接如下:<br>

```txt
https://docs.python.org/3/library/asyncio.html
```

asyncio is a library to write concurrent code using the `async/await` syntax.<br>

asyncio 是一个使用 `async/await` 语法编写并发代码的库。<br>

```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)  # 等待1s后执行之后的代码
    print('... World!')

if __name__ == "__main__":
    asyncio.run(main())
```

终端显示:<br>

```txt
Hello ...
... World!
```

asyncio is used as a foundation(基础) for multiple Python asynchronous(异步的) frameworks(框架) that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.<br>

asyncio 被用作多个 Python 异步框架的基础，这些框架提供高性能的网络和 web 服务器、数据库连接库、分布式任务队列等。<br>

asyncio is often a perfect fit for IO-bound and high-level structured network code.<br>

asyncio 经常非常适合于 I/O 绑定和高级结构化的网络代码。<br>


🔥🔥🔥asyncio provides a set of **high-level** APIs to(asyncio 提供了一套高级 API，用于):<br>

- run Python coroutines(协程) concurrently(同时的；并发的) and have full control over their execution(并发运行 Python 协程并完全控制它们的执行);

- perform(执行) network IO and IPC(执行网络 I/O 和 IPC);

- control subprocesses(控制子进程);

- distribute(分发；分配) tasks via queues(通过队列分配任务);

- synchronize concurrent code(同步并发代码);


💦💦💦Additionally, there are **low-level** APIs for library and framework developers to(此外，还有低级 API 供库和框架开发者使用，以):<br>

- create and manage event loops, which provide asynchronous APIs for networking, running subprocesses, handling OS signals, etc(创建和管理事件循环，这些事件循环为网络通信、运行子进程、处理操作系统信号等提供异步 API);

- implement efficient protocols using transports(使用传输实现高效的协议);

- bridge callback-based libraries and code with async/await syntax(将基于回调的库和代码与 async/await 语法桥接).


🌿🌿🌿如果你是一个 asyncio 的初学者，建议你首先关注 asyncio 的 high-level APIs。这些 high-level APIs 提供了更简单、更易用的接口，可以让你更轻松地编写异步代码，而不必深入了解底层的实现细节。<br>

通过使用 high-level APIs，你可以利用 `async/await` 语法编写异步函数，使用诸如 `asyncio.run()`、`asyncio.create_task()`、`asyncio.gather()` 等函数来管理异步任务的执行和协作。这些 API 使得编写异步代码更加直观和简单，同时也能够满足许多常见的异步编程需求。<br>

一旦你对 asyncio 的基本概念和高级API有了一定的了解之后，再深入学习 low-level APIs 可以帮助你更好地理解 asyncio 的内部工作机制，并且在需要更高度自定义的情况下提供更多的灵活性。但在开始阶段，专注于掌握 high-level APIs 将有助于你更快地上手和理解异步编程的基本概念。<br>


You can experiment with an `asyncio` concurrent context in the REPL(你可以在 REPL 中尝试一个 `asyncio` 并发上下文):

拓展-"REPL"是什么:<br>

```txt
"REPL" 是 "Read-Eval-Print Loop" 的缩写，它是一种简单的、交互式的编程环境。用户可以在REPL中输入单个语句或表达式，环境会读取（Read）这些输入，执行（Eval）它们，然后打印（Print）结果给用户，最后循环（Loop）回到读取步骤等待新的输入。这种交互模式特别适合快速测试代码片段、学习新的编程语言特性或进行探索性编程。
```

原代码:<br>

```bash
$ python -m asyncio
asyncio REPL ...
Use "await" directly instead of "asyncio.run()".(使用 "await" 直接代替 "asyncio.run()"。)
Type "help", "copyright", "credits" or "license" for more information.(输入 "help", "copyright", "credits" 或 "license" 了解更多信息。)
>>> import asyncio
>>> await asyncio.sleep(10, result='hello')
'hello'
```

Availability: not Emscripten, not WASI.<br>

可用性：不适用于 Emscripten，不适用于 WASI。

This module does not work or is not available on WebAssembly platforms `wasm32-emscripten` and `wasm32-wasi`. See WebAssembly platforms for more information.<br>

此模块在 WebAssembly 平台 `wasm32-emscripten` 和 `wasm32-wasi` 上不工作或不可用。有关更多信息，请参阅 WebAssembly 平台。<br>

```python
import asyncio

async def main():
    result = await asyncio.sleep(2, result='hello')
    print(result)

if __name__ == "__main__":
    # 使用asyncio.run()来运行异步函数
    asyncio.run(main())

```

`asyncio.sleep` 函数是非阻塞的，它让出控制权给事件循环，使得事件循环可以继续执行其他任务。`result='hello'` 参数的作用是，在等待结束后，`asyncio.sleep` 会返回 'hello' 字符串作为结果。<br>

使用 `await` 关键字可以挂起当前任务，等到 `asyncio.sleep` 完成后，再继续执行后面的代码。这里，当 `asyncio.sleep(2, result='hello')` 完成后，其返回值（'hello'）被打印出来。<br>


## 部分代码后台执行，避免程序整体耗时:

假设您想将某些操作（如向MySQL写入大量数据）转移到后台执行，并且不希望阻塞当前的异步函数执行流，您可以使用asyncio库中的create_task函数。<br>

这个函数可以将一个协程对象封装成一个Task对象并立即返回，该Task对象将在事件循环中异步执行，从而实现非阻塞的并发执行。<br>

以下列代码为例，当程序运行到 `task = asyncio.create_task(write_to_mysql())` 后，会把这部分程序转移到后台，继续执行之后的内容，终端直接输出 `写入操作已转移到后台，继续执行其他任务。`。<br>

由于我的 `write_to_mysql` 和 `执行其他任务` 的操作耗时都是5s，所以在5s后程序会几乎在同一时刻输出下列内容:<br>

```txt
执行其他任务完成。
数据写入完成
后台写入操作完成。
```

```python
import asyncio

async def write_to_mysql():
    # 假设这是一个异步的向MySQL写入数据的函数
    # 这里使用 asyncio.sleep 来模拟异步操作
    await asyncio.sleep(5)  # 模拟数据库操作耗时
    print("数据写入完成")

async def main():
    # 创建一个任务，将写入操作转移到后台执行
    task = asyncio.create_task(write_to_mysql())

    # 可以继续执行其他操作，不需要等待写入完成
    print("写入操作已转移到后台，继续执行其他任务。")

    # 这里可以执行其他不依赖于写入操作的代码
    # 例如，处理其他逻辑或者等待其他异步操作完成
    await asyncio.sleep(5)
    print("执行其他任务完成。")

    # 如果需要用到写入mysql操作后的返回值，可以在某个点等待后台任务完成。如果不需要写入mysql操作后的返回值，可以将下列2行代码注释。
    await task
    print("后台写入操作完成。")

if __name__ == "__main__":
    asyncio.run(main())
```

上述代码的关键是: 在main函数中，我们使用 `asyncio.create_task(write_to_mysql())` 创建了一个任务，这个任务立即在后台开始执行，允许main函数继续执行后续代码而不必等待write_to_mysql完成。<br>


## High-level APIs-Runners:

Source code: `Lib/asyncio/runners.py` <br>

This section outlines(概述；概要) high-level asyncio primitives(原始的；最基本构建模块) to run asyncio code.<br>

本节概述了运行 asyncio 代码的 high-level asyncio 模块。<br>

They are built on top of an [event loop](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop) with the aim to simplify async code usage for common wide-spread(广泛分布的；spread-分布；扩散) scenarios(场景).<br>

> `event loop` 是底层API，笔者这里不多介绍，读者可自行去python官网学习。

它们是建立在事件循环( `event loop` )之上的，目的是为了简化常见广泛场景下异步代码的使用。<br>

### Running an asyncio Program(运行一个 asyncio 程序):

`asyncio.run(coro, *, debug=None, loop_factory=None)` :<br>

- coro是你想要运行的协程对象。
- debug是一个可选的布尔值，用于设置事件循环的调试模式。如果debug为 `True` ，则事件循环将以调试模式运行。`False` 明确禁用调试模式。None用于遵循全局调试模式设置。
- loop_factory是一个可选的参数，允许用户提供一个自定义的事件循环工厂（即一个无参数的可调用对象，返回一个 asyncio.AbstractEventLoop的实例）。

在大多数情况下，你不需要手动设置 `loop_factory` ，因为 `asyncio.run` 已经为你创建了一个事件循环，并且在协程完成执行后关闭它。 `loop_factory` 的使用场景比较少见，主要用于那些需要自定义事件循环行为的高级用例。<br>

This function( `asyncio.run` ) should be used as a main entry point for asyncio programs, and should ideally(理想的) only be called once. It is recommended to use `loop_factory` to configure the event loop instead of policies.<br>

这个函数( `asyncio.run` )应该作为 `asyncio` 程序的主入口点，并且理想情况下应该只被调用一次。建议使用 `loop_factory` 来配置事件循环，而不是策略。<br>

The executor is given a timeout duration(持续时间；期间) of 5 minutes to shutdown. If the executor hasn’t finished within that duration, a warning is emitted(释放；发出；散发) and the executor is closed.<br>

执行器被给予5分钟的超时时间来关闭。如果执行器在该时间段内没有完成，将发出警告并关闭执行器。<br>

Example:<br>

```python
async def main():
    await asyncio.sleep(1)
    print('hello')

if __name__ == "__main__":
    asyncio.run(main())
```

### Runner context manager(运行器上下文管理器):

暂时用不到，不记录。<br>

### Handling Keyboard Interruption(处理键盘中断):

暂时用不到，不记录。<br>


## Coroutines and Tasks(协程与任务):

This section outlines(概述) high-level asyncio APIs to work with coroutines and Tasks.<br>

本节概述了用于处理协程和任务的高级 asyncio API。<br>

### Coroutines(协程):

Source code: `Lib/asyncio/coroutines.py` <br>

Coroutines declared(声明) with the `async/await` syntax is the preferred way of writing asyncio applications. <br>

用 `async/await` 语法声明的协程是编写 asyncio 应用的首选方式。<br>

For example, the following snippet of code prints “hello”, waits 1 second, and then prints “world”:<br>

例如，下面的代码片段会打印“hello”，等待1秒钟，然后打印“world”：<br>

```python
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

if __name__ == "__main__":
    asyncio.run(main())
```

终端输出:<br>

```txt
hello
world
```

Note that simply calling a coroutine will not schedule it to be executed:<br>

注意，仅仅调用一个协程并不会安排它执行：<br>

```bash
>>> main()
<coroutine object main at 0x1053bb7c8>
```

To actually run a coroutine, asyncio provides the following mechanisms(机制):<br>

为了真正运行一个协程，asyncio 提供了以下机制：<br>

- The `asyncio.run()` function to run the top-level entry point “main()” function (see the above example.)(函数 asyncio.run() 用于运行最顶层的入口点“main()”函数（见上面的示例）)<br>

Awaiting on a coroutine. The following snippet of code will print “hello” after waiting for 1 second, and then print “world” after waiting for another 2 seconds:<br>

等待一个协程。下面的代码片段将在等待1秒后打印“hello”，然后在等待另外2秒后打印“world”：<br>

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main())
```

终端输出:<br>

```txt
started at 16:47:07
hello
world
finished at 16:47:10
```

从结果中我们可以看到，2个时间节点之间的差距一共是3秒，刚好是我们预设的时间。<br>

- The `asyncio.create_task()` function to run coroutines(协程) concurrently(同时的) as asyncio Tasks.(`asyncio.create_task()`函数用于将协程并发运行，同时作为 asyncio 任务。)

Let’s modify the above example and run two `say_after` coroutines concurrently:<br>

让我们修改上述示例，然后并发运行两个 `say_after` 协程：<br>

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
    
if __name__ == "__main__":
    asyncio.run(main())
```

🤭🤭🤭Note that expected output now shows that the snippet runs 1 second faster than before:<br>

🤭🤭🤭请注意，预期输出现在显示该代码段的运行时间比之前快了1秒：<br>

终端输出:<br>

```txt
started at 17:03:40
hello
world
finished at 17:03:42
```

结论，两个协程都放到了 **后台运行** ，不影响程序的其他内容。在等待时，最慢的协程是2s，所以一共的耗时是2s。<br>

如果你后续的代码中需要这2个协程的返回值，可以参考以下写法，这2个协程还是会放到后台运行，只是优先执行完了程序。<br>

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    # await task1
    # await task2

    print(f"finished at {time.strftime('%X')}")
    
if __name__ == "__main__":
    asyncio.run(main())
```

终端输出:<br>

```txt
started at 17:07:48
finished at 17:07:48
```

可以看到，程序开始和结束时间一致，主程序并没有体现出协程的时间，这就是 `create_task()` 的优势所在。<br>

🚨🚨🚨注意: `asyncio.TaskGroup` 从 python 3.11 才开始引入，注意你自己的python版本。<br>

The `asyncio.TaskGroup` class provides a more modern alternative to `create_task()`. Using this API, the last example becomes:<br>

`asyncio.TaskGroup` 类提供了一个比 `create_task()` 更现代的选择。使用这个API，最后的例子变成了：<br>

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.
    # 当上下文管理器退出时，等待操作是隐式进行的。

    print(f"finished at {time.strftime('%X')}")
```


## asyncio--单线程:

`asyncio`通常在单个线程中执行。`asyncio`是Python的一个用于写并发代码的库，它使用`async`和`await`语法来创建一个事件循环，其中协程可以在单个线程中并发执行。这种方式与多线程或多进程并发执行相比，提供了一种不同的并发模型。<br>

在`asyncio`模型中，协程是通过事件循环进行调度的。事件循环负责管理所有的异步操作，当一个协程等待一个非阻塞操作（如I/O操作）完成时，事件循环会暂停该协程的执行，并转而执行另一个协程，直到原来的操作完成。这种方式允许单个线程在不同的任务之间高效地切换，而不是依赖于操作系统的线程切换，这通常更加高效。<br>

这种并发模型特别适合I/O密集型应用，如网络服务和Web应用，其中大部分时间可能被用于等待网络响应或其他I/O操作。通过使用`asyncio`，这些等待时间可以用来处理其他任务，从而提高程序的整体性能和响应能力。<br>

总的来说，尽管`asyncio`是在单个线程内执行，但它通过协程和事件循环提供了一种有效的并发执行模型，使得可以在保持代码简单性的同时，提高程序的并发能力和I/O效率。<br>


## 进程、线程、协程的关系:

简单理解: 一个进程可以开多个线程，一个线程可以开多个协程。<br>

进程（Process）和 线程（Thread）较早出现，协程是后来出现的。<br>

让我们通过电脑上运行的杀毒软件来说明进程、线程和协程之间的关系。这个例子将帮助你更直观地理解这三个概念如何在实际应用程序中协同工作。<br>

### 进程：杀毒软件

想象你的电脑上安装了一款杀毒软件。这款软件作为一个整体运行在你的电脑上，它是一个独立的进程。这意味着它在操作系统中占有自己的内存空间，与其他运行的程序（比如你的浏览器或文档编辑器）相互独立。这个进程（杀毒软件）负责管理所有与病毒扫描、隔离和删除相关的任务。<br>

### 线程：扫描任务

杀毒软件需要同时执行多项任务，比如实时监控、系统全盘扫描、更新病毒数据库等。这些任务在软件的进程内部通过创建不同的线程来实现。每个线程负责一个特定的任务：<br>

- **线程1**：实时监控线程，持续检查新下载的文件或程序，确保它们没有病毒。
- **线程2**：全盘扫描线程，定期检查电脑上的所有文件，寻找潜在的病毒或恶意软件。
- **线程3**：更新线程，负责定期从互联网下载最新的病毒定义和软件更新。

这些线程共享杀毒软件进程的资源（如内存），但它们可以并行运行，以提高效率和响应速度。<br>

### 协程：扫描文件

在进行全盘扫描时（线程2），软件需要检查数以万计的文件。这项任务可以进一步细分，使用协程来高效地管理：<br>

- 当扫描一个大文件时，软件（通过协程）可以在等待文件读取的同时开始扫描下一个文件。这样做的好处是，即使某些操作因为I/O（输入/输出）操作而阻塞，其他任务仍然可以继续进行，而不是让整个线程空闲等待。

在这个例子中，**协程**允许杀毒软件在单个线程内以更高效、更灵活的方式执行多个任务。通过这种方式，杀毒软件能够最大化利用CPU资源，加快扫描速度，同时保持系统的响应性。<br>

### 总结

通过这个杀毒软件的例子，我们可以看到：

- **进程**是运行杀毒软件的独立环境。

- **线程**是进程中执行特定任务（如实时监控、全盘扫描）的执行单元。

- **协程**是线程内部用于提高任务执行效率的轻量级执行单元，特别适用于I/O密集型任务。

这个例子展示了进程、线程和协程如何在实际应用程序中协同工作，提高了任务执行的效率和程序的整体性能。<br>

说句题外话，对应杀毒软件这个，多进程意味着同时运行多个杀毒软件进程，每个进程都是独立的，并且有自己的内存空间和资源，这在实际应用中不太常见，因为运行多个杀毒软件实例可能导致资源冲突和效率低下。<br>


## 并发需求是否使用 asyncio 的考量:

并发（Concurrency）是编程中的一个概念，指的是多个任务在同一时间段内进行，但不一定同时执行。并发编程允许程序有效地利用有限的计算资源来处理多任务问题。<br>

进程、线程、协程，代码中使用任何一项都属于并发，也可以把他们结合使用达到更高的效率和性能。🚨🚨🚨注意异步是并发的一种形式，多聚焦于处理耗时的操作（如I/O操作），异步多用协程实现，对应python就是使用的 asyncio 。<br>

在很多情况下，使用 `asyncio` 对于处理并发任务确实足够了，尤其是在涉及到 I/O 密集型操作（如网络请求、文件I/O等）的场景中。`asyncio` 提供的异步编程模型能够帮助你写出高效的代码，因为它可以在等待 I/O 操作完成的同时执行其他任务，从而提高程序的整体性能和响应速度。<br>

然而，并不是所有类型的并发问题都最适合用 `asyncio` 来解决。选择正确的并发模型取决于你的具体需求，包括任务的类型（CPU密集型 vs I/O密集型）、程序的复杂性、以及你的个人或团队的熟悉度与偏好。下面是一些考虑因素：<br>

### I/O 密集型 vs CPU 密集型任务

- **I/O 密集型任务**：这类任务的瓶颈主要在于等待外部操作的完成，如网络通信、磁盘读写等。`asyncio` 和其他形式的异步编程非常适合这类场景，因为它们能够让程序在等待这些 I/O 操作时执行其他任务。
- **CPU 密集型任务**：这类任务的瓶颈在于处理器的计算能力。对于CPU密集型任务，使用多线程（在Python中可能因为全局解释器锁GIL的存在而受限）或多进程（通过`multiprocessing`模块）可能更合适，因为这可以让任务分布到多个CPU核心上并行执行。

### 程序的复杂性和团队熟悉度

- **程序复杂性**：`asyncio` 需要使用 `async` 和 `await` 关键字，这可能会增加程序的复杂性，特别是在大型项目或多人协作的环境中。正确地管理异步代码的执行流程和错误处理可能比同步代码更复杂。
- **团队熟悉度**：如果团队对异步编程或 `asyncio` 不够熟悉，可能会增加学习成本和引入错误的风险。在这种情况下，采用更传统的并发模型，如多线程或多进程，可能更为适合。

### 结论

虽然 `asyncio` 在很多场景下都是处理并发的强大工具，特别是对于 I/O 密集型任务，但它不一定适用于所有情况。在决定是否使用 `asyncio` 之前，应该根据具体的任务需求、性能瓶颈以及团队的技能和偏好来综合考虑。在某些情况下，结合使用 `asyncio` 与其他并发模型（如多进程处理CPU密集型任务）可能是最佳选择。<br>

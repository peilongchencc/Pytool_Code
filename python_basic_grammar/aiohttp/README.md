# aiohttp

`aiohttp` 默认不会自动从环境变量中获取代理设置。如果你需要使用代理，你通常需要在创建 `aiohttp` 的 `ClientSession` 对象时手动指定代理。这可以通过设置 `proxy` 参数来实现。下面是如何设置代理的一个基本示例：<br>

```python
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxy="http://your.proxy.server:port") as response:
            return await response.text()

# 使用fetch函数获取网页内容
```

在这个示例中，`proxy` 参数就是你的代理服务器的URL。<br>

如果你确实想要让 `aiohttp` 自动从环境变量中读取代理设置，你需要在代码中自己实现这一逻辑。可以通过读取环境变量，然后将其作为参数传递给 `ClientSession`。例如，使用标准库 `os` 来获取环境变量：<br>

```python
import aiohttp
import os
from dotenv import load_dotenv

# 将配置项加载到环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

async def fetch(url):
    # 从环境变量获取代理设置
    http_proxy = os.getenv("HTTP_PROXY")
    https_proxy = os.getenv("HTTPS_PROXY")

    # 根据URL的协议选择合适的代理
    proxy = https_proxy if url.startswith("https") else http_proxy

    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxy=proxy) as response:
            return await response.text()

# 使用fetch函数获取网页内容
```

这样，你的 `aiohttp` 请求就可以根据环境变量中的设置使用适当的代理服务器了。<br>
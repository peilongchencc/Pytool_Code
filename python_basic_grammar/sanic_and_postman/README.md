# Sanic and Postman

Sanic 是一个用于构建异步（asynchronous）Web应用的Python框架，它基于 Python 3.5+ 引入的 `async/await` 语法，旨在提供高性能的 Web 服务器和路由处理功能。它的设计灵感来自于 Flask，但强调了异步处理，适用于高并发的应用。<br>

## Sanic的安装

pip 安装sanic的指令如下：<br>

```bash
pip install sanic
```

## 简单sanic应用示例：

下面是一个简单的介绍，说明如何使用 Sanic 构建一个基本的 Web 应用：<br>

1. 创建一个 Sanic 应用:

创建一个 Python 文件，例如 `sanic_server.py`(文件名可以随意定义)，并导入 Sanic：<br>

```python
from sanic import Sanic
from sanic import response

app = Sanic(__name__)
```

2. 添加路由和处理函数:

在你的应用中，你可以定义不同的路由，并为每个路由定义处理函数。例如：<br>

```python
@app.route("/")
async def index(request):
    return response.text("Hello, Sanic!")

@app.route("/user/<name>")
async def greet_user(request, name):
    return response.text(f"Hello, {name}!")
```

这里，`@app.route` 装饰器用于指定路由，接受 HTTP 请求，并调用相应的处理函数。<br>

3. 启动 Sanic 应用:

在应用的最后，添加以下代码以运行 Sanic 服务器：<br>

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

4. 运行应用:

使用以下命令运行你的应用：<br>

```bash
python sanic_server.py
```

现在，你的 Sanic 应用应该已经在本地运行，并监听在端口 8000 上。<br>

这只是 Sanic 的基本用法，它还提供了许多其他功能，如中间件支持、异步请求处理、WebSocket 支持等等，以满足不同类型的 Web 应用需求。你可以查阅官方文档以深入了解更多信息：https://sanicframework.org/<br>

## 使用postman测试sanic启动的服务：

Postman 是一种流行的应用程序，用于测试和调试网络 API（应用程序编程接口）。它提供了一个用户友好的界面，允许开发人员轻松地创建、发送和接收 HTTP 请求，以测试 API 的各种端点和功能。Postman 还允许您组织请求、保存和分享测试集合，以及自动化 API 测试工作流程。它可用于多种用途，包括单元测试、端到端测试、性能测试和文档编制等。<br>

工作中经常使用 Postman 测试 Sanic 用于构建 Web 应用程序和 API。使用 Postman 进行单个测试，或者使用 Postman 的自动化功能来创建 API 文档和测试集合。这有助于确保 API 的质量和性能。<br>

🐳🐳🐳下面我们使用以下代码(`sanic_server.py`)介绍如何使用 Postman 测试我们所启动的 Sanic 服务效果如何。<br>

```python
# sanic_server.py
from sanic import Sanic
from sanic import response

app = Sanic(__name__)

@app.route("/")
async def index(request):
    return response.text("Hello, Sanic!")

@app.route("/user/<name>")
async def greet_user(request, name):
    return response.text(f"Hello, {name}!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

要使用Postman测试上述Sanic应用程序，请按照以下步骤操作：<br>

1. 启动Sanic应用程序：
   
在命令行中运行你的Python脚本，以启动Sanic应用程序。这将使应用程序在本地运行并监听端口8000。<br>

```bash
python sanic_server.py
```

2. 打开Postman：
   
打开Postman应用程序或访问Postman网站。<br>

3. 创建一个新的请求：

在Postman主界面中，点击"New"（新建）按钮，然后选择HTTP方法。<br>

4. 配置请求：
   
- 在请求的"Request Type"（请求类型）下拉菜单中，选择HTTP方法，如GET、POST等。上述代码我只使用了GET方法的路由，所以请求类型设置为GET。

- 在"Enter request URL"（输入请求URL）字段中，输入Sanic应用程序的URL。默认情况下，它应该是`http://localhost:8000`，但如果你的应用程序在不同的主机或端口上运行，请相应地更改URL。

- 如果你要测试具有参数的路由，如`/user/<name>`，则需要在URL中包含相应的参数，例如`http://localhost:8000/user/John`。

- 在"Headers"（标头）部分，你可以添加任何必要的标头。**通常情况下，不需要添加任何特殊标头。**😀😀😀

- 如果你使用POST请求，你可以在"Body"（正文）部分设置请求正文。根据你的应用程序，可能需要在正文中包含JSON数据或表单数据。

5. 发送请求：

点击"Send"（发送）按钮以发送请求到Sanic应用程序。<br>

6. 查看响应：

Postman将显示从Sanic应用程序接收到的响应。你应该能够看到你的应用程序返回的数据或消息。<br>

通过按照以上步骤配置和发送请求，你可以使用Postman测试你的Sanic应用程序的不同路由和功能。确保你的Sanic应用程序正在运行，并且Postman配置正确以便与其通信。<br>


## GET和POST方法：

笔者在上面的示例中定义的两个路由默认都是使用 GET 方法。


如果你想要定义一个使用 POST 方法的路由，可以通过使用 `methods` 参数来指定请求方法，如下所示：

```python
from sanic import Sanic
from sanic import response

app = Sanic(__name__)

# 使用 GET 方法的路由
@app.route("/")
async def index(request):
    return response.text("Hello, Sanic!")

# 使用 POST 方法的路由
@app.route("/submit", methods=["POST"])
async def submit(request):
    # 在这里处理 POST 请求
    data = request.json  # 假设请求中包含 JSON 数据
    return response.json({"message": "Data received successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

在上面的示例中，`@app.route("/submit", methods=["POST"])` 指定了一个使用 POST 方法的路由。你可以在路由处理函数内部处理 POST 请求的数据，这里使用了 `request.json` 来获取 JSON 数据。你可以根据需要处理不同的请求方法，例如 GET、POST、PUT、DELETE 等。

要测试这个路由，你可以使用工具如 `curl` 或 Postman 发送 POST 请求，或者编写一个发送 POST 请求的客户端脚本。


## response

`from sanic import response` 是 Sanic 框架提供的一个模块，它包含了一些用于构建 HTTP 响应的实用函数。这个模块使得返回不同类型的响应变得更加简单。其中，`response.json` 是其中一个非常常用的函数，它用于构建 JSON 格式的 HTTP 响应。

以下是一些常见用法和示例：

1. 返回 JSON 响应：

   使用 `response.json` 函数，您可以将 Python 字典或对象转换为 JSON 格式的响应并返回给客户端。示例：

   ```python
   from sanic import Sanic
   from sanic import response

   app = Sanic(__name__)

   @app.route("/json")
   async def json_example(request):
       data = {"message": "Hello, Sanic!"}
       return response.json(data)
   ```

   这将返回一个 JSON 响应，其内容为 `{"message": "Hello, Sanic!"}`。

2. 返回文本响应：

   使用 `response.text` 函数，您可以返回普通文本响应。示例：

   ```python
   @app.route("/text")
   async def text_example(request):
       return response.text("This is a text response.")
   ```

   这将返回一个包含指定文本的响应。

3. 返回 HTML 响应：

   使用 `response.html` 函数，您可以返回包含 HTML 内容的响应。示例：

   ```python
   @app.route("/html")
   async def html_example(request):
       html_content = "<html><body><h1>Hello, Sanic!</h1></body></html>"
       return response.html(html_content)
   ```

   这将返回一个包含指定 HTML 内容的响应。

总之，`response` 模块提供了一些方便的函数，用于构建不同类型的 HTTP 响应，包括 JSON、文本、HTML 等。您可以根据您的需求使用这些函数来构建和返回适当类型的响应给客户端。
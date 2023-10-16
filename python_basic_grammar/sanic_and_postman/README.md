# Sanic and Postman

Sanic 是一个用于构建异步（asynchronous）Web应用的Python框架，它基于 Python 3.5+ 引入的 `async/await` 语法，旨在提供高性能的 Web 服务器和路由处理功能。它的设计灵感来自于 Flask，但强调了异步处理，适用于高并发的应用。<br>

- [Sanic and Postman](#sanic-and-postman)
  - [Sanic的安装](#sanic的安装)
  - [简单sanic应用示例：](#简单sanic应用示例)
  - [使用postman测试sanic启动的服务：](#使用postman测试sanic启动的服务)
  - [GET和POST方法：](#get和post方法)
    - [GET 方法进阶：](#get-方法进阶)
    - [POST 方法：](#post-方法)
    - [POST 方法路由的测试：](#post-方法路由的测试)
  - [request 对象：](#request-对象)
  - [response 对象：](#response-对象)

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

Postman 是一种流行的应用程序，用于测试和调试网络 API（应用程序编程接口）。它提供了一个用户友好的界面，允许开发人员轻松地创建、发送和接收 HTTP 请求，以测试 API 的各种端点和功能。Postman 还允许你组织请求、保存和分享测试集合，以及自动化 API 测试工作流程。它可用于多种用途，包括单元测试、端到端测试、性能测试和文档编制等。<br>

工作中经常使用 Postman 测试 Sanic 用于构建 Web 应用程序和 API。使用 Postman 进行单个测试，或者使用 Postman 的自动化功能来创建 API 文档和测试集合。这有助于确保 API 的质量和性能。<br>

Postman 主界面介绍如下：<br>

![Postman主界面](./postman主界面标识.png)

🐳🐳🐳下面我们使用以下代码(`sanic_server.py`)介绍如何使用 Postman 测试我们所启动的 Sanic 服务效果如何。<br>

```python
# sanic_server.py
from sanic import Sanic
from sanic import response

app = Sanic(__name__)

@app.route("/")
async def index(request):
    """该路由为GET方法
    postman选择GET方法，在url填入http://8.140.203.xxx:8848/的网址，点击Send即可查看效果。(不需要额外选择参数。)
    """
    return response.text("Hello, Sanic!")

@app.route("/user/<name>")
async def greet_user(request, name):
    """该路由为GET方法
    这个路由包含了一个动态参数 `<name>`，这个参数可以在 URL 中接受用户提供的值。例如，当用户访问类似 http://8.140.203.xxx:8848/user/John 的URL时，会执行 `greet_user` 函数，并将 `name` 参数设置为 "John"，然后返回 "Hello, John!" 的文本响应。
    """
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

### GET 方法进阶：

笔者在上面的示例中定义的两个路由默认都是使用 GET 方法。GET 方法的使用较为简单，但在使用 GET 方法时依旧要注意一些内容：<br>

GET 方法不一定需要传递参数，因为它可以在URL中包含查询字符串（query string）来传递参数。查询字符串是URL中的一部分，通常跟在问号（?）之后，参数之间用“&”符号分隔。例如：<br>

```log
http://example.com/resource?param1=value1&param2=value2
```

在这个URL中，`param1` 和 `param2` 是两个GET请求的参数，它们的值分别是`value1`和`value2`。<br>

在Sanic中，你可以使用`request.args`来获取URL中的查询参数。例如：<br>

```python
from sanic import Sanic
from sanic import response

app = Sanic(__name__)

@app.route("/example")
async def example(request):
    param1 = request.args.get("param1")
    param2 = request.args.get("param2")
    
    return response.text(f"param1: {param1}, param2: {param2}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

当你访问 `http://localhost:8000/example?param1=value1&param2=value2` 时，Sanic 将从查询字符串中提取参数值，并将它们传递给路由处理函数。然后，你可以在函数内部使用这些参数来执行逻辑操作。<br>

总结一下，GET 方法通常用于从服务器获取数据，参数可以通过查询字符串传递给服务器，然后服务器可以解析查询字符串来获取这些参数的值。 Sanic 的 `request.args` 可以帮助你在路由处理函数中方便地获取这些参数。<br>

### POST 方法：

如果你想要定义一个使用 POST 方法的路由，可以通过使用 `methods` 参数来指定请求方法，如下所示：<br>

```python
from sanic import Sanic
from sanic import response
import jieba

app = Sanic(__name__)

# 使用 GET 方法的路由
@app.route("/")
async def index(request):
    return response.text("Hello, Sanic!")

@app.route("/segment", methods=["POST"])
async def segment(request):
    """分词API"""
    text = request.json.get("text")
    if not text:
        return response.json({"error": "Missing 'text' parameter"}, status=400)

    result = jieba.lcut(text)
    return response.json({"分词结果为：": result})

@app.route("/ans", methods=["POST"])
async def test(request):
    # 获取用户数据
    text = request.form.get("usr_input")
    if not text:
        return response.json({"error": "Missing 'usr_input' parameter"}, status=400)

    result = jieba.lcut(text)
    return response.json({"用户数据分词结果为：": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8848)
```

🚀🚀🚀接下来，我讲解下上述代码中路由"/segment"和"/ans"的不同，以及应该如何用postman测试：<br>

"/segment"和"/ans"两个路由有以下不同点：<br>

1. **路由路径**：
   - "/segment"路由用于处理POST请求，其路径为"/segment"。
   - "/ans"路由也用于处理POST请求，其路径为"/ans"。

2. **请求参数的获取方式**：
   - "/segment"路由使用`request.json.get("text")`来获取请求中的**JSON数据**，并期望数据包含一个名为"text"的字段。
   - "/ans"路由使用`request.form.get("usr_input")`来获取**表单数据**，并期望数据包含一个名为"usr_input"的字段。

3. **响应**：
   - "/segment"路由返回一个JSON响应，其中包含分词的结果。
   - "/ans"路由也返回一个JSON响应，其中包含分词的结果。

### POST 方法路由的测试：

要使用Postman测试"/segment"和"/ans"这两个路由，可以按照以下步骤进行：<br>

1. 打开Postman应用程序。

2. 创建一个新的请求。

3. 在请求的URL栏中输入你的应用程序的地址和端口，例如：http://localhost:8848。

4. 选择HTTP方法为"POST"。

5. 对于"/segment"路由，切换到"Body"选项卡，选择"raw"，然后在文本框中输入JSON数据，如下所示：

```json
{
    "text": "这是一段文本，需要进行分词。"
}
```

6. 点击发送按钮，你将获得分词结果的JSON响应。

7. 对于"/ans"路由，切换到"Body"选项卡，选择"x-www-form-urlencoded"，然后在"Key"中添加一个名为"usr_input"的字段，并在Value中输入文本，如下所示：

```log
usr_input: 这是一段用户数据，需要进行分词。
```

8. 点击发送按钮，你将获得用户数据分词结果的JSON响应。

这样，你可以使用Postman测试这两个不同的路由并查看它们的不同功能。一个路由期望JSON数据，而另一个期望表单数据。<br>

## request 对象：

**request**包含了客户端（浏览器）发过来的HTTP请求的各类数据。request不需要显示导入，Sanic内部含有。request 包含以下属性：<br>

| 属性   | 使用方式        | 意义                                        |
|--------|-----------------|---------------------------------------------|
| json   | request.json | 当客户端POST来的数据是json格式时，访问json数据 |
| args   | request.args | 查询字符串变量，即URL中问号?后面的部分        |
| files  | 字典            | 拥有name、body和type的文件对象的字典           |
| form   | 表单            | 以POST方式传递的form变量                     |
| body   | 字节串          | POST的原始数据                               |  


## response 对象：

`from sanic import response` 是 Sanic 框架提供的一个模块，它包含了一些用于构建 HTTP 响应的实用函数。这个模块使得返回不同类型的响应变得更加简单。其中，`response.json` 是其中一个非常常用的函数，它用于构建 JSON 格式的 HTTP 响应。<br>

以下是一些常见用法和示例：<br>

1. 返回 JSON 响应：

使用 `response.json` 函数，你可以将 Python 字典或对象转换为 JSON 格式的响应并返回给客户端。示例：<br>

```python
from sanic import Sanic
from sanic import response

app = Sanic(__name__)

@app.route("/json")
async def json_example(request):
    data = {"message": "Hello, Sanic!"}
    return response.json(data)
```

这将返回一个 JSON 响应，其内容为 `{"message": "Hello, Sanic!"}`。<br>

2. 返回文本响应：

使用 `response.text` 函数，你可以返回普通文本响应。示例：<br>

```python
@app.route("/text")
async def text_example(request):
    return response.text("This is a text response.")
```

这将返回一个包含指定文本的响应。<br>

3. 返回 HTML 响应：

使用 `response.html` 函数，你可以返回包含 HTML 内容的响应。示例：<br>

```python
@app.route("/html")
async def html_example(request):
    html_content = "<html><body><h1>Hello, Sanic!</h1></body></html>"
    return response.html(html_content)
```

这将返回一个包含指定 HTML 内容的响应。<br>

总之，`response` 模块提供了一些方便的函数，用于构建不同类型的 HTTP 响应，包括 JSON、文本、HTML 等。你可以根据你的需求使用这些函数来构建和返回适当类型的响应给客户端。<br>
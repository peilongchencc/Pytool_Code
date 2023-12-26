# 千帆大模型API调用
- [千帆大模型API调用](#千帆大模型api调用)
  - [代码示例:](#代码示例)
  - [代码解释:](#代码解释)
    - [导入模块和初始化:](#导入模块和初始化)
    - [API密钥和获取Access Token:](#api密钥和获取access-token)
    - [聊天接口地址:](#聊天接口地址)
    - [用户聊天历史存储:](#用户聊天历史存储)
    - [路由和视图函数:](#路由和视图函数)
    - [处理聊天:](#处理聊天)
    - [启动服务器:](#启动服务器)
  - [拓展-`sanic`中有用于渲染HTML模板的吗？](#拓展-sanic中有用于渲染html模板的吗)
  - [jsonify的作用:](#jsonify的作用)

## 代码示例:

```python
from flask import Flask, render_template, request, jsonify, make_response
import requests
import uuid
from loguru import logger

app = Flask(__name__)

# 使用loguru设置日志
logger.add("baidu_llm.log", rotation="1 GB", backtrace=True, diagnose=True, format="{time} {level} {message}", append=True)
logger.remove() # 移除默认的控制台日志输出

# - `"baidu_llm.log"`: 这指定了日志文件的名称。日志消息将被写入到这个文件中。
# - `rotation="1 GB"`: 这设置了文件轮转的条件。在这里，它意味着每当日志文件达到1GB时，将创建一个新的日志文件，旧的日志文件将被保存。
# - `backtrace=True`: 当异常发生时，这会使得`loguru`记录异常的回溯信息，这有助于调试。
# - `diagnose=True`: 这会记录更多的诊断信息，比如变量的值等，以帮助理解导致错误的原因。
# - `format="{time} {level} {message}"`: 这定义了日志消息的格式。每条日志都将包含时间戳、日志级别和日志消息。
# - `append=True`: 这确保日志消息会被追加到指定的文件中，而不是每次运行脚本时都覆盖文件。
# - `logger.remove()`: `logger`默认会将所有消息输出到终端。这行代码移除了所有的默认处理程序，这意味着会按照上一行中已经添加了文件处理程序，所以日志将只记录到文件中。

# 替换成你的API Key和Secret Key
API_KEY = "你的APIKey"  # 填入平台申请的实际APIKey
SECRET_KEY = "你的SecretKey"  # 填入平台申请的实际SecretKey

# 初始化ACCESS_TOKEN
ACCESS_TOKEN = None

# 获取access_token的函数
def get_access_token():
    token_url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={SECRET_KEY}"
    try:
        response = requests.get(token_url)
        response.raise_for_status()
        return response.json()["access_token"]
    except requests.exceptions.RequestException as e:
        logger.error(f"获取access_token失败: {e}")
        return None

# 获取access_token
ACCESS_TOKEN = get_access_token()

# 定义ERNIE-Bot聊天接口地址
CHAT_API_URL = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token={ACCESS_TOKEN}"
user_chat_histories = {}  # 用于存储不同用户的聊天历史

@app.route("/")  # 定义根路由
def index():
    sessionid = str(uuid.uuid4())[:16]  # 生成一个会话ID
    resp = make_response(render_template("index.html"))  # 渲染HTML页面
    resp.set_cookie("sessionid", sessionid)  # 在响应中设置会话ID的cookie
    return resp

@app.route("/chat", methods=["POST"])  # 定义处理聊天请求的路由
def chat_with_ernie_bot():
    try:
        user_id = request.cookies.get("sessionid")  # 从请求中获取用户ID
        user_input = request.json.get("user_input")  # 获取用户输入
        if not user_input:
            raise ValueError("用户输入为空")

        user_history = user_chat_histories.get(user_id, [])  # 获取该用户的对话历史
        user_history.append({"role": "user", "content": user_input})  # 将用户输入添加到历史记录中
        headers = {"Content-Type": "application/json"}  # 设置请求头
        # 创建请求数据,包括所有历史消息。`data`变量代表了要发送给API的请求体(body)
        data = {
            "messages": user_history,  # 包括所有历史消息
            # 添加其他可能需要的参数,其他数据都为非必填项,如 max_tokens, stop, temperature 等
            }
        """
        `messages`(聊天上下文信息)参数说明：
        (1)messages成员不能为空,1个成员表示单轮对话,多个成员表示多轮对话
        (2)最后一个message为当前请求的信息,前面的message为历史对话信息
        (3)必须为奇数个成员,成员中message的role必须依次为user、assistant
        (4)最后一个message的content长度(即此轮对话的问题)不能超过4800个字符,且不能超过2000 tokens
        (5)如果messages中content总长度大于4800个字符或2000 tokens,系统会依次遗忘最早的历史会话,直到content的总长度不超过4800个字符且不超过2000 tokens
        
        body参数详情见 https://cloud.baidu.com/doc/WENXINWORKSHOP/s/clntwmv7t
        """
        response = requests.post(CHAT_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()["result"]  # 从响应中提取结果
        logger.info(f"API响应: {result}")

        user_history.append({"role": "assistant", "content": result})  # 将结果添加到历史记录中
        user_chat_histories[user_id] = user_history  # 更新该用户的聊天历史
        return jsonify({"response": result})  # 返回JSON响应
    except requests.exceptions.RequestException as e:
        logger.error(f"与API通信时出错: {e}")
        return jsonify({"error": "无法获取响应"}), 500
    except ValueError as e:
        logger.error(f"无效输入: {e}")
        return jsonify({"error": "无效输入"}), 400
    except Exception as e:
        logger.error(f"未预料的错误: {e}")
        return jsonify({"error": "服务器内部错误"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1333, debug=False) # 启动应用
```

## 代码解释:

以上代码是一个使用Flask框架构建的简单Web服务器，旨在与百度的ERNIE-Bot聊天接口进行交互。下面是详细解释：<br>

### 导入模块和初始化:
- **Flask** 是一个用于构建Web应用的轻量级框架。
- **render_template** 用于渲染HTML模板。
- **request** 允许你访问请求数据。
- **jsonify** 用于将数据格式化为JSON响应。
- **make_response** 用于创建响应对象。
- **requests** 是一个HTTP库，用于发送HTTP请求。
- **uuid** 用于生成唯一的会话ID。
- `app = Flask(__name__)`: 初始化Flask应用。

### API密钥和获取Access Token:
- **API_KEY** 和 **SECRET_KEY** 需要替换为从百度平台获得的实际API密钥。
- 使用这些密钥向百度的OAuth 2.0接口请求 **ACCESS_TOKEN**。

### 聊天接口地址:
- **CHAT_API_URL** 是ERNIE-Bot聊天接口的地址，使用获取到的 **ACCESS_TOKEN** 构建。

### 用户聊天历史存储:
- `user_chat_histories`: 一个字典，用于存储每个用户的聊天历史。

### 路由和视图函数:
- `@app.route("/")`: 当用户访问根URL时触发。它生成一个会话ID，渲染HTML页面，并将会话ID存储在cookie中。
- `@app.route("/chat", methods=["POST"])`: 定义处理聊天请求的路由。当用户发送聊天内容时，这个函数会被调用。

### 处理聊天:
1. **获取用户ID** 和 **用户输入**。
2. **构建历史消息**：将用户的输入和历史对话添加到请求数据中。
3. **发送请求**：使用构建的数据向ERNIE-Bot接口发送POST请求。
4. **处理响应**：从ERNIE-Bot接收响应并提取结果。
5. **更新聊天历史**：将新的响应添加到用户的聊天历史中。
6. **返回JSON响应**：将ERNIE-Bot的回复以JSON格式返回给用户。

### 启动服务器:
- 最后，`if __name__ == "__main__":` 表明如果这个脚本是作为主程序运行，则启动Flask应用，监听在所有可用的IP上的1333端口，并设置调试模式为关闭。

总之，这个脚本创建了一个可以与百度的ERNIE-Bot进行交互的Web应用，用户可以发送消息并接收来自ERNIE-Bot的回复，所有的交互都通过Web界面进行。<br>



## 拓展-`sanic`中有用于渲染HTML模板的吗？

Sanic 是一个异步Python 3.7+ Web服务器和Web框架，它是为了快速构建高性能的Web应用而设计的。与Flask类似，Sanic也支持HTML模板的渲染，但它不自带模板引擎。你需要结合额外的模板库来渲染HTML模板。<br>

常用的模板引擎有：<br>

1. **Jinja2**: 这是一个非常流行的Python模板引擎，Flask默认使用的也是它。尽管Jinja2不是异步的，但你可以在Sanic中同步地使用它来渲染模板。因为模板渲染通常很快，所以这通常不会成为性能瓶颈。

2. **Sanic-Jinja2**: 这是为Sanic框架定制的Jinja2支持。它提供了一个简单的接口来集成Jinja2模板引擎与Sanic应用。

要在Sanic中使用Jinja2进行模板渲染，你需要首先安装Jinja2或Sanic-Jinja2，然后在Sanic应用中设置并使用它。以下是一个简单的示例，说明如何在Sanic中使用Sanic-Jinja2：<br>

```python
from sanic import Sanic
from sanic.response import html
from sanic_jinja2 import SanicJinja2

app = Sanic(__name__)
jinja = SanicJinja2(app)

@app.route("/")
async def index(request):
    return jinja.render('index.html', request, my_variable='Hello World')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

在这个示例中，`SanicJinja2` 被用来渲染一个名为`index.html`的模板，你可以在模板中使用`my_variable`变量。<br>

请注意，虽然Sanic是异步的，但模板渲染通常是同步进行的。如果你的模板非常复杂或需要处理大量数据，可能需要考虑性能问题，或者寻找可以异步渲染模板的解决方案。<br>


## jsonify的作用:

`jsonify` 是 Flask 框架中的一个函数，用于将数据转换为 JSON 格式并构建一个带有正确 MIME 类型的 Response 对象。其主要作用和特点包括：<br>

1. **数据转换**：`jsonify` 自动将 Python 字典或其他数据结构转换成 JSON 格式的字符串。这意味着你可以将字典、列表等对象传递给 `jsonify`，它会处理转换工作，确保数据以 JSON 格式发送给客户端。

2. **设置响应头**：除了转换数据，`jsonify` 还会自动设置响应的 MIME 类型为 `application/json`。这告诉接收响应的客户端，响应内容是 JSON 格式的数据，有助于客户端正确解析和处理数据。

3. **简化响应创建**：使用 `jsonify` 可以简化 API 开发过程中的响应创建。你不需要手动将数据转换为 JSON，再设置正确的 MIME 类型，`jsonify` 为你处理了这些细节。

4. **支持回调函数**：`jsonify` 支持 JSONP 回调，如果请求中指定了回调，它可以生成 JSONP 响应，这对于跨域请求尤其有用。

例如，在 Flask 应用程序中，你可能会这样使用 `jsonify`：<br>

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {"message": "Hello, World!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
```

在上面的例子中，`jsonify` 将字典 `{"message": "Hello, World!"}` 转换为 JSON 格式，并返回一个带有该 JSON 和正确 MIME 类型的响应。当这个端点被请求时，客户端将接收到一个包含 JSON 数据的响应，可以很容易地在客户端进行解析和使用。<br>
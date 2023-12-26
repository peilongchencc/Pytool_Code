# 千帆大模型API调用

## 代码示例:

```python
from flask import Flask, render_template, request, jsonify, make_response  # 导入Flask及其他必要库
import requests
import uuid

app = Flask(__name__)  # 初始化Flask应用

# 替换成您的API Key和Secret Key
API_KEY="你的APIKey"  # 填入平台申请的实际APIKey
SECRET_KEY="你的SecretKey" # 填入平台申请的实际SecretKey

# 获取access_token
TOKEN_URL = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={SECRET_KEY}"
response = requests.get(TOKEN_URL)
ACCESS_TOKEN = response.json()["access_token"]

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
    user_id = request.cookies.get("sessionid")  # 从请求中获取用户ID
    user_input = request.json["user_input"]  # 获取用户输入
    user_history = user_chat_histories.get(user_id, [])  # 获取该用户的对话历史

    user_history.append({"role": "user", "content": user_input})  # 将用户输入添加到历史记录中
    headers = {"Content-Type": "application/json"}  # 设置请求头
    data = {"messages": user_history}  # 创建请求数据，包括所有历史消息
    response = requests.post(CHAT_API_URL, headers=headers, json=data)  # 向API发送请求并获取响应
    result = response.json()["result"]  # 从响应中提取结果
    print(result)
    user_history.append({"role": "assistant", "content": result})  # 将结果添加到历史记录中
    user_chat_histories[user_id] = user_history  # 更新该用户的聊天历史
    return jsonify({"response": result})  # 返回JSON响应

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1333, debug=False)  # 启动应用
```

## 代码解释:

以上代码是一个使用Flask框架构建的简单Web服务器，旨在与百度的ERNIE-Bot聊天接口进行交互。下面是详细解释：

`sanic`中有用于渲染HTML模板的吗？

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

总之，这个脚本创建了一个可以与百度的ERNIE-Bot进行交互的Web应用，用户可以发送消息并接收来自ERNIE-Bot的回复，所有的交互都通过Web界面进行。
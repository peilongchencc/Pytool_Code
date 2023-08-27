# Flask
Flask是一个用于构建Web应用程序的Python微型框架。它被设计为简单、轻量级和易于扩展，使开发者能够快速地创建具有基本功能的Web应用。Flask提供了一组工具、库和模块，可以帮助处理路由、请求-响应循环、会话管理、模板渲染等常见的Web开发任务。<br>

Flask的特点：<br>
轻量级、路由支持、集成了Jinja2模板引擎，可以在HTML中渲染动态内容、会化管理、WSGI兼容、RESTful支持和各种拓展，例如数据库集成、身份验证、表单验证等功能。<br>

> RESTful支持是指在Web应用程序中实现Representational State Transfer（REST）架构风格的能力。REST是一种用于设计网络应用程序的架构风格，它强调使用标准的HTTP方法（如GET、POST、PUT、DELETE）来操作资源，并通过URL来唯一标识资源。

## Flask的安装：
```shell
pip install flask
```

## 最简单示例：
以下是一个最简单的 Flask 示例代码，演示了如何创建一个基本的 Web 应用程序并定义一个路由，返回 "Hello, Flask!" 消息：<br>
```python
from flask import Flask

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义路由，当访问根路径时执行该函数
@app.route('/')
def hello():
    return 'Hello, Flask!'

# 运行应用
if __name__ == '__main__':
    app.run()
```
> 注意代码顺序，`app.run()` 要运行在 `if __name__ == '__main__':` 下。<br>

将上述代码保存在一个 `.py` 文件中，例如 `app.py`，在终端中进入该文件所在的目录，运行以下命令启动应用：<br>
```shell
python app.py
```
这将会启动一个本地开发服务器，在浏览器中输入 `http://localhost:5000/` ，回车后就可以看到 "Hello, Flask!" 消息。<br>

> 如果你是使用远程服务器(例如阿里云服务器)启动的服务，现在需要在其他地方(例如家里、公司)，需要将 `localhost` 改为远程服务器的公网ip，如 `http://8.140.203.361:5000/` 。<br>
如果远程服务器利用DNS将ip解析为了域名，比如 `8.140.203.361` 解析为了 `myflaskserver`，URL需要改为：`http://myflaskserver:5000/`。<br>
注意：如果只是相同机器上，服务A调用服务B的URL，依旧使用 `localhost` 。这部分再讲就有些多了，涉及到这部分内容的请自行搜索 "公网ip、内网ip、DNS解析" 内容。

因为这是个最简单的示例，并没有加入丰富的界面组件，所以只能看到简单的文字信息～，如果你想更近一步的了解Flask的使用，请往下看。<br>

## 更改端口号：
Flask服务端口号默认为5000，实际工作中由于我们可能会启动多个Flask服务，但一个端口号只能对应一个服务，端口号冲突的时候是无法启动服务的。所以我们需要了解如何更改Flask的端口号，假设我们将端口号更改为7711:<br>
```python
from flask import Flask

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义路由，当访问根路径时执行该函数
@app.route('/')
def hello():
    return 'Hello, Flask!'

# 运行应用，设置端口号为 7711，如果不设置端口号，Flask服务端口号默认为5000。
if __name__ == '__main__':
    app.run(port=7711)
```
现在你可以在浏览器中输入 `http://localhost:7711/` 访问自己的服务了。<br>


## 添加路由的前缀 `/nlp-server`：
路由前缀的优势有二：<br>
1. 隔离命名空间：对于有相同元素的内容，我们可能设置相同命名。以电商为例，例如 "耐克" 旗下有 "鞋类" 商品，"阿迪达斯" 旗下也有 "鞋类" 商品，这就会出现命名重复问题，但不相同的路由前缀可以帮我们转向不同的网址，不会出错。
2. 对于DNS解析的结果进行匹配：以阿里云服务器为例，在监听端口时会将端口监听到一个具体的网址上(假设为 `/nlp-server`)，此时我们就需要将自己的路由前缀设置为相同内容进行匹配。

原理：公网ip`8.140.203.361`--DNS解析-->`myflaskserver`，监听的7711端口映射为 `/nlp-server`，所以我们如果想要访问Flask启动的服务，形式就需要为：`http://myflaskserver/nlp-server/`。

```python
from flask import Flask, Blueprint

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 创建一个 Blueprint 并设置前缀
nlp_server_blueprint = Blueprint('nlp_server', __name__, url_prefix='/nlp-server')

# 在 Blueprint 中定义路由
@nlp_server_blueprint.route('/')
def hello():
    return 'Hello, NLP Server!'

# 注册 Blueprint 到应用
app.register_blueprint(nlp_server_blueprint)

# 运行应用
if __name__ == '__main__':
    app.run(port=7711)
```
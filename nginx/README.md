# Nginx
Nginx（发音为“engine X”）是一个开源的、高性能的Web服务器软件，也可以用作反向代理服务器、负载均衡器、HTTP缓存以及通用的代理服务器。Nginx在处理并发连接和高流量负载方面表现出色，因此在构建稳定、高效的网络应用程序和网站时非常受欢迎。<br>

安装和使用Nginx（Engine-X）在Ubuntu 18.04.6上相对比较简单。本文讲解安装、Nginx的基本使用和常见用法：<br>

## 安装Nginx:
1. 打开终端。
2. 更新软件包列表：
```shell
sudo apt update
```
注意⚠️⚠️⚠️：更新软件包列表是让系统获取各种库的信息，并不会升级或降低个人环境中的库版本。<br>

3. 安装Nginx:
```shell
sudo apt install nginx
```
4. 安装完成后，Nginx将会自动启动。你可以通过以下命令检查Nginx的运行状态：
```shell
sudo systemctl status nginx
```
如果上述指令你无法使用，可以尝试使用：<br>
```shell
ps aux|grep nginx
```
5. 启动Nginx：
```shell
sudo systemctl start nginx
```
或者使用：<br>

```shell
sudo service nginx start
```
`sudo systemctl start nginx` 和 `sudo service nginx start` 这两个命令实际上都是用来启动 Nginx 服务的，但它们之间存在一些区别，主要是因为不同的服务管理系统。<br>

`sudo systemctl start nginx` 是使用 `Systemd` 系统管理工具来控制服务的命令，在现代的 `Linux` 发行版中，`Systemd` 是常见的 `init` 系统，用于管理系统进程和服务。<br>
`sudo service nginx start` 是使用 `System V (SysV) init` 系统的服务管理命令。`SysV init` 系统是☕️☕️☕️旧式的 `init` 系统，用于在 `Linux` 发行版中管理系统服务，但在现代系统中逐渐被 `Systemd` 取代。<br>

`service` 命令提供了一种简化的接口来启动、停止和管理服务，相对来说 `systemctl` 命令提供了更多的功能和灵活性。<br>

6. 停止Nginx服务：
```shell
sudo systemctl stop nginx
```
或者使用：<br>
```shell
sudo service nginx stop
```

7. 为了让Nginx重新加载配置，你可以使用以下命令：
```shell
sudo systemctl reload nginx
```

## Nginx的基本使用：
接下来以**Nginx反向代理**为例，讲解 Flask + Nginx 的使用：<br>
> 其实无论你使用的是 Flask、Fast-API、Sanic或其他Web应用程序框架，和 `Nginx` 结合使用的道理是一样的。

1. 确定自己的路由、端口信息，然后启动自己的Flask服务：
假设你程序入口的代码如下，端口号为7711，访问的URL为 `http://localhost:7711/nlp-server/`：<br>
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

2. 打开 Nginx 配置文件，
根据 Nginx 在 Ubuntu 上的默认位置打开 Nginx 配置文件：<br>
```shell
sudo vim /etc/nginx/nginx.conf
```

3. 在 `http` 模块内添加以下配置：(网址的批量映射请看下一节内容)
```python
server {
    isten 80;
    server_name localhost;
    
    location /nlp/ {
        proxy_pass http://localhost:7711/nlp-server/;
        }
}
```
该配置将监听端口 `80`，并将 `/nlp/ans` 路径代理到 Sanic 服务的 `localhost:7711/nlp-server/` 路径。意思就是：你在访问时只需要输入 `http://localhost:80/nlp/` 就相当于访问了 `http://localhost:7711/nlp-server/`。<br>
😀😀😀值得一提的是，Nginx 反向代理并不会拖慢程序反应速度。<br>

4. 检查配置语法：
```shell
sudo nginx -t
```
如果配置文件中没有语法错误，你将会看到类似以下内容的输出：<br>
```shell
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```
如果存在语法错误，它们会被显示出来，你需要根据错误信息来修复配置文件。<br>

5. 重新加载Nginx配置:

如果配置文件语法没有问题，重新加载Nginx配置，使更改生效即可：<br>
```shell
sudo systemctl reload nginx
```
上面的指令用于不关闭 Nginx 的情况使修改后的配置文件生效。如果你的 Nginx 没有运行，直接启动它等于相同的效果：<br>
```shell
sudo systemctl start nginx
```

现在你就可以通过 `http://localhost:80/nlp/` 访问自己的服务了～<br>

## 网址的批量映射：
```log
server {
    listen       8082;
    server_name  localhost;
    
    # 修改以bp1为前缀的所有网址的映射
    location /nlp/ {
        proxy_pass http://localhost:7711/bp1/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    # 修改以bp2为前缀的所有网址的映射
    location /irm/ {
        proxy_pass http://localhost:7744/bp2/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}                          
```
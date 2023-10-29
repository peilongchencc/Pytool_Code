# Milvus
- [Milvus](#milvus)
  - [Milvus安装:](#milvus安装)
  - [查看Milvus是否运行:](#查看milvus是否运行)
  - [连接Milvus:](#连接milvus)
  - [为Milvus设置密码:](#为milvus设置密码)
  - [关闭Milvus standalone:](#关闭milvus-standalone)
  - [安装Milvus Python SDK:](#安装milvus-python-sdk)
    - [补充说明Install Milvus Python SDK是什么意思？其中的SDK表示什么:](#补充说明install-milvus-python-sdk是什么意思其中的sdk表示什么)

## Milvus安装:

1. 下载 YAML 文件;

> 注意创建一个文件夹存放，因为下载的文件名为`docker-compose.yml`，时间长后你自己都不知道这个文件是什么。

```bash
wget https://github.com/milvus-io/milvus/releases/download/v2.3.2/milvus-standalone-docker-compose.yml -O docker-compose.yml
```

2. 在与` docker-compose.yml` 文件相同的目录中，运行以下命令启动 Milvus:

```bash
sudo docker-compose up -d
```

这个指令的作用是使用 Docker Compose 启动一个由 Docker Compose 配置文件定义的多个容器应用，并且在后台（detached 模式，使用 `-d` 标志）运行这些容器。<br>

- `docker-compose`: 这是 Docker Compose 工具的命令，它用于管理多个 Docker 容器的部署。Docker Compose 使用一个 YAML 配置文件来定义应用程序的多个服务和它们之间的关系。

- `up`: 这是 Docker Compose 命令的一个子命令，用于启动定义在配置文件中的服务。当运行 `docker-compose up` 时，它将会创建并启动定义的容器。

- `-d`: 这是一个选项标志，它告诉 Docker Compose 在后台运行容器。如果不使用 `-d` 标志，Docker Compose 将会在前台显示容器的输出日志，而且如果您关闭终端窗口，容器也会停止。

总的来说，`sudo docker-compose up -d` 命令用于以后台模式启动 Docker Compose 配置文件中定义的容器应用，这些容器应用可以包含多个服务，例如 Web 服务器、数据库等。这个命令对于部署和管理容器化应用程序非常有用。<br>

运行`sudo docker-compose up -d`后，终端显示(官方示例):<br>

```log
Creating milvus-etcd  ... done
Creating milvus-minio ... done
Creating milvus-standalone ... done
```

笔者安装后显示的内容为:<br>

<img src="./milvus_materials/milvus安装成功图片.jpg" alt="image" width="50%" height="50%">


3. 现在检查容器是否已经启动并运行:

```bash
sudo docker compose ps
```

终端显示(官方示例):<br>

```log
      Name                     Command                  State                            Ports
--------------------------------------------------------------------------------------------------------------------
milvus-etcd         etcd -advertise-client-url ...   Up             2379/tcp, 2380/tcp
milvus-minio        /usr/bin/docker-entrypoint ...   Up (healthy)   9000/tcp
milvus-standalone   /tini -- milvus run standalone   Up             0.0.0.0:19530->19530/tcp, 0.0.0.0:9091->9091/tcp
```

笔者安装后显示的内容为:<br>

<img src="./milvus_materials/milvus容器运行状态.jpg" alt="image" width="100%" height="100%">


指令 `sudo docker compose ps` 的作用是列出与当前工作目录下的 `docker-compose.yml` 文件相关的 Docker 服务的状态。<br>

具体来说，这个命令会显示：<br>

- 服务名（service name）
- 命令（command）
- 状态（state，例如 "Up" 或 "Exited"）
- 端口（ports）

使用 `sudo` 前缀是因为 Docker 通常需要超级用户权限来运行。<br>

`docker compose` 是 Docker Compose 的一个新的命令结构，它在 Docker 20.10 之后的版本中被引入。在此之前，通常使用 `docker-compose`（带连字符）的命令格式。两种格式的功能基本相同，但命令结构略有不同。<br>

简而言之，`sudo docker compose ps` 命令用于查看当前目录下由 `docker-compose.yml` 定义的 Docker 服务的状态。<br>

## 查看Milvus是否运行:

要查看你的 Milvus 是否正在 Ubuntu 18.04 上运行，你可以采用以下几种方法：<br>

1. **使用`docker ps`命令**:
   
如果你是通过 Docker 安装和运行 Milvus 的，你可以使用 `docker ps` 来查看正在运行的容器。例如:<br>

```bash
docker ps
```

在输出的列表中，找是否有 Milvus 的容器正在运行。<br>

2. **使用`ps`命令和`grep`工具**:
   
你可以使用 `ps` 命令结合 `grep` 工具来查看是否有与 Milvus 相关的进程正在运行：<br>

```bash
ps aux | grep milvus
```

如果 Milvus 在运行，你应该能看到与 Milvus 相关的进程信息。<br>

3. **使用`netstat`命令查看端口**:
   
通常，Milvus 默认在 `19530` 端口上监听。你可以使用 `netstat` 来查看此端口是否已经被占用：<br>

```bash
netstat -tuln | grep 19530
```

如果你看到有进程监听在这个端口上，那很可能 Milvus 是在运行的。<br>

或者直接使用`netstat -tuln`查看是否有属于Milvus的端口。<br>

4. **查看 Milvus 的日志**:
   
如果你有访问 Milvus 日志的权限，那么你可以直接查看它的日志来判断其是否在正常运行。<br>

不论你采用哪种方法，记得根据实际情况调整命令和参数。如果你有其他关于 Milvus 或 Ubuntu 的问题，请随时提问。<br>

**如果你是使用 Docker 运行的 Milvus**，Milvus 的日志位置通常在容器内部。你可以使用以下命令来查看 Milvus 容器的日志：<br>

```bash
docker logs [CONTAINER_ID_OR_NAME]
```

其中 `[CONTAINER_ID_OR_NAME]` 是你的 Milvus 容器的 ID 或名称。<br>

如果你是按照笔者的方式安装的Milvus，想查看 Milvus 的日志，可以使用以下命令：<br>

```bash
docker logs milvus-standalone
```

此命令会输出 `milvus-standalone` 容器的日志。<br>

如果需要查看 MinIO 或 etcd 的日志，只需将 `milvus-standalone` 替换为相应的容器名称即可。例如，查看 MinIO 的日志：<br>

```bash
docker logs milvus-minio
```

以上信息应该可以帮助你了解当前 Milvus 的运行状态和查看其日志。<br>


## 连接Milvus:

使用以下指令，验证 Milvus 服务器正在监听哪个本地端口。注意将容器名称替换为你自己的:

```bash
docker port milvus-standalone 19530/tcp
```

终端显示信息:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7cxxx:~# docker port milvus-standalone 19530/tcp
0.0.0.0:19530
[::]:19530
```

这表明，你的 Milvus 容器的 `19530` 端口映射到了宿主机的 `0.0.0.0:19530` 和 `[::]:19530`。<br>

其中：<br>

- `0.0.0.0:19530` 表示该端口在所有的 IPv4 地址上都是可访问的。

- `[::]:19530` 表示该端口在所有的 IPv6 地址上都是可访问的。

这意味着，只要你的服务器防火墙规则允许外部访问这个端口，并且没有其他的网络限制，那么你确实应该可以从外部访问这个 Milvus 实例。<br>

但需要注意的是，对于任何服务，尤其是数据库类服务，直接暴露到外网有其风险。确保你已经设置了适当的安全措施，如防火墙规则、强密码、安全的连接方式等，以保护你的服务不被恶意访问。<br>


## 为Milvus设置密码:


## 关闭Milvus standalone:

要关闭 `Milvus standalone`，请运行以下指令:<br>

```bash
sudo docker compose down
```

要在停止 Milvus 后删除数据，请运行以下指令:<br>

```bash
sudo rm -rf  volumes
```

## 安装Milvus Python SDK:

切换到你需要安装`pymilvus`的虚拟环境，然后运行以下指令:<br>

```bash
python3 -m pip install pymilvus==2.3.2
```

现在终端运行以下指令，验证下`pymilvus`是否已经正确安装。如果`pymilvus`的安装没有问题，则终端运行以下命令时不会引发异常:<br>

```bash
python3 -c "from pymilvus import Collection"
```

### 补充说明Install Milvus Python SDK是什么意思？其中的SDK表示什么:

"Install Milvus Python SDK" 的意思是安装 Milvus 的 Python 软件开发工具包。<br>

其中的 "SDK" 是 "Software Development Kit" 的缩写，翻译成中文是“软件开发工具包”。<br>

SDK 通常包括一组软件开发工具，这些工具允许开发者为特定的软件包、软件框架、硬件平台、计算机系统、操作系统或平台创建应用程序。<br>

对于 "Milvus Python SDK"，这意味着**这是一个为 Python 语言提供的工具集，允许开发者更容易地与 Milvus 进行交互和开发。**🫠🫠🫠Milvus 是一个开源的向量搜索引擎，它使得大规模向量数据的相似性搜索变得简单高效。<br>

简而言之，如果你想使用 Python 来开发和 Milvus 相关的应用，你就需要安装 Milvus Python SDK。<br>
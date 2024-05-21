# Milvus

本章介绍向量数据库Milvus的安装与使用，注意⚠️ Milvus 是一个内存数据库，数据需要 `load` 到内存中才能执行查询操作。<br>

- [Milvus](#milvus)
  - [Milvus安装:](#milvus安装)
  - [脱机状态下安装milvus:](#脱机状态下安装milvus)
  - [查看Milvus版本:](#查看milvus版本)
    - [利用yml文件查看:](#利用yml文件查看)
    - [利用docker查看:](#利用docker查看)
  - [查看Milvus是否运行:](#查看milvus是否运行)
  - [连接Milvus:](#连接milvus)
  - [为Milvus设置密码:](#为milvus设置密码)
  - [更改milvus中数据的存储位置：](#更改milvus中数据的存储位置)
  - [关闭Milvus standalone:](#关闭milvus-standalone)
  - [Milvus稳定性简介:](#milvus稳定性简介)
  - [安装Milvus Python SDK:](#安装milvus-python-sdk)
    - [补充说明Install Milvus Python SDK是什么意思？其中的SDK表示什么:](#补充说明install-milvus-python-sdk是什么意思其中的sdk表示什么)
  - [Milvus数据库操作:](#milvus数据库操作)
    - [利用pymilvus与Milvus数据库建立/断开连接:](#利用pymilvus与milvus数据库建立断开连接)
    - [创建数据库:](#创建数据库)
    - [查找 Milvus 集群中的所有现有数据库:](#查找-milvus-集群中的所有现有数据库)
    - [指定使用某个数据库:](#指定使用某个数据库)
    - [删除某个数据库:](#删除某个数据库)
  - [Milvus中集合的操作:](#milvus中集合的操作)
    - [FieldSchema介绍:](#fieldschema介绍)
    - [DataType介绍:](#datatype介绍)
    - [CollectionSchema:](#collectionschema)
    - [Collection(创建集合)介绍:](#collection创建集合介绍)
      - [查看集合名称:](#查看集合名称)
    - [加载/释放集合:](#加载释放集合)
  - [Milvus中分区操作:](#milvus中分区操作)
    - [Partition(分区)和Collection(集合)的关系:](#partition分区和collection集合的关系)
    - [查看某个集合的所有分区:](#查看某个集合的所有分区)
    - [在某个集合下创建分区:](#在某个集合下创建分区)
    - [判断集合中是否有某个分区:](#判断集合中是否有某个分区)
    - [删除某个集合下的分区:](#删除某个集合下的分区)
  - [utility介绍:](#utility介绍)
    - [查看Milvus中所有集合](#查看milvus中所有集合)
    - [查看Milvus中是否有某个集合](#查看milvus中是否有某个集合)
    - [删除指定名称的集合：](#删除指定名称的集合)
    - [集合重命名:](#集合重命名)
    - [计算两组向量之间的距离:](#计算两组向量之间的距离)
    - [查看集合属性:](#查看集合属性)
    - [设置/查看集合的过期时间:](#设置查看集合的过期时间)
    - [Milvus能否设置某条数据的过期时间？](#milvus能否设置某条数据的过期时间)
  - [分批向Milvus插入数据:](#分批向milvus插入数据)
  - [Milvus中的数据操作:](#milvus中的数据操作)
    - [upsert():](#upsert)
    - [使用upsert时的注意事项:](#使用upsert时的注意事项)
  - [删除实体:](#删除实体)
  - [Milvus数据迁移工具--MilvusDM:](#milvus数据迁移工具--milvusdm)
  - [Milvus索引建立:](#milvus索引建立)
    - [index\_type详细解释:](#index_type详细解释)
  - [Milvus使用FAQ:](#milvus使用faq)
    - [我使用的是Ubuntu18.4，我使用的是CPU版本Milvus，Milvus中存储了50万条向量数据，我的向量都是使用Electra转化的。我检索一条数据的耗时竟然需要0.2s，是否有方法提升检索速度？使用维度更低的模型转换词向量如何？我的数据都是中文文本。](#我使用的是ubuntu184我使用的是cpu版本milvusmilvus中存储了50万条向量数据我的向量都是使用electra转化的我检索一条数据的耗时竟然需要02s是否有方法提升检索速度使用维度更低的模型转换词向量如何我的数据都是中文文本)
    - [我使用的是Ubuntu18.4，我使用的是CPU版本Milvus，我使用的是pymilvus 2.x版本，我应该如何使用pymilvus进行批量查询？](#我使用的是ubuntu184我使用的是cpu版本milvus我使用的是pymilvus-2x版本我应该如何使用pymilvus进行批量查询)
    - [flush()后create\_index()卡住:](#flush后create_index卡住)
    - [text字段的模糊匹配无法实现:](#text字段的模糊匹配无法实现)
  - [pymilvus示例代码:](#pymilvus示例代码)
  - [pymilvus简单示例:](#pymilvus简单示例)
  - [python类形式调用milvus:](#python类形式调用milvus)
  - [query\_iterator:](#query_iterator)

## Milvus安装:

1. 选定存放Milvus相关YAML文件的路径:

选择或创建一个文件夹存放Milvus相关YAML文件(文件名为`docker-compose.yml`)，注意将文件夹名称定义为易识别形式，否则时间长后你自己都不知道这个文件是什么。笔者的路径为`/root/`。<br>

2. 下载 YAML 文件;

运行下列指令，会将`docker-compose.yml`下载到当前所在目录:<br>

```bash
wget https://github.com/milvus-io/milvus/releases/download/v2.3.2/milvus-standalone-docker-compose.yml -O docker-compose.yml
```

3. 在` docker-compose.yml` 文件所在目录运行以下命令启动 Milvus:

```bash
sudo docker-compose up -d
```

这个指令的作用是使用 Docker Compose 启动一个由 Docker Compose 配置文件定义的多个容器应用，并且在后台（detached 模式，使用 `-d` 标志）运行这些容器。<br>

  - `docker-compose`: 这是 Docker Compose 工具的命令，它用于管理多个 Docker 容器的部署。Docker Compose 使用一个 YAML 配置文件来定义应用程序的多个服务和它们之间的关系。

  - `up`: 这是 Docker Compose 命令的一个子命令，用于启动定义在配置文件中的服务。当运行 `docker-compose up` 时，它将会创建并启动定义的容器。

  - `-d`: 这是一个选项标志，它告诉 Docker Compose 在后台运行容器。如果不使用 `-d` 标志，Docker Compose 将会在前台显示容器的输出日志，而且如果你关闭终端窗口，容器也会停止。

总的来说，`sudo docker-compose up -d` 命令用于以后台模式启动 Docker Compose 配置文件中定义的容器应用，这些容器应用可以包含多个服务，例如 Web 服务器、数据库等。这个命令对于部署和管理容器化应用程序非常有用。<br>

运行`sudo docker-compose up -d`后，终端显示(官方示例):<br>

```log
Creating milvus-etcd  ... done
Creating milvus-minio ... done
Creating milvus-standalone ... done
```

笔者安装后显示的内容为:<br>

<img src="./milvus_materials/milvus安装成功图片.jpg" alt="image" width="50%" height="50%">


4. 现在检查容器是否已经启动并运行:

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


## 脱机状态下安装milvus:

工作中，你所用的服务器可能无法连网，或者无法从milvus的镜像库获取对应的镜像，此时可在一台可连接网络的电脑上拉取milvus镜像，然后将该镜像压缩，上传至脱机服务器，再导入milvus镜像。具体操作如下:<br>

🤨🤨🤨你可以在你的 Mac/Windows 电脑上拉取 Docker 镜像，然后将其上传到 CentOS 7 的服务器上。Docker 镜像是平台无关的，这意味着你可以在一个系统（如 macOS）上下载它们，然后在另一个系统（如 CentOS）上运行。<br>

假设你现在已经在能连网的电脑上安装了milvus，且能启动milvus，现在使用以下指令，查看下本地镜像库所有docker镜像:<br>

```bash
sudo docker images
```

终端显示:<br>

| REPOSITORY          | TAG                          | IMAGE ID       | CREATED         | SIZE        |
|---------------------|------------------------------|----------------|-----------------|-------------|
| milvusdb/milvus     | v2.3.2                       | 4b6c62c2b5f8   | 3 weeks ago     | 868MB       |
| minio/minio         | RELEASE.2023-03-20T20-16-18Z | 400c20c8aac0   | 8 months ago    | 252MB       |
| quay.io/coreos/etcd | v3.5.5                       | 673f29d03de9   | 14 months ago   | 182MB       |

找一个自己熟悉的位置，保存docker镜像，依次下列指令会将docker镜像转为tar文件，并保存在当前目录。切忌不要保存在`/var/`路径下。<br>

> 注意自己的镜像名称要对应正确。

```bash
sudo docker save milvusdb/milvus:v2.3.2 -o milvus_v2.3.2.tar
sudo docker save minio/minio:RELEASE.2023-03-20T20-16-18Z -o minio.tar
sudo docker save quay.io/coreos/etcd:v3.5.5 -o etcd.tar
```

接下来，将文件传输到无互联网的服务器，将这三个 `.tar` 文件以及 `docker-compose.yml` 文件传输到你无法连接互联网的服务器上。<br>

在你的Linux服务器上，使用以下命令加载这些镜像：<br>

```bash
sudo docker load -i milvus_v2.3.2.tar
sudo docker load -i minio.tar
sudo docker load -i etcd.tar
```

```bash
sudo docker-compose up -d
```

请确保保存和传输的 Docker 镜像版本与你的 `docker-compose.yml` 文件中指定的版本相匹配。如果不匹配，你可能需要在服务器上调整 `docker-compose.yml` 文件。<br>

现在，你的Milvus镜像应该已经安装成功了～🪴🪴🪴🪴🪴<br>


## 查看Milvus版本:

### 利用yml文件查看:

找到你Milvus相关的`docker-compose.yml`文件，文件中会有如下Milvus版本信息:

```yml
  standalone:
    container_name: milvus-standalone
    image: milvusdb/milvus:v2.3.2
```

### 利用docker查看:

终端输入`docker ps`指令后，终端显示(官方示例):<br>

```log
      Name                     Command                  State                            Ports
--------------------------------------------------------------------------------------------------------------------
milvus-etcd         etcd -advertise-client-url ...   Up             2379/tcp, 2380/tcp
milvus-minio        /usr/bin/docker-entrypoint ...   Up (healthy)   9000/tcp
milvus-standalone   /tini -- milvus run standalone   Up             0.0.0.0:19530->19530/tcp, 0.0.0.0:9091->9091/tcp
```

找到自己需要查看的容器名，然后仿照下列指令修改即可:<br>

```bash
docker inspect milvus-standalone | grep "Image" | cut -d '"' -f 4
```

终端显示:<br>

```log
sha256:4b6c62c2b5f8803ec635347be7b430d88a00d1d10226e0cfe6f9a6883ed84ff0
milvusdb/milvus:v2.3.2
```

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


## 更改milvus中数据的存储位置：

更改milvus中数据的存储位置可有效避免因硬盘空间问题引起的Milvus自动关闭，具体操作如下：<br>

1. 找到自己的`docker-compose.yml`文件所在目录，运行以下指令**停止 Milvus 服务**：

```bash
sudo docker-compose down
```

终端显示:<br>

```log
Stopping milvus-minio ... done
Stopping milvus-etcd  ... done
Removing milvus-standalone ... done
Removing milvus-minio      ... done
Removing milvus-etcd       ... done
Removing network milvus
```

2. 查看Milvus中数据存储路径:

打开`docker-compose.yml`文件，查看`standalone`模块对应的`volumes`路径，以笔者为例:<br>

```yml
standalone:
  container_name: milvus-standalone
  image: milvusdb/milvus:v2.3.2
  command: ["milvus", "run", "standalone"]
  security_opt:
  - seccomp:unconfined
  environment:
    ETCD_ENDPOINTS: etcd:2379
    MINIO_ADDRESS: minio:9000
  volumes:
    - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/milvus:/var/lib/milvus
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:9091/healthz"]
    interval: 30s
    start_period: 90s
    timeout: 20s
    retries: 3
  ports:
    - "19530:19530"
    - "9091:9091"
  depends_on:
    - "etcd"
    - "minio"
```

`docker-compose.yml` 文件中的 `volume` 映射是由 `${DOCKER_VOLUME_DIRECTORY:-.}` 这个环境变量决定的。这意味着如果你没有设定 `DOCKER_VOLUME_DIRECTORY` 这个环境变量，它会默认使用当前目录（`.`）。<br>


1. 迁移数据:

如果 Milvus 已经有数据并且你希望保留，你需要迁移数据到新的目录下，假设要迁移到 `/data/milvus_data` 目录下：<br>

```bash
sudo mv ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/milvus /data/milvus_data
```

空的`/data/milvus_data`将显示以下结构:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7cxxx:/data/milvus_data# tree
.
└── milvus
    ├── rdb_data
    └── rdb_data_meta_kv
```

4. 更新 docker-compose.yml 文件:

在 `standalone` 服务的 `volumes` 部分中，更改映射目录到 `/data/milvus_data`。同时，也建议更改 `etcd` 和 `minio` 的存储路径，以避免未来可能出现的空间问题。<br>

```yml
...
etcd:
  ...
  volumes:
    - /data/etcd_data:/etcd

minio:
  ...
  volumes:
    - /data/minio_data:/minio_data

standalone:
  ...
  volumes:
    - /data/milvus_data:/var/lib/milvus
...
```

5. 再次启动服务：

```bash
sudo docker-compose up -d
```


## 关闭Milvus standalone:

要关闭 `Milvus standalone`，请运行以下指令:<br>

```bash
sudo docker compose down
```

要在停止 Milvus 后删除数据，请运行以下指令:<br>

```bash
sudo rm -rf  volumes
```

## Milvus稳定性简介:

Milvus中的数据，默认存储时间是永久。<br>

如果docker意外关闭，或被其他人销毁了，数据也不会丢失，重启后数据依旧存在。(除非你删除了`volumes`下的Milvus数据)<br>


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

对于 "Milvus Python SDK"，这意味着 **这是一个为 Python 语言提供的工具集，允许开发者更容易地与 Milvus 进行交互和开发。** 🫠🫠🫠Milvus 是一个开源的向量搜索引擎，它使得大规模向量数据的相似性搜索变得简单高效。<br>

简而言之，如果你想使用 Python 来开发和 Milvus 相关的应用，你就需要安装 Milvus Python SDK。<br>

## Milvus数据库操作:

与传统的数据库引擎类似，你也可以在 Milvus 创建数据库，并为某些用户分配管理数据库的特权。然后，这些用户有权管理数据库中的集合。Milvus 集群最多支持64个数据库。<br>

### 利用pymilvus与Milvus数据库建立/断开连接:

Milvus 支持两个端口，端口`19530`和端口`9091`，端口19530是用于gRPC的，是默认端口。端口9091是用于 RESTful API 的，当你用 HTTP 客户端连接到 Milvus 服务器时使用它。<br>

pymilvus连接Milvus数据库示例:<br>

```python
from pymilvus import connections
connections.connect(
    alias="default",
    user='username',
    password='password',
    host='localhost',
    port='19530'
)
```

`connections.connect()` 方法用于建立全局连接，可以在整个应用程序中共享。**它会自动创建连接池**，并在后续的操作中使用这个连接池来管理连接。<br>

这意味着，一旦使用 `connections.connect()` 建立连接，后续的 Milvus 操作可以共享同一个连接池中的连接，从而提高了性能和资源利用率。<br>

如果你没有对你的Milvus进行账户、密码等配置，可以使用下列写法:<br>

```python
from pymilvus import connections

connections.connect(host='localhost', port='19530')
```

🚨🚨🚨注意: Milvus 支持的最大连接数是 65,536。这个数字指的是客户端与 Milvus 服务器之间的并发连接数量上限。

在同一时间内，最多可以有 65,536 个与 Milvus 服务器的连接处于活动状态。这个连接数限制可以根据你的硬件资源和性能需求进行调整，但在默认配置下，最大连接数是 65,536。

🫠🫠🫠Milvus使用结束后记得断开与Milvus的连接:<br>

```python
connections.disconnect("default")
```


### 创建数据库:

要创建数据库，首先需要连接到 Milvus 集群并为其准备一个名称，假设你要创建一个名为"book"的database，可以使用以下代码:<br>

```python
from pymilvus import connections, db

conn = connections.connect(host='localhost', port='19530')  # 必须要连接到Milvus才能执行db操作；

database = db.create_database("book")
```

### 查找 Milvus 集群中的所有现有数据库:

```python
from pymilvus import connections, db

conn = connections.connect(host='localhost', port='19530')  # 必须要连接到Milvus才能执行db操作；

# 查找 Milvus 集群中的所有现有数据库
database_name = db.list_database()

print(f"数据库有:{database_name}")
```

终端显示:<br>

```log
数据库有:['default', 'book']
```

Milvus 集群默认只有一个名为"default"的数据库。<br>

### 指定使用某个数据库:

Milvus 集群默认只有一个名为"default"的数据库。除非另有说明，否则集合将在默认数据库中创建。<br>

假设你要更改默认数据库，参考以下代码，在连接Milvus的时候设置`db_name`即可。注意将`default`修改为你的数据库名称:<br>

```python

from pymilvus import connections

conn = connections.connect(host="localhost",port="19530",db_name="default")
```

或者依旧使用`db`进行操作:<br>

```python
db.using_database("book")
```

### 删除某个数据库:

若要删除数据库，必须首先删除其所有集合。否则，删除操作将失败。<br>

```python
db.drop_database("book")

db.list_database()

# Output:
# ['default']
```


## Milvus中集合的操作:

在Milvus中集合的基础是Schema，Schema指结构，例如表结构、字段构成等。在我们介绍Milvus中Schema的定义方式前，先导入必要的方法，并连接到Milvus数据库:<br>

```python
from pymilvus import connections, FieldSchema, DataType, CollectionSchema, Collection

# 连接Milvus
connections.connect(host='localhost', port='19530')
```

在Milvus中，`CollectionSchema`、`FieldSchema`和`DataType`是创建一个集合(collection)的基本组件。Milvus是一个开源的向量数据库，用于存储和检索大量的向量数据。这三个组件定义了集合的结构和数据类型。<br>



### FieldSchema介绍:

`FieldSchema`用于定义集合中的一个字段(field)的结构。一个字段相当于传统数据库中的一个列(column)。它包括字段的名字、字段的数据类型以及一些额外的参数，比如是否是主键、是否自动创建索引等等。<br>

每个`FieldSchema`对象通常需要至少两个参数：<br>

- 字段名称

- 字段数据类型，这里使用的是`DataType`枚举

示例:<br>

```python
id_field = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True)
vector_field = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128)
```

### DataType介绍:

`DataType`是一个枚举类，定义了Milvus中支持的不同数据类型。这些数据类型包括基本的数值类型、字符串和向量类型等。比如，`INT64`用于整数、`FLOAT_VECTOR`用于浮点数向量等。<br>

示例中的`DataType.FLOAT_VECTOR`表示字段是浮点型的向量数据，`dim=128`指的是向量的维度是128。<br>

milvus对于varchar字段的单个长度限制是64k字节。对于中文字符，通常使用 UTF-8 编码。在 UTF-8 编码下，一个中文字符通常占用 3 个字节。因此 64000 字节大约可以存储大约 21333 个中文字符。<br>

> 这里的“字符”指的就是一个汉字，中文的标点符号也算作字符，并且在 UTF-8 编码中通常也占用 3 个字节。

### CollectionSchema:

`CollectionSchema`定义了整个集合的结构。一个集合可以看作是一张表，其中包含了多个字段。当你创建一个`CollectionSchema`对象时，你需要定义集合中的所有字段，并且可以定义一些关于集合的额外属性，如描述等。<br>

创建`CollectionSchema`对象时，需要将一系列`FieldSchema`对象作为参数传入。<br>

示例:<br>

```python
schema = CollectionSchema(fields=[id_field, vector_field], description="Test collection")
```

这样，使用`CollectionSchema`和`FieldSchema`对象，你可以定义一个Milvus集合的完整结构，`DataType`用于指定字段的数据类型。这种结构化的方式使得Milvus可以灵活地处理不同类型的数据，并且可以对其进行有效的索引和搜索。<br>

### Collection(创建集合)介绍:

🚨🚨🚨`CollectionSchema`和`Collection`在Milvus中代表了两个相关但不同的概念：<br>

1. **CollectionSchema**: 

- 这个概念是关于结构定义的。`CollectionSchema`定义了一个集合的结构，包括它包含哪些字段以及这些字段的数据类型。它是创建新集合时的一个蓝图，用于告诉Milvus集合中应该有哪些字段和这些字段的属性（比如数据类型、是否为主键、是否有索引等）。

- `CollectionSchema`不存储任何数据，它只是定义了数据将如何存储的规则。

2. **Collection**:

- `Collection`是基于`CollectionSchema`实际**创建的一个实例**🌿🌿🌿🌿🌿，它是数据存储和检索的容器。你可以向`Collection`中插入数据、对其进行查询和索引操作。一旦根据`CollectionSchema`创建了`Collection`，就可以对其进行这些操作。

- `Collection`实际上存储了数据和索引，你可以认为它是Milvus数据库中的一个“表”。

在实际应用中，首先会定义一个`CollectionSchema`，然后基于这个模式创建一个`Collection`。例如：<br>

```python
from pymilvus import connections, FieldSchema, DataType, CollectionSchema, Collection

# 连接Milvus
connections.connect(host='localhost', port='19530')

# 定义字段
id_field = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True)
vector_field = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128)

# 创建集合模式
schema = CollectionSchema(fields=[id_field, vector_field], description="Test collection")

# 使用集合模式创建集合
collection = Collection(name="test_collection", schema=schema)

# 现在你可以向`collection`插入数据，查询数据等
```

在这个例子中，`schema`是一个`CollectionSchema`对象，定义了`collection`应有的结构。创建`collection`时，我们使用这个结构定义，并且给它命名为"test_collection"，这个名字在Milvus中唯一地标识了这个集合。然后，我们可以在这个`collection`上执行各种操作，如插入数据、搜索、更新和删除数据等。<br>

#### 查看集合名称:

```python
# 获取集合的名字
print(collection.name)
```

### 加载/释放集合:

前面已经介绍过集合的建立了，但偶尔你可能会见到某些代码中出现下列写法:<br>

```python
# 加载集合
collection.load()

"""你的代码"""

# 释放集合
collection.release()
```

此时，如果你没有特殊需求，忽略`collection.load()` 和 `collection.release()`即可。<br>

通常情况下，你不需要手动调用 `collection.load()` 和 `collection.release()`，Milvus 将自动管理集合的加载和释放。<br>



## Milvus中分区操作:

Milvus可以将搜索和其他操作限制在一个分区上，以提高性能。<br>

集合一般由一个或多个分区组成。在创建一个新集合时，Milvus 会自动创建一个默认分区 `_default`。Milvus 中一个集合最多有4096个分区。<br>

### Partition(分区)和Collection(集合)的关系:

Milvus 是一个开源的向量数据库，用于存储大规模的特征向量，这些向量通常由机器学习模型生成，特别是在进行相似性搜索时。在 Milvus 中，“Collection”和“Partition”是两个核心概念，它们在组织数据时扮演着重要的角色。<br>

- **Collection（集合）**：在 Milvus 中，Collection 类似于传统关系型数据库中的“表（table）”。它是最顶层的数据组织单位，用于存储相同特征的数据。比如，一个 Collection 可以是“用户的脸部特征”，所有的用户脸部特征向量都存储在这个 Collection 中。

- **Partition（分区）**：Partition 是 Collection 下的一个子集💦💦💦，它可以帮助用户更细粒度地管理 Collection 中的数据。通过 Partition，用户可以根据某些特征将数据进一步细分，以优化查询效率。比如，在“用户的脸部特征”这个 Collection 中，我们可以根据地理位置、注册时间等属性为数据创建不同的 Partition。

**举例说明**：<br>

想象一个电商网站的推荐系统，我们要为每个用户保存其浏览商品的特征向量，以便执行相似商品的推荐。<br>

- **Collection**：可以创建一个名为“用户商品浏览特征”的 Collection，所有用户浏览商品的特征向量都将存储在这里。

- **Partitions**：如果电商网站是全球性的，用户遍布世界各地，那么可以根据地区创建 Partition，如“北美区用户”，“欧洲区用户”，“亚洲区用户”等，这样在进行商品推荐时，可以只在用户所在地区的 Partition 中搜索，从而提高搜索效率。<br>

这样的数据组织结构既可以保持数据的管理效率，又可以在执行搜索和其他操作时提高性能。通过合理的设计 Collection 和 Partition，可以在 Milvus 中高效地处理和检索大规模向量数据。<br>


### 查看某个集合的所有分区:

```python
from pymilvus import connections, Collection
# 与default Milvus创建连接
connections.connect(host='localhost', port='19530')
# 选择集合
collection = Collection("book")
# 查看该集合的所有分区
print(f"集合book的分区有:{collection.partitions}")
```

终端显示:<br>

```log
集合book的分区有:[{"name":"_default","collection_name":"book","description":""}]
```

### 在某个集合下创建分区:

```python
from pymilvus import connections, Collection
# 与default Milvus创建连接
connections.connect(host='localhost', port='19530')
# 选择集合
collection = Collection("book")
# 在集合中建立分区
collection.create_partition("novel")

# 查看该集合的所有分区
print(f"集合book的分区有:{collection.partitions}")
```

终端显示:<br>

```log
集合book的分区有:[{"name":"_default","collection_name":"book","description":""}, {"name":"novel","collection_name":"book","description":""}]
```

注意:Milvus的集合中，分区不允许重名，如果重复创建相同命名的分区，会引发`PartitionAlreadyExistException: (code=1, message=Partition already exist.)`错误。⛔️⛔️⛔️<br>

### 判断集合中是否有某个分区:

```python
from pymilvus import connections, utility, Collection
# 连接Milvus
connections.connect(host='localhost', port='19530')
# 选定集合
collection = Collection("book")
# 判断集合中是否有某个分区
if collection.has_partition("novel"):
    print(f"集合book中有novel分区")
else:
    print(f"集合book中没有novel分区")
```

如果集合"book"中有"novel"分区，则终端显示:<br>

```log
集合book中有novel分区
```

### 删除某个集合下的分区:

在Milvus中，"删除集合的某个分区" 和 "删除集合的所有分区" 使用的方法是一样的。"删除集合的所有分区"通常需要遍历分区并逐个删除，"删除集合的某个分区"值需要根据名称删除特定分区即可。<br>

因为Milvus不提供直接删除所有分区的单个API，**这是为了确保操作的安全性和可控性，因为删除分区是一个不可逆的操作，分区中的数据也会被删除。**🪴🪴🪴🪴🪴<br>

```python
from pymilvus import connections, Collection

# 连接Milvus服务器
connections.connect(host='localhost', port='19530')

# 指定要删除分区的集合名称
collection_name = 'book'

# 获取指定名称的集合
collection = Collection(name=collection_name)

# 获取集合的所有分区名称
partition_names = collection.partitions

# 遍历分区并删除它们
for partition_name in partition_names:
    collection.drop_partition(partition_name)

# 断开与Milvus服务器的连接
connections.disconnect()
```


## utility介绍:

`pymilvus`中的`utility`模块提供了一组辅助函数，这些函数主要用于执行一些常见的、不直接涉及数据操作的任务。例如，检查集合或分区的存在、重命名集合、获取集合的统计信息等。以下是一些`utility`模块中常用函数的说明和用法：<br>

### 查看Milvus中所有集合

```python
from pymilvus import connections, utility
connections.connect(host='localhost', port='19530')
print(utility.list_collections())   # 返回值为集合名(str)组成的list
```

`list_collections(using='default')`还可以设置数据库名称；<br>

### 查看Milvus中是否有某个集合

```python
from pymilvus import connections, utility
connections.connect(host='localhost', port='19530')
res = utility.has_collection("book")
print(res)  # 如果集合存在，输出True；否则输出False。
```

`has_collection(name, using='default')`：<br>

- `name`：集合的名称。

- `using`：连接的别名。

### 删除指定名称的集合：

```python
from pymilvus import connections, utility
connections.connect(host='localhost', port='19530')
utility.drop_collection("some_collection")
```

`drop_collection(name, using='default')`：<br>

- `name`：要删除的集合的名称。

- `using`：连接的别名。

### 集合重命名:

```python
from pymilvus import connections, utility
connections.connect(host='localhost', port='19530')
utility.rename_collection("old_collection_name", "new_collection_name")
```

`rename_collection(old_name, new_name, timeout=None, using='default')`：<br>

- `timeout`：超时时间（可选）。

- `using`：连接的别名。

### 计算两组向量之间的距离:

```python
from pymilvus import connections, utility
connections.connect(host='localhost', port='19530')
distances = utility.calc_distance([[1, 2]], [[3, 4]], params={"metric": "L2"})
print(distances)  # 输出向量间的距离。
```

`calc_distance(vectors_left, vectors_right, params, timeout=None, using='default')`：

- `vectors_left`和`vectors_right`：两组要计算距离的向量。

- `params`：计算距离时使用的参数，例如距离度量方式。

- `timeout`：超时时间（可选）。

- `using`：连接的别名。

这些辅助函数简化了对Milvus集合的一些常见管理任务的处理，让用户可以更容易地与Milvus集合进行交互。在使用这些函数时，通常需要确保已经通过`connections.connect`与Milvus数据库建立了连接。<br>

### 查看集合属性:

假设你使用了以下代码创建了一个名为`book`的集合:<br>

```python
from pymilvus import Collection, FieldSchema, CollectionSchema, DataType, connections, utility

# 连接Milvus
connections.connect(host='localhost', port='19530')

# 定义集合架构
schema = CollectionSchema(fields=[
    FieldSchema("int64", DataType.INT64, description="int64", is_primary=True),
    FieldSchema("float_vector", DataType.FLOAT_VECTOR, is_primary=False, dim=128),
])

# 架构实例化为一个名为"book"的集合
collection = Collection(name="book", schema=schema)
```

检查默认数据库(`default`)中是否有"book"集合:<br>

```python
from pymilvus import connections, utility

connections.connect(host='localhost', port='19530')
res = utility.has_collection("book")
print(res)  # 没查到会返回False

collections = utility.list_collections()
print(collections)  # 输出所有集合的名称列表。
```

终端显示:<br>

```log
True
['book', 'search_article_in_medium']
```

### 设置/查看集合的过期时间:

设置集合的过期时间(单位为 "秒")需要使用`set_properties`语句，具体操作如下:<br>

```python
from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType
# 连接milvus
connections.connect(host='localhost', port='19530')
# 定义字段
fields = [
    FieldSchema("film_id", DataType.INT64, is_primary=True),
    FieldSchema("films", dtype=DataType.FLOAT_VECTOR, dim=128)
    ]
# 定义集合架构
schema = CollectionSchema(fields=fields)
# 利用集合架构实例化一个集合
collection = Collection("test_set_properties", schema)
# 设置集合的过期时间
collection.set_properties({"collection.ttl.seconds": 1200})
```

设置完成后，想要查看是否设置成功，可以运行下列代码:<br>

```python
from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType
# 连接milvus
connections.connect(host='localhost', port='19530')
# 选定集合
collection = Collection("test_set_properties")
print(f"the name of collection is :\n{collection.name}\n")
# 获取集合的properties属性
expiration_time = collection.describe().get("properties")
print(f"the expiration time of collection is :\n{expiration_time}\n")
print(f"the format of expiration_time is :\n{type(expiration_time)}\n")

# 将"过期时间"属性转为可操作格式--字符串
expiration_time_string = expiration_time.__str__()
print(expiration_time_string)
print(type(expiration_time_string))
```

终端显示:<br>

```txt
the name of collection is :
test_set_properties

the expiration time of collection is :
[key: "collection.ttl.seconds"
value: "60"
]

the format of expiration_time is :
<class 'google._upb._message.RepeatedCompositeContainer'>

[key: "collection.ttl.seconds"
value: "60"
]
<class 'str'>
```

🐳🐳🐳设置过期时间后查看到的结果，格式比较奇怪🤨🤨🤨，只当作参考，毕竟"过期时间"这个概念是Milvus新添加的功能，可能Milvus还没有彻底完善。<br>

### Milvus能否设置某条数据的过期时间？





## 分批向Milvus插入数据:


## Milvus中的数据操作:

### upsert():

### 使用upsert时的注意事项:

官方文档:<br>

```txt
Limits
Updating primary key fields is not supported by upsert().
upsert() is not applicable and an error can occur if autoID is set to True for primary key fields.
```

在这段文档中，提到了Milvus数据库的一些操作限制。<br>

首先解释一下背景知识：<br>

- **Primary Key（主键）**：在数据库中，主键是唯一标识表中每一条记录的字段。它的值必须是唯一的，并且不允许为空。

- **upsert() 操作**：`upsert` 是“update”和“insert”的结合词，指的是一种数据库操作，如果记录不存在，就执行插入（insert）操作；如果记录已经存在，则更新（update）这条记录。在一些数据库系统中，`upsert` 通常通过一个特定的命令或者一组操作来实现。

- **autoID**：是一个设置项，当设置为True时，意味着数据库会自动为每条记录生成一个唯一的主键ID。当用户插入新记录时不需要（也不能）手动指定主键ID，系统会自动生成。

根据你提供的文档内容：<br>

1. **更新主键字段不被支持**：这说明在Milvus数据库中，一旦记录被创建，并且分配了主键值，你就不能使用`upsert()`操作来改变这个主键字段的值。主键一旦设定，就是不可更改的。

2. **如果为主键字段设置了autoID为True，则upsert()不适用**：这表示如果你在定义数据模型时设置了主键字段的`autoID`为True，意味着主键值是由系统自动生成的，那么你不能使用`upsert()`操作。这可能是因为`upsert()`操作需要明确指定哪一条记录将被更新，如果主键是自动生成的，那么在执行`upsert()`操作时，系统可能无法确定要更新的确切记录，因此会引发错误。

总结起来，Milvus在使用自动生成主键的配置下，不支持使用`upsert()`操作来更新或插入数据，你需要在插入数据时避免对主键字段进行操作，或者在设计数据模型时不使用autoID特性。<br>


## 删除实体:

Milvus支持通过主键或复杂布尔表达式来删除实体。**通过主键删除实体比通过复杂布尔表达式删除它们要快得多、也更轻便**🫠🫠🫠。这是因为Milvus在通过复杂布尔表达式删除数据时，会先执行查询操作。<br>


## Milvus数据迁移工具--MilvusDM:

MilvusDM是专门用于导入和导出Milvus数据的开源工具。<br>


## Milvus索引建立:

| 参数        | 描述                               | 选项                                  |
| ----------- | ---------------------------------- | ------------------------------------- |
| metric_type | 用于衡量向量相似度的度量类型         | 对于浮点向量：                        |
|             |                                    | L2（欧几里得距离）                    |
|             |                                    | IP（内积）                            |
|             |                                    | COSINE（余弦相似性）                  |
|             |                                    | 对于二进制向量：                      |
|             |                                    | JACCARD（杰卡德距离）                 |
|             |                                    | HAMMING（汉明距离）                   |
| index_type  | 用于加速向量搜索的索引类型            | 对于浮点向量：                        |
|             |                                    | FLAT（FLAT）                          |
|             |                                    | IVF_FLAT（IVF_FLAT）                  |
|             |                                    | IVF_SQ8（IVF_SQ8）                    |
|             |                                    | IVF_PQ（IVF_PQ）                      |
|             |                                    | GPU_IVF_FLAT*（GPU_IVF_FLAT）         |
|             |                                    | GPU_IVF_PQ**（GPU_IVF_PQ）            |
|             |                                    | HNSW（HNSW）                          |
|             |                                    | DISKANN*（DISK_ANN）                  |
|             |                                    | 对于二进制向量：                      |
|             |                                    | BIN_FLAT（BIN_FLAT）                  |
|             |                                    | BIN_IVF_FLAT（BIN_IVF_FLAT）          |
| params      | 特定于索引的构建参数                   | 查看内存中索引和磁盘上索引了解更多信息。 |

* DISKANN 需要满足一定的先决条件。详情请见磁盘上索引。
* 当你安装了启用了GPU功能的Milvus时，GPU_IVF_FLAT 和 GPU_IVF_PQ才可用。

### index_type详细解释:

1. **FLAT（暴力搜索）**
   - 描述：不使用任何索引，直接计算查询向量与数据库中所有向量之间的距离。
   - 适用场景：适用于小规模数据集，或者在索引构建时间和存储空间成本受限时。

2. **IVF_FLAT（倒排文件）**
   - 描述：数据集被划分为若干个聚类（称为量化中心），在搜索时，只计算查询向量与这些量化中心的距离，然后只搜索最近的若干个量化中心对应的向量。
   - 适用场景：较大规模的数据集，可以显著减少搜索时的计算量。

3. **IVF_SQ8 / IVF_SQ8H（倒排文件+量化）**
   - 描述：在IVF的基础上，数据向量会被进一步量化，降低存储空间和加速搜索。
   - 适用场景：数据集规模较大且需要更高搜索效率和较低存储成本的场合。

4. **IVF_PQ（倒排文件+乘积量化）**
   - 描述：结合了倒排索引和乘积量化的方法，通过将每个向量分割为若干段，然后对每段分别进行量化，以减少存储空间和提升搜索速度。
   - 适用场景：适用于大规模数据集，需要在搜索精度和搜索速度之间取得平衡。

5. **HNSW（分层导航小世界）**
   - 描述：一种基于图的索引方法，将数据点组织成层次化的图结构，搜索时通过图的层次结构导航以快速找到最近邻。
   - 适用场景：适合于高维数据的近似最近邻搜索，尤其在需要高查询性能时。

6. **ANNOY（Approximate Nearest Neighbors Oh Yeah）**
   - 描述：使用树结构进行索引，每棵树都是在数据点之间随机分割的空间，在搜索时并行遍历多棵树来找到最近的点。
   - 适用场景：在查询时间比索引构建时间更重要的情况下非常有用，例如在推荐系统中。

在使用Milvus时，选择合适的索引类型需要考虑数据规模、向量维度、搜索效率要求、内存与存储空间限制等因素。通常，为了确定哪种索引类型最适合特定的应用场景，可能需要进行一些实验和基准测试。在创建集合（collection）时通过参数来指定索引类型，并且可以在数据插入后构建索引。构建索引是一个可以在插入数据的同时或者在数据插入完成后进行的异步操作。<br>


## Milvus使用FAQ:

### 我使用的是Ubuntu18.4，我使用的是CPU版本Milvus，Milvus中存储了50万条向量数据，我的向量都是使用Electra转化的。我检索一条数据的耗时竟然需要0.2s，是否有方法提升检索速度？使用维度更低的模型转换词向量如何？我的数据都是中文文本。

Milvus 是一个开源的向量数据库，用于存储、检索和分析向量数据，特别适合处理大规模、高维度的数据。如果你在使用 Milvus 进行检索操作时遇到了性能瓶颈，以下是一些可能的优化策略：

1. **优化索引类型和参数**：
   Milvus 支持多种索引类型，如 IVF_FLAT、IVF_SQ8、HNSW 等。每种索引类型都有其优缺点，并且可以根据数据特性进行调整。例如，对于高维数据，HNSW 可能是一个更好的选择。另外，优化索引的构建参数，如 nlist 或 M，也可能提高检索效率。

2. **调整查询参数**：
   当执行查询时，可以调整 `top_k` 和 `nprobe` 参数。`nprobe` 是在索引中搜索的桶的数量，增加 `nprobe` 可以提高检索精度，但会减慢检索速度。根据需求调整 `nprobe` 可以在速度与准确性之间取得平衡。

3. **减少向量维度**：
   使用维度更低的模型来转换词向量可能会加快检索速度，因为低维向量占用的空间更少，计算距离更快。但是，这也可能会影响检索结果的质量。可以考虑使用一些降维技术，如 PCA 或 t-SNE，但这应该在确保不会过度损害向量表示的情况下进行。

4. **优化硬件使用**：
   即便你使用的是CPU版本的Milvus，但确保你的服务器或者你的环境具有足够的CPU资源来处理这些请求。如果你的CPU资源紧张，这可能会导致查询速度下降。

5. **批量查询**：
   如果可能的话，将多个查询批量化可以显著提高吞吐量，因为这样可以在单个查询操作中复用更多的资源和计算。

6. **更新Milvus版本**：
   如果你使用的是旧版本的Milvus，考虑升级到最新版本。随着项目的发展，新版本通常会包含性能改进和新特性。

7. **分析瓶颈**：
   使用工具（如 Milvus 的监控系统、Linux 的 perf 工具等）来识别瓶颈所在。这可能是 CPU、内存、磁盘 I/O 或者网络。

8. **合理设置预加载数据量**：
   通过 `load_collection` 接口预加载数据到内存中可以提高检索速度。但是，预加载过多的数据可能会导致内存不足，从而影响性能。

最后，具体优化措施需要基于你的实际情况（如查询类型、系统资源、数据特性等）来决定。建议从监控工具和日志中收集信息，逐一尝试以上建议，并观察每次调整对性能的影响。

### 我使用的是Ubuntu18.4，我使用的是CPU版本Milvus，我使用的是pymilvus 2.x版本，我应该如何使用pymilvus进行批量查询？

在使用`pymilvus`进行批量查询时，主要步骤是创建一个搜索参数字典，并使用`search`函数进行查询。以下是使用pymilvus 2.x版本进行批量查询的大致步骤：<br>

1. **连接到Milvus服务器**：首先，确保你已经启动了Milvus服务，然后使用`pymilvus`连接到服务。

2. **准备数据**：准备你想要查询的向量数据。

3. **构造查询**：构造一个搜索参数字典，指定你想要的搜索参数，例如查询向量、topK（返回最近邻的数量）和指标类型等。

4. **执行搜索**：使用集合（collection）对象的`search`方法执行查询。

5. **处理结果**：处理返回的结果，这通常包括距离分数和对应的ID。

以下是一个简单的示例代码：<br>

```python
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

# 第1步：连接到Milvus服务器
connections.connect("default", host='127.0.0.1', port='19530')

# 检查连接是否成功
print(f"Connected to Milvus: {utility.ping('default')}")

# 第2步：指定你的集合名称
collection_name = 'example_collection'

# 这里假设你的集合已经存在并且你已经知道字段名称和参数
# 如果需要，也可以创建新的集合

# 第3步：准备你的查询向量
# 这应该是一个二维数组，其中每个内部数组是一个查询向量
query_vectors = [[0.1, 0.2, ...], [0.2, 0.3, ...], ...]

# 第4步：构造查询
# 在这里指定你想要搜索的参数
search_params = {
    "metric_type": "L2",  # 或者其他距离度量类型，如 "IP"（内积）
    "params": {"nprobe": 10},
}

# 执行批量查询
# topK是返回结果的数量，len(query_vectors)是查询的向量数
results = collection.search(
    data=query_vectors,
    anns_field='embedding_field',  # 这里的'embedding_field'应该替换为你的向量字段名称
    param=search_params,
    limit=10,  # topK值
    expr=None,
    partition_names=None,
    output_fields=None,
    timeout=None,
    **kwargs
)

# 第5步：处理结果
# 打印查询结果
for result in results:
    for hit in result:
        print(f"ID: {hit.id}, Distance: {hit.distance}")

# 断开连接
connections.disconnect("default")
```

请根据你的集合和字段进行相应的替换。特别是，你需要替换`example_collection`为你的集合名称，`embedding_field`为包含向量的字段名称。<br>

还要注意，这只是一个示例，你可能需要根据你的集合配置和搜索需求调整代码中的参数。例如，你可能需要根据实际情况调整连接参数、搜索参数等。<br>

### flush()后create_index()卡住:

建议使用`top`指令查看CPU状态，查看内存情况，以笔者为例:<br>

| PID  | USER | PR | NI |    VIRT  |   RES  |  SHR | S | %CPU | %MEM |    TIME+   | COMMAND          |
|------|------|----|----|----------|--------|------|---|------|------|------------|------------------|
| 5374 | root | 20 |  0 |  973748  | 66088  | 3176 | R |100.3 |  0.4 | 78390:32   | node             |
| 5825 | root | 20 |  0 |  975028  | 65504  | 1640 | R |100.3 |  0.4 | 78385:25   | node             |
| 5677 | root | 20 |  0 |  833204  | 63768  | 1500 | R |100.0 |  0.4 | 78389:38   | node             |
|29422 | root | 20 |  0 | 8926256  | 846316 | 94696| S |  3.7 |  5.2 |  823:52.92 | milvus           |
|  843 | root | 10 |-10 |  154384  | 17160  |  816 | S |  1.3 |  0.1 |  1092:45   | AliYunDunMonito  |
|29018 | root | 20 |  0 |  720756  | 10196  | 7676 | S |  0.7 |  0.1 |    4:16.82 | containerd-shim  |

😡😡😡笔者在运行下列代码时，发现每次运行都卡在`create_index`不动，思索了好久，才发现是CPU占用的问题，我在运行下列代码的时候CPU占用为400%，而我租用的服务器一共只有4个核，所以会卡住，**处于等待状态**。<br>

```python
# ...省略上文
# 假设插入100条数据，维度为128
data = [
    [i for i in range(100)],
    [[random.random() for _ in range(128)] for _ in range(100)],
]
# 插入数据
demo_collection.insert(data)

# 刷新数据
demo_collection.flush()

# 建立索引
index_param = {
    "index_type": 'IVF_FLAT',
    "params": {"nlist": 10},
    "metric_type": 'L2'}
print(f"开始为向量建立索引，索引建立较慢，请稍等... ...")
demo_collection.create_index('float_vector_field', index_param)
print("\nCreated index:\n{}".format(demo_collection.index().params))

print("\n数据中的实体数量为:")
print(demo_collection.num_entities)
# ...省略下文
```

于是，我果断kill掉了前3个node进程，毕竟是租的服务器，而且我知道我的代码现在用不到nodejs的内容。<br>

如果你也有类似的情况，建议先使用`ps`命令查看这些进程(PID)的命令行参数，这可以提供一些关于进程是如何启动的信息。例如：<br>

```bash
ps -f -p 5374,5825,5677
```

这将显示每个进程的完整命令行，你可能能从中看到它们启动的脚本或是应用程序的名称。如果实在不知道，可能就需要问问同事了。<br>

### text字段的模糊匹配无法实现:

当前，笔者使用的是 `milvus v2.3.2`，该版本不支持模糊匹配，只支持前缀匹配。<br>

假设你的 `text`字段记录的是文本数据，如果你想要检索含有 "老师" 的数据("我的老师...")是无法做到的，只能支持检索到前缀为 "老师" 的文本，即 "老师很..."。<br>

代码为:<br>

```python
from config.server_settings import Milvus_Server_Config
from pymilvus import Collection, connections

def milvus_connection():
    """建立milvus连接(milvus默认为连接池形式)
    Ps: milvus的连接不需要返回值
    """
    connections.connect(host = Milvus_Server_Config['host'], port = Milvus_Server_Config['port'])

def delete_data_in_milvus_according_expr(expression, milvus_collection_name):
    """根据表达式删除milvus数据
    Args:
        expression(str): 布尔表达式, 请使用 milvus 支持的布尔表达式,例如: expr = "text == '货币三佳是t+1到账吗'"
        milvus_collection_name(str): milvus集合的名称,例如: 'standard_financial_question_collection'
    Return:
        无返回值
    """
    # 建立milvus连接,无返回值
    milvus_connection()
    # 连接milvus集合
    milvus_collection = Collection(name=milvus_collection_name)
    # 传入Expression,使用布尔表达式删除数据
    milvus_collection.delete(expression)
    # 提交更改
    milvus_collection.load()

if __name__ == "__main__":
    expr="text LIKE '老师%'"  # 只支持前缀匹配，不支持模糊匹配
    milvus_collection_name = 'standard_collection'
    delete_data_in_milvus_according_expr(expr, milvus_collection_name)
```


## pymilvus示例代码:

```python
# hello_milvus.py 展示了 PyMilvus 的基本操作，PyMilvus 是 Milvus 的 Python SDK。
# 1. 连接到 Milvus
# 2. 创建集合
# 3. 插入数据
# 4. 创建索引
# 5. 在实体上进行搜索、查询和混合搜索
# 6. 通过 PK 删除实体
# 7. 删除集合
import time

import numpy as np
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

# `fmt`和`search_latency_fmt`是字符串格式模板，用于后面的输出。
fmt = "\n=== {:30} ===\n"
search_latency_fmt = "搜索延迟 = {:.4f}s"
# 实体的数量设置为3000，维度设置为8。
num_entities, dim = 3000, 8

#################################################################################
# 1. 连接到 Milvus
# 连接`localhost:19530` 的 Milvus 服务器的 `default` 数据库
# "default" 是默认数据库
# 如果 Milvus 的地址与 `localhost:19530` 相同，你可以省略所有
# 可以省略参数直接调用：`connections.connect()`。
#
# 注意: 以下方法的 `using` 参数默认为 "default"。
print(fmt.format("开始连接到 Milvus"))
connections.connect("default", host="localhost", port="19530")

has = utility.has_collection("hello_milvus")
print(f"Milvus 中是否存在 hello_milvus 集合: {has}")

#################################################################################
# 2. 创建集合
# 我们将创建一个包含 3 个字段的集合。
# +-+------------+------------+------------------+------------------------------+
# | | 字段名称   | 字段类型   | 其他属性         |       字段描述                |
# +-+------------+------------+------------------+------------------------------+
# |1|    "pk"    |   VarChar  |  is_primary=True |      "主键字段"               |
# | |            |            |   auto_id=False  |                              |
# +-+------------+------------+------------------+------------------------------+
# |2|  "random"  |    Double  |                  |      "一个 double 字段"       |
# +-+------------+------------+------------------+------------------------------+
# |3|"embeddings"| FloatVector|     dim=8        |  "维度为 8 的 float 向量"     |
# +-+------------+------------+------------------+------------------------------+
# `pk`：一个VARCHAR类型的字段，作为主键（`is_primary=True`）。该字段不会自动生成ID（`auto_id=False`），并且最大长度为100（`max_length=100`）。
# `random`：一个DOUBLE类型的字段，用于存储浮点数。
# `embeddings`：一个FLOAT_VECTOR类型的字段，用于存储浮点数向量。向量的维度由之前的代码中定义的`dim`变量决定。

fields = [
    FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
    FieldSchema(name="random", dtype=DataType.DOUBLE),
    FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=dim)
]

# `CollectionSchema`函数用于定义一个集合的结构，它接受两个参数：
# 1. `fields`：一个字段列表，定义了集合中的数据结构。
# 2. Description：一个描述该集合的字符串。

schema = CollectionSchema(fields, "hello_milvus 是一个简单的演示，用于介绍 APIs")

print(fmt.format("创建集合 `hello_milvus`"))
hello_milvus = Collection("hello_milvus", schema, consistency_level="Strong")

################################################################################
# 3. 插入数据
# 我们将在 `hello_milvus` 中插入 3000 行数据
# 待插入的数据必须按字段组织。
#
# entities中的内容必须与字段对应，例如索引为0的值为"pk"组成的列表，索引为1的值为"random"组成
# 的列表，索引为3的值为"embeddings"组成的列表。

print(fmt.format("开始插入实体"))
rng = np.random.default_rng(seed=19530)
entities = [
    # 提供 pk 字段，因为 `auto_id` 设置为 False
    [str(i) for i in range(num_entities)],
    rng.random(num_entities).tolist(),  # 字段 random，只支持 list
    rng.random((num_entities, dim)),    # 字段 embeddings，支持 numpy.ndarray 和 list
]

insert_result = hello_milvus.insert(entities)

hello_milvus.flush()
print(f"Milvus 中的实体数量: {hello_milvus.num_entities}")  # 检查 num_entities

################################################################################
# 4. 创建索引
# 我们将为 hello_milvus 集合创建一个 IVF_FLAT 索引。
# create_index() 只能应用于 `FloatVector` 和 `BinaryVector` 字段。
print(fmt.format("开始创建 IVF_FLAT 索引"))
index = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128},
}

hello_milvus.create_index("embeddings", index)

################################################################################
# 5. 搜索、查询和混合搜索
# 数据被插入到 Milvus 并进行索引后，你可以执行：
# - 基于向量相似性的搜索
# - 基于标量筛选（布尔值、整数等）的查询
# - 基于向量相似性和标量筛选的混合搜索。
#

# 在执行查询或搜索之前，需要先加载集合到内存中，使其准备好进行搜索。
print(fmt.format("开始加载数据"))
hello_milvus.load()

# -----------------------------------------------------------------------------
# 基于向量相似性的搜索
print(fmt.format("开始基于向量相似性的搜索"))
vectors_to_search = entities[-1][-2:]
search_params = {
    "metric_type": "L2",
    "params": {"nprobe": 10},
}

start_time = time.time()
result = hello_milvus.search(vectors_to_search, "embeddings", search_params, limit=3, output_fields=["random"])
end_time = time.time()

for hits in result:
    for hit in hits:
        print(f"命中: {hit}, random 字段: {hit.entity.get('random')}")
print(search_latency_fmt.format(end_time - start_time))

# -----------------------------------------------------------------------------
# 基于标量筛选（布尔值、整数等）的查询
print(fmt.format("开始使用 `random > 0.5` 进行查询"))

start_time = time.time()
result = hello_milvus.query(expr="random > 0.5", output_fields=["random", "embeddings"])
end_time = time.time()

print(f"查询结果:\n-{result[0]}")
print(search_latency_fmt.format(end_time - start_time))

# -----------------------------------------------------------------------------
# 分页
r1 = hello_milvus.query(expr="random > 0.5", limit=4, output_fields=["random"])
r2 = hello_milvus.query(expr="random > 0.5", offset=1, limit=3, output_fields=["random"])
print(f"查询分页(limit=4):\n\t{r1}")
print(f"查询分页(offset=1, limit=3):\n\t{r2}")

# -----------------------------------------------------------------------------
# 混合搜索
print(fmt.format("开始使用 `random > 0.5` 进行混合搜索"))

start_time = time.time()
result = hello_milvus.search(vectors_to_search, "embeddings", search_params, limit=3, expr="random > 0.5", output_fields=["random"])
end_time = time.time()

for hits in result:
    for hit in hits:
        print(f"命中: {hit}, random 字段: {hit.entity.get('random')}")
print(search_latency_fmt.format(end_time - start_time))

###############################################################################
# 6. 通过 PK 删除实体
# 你可以使用布尔表达式通过它们的 PK 值删除实体。
ids = insert_result.primary_keys

expr = f'pk in ["{ids[0]}" , "{ids[1]}"]'
print(fmt.format(f"开始使用表达式 `{expr}` 进行删除"))

result = hello_milvus.query(expr=expr, output_fields=["random", "embeddings"])
print(f"使用表达式=`{expr}` 查询删除前的结果 -> 结果: \n-{result[0]}\n-{result[1]}\n")

hello_milvus.delete(expr)

result = hello_milvus.query(expr=expr, output_fields=["random", "embeddings"])
print(f"使用表达式=`{expr}` 查询删除后的结果 -> 结果: {result}\n")

###############################################################################
# 7. 删除集合
# 最后，删除 hello_milvus 集合
print(fmt.format("删除集合 `hello_milvus`"))
utility.drop_collection("hello_milvus")
```

## pymilvus简单示例:

```python
"""查看milvus集合中的量级
"""
import sys
import os
# 获取当前脚本的绝对路径
current_script_path = os.path.abspath(__file__)
# 获取当前脚本的父目录的父目录
parent_directory_of_the_parent_directory = os.path.dirname(os.path.dirname(current_script_path))
# 将这个目录添加到 sys.path
sys.path.append(parent_directory_of_the_parent_directory)

from pymilvus import Collection, connections, utility
from config.server_settings import Milvus_Server_Config

def milvus_connection():
    """建立milvus连接(milvus默认为连接池形式)
    Ps: milvus的连接不需要返回值
    """
    connections.connect(host = Milvus_Server_Config['host'], port = Milvus_Server_Config['port'])

def view_milvus_collection():
    """查看当前所连接数据库中含有的集合名称
    Return:
        milvus_collection_name(list): 返回值为集合名(str)组成的list
    """
    # 建立milvus连接,无返回值
    milvus_connection()
    
    print(f"\n当前所连接数据库中含有的集合为:")
    milvus_collection_name = utility.list_collections()
    print(milvus_collection_name)
    return milvus_collection_name

def view_milvus_collection_num_entities(milvus_collection_name):
    """查看milvus中某个集合的量级
    """
    # 建立milvus连接,无返回值
    milvus_connection()
    
    albert_collection = Collection(milvus_collection_name)
    albert_collection.load()

    num_entities = albert_collection.num_entities
    print(f"{albert_collection.name}集合中num_entities量级为:  ", num_entities)

def flush_milvus_collection(milvus_collection_name):
    """刷新milvus数据
    Args:
        milvus_collection_name(str): milvus集合的名称,例如: 'standard_financial_question_collection'
    """
    # 建立milvus连接,无返回值
    milvus_connection()
    # 连接milvus集合
    milvus_collection = Collection(name=milvus_collection_name)
    print(f"现在进行Milvus{milvus_collection.name}集合数据刷新... ...")
    # 刷新数据
    milvus_collection.flush()
    print(f"Milvus{milvus_collection.name}集合数据刷新成功~")

if __name__ == '__main__':
    # 查看当前所连接数据库中含有的集合名称
    milvus_collection_name = view_milvus_collection()
    for item in milvus_collection_name:
        # 查看milvus中某个集合的量级
        view_milvus_collection_num_entities(item)
```

## python类形式调用milvus:

`env_config/.env.local` 内容如下:<br>

```conf
# milvus连接信息
MILVUS_DB_HOST="localhost"
MILVUS_DB_PORT="19530"
```

```python
"""
File Path: vector_db/milvus_db.py
Description: 实现向量数据库Milvus类的所有操作。
Notes: 
"""
import os
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from pymilvus.client.types import LoadState
from dotenv import load_dotenv

# 以环境变量方式加载配置,正式运行时可将下列代码注释,只在脚本文件导入一次即可。
load_dotenv('env_config/.env.local')

class Milvuser():
    def __init__(self):
        """建立milvus连接(milvus默认为连接池形式)
        Ps: milvus的连接不需要返回值
        """
        connections.connect(host = os.getenv('MILVUS_DB_HOST'), port = os.getenv('MILVUS_DB_PORT'))
        
    def get_or_create_collection(self, collection_config):
        """获取或创建milvus集合
        Args:
            config(dict): 创建集合所需要的字典。
        Return:
            collection: 获取或创建的milvus集合
        """
        # 如果集合不存在就执行创建
        if not utility.has_collection(collection_config['collection_name']):
            # 定义字段
            fields = [
                FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),    # 系统自增id,随机生成，非 0,1,2,3 形式
            ]
            for field in collection_config['fieldschema']:
                if field[1] == DataType.FLOAT_VECTOR:
                    # 设置向量字段
                    fields.append(FieldSchema(name=field[0], dtype=field[1], dim=field[2]))
                else:
                    # 设置其他字段
                    fields.append(FieldSchema(name=field[0], dtype=field[1], max_length=field[2]))

            # 创建集合架构
            schema = CollectionSchema(fields=fields, description=collection_config['description'])

            # 创建集合
            collection = Collection(name=collection_config['collection_name'], schema=schema)

            # 设置索引参数
            collection.create_index(field_name=collection_config['index_field_name'], index_params=collection_config['index_params'])
        # 如果集合存在,获取集合
        else:
            collection = Collection(collection_config['collection_name'])
        # 返回创建的集合对象
        return collection

    def delete_collection(self, collection_name):
        """根据milvus的集合名称删除集合
        Notes:
            执行了删除操作返回True,没有执行返回False,即milvus中还没有该集合。
        """
        # 如果集合存在，输出True；否则输出False。
        if utility.has_collection(collection_name):
            utility.drop_collection(collection_name)
            return True
        else:
            return False

    def check_collection_list(self):
        """列出milvus中所有的集合
        """
        # 列出所有集合
        collections = utility.list_collections()
        return collections

    def check_collection_load_state(self, collection_name):
        """查看milvus中某集合的加载状态
        Notes:
            1. load_state的type为枚举类型(`enum`)。
            2. 状态分为 "Loaded"、"NotLoad"、"NotExist"、"Loading"
        """
        # 获取集合的内存加载状态
        load_state = utility.load_state(collection_name)
        if load_state == LoadState.Loaded:
            return  "Loaded"
        elif load_state == LoadState.NotLoad:
            return  "NotLoad"
        elif load_state == LoadState.Loading:
            return  "Loading"
        # 集合不存在时
        else:
            return "NotExist"

    def check_collection_entity_num(self, collection_name):
        """获取milvus集合中的实体数量
        Args:
            collection_name(str): milvus集合的名称,例如: 'standard_financial_question_collection'
        """
        # 如果集合存在，输出True；否则输出False。
        if utility.has_collection(collection_name):
            # 连接milvus集合
            milvus_collection = Collection(name=collection_name)
            num_entities = milvus_collection.num_entities
            # 可通过 f"\n{milvus_collection.name}集合中num_entities量级为: {num_entities}" 打印查看效果
            return num_entities
        else:
            return False
    
    def load_collection_to_memory(self, collection_name):
        """将集合加载到内存
        Notes:
            从内存检索的速度快于从硬盘检索,所以milvus需要将数据加载到内存。
        """
        # 如果集合存在，输出True；否则输出False。
        if utility.has_collection(collection_name):
            collection = Collection(collection_name)
            collection.load()

    def release_collection_from_memory(self, collection_name):
        """将集合从内存释放
        Notes:
            1. 在查询结束后,可以选择将集合从内存释放,减少内存占用。
            2. 无论集合是否已加载到内存,都可以执行 `release()`。
        """
        # 如果集合存在，输出True；否则输出False。
        if utility.has_collection(collection_name):
            collection = Collection(collection_name)
            collection.release()

    def insert_data(self, collection, data):
        """
        将文本和向量插入 Milvus 集合。
        Args:
            collection: Milvus 集合对象。
            data(list): 数据列表。
        Notes:
            1. data中每一项参数都是列表,Milvus是以列表形式插入数据的,
               例如要插入10条数据,那么text字段的列表中就有10条数据,同理source_from字段的列表中也有10条数据。
            2. 执行数据插入集合中,无返回值。
            3. Milvus不执行向量化操作,需要先将文本转为向量,然后执行向量插入操作。
            4. 插入顺序一定要与构建的collection顺序一致!!!
        """
        # 将数据插入到集合中
        collection.insert(data)
        print(f"现在进行数据刷新... ...")
        # 刷新数据
        collection.flush()
        print(f"现在进行数据刷新成功~")

    def search_data(self, search_config):
        """从milvus集合中查找相似text
        Args:
            search_config (dict): 搜索配置字典，包括以下键：
                - collection_name (str): milvus中集合名称
                - data_vec (list): 向量化数据
                - anns_field (str): 用于从集合中检索的向量字段名称
                - search_params (dict): 检索方式参数字典，包括以下键：
                    - metric_type (str): 距离度量类型
                    - top_K (int): 返回的最近邻居数量
                    - params (dict): 其他检索参数字典，包括以下键：
                        - radius (float): 检索半径
                        - range_filter (float): 范围过滤器
                - limit (int): 返回结果的数量限制
                - output_fields (list): 输出的字段列表
        Return:
            all_search_result (dict): 相似text组成的字典。
        """
        collection_name = search_config["collection_name"]
        data_vec = search_config["data_vec"]
        anns_field = search_config["anns_field"]
        search_params = search_config["search_params"]
        limit = search_config["limit"]
        output_fields = search_config["output_fields"]
        
        # 查看集合的内存加载状态,只有集合处于内存中才能进行检索。
        load_state = self.check_collection_load_state(collection_name)

        # 检查集合的加载状态,状态分为 "Loaded"、"NotLoad"、"NotExist"、"Loading"
        # 这里只区分加载/未加载两种状态。
        if load_state == "NotLoad":
            # 获取集合对象
            collection = Collection(collection_name)
            # 将集合加载到内存
            collection.load()
        else:
            # 获取集合对象
            collection = Collection(collection_name)

        # 构建search参数
        search_result = collection.search(data_vec, anns_field, search_params, limit=limit, output_fields=output_fields)

        # search_result是一个<class 'pymilvus.client.abstract.SearchResult'>类，但可像列表一样调用，查询结果在索引0。
        search_result_extract = search_result[0]
        # 将最终返回的结果放入一个字典
        all_search_result = {}
        for idx, item in enumerate(search_result_extract,1):
            each_res = item.__dict__    # 结果类似：{'id': 263663, 'distance': 1.0, 'fields': {'id': 263663, 'text': '老师'}}，类型为<class 'dict'>
            idx_name = f"结果{idx}"
            all_search_result[idx_name] = each_res

        return all_search_result

    def delete_data_according_expr(self, expression, collection_name):
        """根据表达式删除milvus数据
        Args:
            expression(str): 布尔表达式, 请使用 milvus 支持的布尔表达式,例如: expr = "text == '货币三佳是t+1到账吗'"
            milvus_collection_name(str): milvus集合的名称,例如: 'standard_financial_question_collection'
        Return:
            无返回值
        Notes:
            1. milvus只允许根据表达式删除数据。
            2. milvus不支持单独修改某条数据的某个字段。
            3. milvus更改数据其实是删除然后重新插入的操作。
        """
        # 获取集合对象
        milvus_collection = Collection(collection_name)
        # 传入Expression,使用布尔表达式删除数据
        milvus_collection.delete(expression)
        # 提交更改
        milvus_collection.load()

if __name__ == '__main__':
    # 配置集合字典
    bank_collection_config = {
        "collection_name": "bank_collection",
        "description": "search text",
        "fieldschema": [
            ["text", DataType.VARCHAR, 2000],
            ["source_from", DataType.VARCHAR, 2000],
            ["text_vector", DataType.FLOAT_VECTOR, 768]
            ],
        "index_params": {
            'metric_type': "COSINE",
            'index_type': "HNSW",
            'params': {'efConstruction': 10, 'M':60}
            },
        "index_field_name" : "text_vector"
    }

    # 文本的向量
    data_vec = []
    search_config = {
        "collection_name" : "bank_collection",
        # 检索用到的配置
        "search" :{
            # 文本的向量
            "data_vec" : data_vec,
            # 用于从集合中检索的向量字段名称
            "anns_field": "text_vector",
            # param即检索方式
            "search_params" : {
                "metric_type": 'COSINE',
                "top_K":50,
                "params": {
                    # radius < distance <= range_filter，distance为相似度，milvus计算相似度时，如果完全相同，得到的结果可能是1.0000001192092896(有时是整整的 1.0)，所以，如果你想要返回相同数据，可以将"range_filter" : 1.0注释。
                    "radius": 0,
                    "range_filter" : 1.01
                }
            },
            "limit": 40,
            # 输出的字段
            "output_fields": ["id", "text", "source_from"]
        }
    }
```

## query_iterator:

```python
"""
Description: 测试milvus的 `query_iterator` 函数,方便后期手动迁移出所有数据。
适用场景: 
个人的milvus中bank集合中有几十万条数据,我想要为这个集合重新添加一列"doc"，应该怎么做呢？

我想要尽量避免再把数据向量化的时间。
Notes: 
1. milvus 版本是 2.3.2依旧可用这个方法,只需要安装 pymilvus 2.4.x 就行。
2. `query` 函数只支持最大返回16384条数据,所以需要使用 `query_iterator` 函数。
"""
import sys
import os

# 获取当前脚本的绝对路径
current_script_path = os.path.abspath(__file__)
# 获取当前脚本的父目录的父目录
parent_directory_of_the_parent_directory = os.path.dirname(os.path.dirname(current_script_path))
# 将这个目录添加到 sys.path
sys.path.append(parent_directory_of_the_parent_directory)

from dotenv import load_dotenv
from pymilvus import connections, Collection


# 加载环境变量
load_dotenv('env_config/.env.local')

connections.connect(host = os.getenv('MILVUS_DB_HOST'), port = os.getenv('MILVUS_DB_PORT'))

collection = Collection("bank_collection")  

iterator = collection.query_iterator(
    batch_size=10, # Controls the size of the return each time you call next()
    expr=None,
    output_fields=["text","answer"]
)

results = []

while True:
    result = iterator.next()
    if len(result) == 0:
        iterator.close()
        break

    results.extend(result)
    
print(len(results))

print(results[:3])
```
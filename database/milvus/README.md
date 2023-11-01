# Milvus
- [Milvus](#milvus)
  - [Milvus安装:](#milvus安装)
  - [查看Milvus是否运行:](#查看milvus是否运行)
  - [连接Milvus:](#连接milvus)
  - [为Milvus设置密码:](#为milvus设置密码)
  - [更改milvus中数据的存储位置：](#更改milvus中数据的存储位置)
  - [关闭Milvus standalone:](#关闭milvus-standalone)
  - [安装Milvus Python SDK:](#安装milvus-python-sdk)
    - [补充说明Install Milvus Python SDK是什么意思？其中的SDK表示什么:](#补充说明install-milvus-python-sdk是什么意思其中的sdk表示什么)
  - [利用pymilvus与Milvus数据库建立/断开连接:](#利用pymilvus与milvus数据库建立断开连接)
  - [利用pymilvus管理数据库:](#利用pymilvus管理数据库)
    - [创建数据库:](#创建数据库)
    - [查找 Milvus 集群中的所有现有数据库:](#查找-milvus-集群中的所有现有数据库)
    - [使用数据库:](#使用数据库)
    - [删除数据库:](#删除数据库)
  - [pymilvus示例代码:](#pymilvus示例代码)
    - [导入模块和库:](#导入模块和库)
    - [定义格式变量:](#定义格式变量)
    - [定义实体数量和向量维度:](#定义实体数量和向量维度)
    - [连接到Milvus服务器:](#连接到milvus服务器)
    - [检查集合是否存在:](#检查集合是否存在)
    - [定义字段列表:](#定义字段列表)
    - [定义集合的结构:](#定义集合的结构)
    - [创建新的集合:](#创建新的集合)
    - [插入实体:](#插入实体)
    - [创建索引:](#创建索引)
    - [加载集合:](#加载集合)
    - [基于向量相似性的搜索:](#基于向量相似性的搜索)
    - [基于标量过滤的查询:](#基于标量过滤的查询)
    - [分页查询:](#分页查询)
    - [混合搜索:](#混合搜索)
    - [获取插入实体的主键:](#获取插入实体的主键)
    - [构建删除表达式:](#构建删除表达式)
    - [查询并打印删除前的实体:](#查询并打印删除前的实体)
    - [删除实体:](#删除实体)
    - [查询并打印删除后的实体:](#查询并打印删除后的实体)
    - [删除集合:](#删除集合)

## Milvus安装:

1. 下载 YAML 文件;

创建一个文件夹存放`docker-compose.yml`，注意将文件夹名称定义为易识别形式，时间长后你自己都不知道这个文件是什么。笔者的路径为`/root/`。<br>

```bash
wget https://github.com/milvus-io/milvus/releases/download/v2.3.2/milvus-standalone-docker-compose.yml -O docker-compose.yml
```

1. 在与` docker-compose.yml` 文件相同的目录中，运行以下命令启动 Milvus:

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


## 利用pymilvus与Milvus数据库建立/断开连接:

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




```python

```


## 利用pymilvus管理数据库:

与传统的数据库引擎类似，你也可以在 Milvus 创建数据库，并为某些用户分配管理数据库的特权。然后，这些用户有权管理数据库中的集合。Milvus 集群最多支持64个数据库。<br>


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

### 使用数据库:

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

### 删除数据库:

若要删除数据库，必须首先删除其所有集合。否则，删除操作将失败。<br>

```python
db.drop_database("book")

db.list_database()

# Output:
# ['default']
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

fmt = "\n=== {:30} ===\n"
search_latency_fmt = "搜索延迟 = {:.4f}s"
num_entities, dim = 3000, 8

#################################################################################
# 1. 连接到 Milvus
# 为位于 `localhost:19530` 的 Milvus 服务器添加一个新的连接别名 `default`
# 实际上 "default" 别名在 PyMilvus 中是内置的。
# 如果 Milvus 的地址与 `localhost:19530` 相同，你可以省略所有
# 参数并调用该方法，例如：`connections.connect()`。
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
fields = [
    FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
    FieldSchema(name="random", dtype=DataType.DOUBLE),
    FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=dim)
]

schema = CollectionSchema(fields, "hello_milvus 是一个简单的演示，用于介绍 APIs")

print(fmt.format("创建集合 `hello_milvus`"))
hello_milvus = Collection("hello_milvus", schema, consistency_level="Strong")

################################################################################
# 3. 插入数据
# 我们将在 `hello_milvus` 中插入 3000 行数据
# 待插入的数据必须按字段组织。
#
# insert() 方法返回：
# - 如果 schema 中的 auto_id=True，则由 Milvus 自动生成的主键；
# - 如果 schema 中的 auto_id=False，则返回实体中已有的主键字段。

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

# 在进行搜索或查询之前，你需要将 `hello_milvus` 中的数据加载到内存中。
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

接下来详细解释上述代码各部分的作用：<br>

### 导入模块和库:

```python
import time
import numpy as np
from pymilvus import (
      connections,
      utility,
      FieldSchema, CollectionSchema, DataType,
      Collection,
)
```

- `time`: Python的标准库，用于处理时间。

- `numpy as np`: 一个用于大量数据计算的Python库。

- `pymilvus`: Milvus的Python客户端，用于与Milvus服务器进行交互。

### 定义格式变量:

```python
fmt = "\n=== {:30} ===\n"
search_latency_fmt = "search latency = {:.4f}s"
```

- `fmt`和`search_latency_fmt`是字符串格式模板，用于后面的输出。

### 定义实体数量和向量维度:

```python
num_entities, dim = 3000, 8
```

- `num_entities`：代表实体的数量，这里设置为3000。

- `dim`：代表向量的维度，这里设置为8。

### 连接到Milvus服务器:

```python
print(fmt.format("start connecting to Milvus"))
connections.connect("default", host="localhost", port="19530")
```

- 使用`fmt.format("start connecting to Milvus")`格式化并打印连接开始信息。

- `connections.connect()`用于连接到Milvus服务器，参数`"default"`是连接的别名，`host="localhost"`指定了服务器地址，`port="19530"`指定了服务器端口。

### 检查集合是否存在:

```python
has = utility.has_collection("hello_milvus")
print(f"Does collection hello_milvus exist in Milvus: {has}")
```

- `utility.has_collection("hello_milvus")`：检查名为"hello_milvus"的集合是否在Milvus中存在。

- 使用f-string打印查询结果。

**通过这段代码，可以学到如何使用pymilvus库连接到Milvus服务器并简单地检查一个集合是否存在。**<br>

### 定义字段列表:

```python
fields = [
      FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
      FieldSchema(name="random", dtype=DataType.DOUBLE),
      FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=dim)
]
```

这里定义了三个字段：<br>

- `pk`：一个VARCHAR类型的字段，作为主键（`is_primary=True`）。该字段不会自动生成ID（`auto_id=False`），并且最大长度为100（`max_length=100`）。

- `random`：一个DOUBLE类型的字段，用于存储浮点数。

- `embeddings`：一个FLOAT_VECTOR类型的字段，用于存储浮点数向量。向量的维度由之前的代码中定义的`dim`变量决定。

### 定义集合的结构:

```python
schema = CollectionSchema(fields, "hello_milvus is the simplest demo to introduce the APIs")
```

`CollectionSchema`函数用于定义一个集合的结构，它接受两个参数：<br>

- `fields`：一个字段列表，定义了集合中的数据结构。

- 描述：一个描述该集合的字符串。

### 创建新的集合:

```python
print(fmt.format("Create collection `hello_milvus`"))
hello_milvus = Collection("hello_milvus", schema, consistency_level="Strong")
```

- 使用`fmt.format("Create collection `hello_milvus`")`格式化并打印创建集合的开始信息。

- `Collection`函数用于在Milvus中创建新的集合。它接受三个参数：

    - 集合的名称，这里是`"hello_milvus"`。
    
    - 之前定义的`schema`，即集合的结构。
    
    - `consistency_level`参数，这里设置为`"Strong"`，这意味着Milvus会确保写操作的一致性。

**经过这段代码，我们可以学到如何使用`pymilvus`库定义集合的结构，并在Milvus中创建一个新的集合。**<br>



### 插入实体:

```python
print(fmt.format("Start inserting entities"))
rng = np.random.default_rng(seed=19530)
entities = [
      [str(i) for i in range(num_entities)],
      rng.random(num_entities).tolist(),
      rng.random((num_entities, dim)),
]
```

- 使用`fmt.format("Start inserting entities")`格式化并打印插入实体的开始信息。

- `rng = np.random.default_rng(seed=19530)`：创建一个随机数生成器。`seed=19530`确保每次运行时都可以得到相同的随机数。

- `entities`是一个列表，其中包含三个子列表/数组，分别对应于之前定义的三个字段。

    - 第一个列表：主键字段的值。因为`auto_id`之前设置为`False`，所以需要为每个实体提供一个唯一的主键。

    - 第二个列表：`random`字段的值。使用随机数生成器为每个实体生成一个随机浮点数。
      
    - 第三个数组：`embeddings`字段的值。使用随机数生成器为每个实体生成一个随机浮点数向量。

```python
insert_result = hello_milvus.insert(entities)
```

- 使用`insert`方法将`entities`插入到`hello_milvus`集合中。

```python
hello_milvus.flush()
print(f"Number of entities in Milvus: {hello_milvus.num_entities}")
```

- `hello_milvus.flush()`：确保所有的插入操作都已提交到Milvus。

- 打印`hello_milvus`集合中的实体数量，以确认插入操作成功。

### 创建索引:

```python
print(fmt.format("Start Creating index IVF_FLAT"))
index = {
      "index_type": "IVF_FLAT",
      "metric_type": "L2",
      "params": {"nlist": 128},
}
```

- 使用`fmt.format("Start Creating index IVF_FLAT")`格式化并打印创建索引的开始信息。

- 定义索引参数。这里选择了`IVF_FLAT`索引类型，它适用于浮点数向量。`metric_type`为`L2`，表示使用L2距离来测量向量之间的相似性。`params`指定了索引的额外参数，这里设置`nlist`为128。

```python
hello_milvus.create_index("embeddings", index)
```

- 使用`create_index`方法为`embeddings`字段创建索引。这使得向量搜索操作更快、更高效。

总结，这段代码首先向Milvus的`hello_milvus`集合插入随机生成的实体，然后为`embeddings`字段创建一个`IVF_FLAT`索引，以加速向量搜索操作。<br>


### 加载集合:

```python
print(fmt.format("Start loading"))
hello_milvus.load()
```

在执行查询或搜索之前，需要先加载集合到内存中，使其准备好进行搜索。<br>

### 基于向量相似性的搜索:

```python
print(fmt.format("Start searching based on vector similarity"))
vectors_to_search = entities[-1][-2:]
search_params = {
      "metric_type": "L2",
      "params": {"nprobe": 10},
}
```

- 选择要搜索的向量。这里选择了之前插入的最后两个向量作为查询。

- 定义搜索参数。`metric_type`为`L2`，表示使用L2距离。`params`字典中的`nprobe`参数决定了搜索时考虑的桶数量。

```python
start_time = time.time()
result = hello_milvus.search(vectors_to_search, "embeddings", search_params, limit=3, output_fields=["random"])
end_time = time.time()
```

- 记录搜索开始时间。

- 使用`search`方法搜索最相似的向量。`limit=3`表示为每个查询向量返回3个最相似的结果。

- 记录搜索结束时间。

```python
for hits in result:
      for hit in hits:
      print(f"hit: {hit}, random field: {hit.entity.get('random')}")
print(search_latency_fmt.format(end_time - start_time))
```

- 输出搜索结果和每个结果的`random`字段的值。

- 打印搜索所用的时间。

### 基于标量过滤的查询:

```python
print(fmt.format("Start querying with `random > 0.5`"))
start_time = time.time()
result = hello_milvus.query(expr="random > 0.5", output_fields=["random", "embeddings"])
end_time = time.time()
```

- 使用表达式`random > 0.5`进行查询，意味着查询`random`字段值大于0.5的所有实体。

- 打印查询结果和查询所用的时间。

### 分页查询:

```python
r1 = hello_milvus.query(expr="random > 0.5", limit=4, output_fields=["random"])
r2 = hello_milvus.query(expr="random > 0.5", offset=1, limit=3, output_fields=["random"])
```

- 进行两次查询，第一次返回最多4个结果，第二次跳过第一个结果并返回最多3个结果。

### 混合搜索:

```python
print(fmt.format("Start hybrid searching with `random > 0.5`"))
start_time = time.time()
result = hello_milvus.search(vectors_to_search, "embeddings", search_params, limit=3, expr="random > 0.5", output_fields=["random"])
end_time = time.time()
```

- 同时考虑向量相似性和标量过滤条件进行搜索。

- 打印搜索结果和搜索所用的时间。

总结：这段代码展示了如何使用`pymilvus`库进行基于向量相似性的搜索、基于标量过滤的查询、分页查询和混合搜索。<br>

### 获取插入实体的主键:

```python
ids = insert_result.primary_keys
```

- 从之前的插入操作中获取插入实体的主键。这些主键是唯一的，并用于标识插入的实体。

### 构建删除表达式:

```python
expr = f'pk in ["{ids[0]}" , "{ids[1]}"]'
print(fmt.format(f"Start deleting with expr `{expr}`"))
```

- 构建一个表达式，该表达式表示要删除的实体的主键。在这里，我们选择删除插入实体的前两个。

- 打印开始删除的消息。

### 查询并打印删除前的实体:

```python
result = hello_milvus.query(expr=expr, output_fields=["random", "embeddings"])
print(f"query before delete by expr=`{expr}` -> result: \n-{result[0]}\n-{result[1]}\n")
```

- 使用上面构建的表达式查询这两个实体，以确认它们存在于集合中。

- 打印这两个实体的详细信息。

### 删除实体:

```python
hello_milvus.delete(expr)
```

- 调用`delete`方法删除匹配表达式的实体。

### 查询并打印删除后的实体:

```python
result = hello_milvus.query(expr=expr, output_fields=["random", "embeddings"])
print(f"query after delete by expr=`{expr}` -> result: {result}\n")
```

- 使用相同的表达式再次查询这两个实体，以确认它们已从集合中被删除。

- 打印查询结果。由于实体已被删除，因此结果应该是空的。

### 删除集合:

```python
print(fmt.format("Drop collection `hello_milvus`"))
utility.drop_collection("hello_milvus")
```

- 打印开始删除集合的消息。

- 调用`drop_collection`方法删除整个`hello_milvus`集合。

总之，这段代码首先删除了`hello_milvus`集合中的两个实体，然后删除整个`hello_milvus`集合。<br>
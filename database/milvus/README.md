# Milvus

## Milvus安装:

1. 下载 YAML 文件;

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

运行`sudo docker-compose up -d`后，终端会显示以下内容:<br>

<img src="./milvus_materials/milvus安装成功图片.jpg" alt="image" width="50%" height="50%">


3. 现在检查容器是否已经启动并运行:

```bash
sudo docker compose ps
```

终端显示:<br>

<img src="./milvus_materials/milvus容器运行状态.jpg" alt="image" width="50%" height="50%">


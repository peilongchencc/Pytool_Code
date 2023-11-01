# Docker
- [Docker](#docker)
  - [Docker和Docker Compose 安装:](#docker和docker-compose-安装)
  - [安装Docker Compose 1.25.1版本:](#安装docker-compose-1251版本)
    - [docker-compose --version无法使用的解决方案:](#docker-compose---version无法使用的解决方案)
  - [Docker指令:](#docker指令)
    - [查看Docker版本:](#查看docker版本)
    - [查看Docker Compose版本的指令如下:](#查看docker-compose版本的指令如下)
    - [检查 Docker 服务的状态(按q键退出检查状态):](#检查-docker-服务的状态按q键退出检查状态)
    - [启动 Docker 服务:](#启动-docker-服务)
    - [将 Docker 添加到启动项，以确保在系统重新启动时 Docker 会自动启动：](#将-docker-添加到启动项以确保在系统重新启动时-docker-会自动启动)
  - [卸载Docker Compose:](#卸载docker-compose)


## Docker和Docker Compose 安装:

1. 更新包列表:

```bash
sudo apt update
```

2. 安装依赖包，以便可以通过 HTTPS 使用仓库:

```bash
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
```

3. 添加 Docker 官方 GPG 密钥:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

4. 添加 Docker 官方仓库:

```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

5. 更新包列表:

```bash
sudo apt update
```

6. 安装 Docker 和 Docker Compose:

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose
```

以笔者系统(Ubuntu 18.4)为例，运行上述代码后安装的docker版本为`Docker version 24.0.2, build cb74dfc`，安装的docker compose版本为`docker-compose version 1.17.1, build unknown`。<br>


🚨🚨🚨如果你只想要安装 Docker 而不想安装 Docker Compose，你可以从上述命令中移除`docker-compose`。以下是修改后的命令：<br>

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

这条命令将只会为你安装 Docker 而不包括 Docker Compose。<br>

## 安装Docker Compose 1.25.1版本:

在某些情况下，你可能想要安装不同版本的Docker Compose，此时你可以参考以下指令:<br>

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

运行上述指令后，终端输入`docker-compose --version`将显示以下内容:<br>

```bash
docker-compose version 1.25.1, build a82fef07
```

### docker-compose --version无法使用的解决方案:

如果你终端使用`docker-compose --version`显示如下内容:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7cxxx:/usr/local/bin# docker-compose --version
-bash: /usr/bin/docker-compose: No such file or directory
```

且`/usr/local/bin`目录下的内容有`docker-compose`文件:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7cxxx:/usr/local/bin# ll
total 16676
drwxr-xr-x  2 root root     4096 Oct 27 17:41 ./
drwxr-xr-x 12 root root     4096 Aug  9 10:22 ../
-rwxr-xr-x  1 root root      399 May 15 17:06 cloud-id*
-rwxr-xr-x  1 root root      403 May 15 17:06 cloud-init*
-rwxr-xr-x  1 root root     2108 May 15 17:06 cloud-init-per*
-rwxr-xr-x  1 root root 17032648 Oct 27 17:44 docker-compose*
-rwxr-xr-x  1 root root     1003 May 15 17:06 jsondiff*
-rwxr-xr-x  1 root root     3858 May 15 17:06 jsonpatch*
-rwxr-xr-x  1 root root     1837 May 15 17:06 jsonpointer*
-rwxr-xr-x  1 root root      397 May 15 17:06 jsonschema*
-rwxr-xr-x  1 root root      424 May 15 17:06 normalizer*
```

需要首先检查环境变量是否配置:<br>

```bash
echo $PATH
```

如果没有，需要将`/usr/local/bin`添加至`~/.bashrc` 文件的末尾（对于bash用户）或 `~/.zshrc` （如果你使用zsh）。<br>

> `/usr/local/bin`是按照笔者上方提供的指令安装docker compose的路径。

如果环境变量显示已经有`/usr/local/bin`，那么你可以在终端运行以下指令，用来清除bash的内部命令查找缓存。<br>

```bash
hash -r
docker-compose --version
```

现在大概率已经成功了，会出现这个问题是因为，你之前在不同的位置有 `docker-compose` 的版本，并且bash已经缓存了这个命令的位置。<br>

使用 `hash -r` 来清除缓存是一个有用的技巧，特别是在安装、移动或更改可执行文件的路径时。<br>


## Docker指令:

现在Docker 和 Docker Compose已经安装好了，下面介绍一些工作中常用的Docker相关指令。<br>

### 查看Docker版本:

```bash
docker --version
```

终端显示如下信息:<br>

```log
Docker version 24.0.2, build cb74dfc
```

### 查看Docker Compose版本的指令如下:

```bash
docker-compose --version
```

终端显示如下信息:<br>

```log
docker-compose version 1.17.1, build unknown
```

### 检查 Docker 服务的状态(按q键退出检查状态):

```bash
sudo systemctl status docker
```

如果 Docker 服务正在运行，你将看到类似如下的输出:<br>

```log
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2023-10-27 16:19:38 CST; 6min ago
     Docs: https://docs.docker.com
 Main PID: 3089 (dockerd)
    Tasks: 11
   CGroup: /system.slice/docker.service
           └─3089 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

Oct 27 16:19:37 iZ2zea5v77oawjy2qz7cxxx systemd[1]: Starting Docker Application Container Engine...
Oct 27 16:19:37 iZ2zea5v77oawjy2qz7cxxx dockerd[3089]: time="2023-10-27T16:19:37.206729952+08:00" level=info msg="Starting up"
Oct 27 16:19:37 iZ2zea5v77oawjy2qz7cxxx dockerd[3089]: time="2023-10-27T16:19:37.208940722+08:00" level=info msg="detected 127.0.0.5
Oct 27 16:19:37 iZ2zea5v77oawjy2qz7cxxx dockerd[3089]: time="2023-10-27T16:19:37.525467345+08:00" level=info msg="Loading containers
Oct 27 16:19:38 iZ2zea5v77oawjy2qz7cxxx dockerd[3089]: time="2023-10-27T16:19:38.200223894+08:00" level=info msg="Loading containers
Oct 27 16:19:38 iZ2zea5v77oawjy2qz7cxxx dockerd[3089]: time="2023-10-27T16:19:38.282641593+08:00" level=warning msg="WARNING: No swa
Oct 27 16:19:38 iZ2zea5v77oawjy2qz7cxxx dockerd[3089]: time="2023-10-27T16:19:38.283251872+08:00" level=info msg="Docker daemon" com
Oct 27 16:19:38 iZ2zea5v77oawjy2qz7cxxx dockerd[3089]: time="2023-10-27T16:19:38.283552530+08:00" level=info msg="Daemon has complet
Oct 27 16:19:38 iZ2zea5v77oawjy2qz7cxxx dockerd[3089]: time="2023-10-27T16:19:38.385243114+08:00" level=info msg="API listen on /run
Oct 27 16:19:38 iZ2zea5v77oawjy2qz7cxxx systemd[1]: Started Docker Application Container Engine.
lines 1-19/19 (END)
```

### 启动 Docker 服务:

如果你的Docker服务没有启动，可以运行一下指令启动Docker服务:<br>

```bash
sudo systemctl start docker
```

### 将 Docker 添加到启动项，以确保在系统重新启动时 Docker 会自动启动：

```bash
sudo systemctl enable docker
```

终端显示:<br>

```log
Synchronizing state of docker.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable docker
```

## 卸载Docker Compose:

```bash
sudo apt remove docker-compose
```
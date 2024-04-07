# Installation Process of Neo4j

本章介绍Neo4j在Ubuntu 18.04系统上的安装与启动。<br>

- [Installation Process of Neo4j](#installation-process-of-neo4j)
  - [Neo4j的安装：](#neo4j的安装)
    - [ubuntu 18.04安装java11:](#ubuntu-1804安装java11)
      - [更新系统软件包信息：](#更新系统软件包信息)
      - [安装jdk11:](#安装jdk11)
    - [Centos7 安装java11:](#centos7-安装java11)
    - [下载安装包：](#下载安装包)
    - [安装包上传/移动到指定位置：](#安装包上传移动到指定位置)
    - [解压tar.gz文件并重命名：](#解压targz文件并重命名)
    - [修改neo4j.conf 中的配置，开放远程连接限制:](#修改neo4jconf-中的配置开放远程连接限制)
    - [更改默认密码：](#更改默认密码)
    - [修改环境变量:](#修改环境变量)
    - [开启服务器端口：](#开启服务器端口)
    - [启动/关闭 Neo4j 数据库：](#启动关闭-neo4j-数据库)
    - [Neo4j Desktop 连接远程Neo4j数据库：](#neo4j-desktop-连接远程neo4j数据库)
    - [Centos7修改最大文件打开数(可选):](#centos7修改最大文件打开数可选)

## Neo4j的安装：

### ubuntu 18.04安装java11:

#### 更新系统软件包信息：

终端输入以下指令：<br>

```shell
sudo apt update
```

不用担心，这一步只是让系统确认安装的包的信息，并不会更新或改变包的版本。<br>

#### 安装jdk11:

安装 Java 运行时环境（JRE），Neo4j 需要 Java 运行。运行以下命令安装 OpenJDK 11<br>

```shell
sudo apt install openjdk-11-jre
```

如果你使用的不同系统，注意jdk版本是否与自己的系统兼容～🌿🌿🌿<br>

上述指令运行成功后，输入以下指令查看jdk版本信息：<br>

```shell
java -version
```

此时终端应该可以看到以下信息：<br>

```txt
openjdk version "11.0.19"
```

### Centos7 安装java11:

CentOS 7 同样能够安装 Java 11。安装 Java 11 可以通过多种方式完成，包括使用 CentOS 的包管理器 `yum` 安装 OpenJDK 11（开源版本），或者下载并安装 Oracle JDK 11（商业版本）。以下是使用 `yum` 安装 OpenJDK 11 的步骤：<br>

1. **打开终端**：首先，打开你的 CentOS 7 系统上的终端。

2. **更新你的包管理器**：运行以下命令以确保你的 `yum` 包管理器是最新的。

```
sudo yum update
```

3. **安装 OpenJDK 11**：通过 `yum` 安装 OpenJDK 11，使用以下命令：

```
sudo yum install java-11-openjdk
```

4. **验证安装**：安装完成后，你可以通过运行以下命令来验证 Java 版本：

```
java -version
```

这应该会显示安装的 Java 版本信息，确保显示的是 Java 11 的相关信息。例如:<br>

```txt
[root@localhost ~]# java -version
openjdk version "11.0.22" 2024-01-16 LTS
OpenJDK Runtime Environment (Red_Hat-11.0.22.0.7-1.el7_9) (build 11.0.22+7-LTS)
OpenJDK 64-Bit Server VM (Red_Hat-11.0.22.0.7-1.el7_9) (build 11.0.22+7-LTS, mixed mode, sharing)
```

🚨🚨🚨如果你需要 Oracle JDK 11，你可以从 Oracle 官网下载 JDK 11 的安装包，并遵循官方的安装指南进行安装。Oracle JDK 的安装可能涉及解压下载的文件并设置环境变量，例如 `JAVA_HOME` 和更新 `PATH` 变量以指向 JDK 的安装位置。<br>

🤭🤭🤭使用 OpenJDK 11 是 CentOS 7 上安装 Java 11 的一个简单且推荐的方式，因为它可以直接通过 CentOS 的包管理器安装，**无需手动下载或设置环境变量**。这也确保了易于管理和更新。<br>

### 下载安装包：

要安装Neo4j，首先要确定适合自己的版本，Ubuntu 18.4 的用户直接访问下方链接下载 Neo4j 4.1.0 版本即可。<br>

```txt
https://we-yun.com/doc/neo4j/   # 国内镜像源，微云数聚的仓库，内含Neo4j各历史版本
```

### 安装包上传/移动到指定位置：
将 `neo4j-community-4.1.0-unix.tar.gz` 文件上传/移动到你希望安装 Neo4j 的目录，这里推荐移动/上传到 `/opt` 目录下。<br>
🤗🤗🤗特别提醒：Neo4j的安装包不要删除，如果你想在当前服务器运行多个Neo4j以后还会用到～<br>
> 为什么推荐将Neo4j移动到`/opt`目录中？🥹🥹🥹<br>
> 将Neo4j移动到/opt目录是一种良好的做法，主要基于以下几个原因：
> 1. 遵循标准惯例：/opt目录是用于安装可选软件的常见位置之一。根据Linux Filesystem Hierarchy Standard (FHS)规范，/opt目录用于安装可选软件包，这些软件包在系统中占据独立的位置，与系统的其他部分分离开来。
> 2. 系统范围的可访问性：将Neo4j安装在/opt目录下可以使该软件对整个系统的用户可见和访问，而不仅仅是当前用户。这对于在多个用户之间共享Neo4j或让其他用户管理和维护Neo4j数据库非常有用。
> 3. 文件系统层次结构的整洁性：将Neo4j移动到独立的目录中，例如/opt，有助于保持文件系统的整洁性。它可以防止将Neo4j的文件和目录散布到系统中的多个位置，使得管理和维护变得更加清晰和方便。
> 请注意，将Neo4j安装到/opt目录并不是强制要求的，你也可以选择其他合适的位置来进行安装。但是，根据通用的最佳实践和标准规范，将其安装在/opt目录下是一个常见的选择。

### 解压tar.gz文件并重命名：
将 `neo4j-community-4.1.0-unix.tar.gz` 文件移动到 `/opt` 目录下后，使用以下指令将 `tar.gz` 文件解压到当前目录。<br>
```shell
tar -xf neo4j-community-4.1.0-unix.tar.gz
```
将解压后的文件重命名，如果你要在同一台服务器上创建多个Neo4j数据库，重命名是必须的，如果你只需要一个Neo4j，那么不重命名也是可以的：<br>
```shell
mv neo4j-community-4.1.0 neo4j_1
```

### 修改neo4j.conf 中的配置，开放远程连接限制:
默认Neo4j是不启用远程连接的，使用 `netstat -ntlp` 查看到的端口状态为 `127.0.0.1:7687 ` 和 `127.0.0.1:7687 ` 。`127.0.0.1` 只支持 `localhost` 的方式连接，如果你是在自己电脑上部署的Neo4j，只是本地连接Neo4j，可以跳过这一步和"开启服务器端口"的内容。在自己电脑上部署的Neo4j使用 Neo4j Desktop 连接Neo4j时，`Connect URL` 使用如下内容即可：<br>
```txt
neo4j://localhost:7687
```

如果你是在远程服务器上部署的Neo4j，需要修改配置文件 `neo4j.conf` 中的监听地址。<br>
输入以下指令打开 neo4j.conf 文件：<br>
```confg
vim /opt/neo4j_1/conf/neo4j.conf
```
修改 `Bolt connector` 和 `HTTP Connector`:<br>
修改前：<br>
```conf
# Bolt connector
dbms.connector.bolt.enabled=true
#dbms.connector.bolt.tls_level=DISABLED
#dbms.connector.bolt.listen_address=:7687

# HTTP Connector. There can be zero or one HTTP connectors.
dbms.connector.http.enabled=true
#dbms.connector.http.listen_address=:7474
```

修改后：<br>
```conf
# Bolt connector
dbms.connector.bolt.enabled=true
#dbms.connector.bolt.tls_level=DISABLED
dbms.connector.bolt.listen_address=0.0.0.0:7687


# HTTP Connector. There can be zero or one HTTP connectors.
dbms.connector.http.enabled=true
dbms.connector.http.listen_address=0.0.0.0:7474
```

### 更改默认密码：
在Neo4j中，💢💢💢不能直接更改默认用户名（默认为neo4j），但可以更改默认用户的密码。使用如下命令更改密码：<br>

首先确保路径正确：<br>

```shell
cd /opt/neo4j_1/bin
```

路径正确后输入如下指令：<br>

```shell
neo4j-admin set-initial-password new_password
```

将 `new_password` 改为你的密码即可，笔者设置如下：<br>

```shell
neo4j-admin set-initial-password Flameaway3.
```

回车后，会看到终端提示 `Changed password for user 'neo4j'.`。👏👏👏<br>

如果设置新密码出现问题，命令前加上 `sudo` 再试下:<br>

```shell
sudo neo4j-admin set-initial-password Flameaway3.
```

如果提示`-su: neo4j-admin: command not found`，改为以下方式即可：<br>

```shell
./neo4j-admin set-initial-password Flameaway3.
```

### 修改环境变量:
修改环境变量是为了简化neo4j的操作，如果不修改环境变量会导致终端使用类似 `neo4j start` 指令时会提示 "命令无法识别"。<br>
> 如果你想在同一台服务器部署两个 Neo4j 数据库，最好的做法是两者都不设置全局环境变量。🚨🚨🚨

回归正题，如果你想要修改环境变量，运行以下指令打开 `.bashrc` 文件：<br>
```shell
vim ~/.bashrc 
```
在文件末尾添加如下两行代码：<br>
```conf
export NEO4J_HOME=/opt/neo4j_1
export PATH=$NEO4J_HOME/bin:$PATH
```
修改后，英文状态下点击`:`，输入`x`，回车关闭文件，终端运行以下指令使新的环境变量生效。<br>
```shell
source ~/.bashrc
```
关闭当前终端，重新打开一个终端。此时，你就可以在终端直接使用 `neo4j start` 、`neo4j restart` 等指令。<br>
环境变量其实就是在你终端运行指令时，优先匹配 `bashrc` 中的内容。例如：如果你已经配置了环境变量，你在终端运行 `neo4j start` ，其实是在运行 `/opt/neo4j_1/bin/neo4j start`。<br>

### 开启服务器端口：
以阿里云服务器为例，按照下图所示，依次开放 `7474` 和 `7687` 端口即可。🥴🥴🥴<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/af9f8f1c-44a9-4af6-ac24-73dce3609bcd)

### 启动/关闭 Neo4j 数据库：

现在，你可以选择以下任意一种方式，从终端启动 Neo4j 数据库了：<br>

1. 常规方式启动：

```shell
neo4j start
```

2. 以终端输出日志的方式启动：

```bash
neo4j console
```

3. 以后台方式启动：

```bash
nohup sudo neo4j start &
```

🔥🔥🔥以`nohup`形式启动的服务，在当前终端关闭的情况下依旧会在后台运行。`nohup`指令可以和多种指令搭配，例如：`nohup sudo neo4j console &`或`nohup sudo neo4j restart &`~<br>

你也可以输入以下指令查看端口情况：<br>

```shell
netstat -tuln
```

如果你想要关闭 Neo4j 数据库，使用以下指令：<br>

```shell
neo4j stop
```

### Neo4j Desktop 连接远程Neo4j数据库：
此时你应该能看到7474和7687端口的监听地址为：`:::7474`、`:::7687`，现在你就可以本地通过 Neo4j Desktop 连接到远程服务器部署的Neo4j了。输入用户名和密码后，`Connect URL` 输入类似下列内容即可：<br>
```txt
neo4j://8.140.203.xxx:7687
```
效果如下：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/3d49c7db-311e-488f-aff7-fb93ebd164c2" alt="image" width="70%" height="70%">
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/868ca524-7232-4f1b-abb3-2e3180904dc8" alt="image" width="70%" height="70%">

设置好数据库信息后，点击 `connect` 然后点击 `open` 即可进入 neo4j_1:<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/8d836036-a472-4876-a0bb-a783547bf781" alt="image" width="70%" height="70%">

你也可以本地通过 `telnet` 查看连接状态：<br>
> 不能使用 `ping` 测试的，`ping` 无法指定端口。

```shell
telnet 8.140.203.xxx 7474
```
```shell
telnet 8.140.203.xxx 7687
```
如果出现以下内容，表示成功连接:<br>
```txt
Trying 8.140.203.xxx...
Connected to 8.140.203.xxx
Escape charcter is '^]'.
```
也可以通过域名测试连接状态，例如：<br>
```shell
telnet my_server.com 7474
```
<br>

### Centos7修改最大文件打开数(可选):

你在启动Neo4j时，可能遇到类似以下信息:<br>

```txt
WARNING: Max 1024 open files allowed, minimum of 40000 recommended. See the Neo4j manual.
```

这表明你的系统最大文件打开数太小，需要设置的大一些。<br>

你可以通过以下指令 **查看最大文件打开数** (假设你的系统为Centos7):<br>

```bash
ulimit -Hn # 查看硬限制
ulimit -Sn # 查看软限制
```

修改方式也很简单，按照以下步骤操作即可:<br>

1. 修改/etc/security/limits.conf文件，追加如下内容：

```bash
* soft nofile 65535 
* hard nofile 65535
```

> 65535 是 2^16 - 1，这是一个基于 16 位计算机体系结构的最大数值。

2. 修改/etc/profile，追加如下内容：

```bash
ulimit -n 65535
```

3. 重启主机，然后使用 `ulimit -n` 检查。

重启系统/服务器(Centos7版本):<br>

```bash
sudo systemctl reboot
```
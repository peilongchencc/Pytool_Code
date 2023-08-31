# Neo4j
Neo4j是一种图形数据库管理系统，用于存储和管理图形数据。它是一个基于Java的开源软件，支持高度可扩展的图形数据模型，可以用于各种应用领域，如社交网络分析、推荐系统、网络安全分析等。Neo4j使用Cypher查询语言来操作和查询图形数据，并提供了丰富的API和工具来帮助开发人员与数据库进行交互。由于其图形数据模型的优势，Neo4j可以有效地表示和处理复杂的关系数据，提供了快速且灵活的数据访问和分析能力。<br>

虽然Neo4j是基于Java的软件，但不妨碍我们python用户使用🤣🤣🤣。接下来，笔者就讲一下 Ubuntu 18.4 安装Neo4j 4.1.0和Neo4j的使用经验。<br>
- [Neo4j](#neo4j)
  - [Neo4j的安装：](#neo4j的安装)
    - [下载安装包：](#下载安装包)
    - [安装包上传/移动到指定位置：](#安装包上传移动到指定位置)
    - [解压tar.gz文件：](#解压targz文件)
    - [修改neo4j.conf 中的配置，开放远程连接限制:](#修改neo4jconf-中的配置开放远程连接限制)
    - [更改默认密码：](#更改默认密码)
    - [修改环境变量:](#修改环境变量)
    - [开启服务器端口：](#开启服务器端口)
    - [启动/关闭 Neo4j 数据库：](#启动关闭-neo4j-数据库)
    - [Neo4j Desktop 连接远程Neo4j数据库：](#neo4j-desktop-连接远程neo4j数据库)
  - [Neo4j常用语句：](#neo4j常用语句)

## Neo4j的安装：
### 下载安装包：
要安装Neo4j，首先要确定适合自己的版本，Ubuntu 18.4 的用户直接访问下方链接下载 Neo4j 4.1.0 版本即可。<br>
```txt
https://we-yun.com/doc/neo4j/   # 国内镜像源，微云数聚的仓库，内含Neo4j各历史版本
```

### 安装包上传/移动到指定位置：
将 `neo4j-community-4.1.0-unix.tar.gz` 文件上传/移动到你希望安装 Neo4j 的目录，这里推荐移动/上传到 `/opt` 目录下。<br>
> 为什么推荐将Neo4j移动到`/opt`目录中？🥹🥹🥹<br>
> 将Neo4j移动到/opt目录是一种良好的做法，主要基于以下几个原因：
> 1. 遵循标准惯例：/opt目录是用于安装可选软件的常见位置之一。根据Linux Filesystem Hierarchy Standard (FHS)规范，/opt目录用于安装可选软件包，这些软件包在系统中占据独立的位置，与系统的其他部分分离开来。
> 2. 系统范围的可访问性：将Neo4j安装在/opt目录下可以使该软件对整个系统的用户可见和访问，而不仅仅是当前用户。这对于在多个用户之间共享Neo4j或让其他用户管理和维护Neo4j数据库非常有用。
> 3. 文件系统层次结构的整洁性：将Neo4j移动到独立的目录中，例如/opt，有助于保持文件系统的整洁性。它可以防止将Neo4j的文件和目录散布到系统中的多个位置，使得管理和维护变得更加清晰和方便。
> 请注意，将Neo4j安装到/opt目录并不是强制要求的，你也可以选择其他合适的位置来进行安装。但是，根据通用的最佳实践和标准规范，将其安装在/opt目录下是一个常见的选择。

### 解压tar.gz文件：
将 `neo4j-community-4.1.0-unix.tar.gz` 文件移动到 `/opt` 目录下后，使用以下指令将 `tar.gz` 文件解压到当前目录。<br>
```shell
tar -xf neo4j-community-4.1.0-unix.tar.gz
```

### 修改neo4j.conf 中的配置，开放远程连接限制:
默认Neo4j是不启用远程连接的，使用 `netstat -ntlp` 查看到的端口状态为 `127.0.0.1:7687 ` 和 `127.0.0.1:7687 ` 。`127.0.0.1` 只支持 `localhost` 的方式连接，如果你是在自己电脑上部署的Neo4j，只是本地连接Neo4j，可以跳过这一步和"开启服务器端口"的内容。在自己电脑上部署的Neo4j使用 Neo4j Desktop 连接Neo4j时，`Connect URL` 使用如下内容即可：<br>
```txt
neo4j://localhost:7687
```

如果你是在远程服务器上部署的Neo4j，需要修改配置文件 `neo4j.conf` 中的监听地址。<br>
输入以下指令打开 neo4j.conf 文件：<br>
```confg
vim /opt/neo4j-community-4.1.0/conf/neo4j.conf
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
cd /opt/neo4j-community-4.1.0/bin
```
路径正确后输入如下指令：<br>
```shell
sudo neo4j-admin set-initial-password new_password
```
将 `new_password` 改为你的密码即可，笔者设置如下：<br>
```shell
sudo neo4j-admin set-initial-password Flameaway3.
```
回车后，会看到终端提示 `Changed password for user 'neo4j'.`。👏👏👏<br>

### 修改环境变量:
不修改环境变量会导致终端使用类似 `neo4j start` 指令时会提示 "命令无法识别"。<br>
运行以下指令打开 `.bashrc` 文件：<br>
```shell
vim ~/.bashrc 
```
在文件末尾添加如下两行代码：<br>
```conf
export NEO4J_HOME=/opt/neo4j-community-4.1.0
export PATH=$NEO4J_HOME/bin:$PATH
```
修改后，英文状态下点击`:`，输入`x`，回车关闭文件，终端运行以下指令使新的环境变量生效。<br>
```shell
source ~/.bashrc
```

### 开启服务器端口：
以阿里云服务器为例，按照下图所示，依次开放 `7474` 和 `7687` 端口即可。🥴🥴🥴<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/af9f8f1c-44a9-4af6-ac24-73dce3609bcd)

### 启动/关闭 Neo4j 数据库：
此时你就可以终端输入以下指令启动 Neo4j 数据库了：<br>
```shell
neo4j start
```
你也可以输入以下指令查看端口情况：<br>
```shell
netstat -tuln
```
<br>
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
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/76e88574-2a60-40e2-9006-7cfeb27a1665)

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
也可以通过域名连接，例如：<br>
```shell
telnet my_server.com 7474
```

## Neo4j常用语句：

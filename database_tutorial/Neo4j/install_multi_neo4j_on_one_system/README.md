# install_multi_neo4j_on_one_system

本章介绍在同一台ubuntu 18.04服务器上安装多个Neo4j数据库的方法。注意⚠️:本章部分内容承接`installation_process_of_neo4j`的内容，请结合阅读。<br>
- [install\_multi\_neo4j\_on\_one\_system](#install_multi_neo4j_on_one_system)
  - [Neo4j创建多个数据库：(如果你只需要一个Neo4j数据库，可以跳过此节内容。)](#neo4j创建多个数据库如果你只需要一个neo4j数据库可以跳过此节内容)
    - [cd到Neo4j安装包所在位置：](#cd到neo4j安装包所在位置)
    - [解压tar.gz文件并重命名：](#解压targz文件并重命名)
    - [修改neo4j.conf 中的配置，开放远程连接限制:](#修改neo4jconf-中的配置开放远程连接限制)
    - [更改默认密码：](#更改默认密码)
    - [修改环境变量:](#修改环境变量)
    - [开启服务器端口：](#开启服务器端口)
    - [启动/关闭 neo4j\_2 数据库：](#启动关闭-neo4j_2-数据库)
    - [Neo4j Desktop 连接远程neo4j\_2数据库：](#neo4j-desktop-连接远程neo4j_2数据库)

## Neo4j创建多个数据库：(如果你只需要一个Neo4j数据库，可以跳过此节内容。)

工作中我们可能需要用到多份 Neo4j 数据库的情况，例如"医疗知识图谱"、"金融知识图谱"。那么如何在一台服务器上创建和启动2个或多个Neo4j呢？接下来，笔者将介绍具体的操作。<br>

### cd到Neo4j安装包所在位置：

移动到我们安装 `neo4j_1` 的位置：<br>

```shell
cd /opt
```

依旧是刚刚的服务器，因为我们前面已经安装过jdk，所以这里不需要再安装。<br>

### 解压tar.gz文件并重命名：

终端依次运行下列2个指令：<br>

```shell
tar -xf neo4j-community-4.1.0-unix.tar.gz
```

```shell
mv neo4j-community-4.1.0 neo4j_2
```

### 修改neo4j.conf 中的配置，开放远程连接限制:

输入以下指令打开 neo4j.conf 文件：<br>

```confg
vim /opt/neo4j_2/conf/neo4j.conf
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
dbms.connector.bolt.listen_address=0.0.0.0:7688


# HTTP Connector. There can be zero or one HTTP connectors.
dbms.connector.http.enabled=true
dbms.connector.http.listen_address=0.0.0.0:7475
```

端口可以修改为任意值，只要端口不冲突就可以。<br>

### 更改默认密码：
首先确保路径正确：<br>
```shell
cd /opt/neo4j_2/bin
```
路径正确后输入如下指令：<br>
```shell
neo4j-admin set-initial-password new_password
```
将 `new_password` 改为你的密码即可，笔者设置如下：<br>
```shell
neo4j-admin set-initial-password Giveaway3.
```
回车后，会看到终端提示 `Changed password for user 'neo4j'.`。👏👏👏<br>

如果设置新密码出现问题，命令前加上 `sudo` 再试下:<br>
```shell
sudo neo4j-admin set-initial-password Giveaway3.
```

### 修改环境变量:
这一节的内容针对的是已经设置过Neo4j环境变量的朋友，当要在同一台服务器上运行2个或多个Neo4j时，最好的做法是都不设置环境变量。如果你已经设置了Neo4j环境，按照下方操作注释掉环境变量即可。<br>

运行以下指令打开 `.bashrc` 文件：<br>
```shell
vim ~/.bashrc 
```
找到如下两行代码：<br>
```shell
export NEO4J_HOME=/opt/neo4j_1
export PATH=$NEO4J_HOME/bin:$PATH
```
将这两行代码注释：<br>
```shell
#export NEO4J_HOME=/opt/neo4j_1
#export PATH=$NEO4J_HOME/bin:$PATH
```
保存并退出 `.bashrc` 文件，运行下列文件激活更改：<br>
```shell
source ~/.bashrc
```
关闭当前终端，重新打开一个终端。<br>

### 开启服务器端口：
以阿里云服务器为例，按照下图所示，依次开放你为 `neo4j_2` 配置的端口即可，笔者为 `neo4j_2` 配置的端口为 `7475` 和 `7688` 。🥴🥴🥴<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/b935996e-0ee6-482d-b7ef-9041eaca1df9)


### 启动/关闭 neo4j_2 数据库：
因为我们注释了环境变量，所以我们需要采用完整路径或进入文件中启动 neo4j：<br>
进入文件中：<br>
```shell
cd /opt/neo4j_2/bin
```
```shell
./neo4j start
```
使用完整路径：<br>
```shell
/opt/neo4j_2/bin/neo4j start
```
现在查看端口情况，观察neo4j_2是否开启：<br>
```shell
netstat -tuln
```
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/6ce187f7-ad14-4b2a-859f-6a1117160597" alt="image" width="70%" height="70%">

从图中我们可以看到，`neo4j_1` 和 `neo4j_2` 数据库都启动了～🌿🌿🌿<br>

如果想要关闭 neo4j_2 数据库，在 `/opt/neo4j_2/bin` 路径下使用以下指令即可：<br>
```shell
./neo4j stop
```

### Neo4j Desktop 连接远程neo4j_2数据库：

做法与本地连接neo4j_1操作相同：<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/9c401e72-f2e7-4deb-a453-87644be3f256" alt="image" width="70%" height="70%">

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/bb235d5e-40e1-4082-b115-ecc0ea4e7ea5" alt="image" width="60%" height="60%">

设置好数据库信息后，点击 `connect` 然后点击 `open` 即可进入 neo4j_2:<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/39e1ceb7-198b-4d9e-81df-3a23a2e714d0" alt="image" width="70%" height="70%">

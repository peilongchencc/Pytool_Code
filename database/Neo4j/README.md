# Neo4j
Neo4j是一种图形数据库管理系统，用于存储和管理图形数据。它是一个基于Java的开源软件，支持高度可扩展的图形数据模型，可以用于各种应用领域，如社交网络分析、推荐系统、网络安全分析等。Neo4j使用Cypher查询语言来操作和查询图形数据，并提供了丰富的API和工具来帮助开发人员与数据库进行交互。由于其图形数据模型的优势，Neo4j可以有效地表示和处理复杂的关系数据，提供了快速且灵活的数据访问和分析能力。<br>

虽然Neo4j是基于Java的软件，但不妨碍我们python用户使用🤣🤣🤣。接下来，笔者就讲一下 Ubuntu 18.4 安装Neo4j 4.1.0和Neo4j的使用经验。<br>
- [Neo4j](#neo4j)
  - [Neo4j的安装：](#neo4j的安装)
    - [更新系统软件包信息：](#更新系统软件包信息)
    - [安装jdk11:](#安装jdk11)
    - [下载安装包：](#下载安装包)
    - [安装包上传/移动到指定位置：](#安装包上传移动到指定位置)
    - [解压tar.gz文件并重命名：](#解压targz文件并重命名)
    - [修改neo4j.conf 中的配置，开放远程连接限制:](#修改neo4jconf-中的配置开放远程连接限制)
    - [更改默认密码：](#更改默认密码)
    - [修改环境变量:](#修改环境变量)
    - [开启服务器端口：](#开启服务器端口)
    - [启动/关闭 Neo4j 数据库：](#启动关闭-neo4j-数据库)
    - [Neo4j Desktop 连接远程Neo4j数据库：](#neo4j-desktop-连接远程neo4j数据库)
  - [Neo4j创建多个数据库：(如果你只需要一个Neo4j数据库，可以跳过此节内容。)](#neo4j创建多个数据库如果你只需要一个neo4j数据库可以跳过此节内容)
    - [cd到Neo4j安装包所在位置：](#cd到neo4j安装包所在位置)
    - [解压tar.gz文件并重命名：](#解压targz文件并重命名-1)
    - [修改neo4j.conf 中的配置，开放远程连接限制:](#修改neo4jconf-中的配置开放远程连接限制-1)
    - [更改默认密码：](#更改默认密码-1)
    - [修改环境变量:](#修改环境变量-1)
    - [开启服务器端口：](#开启服务器端口-1)
    - [启动/关闭 neo4j\_2 数据库：](#启动关闭-neo4j_2-数据库)
    - [Neo4j Desktop 连接远程neo4j\_2数据库：](#neo4j-desktop-连接远程neo4j_2数据库)
  - [终端Neo4j常用指令：](#终端neo4j常用指令)
  - [Neo4j Desktop 中常用Cypher语句：](#neo4j-desktop-中常用cypher语句)
    - [CREATE创建有向关系示例：](#create创建有向关系示例)
    - [查询创建的节点和关系：](#查询创建的节点和关系)
    - [常用查询语句：](#常用查询语句)
    - [精确查找和模糊查找：](#精确查找和模糊查找)
    - [CREATE创建中文三元组：](#create创建中文三元组)
    - [MERGE创建三元组：](#merge创建三元组)
    - [CREATE的必要性：](#create的必要性)
    - [为2个节点创建多个关系：](#为2个节点创建多个关系)
    - [更新Neo4j中实体间的关系：](#更新neo4j中实体间的关系)
    - [更新Neo4j中实体的属性的值：](#更新neo4j中实体的属性的值)
    - [为实体添加新的属性：](#为实体添加新的属性)
    - [更新Neo4j中实体的属性的名称：](#更新neo4j中实体的属性的名称)
    - [更新Neo4j中实体的类型：](#更新neo4j中实体的类型)
    - [为节点和关系添加多个属性：](#为节点和关系添加多个属性)
    - [删除指定关系：](#删除指定关系)
    - [删除Neo4j中所有节点和关系：](#删除neo4j中所有节点和关系)
  - [python与Neo4j：](#python与neo4j)
    - [测试python与Neo4j的连接状态：](#测试python与neo4j的连接状态)
    - [创建三元组：](#创建三元组)
    - [获取三元组的值：](#获取三元组的值)
  - [卸载Neo4j：](#卸载neo4j)
  - [为不同用户设置不同JDK：](#为不同用户设置不同jdk)
  - [卸载JDK：](#卸载jdk)

## Neo4j的安装：
### 更新系统软件包信息：
终端输入以下指令：<br>
```shell
sudo apt update
```
不用担心，这一步只是让系统确认安装的包的信息，并不会更新或改变包的版本。<br>

### 安装jdk11:
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

## 终端Neo4j常用指令：

启动Neo4j数据库作为后台服务:<br>

```bash
neo4j start
```

以后台方式启动：<br>

```bash
nohup sudo neo4j start &
```

停止Neo4j数据库服务:<br>

```bash
neo4j stop
```

重新启动Neo4j数据库服务:<br>

```bash
neo4j restart
```

检查Neo4j数据库服务的状态:<br>

```bash
neo4j status
```

显示Neo4j的版本信息:<br>

```bash
neo4j version
```

以控制台模式查看 Neo4j 数据库基本信息:<br>

```bash
neo4j console 
```

## Neo4j Desktop 中常用Cypher语句：
在Neo4j中，关系是有向的‼️‼️‼️。这意味着当你创建一个关系时，你必须指定它的方向🥶🥶🥶。然而，当查询这些关系时，你可以选择忽略方向🥴🥴🥴。<br>

### CREATE创建有向关系示例：
假设你想创建一个描述 `汤姆抓杰瑞` 的三元组信息，你可以使用以下指令：<br>
```sql
// Neo4j支持以 "//" 作为注释
CREATE (m:Leading_role {name: 'Tom'})-[r:catch]->(n:supporting_role {name: 'Jerry'})
RETURN m,r,n
```
> 注意变量名不能以空格为间隔，`Leading role` 会报错，需要使用 `Leading_role` 或 `LeadingRole` 形式。

这里详细解释下上述语句：<br>
`CREATE`: 这是一个Cypher命令，用于创建节点或关系。<br>
`(m:Leading_role {name: 'Tom'})`: <br>
- 此处创建了一个名为`Tom`的`Leading_role`类型节点。<br>
- `(m)`表示节点的变量名或引用🔥🔥🔥，这样在后面的查询中你可以使用这个变量名引用该节点。<br>
- `:Leading_role` 表示节点的标签，标签通常用来表示**节点的类型或类别**。🌿🌿🌿<br>
- `{name: 'Tom'}` 是节点的属性，这里定义了一个名为`name`的属性，其值为`Tom`。<br>

`-[r:catch]->`: <br>
- 此处创建了一个从`Tom`节点到`Jerry`节点的关系。<br>
- `-[]->` 是一个关系的模式，其中`-`表示开始节点，`->`表示关系的方向，指向结束节点。<br>
- `[r:catch]` 中，`r`是关系的变量名🔥🔥🔥，`:catch`是关系的类型。<br>

`(n:supporting_role {name: 'Jerry'})`: <br>
- 此处创建了一个名为`Jerry`的`supporting_role`类型节点。<br>
- `(n)`表示节点的变量名。<br>
- `:supporting_role` 是节点的标签。<br>
- `{name: 'Jerry'}` 是节点的属性。<br>

`RETURN m,r,n`:<br>
- 在执行完上述创建操作后，返回创建的节点`m`和`n`以及关系`r`作为结果。<br>

所以，这条Cypher语句的大致意思是：“创建一个名为`Tom`的`Leading_role`类型节点，一个名为`Jerry`的`supporting_role`类型节点，并在它们之间创建一个类型为`catch`的关系，之后返回创建的实体与关系。”<br>
<br>
Neo4j中效果如下：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/e78e22cd-fe02-4115-a0ba-df5529bbf9a2" alt="image" width="30%" height="30%">

🚀🚀🚀节点颜色、节点大小、关系颜色、对外显示的属性都可以通过点击对应图标设置：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/45fb1c3d-8e82-4cb8-8c2f-80f267787e7f" alt="image" width="50%" height="50%">
<br>

### 查询创建的节点和关系：
虽然物理存储的关系是有向的，但你可以通过查询时的方式来看待它们为无向关系。查询时可以选择忽略关系方向，视为无向关系：<br>
```sql
MATCH (m:Leading_role {name: 'Tom'})-[r:catch]-(n:supporting_role {name: 'Jerry'})
RETURN m,r,n
```
当然，你也可以把方向带上：<br>
```sql
MATCH (m:Leading_role {name: 'Tom'})-[r:catch]->(n:supporting_role {name: 'Jerry'})
RETURN m,r,n
```
总之，虽然在创建时必须指定关系的方向，但在查询时你可以选择视其为无向关系。<br>

### 常用查询语句：
从Neo4j数据库中匹配所有的节点`n`、关系`r`和节点`m`的组合，并返回这些结果，但限制返回的记录数为25。<br>
> 默认情况下，当你不指定排序或其他筛选条件时，Neo4j可能会基于内部存储和处理的顺序返回结果🌿🌿🌿，这可能会看起来像是随机的，尤其是在大型数据集中。
```sql
MATCH (n)-[r]->(m) RETURN n, r, m LIMIT 25
```

如果你想要查看Neo4j中所有节点和关系，可以使用：<br>
```sql
MATCH (n)-[r]->(m) RETURN n, r, m
```

如果你只想要查看所有节点，可以使用：<br>
```sql
MATCH (n) RETURN n
```

如果你只是想要查看所有关系，可以使用：<br>
```sql
MATCH ()-[r]->() RETURN r
```

如果你想要查看含有 `catch` 关系的所有节点，可以使用：
```sql
MATCH (m)-[r:catch]->(n)
RETURN m,n,r
```


如果你想按节点`n`的`name`属性排序，你可以这样写：<br>
```sql
MATCH (n)-[r]->(m)
RETURN n, r, m
ORDER BY n.name
LIMIT 25
```

### 精确查找和模糊查找：
讲精确查找和模糊查找前，首先要明确一个关键点：Neo4j 中查找时遵循的是匹配节点标签(类型)和属性，要查找到你想要寻找的节点，知道其一才能快速匹配。如果这2者你都不知道，那就需要进行模糊匹配查找了。<br>
然而，这种查询可能会在大型数据库中变得很慢，因为它需要遍历所有节点和属性。这只是一种尝试，如果可能的话，还是建议在设计数据库时为节点名称使用明确的属性或给所有节点配一个统一的属性，例如 `name`，以便更有效地进行查询。🚨🚨🚨<br>

举个例子，假设其他人根据下列语句创建了一个三元组信息。<br>
```sql
// 创建节点信息
CREATE (m:Charactor {name:'Tom'})-[r:catch]->(n:Charactor {name:'Jerry'}) RETURN m,n,r
```

现在你只知道节点的`name`属性为 `Tom`，你想知道这个节点的更多信息，可以根据需要执行以下代码：<br>

返回匹配到的节点的所有信息：<br>
```sql
MATCH (n) WHERE n.name = 'Tom' RETURN n;
```
返回匹配到的节点的标签(类型)信息：<br>
```sql
MATCH (n) WHERE n.name = 'Tom' RETURN labels(n);
```
<br>

假设你同时知道节点的`name`属性为 `Tom`，关系为 `catch`，你想知道这个节点的更多信息，可以根据需要执行以下代码：<br>
```sql
MATCH (n {name: 'Tom'})-[r:catch]->()
RETURN n, r
```
如果你想获取特定属性的值，比如假设节点`Tom`还有一个`age`属性，你可以这样查询：<br>
```sql
MATCH (n {name: 'Tom'})-[r:catch]->()
RETURN n.name, n.age, r
```

如果你想获取节点的所有属性，可以使用以下查询：<br>
```sql
MATCH (n {name: 'Tom'})-[r:catch]->()
RETURN n, r, keys(n) as node_properties
```

### CREATE创建中文三元组：
Neo4j中的关系类型、节点标签以及属性的键和值都支持中文字符。你可以使用中文字符来定义关系类型或属性名称:<br>
```sql
CREATE (m:Person {name: '张三'})-[r:知道]->(n:Person {name: '李四'})
RETURN m,r,n
```
Neo4j中效果如下：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/ec50592e-1b2a-4e6c-ba9b-a596ab00dce2" alt="image" width="30%" height="30%">

### MERGE创建三元组：
`CREATE` 和 `MERGE` 都是用于在Neo4j中创建数据的命令，`CREATE` 更关注于直接创建，`MERGE` 更关注于检查Neo4j中是否有重复数据。<br>
举例来说，当你依次运行下面两个语句时，会在Neo4j中创建2个名为 `张三` 的节点，而不是关联了2组关系。<br>
```sql
// 语句1
CREATE (m:Person {name: '张三'})-[r:知道]->(n:Person {name: '李四'})
RETURN m,r,n
```
```sql
// 语句2
CREATE (m:Person {name: '张三'})-[r:知道]->(n:Person {name: '王五'})
RETURN m,r,n
```
Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/db837467-b0cd-4d20-8511-863641efa6a1" alt="image" width="30%" height="30%">


如果你想将2组关系关联起来，需要使用关键字 `MERGE` ：<br>
```sql
// 首先检查张三的节点是否存在，如果不存在，会创建一个名为张三的节点
MERGE (m:Person {name: '张三'})

// 然后检查张三与李四之间的知道关系是否存在，如果不存在，会创建张三与李四之间的知道关系
MERGE (m)-[r1:知道]->(n1:Person {name: '李四'})

// 最后检查张三与王五之间的知道关系是否存在，如果不存在，会创建张三与王五之间的知道关系
MERGE (m)-[r2:知道]->(n2:Person {name: '王五'})

RETURN m, r1, n1, r2, n2
```
Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/742ff813-972f-4e18-b277-460ae5a4be56" alt="image" width="30%" height="30%">

‼️‼️‼️注意：`MERGE` 的使用一定要正确，必须按照上述语句中的逻辑。举个例子，假设你依次运行了下面2个语句，猜猜会发生什么~🥴🥴🥴<br>
```sql
// 语句1
MERGE (m:Person {name: '张三'})-[r:知道]->(n:Person {name: '李四'})
RETURN m,r,n
```
```sql
// 语句2
MERGE (m:Person {name: '张三'})-[r:知道]->(n:Person {name: '王五'})
RETURN m,r,n
```
Bingo! 答案是和使用 `CREATE` 效果相同，会在Neo4j中创建2个张三节点，而不是关联了2组关系。🥹🥹🥹<br>
Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/db837467-b0cd-4d20-8511-863641efa6a1" alt="image" width="30%" height="30%">


### CREATE的必要性：
讲了 `MERGE` 后，可能有人会想: 既然 `MERGE` 这么好用，为什么还要有 `CREATE` 呢❓❓❓ 这里就需要讲一下使用 `CREATE` 的一些必要性和场景了：<br>

**明确性**：当你知道要创建的节点或关系绝对不在数据库中时，使用 `CREATE` 可以明确地表示这一点。这在语义上为读代码的人提供了清晰性。<br>
**性能**：在某些情况下，`CREATE` 可能比 `MERGE` 更快，因为它不需要先检查节点或关系是否已存在。<br>
**数据导入**：当从没有重复数据的来源导入数据时，使用 `CREATE` 是有意义的。<br>
**临时或测试数据**：当需要插入临时或测试数据并且不担心数据重复时，`CREATE` 是一个好选择。<br>
**特定的模型设计**：在某些图形模型设计中，可能需要允许具有相同属性的多个节点存在。在这种情况下，`CREATE` 可以确保总是创建一个新节点，而不是复用现有节点。<br>

总的来说，尽管 `MERGE` 提供了确保数据唯一性的功能，但 `CREATE` 仍然在很多场景下是有必要的。选择使用哪一个取决于你的具体需求和上下文。<br>

### 为2个节点创建多个关系：
工作中，你可能会遇到需要为2个节点创建多个关系的情况，例如张三和李四既是同事，张三又是李四的姐夫，张三还是李四的领导。下面介绍一下这种创建方式：<br>
```sql
// 首先确保张三和李四的节点存在
MERGE (zhangsan:Person {name: '张三'})
MERGE (lisi:Person {name: '李四'})

// 创建“同事”关系
MERGE (zhangsan)-[:同事]->(lisi)

// 创建“姐夫”关系
MERGE (zhangsan)-[:姐夫]->(lisi)

// 创建“领导”关系
MERGE (zhangsan)-[:领导]->(lisi)

RETURN zhangsan, lisi
```
Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/26e4c2f1-f5eb-4ec5-b66c-d3a55cf70ffe" alt="image" width="30%" height="30%">

你可能注意到了，我这里使用的变量名为 `zhangsan`、`lisi`，不是前面经常使用的 `m,n,r`，这是因为在Cypher中，变量名的选择完全取决于开发者的个人习惯和上下文。🤣🤣🤣<br>

为了避免遗忘，这里我们再回顾一下查询，假设你要查询含有 `领导` 关系的所有节点，你只需要输入以下语句即可：<br>
```sql
MATCH (m)-[r:领导]->(n)
RETURN m,n,r
```

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/cc3083d9-4c93-4924-8695-4b440c7bce6b" alt="image" width="40%" height="40%">

别被 `Graph` 吓到了，从 `Text` 选项我们可以看到，返回的内容是正确的～🌿🌿🌿🤭🤭🤭<br>

### 更新Neo4j中实体间的关系：
假如现在张三和李四的姐姐离婚了，你要将张三和李四的 `姐夫` 关系改为 `前姐夫`，运行下列语句即可：<br>
```sql
MATCH (zhangsan:Person {name: '张三'})-[rel:姐夫]->(lisi:Person {name: '李四'})
DELETE rel
CREATE (zhangsan)-[:前姐夫]->(lisi)
```
‼️‼️注意，Neo4j不支持直接重命名关系类型，所以这里的方法是删除旧的关系并创建一个新的关系。<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/4e9f6183-a2bc-4f2d-9e37-a238c021cbba" alt="image" width="30%" height="30%">
<br>

### 更新Neo4j中实体的属性的值：
假设现在李四觉得自己的名字不好听，改名了，改成了 `李斯`，你可以运行下列语句更新数据：<br>
```sql
MATCH (lisi:Person {name: '李四'})
SET lisi.name = '李斯'
RETURN lisi
```
‼️‼️注意，更改属性时需要点击实体或知道创建语句，知道 `实体名称` 对应的属性名称。例如 `李四` 是实体类型为 `Person` 的 `name` 属性。<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/d3e7d7d7-87ee-401f-a463-59922d60c8e7" alt="image" width="30%" height="30%">
<br>

### 为实体添加新的属性：
为实体添加新的属性使用的依旧是 `SET` 关键字，例如：为 `李四` 添加一个新的属性 `age`：<br>
```sql
MATCH (lisi:Person {name: '李四'})
SET lisi.age = 26
RETURN lisi
```
注意要确定你 `MATCH` 的节点信息是正确的，`Person`、`name` 和 `李四` 的信息是对应的。如果你 `MATCH` 的信息是错误的，是无法修改信息的，或者错误的修改为了其他节点的信息。🚀🚀🚀<br>

### 更新Neo4j中实体的属性的名称：
假设你现在觉得 `name` 属性无法完全体现 `李斯` 的意义，想要将 `name` 属性的名称改为 `true_name` 可以使用以下语句：<br>
```sql
MATCH (lisi:Person {name: '李斯'})
SET lisi.true_name = lisi.name
// 删除原属性需要视情况而定
REMOVE lisi.name
RETURN lisi
```
Cypher语句解释：<br>
使用`MATCH`语句查找到名为`李斯`的节点。<br>
使用`SET`设置`true_name`属性的值为`name`属性的值。<br>
使用`REMOVE`删除原先的`name`属性。<br>
最后返回更新后的`lisi`节点。<br>

Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/4e86442b-8390-4eb0-bfac-8590d7f3784f" alt="image" width="50%" height="50%">

咦？好像和我们设想的有些出入，为什么只有一个实体显示了内容，另一个实体什么也不显示❓❓❓<br>
🚀🚀🚀这是因为一个实体只能有一个对外显示的属性，而 `张三` 并没有 `true_name` 属性，`张三` 是 `name` 属性，所以对外显示的内容为空。<br>

这种做法看似不合理，但在某些时候实体有某些独有的属性时，这种设置就比较合理了，具体的使用场景需要你在工作中慢慢体会～<br>

Ps:这里再介绍下将所有 `Person` 类型的 `name` 属性改名为 `true_name` 的语句：<br>
```sql
MATCH (p:Person)
// 使用 `SET` 设置每个节点的 `true_name` 属性为当前的 `name` 属性值。
SET p.true_name = p.name
REMOVE p.name
RETURN p
```
Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/63c4f4c3-917e-44d1-b1e0-a001cb423525" alt="image" width="50%" height="50%">

可以看到，`Person` 类型现在已经没有 `name` 属性了，只有 `true_name` 属性了，且 `张三` 和 `李斯` 两个 `true_name` 都正常显示了。<br>

### 更新Neo4j中实体的类型：
假如 `李斯` 翻身了，从一个普通人变成了 `Actor`，你此时需要将他的标签类型更改，可以使用下列语句：<br>
```sql
MATCH (m:Person{true_name:'李斯'}) remove m:Person  set m:Actor
RETURN m
```
Cypher语句解释：<br>
`MATCH (m:Person{true_name:'李斯'})`: <br>
- 这是一个匹配指令，它在数据库中查找一个标签为`Person`且`true_name`属性为 `'李斯'` 的节点，并将其赋给变量`m`。<br>
`remove m:Person`:<br>
- 这是一个删除操作，它从与变量`m`匹配的节点中移除`Person`标签。注意‼️‼️‼️，这并不是删除节点本身，而只是移除该节点的`Person`标签。🌿🌿🌿<br>
`set m:Actor`:<br>
- 这是一个设置操作，它为与变量`m`匹配的节点添加`Actor`标签。🌿🌿🌿<br>
`RETURN m`:<br>
- 这个指令表示将经过上述操作修改的节点返回给用户。<br>

简而言之，这个Cypher语句的功能是找到名为'李斯'的`Person`节点，移除其`Person`标签，并为其添加一个`Actor`标签，然后返回这个修改后的节点。<br>

假如你是想将 `李斯` 设定为2种实体类型，可以参考下方语句写法：<br>
```sql
MATCH (m:Person{true_name:'李斯'}) remove m:Person  set m:Actor:Man
```

### 为节点和关系添加多个属性：
前面折腾张三和李四(斯)已经够多了，这里暂且放过他们，同时用一个简单的例子实现为节点和关系添加多个属性，这样也方便大家查看效果。如果你只想为单个节点添加多个属性可以使用以下代码：<br>
```sql
MERGE (a:Person {name: 'Alice', age: 30, email: 'alice@example.com'})
```

如果你想同时为节点和关系添加多个属性，可以使用以下代码：🤗🤗🤗<br>
```sql
MERGE (m:Person {name: 'Alice', age: 30, email: 'alice@example.com'})-[r:KNOWS {since: 2020, reason: 'work'}]->(n:Person {name: 'Bob', age: 26, email: 'bob@example.com'})
return m,r,n
```
Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/59e9c5e7-17cd-45cf-b9b7-dc2d43d39b64" alt="image" width="50%" height="50%">

这里再回顾一下查询，假如你想要查看节点 `Alice` 的 `email` 属性的值，使用下列语句即可：<br>
```sql
MATCH (m:Person {name: 'Alice'}) RETURN m.email
```
Neo4j效果如下：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/053bbba1-3a9a-4dcd-9336-b7ba5db3d243" alt="image" width="50%" height="50%">

### 删除指定关系：
假设你现在想删除张三和李四之间的"前姐夫"关系，运行下列语句即可：(做法与 `更新Neo4j中实体间的关系` 那一节的语句相似)<br>
```sql
MATCH (zhangsan:Person {true_name: '张三'})-[r:前姐夫]->(lisi:Person {true_name: '李斯'})
DELETE r

RETURN zhangsan, lisi
```
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/6ba391a2-760d-451f-943a-3c1f9c950da7" alt="image" width="70%" height="70%">
<br>

如果你是想要删除所有 `Person` 类型实体间的 `前姐夫` 关系，可以使用下列语句：<br>
```sql
MATCH (m:Person)-[r:前姐夫]->(n:Person)
DELETE r

RETURN m, n
```

### 删除Neo4j中所有节点和关系：
删除操作无法撤回，尤其是删除所有‼️‼️‼️除非你打算删库跑路🥴🥴🥴<br>
```sql
MATCH (m) OPTIONAL MATCH (m)-[r]-() DELETE m, r
```

## python与Neo4j：
在 Neo4j Desktop 中输入 Cypher 语句执行查询等操作是我们工作中必须要掌握的本领，但更常见的是我们使用代码与Neo4j连接执行操作，笔者常用的语言为python，这里就介绍python连接Neo4j的常见操作。<br>

笔者惯用 `py2neo` 库连接 Neo4j，安装方法非常简单：<br>
```shell
pip install py2neo
```

### 测试python与Neo4j的连接状态：
如果你是访问远程Neo4j数据库，可以按照类似下方代码的方式，修改自己的信息进行测试。如果你开了多个Neo4j数据库，注意端口是否正确。🚀🚀🚀<br>
```python
from py2neo import Graph
try:
    print('----开始尝试连接Neo4j----')
    # 连接到Neo4j数据库
    Graph('neo4j://8.140.203.xxx:7687', auth=("neo4j", "Flameaway3."))
    print('Neo4j连接成功!!!')
except:
    print('Neo4j连接失败')
```
如果你是在部署Neo4j的机器上操作，将 `ip` 改为 `localhost` 即可。<br>
```python
from py2neo import Graph
try:
    print('----开始尝试连接Neo4j----')
    # 连接到Neo4j数据库
    Graph('neo4j://localhost:7687', auth=("neo4j", "Flameaway3."))
    print('Neo4j连接成功!!!')
except:
    print('Neo4j连接失败')
```

### 创建三元组：
`py2neo` 支持很多类似Neo4j中Cypher的操作，比如 `create`、`Node` 等方法，但笔者用的最多的还是 `Graph` 对象和 `run` 方法，`Graph` 对象可以直接接受Cypher语句，然后使用 `run` 方法运行Cypher语句。<br>

`Graph` 对象和 `run` 方法的使用的使用很简单，通过复用之前的代码，这里介绍下具体操作：<br>
```python
from py2neo import Graph

# 连接到Neo4j数据库
graph = Graph('neo4j://localhost:7688', auth=("neo4j", "Giveaway3."))

# 使用MERGE创建或查找节点和关系
cypher_query = """
MERGE (zhangsan:Person {name: '张三'})
MERGE (lisi:Person {name: '李四'})
MERGE (zhangsan)-[:同事]->(lisi)
MERGE (zhangsan)-[:姐夫]->(lisi)
MERGE (zhangsan)-[:领导]->(lisi)
RETURN zhangsan, lisi
"""

result = graph.run(cypher_query)
```

### 获取三元组的值：
获取三元组的值时需要采用 `graph.run().data()` 方法，这样才方便操作～🌿🌿🌿<br>

假设我们构建三元组的代码如下：<br>
```python
from py2neo import Graph

# 连接到Neo4j数据库
graph = Graph('neo4j://localhost:7688', auth=("neo4j", "Giveaway3."))

# 使用MERGE来创建节点和关系信息
cypher_query = """
MERGE (m:Word {name: '卖出'})-[r:Pat {name_zh: '受事', snowflake_id: 7104708589926234047}]->(n:Word {name: '钢琴'})
return m,r,n
"""

result = graph.run(cypher_query)
```
我们如果想要利用 `py2neo` 获取详细的实体和关系信息，可以使用如下代码：<br>
```python
from py2neo import Graph

# 连接到Neo4j数据库
graph = Graph('neo4j://localhost:7688', auth=("neo4j", "Giveaway3."))

# 使用MATCH来查找节点和关系信息
cypher_query = """
MATCH (m:Word {name: '卖出'})-[r:Pat {name_zh: '受事', snowflake_id: 7104708589926234047}]->(n:Word {name: '钢琴'})
RETURN m, n, r
"""

result = graph.run(cypher_query).data()
# print(result)
# [{'m': Node('Word', name='卖出'), 'n': Node('Word', name='货币三佳'), 'r': Pat(Node('Word', name='卖出'), Node('Word', name='货币三佳'), snowflake_id=7104708589926234047)}]

#########################
# m 信息
#########################
node_m_info = result[0]['m']['name']
print(node_m_info)  # 卖出，类型为 str

#########################
# n 信息
#########################
node_n_info = result[0]['n']['name']
print(node_n_info)  # 钢琴，类型为 str

#########################
# relation 信息
#########################
relationship = result[0]['r']
relationship_type = type(relationship).__name__
print(relationship_type)  # Pat，类型为 str

name_zh = relationship['name_zh']
print(name_zh)        # 受事，类型为 str

snowflake_id = relationship['snowflake_id']
print(snowflake_id)        # 7104708589926234047，类型为 int
```

## 卸载Neo4j：

如果你是按照我的方式(安装包)安装的Neo4j，卸载非常简单，只需要2步：<br>

1. 删除`/opt`路径下的Neo4j文件;
2. 删除`~/.bashrc`文件中NEO4J_HOME的环境变量即可；


如果你是通过其他方式安装的Neo4j，要完全卸载 Neo4j 数据库，你可以按照以下步骤进行操作：<br>

1. **停止 Neo4j 服务**：

在终端中运行以下命令，以确保 Neo4j 服务器已停止运行：<br>

```bash
sudo service neo4j stop
```

2. **卸载 Neo4j 软件包**：

使用以下命令卸载 Neo4j 软件包：<br>

```bash
sudo apt-get remove neo4j
```

3. **删除配置文件和数据**：

删除 Neo4j 的配置文件和数据目录，以确保所有数据都被清除。默认情况下，这些文件位于 `/etc/neo4j/` 和 `/var/lib/neo4j/` 目录中。你可以使用以下命令删除这些目录：<br>

```bash
sudo rm -rf /etc/neo4j/
sudo rm -rf /var/lib/neo4j/
```

4. **删除 Neo4j 用户和组**：

Neo4j 安装通常会创建一个系统用户和组。你可以使用以下命令删除它们：<br>

```bash
sudo userdel neo4j
sudo groupdel neo4j
```

5. **清除其他残留文件**：

你可能还需要检查其他可能残留的配置文件或日志文件，并删除它们。<br>

6. **卸载 Java**（可选）：

如果你的系统上安装了 Neo4j 之前的 Java 版本，你可以选择卸载它们，或者保留它们，具体取决于你的需求。<br>

完成上述步骤后，Neo4j 就会被完全卸载并清除了与其相关的文件和配置。请务必小心操作，并确保备份任何重要数据，因为这些步骤将永久删除与 Neo4j 相关的所有内容。<br>


## 为不同用户设置不同JDK：

不同用户可以设置不同的JDK版本，例如：root用户使用JDK 11，普通用户使用JDK 8。具体的操作如下：<br>

1. **配置默认 Java 版本**。假设你想要配置root用户默认使用的JDK版本为11。使用以下命令查看系统上所有的 Java 版本：

```bash
sudo update-alternatives --config java
```

在出现的列表中，选择 Java 11（它应该有一个编号，`*`开头的是当前所用的Java版本）。按照指示输入相应的数字(类似0，1，2)，然后按 Enter。<br>

2. **配置默认 Javac 版本**（这是 Java 的编译器）。与配置 Java 命令类似：

```bash
sudo update-alternatives --config javac
```

再次在列表中选择 Java 11。<br>

3. **设置 `JAVA_HOME` 环境变量**。编辑 `/root/.bashrc`或`/etc/profile` 文件：

> 在`.bashrc`中设置环境变量是一种很好的习惯，无论你采用那种防止设置环境变量，一定要注意不要将你的环境变量写的太分散，否则后续想要修改非常麻烦。<br>
> 今天在`/root/.bashrc`中写环境变量，明天在`/etc/profile`中写环境变量，后天在`/etc/environment`中写环境变量，这种方式是非常不可取的。❌❌❌<br>


```bash
vim /root/.bashrc
```

在文件的末尾添加以下行：<br>

```
JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
```

然后保存并关闭文件。<br>

为了让这个变更生效，需要使用以下命令：<br>

```bash
source /root/.bashrc
```

如果你修改的是`/etc/profile`文件，生效指令类似：<br>

```bash
source /etc/profile
```

## 卸载JDK：

假设你的系统中有多个jdk，你想要删除 `java-1.8.0-openjdk-amd64`，可以参考如下方式：<br>

1. 终端输入以下指令查看jdk信息：<br>

```bash
update-java-alternatives --list
```

由下图可知，你的系统中同时存在jdk8和jdk11。<br>

```log
java-1.11.0-openjdk-amd64      1111       /usr/lib/jvm/java-1.11.0-openjdk-amd64
java-1.8.0-openjdk-amd64       1081       /usr/lib/jvm/java-1.8.0-openjdk-amd64
```

2. 使用`apt-get`卸载Java 8的OpenJDK包。执行以下命令：

```bash
sudo apt-get purge openjdk-8-jre openjdk-8-jre-headless openjdk-8-jdk openjdk-8-jdk-headless
```

3. 删除任何相关的未使用的依赖包：

```bash
sudo apt-get autoremove
```

4. 更新软件包列表：

```bash
sudo apt-get update
```

5. 为了确保Java 8已完全从你的系统中删除，你可以检查`/usr/lib/jvm/`目录下的内容。执行以下命令：

```bash
ls /usr/lib/jvm/
```

确保`java-1.8.0-openjdk-amd64`目录不再存在。<br>

6. 你还可以再次运行`update-java-alternatives --list`命令来确保Java 8不再列出。

执行上述步骤后，Java 8的OpenJDK应该已从你的Ubuntu 18.04系统中完全删除。<br>
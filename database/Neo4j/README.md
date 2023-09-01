# Neo4j
Neo4j是一种图形数据库管理系统，用于存储和管理图形数据。它是一个基于Java的开源软件，支持高度可扩展的图形数据模型，可以用于各种应用领域，如社交网络分析、推荐系统、网络安全分析等。Neo4j使用Cypher查询语言来操作和查询图形数据，并提供了丰富的API和工具来帮助开发人员与数据库进行交互。由于其图形数据模型的优势，Neo4j可以有效地表示和处理复杂的关系数据，提供了快速且灵活的数据访问和分析能力。<br>

虽然Neo4j是基于Java的软件，但不妨碍我们python用户使用🤣🤣🤣。接下来，笔者就讲一下 Ubuntu 18.4 安装Neo4j 4.1.0和Neo4j的使用经验。<br>
- [Neo4j](#neo4j)
  - [Neo4j的安装：](#neo4j的安装)
    - [更新系统软件包信息：](#更新系统软件包信息)
    - [安装jdk11:](#安装jdk11)
    - [下载安装包：](#下载安装包)
    - [安装包上传/移动到指定位置：](#安装包上传移动到指定位置)
    - [解压tar.gz文件：](#解压targz文件)
    - [修改neo4j.conf 中的配置，开放远程连接限制:](#修改neo4jconf-中的配置开放远程连接限制)
    - [更改默认密码：](#更改默认密码)
    - [修改环境变量:](#修改环境变量)
    - [开启服务器端口：](#开启服务器端口)
    - [启动/关闭 Neo4j 数据库：](#启动关闭-neo4j-数据库)
    - [Neo4j Desktop 连接远程Neo4j数据库：](#neo4j-desktop-连接远程neo4j数据库)
  - [终端Neo4j常用指令：](#终端neo4j常用指令)
  - [Neo4j Desktop 中常用Cypher语句：](#neo4j-desktop-中常用cypher语句)
    - [CREATE创建有向关系示例：](#create创建有向关系示例)
    - [查询创建的节点和关系：](#查询创建的节点和关系)
    - [常用查询语句：](#常用查询语句)
    - [CREATE创建中文三元组：](#create创建中文三元组)
    - [MERGE创建三元组：](#merge创建三元组)
    - [CREATE的必要性：](#create的必要性)
    - [为2个节点创建多个关系：](#为2个节点创建多个关系)
    - [更新Neo4j中实体间的关系：](#更新neo4j中实体间的关系)
    - [更新Neo4j中实体的属性的值：](#更新neo4j中实体的属性的值)
    - [更新Neo4j中实体的属性的名称：](#更新neo4j中实体的属性的名称)
    - [更新Neo4j中实体的类型：](#更新neo4j中实体的类型)
  - [删除Neo4j中所有节点和关系：](#删除neo4j中所有节点和关系)

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
也可以通过域名测试连接状态，例如：<br>
```shell
telnet my_server.com 7474
```

## 终端Neo4j常用指令：
启动Neo4j数据库作为后台服务:<br>
```shell
neo4j start
```
停止Neo4j数据库服务:<br>
```shell
neo4j stop
```
重新启动Neo4j数据库服务:<br>
```shell
neo4j restart
```
检查Neo4j数据库服务的状态:<br>
```shell
neo4j status
```
显示Neo4j的版本信息:<br>
```shell
neo4j version
```
以控制台模式查看 Neo4j 数据库基本信息:<br>
```shell
neo4j console 
```

## Neo4j Desktop 中常用Cypher语句：
在Neo4j中，关系是有向的‼️‼️‼️。这意味着当你创建一个关系时，你必须指定它的方向🥶🥶🥶。然而，当查询这些关系时，你可以选择忽略方向🥴🥴🥴。<br>

### CREATE创建有向关系示例：
假设你想创建一个描述 `汤姆抓杰瑞` 的三元组信息，你可以使用以下指令：<br>
```sql
// 汤姆抓杰瑞，neo4j支持以 "//" 作为注释
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

节点或关系颜色可以通过点击对应图标设置：<br>
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
> 默认情况下，当你不指定排序或其他筛选条件时，Neo4j可能会基于内部存储和处理的顺序返回结果，这可能会看起来像是随机的，尤其是在大型数据集中。
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
举例来说，当你依次运行下面两个语句时，会在Neo4j中创建2个张三节点，而不是关联了2组关系。<br>
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


如果你是想将2组关系关联起来，需要使用关键字 `MERGE` ：<br>
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

‼️‼️‼️注意：`MERGE` 的使用一定要正确，要按照上述语句中的逻辑。举个例子，假设你依次运行了下面2个语句，猜猜会发生什么~🥴🥴🥴<br>
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
答案是和使用 `CREATE` 效果相同，会在Neo4j中创建2个张三节点，而不是关联了2组关系。🥹🥹🥹<br>
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

### 更新Neo4j中实体的属性的名称：
假设你现在觉得 `name` 属性无法完全体现 `李斯` 的意义，想要将 `name` 属性的名称改为 `true_name` 可以使用以下语句：<br>
```sql
MATCH (lisi:Person {name: '李斯'})
SET lisi.true_name = lisi.name
REMOVE lisi.name
RETURN lisi
```
Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/4e86442b-8390-4eb0-bfac-8590d7f3784f" alt="image" width="50%" height="50%">

### 更新Neo4j中实体的类型：
那如何将李斯的实体类型改为Actor，属性name改为true_name呢？<br>

假如 `李斯` 翻身了，从一个普通人变成了 `Actor`，你此时需要将他的标签类型更改，可以使用下列语句：<br>
```sql
MATCH (m:Person{name:'李斯'}) remove m:Person  set m:Actor
RETURN m
```
Cypher语句解释：<br>
`MATCH (m:Person{name:'李斯'})`: <br>
- 这是一个匹配指令，它在数据库中查找一个标签为`Person`且`name`属性为 `'李斯'` 的节点，并将其赋给变量`m`。<br>
`remove m:Person`:<br>
- 这是一个删除操作，它从与变量`m`匹配的节点中移除`Person`标签。注意‼️‼️‼️，这并不是删除节点本身，而只是移除该节点的`Person`标签。🌿🌿🌿<br>
`set m:Actor`:<br>
- 这是一个设置操作，它为与变量`m`匹配的节点添加`Actor`标签。🌿🌿🌿<br>
`RETURN m`:<br>
- 这个指令表示将经过上述操作修改的节点返回给用户。<br>

简而言之，这个Cypher语句的功能是找到名为'李斯'的`Person`节点，移除其`Person`标签，并为其添加一个`Actor`标签，然后返回这个修改后的节点。<br>

```sql
MATCH (m:Actor {name: '李斯'})
SET lisi.name = '李斯'
RETURN lisi
```


```sql
MATCH (m:Person{name:'李斯'}) remove m:Person  set m:Actor:Man
```

## 删除Neo4j中所有节点和关系：
删除操作无法撤回，尤其是删除所有‼️‼️‼️除非你打算删库跑路🥴🥴🥴<br>
```sql
MATCH (m) OPTIONAL MATCH (m)-[r]-() DELETE m, r
```

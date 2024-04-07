# backup_and_migration_of_neo4j_data

本章介绍Neo4j数据备份与迁移。<br>
- [backup\_and\_migration\_of\_neo4j\_data](#backup_and_migration_of_neo4j_data)
  - [Neo4j Desktop配合apoc插件进行Neo4j数据迁移：](#neo4j-desktop配合apoc插件进行neo4j数据迁移)
    - [安装对应版本的apoc:](#安装对应版本的apoc)
    - [apoc 文件选择与下载：](#apoc-文件选择与下载)
    - [将apoc文件移动到Neo4j的插件目录：](#将apoc文件移动到neo4j的插件目录)
    - [修改neo4j.conf中apoc设置：](#修改neo4jconf中apoc设置)
    - [启动或重新启动Neo4j数据库：](#启动或重新启动neo4j数据库)
    - [验证apoc插件是否成功安装：](#验证apoc插件是否成功安装)
    - [查看Neo4j数据库中的节点情况：](#查看neo4j数据库中的节点情况)
    - [导出 Neo4j 数据库中的数据：](#导出-neo4j-数据库中的数据)
      - [导出孤立节点：](#导出孤立节点)
      - [导出常规关系型节点、边：](#导出常规关系型节点边)
    - [将cypher文件移至新的neo4j数据库的import文件夹下：](#将cypher文件移至新的neo4j数据库的import文件夹下)
    - [重复在本地Neo4j安装apoc插件的操作：](#重复在本地neo4j安装apoc插件的操作)
    - [利用Neo4j Desktop导入数据：](#利用neo4j-desktop导入数据)
    - [查看效果：](#查看效果)

## Neo4j Desktop配合apoc插件进行Neo4j数据迁移：

Apoc可以将Neo4j中的数据以`xxx.cypher`脚本的形式导出，在导入时可以直接运行`xxx.cypher`脚本构建节点和关系，不需要自己额外写构建节点、关系的代码。<br>

这种做法类似于Navicat将MySQL数据导出为`xxx.sql`脚本，既方便又快速，推荐大家使用。🫠🫠🫠<br>

### 安装对应版本的apoc:

笔者安装的 Neo4j 版本为 4.1.0，所以需要安装 apoc 4.1.0.x版本；apoc的下载链接如下：<br>

```log
https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/tag/4.1.0.12
```

### apoc 文件选择与下载：

进入链接后，下拉进度条至Assets模块，就是我们需要的文件。其中有很多文件，接下来笔者逐个解释一下：<br>

- apoc-4.1.0.12-all.jar：这是apoc库的主要JAR文件，包含了所有功能和函数。这是必需的文件，用于安装apoc库的核心功能。❤️

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其他的apoc-*-dependencies-4.1.0.12.jar文件是用于支持特定功能的依赖库。根据你的需求，你可以选择安装这些依赖库文件。<br>

- apoc-couchbase-dependencies-4.1.0.12.jar：用于支持与Couchbase NoSQL数据库的集成。
- apoc-email-dependencies-4.1.0.12.jar：用于支持发送电子邮件的功能。
- apoc-mongodb-dependencies-4.1.0.12.jar：用于支持与MongoDB NoSQL数据库的集成。
- apoc-nlp-dependencies-4.1.0.12.jar：用于支持自然语言处理（NLP）相关功能。
- apoc-redis-dependencies-4.1.0.12.jar：用于支持与Redis数据库的集成。
- apoc-xls-dependencies-4.1.0.12.jar：用于支持处理Excel文件的功能。

🚨🚨🚨请注意，这些依赖库文件不是必需的，只有在你需要相关功能时才需要安装它们。**如果你只想安装apoc库的核心功能，只需下载apoc-4.1.0.12-all.jar文件即可**。<br>

### 将apoc文件移动到Neo4j的插件目录：

1. 在你的Neo4j安装目录下找到 plugins 文件夹。

如果你是按照笔者的教程安装的Neo4j，plugins的路径如下，将`apoc-4.1.0.12-all.jar`让入路径下即可(不需要解压🥴)：<br>

```bash
/opt/neo4j-community-4.1.0/plugins
```

如果你是接手的其他人的项目，不知道`plugins`目录位置，可以通过`neo4j.conf`文件中的信息查看，`neo4j.conf`文件中对应的信息如下：<br>

```log
# Paths of directories in the installation.
#dbms.directories.data=data
#dbms.directories.plugins=plugins
#dbms.directories.logs=logs
#dbms.directories.lib=lib
#dbms.directories.run=run
#dbms.directories.transaction.logs.root=data/transactions

# This setting constrains all `LOAD CSV` import files to be under the `import` directory. Remove or comment it out to
# allow files to be loaded from anywhere in the filesystem; this introduces possible security problems. See the
# `LOAD CSV` section of the manual for details.
dbms.directories.import=import
```

> import的路径就是apoc输出的cypher脚本的存储路径：

由于笔者是通过安装包安装的，所以`data`、`plugins`等文件是集中在一起的，默认情况下`neo4j.conf`中的路径是注释的。某些情况下，部分用户可能会改变这些路径，以`plugins`为例，用户可能改为:<br>

```log
dbms.directories.plugins=/var/lib/neo4j/plugins
```

如果是这种情况，将`apoc-4.1.0.12-all.jar`文件放入`/var/lib/neo4j/plugins`路径下即可。<br>

如果你连`neo4j.conf`都不知道在哪里，可以终端输入下列指令全局搜索`neo4j.conf`所在路径：<br>

```bash
find / -name "neo4j.conf"
```

### 修改neo4j.conf中apoc设置：

首先找到自己的 `neo4j.conf` 文件，我的`neo4j.conf`文件在以下路径中：<br>

```log
/opt/neo4j-community-4.1.0/conf
```

使用 vim 将apoc部分修改为如下形式：<br>

```log
# A comma separated list of procedures to be loaded by default.
# Leaving this unconfigured will load all procedures found.
#dbms.security.procedures.whitelist=apoc.coll.*,apoc.load.*
dbms.security.procedures.unrestricted=apoc.*

apoc.export.file.enabled=true
apoc.import.file.enabled=true
```


### 启动或重新启动Neo4j数据库：

如果Neo4j数据库正在运行，执行以下指令，重启Neo4j以加载新安装的apoc插件:<br>

```bash
neo4j restart
```

如果Neo4j数据库没有启动，执行以下指令，启动并加载新安装的apoc插件：<br>

```bash
neo4j start
```

### 验证apoc插件是否成功安装：

打开`Neo4j Desktop`，输入如下指令，查看 apoc 版本号。若有版本号，则成功；<br>

```sql
return apoc.version()
```

正常情况下会显示：<br>

```log
apoc.version()
"4.1.0.12"
```

### 查看Neo4j数据库中的节点情况：

打开`Neo4j Desktop`，输入以下指令，查看Neo4j数据库中的节点情况：<br>

> ⚠️注意记录查看到的结果，方便比较数据迁移前后是否存在数据丢失。

查询所有节点的数量(包含孤立节点的数量；)：<br>

```sql
MATCH (n) RETURN count(n) AS nodeCount;
```

查看孤立节点的数量(没有关系的孤立节点不要遗漏了～):<br>

```sql
MATCH (n)
WHERE NOT ()-[]-(n)
RETURN count(n) AS isolatedNodeCount
```

如果孤立节点数量为0，说明所有节点之间都构建了关系。<br>


查询关系类型总体的数量，只返回一个值。<br>

```sql
MATCH ()-[r]->()
RETURN count(r) AS relationshipCount
```

🚨🚨🚨数据迁移时，如果你的Neo4j中关系类型特别多，比较每一个关系类型的样本数量不是一个好的选择。<br>

### 导出 Neo4j 数据库中的数据：

打开`Neo4j Desktop`，依次输入以下指令，即可在Neo4j的`import`目录下生成`xxx.cypher`文件：<br>

#### 导出孤立节点：

孤立节点：没有构建关系，不代表没有用处，不要遗忘了～<br>

```sql
CALL apoc.export.cypher.query('MATCH (n) WHERE NOT ()-[]-(n) RETURN n', 'single_nodes.cypher', {})
```

#### 导出常规关系型节点、边：

```sql
CALL apoc.export.cypher.query('MATCH (n)-[r]->(m) RETURN n, r, m ', "all_relation_data.cypher", {}) 
```

❤️❤️❤️现在Neo4j的`import`目录下已经有了**你自己定义名称的`xxx.cypher`文件。**<br>


### 将cypher文件移至新的neo4j数据库的import文件夹下：

cypher文件需要放在Neo4j数据库的import文件夹下才能被导入，所以需要将你上一步生成的`xxx.cypher`文件放入待接收数据的Neo4j的import文件夹下。<br>

假设你是要将数据从本地Neo4j迁移至阿里云服务器部署的neo4j数据库中，你在阿里云服务器部署的neo4j数据库也是按照笔者的教程安装的，那么Neo4j的import文件夹路径为：<br>

```bash
/opt/neo4j-community-4.1.0/import/
```

### 重复在本地Neo4j安装apoc插件的操作：

1. 以同样的方式安装apoc插件；

2. 以同样的方式修改阿里云服务器上部署的`neo4j.conf`文件；

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;与前面的操作相同，同样要注意 "neo4j的版本和apoc的版本" 要一致；<br>

3. 启动或重新启动Neo4j数据库：

如果Neo4j数据库正在运行，请重启它以加载新安装的apoc库:<br>

```bash
neo4j restart
```

如果Neo4j数据库尚未启动，请启动它:<br>

```bash
neo4j start
```

4. 打开`Neo4j Desktop`，输入如下指令，查看 apoc 版本号。若有版本号，则成功；<br>

```sql
return apoc.version()
```

### 利用Neo4j Desktop导入数据：

在`Neo4j Desktop`，输入如下指令，依次导入你放在import文件夹下的数据：<br>

```sql
CALL apoc.cypher.runFile('file:///single_nodes.cypher');
```

```sql
CALL apoc.cypher.runFile('file:///all_relation_data.cypher');
```

上述指令会默认读取import路径下的`xxx.cypher`文件，将以上指令中的cypher脚本名称替换为自己的cypher脚本即可。<br>

现在，静静等待数据导入即可，可打开客户端侧边栏查看导入进度，节点导入的快，关系构建慢。<br>

🚨🚨🚨注意对比数据迁移前后数据是否有数据丢失，这就是前面让你查看节点和关系数量的原因，尽可能避免因数据丢失造成的个人工作量上升。<br>

### 查看效果：

数据导入后，我们可以使用以下cypher语句查看数据是否确实正常导入：<br>

查看25个节点和关系:<br>

```sql
MATCH (n)-[r]->(m) RETURN n, r, m LIMIT 25
```

查看所有节点和关系:<br>

```sql
MATCH (n)-[r]->(m) RETURN n, r, m
```

查看所有关系:<br>

```sql
MATCH ()-[r]->() RETURN r
```

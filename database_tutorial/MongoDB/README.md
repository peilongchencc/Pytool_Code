# MongoDB:
MongoDB是一种开源的NoSQL数据库(非关系型数据库)管理系统，它使用文档数据库模型来存储数据。<br>

🥴🥴🥴与传统的关系型数据库（如MySQL、Oracle等）不同，它不使用表格来组织数据，而是使用类似JSON的文档来存储数据。<br>

这使得MongoDB非常适合存储和处理半结构化或非结构化数据，以及需要高度可扩展性和灵活性的应用程序。<br>

- [MongoDB:](#mongodb)
  - [Ubuntu 18.04上安装MongoDB](#ubuntu-1804上安装mongodb)
    - [导入MongoDB公钥：](#导入mongodb公钥)
    - [添加MongoDB APT仓库：](#添加mongodb-apt仓库)
    - [更新包数据库：](#更新包数据库)
    - [安装MongoDB：](#安装mongodb)
    - [启动MongoDB服务：](#启动mongodb服务)
    - [查看mongodb版本信息：](#查看mongodb版本信息)
      - [命令行:](#命令行)
      - [使用 `mongo` 客户端:](#使用-mongo-客户端)
      - [Mongo Shell:](#mongo-shell)
  - [python使用mongodb示例：](#python使用mongodb示例)


## Ubuntu 18.04上安装MongoDB

系统|MongoDB版本|python版本
---|---|---
Ubuntu 18.04.6 LTS | db version v4.2.24 | Python 3.10.11

### 导入MongoDB公钥：

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
```

在Ubuntu 18.04（以及其他Debian和Ubuntu衍生版本）上安装软件时，导入软件源的公钥是一个常见的步骤。导入公钥可以确保从该仓库下载的软件包是原始的、未被篡改的。导入并信任公钥意味着你信任该软件源提供的软件包。这确保你只从已知和信任的源安装软件。<br>

执行效果如下：<br>
```log
(base) root@iZ2zea5v77oawjy2qxxxxxx:/data/code_draft# wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
OK
```

### 添加MongoDB APT仓库：

```bash
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
```

APT工具会使用上述公钥来验证下载的软件包的签名。<br>

执行效果如下：<br>
```log
(base) root@iZ2zea5v77oawjy2qxxxxxx:/data/code_draft# echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse
```

### 更新包数据库：

```bash
sudo apt-get update
```

执行效果如下：<br>
```log
(base) root@iZ2zea5v77oawjy2qxxxxxx:/data/code_draft# sudo apt-get update
Hit:1 http://mirrors.cloud.aliyuncs.com/ubuntu bionic InRelease
Get:2 http://mirrors.cloud.aliyuncs.com/ubuntu bionic-updates InRelease [88.7 kB]      
Get:3 http://mirrors.cloud.aliyuncs.com/ubuntu bionic-backports InRelease [83.3 kB]    
Get:4 http://mirrors.cloud.aliyuncs.com/ubuntu bionic-security InRelease [88.7 kB]             
Get:5 http://mirrors.cloud.aliyuncs.com/ubuntu bionic-updates/main Sources [546 kB] 
Get:6 http://mirrors.cloud.aliyuncs.com/ubuntu bionic-updates/main i386 Packages [1,665 kB]               
Get:7 http://mirrors.cloud.aliyuncs.com/ubuntu bionic-updates/main amd64 Packages [3,045 kB]                         
Ign:8 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 InRelease                                                           
Get:9 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 Release [3,096 B]
Get:10 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 Release.gpg [801 B]
Get:11 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 Packages [29.0 kB]
Fetched 5,549 kB in 3s (1,952 kB/s)
Reading package lists... Done
```

### 安装MongoDB：

```bash
sudo apt-get install -y mongodb-org
```

执行效果如下：<br>
```log
(base) root@iZ2zea5v77oawjy2qxxxxxx:/data/code_draft# sudo apt-get install -y mongodb-org
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  gyp javascript-common libc-ares2 libhttp-parser2.7.1 libjs-async libjs-inherits libjs-jquery libjs-node-uuid libjs-underscore libssl1.0-dev libuv1 libuv1-dev node-abbrev node-ansi
  node-ansi-color-table node-archy node-async node-balanced-match node-block-stream node-brace-expansion node-builtin-modules node-combined-stream node-concat-map node-cookie-jar
  node-delayed-stream node-forever-agent node-form-data node-fs.realpath node-fstream node-fstream-ignore node-github-url-from-git node-glob node-graceful-fs node-gyp node-hosted-git-info
  node-inflight node-inherits node-ini node-is-builtin-module node-isexe node-json-stringify-safe node-lockfile node-lru-cache node-mime node-minimatch node-mkdirp node-mute-stream node-node-uuid
  node-nopt node-normalize-package-data node-npmlog node-once node-osenv node-path-is-absolute node-pseudomap node-qs node-read node-read-package-json node-request node-retry node-rimraf
  node-semver node-sha node-slide node-spdx-correct node-spdx-expression-parse node-spdx-license-ids node-tar node-tunnel-agent node-underscore node-validate-npm-package-license node-which
  node-wrappy node-yallist nodejs nodejs-dev nodejs-doc python-pkg-resources
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  mongodb-org-mongos mongodb-org-server mongodb-org-shell mongodb-org-tools
The following NEW packages will be installed:
  mongodb-org mongodb-org-mongos mongodb-org-server mongodb-org-shell mongodb-org-tools
0 upgraded, 5 newly installed, 0 to remove and 39 not upgraded.
Need to get 98.5 MB of archives.
After this operation, 298 MB of additional disk space will be used.
Get:1 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 mongodb-org-shell amd64 4.2.24 [12.2 MB]
Get:2 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 mongodb-org-server amd64 4.2.24 [18.9 MB]
Get:3 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 mongodb-org-mongos amd64 4.2.24 [10.3 MB]
Get:4 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 mongodb-org-tools amd64 4.2.24 [57.1 MB]
Get:5 https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2/multiverse amd64 mongodb-org amd64 4.2.24 [3,520 B]                                                                                
Fetched 98.5 MB in 9s (10.8 MB/s)                                                                                                                                                                   
Selecting previously unselected package mongodb-org-shell.
(Reading database ... 114219 files and directories currently installed.)
Preparing to unpack .../mongodb-org-shell_4.2.24_amd64.deb ...
Unpacking mongodb-org-shell (4.2.24) ...
Selecting previously unselected package mongodb-org-server.
Preparing to unpack .../mongodb-org-server_4.2.24_amd64.deb ...
Unpacking mongodb-org-server (4.2.24) ...
Selecting previously unselected package mongodb-org-mongos.
Preparing to unpack .../mongodb-org-mongos_4.2.24_amd64.deb ...
Unpacking mongodb-org-mongos (4.2.24) ...
Selecting previously unselected package mongodb-org-tools.
Preparing to unpack .../mongodb-org-tools_4.2.24_amd64.deb ...
Unpacking mongodb-org-tools (4.2.24) ...
Selecting previously unselected package mongodb-org.
Preparing to unpack .../mongodb-org_4.2.24_amd64.deb ...
Unpacking mongodb-org (4.2.24) ...
Setting up mongodb-org-shell (4.2.24) ...
Setting up mongodb-org-mongos (4.2.24) ...
Setting up mongodb-org-tools (4.2.24) ...
Setting up mongodb-org-server (4.2.24) ...
Adding system user `mongodb' (UID 111) ...
Adding new user `mongodb' (UID 111) with group `nogroup' ...
Not creating home directory `/home/mongodb'.
Adding group `mongodb' (GID 120) ...
Done.
Adding user `mongodb' to group `mongodb' ...
Adding user mongodb to group mongodb
Done.
Setting up mongodb-org (4.2.24) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
```

### 启动MongoDB服务：

```bash
sudo systemctl start mongod
```

执行效果如下：<br>
```log
(base) root@iZ2zea5v77oawjy2qxxxxxx:/data/code_draft# sudo systemctl start mongod
(base) root@iZ2zea5v77oawjy2qxxxxxx:/data/code_draft# 
```

如果你想让MongoDB在启动时自动启动，可以使用：<br>

```bash
sudo systemctl enable mongod
```

执行效果如下：<br>
```log
(base) root@iZ2zea5v77oawjy2qxxxxxx:/data/code_draft# sudo systemctl enable mongod
Created symlink /etc/systemd/system/multi-user.target.wants/mongod.service → /lib/systemd/system/mongod.service.
```

### 查看mongodb版本信息：

现在，MongoDB已经安装并正在运行。你可以选择以下任意一种方式查看mongodb版本信息:<br>

#### 命令行:

打开终端或命令行窗口，然后输入以下命令:<br>

```bash
mongod --version
```

执行效果如下：<br>
```log
(nudge_new) root@iZ2zea5v77oawjy2qxxxxxx:/data/code_draft# mongod --version
db version v4.2.24
git version: 5e4ec1d24431fcdd28b579a024c5c801b8cde4e2
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
```

#### 使用 `mongo` 客户端:

```bash
mongo --version
```

这会显示`mongod`或`mongo`客户端的版本，通常它们的版本应该是相同的。<br>

#### Mongo Shell:

如果你已经进入Mongo Shell, 可以使用以下命令来获取版本:<br>

```javascript
db.version()
```

这会显示你连接的MongoDB实例的版本。<br>


## python使用mongodb示例：

要使用Python向mongodb来插入和检索数据，你需要安装`pymongo`，这是一个Python MongoDB驱动程序：<br>

```bash
pip install pymongo
```

执行效果如下：<br>
```log
(base) root@iZ2zea5v77oawjy2qxxxxxx:/data/code_draft# pip install pymongo
Looking in indexes: http://mirrors.cloud.aliyuncs.com/pypi/simple/
Collecting pymongo
  Downloading http://mirrors.cloud.aliyuncs.com/pypi/packages/77/c8/aa46a179d476a06630cf9a5463c5edc06b938fa8894b99194ebbdc775d76/pymongo-4.5.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (675 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 675.1/675.1 kB 15.8 MB/s eta 0:00:00
Collecting dnspython<3.0.0,>=1.16.0 (from pymongo)
  Downloading http://mirrors.cloud.aliyuncs.com/pypi/packages/f6/b4/0a9bee52c50f226a3cbfb54263d02bb421c7f2adc136520729c2c689c1e5/dnspython-2.4.2-py3-none-any.whl (300 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 300.4/300.4 kB 23.6 MB/s eta 0:00:00
Installing collected packages: dnspython, pymongo
Successfully installed dnspython-2.4.2 pymongo-4.5.0
```

然后，你可以使用以下Python代码来存入并取出数据：<br>

```python
from pymongo import MongoClient

# 创建一个MongoClient连接到本地MongoDB实例
client = MongoClient('localhost', 27017)

# 选择一个数据库和集合
db = client['test_database']
collection = db['test_collection']

# 插入文档
document = {
    "name": "Alice",
    "hobbies": [
        {"name": "Reading", "level": "Intermediate"},
        {"name": "Painting", "level": "Beginner"}
    ]
}
result = collection.insert_one(document)
print(f"Inserted document with id: {result.inserted_id}")

# 取出文档
retrieved_document = collection.find_one({"name": "Alice"})
print(retrieved_document)

# 记得在结束时关闭连接
client.close()
```

此代码首先连接到本地的MongoDB服务器，然后选择一个名为`test_database`的数据库和一个名为`test_collection`的集合。之后，它插入所提供的文档并检索该文档。<br>

确保在运行此代码之前，MongoDB服务已经启动并运行。<br>
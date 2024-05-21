# Milvus Backup

Milvus Backup provides data backup and restoration features to ensure the security of your Milvus data.<br>

Milvus备份提供数据备份和恢复功能，以确保您的Milvus数据安全。<br>

- [Milvus Backup](#milvus-backup)
  - [安装Go语言](#安装go语言)
  - [Obtain Milvus Backup(获取 Milvus 备份)](#obtain-milvus-backup获取-milvus-备份)
      - [the compiled binary(预编译的二进制文件):](#the-compiled-binary预编译的二进制文件)
      - [compile from the source(源码编译):](#compile-from-the-source源码编译)
  - [Prepare configuration file(准备配置文件):](#prepare-configuration-file准备配置文件)
    - [backup.yaml 修改注意项:](#backupyaml-修改注意项)
  - [Back up data](#back-up-data)
  - [Minio Console、mc client和Attu的关系:](#minio-consolemc-client和attu的关系)
    - [1. Minio Console](#1-minio-console)
    - [2. mc client](#2-mc-client)
    - [3. Attu](#3-attu)
    - [如何理解它们之间的关系？](#如何理解它们之间的关系)
    - [总结:](#总结)


## 安装Go语言

在Ubuntu 20.04上安装Go语言不会影响您当前使用的Python环境，特别是如果您是通过Conda来管理Python环境。Conda和Go语言可以共存，并且它们不会相互干扰。以下是详细说明和步骤：

1. **下载Go语言**：

- 访问Go语言的官方网站并下载适用于Linux的安装包：[Go语言下载页面](https://golang.org/dl/)

- 或者，您可以使用以下命令直接从命令行安装Go语言：

> 需要开启网络代理，否则会提示网络连接错误。

```bash
wget https://golang.org/dl/go1.22.3.linux-amd64.tar.gz
```

2. **解压并安装**：

- 解压下载的文件并将其安装到`/usr/local`目录：

```bash
sudo tar -C /usr/local -xzf go1.22.3.linux-amd64.tar.gz
```

3. **设置环境变量**：

- 打开或创建`~/.bashrc`文件，并添加以下行：

> 如果你不知道自己的shell版本，可以终端输入 `echo $SHELL` 查看，笔者显示的是 `/bin/bash`，所以用的 `~/.bashrc`。

```bash
export PATH=$PATH:/usr/local/go/bin
```

- 重新加载配置文件：

```bash
source ~/.bashrc
```

4. **验证安装**：

- 在终端中运行以下命令验证Go语言是否安装成功：

```bash
go version
```

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/Pytool_Code# go version
go version go1.22.3 linux/amd64
```

5. **删除Go安装包:**

- 在终端中运行以下命令，删除前面下载的Go安装包:

```bash
rm go1.22.3.linux-amd64.tar.gz
```


## Obtain Milvus Backup(获取 Milvus 备份)

You can either download the compiled binary or build from the source.<br>

您可以下载编译好的二进制文件或从源代码构建。<br>

> 如果您选择从源代码构建Milvus Backup工具，那么您需要安装Go语言。如果您不想安装Go语言，可以选择直接下载预编译的二进制文件。

#### the compiled binary(预编译的二进制文件):

🥰To download the compiled binary, go to the [release page](https://github.com/zilliztech/milvus-backup/releases), where you can find all official releases.<br>

🥰要下载编译好的二进制文件，请访问发布页面，您可以在其中找到所有官方发布的版本。<br>

Remember, always use the binaries in the release marked as **Latest**.<br>

请记住，请始终使用标记为 **Latest** 的发布版本中的二进制文件。<br>

#### compile from the source(源码编译):

To compile from the source, do as follows:<br>

要从源代码进行编译，请执行以下操作：<br>

```bash
git clone git@github.com:zilliztech/milvus-backup.git
go get
go build
```


## Prepare configuration file(准备配置文件):

Download the example configuration file and tailor it to fit your needs.<br>

下载示例配置文件并根据需要进行调整。<br>

Then create a folder alongside the downloaded or built Milvus Backup binary, name the folder configs, and place the configuration file inside the configs folder.<br>

然后在下载或构建的 Milvus Backup 二进制文件旁边创建一个文件夹，命名为 configs，并将配置文件放入 configs 文件夹中。<br>

Your folder structure should be similar to the following:<br>

您的文件夹结构应类似于以下内容：<br>

```log
workspace
├── milvus-backup
└── configs
     └── backup.yaml
```

Because Milvus Backup cannot back up your data to a local path, ensure that Minio settings are correct when tailoring the configuration file.<br>

由于 Milvus Backup 无法将数据备份到本地路径，请在调整配置文件时确保 Minio 设置正确。<br>

```yaml
# Configures the system log output.
log:
  level: info # Only supports debug, info, warn, error, panic, or fatal. Default 'info'.
  console: true # whether print log to console
  file:
    rootPath: "logs/backup.log"

http:
  simpleResponse: true

# milvus proxy address, compatible to milvus.yaml
milvus:
  address: localhost
  port: 19530
  authorizationEnabled: false
  # tls mode values [0, 1, 2]
  # 0 is close, 1 is one-way authentication, 2 is two-way authentication.
  tlsMode: 0
  user: "root"
  password: "Milvus"

# Related configuration of minio, which is responsible for data persistence for Milvus.
minio:
  # cloudProvider: "minio" # deprecated use storageType instead
  storageType: "minio" # support storage type: local, minio, s3, aws, gcp, ali(aliyun), azure, tc(tencent)
  
  address: localhost # Address of MinIO/S3
  port: 9000   # Port of MinIO/S3
  accessKeyID: minioadmin  # accessKeyID of MinIO/S3
  secretAccessKey: minioadmin # MinIO/S3 encryption string
  useSSL: false # Access to MinIO/S3 with SSL
  useIAM: false
  iamEndpoint: ""
  
  bucketName: "a-bucket" # Milvus Bucket name in MinIO/S3, make it the same as your milvus instance
  rootPath: "files" # Milvus storage root path in MinIO/S3, make it the same as your milvus instance

  # only for azure
  backupAccessKeyID: minioadmin  # accessKeyID of MinIO/S3
  backupSecretAccessKey: minioadmin # MinIO/S3 encryption string
  
  backupBucketName: "a-bucket" # Bucket name to store backup data. Backup data will store to backupBucketName/backupRootPath
  backupRootPath: "backup" # Rootpath to store backup data. Backup data will store to backupBucketName/backupRootPath

backup:
  maxSegmentGroupSize: 2G

  parallelism: 
    # collection level parallelism to backup
    backupCollection: 4
    # thread pool to copy data. reduce it if blocks your storage's network bandwidth
    copydata: 128
    # Collection level parallelism to restore
    restoreCollection: 2
  
  # keep temporary files during restore, only use to debug 
  keepTempFiles: false
  
  # Pause GC during backup through Milvus Http API. 
  gcPause:
    enable: true
    seconds: 7200
    address: http://localhost:9091
```

英汉双语形式:<br>

```yaml
# 配置系统日志输出
# Configures the system log output.
log:
  level: info # 仅支持 debug、info、warn、error、panic 或 fatal。默认值为 'info'。
              # Only supports debug, info, warn, error, panic, or fatal. Default 'info'.
  console: true # 是否打印日志到控制台
                # Whether to print log to console.
  file:
    rootPath: "logs/backup.log"

http:
  simpleResponse: true

# milvus 代理地址，兼容 milvus.yaml
# milvus proxy address, compatible to milvus.yaml
milvus:
  address: localhost
  port: 19530
  authorizationEnabled: false
  # tls 模式值 [0, 1, 2]
  # 0 为关闭，1 为单向认证，2 为双向认证。
  # tls mode values [0, 1, 2]
  # 0 is close, 1 is one-way authentication, 2 is two-way authentication.
  tlsMode: 0
  user: "root"
  password: "Milvus"

# minio 相关配置，负责 Milvus 的数据持久化
# Related configuration of minio, which is responsible for data persistence for Milvus.
minio:
  # cloudProvider: "minio" # 已弃用，请使用 storageType
                          # Deprecated, use storageType instead
  storageType: "minio" # 支持的存储类型：local、minio、s3、aws、gcp、ali(aliyun)、azure、tc(tencent)
                       # Support storage type: local, minio, s3, aws, gcp, ali(aliyun), azure, tc(tencent)
  
  address: localhost # MinIO/S3 的地址
                     # Address of MinIO/S3
  port: 9000   # MinIO/S3 的端口
               # Port of MinIO/S3
  accessKeyID: minioadmin  # MinIO/S3 的 accessKeyID
                           # accessKeyID of MinIO/S3
  secretAccessKey: minioadmin # MinIO/S3 的加密字符串
                              # MinIO/S3 encryption string
  useSSL: false # 使用 SSL 访问 MinIO/S3
                # Access to MinIO/S3 with SSL
  useIAM: false
  iamEndpoint: ""
  
  bucketName: "a-bucket" # MinIO/S3 中的 Milvus 桶名称，请与您的 milvus 实例保持一致
                         # Milvus Bucket name in MinIO/S3, make it the same as your milvus instance
  rootPath: "files" # MinIO/S3 中的 Milvus 存储根路径，请与您的 milvus 实例保持一致
                    # Milvus storage root path in MinIO/S3, make it the same as your milvus instance

  # 仅适用于 Azure
  # Only for Azure
  backupAccessKeyID: minioadmin  # MinIO/S3 的 accessKeyID
                                 # accessKeyID of MinIO/S3
  backupSecretAccessKey: minioadmin # MinIO/S3 的加密字符串
                                    # MinIO/S3 encryption string
  
  backupBucketName: "a-bucket" # 用于存储备份数据的桶名称。备份数据将存储到 backupBucketName/backupRootPath
                               # Bucket name to store backup data. Backup data will store to backupBucketName/backupRootPath
  backupRootPath: "backup" # 用于存储备份数据的根路径。备份数据将存储到 backupBucketName/backupRootPath
                           # Rootpath to store backup data. Backup data will store to backupBucketName/backupRootPath

backup:
  maxSegmentGroupSize: 2G

  parallelism: 
    # 备份的集合级别并行度
    # Collection level parallelism to backup
    backupCollection: 4
    # 拷贝数据的线程池。如果占用存储的网络带宽，请减少此值
    # Thread pool to copy data. Reduce it if blocks your storage's network bandwidth
    copydata: 128
    # 恢复的集合级别并行度
    # Collection level parallelism to restore
    restoreCollection: 2
  
  # 在恢复过程中保留临时文件，仅用于调试
  # Keep temporary files during restore, only use to debug 
  keepTempFiles: false
  
  # 通过 Milvus HTTP API 在备份期间暂停 GC
  # Pause GC during backup through Milvus HTTP API.
  gcPause:
    enable: true
    seconds: 7200
    address: http://localhost:9091
```

### backup.yaml 修改注意项:

**Note**:<br>

The name of the default Minio bucket varies with the way you install Milvus. When making changes to Minio settings, do refer to the following table.<br>

| Field        | Docker Compose | Helm / Milvus Operator |
|--------------|----------------|------------------------|
| `bucketName` | a-bucket       | milvus-bucket          |
| `rootPath`   | files          | file                   |


**注意**:<br>

默认的 Minio 桶的名称因安装 Milvus 的方式不同而有所变化。在更改 Minio 设置时，请参考下表。<br>

| 字段          | Docker Compose 安装方式 | Helm 或 Milvus Operator 安装方式 |
|---------------|-------------------------|-----------------------------------|
| `bucketName`  | a-bucket                | milvus-bucket                     |
| `rootPath`    | files                   | file                              |


## Back up data

Note that running Milvus Backup against a Milvus instance will not normally affect the running of the instance.<br>

请注意，对 Milvus 实例运行 Milvus Backup 通常不会影响实例的运行。<br>

Your Milvus instance is fully functional during backup or restore.<br>

在备份或恢复期间，您的 Milvus 实例仍然可以正常运行。<br>

Run the following command to create a backup.<br>

运行以下命令以创建备份。<br>

```bash
./milvus-backup create -n <backup_name>
```

Once the command is executed, you can check the backup files in the bucket specified in the Minio settings.<br>

执行命令后，您可以在Minio设置中指定的桶中查看备份文件。<br>

Specifically, you can download them using **Minio Console** or the **mc client**.<br>

具体来说，您可以使用Minio Console或mc客户端下载它们。<br>

To download from Minio Console, log into Minio Console, locate the bucket specified in minio.address, select the files in the bucket, and click Download to download them.<br>

要从Minio Console下载，请登录Minio Console，找到在minio.address中指定的桶，选择桶中的文件，然后点击下载以下载它们。<br>

If you prefer the mc client, do as follows:<br>

如果您更喜欢mc客户端，请按以下步骤操作：<br>


## Minio Console、mc client和Attu的关系:

在Milvus中，Minio Console和mc client的使用可以让人感到困惑，尤其是当你已经熟悉Attu作为Milvus的GUI时。让我们逐一解释这些工具的功能和用途：<br>

### 1. Minio Console

**Minio Console** 是一个用于管理MinIO对象存储系统的Web界面。MinIO是一个高性能的对象存储系统，常用于存储大规模数据，特别是在云环境中。Milvus使用MinIO来管理和存储数据文件。<br>

- **功能**: 通过Minio Console，你可以轻松地浏览、上传、下载和管理存储在MinIO中的对象（如数据文件）。
- **用途**: 它主要用于运维和管理层面的操作，提供一个直观的图形界面来查看和操作MinIO存储系统中的内容。

### 2. mc client

**mc client** 是MinIO提供的命令行客户端工具，称为MinIO Client（mc）。它用于与MinIO服务器进行交互，支持文件管理和数据操作。<br>

- **功能**: mc client提供了一系列命令，用于管理MinIO存储中的文件和数据，包括上传、下载、同步、复制等操作。
- **用途**: 它更适合开发者或系统管理员在脚本和命令行环境下进行批量操作和自动化任务。

### 3. Attu

**Attu** 是Milvus提供的官方图形用户界面（GUI）。它专门用于管理和可视化Milvus数据库中的数据和元数据。<br>

- **功能**: Attu允许用户创建和管理集合（collections）、分区（partitions）、索引（indexes）、以及执行向量搜索等操作。它是一个专门针对Milvus的管理工具。
- **用途**: Attu提供一个用户友好的界面来管理Milvus实例，适合于数据科学家和工程师进行交互式数据操作和查询。

### 如何理解它们之间的关系？

- **Minio Console和mc client** 是用于管理MinIO存储系统的工具。MinIO在Milvus中扮演了存储底层数据文件的角色，因此这些工具主要涉及到数据存储和管理层面。
- **Attu** 是用于直接管理Milvus数据库的图形界面工具，专注于数据库的操作和查询，而不是底层存储管理。

### 总结:

- 使用Minio Console和mc client来管理Milvus使用的MinIO对象存储。
- 使用Attu来管理Milvus数据库本身。

如果你仅仅需要管理和操作Milvus数据库的数据，Attu将是你的主要工具。如果你还需要处理底层存储数据（例如数据备份、文件管理等），则Minio Console和mc client将是必不可少的工具。<br>
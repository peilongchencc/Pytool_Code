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

请将下列内容的注释部分改为英汉双语形式:

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

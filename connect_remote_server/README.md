# connect_remote_server
记载笔者通过 终端/vscode 连接阿里云远程服务器的一些经验，包括如何连接远程服务器，出现的错误和相应的解决方案。<br>
- [connect\_remote\_server](#connect_remote_server)
  - [连接阿里云服务器：](#连接阿里云服务器)
    - [进入实例：](#进入实例)
    - [重置实例密码：(可选)](#重置实例密码可选)
    - [workbench连接阿里云服务器：](#workbench连接阿里云服务器)
    - [终端、vscode连接阿里云服务器：](#终端vscode连接阿里云服务器)
    - [通过ssh密钥连接--创建密钥对：(强烈推荐🤭🤭🤭)](#通过ssh密钥连接--创建密钥对强烈推荐)
    - [将别人的SSH密钥添加到自己的Ubuntu 18.04服务器:](#将别人的ssh密钥添加到自己的ubuntu-1804服务器)
  - [使用阿里云提供的Redis时流量占用问题：](#使用阿里云提供的redis时流量占用问题)
    - [问题描述：](#问题描述)
    - [阿里云客服回应：](#阿里云客服回应)
  - [阿里云的RAM用户登陆和普通用户登陆有区别吗？](#阿里云的ram用户登陆和普通用户登陆有区别吗)
  - [cannot create temp file for here-document: No space left on device](#cannot-create-temp-file-for-here-document-no-space-left-on-device)
  - [Could not establish connection to "xxx.xxx.xxx.xxx": Cannot read properties of undefined (reading 'replace').](#could-not-establish-connection-to-xxxxxxxxxxxx-cannot-read-properties-of-undefined-reading-replace)
  - ["项目部署在AWS的Lambda"是什么意思？](#项目部署在aws的lambda是什么意思)

## 连接阿里云服务器：
### 进入实例：
进入个人阿里云主界面后点击相应实例名，然后点击控制台即可进入自己选择的实例～<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/1f4715ed-7157-453c-84f8-d20a61600dbb)

### 重置实例密码：(可选)
如果你忘记了自己阿里云服务器的密码，可以通过实例的主界面点击 `重置实例密码` 重新设置密码，可以参考以下图片：<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/dcc47e26-439d-45e8-a2ab-3f244b08a780)

然后会弹出下列界面：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/e399da7d-93f4-4e4f-8170-b603d8777cac" alt="image" width="70%" height="70%">


### workbench连接阿里云服务器：
可以通过密码连接阿里云服务器，也可以通过密钥连接阿里云服务器，这里先介绍一下通过密码连接阿里云服务器。<br>
1. 点击远程连接
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/3dc2c8bb-ea73-493f-b833-22613a26cd37)

2. 现在，你应该能看到以下界面，点击"立即登录"即可

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/61e0dc5f-cc77-43a3-b911-8812c7f5b59e)

3. 选择"密码认证"，然后输入个人用户名和密码，点击"确认"

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/a27ea891-09c3-4072-90de-af2acfd20c9b" alt="image" width="50%" height="50%">

现在，你应该已经进入了阿里云服务器界面了。但我不得不提醒你，通过这种方式操作很不方便，且相应速度很慢，最好的方式还是通过IDE或终端的方式连接阿里云服务器，简洁、速度快🚀🚀🚀<br>
<br>

### 终端、vscode连接阿里云服务器：
终端、vscode可以使用密码连接阿里云服务器，终端可以输入以下指令：<br>
```bash
ssh root@8.140.203.xxx
```
将 `IP` 部分改为你自己的远程服务器公网IP即可，示意图如下：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/c38a10b1-10f9-4670-8266-f784695f45c8" alt="image" width="50%" height="50%">

vscode等IDE远程连接服务器，然后操作代码，这才是我们最常见的情况。vscode等IDE远程连接服务器需要下载ssh插件，以vscode为例，需要在主界面左侧的 `拓展` 中搜索以下内容进行安装：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/4c1c0d4c-c003-4411-8472-2161a0ef37b0" alt="image" width="50%" height="50%">

然后按照下图创建连接：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/7df0264c-443b-405d-8a12-238fc20612c1" alt="image" width="70%" height="70%">

在弹出的窗口中输入以下指令：<br>
```bash
ssh root@8.140.203.xxx
```
回车后，会提示你输入密码。如果没有问题，你就会进入远程服务器中～🐳🐳🐳<br>
<br>

### 通过ssh密钥连接--创建密钥对：(强烈推荐🤭🤭🤭)
虽然用密码连接远程服务器也挺方便，但你如果用远程服务器非常频繁，就会觉得每次输密码实在太累，那么你就可以考虑使用密钥对连接远程服务器。<br>

🚨🚨🚨**首先提醒一点**：一定要选择阿里云自己创建的密钥队，自己上传的ssh-rsa之类算法的密钥队是不支持的，阿里云自己创建的是pem密钥对，点击创建密钥队后，私钥pem会自动在远程服务器中创建，公钥pem会自动下载到本地。<br>

操作方式如下：<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/8a92d92b-25dd-41b5-be21-53f9cf447cc0)

接下来需要将公钥pem放到指定位置，可以放到常规远程连接密钥存放的位置，也可以自定义位置。常规远程连接密钥存放的位置为：<br>
```bash
~/.ssh/
```

我们还需要修改公钥pem的权限，要为存放的公钥pem设置权限，否则会提示你 `权限过于开放，无法连接`。示例图如下：<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/b03d7adf-c32e-4c68-9d1e-133215542af0)

为存放的公钥pem设置权限很简单，根据自己存放公钥pem文件的路径，输入以下指令即可：<br>
> 笔者使用的是mac，如果你使用的是win，不保证下列指令正常使用。

```bash
chmod 600 /Users/peilongchencc/Desktop/personal_aliyun_keys/peilongchencc_mac_20230808.pem
```

修改config文件内容：
如果想快速修改config文件，可以使用以下指令：<br>
```bash
vim ~/.ssh/config
```
直接添加就行，不需要做额外的修改。可以参考下图：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/f03ea3a7-24ec-4f2c-9a27-63078c2daa9d" alt="image" width="70%" height="70%">

现在，无论你使用终端，还是使用vscode等IDE，都可以直接连接远程服务器了。～<br>

终端输入以下指令，会自动连接到远程服务器。<br>
```bash
ssh root@8.140.203.xxx
```

vscode更智能，直接按下图点击选项即可：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/d138d0f7-a974-4c2d-b895-b5aff9f121a3" alt="image" width="50%" height="50%">

<br>

### 将别人的SSH密钥添加到自己的Ubuntu 18.04服务器:

要将别人的SSH密钥添加到你的Ubuntu 18.04服务器中的`deployer`账户，你可以按照以下步骤操作：<br>

1. **获取密钥**：首先，确保你获得了对方的公共SSH密钥。这通常是一个`.pub`文件，例如`id_rsa.pub`。

2. **登录到服务器**：使用你的`deployer`账户登录到服务器。你可以使用SSH客户端来完成这一步，例如通过命令`ssh deployer@your_server_ip`。

3. **编辑authorized_keys文件**：

  - 切换到`deployer`用户的主目录（如果你已作为`deployer`登录，那么你应该已经在这个目录里，或者 `cd /home/deployer` 进入该目录）。
 
  - 查找(`ll -a`)一个名为`.ssh`的目录。如果没有，可以使用命令`mkdir -p ~/.ssh`来创建这个目录。
 
  - 在`.ssh`目录中，有一个名为`authorized_keys`的文件用于存储公钥。如果该文件不存在，你可以创建它。
 
  - 使用文本编辑器（如`vim`）打开`authorized_keys`文件。例如，`vim ~/.ssh/authorized_keys`。

4. **添加公钥**：将对方的公钥（从`.pub`文件中获得）复制并粘贴到`authorized_keys`文件中。每个密钥应该占一行。

5. **保存并关闭文件**：保存`authorized_keys`文件并关闭编辑器。

6. **设置权限**：

  - 如果其他人已经设置过权限，可以跳过这一步。

  - 确保`.ssh`目录的权限是700（只有所有者可以读写执行）。使用命令`chmod 700 ~/.ssh`。
 
  - 确保`authorized_keys`文件的权限是600（只有所有者可以读写）。使用命令`chmod 600 ~/.ssh/authorized_keys`。

7. **测试连接**：让对方尝试使用他们的SSH私钥连接到你的服务器，看是否成功。

完成这些步骤后，对方应该能够使用他们的SSH密钥登录到你的服务器上的`deployer`账户。<br>

## 使用阿里云提供的Redis时流量占用问题：

### 问题描述：

我的服务向阿里云提供的redis写入数据，和从阿里云提供的redis获取数据会占用流量吗？<br>

### 阿里云客服回应：

```log
您好：

请问，我的服务向阿里云提供的redis写入数据，和从阿里云提供的redis获取数据会占用流量吗？

----您可以理解为会占用带宽

Redis实例作为更靠近应用服务的数据层，通常会执行较多的数据存取并消耗网络带宽。不同的实例规格对应的最大带宽有所不同，当超过该规格的最大带宽时，将对应用服务的数据访问性能造成影响。

参考文档：

排查Redis实例流量使用率高的问题  https://help.aliyun.com/zh/redis/user-guide/troubleshoot-high-traffic-usage-on-an-apsaradb-for-redis-instance?spm=a2c4g.11174283.0.i10
```
<br>


## 阿里云的RAM用户登陆和普通用户登陆有区别吗？

阿里云（Alibaba Cloud）的RAM（Resource Access Management）用户登录和普通用户登录确实存在一些区别，这些区别主要体现在权限管理、访问控制和用途上：<br>

1. **用户类型**:

- **普通用户**: 通常指的是拥有阿里云账户的主用户，可以访问和管理阿里云的所有资源和服务，具有账户的最高权限。

- **RAM用户**: 是在主账户下创建的子账户，通常用于对权限进行细粒度的控制。通过为RAM用户分配不同的权限，账户拥有者可以限制他们可以访问和管理的资源范围。

2. **登录方式**:

- **普通用户登录**: 通常通过阿里云主页面登录，使用注册时设置的邮箱或手机号和密码。

- **RAM用户登录**: 通常通过RAM用户的登录链接进行，该链接是由主账户用户提供的，RAM用户需要该特定的URL，以及他们的用户名和密码。

3. **权限管理**:

- **普通用户**: 拥有对账户下所有资源的完全控制权，可以创建和管理RAM用户，分配权限等。
- **RAM用户**: 权限受限，只能进行被授权的操作，这有助于遵循最小权限原则，降低安全风险。

4. **用途**:

- **普通用户**: 适用于账户的主要拥有者和需要完全控制的管理员。

- **RAM用户**: 适合需要对不同员工或系统分配不同权限的情况，例如开发者、审计员或只需要访问特定服务的应用程序。

通过这种方式，阿里云用户可以更安全、更灵活地管理他们的资源和权限。在实际使用中，根据具体的业务需求和安全要求选择合适的用户类型和权限设置非常重要。<br>


## cannot create temp file for here-document: No space left on device

当你使用 `cd` 指令时，如果一直提示下列信息，表明你的服务器上的磁盘空间已经用完，无法创建临时文件来处理一个"here-document"。<br>

```bash
cannot create temp file for here-document: No space left on device
```

"here-document" 是一种用于在shell脚本中包含多行文本的方式。当服务器上的磁盘空间不足时，系统无法创建所需的临时文件，从而导致这个错误。<br>

🚨🚨🚨要解决这个问题，你可以采取以下步骤：<br>

**检查磁盘空间使用情况：**<br> 

首先，使用 `df -h` 命令来查看服务器上各个分区的磁盘空间使用情况。这将显示磁盘空间使用百分比以及可用空间。<br>

```bash
df -h
```

通过查看这些信息，确定哪个分区的空间已经耗尽。<br>

**清理不必要的文件：**<br>

如果你确定哪个分区空间不足，可以尝试删除不必要的文件或日志，以释放磁盘空间。使用 `rm` 命令来删除文件，或者 `find` 命令来查找和删除较旧或不需要的文件。<br>

例如，删除旧日志文件：<br>

```bash
rm /path/to/old/log/files/*.log
```

**查找大文件：**<br>

使用 `du` 和 `sort` 命令来查找占用磁盘空间较多的文件或目录。例如，以下命令将列出指定目录中最大的文件：<br>

```bash
du -h /path/to/directory | sort -rh | head -n 10
```

这将显示前10个最大的文件或目录。<br>

**清空临时文件：**<br> 

有时，服务器上的临时文件可能占用了大量磁盘空间，例如 `nohup.out` 文件。你可以使用 `rm` 命令来删除不再需要的临时文件。<br>

**增加磁盘空间：**<br> 

如果磁盘空间问题经常发生，可能需要考虑增加服务器的磁盘空间，或者将一些数据迁移到其他存储设备。<br>

**检查日志文件：**<br> 

如果你的服务器有日志记录问题，日志文件可能会快速增长，导致磁盘空间耗尽。检查并限制日志文件的大小，以避免此问题。<br>

🥹🥹🥹一旦你释放了足够的磁盘空间，你应该能够解决这个错误并正常执行你的任务。确保定期监视服务器的磁盘空间使用情况，以及时采取措施来防止空间不足的问题。笔者解决这个问题就是通过删除了一些占用空间巨大的文件夹。🫠🫠🫠🫠<br>
<br>

## Could not establish connection to "xxx.xxx.xxx.xxx": Cannot read properties of undefined (reading 'replace').

情况描述：使用终端连接远程服务器正常，但使用 vscode 连接远程服务器时，出现错误提示:

```txt
Could not establish connection to "xxx.xxx.xxx.xxx": Cannot read properties of undefined (reading 'replace').
```

解决方案：<br>

1. 点击 vscode 中的拓展模块；

2. 点击远程连接的插件，我使用的是 Remote Explorer；

3. 将 Remote 版本切换为 "预发布" 版本；("预览"-->"预发布")


## "项目部署在AWS的Lambda"是什么意思？

"项目部署在AWS的Lambda" 这句话是关于云计算服务的。这里的“项目”指的是某种软件应用或代码，而“部署”是指在某个平台上设置和运行这个应用或代码。<br>

AWS（Amazon Web Services）是亚马逊提供的一种云计算服务平台。Lambda是AWS提供的一种服务，允许你运行代码而不需要管理服务器。在Lambda上部署项目意味着你的代码会在AWS的云基础设施上运行，而无需担心底层服务器的维护和管理。<br>

使用AWS Lambda的优点包括：<br>

1. **无服务器架构**：你不需要管理或维护服务器，只需关注你的代码。

2. **按需定价**：你只需为代码执行时消耗的计算资源付费。

3. **自动扩展**：Lambda可以根据需要自动增加或减少计算资源，以适应应用程序的需求。

4. **事件驱动**：Lambda可以配置为响应AWS内的各种事件，如文件上传到S3、更新数据库等。

总之，这是一种现代的、高效的方式来运行和扩展应用程序，特别适合那些希望减少基础设施管理负担的开发者或企业。<br>
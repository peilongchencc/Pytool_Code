# Linux Command
Linux指令都是通过终端或shell脚本操作的，所以下文笔者不会备注在哪里操作。<br>
Ps:本文所有指令为 Linux 版本，Windows 或 MacOS 指令请自行从网络寻找。<br>
- [Linux Command](#linux-command)
  - [Linux 中的重要目录：](#linux-中的重要目录)
  - [权限指令：](#权限指令)
    - [sudo su - 和 su root 指令的区别是什么？](#sudo-su---和-su-root-指令的区别是什么)
    - [查看环境变量：](#查看环境变量)
    - [Linux系统环境变量常见位置：](#linux系统环境变量常见位置)
    - [shell解释器查看与类型更改：](#shell解释器查看与类型更改)
    - [linux更改文件夹下所有内容的权限，例如从root改为deployer用户：](#linux更改文件夹下所有内容的权限例如从root改为deployer用户)
  - [系统信息指令：](#系统信息指令)
    - [查看自己电脑的硬盘空间:](#查看自己电脑的硬盘空间)
  - [清理磁盘空间:](#清理磁盘空间)
    - [查看自己电脑的系统内存:](#查看自己电脑的系统内存)
  - [CPU 和 GPU 相关：](#cpu-和-gpu-相关)
    - [`nvcc -V` 是什么意思？和 `nvidia-smi` 有什么区别？](#nvcc--v-是什么意思和-nvidia-smi-有什么区别)
    - [同一台服务器下，为什么CUDA的版本不同，`nvidia-smi`显示的是`12.0`，`nvcc -V`显示的是`11.7`:](#同一台服务器下为什么cuda的版本不同nvidia-smi显示的是120nvcc--v显示的是117)
    - [如果安装pytorch，应该安装基于cuda 11.7的pytorch，还是安装基于cuda 12.0的pytorch？](#如果安装pytorch应该安装基于cuda-117的pytorch还是安装基于cuda-120的pytorch)
  - [服务相关：](#服务相关)
    - [nohup指令启动服务：](#nohup指令启动服务)
  - [常规文件操作：](#常规文件操作)
    - [find 和 grep--查找特定目录下是否有某个文件或某个文件中是否包含特定内容:](#find-和-grep--查找特定目录下是否有某个文件或某个文件中是否包含特定内容)
    - [查看当前目录下的文件个数：](#查看当前目录下的文件个数)
  - [创建、移动、查看、清空、复制、删除文件/文件夹：](#创建移动查看清空复制删除文件文件夹)
    - [查看文件内容：](#查看文件内容)
    - [清空一个文件中的内容：](#清空一个文件中的内容)
    - [清空文件夹下所有内容(不删除文件):](#清空文件夹下所有内容不删除文件)
  - [压缩文件、解压文件：](#压缩文件解压文件)
  - [文件或文件夹的上传与下载：](#文件或文件夹的上传与下载)
  - [目录树生成：](#目录树生成)
    - [使用 find 指令生成目录树：](#使用-find-指令生成目录树)
      - [基于当前目录所有文件生成目录树：](#基于当前目录所有文件生成目录树)
      - [设置树的深度：](#设置树的深度)
      - [设置只生成基于文件夹的目录树：](#设置只生成基于文件夹的目录树)
      - [解释：生成的目录树中 .DS\_Store 是什么？](#解释生成的目录树中-ds_store-是什么)
        - [设置树的深度为2，不输出 mac 的 ".DS\_Store" 文件:](#设置树的深度为2不输出-mac-的-ds_store-文件)
      - [将终端显示的目录树内容输出到 txt 文件中:](#将终端显示的目录树内容输出到-txt-文件中)
    - [使用 tree 指令生成目录树：](#使用-tree-指令生成目录树)
      - [安装 tree 库:](#安装-tree-库)
      - [基于当前目录所有文件生成目录树：](#基于当前目录所有文件生成目录树-1)
      - [将输出保存到一个文本文件中（例如，"tree.txt"）：](#将输出保存到一个文本文件中例如treetxt)
      - [设置屏蔽项:](#设置屏蔽项)
      - [同时屏蔽文件夹和文件：](#同时屏蔽文件夹和文件)
    - [find+tree，限制树的深度，同时屏蔽某些文件或文件夹：](#findtree限制树的深度同时屏蔽某些文件或文件夹)
  - [ubuntu系统如何设置root级别的别名--例如 alias cls='clear'](#ubuntu系统如何设置root级别的别名--例如-alias-clsclear)

## Linux 中的重要目录：

主目录：<br>

```bash
/root
/home/username
```

用户可执行文件：<br>

```bash
/bin
/usr/bin
/usr/local/bin
```

系统可执行文件：<br>

```bash
/sbin
/usr/sbin
/usr/local/sbin
```

其他挂载点：<br>

```bash
/media
/mnt
```

配置：<br>

```bash
/etc
```

临时文件：<br>

```bash
/tmp
```

内核和Bootloader：

```bash
/boot
```

服务器数据：<br>

```bash
/var
/srv
```

系统信息：<br>

```bash
/proc
/sys
```

共享库：<br>

```bash
/lib
/usr/lib
/usr/local/lib
```

## 权限指令：

查看自己是何种类型的用户，root或普通用户：<br>

```bash
whoami
```

如果返回 `root` 就代表你是 `root` 用户，如果返回的是其他内容，代表你不是 `root` 用户。<br>

或者可以单纯从终端行首的命令符号 `$` 和 `#` 区分：<br>

普通用户显示的就是 `$`；<br>

root用户显示的就是  `#`；<br>

普通用户切换为 `root` 用户<br>

```shell
sudo su -
```

如果没有设置密码，会直接切换到 `root` 用户，拥有 `root` 权限。如果设置了密码，此时会提示你输入**当前用户的密码**‼️‼️，正常输入即可。注意⚠️：密码是不显示状态的，没法直接看到的。键盘正常输入密码，然后回车即可。<br>
<br>

### sudo su - 和 su root 指令的区别是什么？

`sudo su -` 和 `su root` 都是用于在 Linux 系统上以超级用户（root）身份运行命令或进入 root 用户的shell环境的命令，但它们之间有一些重要的区别：<br>

1. `sudo su -`：
   - `sudo` 是一个命令，用于以其他用户的身份执行命令，通常是以超级用户（root）的身份执行。
   - `su -` 是一个子命令，用于切换到另一个用户的身份，并且 `-` 选项表示切换后将使用目标用户的环境变量。
   - `sudo su -` 结合了两个命令，首先使用 `sudo` 以 root 用户的权限执行 `su -` 命令，因此您需要输入当前用户的密码来确认权限。
   - 使用 `sudo su -` 可以在不知道 root 用户密码的情况下以 root 用户身份执行命令，只需输入当前用户的密码。

2. `su root`：
   - `su` 是一个命令，用于切换用户的身份。
   - `su root` 表示要切换到 root 用户的身份。在执行此命令之前，您需要知道 root 用户的密码，并输入它来进行切换。
   - 使用 `su root` 后，您将完全进入 root 用户的环境，包括工作目录和环境变量。

总结：
- `sudo su -` 适用于在不知道 root 用户密码的情况下以 root 用户的权限执行命令，并且使用当前用户的密码来进行授权验证。
- `su root` 适用于已知 root 用户密码的情况下切换到 root 用户的身份，需要输入 root 用户的密码来进行验证。

注意：当前用户密码和root用户的密码是两码事。<br>

请谨慎使用这些命令，因为以 root 用户的身份运行命令具有潜在的危险性，可以对系统造成损害。只有在必要的情况下才应该使用 root 权限。<br>

### 查看环境变量：

查看当前用户环境变量：<br>

```bash
echo $PATH
```

查看当前用户的JAVA_HOME路径：<br>

```bash
echo $JAVA_HOME
```

如果已经设置了JAVA_HOME环境变量，这个命令会显示JAVA_HOME的值。如果它为空、环境变量文件中注释或未定义，将不会显示任何输出。<br>

### Linux系统环境变量常见位置：

```bash
~/.bashrc
~/.zshrc
~/.profile
/etc/environment
```

或者有可能是`/etc/profile.d`下的任意文件(develop.sh文件是我瞎写的🫠)：<br>

```bash
/etc/profile.d/develop.sh
```

### shell解释器查看与类型更改：

查看当前终端正在使用的 shell 解释器类型：<br>

```bash
echo $SHELL
```

查看所有可用的 shell 列表：<br>

```bash
cat /etc/shells
```

切换到另一个 shell 解释器，假设我现在正处于 zsh 解释器，使用以下指令可切换到 bash 解释器：<br>

```bash
chsh -s /bin/bash
```

修改后，如果不放心，可以检查`/etc/passwd`文件：<br>

```bash
cat /etc/passwd
```

你可以手动检查`/etc/passwd`文件中的用户条目，确保已更改默认shell。打开/etc/passwd文件，找到包含你用户名的行，然后检查shell字段是否已更改为/bin/bash。<br>

**shell 和 bash 的关系**：<br>

shell 指的是一类程序，能按照用户要求去调用操作系统接口的程序。linux发展至今,有许多shell程序(例如：sh、ksh、bash、zsh)，bash是其中之一。<br>
<br>

获取系统所有库最新信息：<br>

用于让系统获取所有库的最新信息，不会更改任何安装库的版本。<br>

```bash
sudo apt update
```

### linux更改文件夹下所有内容的权限，例如从root改为deployer用户：

更改前，终端运行`ll`指令效果如下：<br>

```log
-rw-r--r--  1 root     root          538 Oct 11 22:42  set_metadata_py_from_redis.py
-rw-r--r--  1 root     root          979 Oct 11 22:42  set_metadata_py_to_redis.py
```

此时，如果你是其他用户(例如deployer)，你无法写入内容，如果你想要实现写入，**假设要更改一个文件夹下所有内容的权限，包括子文件夹和文件**，以将其所有权从root用户更改为deployer用户，你可以使用`chown`命令。在终端中执行以下命令：<br>

```bash
sudo chown -R deployer:deployer /path/to/your/folder
```

在这个命令中：<br>

- `sudo`用于以超级用户权限执行命令，因为更改文件夹权限通常需要管理员权限。
- `chown`是更改文件夹或文件所有权的命令。
- `-R`选项表示递归地更改所有子文件夹和文件的权限。
- `deployer:deployer`表示要将所有权更改为deployer用户和deployer用户组。您可以根据需要更改为其他用户和用户组。

最后，将`/path/to/your/folder`替换为你要更改权限的实际文件夹路径。执行此命令后，文件夹下的所有内容都将更改为deployer用户的所有权。<br>

此时，终端输入`ll`的效果如下：<br>

```log
-rw-r--r--  1 deployer deployer      538 Oct 11 22:42  set_metadata_py_from_redis.py
-rw-r--r--  1 deployer deployer      979 Oct 11 22:42  set_metadata_py_to_redis.py
```

🚨🚨🚨请小心使用`chown`命令，确保你知道你在做什么，以免意外更改了文件和文件夹的权限。<br>

💦💦💦如果你只想更改一个特定文件的权限，而不是整个文件夹，你可以使用`chown`命令，并指定要更改权限的文件的路径。以下是如何执行此操作的示例：<br>

```bash
sudo chown deployer:deployer /path/to/your/file
```

在这个示例中，我使用了`chown`命令来将文件的所有权更改为deployer用户和deployer用户组。请确保将`/path/to/your/file`替换为你要更改权限的实际文件的路径。<br>

🚨🚨🚨同样，请谨慎使用`chown`命令，确保你知道你在做什么，以免不小心更改了文件的权限。<br>


## 系统信息指令：
Linux查看自己是什么系统的方式：<br>
```shell
cat /etc/os-release
```

Linux系统查看操作系统的位数是x86还是x64的方式：<br>

```shell
getconf LONG_BIT
```
<br>

### 查看自己电脑的硬盘空间:

```bash
df -h
```

终端显示:<br>

```log
Filesystem      Size  Used Avail Use% Mounted on
udev            7.7G     0  7.7G   0% /dev
tmpfs           1.6G  5.6M  1.6G   1% /run
/dev/vda1        40G   36G  1.5G  97% /
tmpfs           7.8G   60K  7.8G   1% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           7.8G     0  7.8G   0% /sys/fs/cgroup
/dev/vdb1        40G  876M   37G   3% /data
tmpfs           1.6G     0  1.6G   0% /run/user/0
overlay          40G   36G  1.5G  97% /var/lib/docker/overlay2/ff77fb7b64682ad3a6dd83f7cf7634ee815f66078bc1cc1f4ebe185fa6fdf12a/merged
shm              64M     0   64M   0% /var/lib/docker/containers/7f3d70a2ab7f4e58e6609732c73146dd7b324449b7ff0d13032e64af95fccf81/mounts/shm
overlay          40G   36G  1.5G  97% /var/lib/docker/overlay2/36be850d4ad711091fab1e30784376e610d63cad4587cb16609b7d50d9584fce/merged
shm              64M     0   64M   0% /var/lib/docker/containers/1fe5aacddf2124aa0c1d769207856c960e5791b346e1957971492658eeb5c773/mounts/shm
overlay          40G   36G  1.5G  97% /var/lib/docker/overlay2/eaf422348a6447ce175405d30c1128e3259faea4b015a6a4a41b9083d4c05391/merged
shm              64M     0   64M   0% /var/lib/docker/containers/a4959f4ba78158d1a8564a882b6c9440547d46aad6c16c8b37afd4dcdf715088/mounts/shm
```

- `/dev/vda1`是"根分区"，这个分区挂载在文件系统的根目录`/`上。

- `/dev/vdb1`是我挂载的云盘。

- `overlay`是Docker使用的存储驱动程序之一，Docker的默认存储位置是在`/var/lib/docker`，而这个目录位于`/dev/vda1`上，即挂载在文件系统的根目录`/`上。这有可能会导致硬盘空间不足，以笔者举例，笔者为避免由于空间问题导致Docker无法启动/运行，将Docker(Milvus相关)的数据文件移到了挂载的云盘(`/data`)上了。


## 清理磁盘空间:

在使用阿里云服务器时，经常遇到的一个问题为 "磁盘空间不足"，"磁盘空间不足"会导致mysql停止运行，各种程序无法启动。所以知道如何清理磁盘空间非常重要。<br>

输入以下指令查看 `/` 根目录下磁盘空间占用情况:<br>

```bash
sudo du -ah / | sort -rh | head -n 20
```

这个命令会列出 `/` 目录下最大的20个文件和目录。`du` 命令用于计算文件大小，`sort` 命令用于排序，`head` 命令用于只显示列表的前20项。<br>

终端效果如下:<br>

```txt
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/Pytool_Code# du -ah / | sort -rh | head -n 20
du: cannot access '/proc/29422/task/29825': No such file or directory
du: cannot access '/proc/29827/task/29827/fd/4': No such file or directory
du: cannot access '/proc/29827/task/29827/fdinfo/4': No such file or directory
du: cannot access '/proc/29827/fd/3': No such file or directory
du: cannot access '/proc/29827/fdinfo/3': No such file or directory
du: cannot access '/proc/29875': No such file or directory
du: cannot access '/proc/29876': No such file or directory
du: cannot access '/proc/29882': No such file or directory
du: cannot access '/proc/29887': No such file or directory
du: cannot access '/proc/29888': No such file or directory
du: cannot access '/proc/29893': No such file or directory
37G     /
18G     /root
12G     /root/anaconda3
8.4G    /data
5.7G    /var
5.4G    /var/lib
4.5G    /root/anaconda3/lib
4.5G    /root/anaconda3/envs/nudge_new/lib/python3.10/site-packages
4.5G    /root/anaconda3/envs/nudge_new/lib/python3.10
4.5G    /root/anaconda3/envs/nudge_new/lib
4.5G    /root/anaconda3/envs/nudge_new
4.5G    /root/anaconda3/envs
4.4G    /data/milvus_data
4.3G    /data/milvus_data/rdb_data
3.4G    /root/.cache
3.3G    /root/.cache/pip/http
3.3G    /root/.cache/pip
2.9G    /usr
2.7G    /var/lib/docker
2.6G    /root/anaconda3/envs/nudge_new/lib/python3.10/site-packages/nvidia
```

此时根据路径情况删除对应的内容即可，如果不是很清楚某个路径下占用空间较大的文件是那个，可以修改路径再次运行上述指令。<br>

```bash
sudo du -ah /var/lib | sort -rh | head -n 20
```

这个命令会列出 `/var/lib` 目录下最大的20个文件和目录。<br>


### 查看自己电脑的系统内存:

```shell
free -h
```
如果想要动态查看系统内存，只能反复运行 `free -h`，这一点是比较尴尬的。当然你也可以运行 `top` 或 `htop` 指令，实时地显示系统的各种性能指标，包括内存使用情况。但我觉得 `top` 或 `htop` 指令在查看内存方面不好用。<br>

`top` 是一个常用的命令行工具，用于实时监视系统的性能指标，包括 CPU 使用率、内存使用率、进程状态等。当你运行 `top` 命令时，它会以交互式的方式显示当前系统的各种信息，并会不断更新这些信息，让你能够实时监视系统的状态。<br>

以下是一些在 top 界面中可能看到的主要信息：<br>

**顶部信息栏**: 显示系统的总体性能摘要，包括当前时间、系统运行时间、登录用户数量、负载平均值等。<br>

**任务信息区域**: 显示了关于每个运行进程的信息，如进程 ID、CPU 使用率、内存使用量、状态等。你可以看到哪些进程正在使用最多的资源。<br>

**全局操作栏**: 这是你可以执行的命令列表，例如刷新、杀死进程等。<br>

在 `top`` 的界面中，你可以使用一些按键来进行交互，如：<br>

**空格键**: 刷新 `top` 显示，更新信息。<br>
**数字键 1**: 切换到全局视图，显示每个 CPU 核心的使用情况。<br>
**数字键 M**: 切换到按内存排序的视图，显示最消耗内存的进程。<br>
**数字键 P**: 按 CPU 使用率对进程进行排序。<br>
**数字键 T**: 按时间排序，以查看最新的进程。<br>
要退出 `top`，可以按下 `q` 键。<br>

`top` 是一个强大的工具，可以帮助你实时地监视系统性能，了解哪些进程在消耗资源，以及系统的负载情况。它对于诊断性能问题和资源管理非常有用。


## CPU 和 GPU 相关：
查看cpu详细信息：
```shell
lscpu 
```
执行该命令后，会显示有关CPU的详细信息，包括内存核数。你可以查找"CPU(s)"或"Core(s) per socket"字段来获取内存核数的信息。

也可直接通过如下指令查看cpu核数：
```shell
nproc
```
<br>

如果你想要做深度学习任务，想查看GPU使用情况，动态查看(0.5秒刷新一次)nvidia-smi使用情况指令为：<br>

```shell
watch -n .5 nvidia-smi
```

如果想要2秒刷新一次，简单修改指令即可：<br>

```shell
watch -n 2 nvidia-smi
```

查看GPU详细信息：<br>

```shell
nvidia-smi -a
```

查看CUDA编译器版本:<br>

```bash
nvcc -V
```

### `nvcc -V` 是什么意思？和 `nvidia-smi` 有什么区别？

`nvcc -V` 和 `nvidia-smi` 是两个与NVIDIA CUDA Toolkit相关的不同命令，它们的作用和输出信息有显著区别。<br>

1. **`nvcc -V`**:
    - `nvcc` 是 NVIDIA CUDA Compiler(编译) 的简称，它是 CUDA Toolkit 的一部分，用于编译 CUDA 代码。
    - 执行 `nvcc -V` 命令会显示 `nvcc` 编译器的版本信息，这对于开发者来说很重要，因为不同版本的 CUDA Toolkit 支持不同版本的 CUDA 和 GPU 架构。
    - 该命令的输出信息主要包括 `nvcc` 的版本号，以及它依赖的一些组件的版本信息，比如 C++ 编译器的版本。

2. **`nvidia-smi`**:
    - `nvidia-smi` 是 NVIDIA System Management Interface 的简称，它是一个命令行工具，用于查询和监控 NVIDIA GPU 设备的状态。
    - 执行 `nvidia-smi` 命令会显示当前系统中 NVIDIA GPU 的详细信息，包括 GPU 型号、总显存、已使用显存、GPU 使用率、GPU 温度等。
    - `nvidia-smi` 是一个面向系统管理和监控的工具，它可以显示当前系统中所有 NVIDIA GPU 的状态和配置信息，对于系统管理员和进行性能调优的开发者来说非常有用。

总结来说，`nvcc -V` 用于显示 CUDA 编译器的版本信息，主要关注于 CUDA 开发环境；而 `nvidia-smi` 用于显示系统中 NVIDIA GPU 的状态和监控信息，更多地关注于硬件和系统层面的信息。两者都是 NVIDIA CUDA Toolkit 的重要组成部分，但服务于不同的目的和用户群体。<br>

### 同一台服务器下，为什么CUDA的版本不同，`nvidia-smi`显示的是`12.0`，`nvcc -V`显示的是`11.7`:

```txt
(base) root@5f7d2xxx:~# nvidia-smi
Thu Feb 29 17:46:45 2024       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.60.11    Driver Version: 525.60.11    CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA A100-PCI...  On   | 00000000:00:07.0 Off |                    0 |
| N/A   29C    P0    34W / 250W |      0MiB / 40960MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA A100-PCI...  On   | 00000000:00:08.0 Off |                    0 |
| N/A   27C    P0    31W / 250W |      0MiB / 40960MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
|   2  NVIDIA A100-PCI...  On   | 00000000:00:09.0 Off |                  Off |
| N/A   28C    P0    32W / 250W |      0MiB / 40960MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
|   3  NVIDIA A100-PCI...  On   | 00000000:00:0A.0 Off |                    0 |
| N/A   28C    P0    34W / 250W |      0MiB / 40960MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+

(base) root@5f7d2xxx:~# nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Tue_May__3_18:49:52_PDT_2022
Cuda compilation tools, release 11.7, V11.7.64
Build cuda_11.7.r11.7/compiler.31294372_0
```

这种现象是正常的，原因在于`nvidia-smi`和`nvcc`显示的版本信息指的是不同的东西。<br>

1. **`nvidia-smi`显示的CUDA版本**是指你的**NVIDIA驱动**当前支持的最新CUDA版本。这意味着你的系统驱动能够支持运行编译为该CUDA版本（或更低版本）的应用程序。在你提供的信息中，`nvidia-smi`显示支持的CUDA版本是12.0。

2. **`nvcc -V`显示的CUDA版本**是指你安装的**CUDA Toolkit**的版本。`nvcc`（NVIDIA CUDA Compiler）是CUDA Toolkit的一部分，用于编译CUDA程序。在你的情况下，安装的CUDA Toolkit版本是11.7。

这种差异意味着虽然你的系统驱动支持最新的CUDA 12.0应用程序，但你安装的CUDA Toolkit是11.7版本，所以你只能编译和运行最高为CUDA 11.7版本的应用程序。如果你需要开发或运行基于CUDA 12.0的应用程序，你需要安装匹配该版本的CUDA Toolkit。<br>

简而言之，`nvidia-smi`显示了你的GPU驱动能支持的CUDA最高版本，而`nvcc`显示的是实际安装的CUDA Toolkit版本。这两者不需要完全匹配，但开发者通常会根据需要更新CUDA Toolkit以利用新版本CUDA的新特性或改进。<br>

### 如果安装pytorch，应该安装基于cuda 11.7的pytorch，还是安装基于cuda 12.0的pytorch？

选择安装基于CUDA 11.7还是CUDA 12.0版本的PyTorch，主要取决于两个因素：你已安装的CUDA Toolkit版本和你打算使用的功能或特性。根据你提供的信息，你的系统中安装了CUDA Toolkit 11.7。这里有几点考虑：<br>

1. **与已安装的CUDA Toolkit兼容**：理想情况下，你应该安装一个与你当前安装的CUDA Toolkit版本兼容的PyTorch版本。这样可以确保你能够使用CUDA加速功能，而不会遇到版本不兼容的问题。因此，基于CUDA 11.7的PyTorch版本是首选。

2. **利用NVIDIA驱动的支持**：由于`nvidia-smi`显示你的系统支持CUDA 12.0，这意味着你的NVIDIA驱动能够运行基于CUDA 12.0的应用程序。如果你打算使用PyTorch的一些最新功能，这些可能只在基于CUDA 12.0的版本中可用，那么安装基于CUDA 12.0的PyTorch可以是一个选项。然而，为了这样做，你可能需要升级你的CUDA Toolkit到12.0，以确保开发和运行环境的一致性。

3. **考虑其他依赖**：如果你的项目或其他库有特定的CUDA版本要求，这也可能影响你的选择。

总之，如果你不打算升级CUDA Toolkit，或者没有特定需求需要CUDA 12.0的特性，基于CUDA 11.7的PyTorch版本是更安全、更兼容的选择。这将确保你的开发环境稳定，且能够利用CUDA加速功(例如 **DeepSpeed** )能而不会遇到兼容性问题。<br>

如果你决定需要基于CUDA 12.0的功能，那么考虑升级CUDA Toolkit到12.0，并安装相应的PyTorch版本。这可能需要更多的配置工作，但可以让你利用最新的CUDA特性。<br>


## 服务相关：

终端查看系统时间：<br>

> CST表示上海时间，也就是国际规定的东八区时间。

```bash
date
```

按照 `"年-月-日 时:分:秒"` 显示系统时间:

```bash
date "+%Y-%m-%d %H:%M:%S"
```

在Linux系统中，可以使用以下命令来查看端口的占用情况：<br>

1. 使用 netstat 命令：

```bash
netstat -ntlp 
```

这将显示当前正在监听的所有TCP和UDP端口以及它们的占用情况。TCP端口以 "tcp" 标识，UDP端口以 "udp" 标识。<br>

Centos系统需要先安装net-tools:<br>

```bash
yum install net-tools
```

然后运行以下指令:<br>

```bash
netstat -tuln # Centos系统使用
```

2. 使用 lsof 命令：

```bash
lsof -i :端口号
```

例如查看端口号 `7711` 的占用情况：<br>

```bash
lsof -i :7711
```

如果端口号 `7711`没有被占用，不会返回任何信息，如果被占用，会返回如下对应进程的pid和应用程序的详细信息。<br>

```log
COMMAND   PID     USER   FD   TYPE    DEVICE SIZE/OFF NODE NAME
python  46386 deployer   47u  IPv4 142357123      0t0  TCP *:7711 (LISTEN)
```

3. 关闭端口：

根据上面获取的pid，kill掉已经对应的进程。注意⚠️：一定要看清进程pid，不要误杀了其他人的进程‼️‼️<br>

```bash
kill -9 pid
```

如果是关闭我上方的例子，就运行下列指令：<br>

```bash
kill -9 46386
```

### nohup指令启动服务：

nohup是一个在Unix和类Unix系统（比如Linux）中使用的命令行工具，用于运行命令，使其在终端被关闭或用户注销后仍然继续运行。<br>

通常，当你在终端中运行一个命令或程序，并且关闭终端窗口或者断开SSH连接时，该命令或程序会收到一个SIGHUP（hangup）信号，导致其终止。<br>

🚀🚀🚀nohup命令可以阻止这种情况，允许命令在后台继续执行，即使终端会话已经结束。<br>

例如，如果你想在后台运行一个叫做`my_script.sh`的脚本，并且即使关闭终端也要让它继续运行，你可以使用以下命令：<br>

```bash
nohup ./my_script.sh &
```

这里的`&`将命令放到后台执行。nohup会将输出重定向到一个名为nohup.out的文件，除非另行指定。<br>

正常情况下终端输入`nohup ./my_script.sh &`指令后，会停在当前命令行，需要按Enter才能进入下一个命令行。<br>

> 停在当前命令行时，直接Enter按就行，不用担心，对nohup启用的程序无影响。

🫠🫠🫠如果你运行nohup指令失效，大概率是你的权限不够，可以切换至root权限运行，或者向系统管理员申请更高级别权限。<br>


如果你想把输出重定向到一个特定的文件，你可以这样做：<br>

```bash
nohup ./my_script.sh > output.log 2>&1 &
```

这条命令将标准输出和错误输出都重定向到output.log文件。<br>


## 常规文件操作：

### find 和 grep--查找特定目录下是否有某个文件或某个文件中是否包含特定内容:

假设你想要在 `/` 根目录下按名称查找 `files.zip` 文件:<br>

```shell
find / -name files.zip
```

假设你只记得文件名的部分内容，可以采用模糊查找：<br>

```shell
find / -name "*文件名"： 
```

`find`命令用于查找文件， `grep` 命令用于从文件本身中查找，以 `grep -r "jdk1.8.0_221" /etc` 命令为例：<br>

这个命令用于搜索指定目录下的文件，查找包含特定文本字符串的行。让我详细解释这个命令的各个部分：<br>

1. `grep`: `grep`是一个文本搜索工具，用于在文件中查找指定的文本模式，并将匹配的行打印到标准输出。

2. `-r`: 这是`grep`命令的一个选项，代表"递归"。使用`-r`选项后，`grep`将在指定的目录及其子目录中递归搜索文件，而不仅仅是在指定目录中搜索。

3. `"jdk1.8.0_221"`: 这是你要搜索的文本模式或字符串。在这个例子中，`grep`将会搜索所有包含文本字符串"jdk1.8.0_221"的行。

4. `/etc`: 这是搜索的起始目录，也就是`grep`将在其中搜索文件的根目录。在这种情况下，`grep`将在`/etc`目录及其所有子目录中搜索包含指定文本的行。

总结起来，这个命令的作用是在Linux或Unix系统上递归地搜索`/etc`目录及其子目录中的所有文件，查找包含字符串"jdk1.8.0_221"的行，并将这些行打印到标准输出。这通常用于查找配置文件或日志文件中的特定信息，以便进行故障排除或系统维护。<br>

😀😀😀可以记住这种查找方式，当你找不到某些配置文件时，这个命令非常有用。<br>

如果你要查找的路径下，有一些目录你想要排除，可以参考以下指令：<br>

```bash
grep -r "jdk1.8.0_221" --exclude-dir=/home/deployer/Project/ --exclude-dir=/home/deployer/TestProject/ --exclude-dir=/home/deployer/peilongchencc /home/deployer/ 
```

查看当前所在的目录：<br>
```shell
pwd
```

切换路径使用 `cd` 指令，假设要切换到根目录：<br>
```shell
cd /
```

返回上一级目录：<br>
```shell
cd ..
```
此指令可重复使用，例如返回上、上级目录：<br>
```shell
cd ../..
```
当然，重复套用太多自己都不知道自己在哪里了，更好的方式是 `cd` 到指定路径。<br>
<br>

查看文件：<br>
```shell
ll
```
或<br>
```shell
ls
```

查看文件，可以看到隐藏文件： <br>
```shell
ll -ah
```
<br>

查找文件夹下文件个数：<br>

```shell
ls -l <文件夹路径>|grep "^-"|wc -l
```

### 查看当前目录下的文件个数：

```shell
ls -l | grep "^-" | wc -l
```

或者使用`find`指令查看文件个数：<br>

```shell
find <文件夹路径> -type f | wc -l
```

假设想查看当前目录下的文件个数：<br>

```shell
find ./ -type f | wc -l
```


## 创建、移动、查看、清空、复制、删除文件/文件夹：

创建文件夹：<br>

```shell
mkdir example

```

这将在当前路径下创建一个名为 `example` 的文件夹。<br>

创建文件：<br>

创建文件的方式非常多，可以用各种编辑器实现，例如 `nano`、`vim`，这里介绍2种：<br>

采用 `touch` 的方式：<br>

```shell
touch example.txt
```

采用 `vim` 的方式：<br>

```shell
vim example.txt
```

注意⚠️：`touch` 方式创建文件后不会直接进入文件内部，`vim` 创建文件后会自动打开文件，进入文件内部。使用 `vim` 创建文件很方便，但前提是你需要熟悉 `vim` 的语法。<br>

如果你不够熟悉 `vim` 的语法，可以先用 `echo` ，`echo`结合`>`可以通过终端将内容写入文件:<br>

```shell
echo "想要写入的内容" > example.txt
```

上述指令会将内容 "覆盖" 写入到对应的文件中，文件之前的内容不复存在，只有新写入的内容。如果想要采用 "追加" 的形式写入内容，需要使用以下指令：<br>

```shell
echo "想要写入的内容" >> example.txt
```

### 查看文件内容：

写入内容后，想要查看文件中的内容，通过以下指令：<br>

```shell
cat example.txt
```

如果想要查看某个文件的最后20行内容，你可以使用一些不同的命令。以下是两种常见的方法：<br>

1. 使用`tail`命令：

`tail`命令用于显示文件的末尾内容。要查看某个文件的最后20行，可以使用以下命令：<br>

```bash
tail -n 20 文件名
```

例如，如果要查看文件名为`example.txt`的文件的最后20行，可以运行：<br>

```bash
tail -n 20 example.txt
```

2. 使用`cat`和`tail`命令的组合：

你还可以使用`cat`命令将文件的内容输出到标准输出，然后使用`tail`命令查看最后20行。以下是示例命令：<br>

```bash
cat 文件名 | tail -n 20
```

例如，要查看`example.txt`文件的最后20行，可以运行：<br>

```bash
cat example.txt | tail -n 20
```

这两种方法都可以让你查看文件的最后20行内容。选择其中一种方法根据你的个人偏好和需求。<br>

### 清空一个文件中的内容：

> 文件的内容将被清空，但文件本身仍然存在。

在Linux中，如果要清空名为example.txt的文件的内容，可以运行以下命令：<br>

```bash
> example.txt
```

这将清空 `example.txt` 文件中的内容，也可以按照路径的方式去清理对应路径下的某个文件。<br>
<br>

### 清空文件夹下所有内容(不删除文件):

`/var/log/`路径下常记录各种日志文件，如果长时间不清理会占用大量硬盘空间，应该如何将`/var/log/`路径下的文件都清空，而不删除/var/log/路径下的文件呢？<br>

如果你想要清空 `/var/log/` 路径下的文件内容而不删除文件本身，你可以使用 `truncate` 命令。以下是如何为 `/var/log/` 下的每个文件执行此操作：<br>

```bash
sudo find /var/log/ -type f -exec truncate -s 0 {} \;
```

这个命令的工作原理如下：<br>

- `find /var/log/ -type f`：在 `/var/log/` 目录中查找所有的文件（不包括子目录）。

- `-exec truncate -s 0 {} \;`：对于每个找到的文件 (`{}`)，使用 `truncate` 命令将其大小设置为 0，从而清空文件内容。

此命令将清空 `/var/log/` 下所有文件的内容，但不会删除文件本身。 <br>

注意：在执行此操作之前，请确保你真的想清空这些日志文件，并且知道这样做的后果。<br>

<br>


终端运行自己的python程序时，如果python程序中有 `print` 或 `log` 项，可以通过以下指令将终端的输出写入`example.txt`文件：<br>

```bash
python main.py > example.txt
```

这种方式每次运行上述代码都会将 `example.txt` 清空，然后重新写入。如果想要采用追加的方式写入，可以采用以下指令：<br>

```bash
python main.py >> example.txt
```


移动文件：<br>

```shell
mv file.txt target_path
```

移动有相同格式的文件：<br>
```shell
mv xxx* target_path
```

文件夹或文件重命名(**等同于移动文件**)：<br> 
```shell
mv old_name new_name
```

移动文件夹：<br>
```shell
mv -f old/path new/path
```

复制文件夹：<br>
```shell
cp -r old/path new/path
```

复制文件：<br>
```shell
cp old_name.py new_name.py
```

复制文件夹下的🚨内容🚨到另一个文件夹下，注意文件夹本身不复制：<br>
```shell
cp -r /path/to/source/* /path/to/destination/
```
例如：<br>
```shell
cp -r ./dist/* ../IRM2022_WebServer/src/public 
```
<br>

🥶🥶🥶接下来讲解删除操作，Linux的删除操作不像Windows会先将内容存到回收站，Linux执行的是直接删除、无法撤销，使用需注意‼️‼️‼️<br>
删除文件：<br>
```shell
rm /xxx/file.py 
```

删除文件夹：<br>
```shell
rm -rf target_folder
```

批量删除类似文件：<br>
假设你在终端输入 `ll` 后，发现类似下列的文件有很多：<br>
```txt
-rw-r--r--  1 root     root         308 Jul  6 15:12 nlp.20230621.log
-rw-r--r--  1 root     root         423 Jul  6 15:12 nlp.20230622.log
-rw-r--r--  1 root     root         282 Jul  6 15:12 nlp.20230623.log
-rw-r--r--  1 root     root         423 Jul  6 15:12 nlp.20230624.log
-rw-r--r--  1 root     root         462 Jul  6 15:12 nlp.20230625.log
-rw-r--r--  1 root     root        3309 Jul  6 15:12 nlp.20230626.log
-rw-r--r--  1 root     root        5743 Jul  6 15:12 nlp.20230627.log
-rw-r--r--  1 root     root        4691 Jul  6 15:12 nlp.20230628.log
-rw-r--r--  1 root     root        1070 Jul  6 15:12 nlp.20230629.log
-rw-r--r--  1 root     root        3040 Jul  6 15:12 nlp.20230630.log
```
要批量删除类似的文件，可以使用命令行中的通配符来匹配文件名模式。<br>

在示例中，文件名具有相同的前缀"nlp."，后面跟着一个日期。如果希望删除所有以"nlp."开头的文件，可以使用如下命令：<br>
```shell
rm nlp.*
```
上述命令将删除当前目录下以"nlp."开头的所有文件。<br>


如果只想删除特定日期范围内的文件，可以使用更精确的通配符模式。例如，如果只想删除从2023年6月21日到2023年6月30日的文件，可以使用以下命令：<br>
```shell
rm nlp.2023062[1-9].log nlp.2023063[0-1].log
```
上述命令将删除匹配模式的文件，其中[1-9]表示匹配范围为1到9的数字，[0-1]表示匹配范围为0到1的数字。<br>

在执行删除命令之前，请确保已经仔细检查了文件名模式，以免意外删除了不希望删除的文件。<br>
<br>

项目文件夹下有多个文件或文件夹，🥴🥴🥴如何只保留其中某一个文件或文件夹，删除其他所有内容：<br>
假设只保留 `settings`` 文件夹，使用以下指令即可:<br>
```shell
rm -r !(settings)
```

假设要保留多个文件或文件夹，删除其他所有内容，可以参考以下指令：<br>
```bash
rm -r !(config|nlp_models|simple)
```
<br>


## 压缩文件、解压文件：
Linux安装 `zip` 和 `unzip` 模块的指令如下：<br>

```shell
sudo apt-get install zip
```

```shell
sudo apt-get install unzip
```

如果你不是`root`用户，可以使用以下指令切换到`root`用户:<br>

```bash
sudo su -
```

🚨🚨🚨如果你的系统设置了普通用户切换到`root`需要输入密码，会提示你输入密码，如果不需要输入密码，会直接切换到`root`用户。<br>

<br>

zip压缩指令：
```shell
zip -r -q -o 压缩后的文件名.zip 文件路径或当前目录下的文件名
```

zip格式文件的解压指令非常简单：<br>
```shell
unzip 文件名.zip
```
<br>

tar.gz压缩指令：<br>
```shell
tar -czvf archive.tar.gz folder_name
```

tar.gz解压指令：<br>
```shell
tar -xzvf archive.tar.gz -C /path/to/targert_directory # 解压到目标路径
```

## 文件或文件夹的上传与下载：
与远程服务器连接进行文件上传或文件下载操作可以使用 `scp` 或 `rz`、`sz`指令，windows用户也可以使用 xshell 软件。笔者经常使用的是 `scp` 指令，这里介绍 `scp` 的常见用法。<br>

使用 `scp` 将代码上传至服务器：<br>
```shell
scp -r -v ./local_folder root@8.140.203.xxx:/root/peilongchencc/
```
使用 `scp` 将代码从服务器下载到本地：<br>
```shell
scp -r -v root@8.140.203.xxx:/data/nlp/target.zip ./Desktop/
```
使用时注意将远程服务器的 `ip` 改为自己的服务器 `ip` 即可。`scp -r -v` 表示👏👏👏 "以显示进度条方式复制文件或文件夹到目标路径" 。<br>


如果想从互联网下载某些内容到Linux系统的某个位置，可以使用 `wget` 指令：<br>
> `curl`指令类似wget，用法相同，都是URL下载工具。

最基本形式为：<br>
```shell
wget <URL>
```
使用示例：<br>
```shell
wget http://url_information/xxx.zip
```

如果想要将下载的文件保存为特定的文件名，可以使用以下指令：<br>
```shell
wget -O <filename> <URL>
```

直接使用 `wget` 会下载到当前目录，这里不多讲 `wget` 的使用，`wget` 会有网速限制，有时需要尝试好几遍才能成功，笔者在工作中大多数采用的是手动从网络下载特定内容，然后上传至服务器。<br>

## 目录树生成：
当你在看某些项目时，可能会发现作者使用了以下方式向你展示了他项目中的文件结构，那这种文件结构要如何生成呢？<br>
```log
.
├── mypackage
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
└── main.py
```

首先明确一点，这种文件结构叫做目录树，`Ubuntu` 系统生成目录树的方式有两种，使用 `find` 和 `tree`指令。Mac 电脑也可以使用以下指令～<br>

### 使用 find 指令生成目录树：
使用 `find` 指令生成目录树较为复杂，且 **很难实现同时屏蔽多个文件夹和文件**，但 `find` 指令生成目录树的优势不可替代，那就是**可以限制树的深度**🚀🚀🚀(刚好和 `tree` 指令生成目录树指令互补)，使用方式如下：<br>

#### 基于当前目录所有文件生成目录树：
```shell
find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'
```

#### 设置树的深度：
当前文件夹下的内容为 `maxdepth 1`，下一级为 `maxdepth 2`，以此类推；<br>
```shell
find . -maxdepth 2 -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'
```

#### 设置只生成基于文件夹的目录树：
`-type d`参数用于仅匹配目录（文件夹）而不包括文件。<br>
```shell
find . -maxdepth 2 -type d -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'
```

#### 解释：生成的目录树中 .DS_Store 是什么？
.DS_Store 是 macOS 操作系统在每个文件夹中自动生成的隐藏文件。它包含有关文件夹的自定义属性和元数据，例如文件夹的图标位置、窗口大小和视图选项等。.DS_Store 文件的目的是在图形用户界面（GUI）中维护文件夹的外观和显示设置。<br>

通常情况下，.DS_Store 文件对于文件夹的功能并不重要，而且在大多数情况下，它是隐藏的，不会干扰正常的文件操作。但是，在生成目录树时，.DS_Store 文件会显示在输出中，可能会干扰您查看纯粹的目录结构。<br>

如果你希望在生成目录树时排除.DS_Store 文件，你可以修改命令以过滤掉这些文件。以下是一个示例命令：<br>

##### 设置树的深度为2，不输出 mac 的 ".DS_Store" 文件:
```shell
find . -maxdepth 2 -not -name ".DS_Store" -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'
```
在这个命令中，我们添加了 `-not -name ".DS_Store"` 参数，用于排除文件名为.DS_Store的文件夹。其余部分与之前的命令相同。运行此命令后，生成的目录树将不包括.DS_Store 文件。

#### 将终端显示的目录树内容输出到 txt 文件中:
> txt文件会自动生成。

```shell
find . -maxdepth 2 -not -name ".DS_Store" -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g' > tree.txt
```

### 使用 tree 指令生成目录树：
使用 tree 指令生成目录树非常方便，但 tree 指令有一点缺陷，无法限制树的深度；（刚好和 find 指令生成目录树指令互补）<br>

#### 安装 tree 库:
Ubuntu 和 Mac 都内置了 find 指令，但没有自带 tree 指令，需要使用如下指令安装：<br>
Ubuntu安装 tree：<br>
```shell
apt install tree
```
Mac安装 tree：<br>
```shell
brew install tree
```

#### 基于当前目录所有文件生成目录树：
> 直接一个tree就搞定～

```shell
tree
```

#### 将输出保存到一个文本文件中（例如，"tree.txt"）：
```shell
tree > tree.txt
```

#### 设置屏蔽项:
tree 指令的优势是可以设置屏蔽项，假设你不想要目录树中显示 `lib.egg-info` 和 `__pycache__` 文件夹下的内容，可以使用以下指令:<br>
```shell
tree -I 'lib.egg-info|__pycache__'
```

‼️‼️‼️`-I` 参数后面的内容用于排除匹配的文件或文件夹。注意`|`两边的内容不能有空格‼️‼️‼️<br>


#### 同时屏蔽文件夹和文件：
```shell
tree -I 'lib.egg-info|__pycache__|README.md'
```

### find+tree，限制树的深度，同时屏蔽某些文件或文件夹：
```shell
find . -maxdepth 2 -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g' | tree -I 'lib.egg-info|__pycache__'
```
解释：<br>
限制目录树的深度为2层，同时目录树中不含文件夹 `lib.egg-info` 和 `__pycache__` 及其下属内容。<br>


## ubuntu系统如何设置root级别的别名--例如 alias cls='clear'

如果你想在以root用户身份切换后也能够使用别名，可以进行以下操作：<br>

1. 打开root用户的配置文件`.bashrc`，可以使用任何文本编辑器来打开该文件。以下示例使用vim编辑器：

```bash
vim ~/.bashrc
```

如果你是root用户，该指令会默认打开root用户的目录文件。如果你是常规用户，该指令会默认打开常规用户的目录文件。<br>

2. 在`.bashrc`文件的末尾，添加你想要设置的别名。例如，添加一个名为cls的别名，将其映射到clear命令：

```bash
alias cls='clear'
```

3. 保存并关闭文件(`:x`)。

4. 重新加载`.bashrc`文件，使设置生效。可以使用以下命令重新加载：

```bash
source /root/.bashrc
```

不需要重启终端，现在，你已经成功设置了root级别的别名。在以root身份运行的终端会话中，输入`cls`命令将会执行`clear`命令来清空终端屏幕。

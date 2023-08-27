# Linux Command
Linux指令都是通过终端或shell脚本操作的，所以下文笔者不会备注在哪里操作。<br>
Ps:本文所有指令为 Linux 版本，Windows 或 MacOS 指令请自行从网络寻找。<br>
<br>
- [Linux Command](#linux-command)
  - [权限指令：](#权限指令)
  - [系统信息指令：](#系统信息指令)
  - [CPU 和 GPU 相关：](#cpu-和-gpu-相关)
  - [服务相关：](#服务相关)
  - [常规文件操作：](#常规文件操作)
  - [创建、移动、复制、删除文件/文件夹：](#创建移动复制删除文件文件夹)
  - [压缩文件、解压文件：](#压缩文件解压文件)
  - [文件或文件夹的上传于下载：](#文件或文件夹的上传于下载)

## 权限指令：
查看自己是何种类型的用户，root或普通用户：<br>
```shell
whoami
```
如果返回 `root` 就代表你是 `root` 用户，如果返回的是其他内容，代表你不是 `root` 用户。

或者可以单纯从终端行首的命令符号 `$` 和 `#` 区分：<br>
普通用户显示的就是 `$`；
root用户显示的就是  `#`；

切换为 `root` 用户<br>
```shell
sudo su -
```
如果没有设置密码，会直接切换到 `root` 用户，拥有 `root` 权限。如果设置了密码，此时会提示你输入密码，正常输入即可。注意⚠️：密码是不显示状态的，没法直接看到的。键盘正常输入密码，然后回车即可。<br>
<br>

获取系统所有库最新信息：<br>

用于让系统获取所有库的最新信息，不会更改任何安装库的版本。
```shell
sudo apt update
```
<br>

shell 和 bash 的关系：<br>
shell 指的是一类程序，能按照用户要求去调用操作系统接口的程序。linux发展至今,有许多shell程序(例如：sh、ksh、bash、zsh)，bash是其中之一。<br>
<br>

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

查看自己电脑的系统内存：
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
<br>


## 服务相关：
终端查看系统时间：<br>
> CST表示上海时间，也就是国际规定的东八区时间。
```shell
date
```
按照 `"年-月-日 时:分:秒"` 显示系统时间:
```shell
date "+%Y-%m-%d %H:%M:%S"
```

在Linux系统中，可以使用以下命令来查看端口的占用情况：
1. 使用 netstat 命令：

```shell
netstat -ntlp 
```
这将显示当前正在监听的所有TCP和UDP端口以及它们的占用情况。TCP端口以 "tcp" 标识，UDP端口以 "udp" 标识。

2. 使用 lsof 命令：
```shell
lsof -i :端口号
```
例如查看端口号 `7711` 的占用情况：<br>
```shell
lsof -i :7711
```
如果端口号 `7711`没有被占用，不会返回任何信息，如果被占用，会返回对应进程的pid和应用程序的详细信息。<br>

3. 关闭端口：
根据上面获取的pid，kill掉已经对应的进程。注意⚠️：一定要看清进程pid，不要误杀了其他人的进程‼️‼️<br>
```shell
kill -9 pid
```

## 常规文件操作：
清空一个文件中的内容：<br>
> 文件的内容将被清空，但文件本身仍然存在。

在Linux中，如果要清空名为example.txt的文件的内容，可以运行以下命令：<br>
```shell
> example.txt
```
这将清空 `example.txt` 文件中的内容，也可以按照路径的方式去清理对应路径下的某个文件。<br>
<br>

终端运行自己的python程序时，如果python程序中有 `print` 或 `log` 项，可以通过以下指令将终端的输出写入`example.txt`文件：<br>
```shell
python main.py > example.txt
```
这种方式每次运行上述代码都会将 `example.txt` 清空，然后重新写入。如果想要采用追加的方式写入，可以采用以下指令：<br>
```shell
python main.py >> example.txt
```
<br>


假设你想要在 `/` 根目录下按名称查找 `files.zip` 文件:<br>
```shell
find / -name files.zip
```


假设你只记得文件名的部分内容，可以采用模糊查找：<br>
```shell
find / -name "*文件名"： 
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
假设想查看当前目录下的文件个数：<br>
```shell
ls -l ./|grep "^-"|wc -l
```
或者使用`find`指令查看文件个数：<br>
```shell
find <文件夹路径> -type f | wc -l
```
假设想查看当前目录下的文件个数：<br>
```shell
find ./ -type f | wc -l
```
<br>


## 创建、移动、复制、删除文件/文件夹：
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

如果你不够熟悉 `vim` 的语法，可以先用 `echo` ，`echo`支持通过终端将内容写入文件:<br>
```shell
echo "想要写入的内容" > example.txt
```
上述指令会将内容 "覆盖" 写入到对应的文件中，文件之前的内容不复存在，只有新写入的内容。如果想要采用 "追加" 的形式写入内容，需要使用以下指令：<br>
```shell
echo "想要写入的内容" >> example.txt
```

写入内容后，想要查看文件中的内容，通过以下指令：<br>
```shell
cat example.txt
```
<br>

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
<br>


## 压缩文件、解压文件：
Linux安装 `zip` 和 `unzip` 模块：<br>
```shell
sudo apt-get install zip
```
```shell
apt-get install unzip
```
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

## 文件或文件夹的上传于下载：
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
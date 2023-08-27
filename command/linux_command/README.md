# Linux Command
Linux指令都是通过终端或shell脚本操作的，所以下文笔者不会备注在哪里操作。<br>
Ps:本文所有指令为 Linux 版本，Windows 或 MacOS 指令请自行从网络寻找。<br>

- 查看自己是何种类型的用户，root或普通用户：<br>
```shell
whoami
```
如果返回 `root` 就代表你是 `root` 用户，如果返回的是其他内容，代表你不是 `root` 用户。

或者可以单纯从终端行首的命令符号 `$` 和 `#` 区分：<br>
普通用户显示的就是 `$`；
root用户显示的就是  `#`；

- 切换为 `root` 用户<br>
```shell
sudo su -
```
如果没有设置密码，会直接切换到 `root` 用户，拥有 `root` 权限。如果设置了密码，此时会提示你输入密码，正常输入即可。注意⚠️：密码是不显示状态的，没法直接看到的。键盘正常输入密码，然后回车即可。<br>

- 获取系统所有库最新信息：<br>

用于让系统获取所有库的最新信息，不会更改任何安装库的版本。
```shell
sudo apt update
```

- shell 和 bash 的关系：<br>
shell 指的是一类程序，能按照用户要求去调用操作系统接口的程序。linux发展至今,有许多shell程序(例如：sh、ksh、bash、zsh)，bash是其中之一。<br>

- Linux查看自己是什么系统的方式：<br>
```shell
cat /etc/os-release
```

- Linux系统查看操作系统的位数是x86还是x64的方式：<br>
```shell
getconf LONG_BIT
```


如果你想要做深度学习任务，想查看GPU使用情况：<br>
动态查看(0.5秒刷新一次)nvidia-smi使用情况指令为：<br>
```shell
watch -n .5 nvidia-smi
```
如果想要2秒刷新一次，简单修改指令即可：<br>
```shell
watch -n 2 nvidia-smi
```

nvidia-smi -a 查看gpu细节情况：
将返回如下信息：

lscpu 查看cpu详细信息：
执行该命令后，会显示有关CPU的详细信息，包括内存核数。你可以查找"CPU(s)"或"Core(s) per socket"字段来获取内存核数的信息。

也可直接通过如下指令查看：
nproc # 查看cpu核数；


getconf LONG_BIT 返回的 64 和 lscpu 返回的 Architecture: x86_64 有什么区别？为什么一个是64，一个是86？
getconf LONG_BIT和lscpu返回的结果中的 "64" 和 "x86_64" 实际上指的是不同的概念。

- getconf LONG_BIT 返回的是操作系统的位数，表示操作系统的寻址空间大小，即指针的位数。在这种情况下，返回的值为 "64"，表示操作系统是64位的，即支持64位的寻址空间。

- lscpu 返回的是CPU架构的信息。"Architecture: x86_64" 表示CPU架构是x86，且是64位的。在这种情况下，"x86"是指基于英特尔x86架构的处理器，而 "64" 表示该CPU支持64位的指令集。

因此，"64" 在 getconf LONG_BIT 中表示操作系统位数，而在 lscpu 中表示CPU架构的指令集位数。这两个值并不是直接相关的，因为操作系统的位数可以不同于CPU架构的指令集位数。在现代计算机中，通常会将64位的操作系统安装在支持64位指令集的CPU上，以充分利用更大的寻址空间和处理器功能。
当终端显示(end)时的解决方案：按q键回归正常。
查看自己是否为root用户：
看符号，#为root，$说明是普通用户。
或者直接输入指令：
whoami

查看自己电脑的限制内存：
free -h

终端查看系统时间：

CST表示上海时间，也就是国际规定的东八区时间。
date # 直接查看系统时间

date "+%Y-%m-%d %H:%M:%S" # 按照 "年-月-日 时:分:秒" 显示系统时间

linux如何查看自己的端口占用情况？
在Linux系统中，你可以使用以下命令来查看端口的占用情况：

1. 使用 netstat 命令：
netstat -tuln

netstat -ntlp 


   这将显示当前正在监听的所有TCP和UDP端口以及它们的占用情况。TCP端口以 "tcp" 标识，UDP端口以 "udp" 标识。

2. 使用 lsof 命令：
lsof -i :端口号

lsof -i :7711

lsof -i :8082

sudo lsof -i :端口号

   将 "端口号" 替换为你想要查看的具体端口号。这将显示占用该端口的进程和应用程序的详细信息。

关闭端口：
kill -9 pid（kill掉已经启动的服务）


Mac如何查看自己的端口占用情况？
netstat -an | grep LISTEN





清空一个文件中的内容：
文件的内容将被清空，但文件本身仍然存在。
在Linux中，如果要清空名为example.txt的文件的内容，可以运行以下命令：
> example.txt

这将清空example.txt文件中的内容。
查找文件：find / -name files.zip
精确查找
find / -name "文件名" : 在/根目录下按名称查找文件


模糊查找
find / -name "*文件名"： 在/根目录下按*名称*模糊查找文件

查看当前目录：pwd
查看上一级目录：cd ..
切换目录：cd
切换到根目录：cd /
查看文件(含隐藏，为git仓库使用方便)： ll -ah
查找文件夹下文件个数：ls -l 的拓展
ls -l ./|grep "^-"|wc -l
# "-" 在linux查找中表示文件，d表示directory，表示文件夹。
# -rw-r--r--
# drwxr-xr-x

示例图片：

linux如何查看文件夹下文件数量？
要查看Linux中文件夹下的文件数量，您可以使用ls命令结合一些选项来完成。以下是几种方法：

方法1：使用ls命令和wc命令
ls -l | grep "^-" | wc -l

这个命令将列出文件夹中的所有文件和目录，并使用grep命令过滤只显示文件（不包括目录）。然后，使用wc -l命令计算输出行数，即文件数量。



方法2：使用find命令和wc命令
find <文件夹路径> -type f | wc -l
find ./ -type f | wc -l    # 查看当前路径下文件数量

将<文件夹路径>替换为您要查看的实际文件夹路径。该命令使用find命令递归查找指定文件夹下的所有文件（不包括目录），然后使用wc -l命令计算输出行数，即文件数量。


创建目录：mkdir

Mkdir -p .../.../...  直接创建多级目录：

下面这个例子省略了cd到创建的目录下，主要意思是，在当前目录下直接 mkdir -p a/b/c 是直接在当前目录下延后。

解压：unzip
zip压缩指令：

zip -r -q -o xgb.zip xgboost的交付代码

如果终端提示：-bash: zip: command not found
这是因为liunx服务器上没有安装zip命令，需要安装一下即可。
# linux安装zip命令：
apt-get install zip 或yum install zip
# linux安装unzip命令：
apt-get install unzip 或yum install unzip

tar.gz压缩指令：
tar -czvf archive.tar.gz folder_name


tar.gz解压指令：
tar -xzvf archive.tar.gz # 解压到当前文件夹；

tar -xzvf archive.tar.gz -C /path/to/targert_directory # 解压到目标路径




重命名： mv old_name new_name(等同于移动文件)
移动有相同格式的文件 mv xxx* ：

移动文件夹：--mv -f 
mv -f old/path new/path    # mv的参数中没有 -r ；

案例分析：


复制文件 cp：
cp -r old_path new_path
cp -rf old_path new_path # 可以复制文件夹

复制文件夹下的内容到另一个文件夹下：
cp -r /path/to/source/* /path/to/destination/

例如：
cp -r ./dist/* ../IRM2022_WebServer/src/public 



删除指令 rm 的使用：
删除文件(不能删除文件夹)rm：
rm -r /xxx/file.py 


批量删除类似文件：
类似下列的文件有很多，如何批量删除
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

要批量删除类似的文件，您可以使用命令行中的通配符来匹配文件名模式。在Linux和类Unix系统中，可以使用rm命令结合通配符来删除文件。

在您的示例中，文件名具有相同的前缀"nlp."，后面跟着一个日期。如果您希望删除所有以"nlp."开头的文件，可以使用如下命令：

rm nlp.*


上述命令将删除当前目录下以"nlp."开头的所有文件。

如果您只想删除特定日期范围内的文件，可以使用更精确的通配符模式。例如，如果您只想删除从2023年6月21日到2023年6月30日的文件，可以使用以下命令：

rm nlp.2023062[1-9].log nlp.2023063[0-1].log


上述命令将删除匹配模式的文件，其中[1-9]表示匹配范围为1到9的数字，[0-1]表示匹配范围为0到1的数字。

在执行删除命令之前，请确保您已经仔细检查了文件名模式，以免意外删除了不希望删除的文件。


删除文件(可以删除文件夹)（全部删除，不提示）：
rm -rf /bbb/file.py


项目文件夹下有多个文件或文件夹，如何只保留其中某一个文件或文件夹，删除其他所有内容：
假设只保留 env_nazhi 文件夹，使用以下指令即可：【操作无法撤销，使用需注意！】
rm -r !(env_nazhi)


创建文件--touch
touch 命令可以创建一个新的空文件夹，也可以修改访问的一些属性(这部分没有细了解)。

终端中将内容写入文件操作--echo
1. echo "想要写入的内容" > 文件名
将想要的内容覆盖到对应的文件中，文件之前的内容不复存在，只有新写入的内容。
2. echo "想要写入的内容" >> 文件名

查看文件中的内容--cat

运行shell脚本-- source xxx.sh或 bash xxx.sh :
向 Linux服务器 上传文件和下载文件：rz、sz
注意：无论是 rz 还是 sz，都只能上传或下载文件(可以多个)，但无法上传或下载文件夹；
注：上传的时候，如果上传到的linux目录有同名的文件，是无法上传的，需要先删掉 Linux 上的同名文件。
rz 和 sz 的作用都是让服务器做某事，以服务器为主体。
rz用法：
rz：（receive ZMODEM）意为让服务器接受文件；
rz -be # 输入后会弹出对话框让用户选择需要上传的文件

-b：--binary:以二进制方式传输，推荐使用
-e：-e, --escape:对所有控制字符转义，建议使用
sz用法：
sz：（send ZMODEM）意为让服务器发送文件；
下载一个文件：sz filename
下载多个文件：sz filename1 filename2
下载dir目录下的所有文件，不包含dir下的文件夹：sz dir/*
如果无法使用 rz 或 sz 指令，需要先安装 lrzsz 。
yum -y install lrzsz 

服务器--服务器，服务器--本地传输方式：scp

员工大多没有root权限，不能使用这种写法。
scp -r rec@10.115.81.93:/app/clients/supply_dev/supply_dev/luozijian2/chenpeilong.csv /data_file/




linux 和 shell 的关系：
Shell 是 linux 命令的整合，通过 shell 脚本可以实现一大堆 linux 命令的顺序运行。
Shell 脚本通过 source 指令运行。
Vim 指令可以创建 shell脚本，非常方便。





Linux 去除 pandas.columns 中表头重复性内容的指令：
# linux 去重表头重复性内容的指令
sed -i '1!b;s,dwr_alg_bert_train_merge_v1.,,g' xgb_chenpeilong.csv 

curl 命令 类似wget：
在 Linux 中 curl 是一个利用 URL 规则在命令行下工作的文件传输工具，可以说是一款很强大的 http命令行工具。它支持文件的上传和下载，是综合传输工具，但按传统，习惯称为 URL下载工具。
curl 全称 CommandLine URL 命令行网址。
# 语法： 用法和 wget 相同
curl [option] [url]

wget 的使用：
直接使用 wget [网址] 会下载到当前目录。

ETA 智能进度条
意思为：预计抵达时间 ( Estimated time of arrival )
git clone 的用法：
用法为 git clone https://xxxx.git ，其中后面的网址并不是直接粘贴了对应的网址，有专门的位置输出git网址用于clone。以下为示例：

git clone https://github.com/shibing624/textgen.git

docker 命令：
docker是容器化技术，将docker理解为一个方便的虚拟机即可，一个系统允许多个虚拟机，允许多个docker，一个意思。
docker ps   显示正在运行的容器：
docker ps -a 显示所有的容器，包括未运行的；
docker run 容器运行，需配合相关参数；
docker run --rm 退出容器后，容器会被删除，常用于测试；
export命令的作用：
命令 export 可新增，修改或删除环境变量，供后续执行的程序使用，但是 export 产生的效果仅在本次会话中有效。
举例说明，将路径 /opt/au1200_rm/build_tools/bin 追加到环境变量 PATH 中：
export PATH="$PATH:/opt/au1200_rm/build_tools/bin"

永久修改环境变量：
在 /etc/profile 文件中声明定义环境变量，那么每次创建进程的时候，就都可以获取到该变量的值。
[root@htlwk0001host ~]# vi /etc/profile

在里面加入：
export PATH="$PATH:/opt/au1200_rm/build_tools/bin"

修改配置文件 /etc/profile 是对所有的用户有效，建议修改用户根目录下的配置文件 .bashrc 或 .bash_profile，这两个配置文件仅对当前登录用户有效。

注：在全局配置文件 /etc/profile 中，如果把变量定义成上述的语句，那么第一个进程创建时变量 $PATH 的取值必然为空，因为没有父进程，所以谈不上复制父进程的全局变量。第一个进程创建时先读取 /etc/profile 文件，此时第一个进程的内存中根本不存在变量 $PATH，所以何来“旧值”替换。
~/.bashrc和/etc/profile的不同：
在Linux系统中，~/.bashrc和/etc/profile都是用来配置用户的bash环境的文件，但它们的优先级是不同的。

~/.bashrc是每个用户的个人bash配置文件，位于用户的主目录下。当一个用户登录时，bash会首先读取/etc/profile文件，然后读取~/.bashrc文件。因此，~/.bashrc的优先级更高，它可以覆盖/etc/profile中的设置。

/etc/profile是系统级别的bash配置文件，适用于所有用户。它定义了系统范围的环境变量、默认路径和其他全局设置。如果在~/.bashrc中没有设置某个环境变量或其他设置，bash会查找/etc/profile文件中的对应项。

综上所述，~/.bashrc的优先级更高，它可以覆盖/etc/profile中的设置。但是，/etc/profile中的设置对所有用户都有效，而~/.bashrc中的设置只对当前用户有效。
cd /etc/ 中的etc是什么意思？全称是什么？
在计算机中，"etc" 是指"et cetera"，这是拉丁语短语，意思是"和其他的"。在Linux和类Unix系统中，"/etc"是一个目录，用于存放系统的配置文件和其他重要的文件。它包含了许多系统级别的配置文件，例如网络配置、用户帐户和密码策略、启动脚本等。

"etc" 目录的全称是 "et cetera"，但它通常被简称为 "etc"，成为计算机领域的术语。

以下信息中文件名带*是什么意思？
root@7minAI-1:/mnt/aidata/wechatdata/mysql# ll
drwxrwxrwx 7 mysql mysql      4096 Jul 26 09:35 ./
drwxr-xr-x 5 root  root       4096 Aug  8 10:55 ../
-rwxrwxrwx 1 mysql mysql      1036 Oct 14  2019 advisor.csv*
-rwxrwxrwx 1 mysql mysql   1283637 Oct 14  2019 friend.csv*
-rwxrwxrwx 1 mysql mysql      2476 May 10 17:20 ib_buffer_pool*
-rwxrwxrwx 1 mysql mysql 146800640 Aug  8 10:43 ibdata1*
drwxrwxrwx 2 mysql mysql     12288 Jul 30 20:45 irmdata/

在所提供的信息中，文件名带*表示这些文件是可执行文件或者脚本文件。

# Crontab 设置定时任务：
Crontab是一个用于在Linux和Unix系统中定期执行任务的命令。它允许你按照特定的时间和日期计划执行脚本、命令或程序。<br>
- [Crontab 设置定时任务：](#crontab-设置定时任务)
  - [个人配置：](#个人配置)
  - [编辑crontab:](#编辑crontab)
  - [crontab 的使用规则：](#crontab-的使用规则)
  - [设置定时任务的流程(以shell脚本运行python文件为例):](#设置定时任务的流程以shell脚本运行python文件为例)
    - [1. 准备好你需要做定时任务的代码(`main.py`):](#1-准备好你需要做定时任务的代码mainpy)
    - [2. 查看设置环境变量以及配置系统中的 Anaconda 环境的方式:](#2-查看设置环境变量以及配置系统中的-anaconda-环境的方式)
    - [3. 查看自己的shell环境:](#3-查看自己的shell环境)
    - [4. 编写shell脚本,假设你的shell脚本为 `main.sh`:](#4-编写shell脚本假设你的shell脚本为-mainsh)
    - [5. 为shell脚本开通运行权限:](#5-为shell脚本开通运行权限)
    - [6. 运行shell脚本测试是否正常运行:](#6-运行shell脚本测试是否正常运行)
    - [7. crontab 编辑任务:](#7-crontab-编辑任务)
    - [8. 查看所有的 crontab 任务(可选):](#8-查看所有的-crontab-任务可选)
  - [关于定位conda.sh的补充:](#关于定位condash的补充)
  - [shell 解释器相关指令：](#shell-解释器相关指令)
  - [查看所有定时任务：](#查看所有定时任务)
  - [删除定时任务：](#删除定时任务)
  - [Crontab 默认的日志输出路径：](#crontab-默认的日志输出路径)
  - [crontab命令解释:](#crontab命令解释)

## 个人配置：

系统：Ubuntu 18.04<br>

## 编辑crontab:

终端输入 `crontab -e` 进入crontab编辑模式：<br>

```shell
crontab -e
```

第一次使用 crontab 会显示如下界面:<br>

```shell
no crontab for root - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/vim.tiny
  4. /bin/ed

Choose 1-4 [1]: 
```

这是cron服务询问你选择使用哪个编辑器进行设置。在这里，你可以选择以下编辑器:<br>

1. /bin/nano - 这是最简单的编辑器。

2. /usr/bin/vim.basic - 这是Vim编辑器的基本版本。

3. /usr/bin/vim.tiny - 这是Vim编辑器的精简版本。

4. /bin/ed - 这是一个行文本编辑器。

根据你的偏好选择一个编辑器。你可以输入1、2、3或4来选择相应的编辑器。如果没有特殊需求，可以选择输入1以使用nano编辑器。<br>

笔者比较习惯vim，选择的是2。<br>

第一次进入crontab后会显示提示内容:<br>

```shell
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
```

**内容解释:** <br>

编辑此文件以介绍要由cron运行的任务。<br>

每个要运行的任务都必须通过一行来定义， 指示任务将在何时运行以及运行任务的命令是什么。<br>

要定义时间，可以为分钟（m）、小时（h）、每月的日期（dom）、月份（mon）和星期几（dow）提供具体的值， 或者在这些字段中使用“*”（表示“任意”）。<br>

请注意，任务将根据cron系统守护进程对时间和时区的概念启动。<br>

crontab任务的输出（包括错误信息）将通过电子邮件发送给属于crontab文件的用户（除非重定向）。<br>

例如，您可以每周5点备份所有用户账户： `0 5 * * 1 tar -zcf /var/backups/home.tgz /home/` <br>

分钟 小时 每月日期 月份 星期几 命令。<br>

其实，只需要注意 crontab 的最小单位是分钟，时间选项有5个，其他没什么。<br>

可以使用vim的快捷键清除 crontab 中初始化的提示内容：<br>

```shell
ggdG
```


## crontab 的使用规则：

```shell
# crontab 支持用 "#" 进行注释；
* * * * * your_task_command_1
* * * * * your_task_command_2
* * * * * your_task_command_3
```

五个*分别表示：分钟(0-59) 、小时(0-23)、 天(1-31) 、月份(1-12)、 星期几(0-7，其中0和7都可以表示星期天)<br>

Crontab 支持同时设定多个定时任务，每一行都代表一个独立的任务，并且它们彼此独立运行，互不影响。因此，如果某一行的脚本出现错误或失败，通常不会直接影响其他行脚本的执行。<br>

然而，要注意以下几点：<br>

1. 脚本的错误可能会导致日志文件的异常增长：如果脚本中有错误信息输出，这些错误信息可能会填满日志文件，从而影响其他任务的日志记录。

2. 脚本的错误可能会引起资源问题：某些错误可能导致脚本无限循环或占用大量资源，从而对系统性能产生影响。

3. 脚本的错误可能会影响后续任务：如果一个脚本的错误导致了系统资源问题或者系统崩溃，这可能会影响后续的任务执行。


## 设置定时任务的流程(以shell脚本运行python文件为例):

### 1. 准备好你需要做定时任务的代码(`main.py`):

确保自己的python文件可以正常运行。<br>

### 2. 查看设置环境变量以及配置系统中的 Anaconda 环境的方式:

设置环境变量以及配置系统中的 Anaconda 需要激活 `conda.sh` 文件,运行以下指令查看conda的安装路径:<br>

```bash
which conda
```

终端输出:<br>

```log
/root/anaconda3/bin/conda
```

通常情况下，`conda.sh` 文件位于 Anaconda 安装目录的 `etc/profile.d` 目录下。因此,此例中conda激活方式为:<br>

```bash
source /root/anaconda3/etc/profile.d/conda.sh
```

### 3. 查看自己的shell环境:

终端运行以下指令，查看当前shell环境:<br>

```bash
echo $SHELL
```

笔者终端输出:<br>

```log
/bin/bash
```

由于crontab运行在一个相对干净的shell环境中(例如 `/bin/sh` )，所用的shell环境可能与个人终端所使用的终端环境不同‼️‼️‼️，需要根据终端的输出进行shell脚本设置。<br>

基于笔者终端的shell环境，编写shell脚本时，需要在文件第一行添加以下内容，指定shell脚本运行时的所用的shell环境:<br>

```bash
#!/bin/bash
```

### 4. 编写shell脚本,假设你的shell脚本为 `main.sh`:

```bash
#!/bin/bash

# 查看自己正在使用的shell解释器名称,这里是为了检查crontab运行的环境是否为 `/bin/bash`。
echo $SHELL

# 初始化conda环境
source /root/anaconda3/etc/profile.d/conda.sh

# 激活conda环境
conda activate langchain

# 切换路径
cd /data/

# conda环境下运行python文件
python main.py
```

### 5. 为shell脚本开通运行权限:

Linux为shell脚本开通权限的指令为：<br>

```shell
chmod +x /your_script_path/main.sh  # 开启权限；
```

⚠️注意：必须要开启权限，否则脚本是无法正常运行的。❌❌❌<br>

🚀如果你当前处于shell脚本所在目录，可以使用相对路径开启shell脚本权限:<br>

```shell
chmod +x ./main.sh  # 开启权限；
```

### 6. 运行shell脚本测试是否正常运行:

构建crontab任务前，应终端先测试下shell脚本是否运行正常:<br>

```bash
./main.sh
```

如果没有报错，我们就可以构建crontab任务了。<br>

### 7. crontab 编辑任务:

终端输入以下命令进入 crontab 编辑模式:<br>

```bash
crontab -e
```

进入 crontab 编辑模式后输入自己的指令，以 vim 举例，英文状态下按 `i` 开启 **vim** 编辑模式，假设你想要每隔5分钟运行一次shell脚本:<br>

```shell
*/5 * * * * /data/main.sh >> /data/task_log.log 2>&1
```

🌈然后保存内容并退出crontab即可，crontab 编辑后不需要激活，会自动按照设定的指令运行。<br>

🚨🚨🚨注意:<br>

在`crontab`中添加这样的条目后，指定的脚本或命令（在这个例子中是`*/5 * * * * /data/main.sh >> /data/task_log.log 2>&1`）将会在每个小时的第 5 分钟、第 10 分钟、第 15 分钟等等执行。这意味着它将按照设定的时间间隔（在这里是每 5 分钟）执行，而不是立即执行。<br>

所以，如果你在 10:02 添加了这个`crontab`条目，那么第一次执行将在 10:05 发生。如果你在 10:04 添加了这个条目，同样，第一次执行也是在 10:05。这意味着，保存并退出`crontab`之后，脚本或命令的执行不会立即发生，而是等到下一个符合设定时间（即每小时的第 5、10、15... 分钟）的时刻。<br>

### 8. 查看所有的 crontab 任务(可选):

运行以下指令可以查看crontab中所有的定时任务:<br>

```bash
crontab -l
```

## 关于定位conda.sh的补充:

`.bashrc` 或 `.zshrc` 中 `conda.sh` 相关内容如下:<br>

```shell
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/opt/anaconda3/bin:$PATH"
    fi
fi
```

所以，conda 激活指令为：<br>

```shell
source /opt/anaconda3/etc/profile.d/conda.sh
```


## shell 解释器相关指令：

查看当前终端正在使用的 shell 解释器：<br>

```shell
echo $SHELL
```

查看所有可用的 shell 列表：<br>

```shell
cat /etc/shells
```

切换到另一个 shell 解释器，假设我现在正处于 zsh 解释器，使用以下指令可切换到 bash 解释器：<br>

```shell
chsh -s /bin/bash
```


## 查看所有定时任务：

```shell
crontab -l
```

## 删除定时任务：

要从 Crontab 中删除某个定时任务，可以按照以下步骤进行操作：<br>

1. 打开终端窗口，输入 `crontab -e` 命令以编辑 Crontab 文件：

2. 在文本编辑器中，定位到你要删除的定时任务所在的行。

3. 删除该行，并保存文件。

4. 当保存并退出文本编辑器后，Crontab文件将被更新，相应的定时任务也会被删除。

如果你想删除全部的Crontab定时任务，可以使用以下命令：<br>

```shell
crontab -r
```

这将删除你当前用户的所有定时任务。<br>

请注意，删除Crontab定时任务是永久性的，一旦删除无法恢复，请确保你只删除了所需的定时任务。<br>


## Crontab 默认的日志输出路径：

```shell
cat /var/log/syslog
```


## crontab命令解释:

```bash
# 注释以"#"开头, crontab支持注释, 用户输入 `crontab -l` 可以查看到注释信息
0 0 * * * /path/to/semantic_task_cold_start.sh >> /data/semantic_task_log.log 2>&1
```

这个cron表达式的含义是：<br>

- `0 0 * * *` 表示在每天的0点0分执行任务。
  
- `/path/to/semantic_task_cold_start.sh` 是要执行的脚本的绝对路径，你需要将它替换为实际的脚本路径。
  
- `>> /data/semantic_task_log.log` 表示将脚本的标准输出追加到 `/data/semantic_task_log.log` 文件中。
  
- `2>&1` 将标准错误输出（stderr）也重定向到标准输出，以便将错误信息一并写入日志文件。

注意确保将路径替换为实际的文件路径，然后保存并退出编辑器。<br>

注意⚠️:<br>

使用 **`2>&1`** ，脚本的所有输出，无论是正常的输出还是错误信息，都会被记录在同一个日志文件中。如果不使用 `2>&1`，那么 stderr（错误信息）将不会被重定向，可能会被丢弃或者发送到不同的地方，例如邮件给系统管理员或者默认的错误日志位置。(默认crontab的日志输出路径为`cat /var/log/syslog`)<br>

如果不存在`semantic_task_log.log`，系统会自动创建，但需要确定这个用户(例如我是`ecs-user`)需要有足够的权限来在指定的目录下创建文件。如果权限不足，重定向操作会失败，并且可能会生成错误消息。<br>
# shell脚本运行py文件示例
## 文件解释：
main.py:<br>
测试文件，用于确定本地是否能连接到自己localhost的mysql数据库。<br>
run_main.sh:<br>
可运行shell脚本，包含使用conda切换到指定虚拟环境，运行main.py指令。<br>

## 运行方式：
cd 到当前目录，然后运行以下指令即可:
```shell
./run_main.sh           # 终端直接输入即可。
```

如果提示 permission denied:./run_main.sh，运行以下指令，然后再次运行上一步的操作即可。
```shell
chmod +x ./run_main.sh  # 开启权限；
```

⚠️注意：必须要开启权限，否则脚本是无法正常运行的。❌❌❌

## run_main.sh 相关内容拓展：

conda 的默认激活指令如下:<br>

```shell
source ~/anaconda3/etc/profile.d/conda.sh   # 默认路径
```

如果使用默认 conda 激活指令报错，可先查看终端正在使用的shell解释器，确定自己的shell解释器:<br>

```shell
echo $SHELL
```

> 部分系统在使用 `crontab` 的定时任务时，必须指定sh环境，因为 `crontab` 运行的环境不一定和自己手动运行脚本时的环境相同。
> 即，需要在shell文件第一行添加类似 `#!/bin/bash` 的内容。

若上述指令显示 /bin/zsh，可通过以下指令确定 conda.sh 的路径。<br>

```shell
cat ~/.zshrc
```

我的 zshrc 中 conda.sh 相关内容如下:<br>

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
所以，我使用的 conda 激活指令为：<br>
```shell
source /opt/anaconda3/etc/profile.d/conda.sh
```

## 应对的错误信息：
```shell
CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.

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

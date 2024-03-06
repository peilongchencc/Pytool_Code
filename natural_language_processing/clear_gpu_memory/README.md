# Linux清空GPU显存:
- [Linux清空GPU显存:](#linux清空gpu显存)
  - [情况描述:](#情况描述)
  - [解决方式:](#解决方式)
  - [查看清理后的效果:](#查看清理后的效果)

## 情况描述:

当GPU占用率为0%时，显存没有清空。显存不清空会对后续自己或其他人使用GPU产生影响，毕竟任务占用的GPU显存小了。<br>

终端输入`nvidia-smi`查看到的GPU状态如下:<br>

```txt
(base) root@5f7d2ce68c26:~/Documents/Llama-Chinese_Custom# nvidia-smi
Wed Mar  6 15:43:50 2024       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.60.11    Driver Version: 525.60.11    CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA A100-PCI...  On   | 00000000:00:07.0 Off |                    0 |
| N/A   30C    P0    36W / 250W |  10360MiB / 40960MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA A100-PCI...  On   | 00000000:00:08.0 Off |                    0 |
| N/A   28C    P0    33W / 250W |  10360MiB / 40960MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
|   2  NVIDIA A100-PCI...  On   | 00000000:00:09.0 Off |                  Off |
| N/A   28C    P0    34W / 250W |  10360MiB / 40960MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
|   3  NVIDIA A100-PCI...  On   | 00000000:00:0A.0 Off |                    0 |
| N/A   28C    P0    36W / 250W |  10360MiB / 40960MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
```

## 解决方式:

显存没有清空，而且没有进程正在执行，说明有僵尸进程。此时可通过下列方式清空显存:<br>

1. 安装`psmisc`。(可选)

> 你的Linux系统可能已经安装了`psmisc`，但不妨碍再运行一遍下列指令。

```bash
apt-get install psmisc
```

安装了`psmisc`包，你才能使用`fuser`指令。`fuser`指令用于识别使用指定文件或文件系统的进程。这可以帮助你找出哪个进程正在使用某个文件。<br>

2. 查找占用GPU资源的PID:

```bash
fuser -v /dev/nvidia*
```

效果如下:<br>

```txt
(base) root@5f7d2ce68c26:~/Documents/Llama-Chinese_Custom# fuser -v /dev/nvidia*
Cannot stat file /proc/131/fd/0: Permission denied
Cannot stat file /proc/131/fd/1: Permission denied
Cannot stat file /proc/131/fd/2: Permission denied
Cannot stat file /proc/131/fd/3: Permission denied
Cannot stat file /proc/133/fd/0: Permission denied
Cannot stat file /proc/133/fd/1: Permission denied
Cannot stat file /proc/133/fd/2: Permission denied
Cannot stat file /proc/133/fd/3: Permission denied
Cannot stat file /proc/133/fd/4: Permission denied
Cannot stat file /proc/133/fd/5: Permission denied
Cannot stat file /proc/133/fd/6: Permission denied
Cannot stat file /proc/133/fd/7: Permission denied
Cannot stat file /proc/133/fd/8: Permission denied
                     USER        PID ACCESS COMMAND
/dev/nvidia1:        root     kernel mount /dev/nvidia1
                     root      33118 F...m python
/dev/nvidia2:        root     kernel mount /dev/nvidia2
                     root      33118 F...m python
/dev/nvidia3:        root     kernel mount /dev/nvidia3
                     root      33118 F...m python
/dev/nvidia4:        root     kernel mount /dev/nvidia4
                     root      33118 F...m python
/dev/nvidiactl:      root     kernel mount /dev/nvidiactl
                     root      33118 F...m python
/dev/nvidia-uvm:     root     kernel mount /dev/nvidia-uvm
                     root      33118 F...m python
/dev/nvidia-uvm-tools:
                     root     kernel mount /dev/nvidia-uvm-tools
```

3. 根据PID关闭进程，解除显存占用:

```bash
kill -9 ***(PID)
```

比如笔者需关闭的进程为`33118`，则执行:<br>

```bash
kill -9 33118
```

## 查看清理后的效果:

输入以下指令查看GPU使用状态:<br>

```bash
nvidia-smi
```

由以下信息可知，GPU显存已经清空，现在我们可以正常运行我们的训练/推理代码了～<br>

```txt
(base) root@5f7d2ce68c26:~/Documents/Llama-Chinese_Custom# nvidia-smi
Wed Mar  6 16:21:35 2024       
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
```

或者，你还有点迷惑你的进程是否真的被清理了，可以运行下列指令检查:<br>

```bash
fuser -v /dev/nvidia*
```

终端效果如下:<br>

```txt
(base) root@5f7d2ce68c26:~/Documents/Llama-Chinese_Custom# fuser -v /dev/nvidia*
Cannot stat file /proc/131/fd/0: Permission denied
Cannot stat file /proc/131/fd/1: Permission denied
Cannot stat file /proc/131/fd/2: Permission denied
Cannot stat file /proc/131/fd/3: Permission denied
Cannot stat file /proc/133/fd/0: Permission denied
Cannot stat file /proc/133/fd/1: Permission denied
Cannot stat file /proc/133/fd/2: Permission denied
Cannot stat file /proc/133/fd/3: Permission denied
Cannot stat file /proc/133/fd/4: Permission denied
Cannot stat file /proc/133/fd/5: Permission denied
Cannot stat file /proc/133/fd/6: Permission denied
Cannot stat file /proc/133/fd/7: Permission denied
Cannot stat file /proc/133/fd/8: Permission denied
                     USER        PID ACCESS COMMAND
/dev/nvidia1:        root     kernel mount /dev/nvidia1
/dev/nvidia2:        root     kernel mount /dev/nvidia2
/dev/nvidia3:        root     kernel mount /dev/nvidia3
/dev/nvidia4:        root     kernel mount /dev/nvidia4
/dev/nvidiactl:      root     kernel mount /dev/nvidiactl
/dev/nvidia-uvm:     root     kernel mount /dev/nvidia-uvm
/dev/nvidia-uvm-tools:
                     root     kernel mount /dev/nvidia-uvm-tools
```
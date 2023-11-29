# Conda安装和虚拟环境创建：
- [Conda安装和虚拟环境创建：](#conda安装和虚拟环境创建)
  - [Anaconda、pip 和 Python的关系：](#anacondapip-和-python的关系)
  - [Ubuntu 18.04.6 LTS安装anaconda：](#ubuntu-18046-lts安装anaconda)
    - [下载ubuntu脚本：](#下载ubuntu脚本)
    - [运行anaconda脚本：](#运行anaconda脚本)
    - [接受协议：](#接受协议)
    - [确认安装位置：](#确认安装位置)
    - [初始化Anaconda（包含环境变量的设置）:](#初始化anaconda包含环境变量的设置)
  - [Conda虚拟环境：](#conda虚拟环境)
    - [创建虚拟环境：](#创建虚拟环境)
      - [conda 创建虚拟环境失败解决方案--关闭网络代理：](#conda-创建虚拟环境失败解决方案--关闭网络代理)
    - [激活虚拟环境：](#激活虚拟环境)
    - [安装和管理软件包：](#安装和管理软件包)
      - [指定库的版本号安装：](#指定库的版本号安装)
      - [同时安装多个库：](#同时安装多个库)
      - [通过requirements.txt安装多个库：](#通过requirementstxt安装多个库)
      - [查看当前虚拟环境的软件包列表：](#查看当前虚拟环境的软件包列表)
      - [查看pip版本：](#查看pip版本)
      - [安装最新版pip:](#安装最新版pip)
      - [pip 查看某个库的版本：](#pip-查看某个库的版本)
    - [切换虚拟环境：](#切换虚拟环境)
    - [安装 jupyter 内核，使系统支持jupyter端环境切换:(可选)](#安装-jupyter-内核使系统支持jupyter端环境切换可选)
      - [安装kernel时可能出现的错误--'jedi'not defined：](#安装kernel时可能出现的错误--jedinot-defined)
    - [退出虚拟环境：](#退出虚拟环境)
    - [克隆环境:](#克隆环境)
    - [删除虚拟环境：](#删除虚拟环境)
  - [conda/pip镜像源设置：](#condapip镜像源设置)
    - [conda镜像源设置：](#conda镜像源设置)
    - [pip镜像源设置：](#pip镜像源设置)
    - [conda镜像源重置：](#conda镜像源重置)
    - [pip镜像源重置：](#pip镜像源重置)


## Anaconda、pip 和 Python的关系：
Anaconda、pip 和 Python 是与 Python 编程语言相关的三个工具或概念，它们之间有一定的关系，但它们的作用和功能有所不同。<br>

1. Python（Python 编程语言）：
   - Python 是一种高级编程语言，广泛用于开发各种类型的应用程序，包括网站、桌面应用程序、数据分析、机器学习、科学计算等等。
   - Python 由一个核心解释器和标准库组成，可以用于执行 Python 代码。

2. pip（Python 包管理器）：
   - pip 是 Python 的包管理器，用于安装、升级和管理 Python 包（也称为模块或库）。Python 包是用于扩展 Python 功能的代码块，它们可以包含函数、类、变量等。
   - pip 可以从 Python 包索引（PyPI）下载和安装第三方 Python 包。它是 Python 生态系统中的标准包管理工具。

3. Anaconda（Python 数据科学平台）：
   - Anaconda 是一个开源的数据科学平台，用于数据科学家和分析师进行数据分析、机器学习和科学计算。
   - Anaconda 包含了 Python 解释器以及大量用于数据科学的包和工具，如 NumPy、Pandas、Matplotlib、scikit-learn 等。
   - Anaconda 还提供了 conda，这是一个包管理器和环境管理器，类似于 pip，但更强大。conda 可以用于创建和管理独立的 Python 环境，以便在同一系统上安装和管理不同版本的 Python 和包。

关系总结：
- Python 是编程语言本身，用于编写和执行代码。
- pip 是 Python 的包管理器，用于安装和管理 Python 包。
- Anaconda 是一个包含 Python 解释器和数据科学相关工具的综合平台，同时提供了 conda 包管理器和环境管理功能，使得数据科学家能够更轻松地配置和管理环境。

🚀🚀🥴🥴通常情况下，工作中都会使用 Anaconda，安装或管理 Python 包可以使用conda(anaconda的缩写)也可以使用pip(部分库只支持pip)。<br>

## Ubuntu 18.04.6 LTS安装anaconda：
### 下载ubuntu脚本：
可使用清华大学镜像或使用anaconda网站，可从清华镜像网查看需要的版本。<br>
清华大学开软软件镜像站：<br>
```log
https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
```
选定需要的conda版本后，可以通过`wget`下载需要的文件。下列指令会将文件下载到当前目录下，如果你想下载到其他位置，请先`cd`到指定位置，或自行搜索`wget`下载到指定位置的指令：<br>
```shell
wget https://repo.anaconda.com/archive/Anaconda3-2023.07-2-Linux-x86_64.sh
```
> 如果下载失败就多试几次，或者可以手动下载~

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/57187acd-b05d-40aa-a75b-9cb2291fa6c6)


下载成功后的样子：<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/5de4d067-9501-4cd1-9296-c6a58fef18cf)

### 运行anaconda脚本：
找到你刚刚下载的 `Anaconda3-2023.07-2-Linux-x86_64.sh`文件所在位置，然后终端运行以下指令即可运行anaconda脚本:<br>
```shell
bash Anaconda3-2023.07-2-Linux-x86_64.sh 
```

### 接受协议：
运行anaconda脚本后，首先让我们审阅安装协议，这里一直按Enter直到出现 `Do you accept the license terms? [yes|no]` ，表示协议阅读完毕输入`yes`即可继续安装。<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/58b9f7ee-1586-4d90-a268-03f5615bccd7)
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/ff077302-acee-451a-a37e-0c00db426f3b)

### 确认安装位置：
输入 Enter 就是选用默认安装路径。<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/37c14bd9-e516-4e2e-be44-8fe0eefa3561)

### 初始化Anaconda（包含环境变量的设置）:
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/2c83fa1b-3a83-4427-a12b-a829781515bf)
现在就已经完成了anaconda的安装了，重启当前界面，终端前显示`(base)`就表明你已经进入了conda环境~<br>

PS：Anaconda安装完成以后出现 "英文提示" 解读<br>
1️⃣For changes to take effect, close and re-open your current shell.<br>
翻译过来就是：关闭当前命令行，并重新打开，刚刚安装和初始化Anaconda设置才可以生效，重新打开一个命令行后直接就进入了conda的base环境。<br>

2️⃣If you'd prefer that conda's base environment not be activated on startup, set the auto_activate_base parameter to false:<br>
翻译过来就是：如果你希望 conda 的基础环境在启动时不被激活，请将 auto_activate_base 参数设置为 false，命令如下：<br>
```shell
conda config --set auto_activate_base false
```
当这一条命令执行完毕后，想要再次进入conda的base环境，只需要使用对应的conda指令即可，如下：<br>
```shell
conda activate base
```

## Conda虚拟环境：
Conda虚拟环境是一种用于管理和隔离Python软件包和其依赖关系的工具。它允许你在同一系统上创建多个独立的Python环境，每个环境都可以具有不同版本的Python解释器和不同的软件包集合。这对于在同一计算机上开发和运行不同项目，每个项目需要不同的Python版本或软件包组合时非常有用。<br>

以下是使用Conda虚拟环境的一般步骤：<br>
### 创建虚拟环境：
使用以下命令创建一个新的Conda虚拟环境，其中`"myenv"`是虚拟环境的名称，你可以自行替换为其他名称：<br>
```shell
conda create --name myenv python=3.8
```
这将创建一个名为`"myenv"`的虚拟环境，并且指定了Python的版本为3.8。你也可以根据需要选择不同的Python版本。<br>

#### conda 创建虚拟环境失败解决方案--关闭网络代理：
> 首先检查在关闭 VPN 情况下重试命令是否可行，若不行则尝试以下方案。

终端输入以下指令，查看是否为proxy的原因：<br>
```shell
env | grep -i "_PROXY"
```
若终端显示类似如下的内容，需要关闭网络代理：<br>
```log
http_proxy=http://127.0.0.1:8118
https_proxy=http://127.0.0.1:8118
```
在终端中依次输入以下内容即可：<br>
指令1:<br>
```shell
unset http_proxy
```
指令2:<br>
```shell
unset https_proxy
```
此时 `conda create` 或 `conda install` 指令就可以使用了，出现这个错误的原因是因为 `conda` 的源在国外，问题出现在网络代理，没有完美的解决方案，只能遇到的时候注意个人科学上网的状态。<br>

### 激活虚拟环境：
激活虚拟环境以开始使用它，不同系统支持的指令方式不同，运行以下两种命令看看自己的系统支持哪一种就选哪一种：<br>
方式一：<br>
```shell
conda activate myenv
```
方式二：<br>
```shell
source activate myenv
```

### 安装和管理软件包：
🚨🚨🚨如果你是第一次接触anaconda，请先学习 `conda/pip镜像源设置` 部分的内容，否则会因为网络原因(互联网墙，懂得都懂)导致指令运行失败。🚨🚨🚨<br>

在虚拟环境中，你可以使用`conda install`命令来安装Python软件包。例如安装`numpy`库：<br>
```shell
conda install numpy
```
当然，也可以使用 `pip install` 的方式安装：<br>
```shell
pip install numpy
```
`conda install`的优势在于不仅会安装指定库，更会安装指定库的相关依赖库，更方便。但有一些库只支持`pip install`安装，这就没办法了，只能一点点安装了～<br>

#### 指定库的版本号安装：
conda和pip可以指定库的版本号进行安装：<br>
```shell
conda install numpy==1.19.5
```
```shell
pip install numpy==1.19.5
```

#### 同时安装多个库：
conda 和 pip 都支持一次性安装多个库。以下是如何使用它们来一次性安装多个库的方法：<br>
使用 conda 安装多个库的形式如下：<br>
```bash
conda install 包名1 包名2 包名3
```

你可以通过在一条命令中列出多个包名来同时安装它们。例如，要安装 NumPy、Pandas 和 Matplotlib，可以运行以下命令：<br>

```bash
conda install numpy pandas matplotlib
```

使用 pip 安装多个库：<br>
```bash
pip install 包名1 包名2 包名3
```

与 conda 类似，如果你想通过 pip 安装 NumPy、Pandas 和 Matplotlib，你可以运行以下命令：<br>
```bash
pip install numpy pandas matplotlib
```

#### 通过requirements.txt安装多个库：
工作中，你经常会看到大家把项目所需要的库写在了 `requirements.txt` 文件中，格式如下：<br>
> 确保每行一个库，如果有特定的版本要求需要指明库的版本号。

```txt
numpy==1.19.5
pandas
matplotlib==3.4.3
```
此时，可通过下方任意一种方式安装对应的库：<br>
```bash
conda install -f requirements.txt
```
```bash
pip install -r requirements.txt
```

#### 查看当前虚拟环境的软件包列表：
虚拟环境中的软件包仅在虚拟环境中可用，不会影响系统的全局Python安装。你可以使用以下指令来查看**当前虚拟环境**中已安装的软件包列表。<br>
```shell
conda list
```
也可以使用`pip`的方式进行查看，两者显示的结果是一样的：<br>
```shell
pip list
```

#### 查看pip版本：
终端运行以下指令：<br>
```shell
pip --version
```

#### 安装最新版pip:
终端运行以下指令：<br>
```shell
pip install --upgrade pip
```

#### pip 查看某个库的版本：
假设你要查询 `pandas` 库的详细信息：<br>
```shell
pip show pandas
```
如果你已经安装了这个库，将显示类似下面的信息：<br>
```txt
(nudge_new) root@iZ2zea5v77oawjy2qxxxxxx:/data/Pytool_Code# pip show pandas
Name: pandas
Version: 1.5.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: The Pandas Development Team
Author-email: pandas-dev@python.org
License: BSD-3-Clause
Location: /root/anaconda3/envs/nudge_new/lib/python3.10/site-packages
Requires: numpy, python-dateutil, pytz
Required-by: 
```
了解详细的信息有时很有用，例如可以根据 `Home-page` 的链接访问原网页，查询该库的更多细节。尤其是对于用户较少的某些库，例如 `snowflake-id`。<br>


### 切换虚拟环境：
你可以在终端输入以下指令查看系统有哪些虚拟环境：<br>
```shell
conda env list
```
效果如下：<br>
> `*` 表示你当前所处的虚拟环境。

```log
(base) root@iZ2zea5v77oawjy2qz7xxxx:/root# conda env list
# conda environments:
#
base                  *  /root/anaconda3
doccano                  /root/anaconda3/envs/doccano
myenv                    /root/anaconda3/envs/myenv
```

现在可以通过激活虚拟环境的指令，切换环境：<br>
```shell
conda activate myenv
```
你的终端状态栏就会变为以下形式:<br>
```shell
(myenv) root@iZ2zea5v77oawjy2qz7xxxx:/root#
```

### 安装 jupyter 内核，使系统支持jupyter端环境切换:(可选)
如果你只想通过终端的方式操作conda虚拟环境，可以跳过此节内容。如果你需要使用`jupyter`，想要在`jupyter`中也能切换虚拟环境，那么这节内容很适合你🥴🥴🥴<br>

想要在`jupyter`中也能切换虚拟环境，首先需要安装`jupyter`内核：<br>
```shell
conda install -c anaconda ipykernel
```
有了`jupyter`内核后，需要为当前虚拟环境创建jupyter环境，使jupyter主界面可以切换`kernel`：<br>
```shell
python -m ipykernel install --user --name=new_env_name
```
注意将 `new_env_name` 替换为你`jupyter`中想要定义的环境名称，建议终端的虚拟环境名称和jupyter的虚拟环境名称对应：<br>

现在，你已经可以在jupyter中切换环境了～<br>

可以通过以下指令查看自己安装的 `kernel` 列表:<br>
```shell
jupyter kernelspec list
```

也可以通过以下指令删除对应的 `kernel`:<br>
```shell
jupyter kernelspec remove kernel_name
```

#### 安装kernel时可能出现的错误--'jedi'not defined：
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/405a0c58-7e5a-4268-83f1-2756c6ec4e06" alt="image" width="50%" height="50%">

问题出在`jedi`的版本问题，终端运行下列指令即可:<br>
```shell
pip install jedi==0.17
```


### 退出虚拟环境：
当你完成虚拟环境中的工作时，可以使用以下命令来退出它：<br>
```shell
conda deactivate
```

### 克隆环境:
工作中，你可能不想要从0搭建一下新环境，此时我们可以克隆某个已存在的环境，在这个环境的基础上进行修改。那么你就可以使用以下指令：<br>
> `old_env_name` 为克隆源，`new_env_name` 为克隆后的环境名称。

```shell
conda create --clone old_env_name --name new_env_name
```

### 删除虚拟环境：
如果你想要删除某个虚拟环境，可以运行以下指令，注意将 `env_name` 替换为你要删除的环境名：<br>
```shell
conda remove -n env_name --all
```

## conda/pip镜像源设置：
由于墙🧱🧱🧱的存在，我们在使用 `conda install` 或 `pip install` 下载我们需要的库时，总是会由于网络原因失败。所以将库的下载链接转向国内镜像源是一个非常好的方式，常见的镜像源有好几种，例如阿里云镜像源、清华镜像源。笔者经常使用的是清华镜像源，这里介绍下清华镜像源的设置方式，如果你想采用其他镜像源，只需要替换对应链接即可～<br>
### conda镜像源设置：
```shell
# 查看镜像源
conda config --show channels
# 添加镜像源
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
# 显示检索路径，每次安装包时会将包源路径显示出来
conda config --set show_channel_urls yes
conda config --set always_yes True
```
### pip镜像源设置：
```shell
# 查看镜像源
pip config list
# 添加镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### conda镜像源重置：
```shell
# 查看镜像源
conda config --show channels
# 重置镜像源
conda config --remove-key channels
```

### pip镜像源重置：
清空/修改 `~/.pip/pip.conf` (没有就创建一个)内容，示例内容如下：<br>
```shell
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
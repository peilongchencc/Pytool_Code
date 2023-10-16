# Python Basci Grammar
介绍 python 基本语法、常见函数的使用与笔者常用的感觉非常方便的python库。<br>
- [Python Basci Grammar](#python-basci-grammar)
  - [python常用库：](#python常用库)
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
  - [python入门：](#python入门)
    - [IDE的选择：](#ide的选择)
    - [第一个代码文件--hello,world:](#第一个代码文件--helloworld)
    - [print()换行控制：](#print换行控制)
  - [python基础数据结构：](#python基础数据结构)
  - [字符串(str):](#字符串str)
    - [创建字符串：](#创建字符串)
    - [字符串索引：](#字符串索引)
    - [字符串切片：](#字符串切片)
    - [字符串长度：](#字符串长度)
    - [字符串拼接：](#字符串拼接)
    - [字符串重复：](#字符串重复)
    - [字符串方法：](#字符串方法)
    - [字符串格式化：](#字符串格式化)
    - [转义字符：](#转义字符)
    - [原始字符串（Raw Strings）：](#原始字符串raw-strings)
    - [字符串比较：](#字符串比较)
    - [字符串查找和替换：](#字符串查找和替换)
    - [多行字符串的处理：](#多行字符串的处理)
      - [隐式换行（不使用反斜杠 `\`）：](#隐式换行不使用反斜杠-)
      - [使用反斜杠 `\` 进行换行：](#使用反斜杠--进行换行)
  - [列表：](#列表)
    - [创建列表：](#创建列表)
    - [列表索引：](#列表索引)
    - [列表切片：](#列表切片)
    - [列表长度：](#列表长度)
    - [列表操作：](#列表操作)
      - [添加元素：](#添加元素)
      - [删除元素：](#删除元素)
        - [del用法拓展：](#del用法拓展)
      - [更新元素：](#更新元素)
      - [合并列表：](#合并列表)
      - [复制列表：](#复制列表)
      - [嵌套列表：](#嵌套列表)
      - [比较列表：](#比较列表)
    - [列表方法：](#列表方法)
      - [`sorted`排序和`sort()`排序：](#sorted排序和sort排序)
      - [`count()`计数：](#count计数)
      - [`reverse()`反转：](#reverse反转)
      - [`index()`获取索引：](#index获取索引)
      - [append()、extend()和加法操作符：](#appendextend和加法操作符)
    - [列表解析：](#列表解析)
  - [元组：](#元组)
    - [创建元组：](#创建元组)
    - [访问元组元素：](#访问元组元素)
    - [切片元组：](#切片元组)
    - [元组的长度和成员检查：](#元组的长度和成员检查)
    - [元组的拼接和复制：](#元组的拼接和复制)
    - [元组的解包（Unpacking）：](#元组的解包unpacking)
  - [字典：](#字典)
    - [创建字典](#创建字典)
    - [访问字典中的值](#访问字典中的值)
      - [使用键来访问字典中的值：](#使用键来访问字典中的值)
      - [使用get()方法来访问字典中的值：](#使用get方法来访问字典中的值)
      - [使用关键字in判断字典中是否存在某个键：](#使用关键字in判断字典中是否存在某个键)
    - [修改字典中的值：](#修改字典中的值)
    - [添加新键值对：](#添加新键值对)
    - [利用函数修改或添加内容到字典中：](#利用函数修改或添加内容到字典中)
    - [利用函数修改或添加内容到字典中(文件版)：](#利用函数修改或添加内容到字典中文件版)
    - [删除键值对：](#删除键值对)
      - [使用del语句：](#使用del语句)
      - [使用pop()方法：](#使用pop方法)
      - [使用popitem()方法删除最后一个键值对：](#使用popitem方法删除最后一个键值对)
      - [使用clear()方法删除所有键值对：](#使用clear方法删除所有键值对)
    - [字典的常用方法:](#字典的常用方法)
      - [`keys()`, `values()`, 和 `items()` 方法:](#keys-values-和-items-方法)
      - [`for` 循环遍历字典:](#for-循环遍历字典)
      - [清空字典--`clear()`:](#清空字典--clear)
    - [字典的嵌套:](#字典的嵌套)
    - [以数字作为字典的key:](#以数字作为字典的key)
    - [字典中\*\*的使用：](#字典中的使用)
  - [python集合：](#python集合)
    - [创建集合并添加元素：](#创建集合并添加元素)
    - [删除集合中的元素：](#删除集合中的元素)
    - [集合的交集、并集和差集操作：](#集合的交集并集和差集操作)
    - [使用`in`操作符检查元素是否在集合中：](#使用in操作符检查元素是否在集合中)
    - [获取集合中的值：](#获取集合中的值)
    - [集合的遍历：](#集合的遍历)
  - [None条件的判断：](#none条件的判断)
  - [python类：](#python类)
    - [python类简单示例：](#python类简单示例)
    - [查看python类的"类属性/方法"和"实例属性"：](#查看python类的类属性方法和实例属性)
    - [修改类属性和实例属性：](#修改类属性和实例属性)
    - [类中调用类内部的方法：](#类中调用类内部的方法)
    - [类中调用类外部的方法：](#类中调用类外部的方法)
    - [不定义\_\_init\_\_创建类：](#不定义__init__创建类)
    - [python类与装饰器：](#python类与装饰器)
      - [@staticmethod：](#staticmethod)
      - [@classmethod:](#classmethod)
    - [python类使用 import 导入时文件顺序解析：](#python类使用-import-导入时文件顺序解析)
    - [`__init__.py`文件的作用和使用方法](#__init__py文件的作用和使用方法)
  - [python类的特殊方法(双"\_"开头)：](#python类的特殊方法双_开头)
    - [`__init__()` 方法：](#__init__-方法)
    - [`__str__()` 方法：](#__str__-方法)
    - [`__repr__()` 方法：](#__repr__-方法)
    - [`__len__()` 方法：](#__len__-方法)
    - [`__getitem__()` 和 `__setitem__()` 方法：](#__getitem__-和-__setitem__-方法)
    - [`__del__()` 方法：](#__del__-方法)
    - [`__call__()` 方法：](#__call__-方法)
    - [`__eq__()` 方法：](#__eq__-方法)
    - [`__dict__`方法：](#__dict__方法)
  - [python的函数语法：](#python的函数语法)
    - [函数的定义：](#函数的定义)
    - [参数类型：](#参数类型)
    - [参数构建原则：](#参数构建原则)
    - [函数调用：](#函数调用)
    - [返回值：](#返回值)
    - [函数的文档字符串：](#函数的文档字符串)
    - [默认参数：](#默认参数)
    - [指定参数数据类型：](#指定参数数据类型)
    - [不定参数：](#不定参数)
      - [不定位置参数 (\*args)：](#不定位置参数-args)
      - [不定关键字参数 (\*\*kwargs)：](#不定关键字参数-kwargs)
    - [函数中定义函数：](#函数中定义函数)
  - [lambda函数：](#lambda函数)
  - [lambda函数进阶(sorted+字典+lambda)：](#lambda函数进阶sorted字典lambda)
  - [python常用内建函数：](#python常用内建函数)
    - [open() 函数：](#open-函数)
    - [read():](#read)
    - [readline():](#readline)
    - [readlines():](#readlines)
    - [join() 函数：](#join-函数)
    - [min():](#min)
    - [isinstance():](#isinstance)
      - [检查对象是否是特定类型：](#检查对象是否是特定类型)
      - [检查对象是否是多个类型之一：](#检查对象是否是多个类型之一)
      - [检查对象是否是某个类的实例-含避坑指南：](#检查对象是否是某个类的实例-含避坑指南)
      - [检查对象是否是某个基本数据类型：](#检查对象是否是某个基本数据类型)
  - [if __name__ == '__main__':的使用：](#if-name--main的使用)

## python常用库：

本内容亦为当前目录下各文件夹目录，如果你还没有一个很好的python基础，请优先阅读其他章节。<br>

库名|作用|备注
---|---|---
flask | Python Web应用程序框架 | 与sanic用处相同，但用户更多。
counter | Python内置计数器 | 
dataclass | 用于创建具有一些默认功能的类的装饰器 | 旨在简化创建用于存储数据的类，本质是装饰器(不常用，仅作为记录)
enum | Python中用于创建和管理枚举类型的库 | 不常用，仅作为记录
loguru | 日志库 | 比python内置的logging方便
request | 用于发送HTTP请求的强大工具 | 允许你轻松地与Web服务交互，包括获取网页内容、发送POST请求、处理Cookies和Headers等
time | 时间处理 | 工作中超级常用
typing | 类型提示和类型注解 | 不常用，仅作为记录


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

## python入门：
### IDE的选择：
以python作为开发语言的程序员，IDE(集成开发环境)的选择一般都是vscode或pycharm。笔者习惯使用的IDE为vscode，没什么特殊的，各有各的优势，仅仅是用习惯了～<br>

安装方式也很简单，网页搜索对应名称下载即可。<br>

### 第一个代码文件--hello,world:
安装了vscode后，新建一个以`.py`为后缀的文件，就可以开始我们的代码之旅了。假设你创建的文件为 `sample.py`，将以下内容复制到你的文件中：<br>
```python
print('hello,world')
```
现在，请在屏幕右下角选择你的python解释器，根据需要选择自己需要的解释器即可～<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/87f42aa3-ff36-4bc9-8c23-6436c09985d1)

终端运行以下指令即可运行`sample.py`文件：<br>
> Tips:终端输入一部分内容后，可以按 `tab` 进行智能填充。

```python
python sample.py
```
此时，你应该可以从终端看到以下内容：<br>
```log
hello,world
```

### print()换行控制：
在Python中，print 函数默认会在打印完内容后自动添加换行符(`\n`)，使下一次打印内容从新的一行开始。如果你想控制 print 函数不换行，可以使用 `end` 参数来指定打印结束时的字符，将其设置为空字符串 `""` 即可。例如：<br>
```python
print("这是一行内容", end="")
print("这是同一行的内容")
print("这是另一行内容")  # 这个print会自动换行
```
终端效果：<br>
```log
这是一行内容这是同一行的内容
这是另一行内容
```
🤭🤭🤭从上述内容我们可以看出，`print()` 其实等效于 `print(end="\n")`。<br>

## python基础数据结构：
数据结构是不同编程语言的操作基础，各种函数，对象都与数据结构密不可分，对基础数据结构的了解是必要的。Python具有多种基础数据结构，这些数据结构用于存储和组织数据。以下是Python中常见的基础数据结构：<br>

1. **整数（int）**：整数是不带小数点的数字，可以是正数、负数或零。例如：`-5`, `0`, `42`。
```python
x = 5
y = -10
result = x + y
print(result)  # 输出: -5
```

2. **浮点数（float）**：浮点数用于表示带有小数点的数字。例如：`3.14`, `2.71828`。
```python
pi = 3.14159
radius = 2.0
area = pi * (radius ** 2)
print(area)  # 输出: 12.56636
```

3. **字符串（str）**：字符串是一系列字符的序列，可以用单引号或双引号括起来。例如：`"Hello, World!"`, `'Python'`。
```python
name = "Alice"
greeting = "Hello, " + name
print(greeting)  # 输出: Hello, Alice
```

4. **列表（list）**：列表是有序的可变序列，可以包含不同类型的元素。列表使用方括号表示。例如：`[1, 2, 3]`, `['apple', 'banana', 'cherry']`。
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)  # 输出: ['apple', 'banana', 'cherry', 'date']
```

5. **元组（tuple）**：元组也是有序的序列，但是与列表不同，元组是不可变的，用圆括号表示。例如：`(1, 2, 3)`, `('red', 'green', 'blue')`。
```python
coordinates = (3, 4)
x, y = coordinates
print("x =", x)  # 输出: x = 3
print("y =", y)  # 输出: y = 4
```

6. **集合（set）**：集合是无序的唯一元素的集合。集合中不允许重复的元素，用大括号或`set()`构造函数表示。例如：`{1, 2, 3}`, `set([2, 2, 3, 4])`。
```python
unique_numbers = {1, 2, 3, 2, 4, 5}
print(unique_numbers)  # 输出: {1, 2, 3, 4, 5}
```

7. **字典（dictionary）**：字典是一种键-值对的映射，用大括号表示。每个键都是唯一的，用于查找相应的值。例如：`{'name': 'Alice', 'age': 30}`。
```python
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person['name'])  # 输出: Alice
print(person['age'])   # 输出: 30
```

8. **布尔值（bool）**：布尔值表示逻辑真或假，只有两个可能的值：`True`和`False`。
```python
is_python_fun = True
is_learning = False
print(is_python_fun)  # 输出: True
print(is_learning)    # 输出: False
```

9.  **None**：`None`是Python中的特殊值，表示空或缺失的数据。
```python
value = None
if value is None:
    print("Value is not set.")
```

这些基础数据结构是Python编程中的基础，开发人员可以使用它们来存储和操作不同类型的数据。 Python还提供了许多内置函数和方法来处理这些数据结构，以满足各种编程需求。<br>

现在暂时简单了解下有这些数据结构就行，后续的内容会让你不断加强对数据结构的认识～🌿🌿🌿<br>


## 字符串(str):
Python 中的字符串是一个非常重要的数据类型，用于存储文本信息。字符串是不可变的，这意味着一旦创建，就不能修改它们的内容🚨🚨🚨。下面是关于 Python 字符串的详细介绍：<br>

### 创建字符串：
你可以使用单引号 `'`、双引号 `"` 或三重引号 `'''` 或 `"""` 来创建字符串。<br>
```python
str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = '''This is a multi-line
string.'''
```

### 字符串索引：
字符串中的每个字符都可以通过索引访问，索引从0开始，负索引表示从字符串末尾向前数。<br>
```python
str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = '''This is a multi-line
string.'''

print(str1[0])  # 输出 'H'
print(str2[-1])  # 输出 'g'
```

### 字符串切片：
你可以使用切片来获取字符串的子串。<br>
```python
str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = '''This is a multi-line
string.'''

substring = str1[0:5]  # 从索引0到4获取子串 'Hello'
```

### 字符串长度：
使用 `len()` 函数获取字符串的长度。<br>
```python
str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = '''This is a multi-line
string.'''

length = len(str1)  # 获取字符串 str1 的长度，结果为 13
```

### 字符串拼接：
你可以使用 `+` 运算符将两个字符串连接起来。<br>
```python
str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = '''This is a multi-line
string.'''

combined_str = str1 + " " + str2  # 将 str1 和 str2 连接为 'Hello, World! Python Programming'
```

### 字符串重复：
使用 `*` 运算符重复一个字符串。<br>
```python
str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = '''This is a multi-line
string.'''

repeated_str = str1 * 3  # 将 str1 重复 3 次，结果为 'Hello, World!Hello, World!Hello, World!'
```

### 字符串方法：
Python 提供了许多字符串方法来操作和处理字符串，例如 `split()`、`join()`、`upper()`、`lower()`、`strip()` 等。这些方法允许你执行各种字符串操作。<br>
```python
str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = '''This is a multi-line
string.'''

words = str2.split()  # 用空格分割字符串，结果为 ['Python', 'Programming']
uppercase_str = str1.upper()  # 将字符串转换为大写，结果为 'HELLO, WORLD!'
```

### 字符串格式化：
使用字符串的 `format()` 方法或 `f-strings`（Python 3.6+）来创建格式化字符串。更推荐 `f-string` 的方式🥴🥴🥴<br>
```python
name = "Alice"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
# 或者使用 f-strings
formatted_str = f"My name is {name} and I am {age} years old."
```

### 转义字符：
可以使用反斜杠 `\` 来转义特殊字符，例如 `\n` 表示换行符，`\t` 表示制表符等。<br>
```python
escaped_str = "This is a line with\na newline character."
```

### 原始字符串（Raw Strings）：
使用 `r` 或 `R` 前缀创建原始字符串，这将禁用转义字符的处理。<br>
```python
raw_str = r"C:\path\to\file.txt"  # 创建原始字符串
```

### 字符串比较：
你可以使用比较运算符（如 `==`、`!=`、`<`、`>`、`<=`、`>=`）来比较字符串。<br>
```python
str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = '''This is a multi-line
string.'''

result = str1 == str2  # 比较两个字符串是否相等
```

### 字符串查找和替换：
使用 `find()`、`index()`、`replace()` 等方法来查找和替换字符串中的子串。<br>
```python
str1 = 'Hello, World!'
str2 = "Python Programming"
str3 = '''This is a multi-line
string.'''

index = str1.find("World")  # 查找子串在字符串中的索引，如果不存在返回 -1
replaced_str = str1.replace("Hello", "Hi")  # 替换字符串中的子串
```

这些是 Python 中字符串的基本用法和操作。字符串在 Python 中非常灵活，你可以使用它们来处理文本数据、格式化输出、解析文本文件等各种任务。希望这个详细的介绍对你有所帮助！<br>

### 多行字符串的处理：
工作中你会遇到大量字符串堆积的情况，此时采用一种合理的方式，在不破坏字符串结构的基础上，将字符串换行显示是一种很好的方式。常见的方式有两种：**隐式换行（不使用反斜杠 `\`）**、**使用反斜杠 `\` 进行换行** <br>

这两种换行方式在Python中都用于多行字符串的处理，但它们在使用和风格上有一些区别，每种方式都有自己的优劣势。<br>

#### 隐式换行（不使用反斜杠 `\`）：
```python
formatted_string = (
    f"Line 1\n"
    f"Line 2\n"
    f"Line 3"
)
```
**优势**：<br>
可读性好：每个字符串段都在自己的行上，易于阅读和维护。<br>
对齐性：属性名称和变量值可以垂直对齐，提高可读性。<br>

**劣势**：<br>
在某些情况下，如果字符串中有大量的换行和缩进，可能会导致代码在编辑器中出现不必要的垂直滚动，降低可见性。<br>

#### 使用反斜杠 `\` 进行换行：
```python
formatted_string = \
    f"Line 1\n" \
    f"Line 2\n" \
    f"Line 3"
```

**优势**：<br>
可以在不引入额外换行的情况下，将字符串段放在一行内，减少代码文件的垂直空间。<br>
在某些情况下，这种方式可能有助于减少代码文件的长度，使代码更紧凑。<br>

**劣势**：<br>
可读性稍差：连续的反斜杠 `\` 可能会使代码不够清晰，阅读起来会稍显困难。<br>
对齐性较差：属性名称和变量值可能无法垂直对齐，降低可读性。<br>

**选择使用哪种方式主要取决于个人偏好和项目的代码风格指南**。一些项目可能更喜欢隐式换行方式，以提高可读性和维护性，而另一些项目可能更注重代码的紧凑性，因此更喜欢使用反斜杠进行换行。<br>

总之，重要的是在整个项目中保持一致的风格，以确保代码的可读性和可维护性。无论你选择哪种方式，都应该遵循项目的代码风格指南和团队的约定。<br>
<br>

## 列表：
Python 中的列表是一种非常常见和有用的数据结构，用于存储一组有序的元素。列表是可变的，这意味着你可以添加、删除和修改其中的元素。下面是关于 Python 列表的详细介绍：<br>

### 创建列表：
你可以使用方括号 `[]` 来创建一个空列表，或者使用方括号包含元素来创建一个包含元素的列表。<br>
```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
```

### 列表索引：
列表中的每个元素都可以通过索引访问，索引从0开始，负索引表示从列表末尾向前数。<br>
```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

print(numbers[0])    # 输出 1
print(fruits[-1])    # 输出 "cherry"
```

### 列表切片：
你可以使用切片来获取列表的子列表，注意：切换的范围为左闭右开，即`numbers[1:4]`表示获取numbers中索义为1到索引为3的值，不包括索引为4的值。<br>
```python
numbers = [1, 2, 3, 4, 5]

sublist = numbers[1:4]      # 获取包含索引 1 到 3 的子列表
print(sublist)              # [2, 3, 4]

sublist2 = numbers[1:4:1]   # 以步长为1，获取包含索引 1 到 3 的子列表
print(sublist2)             # [2, 3, 4]

sublist3 = numbers[1:4:2]   # 以步长为2，获取包含索引 1 到 3 的子列表
print(sublist3)             # [2, 4]

# 逆向取值
sublist4 = numbers[4:1:-1]   # 以步长为1，获取包含索引 4 到 1 的子列表
print(sublist4)             # [5, 4, 3]
```

### 列表长度：
使用 `len()` 函数获取列表的长度。<br>
```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

length = len(numbers)  # 获取列表 numbers 的长度，结果为 5
```

### 列表操作：
列表支持多种操作，包括添加元素、删除元素、更新元素等。<br>

#### 添加元素：
- `append()`：将元素添加到列表的末尾。
- `insert()`：在指定位置插入元素。

```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")  # 在列表末尾添加 "orange"
numbers.insert(2, 99)    # 在索引 2 处插入 99，列表变为 [1, 2, 99, 3, 4, 5]
```

#### 删除元素：
- `remove()`：删除列表中的第一个指定元素。
- `pop()`：删除指定索引处的元素。
- `del` 语句：删除指定索引处的元素或整个列表。

```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

fruits.remove("banana")  # 删除第一个 "banana"
numbers.pop(3)           # 删除索引 3 处的元素，列表变为 [1, 2, 99, 4, 5]
del numbers[0]           # 删除索引 0 处的元素，列表变为 [2, 99, 4, 5]
```

##### del用法拓展：
`del` 可以通过指定要删除的元素的索引，删除列表中的一个或多个元素，。<br>

删除列表中单个元素：<br>
```python
numbers = [1, 2, 3, 4, 5]
del numbers[2]  # 删除列表中索引为 2 的元素，列表变为 [1, 2, 4, 5]
```

删除列表中多个元素：<br>
```python
numbers = [1, 2, 3, 4, 5]
del numbers[1:3]  # 删除列表中索引 1 到 2 的元素，列表变为 [1, 5]
```
‼️‼️‼️Python 不支持直接使用 del 来删除多个不相邻的列表元素，如 `del numbers[2, 4]`。‼️‼️‼️<br>


#### 更新元素：
直接通过索引赋值来更新列表中的元素。<br>
```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

fruits[0] = "grape"  # 将列表中的第一个元素更新为 "grape"
```

#### 合并列表：
使用 `+` 运算符可以将两个列表合并成一个新列表。<br>
```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

combined_list = numbers + [6, 7, 8]  # 合并 numbers 列表和 [6, 7, 8] 到一个新列表
```

#### 复制列表：
列表的复制可以使用切片或 `copy()` 方法。<br>

```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

copied_list = numbers[:]      # 使用切片复制列表
copied_list = numbers.copy()  # 使用 copy() 方法复制列表
```

#### 嵌套列表：
列表可以包含其他列表，形成嵌套结构。<br>
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

#### 比较列表：
你可以使用比较运算符（如 `==`、`!=`、`<`、`>`、`<=`、`>=`）来比较两个列表。<br>
```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

result = numbers == [2, 99, 4, 5]  # 比较两个列表是否相等
```

### 列表方法：
Python 提供了许多有用的列表方法，如 `sort()`、`reverse()`、`count()`、`index()` 等，用于操作和查询列表。<br>

#### `sorted`排序和`sort()`排序：
在Python中，`sorted()` 和 `sort()` 都用于对列表进行排序，但它们的用法略有不同：<br>
- 如果你需要保留原始列表并获得一个已排序的新列表，使用 `sorted()` 函数。
- 如果你想在原始列表上进行排序，改变它的顺序，并且不需要一个新的列表，使用 `list.sort()` 方法。

`sorted`使用示例:<br>
```python
numbers = [4, 1, 5, 3, 2]
sorted_numbers = sorted(numbers)
print(f'numbers的结果为：{numbers}')                        # numbers的结果为：[4, 1, 5, 3, 2]
print(f'numbers经过sorted排序的结果为：{sorted_numbers}')    # numbers经过sorted排序的结果为：[1, 2, 3, 4, 5]
```

`sort`使用示例:<br>
```python
numbers = [4, 1, 5, 3, 2]
numbers.sort()             # 升序排序列表
print(numbers)             # [1, 2, 3, 4, 5]
```

#### `count()`计数：
```python
numbers = [4, 1, 5, 3, 2]
count = numbers.count(3)   # 统计列表中元素 3 的个数
print(count)               # 1
```

#### `reverse()`反转：
```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()           # 反转列表元素的顺序
print(fruits)              # ['cherry', 'banana', 'apple']
```
还可以通过切片的方式反转列表，`[::-1]` 是切片语法，它表示从列表的末尾开始，以步长为-1（逆向）取所有元素，从而实现了列表的反转。<br>
```python
fruits = ["apple", "banana", "cherry"]
reversed_fruits = fruits[::-1]
```

#### `index()`获取索引：
```python
fruits = ["apple", "banana", "cherry"]
index = fruits.index("cherry")  # 查找元素 "cherry" 的索引
print(index)               # 2
```

#### append()、extend()和加法操作符：
`append()` 函数是用于在列表（list）末尾添加单个元素的方法，代码示例如下：<br>

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)      # 输出：[1, 2, 3, 4]
my_list.append(5)
print(my_list)      # 输出：[1, 2, 3, 4, 5]
```

🚨🚨🚨注意：`append()`函数不能一次性传入多个值，每次调用`append()`只能添加一个元素到列表的末尾。类似下列写法会报错：<br>

```python
my_list = [1, 2, 3]
my_list.append(4,5,6)   # 报错：TypeError: list.append() takes exactly one argument (3 given)
print(my_list)
```

如果你想一次性添加多个值到列表，可以考虑使用`extend()`方法或者使用加法操作符`+`来合并多个列表，然后将合并后的列表赋值给目标列表。例如：<br>

使用`extend()`方法：<br>
```python
my_list = [1, 2, 3]
values_to_add = [4, 5, 6]
my_list.extend(values_to_add)
print(my_list)  # 输出 [1, 2, 3, 4, 5, 6]
```

相信你也发现了笔者并没有使用 `my_list.extend(4, 5, 6)` 这种写法，因为这种写法也会报错，同样提示：<br>
```log
TypeError: list.extend() takes exactly one argument (3 given)
```

所以，需要将传入的内容转为list才能使用`extend()`。<br>

使用加法操作符`+`：<br>
```python
my_list = [1, 2, 3]
values_to_add = [4, 5, 6]
my_list += values_to_add
print(my_list)  # 输出 [1, 2, 3, 4, 5, 6]
```

这两种方法允许你一次性添加多个值到列表中。<br>

### 列表解析：
列表解析是一种简洁的方式来创建新的列表，通常通过对现有列表的元素进行变换和筛选来实现。<br>
```python
squares = [x**2 for x in range(1, 6)]  # 创建包含 1 到 5 的平方的列表 [1, 4, 9, 16, 25]
```

Python 列表是非常灵活和强大的数据结构，用于处理和操作一组元素。它们在编程中非常常见，用途广泛。希望这个详细的介绍对你有所帮助！<br>
<br>

## 元组：
Python中的元组（tuple）是一种有序、不可变的数据结构，它允许你存储多个元素，就像列表（list）一样，但与列表不同，元组的内容不可修改‼️‼️‼️。<br>

以下是关于Python元组的详细介绍：<br>

### 创建元组：
你可以使用圆括号来创建元组，可以包含一个或多个元素。例如：<br>
```python
my_tuple = (1, 2, 3)
another_tuple = ('apple', 'banana', 'cherry')
empty_tuple = ()
single_element_tuple = (42,)
```

🔥🔥🔥注意：单个元素的元组需要在元素后面加上逗号，以区分它与一个普通值或表达式的区别。<br>

元组的元素不可修改，这意味着一旦创建，你不能更改、添加或删除元素。如果你尝试修改元组中的元素，会引发`TypeError`。<br>

### 访问元组元素：
你可以使用索引来访问元组中的元素，索引从0开始。例如：<br>
```python
my_tuple = (1, 2, 3)
another_tuple = ('apple', 'banana', 'cherry')

print(my_tuple[0])  # 输出 1
print(another_tuple[2])  # 输出 'cherry'
```

### 切片元组：
你可以使用切片来访问元组的子集。切片的语法是`[start:stop:step]`，其中`start`是起始索引，`stop`是结束索引（不包括该位置的元素），`step`是步长。例如：<br>
```python
my_tuple = (1, 2, 3)
a_slice = my_tuple[1:3]  # 返回一个包含(2, 3)的新元组
```

### 元组的长度和成员检查：
你可以使用内置函数`len()`来获取元组的长度，并使用`in`来检查某个元素是否存在于元组中。例如：

```python
my_tuple = (1, 2, 3)
another_tuple = ('apple', 'banana', 'cherry')

print(len(my_tuple))  # 输出 3
print('apple' in another_tuple)  # 输出 True
```

### 元组的拼接和复制：
你可以通过使用`+`操作符将两个元组拼接在一起，创建一个新的元组。也可以使用`*`操作符复制元组中的元素。例如：<br>
```python
my_tuple = (1, 2, 3)
another_tuple = ('apple', 'banana', 'cherry')

combined_tuple = my_tuple + another_tuple  # 创建一个新元组包含(1, 2, 3, 'apple', 'banana', 'cherry')
repeated_tuple = my_tuple * 3  # 创建一个新元组包含(1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### 元组的解包（Unpacking）：
你可以将元组中的元素解包给多个变量。例如：<br>
```python
my_tuple = (1, 2, 3)

x, y, z = my_tuple  # 将元组中的元素分别赋值给x、y、z变量
```

## 字典：
Python 中的字典允许你存储键值对（key-value pairs），并且可以根据键来快速检索和访问值。字典是可变的（Mutable）和无序的（Unordered），这意味着你可以随时添加、修改和删除键值对，但字典中的元素没有固定的顺序。<br>
> 在 Python 3.7 之前，字典是无序的，这意味着字典中的键值对没有固定的顺序。Python 3.8 开始字典变为有序。

以下是 Python 字典的详细用法和操作：<br>

### 创建字典
可以使用花括号 `{}` 或者内置的 `dict()` 构造函数来创建一个字典。键值对用冒号 `:` 分隔，键与键值对之间用逗号 `,` 分隔。<br>
```python
# 创建一个空字典
my_dict = {}

# 创建一个带有键值对的字典
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# 创建一个字典嵌套字典的结构
my_dict = {'name': 'John', 'age': 30, 'score': {'chinese':87, 'math':99, 'english':92}}
```

### 访问字典中的值

#### 使用键来访问字典中的值：
```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

name = my_dict['name']  # 获取键'name'对应的值
print(name)  # 输出: 'John'
```

#### 使用get()方法来访问字典中的值：
可以使用 `get()` 方法来安全地获取值，如果键不存在，不会抛出异常。<br>
```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

age = my_dict.get('age')  # 获取键'age'对应的值
if age is not None:
    print(age)
```

如果不确定字典中是否有某个key，需要用 `get()` 函数进行判断，不能用 `if item["key_name"]:` 的方式判断，如果字典中没有 `"key_name"` 这个键，使用 `if item["key_name"]:` 运行代码会报错。<br>
```python
data = [{"name":"Tom(汤姆)","score":"640(720)"}, {"name":"Spike(斯派克)"},{"name":"Jerry(杰瑞)","score":"700(720)"}]

for item in data:
    if item.get("score"):
        name = item["name"]
        score = item["score"]
        print(f"{name}的考试成绩为:{score}")    # f-string 不支持 f"...{item["name"]}..." 写法。
    else:
        name = item["name"]
        print(f"没有查询到{name}的考试成绩，TA可能缺考了。")
```

#### 使用关键字in判断字典中是否存在某个键：
可以使用 `in` 操作符来检查键是否存在于字典中。<br>
```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

key_name = 'id'
if key_name in my_dict:
    print(f'my_dict中{key_name}键存在。')
else:
    print(f'my_dict中{key_name}键不存在。')
    
# 终端输出：
# my_dict中id键不存在。
```

### 修改字典中的值：
可以通过赋值操作来修改字典中的值。<br>
```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

my_dict['age'] = 31  # 修改键'age'对应的值为31
```

### 添加新键值对：
可以通过赋值操作来添加新的键值对。<br>
```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

my_dict['country'] = 'USA'  # 添加新的键值对'country': 'USA'
```

### 利用函数修改或添加内容到字典中：

要在函数内部更新字典或向字典添加内容，你可以将字典作为参数传递给函数，并在函数内部进行修改。在Python中，字典是可变对象，所以你可以在函数内部直接修改它，而不需要返回新的字典。以下是一个示例：<br>

```python
# 定义一个字典
my_dict = {'key1': 'value1', 'key2': 'value2'}

# 定义一个函数，该函数接受一个字典作为参数并向其中添加新的键值对
def add_to_dict(input_dict, key, value):
    input_dict[key] = value

# 调用函数以向字典添加新内容
add_to_dict(my_dict, 'key3', 'value3')

# 现在my_dict已经包含了新的键值对
print(my_dict)
```

终端输出：<br>

```
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```

### 利用函数修改或添加内容到字典中(文件版)：

🚨🚨🚨如果你的字典更新函数定义在另一个文件中，你可以按照以下方法传递字典并在函数内部进行修改：<br>

假设你有两个文件：`main.py` 和 `utils.py`，其中 `utils.py` 包含了你的字典更新函数，你可以这样操作：<br>

在 `utils.py` 中定义函数并导入必要的模块：<br>

```python
# utils.py

def update_dict(input_dict, key, value):
    input_dict[key] = value
```

然后，在 `main.py` 中导入 `utils.py` 并使用该函数：<br>

```python
# main.py

# 导入你的模块
from utils import update_dict

# 定义一个字典
my_dict = {'key1': 'value1', 'key2': 'value2'}

# 调用函数以更新字典
update_dict(my_dict, 'key3', 'value3')

# 现在my_dict已经包含了新的键值对
print(my_dict)
```

这样，你可以在不同的文件中定义函数和使用字典，并且函数可以更新字典的内容。确保 `main.py` 和 `utils.py` 位于同一目录中或在Python路径中能够找到。<br>


### 删除键值对：

#### 使用del语句：
```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
del my_dict["key2"]  # 删除键"key2"及其对应的值
```

#### 使用pop()方法：
```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
my_dict.pop("key2")  # 删除键"key2"及其对应的值
print(my_dict)       # {'key1': 'value1', 'key3': 'value3'}
```

请注意，如果要删除一个不存在的键，使用`del`语句或`pop()`方法会引发`KeyError`异常。如果不确定键是否存在，可以使用`pop()`方法的第二个参数来设置默认值，以避免异常。例如：<br>
```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
deleted_value = my_dict.pop("key4", None)  # 如果键"key4"不存在，则返回None，而不会引发异常
print(my_dict)                             # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(deleted_value)                       # None
```

#### 使用popitem()方法删除最后一个键值对：
```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
my_dict.popitem()  # 删除最后一个键值对，返回一个元组
print(my_dict)     # {'key1': 'value1', 'key2': 'value2'}
```

#### 使用clear()方法删除所有键值对：
```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
my_dict.clear()  # 删除所有键值对，字典变为空字典
print(my_dict)   # {}
```

### 字典的常用方法:

#### `keys()`, `values()`, 和 `items()` 方法:

- `keys()`: 返回所有的键。
- `values()`: 返回所有的值。
- `items()`: 返回所有的键值对作为元组。

```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys)  # 输出: dict_keys(['name', 'age', 'country'])
print(values)  # 输出: dict_values(['John', 31, 'USA'])
print(items)  # 输出: dict_items([('name', 'John'), ('age', 31), ('country', 'USA')])
```

#### `for` 循环遍历字典:
可以使用 `for` 循环来遍历字典的键值对。<br>

```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
for key in my_dict:
    print(key, my_dict[key])
```

或者使用 `items()` 方法:<br>
```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

for key, value in my_dict.items():
    print(key, value)
```

#### 清空字典--`clear()`:
可以使用 `clear()` 方法来清空字典。<br>
```python
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

my_dict.clear()  # 清空字典中的所有键值对
```

### 字典的嵌套:
字典可以嵌套在其他字典中，或者嵌套在列表中，以构建更复杂的数据结构。<br>
```python
nested_dict = {
    'person': {'name': 'Alice', 'age': 25},
    'address': {'street': '123 Main St', 'city': 'Some City'}
}

# 访问嵌套字典的值
name = nested_dict['person']['name']  # 获取'person'字典中'name'键对应的值
print(name)  # 输出: 'Alice'
```

### 以数字作为字典的key:
python中字典支持以数字作为键，但不推荐这种写法，毕竟我们也代码要考虑可读性，单纯的数字作为 `key` 自己或同事并不能看出代码的含义。<br>
> 无用的知识又增加了。。。我真不想在工作中见到这种无用的知识。😰😰😰

```python
my_dict = {1: "financial", 2: "sale", 3: "insurance"}    # python中字典支持以数字作为键；
print(my_dict)
print(my_dict[1])    # 调用的时候也以数字的方式调用，如果写为 print(dictionary['1']) 会报错。
print(my_dict[2])
```
<br>

### 字典中**的使用：

在Python中，`**` 运算符的作用有三个：<br>

1. 进行幂运算；
2. 用于在函数调用时将一个字典中的键值对作为关键字参数传递给函数；
3. 用于将一个字典中的键值对合并到另一个字典中。

**1. 幂运算:**

```python
base = 2
exponent = 3    # exponent n. 指数，幂
result = base ** exponent
print(result)   # 8
```

**2. 将字典中的键值对作为关键字参数传递给函数：**

假设你有一个函数 `print_person_info` 接受多个关键字参数，如下所示：<br>

```python
def print_person_info(name, age, city):
    print(f"User_Name: {name}")
    print(f"User_Age: {age}")
    print(f"User_City: {city}")
```

现在，你有一个包含个人信息的字典：<br>

```python
person_info = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
```

你可以使用 `**` 运算符将字典中的键值对传递给函数：<br>

```python
print_person_info(**person_info)
```

这将打印出：<br>

```txt
User_Name: Alice
User_Age: 30
User_City: New York
```

通过 `**` 运算符，字典中的键值对被解包并传递给函数作为关键字参数，这种操作通常用于简化函数调用。<br>

**3. 合并字典：**

你可以使用 `**` 运算符将一个字典中的键值对合并到另一个字典中。例如：<br>

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'd': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)
```

这将创建一个新的字典 `merged_dict` 包含两个字典中的所有键值对：<br>

```txt
{'a': 1, 'b': 3, 'd': 4}
```

🚨🚨🚨请注意，**如果字典之间有重复的键，后面的字典中的值将覆盖前面字典中对应键的值**。这是因为字典是无序的，所以合并的顺序是不确定的。<br>

总之，`**` 运算符在Python中用于在字典中的两个主要用途是将字典解包并传递给函数作为关键字参数，以及合并字典。<br>

**3. 合并字典和键值对：**

合并字典的一个变体就是合并字典和键值对，使用方法类似：<br>

```python
my_data = {
    'intentTags': '',
    'advisorId': 1,
    'labelIds': ''
}
question = "定投"

data = {**my_data, 'question': question}
print(data)
```

终端效果：<br>

```txt
{'intentTags': '', 'advisorId': 1, 'labelIds': '', 'question': '定投'}
```

## python集合：
Python中的集合是一种**无序且不重复**的数据结构。你可以使用 `set` 关键字创建集合，也可以使用大括号 `{}` 来表示。集合中只能包含唯一的元素，重复的元素会被自动去重。你可以向集合添加、删除元素，还可以执行交集、并集、差集等操作。需要注意的是，集合中的元素必须是不可变的，例如数字、字符串、元组等。<br>

### 创建集合并添加元素：
```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # 输出: {1, 2, 3, 4}
```

### 删除集合中的元素：
```python
my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)  # 输出: {1, 2, 4}
```

### 集合的交集、并集和差集操作：
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1 & set2  # 交集
union = set1 | set2  # 并集
difference = set1 - set2  # 差集
print(intersection)  # 输出: {3}
print(union)  # 输出: {1, 2, 3, 4, 5}
print(difference)  # 输出: {1, 2}
```
集合的交集和并集都好理解，我重点讲下差集。集合的差集是指从一个集合中去除另一个集合中的所有元素，返回结果中只包含存在于第一个集合中而不在第二个集合中的元素，所以 `set1 - set2` 和 `set2 - set1` 的结果是不同的。🚨🚨🚨<br>

假设我们有两个集合，`set1` 和 `set2` ，我们可以使用减号（`-`）操作符来计算它们的差集。具体示例如下：<br>
```python
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
difference = set1 - set2
print(difference)  # 输出: {1, 2}
```
在这个例子中，`difference` 集合中包含了 `set1` 中存在，但是在 `set2` 中不存在的元素，即 `1` 和 `2` 。<br>

要注意的是，差集操作是针对第一个集合进行的，它并不考虑第二个集合中的元素。如果需要计算两个集合之间的对称差（也称为对称补集），可以使用异或（`^`）操作符：<br>
```python
symmetric_difference = set1 ^ set2
print(symmetric_difference)  # 输出: {1, 2, 6, 7}
```
在这个例子中，`symmetric_difference` 集合包含了存在于 `set1` 或 `set2` 中但不同时存在于两个集合中的元素，即 `1` 、`2` 、 `6` 和 `7` 。<br>

### 使用`in`操作符检查元素是否在集合中：
```python
my_set = {1, 2, 3}
print(1 in my_set)  # 输出: True
print(4 in my_set)  # 输出: False
```

### 获取集合中的值：
想要获取集合中的值，首先要了解下集合的无序性，以下列代码为例：<br>
```python
res = {'Person', 'Charact'}
print(res)
```
当你执行上述代码，终端返回的结果可能是 `{'Person', 'Charact'}`，也可能是 `{'Charact', 'Person'}`，因为集合是无序的，所以返回内容的顺序是随机的，因此集合是无法使用索引的，使用的时候一定要注意。<br>

在python中，你可以通过以下方式来获取集合（set）中的值：<br>

使用循环遍历集合的每个元素：<br>
```python
my_set = {1, 2, 3, 4, 5}
for value in my_set:
    print(value)
```

转为list再使用索引（不推荐，因为集合是无序的，没有固定的索引，除非你不在乎转换后的元素乱序）：<br>
```python
my_set = {1, 2, 3, 4, 5}
# set转list，但顺序会乱
my_set_2_list = list(my_set)
```

判断一个值是否在集合中，然后进行操作：<br>

```python
my_set = {1, 2, 3, 4, 5}
if 3 in my_set:
    print("3 存在于集合中")
```

确保理解集合是无序且不重复的数据结构，所以不能通过索引来获取值，只能使用遍历或成员判断的方法来操作集合中的值。<br>

### 集合的遍历：
Python中的集合（set）是可迭代的，可以使用循环来遍历集合中的元素。你可以使用for循环来遍历集合中的每个元素，就像遍历列表或其他可迭代对象一样。以下是一个简单的示例：<br>

```python
my_set = {1, 2, 3, 4, 5}

for element in my_set:
    print(element)
```

这段代码将遍历集合`my_set`中的每个元素，并将其打印出来。请注意，集合是无序的，所以元素的顺序可能不同于你添加它们的顺序。如果你需要有序的元素遍历，可以考虑使用有序集合（OrderedSet）或将集合中的元素转换为列表再进行遍历。例如：<br>

```python
my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)

for element in my_list:
    print(element)
```

这将按照元素在集合中的顺序遍历元素。🚨🚨🚨注意：集合转list后不要随便使用索引，因为集合是无序的，转换为list后没有固定的索引，除非你不在乎转换后的元素乱序。<br>
<br>

## None条件的判断：

🚨🚨🚨注意：空的字符串`my_string = ""`，空的列表`my_list = []`，空的集合或字典`my_dict = {}`在进行if条件判断时，并不会被视为None。<br>

示例代码如下：<br>

```python
my_list = []

if my_list is None:
    print("my_list为空")
else:
    print("my_list有值")
```

终端输出：<br>

```log
my_list有值
```

## python类：
在Python中，类是一种用来创建对象的蓝图或模板。它们允许定义对象的属性和方法，从而可以创建多个相似的对象。python类在工作中用处非常多，学习时需要多多注意‼️‼️‼️<br>
### python类简单示例：
先举一个简单的Python类的示例，简单了解下python类的结构：<br>
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make    # 汽车厂商；
        self.model = model  # 汽车型号；
        self.year = year    # 汽车出厂年份；

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
```
在上面的示例中，我们定义了一个名为Car的类。__init__方法是一个特殊的方法，被用来初始化类的实例并设置其属性。在本例中，__init__方法接收make，model和year三个参数，并将它们作为实例的属性进行设置。<br>

start_engine和stop_engine是类的方法，它们用于执行启动和停止引擎的操作。这些方法可以通过类的实例进行调用。<br>

get_info是另一个方法，它返回描述汽车的字符串。注意，方法可以访问实例的属性，例如self.year。<br>

要使用这个类，我们首先需要创建一个类的实例，然后使用实例调用方法。例如：<br>

```python
my_car = Car("Toyota", "Camry", 2020)
my_car.start_engine()
print(my_car.get_info())
my_car.stop_engine()

# 输出：
# Engine started.
# 2020 Toyota Camry
# Engine stopped.
```
代码解释：<br>
以上代码将创建一个名为my_car的Car类的实例。然后，我们调用start_engine方法启动引擎，使用get_info方法获取关于汽车的信息，并最后调用stop_engine方法停止引擎。<br>

### 查看python类的"类属性/方法"和"实例属性"：
工作中，某个方法的返回值可能是一个类，比如 `Node('Person', name='张三')` ，此时如果我们想要的结果是 `Person` ，很多人就会困惑如何获取，正确做法是调用 `dir()` 或 `vars()` 方法进行查看。<br>
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make    # 汽车厂商；
        self.model = model  # 汽车型号；
        self.year = year    # 汽车出厂年份；

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

# 实例化python类
my_car = Car("Toyota", "Camry", 2020)
# 使用dir()查看类的属性和方法
print(dir(my_car))
# 使用vars()查看实例的属性
print(vars(my_car))
# 根据vars()返回的内容，选择我们需要的输出
print(my_car.make)
```
接下来详细罗列下上述代码的返回内容，看到返回的内容，想必你就懂以后遇到python类怎么查看类属性/方法和实例属性了～<br>
上述代码中 `dir()` 返回的内容如下：<br>
```python
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_info', 'make', 'model', 'start_engine', 'stop_engine', 'year']
```
上述代码中 `vars()` 返回的内容如下：<br>
```python
{'make': 'Toyota', 'model': 'Camry', 'year': 2020}
```
回到本节开篇提到的 `Node('Person', name='张三')` 中 `Person` 的获取，正确做法是：`print(vars(Node('Person', name='张三')))` 查看 `Person` 对应的属性名是什么，然后按照属性名打印需要的内容即可。🔥🔥🔥<br>

### 修改类属性和实例属性：
修改Python类的类属性，是为了让其他实例化的类拥有修改后的类属性，修改的方法为：直接访问类属性并进行更改。<br>
```python
class MyClass:
    class_attribute = 0  # 定义类属性
    def __init__(self):
        self.instance_attribute = 0 # 定义实例属性

# 创建两个实例
obj1 = MyClass()
obj2 = MyClass()

# 查看初始类属性值
print(obj1.class_attribute)  # 输出：0
print(obj2.class_attribute)  # 输出：0

# 查看初始实例属性值
print(obj1.instance_attribute)  # 输出：0
print(obj2.instance_attribute)  # 输出：0

# 修改类属性的值
MyClass.class_attribute = 42

# 查看类属性值
print(obj1.class_attribute)  # 输出：42
print(obj2.class_attribute)  # 输出：42

# 修改实例属性的值
obj1.instance_attribute = 42

# 查看实例属性值
print(obj1.instance_attribute)  # 输出：42
print(obj2.instance_attribute)  # 输出：0（不受影响）
```

修改类属性还有高级点的操作，与`classmethod`装饰器结合：<br>
```python
class Sample:
    
    _instances = []

    @classmethod
    def create_instance(cls, data):
        instance = cls()  # 在这里，cls代表Sample类
        instance.data = data
        cls._instances.append(instance)
        return instance

    def display(self):
        print(self.data)

# 使用类方法来创建Sample类的实例
sample1 = Sample.create_instance("Data 1")
sample2 = Sample.create_instance("Data 2")

sample1.display()  # 输出: Data 1
sample2.display()  # 输出: Data 2

sample_instances = Sample._instances
# Sample._instances 其实存储的是两个实例
# 输出为：[<__main__.Sample object at 0x7f03ae9b7e50>, <__main__.Sample object at 0x7f03ae9b7df0>]
# 我们依次遍历这两个实例，然后使用类方法看一下效果～
print(f"Sample._instances中结果：")
for i in sample_instances:
    i.display()

# 终端显示：
# Data 1
# Data 2
# Sample._instances中结果：
# Data 1
# Data 2
```
**代码解释**：<br>
当我们看到 `instance = cls()` 这样的语句，可能初次看起来有点混淆，因为我们通常看到的是类名直接后跟括号来创建实例，比如 `obj = SomeClass()`。但在类方法中，由于我们没有直接的引用类名（并且为了使代码更加通用），我们使用传递给类方法的第一个参数，通常命名为 `cls`，来代表类本身。<br>
在上面的示例中，我们定义了一个名为 `Sample` 的类，它有一个类方法 `create_instance`。这个方法的目的是创建类的实例，并将它添加到类级的列表 `_instances` 中。当我们调用 `create_instance` 方法时，它使用 `cls()` （这里，`cls` 是 `Sample` 类的一个引用）来创建类的一个新实例。<br>

🚨🚨🚨警告、警告🚨🚨🚨
如果你的代码中有序列化或反序列化操作，一定要注意项目代码中是否有进行类属性的修改，如果原项目中进行了类属性的修改，在反序列化时一定要注意加这部分代码加上。(来自笔者血淋淋的教训💦💦💦💦💦💦)
<br>

### 类中调用类内部的方法：
类中调用类内部的方法与调用 **"实例化属性"** 的方法相同，都是加上 self。示例代码如下：<br>
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make    # 车的厂商；
        self.model = model  # 车的型号；
        self.year = year    # 车的出厂年份；

    def start_engine(self):
        print("Engine started.")
        print(self.get_info())      # 调用类内部的get_info方法；

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    
my_car = Car("Toyota", "Camry", 2020)
my_car.start_engine()
my_car.stop_engine()

# 输出：
# Engine started.
# 2020 Toyota Camry
# Engine stopped.
```

### 类中调用类外部的方法：
```python
def slogan():   # 标语；
    print('出入平安')

class Car:
    def __init__(self, make, model, year):
        self.make = make    # 车的厂商；
        self.model = model  # 车的型号；
        self.year = year    # 车的出厂年份；

    def start_engine(self):
        print("Engine started.")
        slogan()

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

# 输出：
# Engine started.
# 出入平安
# 2020 Toyota Camry
# Engine stopped.
```

### 不定义__init__创建类：
Python的类可以不定义__init__函数。当没有定义__init__函数时，Python会自动提供一个默认的构造函数。<br>

默认的构造函数不接受任何参数，并且不执行任何操作。它的存在只是为了创建类的实例对象，使你能够访问类的属性和方法。<br>

下面是一个没有自定义__init__函数的示例：<br>
```python
class MyClass:
    def method(self):   # 虽然没有定义init，但类中的方法第一个参数依旧要为 self。
        print("Hello")

# 创建类的实例
obj = MyClass()         # 尽管没有自定义的__init__函数，但仍然能够使用类和实例对象。

# 调用类的方法
obj.method()            # 输出: hello
```


**🥸拓展：对于python 类，无论是否定义 __init__ 函数，同一个类中 method_A 调用 method_B 的方法是一样的：**<br>
```python
class MyClass:
    def method_A(self):
        # 调用method_B
        self.method_B()
        # 执行其他代码
    
    def method_B(self):
        # 方法B的实现
        pass
```

### python类与装饰器：
这里的装饰器仅罗列：`@staticmethod` 和 `@classmethod` 。<br>
`@staticmethod` 和 `@classmethod` 都能实现 🫥**在不进行实例化的情况下调用类方法。**<br>

#### @staticmethod：
在Python中，@staticmethod装饰器用来声明一个静态方法。静态方法是一个属于类而不是实例的方法，因此它可以在类的所有实例之间共享和访问。<br>

静态方法可以通过类名直接调用，而不需要创建类的实例。这使得静态方法非常适用于执行与类特性或类级别操作相关的任务，而不需要访问实例属性。<br>

下面是一个示例，展示了使用@staticmethod装饰器声明和使用静态方法：<br>

```python
class MathUtils:        # 数学方法
    @staticmethod
    def add(x, y):      # 加法；
        return x + y

result = MathUtils.add(5, 3)
print(result)  # 输出：8
```
需要注意的是，🚨🚨🚨静态方法中不能访问类的属性或实例属性，因为它们与实例无关。静态方法仅与类关联，而不与任何特定实例相关联。<br>

因此，静态方法在一些独立于实例的任务中非常有用，例如辅助函数或实用函数。<br>

🟡请记住，如果你的类既包含静态方法又包含实例方法，那么通常会同时定义 __init__ 方法来初始化实例属性。但对于只包含静态方法的类，可以省略 __init__ 方法的定义。<br>

#### @classmethod:
在Python中，@classmethod是一个装饰器，用于定义类方法。类方法是绑定到类而不是实例的方法。通过@classmethod装饰器，可以在方法上添加一个特殊的标记，告诉Python解释器将该方法视为类方法，而不是实例方法，🫥**这意味着这个方法可以在没有创建类的实例的情况下被调用。**<br>

类方法具有以下特点： 
1. 类方法的第一个参数是类本身，通常被约定为"cls"。 
2. 类方法可以通过类名或实例调用，但实例调用时会自动将对应的类作为第一个参数传递给方法。 
3. 类方法可以访问类的属性和调用其他类方法。
4. 能以多种方式初始化类对象。


下面是一个示例代码，演示了@classmethod的使用：
```python
class MyClass:
    class_attribute = "Hello"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    @classmethod
    def print_class_attribute(cls):
        print(cls.class_attribute)                          # 调用类属性；

    @classmethod
    def create_instance_with_default(cls, default_value="Default"):
        return cls(instance_attribute=default_value)        # 记住，cls等同于类本身，所以这行代码等同于 MyClass(instance_attribute=default_value)。

# 使用 @classmethod
MyClass.print_class_attribute()  # 输出: Hello

instance = MyClass.create_instance_with_default('peilongchencc')
print(instance.instance_attribute)  # 输出: peilongchencc
```

### python类使用 import 导入时文件顺序解析：
项目有入口文件和工具文件之分，我们经常从入口文件引入工具文件中的部分内容，很多人很迷惑import导入文件的流程，这里借助 `jieba` 和 `python类` 梳理一下 `import` 时代码读取流程。<br>
假设我们现在有两个文件 入口文件`main.py` 和 工具文件`tools.py`，具体内容如下：<br>
```python
# tools.py
import time
import jieba
print('This is the start of tools.py')

current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class Segment:
    # 模拟根据用户的登录id、user_name、text，返回附加时间的分词结果。
    def __init__(self,id,name) -> None:
        self.id = id
        self.name = name
        self.date = current_time
    
    def split_words(self,text):
        result = jieba.lcut(text)
        return f'{self.date}：用户{self.id}，{self.name}先生/女士你好，你的分词结果是：{result}'

print('This is the end of tools.py')
```

```python
# main.py
from tools import Segment
text = '长江市市长江大桥。'

# 模拟用户登录
personal_information = Segment('007','peilongchencc')
# 模拟获取到用户输入文本
res = personal_information.split_words(text)    # 执行分词方法
print(res)
```

输出：<br>
```txt
This is the start of tools.py
This is the end of tools.py
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 0.706 seconds.
Prefix dict has been built successfully.
2023-07-28 17:01:32：用户007，peilongchencc先生/女士你好，你的分词结果是：['长江', '市市', '长江大桥', '。']
```
从输出可以看出，`from tools import Segment` 会将导入文件的所有内容都执行一遍，`函数、类`是因为没有调用所以没有执行。当运行到 `personal_information.split_words(text)` 才真正执行了类 `Segment` 中的函数。<br>

笔者讲这个的原因是：希望大家不要随意在工具文件中写可执行内容，很容易重复调用，产生无用的开销。尤其是文件中有 python类，不要在定义类的文件中就把类实例化了。可能有部分人觉得这样便于维护，调用方便(只需要`from ... import ...`)，但这会增加共同维护项目仓库人员的负担，会增大内存、CPU开销，因为只要调用这个文件就会自动实例化一次对应的类。除非这个文件中你只写了一个类，或是专门用于各种类实例化的文件，但这种方式显然不可能。所以最好的方式依旧是在该实例化的地方实例化，至于维护问题，采用 `from config import ...` 这种方式维护即可。 ❌❌❌<br>

### `__init__.py`文件的作用和使用方法
`__init__.py` 文件是 Python 中的一个特殊文件，主要用于标记一个目录是 Python 的模块或包。当你有一个目录，想要将其当作 Python 包来使用时，你需要在该目录下创建一个 `__init__.py` 文件。这样 Python 才会将该目录视为包或模块，否则它只会被视为一个普通的目录。<br>

`__init__.py` 的主要作用和使用方法如下：

1. **标记目录为包或模块**：如上所述，`__init__.py` 的存在使得 Python 认为包含该文件的目录是一个包或模块。

2. **初始化代码**：当你导入一个包时，`__init__.py` 中的代码会自动运行。这对于包的初始化非常有用。例如，你可以在此文件中初始化包级的变量或执行其他启动代码。

3. **包的导入控制**：你可以在 `__init__.py` 中定义 `__all__` 变量，来指定当从包中使用 `from package import *` 时应该导入哪些模块，`__all__` 以”白名单“的形式指明要暴露的接口。

`__all__` 是一个特殊的模块级变量，通常在 `__init__.py` 中定义，但也可以在其他模块中定义。如果没有定义 `__all__`，则 `from package import *` 时默认会导入所有不以下划线 (`_`) 开头的名称🚨🚨🚨。<br>

假设你的文件结构如下：<br>
```log
.
├── mypackage
│   ├── __init__.py
│   ├── module1.py
│   ├── module2.py
│   └── module3.py
└── main.py
```
当你在 `__init__.py` 文件中加入以下代码：<br>
```python
__all__ = ["module1", "module2"]
```
在 `main.py` 文件中使用 `from my_package import *` 时仅可以导入 `module1.py` 和 `module2.py` ：<br>
```python
from my_package import *

fun1 = module1.func()   # 正常引入
fun2 = module2.func()   # 正常引入
fun3 = module3.func()   # 无法引入，会提示 NameError: name 'module3' is not defined. 
```
<br>

**拓展--`__all__`在文件中的使用：**<br>
刚才介绍的是 `__all__` 在 `__init__.py` 文件中的使用，其实 `__all__` 也可以在常规文件中使用，接下来介绍一下 `__all__` 在常规文件中的使用：<br>
假设你的文件结构如下：<br>
```log
.
├── test1.py
├── test2.py
└── main.py
```
`test1.py` 文件内容如下：<br>
```python
#__all__ = ['func']
def func():
    pass
```

`test2.py` 文件内容如下：<br>
```python
import test1

__all__ = ['func2', 'test1']    # 如果 __all__ = ['func2']，则main.py文件中 test1.func() 无法引用。

def func2():
    pass

def func22():
    pass
```

`main.py` 文件内容如下：<br>
```python
from test2 import *

func2()         # 正常引用
test1.func()    # 正常引用
func22()        # 无法引用
```
当运行 `main.py` 时，会发现 `func22()` 无法引用，这就是 `__all__` 白名单的作用。<br>

💢💢💢尽管我在这里讲述了 `__all__` 的用法，但我不得不提示你，一般建议尽量避免使用 `from module_or_package import *` 这种导入方式，因为它可能使代码的来源不清晰，导致后续维护困难。<br>

4. **简化导入**：你可以在 `__init__.py` 中导入包内的模块，这样外部使用包时可以更加简洁。

假设你的文件结构如下：<br>
```log
.
├── mypackage
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
└── main.py
```
如果在 `__init__.py` 中写入以下代码：<br>
```python
from .module1 import func1
from .module2 import func2
```

那么在`main.py`导入时可以直接这样写：<br>
```python
from mypackage import func1, func2
```

而不是：<br>
```python
from mypackage.module1 import func1
from mypackage.module2 import func2
```

5. **提供包的元信息**：你可以在 `__init__.py` 中定义变量如 `__version__` 来提供包的版本信息。

总之，`__init__.py` 文件在 Python 包和模块的设计中扮演了非常关键的角色，它提供了很多灵活的方式来组织和控制你的代码结构。<br>

## python类的特殊方法(双"_"开头)：

Python中的特殊方法（也称为魔术方法或双下划线方法）是具有特定名称和行为的方法，它们在类中定义，用于控制类的一些特殊行为。这些方法通常由Python解释器在特定情况下自动调用，以执行与对象创建、运算符重载、容器操作等相关的操作。特殊方法的名称由双下划线（例如`__init__`）括起来。<br>

以下是一些常见的Python特殊方法及其用途：<br>

1. `__init__(self, ...)`: 构造函数，用于初始化类的实例。
2. `__str__(self)`: 返回一个可打印的字符串表示对象，通过`str(obj)`调用。
3. `__repr__(self)`: 返回一个字符串，用于表示对象的"官方"字符串表示，通过`repr(obj)`调用。
4. `__len__(self)`: 返回对象的长度，通过`len(obj)`调用。
5. `__getitem__(self, key)`: 用于获取对象的元素，通过`obj[key]`调用。
6. `__setitem__(self, key, value)`: 用于设置对象的元素，通过`obj[key] = value`调用。
7. `__delitem__(self, key)`: 用于删除对象的元素，通过`del obj[key]`调用。
8. `__iter__(self)`: 返回一个迭代器对象，通过`iter(obj)`调用，用于迭代对象的元素。
9. `__next__(self)`: 用于迭代器的下一个元素，通过`next(obj)`调用。
10. `__eq__(self, other)`: 用于比较两个对象是否相等，通过`obj == other`调用。
11. `__lt__(self, other)`: 用于比较两个对象是否小于，通过`obj < other`调用。
12. `__gt__(self, other)`: 用于比较两个对象是否大于，通过`obj > other`调用。

这些特殊方法允许你自定义类的行为，使其与Python的内置功能（如运算符、迭代和容器）交互。通过重写这些方法，你可以为自己的类添加自定义行为，使其更加灵活和强大。<br>

接下来，我会讲解工作中经常用到的几个特殊方法：<br>

### `__init__()` 方法：
- 作用：用于对象的初始化。它在创建类的实例时自动调用，允许你为对象的属性设置初始值。
- 示例：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建一个Person类的实例
person = Person("Alice", 30)
```

🌿🌿🌿补充：<br>
如果你使用的是 `from dataclasses import dataclass` 创建的类，你可能需要定义 `__post_init__(self)`，`__post_init__(self)`是 `dataclass` 中的一个特殊方法，当对象初始化后被调用。<br>


### `__str__()` 方法：
- 作用：类似于`__repr__()`方法，用于返回对象的字符串表示。不过，`__str__()`通常用于返回对象的用户友好字符串表示。
- 示例：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

person = Person("Alice", 30)
print(person)  # 输出：Name: Alice, Age: 30
```


### `__repr__()` 方法：
- 作用：用于返回对象的字符串表示。通常用于开发和调试，以便以可读的方式表示对象的内容。
- 示例：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)
print(person)  # 输出：Person(name='Alice', age=30)
```

### `__len__()` 方法：
- 作用：定义对象的长度。通常用于自定义容器类，例如列表、字典等。
- 示例：

```python
class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # 输出：5
```

### `__getitem__()` 和 `__setitem__()` 方法：
- 作用：用于定义对象的索引和赋值操作。通常用于创建自定义容器类，使其支持索引操作。
- 示例：

```python
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[2])  # 输出：3
my_list[2] = 10
print(my_list[2])  # 输出：10
```

### `__del__()` 方法：
- 作用：用于定义对象销毁时的行为。通常不建议使用，因为Python会自动管理对象的垃圾回收。只有在需要进行资源清理时才使用它。
- 示例：

```python
class MyClass:
    def __del__(self):
        print("Object is being destroyed")

obj = MyClass()
del obj  # 在这里对象被销毁
```

### `__call__()` 方法：
- 作用：使对象可以像函数一样被调用。通过定义`__call__()`方法，你可以使对象的实例成为可调用的。
- 示例：

```python
class Adder:
    def __call__(self, x, y):
        return x + y

add = Adder()
result = add(2, 3)
print(result)  # 输出：5
```

### `__eq__()` 方法：
- 作用：用于定义对象的相等性。它在比较两个对象是否相等时自动调用。默认情况下，它比较对象的身份（内存地址），但你可以重写它以根据对象的属性来定义相等性。
- 示例：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

person1 = Person("Alice", 30)
person2 = Person("Alice", 30)

print(person1 == person2)  # 输出：True
```

### `__dict__`方法：
- 作用：用于获取或操作对象的所有属性(包括属性名和值)，而不是直接访问对象的属性。
- 示例：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建一个Person对象
person1 = Person("Alice", 30)

# 使用__dict__属性查看对象的属性字典
print(person1.__dict__)
# 输出: {'name': 'Alice', 'age': 30}

# 使用__dict__属性动态添加属性
person1.__dict__["city"] = "New York"

# 再次使用__dict__属性查看对象的属性字典
print(person1.__dict__)
# 输出: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 使用__dict__属性动态修改属性
person1.__dict__["age"] = 31

# 再次使用__dict__属性查看对象的属性字典
print(person1.__dict__)
# 输出: {'name': 'Alice', 'age': 31, 'city': 'New York'}
```

<br>

## python的函数语法：
函数是一段可重复使用的代码块，它可以接受输入参数，执行一些操作，然后返回结果。在Python中，函数使用`def`关键字来定义，下面是一些关于Python函数的基本用法：<br>

### 函数的定义：
使用`def`关键字来定义函数，后面跟着函数的名称和一对小括号，括号内可以包含参数列表。函数定义的基本语法如下：<br>
```python
def function_name(parameters):
    # 函数体，包含一系列操作
    # 可以使用参数执行操作
    return result  # 可选，如果需要返回结果
```

### 参数类型：
函数可以接受零个或多个参数。参数是在函数调用时传递给函数的值。参数类型有：**位置参数**、**关键字参数**和**默认参数**。<br>

在Python中，位置参数、关键字参数和默认参数是函数参数的不同类型，它们之间有以下关系：<br>

1. 位置参数（Positional Arguments）：
   - 位置参数是函数定义中的参数，它们按照在函数参数列表中的顺序接收传递给函数的值。
   - 调用函数时，必须按照函数定义的顺序传递位置参数的值。

2. 关键字参数（Keyword Arguments）：
   - 关键字参数是通过参数名来传递值的参数，与参数的位置无关。
   - 调用函数时，你可以使用参数名来指定要传递给函数的值，这样可以不考虑参数的位置顺序。

3. 默认参数（Default Arguments）：
   - 默认参数是在函数定义中给参数设置了默认值的参数。
   - 如果调用函数时不提供默认参数的值，函数将使用参数的默认值。
   - 默认参数通常位于参数列表的末尾。

关系总结：<br>
- 位置参数是在函数定义中按顺序声明的参数，必须按照相同的顺序传递值。
- 关键字参数是通过参数名来传递值的，可以在调用函数时以任何顺序使用。
- 默认参数是具有默认值的参数，如果调用函数时不提供值，将使用默认值。默认参数通常与关键字参数一起使用，以提供更多的灵活性。

示例：<br>

```python
def example_function(name, age, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

# 位置参数调用
example_function("Alice", 30)  # Name: Alice, Age: 30, City: Unknown

# 关键字参数调用
example_function(city="New York", age=25, name="Bob")  # Name: Bob, Age: 25, City: New York

# 默认参数调用
example_function("Carol", 35)  # Name: Carol, Age: 35, City: Unknown
```


### 参数构建原则：
在Python中，函数的参数构建遵循以下原则：<br>

1. 位置参数（没有默认值）应该放在参数列表的前面，而默认参数（有默认值）应该放在后面。

2. 默认参数可以有多个，但是它们必须位于参数列表的最后。

这个原则的目的是为了确保函数的调用具有清晰的语法和易于理解的参数传递方式。当你调用一个函数时，你可以只传递位置参数，而省略掉默认参数，或者你可以显式地指定默认参数的值。这种方式使得函数调用更加灵活，并且使得函数的参数使用更加直观。<br>

下面是一个示例，演示了这个原则：<br>

```python
def example_function(name, age, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

# 正确的使用方式
example_function("Alice", 30)                               # 输出：Name: Alice, Age: 30, City: Unknown
example_function("Bob", 25, "New York")                     # 输出：Name: Bob, Age: 25, City: New York
example_function(name="Carol", city="Los Angeles", age=35)  # 输出：Name: Carol, Age: 35, City: Los Angeles

# 错误的使用方式（位置参数放在默认参数后面）
# example_function("Carol", city="Los Angeles", 35)  # 这会导致语法错误，位置参数不能出现在关键字参数之后
```

在上面的示例中，`name` 和 `age` 是位置参数，它们必须在调用时提供值，而 `city` 是默认参数，**可以根据需要省略或显式提供值或采用键值对形式传参**🐳🐳🐳。如果你试图将位置参数放在默认参数后面，会导致语法错误。<br>

### 函数调用：
要调用一个函数，只需使用函数的名称，并传递所需的参数。例如：<br>
```python
result = function_name(arg1, arg2, kwarg1=value1, kwarg2=value2)
```

### 返回值：
函数可以使用`return`语句返回一个值。如果没有`return`语句，函数将返回`None`。<br>
```python
def add(a, b):
    return a + b
```

### 函数的文档字符串：
函数通常应该包含一个文档字符串（docstring），它用于描述函数的用途和参数，以及其他相关信息。它是函数的用户和其他开发者了解函数如何工作的重要来源。<br>

良好的文档字符串可以提高代码的可读性和可维护性。这个文档字符串会在调用`help()`函数时显示出来。<br>

格式约定：Python社区通常采用一种特定的文档字符串格式约定，称为"Google风格"或"reStructuredText风格"。这些约定包括以下部分：<br>
- 函数的简短描述（一行），概括性地描述函数的用途。
- 空行。
- 参数说明，列出每个参数的名称、类型和说明。
- 返回值说明，描述函数的返回值类型和含义。
- 示例用法，提供函数的使用示例。

示例，Google风格的文档字符串：<br>
```python
def calculate_total(price, quantity):
    """Calculate the total cost of items.
    
    Args:
        price (float): The price of a single item.
        quantity (int): The number of items.
    
    Returns:
        float: The total cost of the items.
    """
    total_cost = price * quantity
    return total_cost

help(calculate_total)   # 也可以使用 print(help(calculate_total)) 的形式。
```
终端显示效果：<br>
```log
Help on function calculate_total in module __main__:

calculate_total(price, quantity)
    Calculate the total cost of items.
    
    Args:
        price (float): The price of a single item.
        quantity (int): The number of items.
    
    Returns:
        float: The total cost of the items.
(END)
```
上述内容会自动在一个新的界面显示，可以按字母`q`退出。<br>

### 默认参数：
可以为函数的参数指定默认值，这样在调用函数时如果没有提供该参数，将使用默认值。<br>
```python
def add_numbers(a=5, b=3):
    """计算并返回两个数的和。"""
    result = a + b
    return result

# 调用函数
sum_result = add_numbers()
print(sum_result)  # 输出：8
```

### 指定参数数据类型：
在Python中，通常不需要显式指定函数参数的数据类型，因为Python是一种动态类型语言，它会自动推断参数的类型。这意味着你可以将不同类型的数据传递给函数参数，Python会根据传入的实际数据来执行相应的操作。这种特性称为动态类型检查。<br>

例如，你可以编写一个函数，接受整数、浮点数、字符串或其他数据类型的参数，Python会根据传递的参数执行相应的操作，而不需要显式指定参数的数据类型：<br>

```python
def add(a, b):
    return a + b

result1 = add(3, 5)           # 整数相加，结果是整数 8
result2 = add(3.5, 2.5)       # 浮点数相加，结果是浮点数 6.0
result3 = add("Hello, ", "world")  # 字符串连接，结果是字符串 "Hello, world"
```

虽然Python通常不需要显式指定参数的数据类型，但有时你可能希望在函数内部进行类型检查或处理。你可以使用`isinstance()`函数来检查变量的类型。例如：<br>

```python
def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise ValueError("Both arguments must be numeric.")
```

在这个示例中，函数内部使用`isinstance()`来检查参数 `a` 和 `b` 是否属于整数或浮点数类型，如果不是，则抛出一个值错误。<br>

尽管Python支持动态类型，但有时在文档和代码可读性方面，显式指定函数参数的预期数据类型是一个好习惯。你可以使用函数的文档字符串（docstring）来描述参数的预期类型和用法，以帮助其他开发者理解函数的行为。<br>

请注意，从Python 3.5开始，引入了类型提示（Type Hints）的功能，可以使用类型注解来标注函数参数和返回值的预期类型，这有助于提高代码的可读性和静态类型检查工具的效果。例如：<br>

```python
def add(a: int, b: int) -> int:
    return a + b
```

尽管这些类型提示不会影响运行时的行为，但它们可以在编辑器中提供更好的自动补全和静态类型检查支持。同时，一些工具和IDE（集成开发环境）可以根据这些类型提示提供更好的代码分析和错误检查。<br>

### 不定参数：
Python支持不定数量的位置参数和关键字参数，可以使用不定位置参数`*args`和不定关键字参数`**kwargs`来处理这些参数。<br>

#### 不定位置参数 (*args)：
不定位置参数允许你传递任意数量的位置参数给函数。这些参数将被打包成一个元组（tuple），可以在函数内部进行迭代或处理。<br>

示例：<br>
```python
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3, "hello")
# 输出:
# 1
# 2
# 3
# hello
```
在这个示例中，`*args` 接受了任意数量的位置参数，并在函数内部以元组的形式进行处理。<br>

#### 不定关键字参数 (**kwargs)：
不定关键字参数允许你传递任意数量的关键字参数给函数。这些参数将被打包成一个字典（dictionary），其中关键字是参数名称，对应的值是参数的值。<br>

示例：<br>
```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="New York")
# 输出:
# name: Alice
# age: 30
# city: New York
```
在这个示例中，`**kwargs` 接受了任意数量的关键字参数，并在函数内部以字典的形式进行处理。<br>

使用不定参数可以使函数更加灵活，因为它们允许函数接受不同数量的参数而不需要提前定义固定数量的参数。通常，`*args` 用于不确定数量的位置参数，而 `**kwargs` 用于不确定数量的关键字参数。这对于编写通用函数或包装其他函数时非常有用，因为它们可以适应各种输入情况。<br>

### 函数中定义函数：
python支持在函数内部定义函数，这被称为**内嵌函数或局部函数**。内嵌函数在外部函数的作用域内定义，只能在外部函数内部访问。这可以用于封装某些逻辑或将代码模块化，以便在外部函数中更清晰地组织代码。🌵🌵🌵<br>
示例代码如下：<br>
```python
def outer_function():
    def inner_function():
        print("这是内部函数")
    
    # 调用内部函数
    inner_function()

# 调用外部函数
outer_function()
```
🚨🚨🚨一定要注意，内部函数是无法在外部调用的，除非你采用了返回值的方式。例如下列代码形式的调用会返回 `NameError`。<br>
```python
def outer_function():
    def inner_function():
        print("这是内部函数")
    
    # 调用内部函数
    inner_function()

# 调用外部函数
outer_function()

# 尝试在外部函数之外调用内部函数，将引发 NameError: name 'inner_function' is not defined. 
inner_function()
```

## lambda函数：

在Python中，lambda函数是一种匿名函数，也称为内联函数或lambda表达式。它允许你创建一个简单的函数，而不必使用`def`关键字来定义一个正式的函数。lambda函数通常用于需要一个小而简单的函数的情况，而**不是为了创建复杂的函数**。<br>

lambda函数的基本语法如下：<br>

```python
lambda arguments: expression
```

- `arguments` 是传递给lambda函数的参数，可以是零个或多个参数。
- `expression` 是lambda函数的主体，它包含了对参数的计算和返回结果的表达式。

下面是一些使用lambda函数的示例：<br>

1. 简单的lambda函数，接受两个参数并返回它们的和：

```python
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # 输出 8
```

2. 在列表排序中使用lambda函数：

```python
fruits = [("apple", 5), ("banana", 2), ("cherry", 8)]
fruits.sort(key=lambda x: x[1])  # 根据元组中的第二个元素排序
print(fruits)  # 输出 [('banana', 2), ('apple', 5), ('cherry', 8)]
```

3. 使用lambda函数作为map的参数：

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # 输出 [1, 4, 9, 16, 25]
```

4. 使用lambda函数筛选列表中的元素：

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # 输出 [2, 4, 6, 8]
```

`filter()`函数不常用，这里就不多介绍了。<br>

需要注意的是，lambda函数通常用于简单的操作，如果需要进行复杂的逻辑或包含多行代码的函数，建议使用正式的`def`语句来定义函数。另外，lambda函数的作用域是有限的，通常仅在定义它的地方可见，而不是全局可见的。<br>


## lambda函数进阶(sorted+字典+lambda)：

不只是列表能用sort/sorted，字典也可以结合lambda使用，但需要注意：返回结果的数据类型为list。🚨🚨🚨<br>

```python
my_dict = {'C': 30, 'A': 50, 'B': 40}

sorted_items = sorted(my_dict.items(), key=lambda element: element[1], reverse=True)
print(sorted_items)
```

终端输出：<br>

```log
[('A', 50), ('B', 40), ('C', 30)]
```

代码解释：<br>

lambda 表达式定义了一个函数，它接受一个元组 `element`（表示键值对），例如('C', 30)<br>

`element[0]` 表示返回其中索引为0的元素，也就是字典中的键。<br>

`element[1]` 表示返回其中索引为1的元素，也就是字典中的值。<br>

`reverse=True`: 这部分是一个可选参数，如果设置为 `True`，则表示按降序排序；如果设置为 `False` 或省略，就是按升序排序。<br>


## python常用内建函数：
python一些内建函数非常有用，这里介绍一些笔者常用的python内建函数，笔者常用的python库会在对应的文件夹中介绍，如果需要请自行查看～<br>
### open() 函数：
Python 的内建函数 `open()` 函数用于打开文件，常搭配 `read()`, `readline()` 和 `readlines()` 方法来读取文件内容。<br>

`read()`: 一次性读取所有内容为字符串。可通过添加 `size` 参数控制读取的字节，例如 `file.read(100)` 表示读取前100个字节的内容。<br>
`readline()`: 每次调用，读取文件的下一行。通常用于逐行读取大文件，这样可以不必一次性加载整个文件到内存。<br>
`readlines()`: 读取整个文件并返回一个包含文件每一行的列表。虽然这个方法很方便，但如果文件很大，一次性加载所有行到一个列表可能会消耗大量内存。<br>

现在以读取 `test.txt` 文件为例，讲解三种读取方式的不同。`test.txt`文件内容如下：<br>
```txt
黄鹤楼送孟浩然之广陵
    唐·李白
故人西辞黄鹤楼，烟花三月下扬州。
孤帆远影碧空尽，唯见长江天际流。
```
### read():
```python
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
```
`python read_file.py` 运行结果如下，以😲😲😲字符串形式😲😲😲一次性返回所有内容：<br>
```shell
黄鹤楼送孟浩然之广陵
    唐·李白
故人西辞黄鹤楼，烟花三月下扬州。
孤帆远影碧空尽，唯见长江天际流。
```

### readline():
```python
with open("test.txt", "r") as file:
    line = file.readline()
    while line:                     # 当line存在时，读取下一行
        print(line, end='')         # end='' 用来避免重复的换行
        line = file.readline()
```
`line` 第一次调用 `print` 的结果为 "黄鹤楼送孟浩然之广陵"，`line` 第二次调用 `print` 的结果为 "    唐·李白"，每次返回一行内容。<br>

### readlines():
```python
with open("test.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')  # end='' 用来避免重复的换行
```
`lines` 的结果如下：<br>
```shell
['黄鹤楼送孟浩然之广陵\n', '    唐·李白\n', '故人西辞黄鹤楼，烟花三月下扬州。\n', '孤帆远影碧空尽，唯见长江天际流。']
```
所以要进行 `for循环` 遍历，同时控制 `end` 才能复原数据。<br>
<br>

### join() 函数：
在Python中，`join()` 函数是用于将序列中的元素连接为一个字符串的方法。它可以将一个可迭代对象（比如列表、元组、字符串等）中的元素以🌵**指定的分隔符**🌵连接起来，生成一个新的字符串。<br>

☪️**可迭代对象的要求：** 必须每一项都是字符串类型。如果不是，可以借助列表推导式或 `map()` 函数将每一项元素都转为字符串类型，再执行 `json()` 函数。接下来看几个例子：<br>

将列表中每个元素以 `-` 进行连接，拼接为字符串：<br>
```python
information = ['O', 'l', 'd', ':', '1', '8']
# 分隔符
separator = '-'
result = separator.join(information)
print(result)   # O-l-d-:-1-8
```

不要分隔符，将列表中每个元素进行连接，拼接为字符串：<br>
```python
information = ['O', 'l', 'd', ':', '1', '8']
# 分隔符
separator = ''
result = separator.join(information)
print(result)   # Old:18
```

‼️如果列表中某个元素不是字符串，会报错：<br>
```python
information = ['O', 'l', 'd', ':', 1, '8']
# 分隔符
separator = '-'
result = separator.join(information)
print(result)   # TypeError: sequence item 4: expected str instance, int found
```

可采用列表推导式，先将列表中的每一项转为字符串，再执行 `json` 函数：<br>
```python
information = ['O', 'l', 'd', ':', 1, '8']
# 分隔符
separator = '-'
result = separator.join([str(i) for i in information])
print(result)   # O-l-d-:-1-8
```

也可以采用 `map` 函数：<br>
```python
information = ['O', 'l', 'd', ':', 1, '8']
# 分隔符
separator = '-'
result = separator.join(map(str, information))
print(result)   # O-l-d-:-1-8
```

### min():
`min()` 函数是 Python 中的一个内置函数，它用于找到一组值中的最小值。你可以将多个参数传递给 `min()` 函数，或者传递一个可迭代对象（如列表或元组），然后它会返回其中最小的元素。<br>

以下是 `min()` 函数的用法示例：<br>

1. 传递多个参数：

```python
a = 10
b = 5
c = 15

# 找到最小的值
min_value = min(a, b, c)

print("最小值是:", min_value)  # 输出: 最小值是: 5
```

2. 传递可迭代对象：

```python
numbers = [10, 5, 15, 20, 3]

# 找到列表中的最小值
min_value = min(numbers)

print("最小值是:", min_value)  # 输出: 最小值是: 3
```

`min()` 函数还可以接受一个可选的参数 `key`，它允许你指定一个函数来计算比较的键值。这在需要比较复杂对象时非常有用。例如：<br>

```python
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# 使用 key 参数找到分数最低的学生
min_student = min(students, key=lambda student: student["score"])

print("分数最低的学生是:", min_student["name"])  # 输出: 分数最低的学生是: Charlie
```

上述示例中，`key` 参数指定了一个 lambda 函数，以学生字典中的 "score" 键作为比较依据来找到分数最低的学生。<br>

### isinstance():
`isinstance()` 函数是 Python 中用于检查一个对象是否是某个特定类型或特定类型之一的函数。其语法如下：<br>

```python
isinstance(object, classinfo)
```

- `object`：要检查的对象。
- `classinfo`：可以是一个类型（类或类型）或包含多个类型的元组。如果 `object` 是 `classinfo` 指定的类型之一，函数返回 `True`，否则返回 `False`。

以下是一些 `isinstance()` 函数的示例用法：<br>

#### 检查对象是否是特定类型：

```python
x = 5
if isinstance(x, int):
    print("x 是一个整数")
```

#### 检查对象是否是多个类型之一：

```python
x = 5
if isinstance(x, (int, float)):
    print("x 是整数或浮点数")
```

#### 检查对象是否是某个类的实例-含避坑指南：
```python
class Person:
    pass

person = Person()
if isinstance(person, Person):
    print("person 是 Person 类的实例")
```

🪼🪼🪼重中之重：<br>
`isinstance()` 在检查对象是否是某个类的实例时，不仅与类的定义方式有关，也与类的定义位置有关。举一个极端的例子：<br>

假设有两个不同的文件 `module1.py` 和 `module2.py`，它们都包含一个名为 `MyClass` 的类定义：<br>

```python
# module1.py
class MyClass:
    pass
```

```python
# module2.py
class MyClass:
    pass
```

然后在另一个文件(假设为`main.py`)中，你可以导入这两个模块并使用 `isinstance()` 检查对象是否是这两个类的实例：<br>

```python
# main.py
from module1 import MyClass as MyClass1
from module2 import MyClass as MyClass2

obj1 = MyClass1()
obj2 = MyClass2()

if isinstance(obj1, MyClass1):
    print("obj1 是 module1 中的 MyClass1 的实例")

if isinstance(obj2, MyClass2):
    print("obj2 是 module2 中的 MyClass2 的实例")

if isinstance(obj1, MyClass2):
    print("obj1 是 module2 中的 MyClass2 的实例")
else:
    print("类的定义虽然完全相同，但由于类的导入位置不同，判断结果也不同。")
```

在上述示例中，类的定义完全一样，我们用 `isinstance()` 进行检查，猜猜运行 `main.py` 文件后，终端会显示什么❓❓❓<br>

公布答案，终端显示：<br>
```log
obj1 是 module1 中的 MyClass1 的实例
obj2 是 module2 中的 MyClass2 的实例
类的定义虽然完全相同，但由于类的导入位置不同，判断结果也不同。
```

看到终端显示的内容，想必你就明白了笔者前面所说的话了吧。<br>

再次重申：`isinstance()` 在检查对象是否是某个类的实例时，不仅与类的定义方式有关，也与类的定义位置有关。<br>

Tips: 在同一个项目中，如果你要用到某一个python类，最好的方式一定是导入，而不是将这个类复制到当前文件夹，尤其是当你的项目文件中有 `isinstance()` 进行对象检查的时候。🚨🚨🚨<br>

#### 检查对象是否是某个基本数据类型：
```python
x = 3.14
if isinstance(x, (int, float, str)):
    print("x 是整数、浮点数或字符串")
```

`isinstance()` 函数在编写具有灵活性的代码时非常有用，因为它允许你在不确定对象类型的情况下进行类型检查，从而避免出现类型错误。<br>

## if __name__ == '__main__':的使用：

`if __name__ == '__main__':` 是一个常见的 Python 代码结构，用于确定 Python 脚本是被直接执行还是被作为模块导入到其他脚本中运行的。这个结构通常用于确保某些代码只在脚本直接运行时执行，而不在被导入为模块时执行。<br>

以下是该结构的一些用法和解释：<br>

1. 直接执行脚本：

当你直接执行一个 Python 脚本时，Python 解释器会设置一个特殊的全局变量 `__name__` 为 `'__main__'`。这就意味着，当脚本被直接执行时，`if __name__ == '__main__':` 下面的代码块将被执行。<br>

例如：<br>

```python
# 示例脚本.py
def some_function():
    print("This is a function.")

if __name__ == '__main__':
    print("This is the main block of the script.")
    some_function()
```

当你运行 `python 示例脚本.py` 时，输出将包含 "This is the main block of the script." 和 "This is a function."。<br>

2. 导入为模块时：

如果你将上面的脚本作为一个模块导入到其他脚本中，`if __name__ == '__main__':` 下面的代码块将不会被执行。这允许你将代码组织成模块，并在需要时重用函数、类等定义，而不会立即执行其中的代码。<br>

例如，如果有另一个脚本 `另一个脚本.py`：<br>

```python
# 另一个脚本.py
import 示例脚本

示例脚本.some_function()
```

当你运行 `python 另一个脚本.py` 时，只会执行 `some_function()`，而不会执行示例脚本的主代码块。<br>

这个结构对于编写可重用的模块和测试代码非常有用，因为它允许你将代码分成可执行部分和库部分，并确保库部分不会在导入时执行。这有助于维护代码的可读性和可维护性。<br>
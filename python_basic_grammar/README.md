# Python Basci Grammar
介绍 python 基本语法、常见函数的使用与笔者常用的感觉非常方便的python库。<br>
- [Python Basci Grammar](#python-basci-grammar)
  - [Anaconda、pip 和 Python的关系：](#anacondapip-和-python的关系)
  - [Ubuntu 18.04.6 LTS安装anaconda：](#ubuntu-18046-lts安装anaconda)
    - [下载ubuntu脚本：](#下载ubuntu脚本)
    - [运行anaconda脚本：](#运行anaconda脚本)
    - [接受协议：](#接受协议)
    - [确认安装位置：](#确认安装位置)
    - [初始化Anaconda（包含环境变量的设置）:](#初始化anaconda包含环境变量的设置)
  - [Conda虚拟环境：](#conda虚拟环境)
    - [创建虚拟环境：](#创建虚拟环境)
    - [激活虚拟环境：](#激活虚拟环境)
    - [安装和管理软件包：](#安装和管理软件包)
    - [查看当前虚拟环境的软件包列表：](#查看当前虚拟环境的软件包列表)
      - [pip 查看某个库的版本：](#pip-查看某个库的版本)
    - [切换虚拟环境：](#切换虚拟环境)
    - [安装 jupyter 内核，使系统支持jupyter端环境切换:(可选)](#安装-jupyter-内核使系统支持jupyter端环境切换可选)
      - [安装kernel时可能出现的错误--'jedi'not defined：](#安装kernel时可能出现的错误--jedinot-defined)
    - [退出虚拟环境：](#退出虚拟环境)
    - [克隆环境:](#克隆环境)
    - [删除虚拟环境：](#删除虚拟环境)
  - [字典(dict):](#字典dict)
    - [查看字典中是否有某个key及该key对应的值：](#查看字典中是否有某个key及该key对应的值)
  - [python集合：](#python集合)
    - [创建集合并添加元素：](#创建集合并添加元素)
    - [删除集合中的元素：](#删除集合中的元素)
    - [集合的交集、并集和差集操作：](#集合的交集并集和差集操作)
    - [使用`in`操作符检查元素是否在集合中：](#使用in操作符检查元素是否在集合中)
    - [获取集合中的值：](#获取集合中的值)
  - [python类：](#python类)
    - [python类简单示例：](#python类简单示例)
    - [查看python类的"类属性/方法"和"实例属性"：](#查看python类的类属性方法和实例属性)
    - [类中调用类内部的方法：](#类中调用类内部的方法)
    - [类中调用类外部的方法：](#类中调用类外部的方法)
    - [不定义\_\_init\_\_创建类：](#不定义__init__创建类)
    - [python类与装饰器：](#python类与装饰器)
      - [@staticmethod：](#staticmethod)
      - [@classmethod:](#classmethod)
    - [python类使用 import 导入时文件顺序解析：](#python类使用-import-导入时文件顺序解析)
    - [`__init__.py`文件的作用和使用方法](#__init__py文件的作用和使用方法)
  - [python的函数语法：](#python的函数语法)
    - [函数的定义：](#函数的定义)
    - [参数传递：](#参数传递)
    - [函数调用：](#函数调用)
    - [返回值：](#返回值)
    - [函数的文档字符串：](#函数的文档字符串)
    - [默认参数：](#默认参数)
    - [指定参数数据类型：](#指定参数数据类型)
    - [不定参数：](#不定参数)
      - [不定位置参数 (\*args)：](#不定位置参数-args)
      - [不定关键字参数 (\*\*kwargs)：](#不定关键字参数-kwargs)
    - [函数中定义函数：](#函数中定义函数)
  - [python常用内建函数：](#python常用内建函数)
    - [open() 函数：](#open-函数)
    - [read():](#read)
    - [readline():](#readline)
    - [readlines():](#readlines)
    - [join() 函数：](#join-函数)
  - [常见库解释：](#常见库解释)
    - [flask](#flask)
    - [nginx:](#nginx)
    - [time](#time)

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
翻译过来就是：如果您希望 conda 的基础环境在启动时不被激活，请将 auto_activate_base 参数设置为 false，命令如下：<br>
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

### conda 创建虚拟环境失败解决方案：
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
在虚拟环境中，你可以使用`conda install`命令来安装Python软件包。例如安装`jieba`库：<br>
```shell
conda install jieba
```
当然，也可以使用 `pip install` 的方式安装：<br>
```shell
pip install jieba
```
`conda install`的优势在于不仅会安装指定库，更会安装指定库的相关依赖库，更方便。但有一些库只支持`pip install`安装，这就没办法了，只能一点点安装了～<br>

### 查看当前虚拟环境的软件包列表：
虚拟环境中的软件包仅在虚拟环境中可用，不会影响系统的全局Python安装。你可以使用以下指令来查看**当前虚拟环境**中已安装的软件包列表。<br>
```shell
conda list
```
也可以使用`pip`的方式进行查看，两者显示的结果是一样的：<br>
```shell
pip list
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


## 字典(dict):
python中字典支持以数字作为键，但不推荐这种写法，毕竟我们也代码要考虑可读性，单纯的数字作为 `key` 自己或同事并不能看出代码的含义。<br>
```python
dictionary = {1: "financial", 2: "sale", 3: "insurance"}    # python中字典支持以数字作为键；
print(dictionary)
print(dictionary[1])    # 调用的时候也以数字的方式调用，如果写为 print(dictionary['1']) 会报错。
print(dictionary[2])
```

### 查看字典中是否有某个key及该key对应的值：
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
        return f'{self.date}：用户{self.id}，{self.name}先生/女士您好，您的分词结果是：{result}'

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
2023-07-28 17:01:32：用户007，peilongchencc先生/女士您好，您的分词结果是：['长江', '市市', '长江大桥', '。']
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

总之，`__init__.py` 文件在 Python 包和模块的设计中扮演了非常关键的角色，它提供了很多灵活的方式来组织和控制你的代码结构。
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

### 参数传递：
函数可以接受零个或多个参数。参数是在函数调用时传递给函数的值。有两种类型的参数：**位置参数**和**关键字参数**。<br>
- 位置参数：按照参数在函数定义中的位置传递值。
- 关键字参数：通过参数名称来传递值，这可以使代码更加清晰和可读。


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

## 常见库解释：
### flask
介绍Python Web应用程序框架Flask的安装和使用。<br>

### nginx:
以Nginx在反向代理方面的应用为切入，介绍Nginx的安装和使用。<br>

### time
time库是Python标准库中的一个模块，它提供了处理时间的功能。time 文件夹下是一些常见的time库的用法。<br>
**Ps1**:文章中的时间如果格式化，统一转化为 2022-01-01 12:05:44 形式，原因为：该时间格式可以直接写入mysql，在实际操作中非常方便。<br>
**Ps2**:文章中使用的都是 `time` 模块中的用法，并没有使用利用 `datetime` 等其他时间模块，这样做的好处是：在项目中使用统一的时间获取方式。<br>

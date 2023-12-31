# Vscode Skill
本文记录笔者在使用vscode时所遇到的一些问题和解决方案，希望对大家有帮助。<br>

声明：本文所列快捷键为 MacOs 版，windows用于请自行百度对应快捷键。<br>
- [Vscode Skill](#vscode-skill)
  - [断点调试：](#断点调试)
    - ["Special Variables" 和 "Function Variables"作用解释:](#special-variables-和-function-variables作用解释)
    - [断点调试图标作用解释：](#断点调试图标作用解释)
    - [断点调试中justMyCode的设置：](#断点调试中justmycode的设置)
  - [Vscode的2种Debug方式介绍:](#vscode的2种debug方式介绍)
    - [问题描述:](#问题描述)
    - [问题解答:](#问题解答)
  - [vscode关闭预览模式：](#vscode关闭预览模式)
  - [vscode光标移动--进出函数特别有用：](#vscode光标移动--进出函数特别有用)
  - [vscode跳转到当前文件的指定行：](#vscode跳转到当前文件的指定行)
  - [VScode相对路径无法使用问题：](#vscode相对路径无法使用问题)
    - [相对路径设置后可能引发的根目录问题：](#相对路径设置后可能引发的根目录问题)
  - [vscode查找文件时如何设置排除文件：](#vscode查找文件时如何设置排除文件)
  - [Github中MarkDown文档中所用的目录生成方式：](#github中markdown文档中所用的目录生成方式)

## 断点调试：

### "Special Variables" 和 "Function Variables"作用解释:

1. **Special Variables**: 这通常表示那些在当前上下文中具有特殊意义的变量。例如，如果你正在调试 Python 代码，这里可能会显示像 `__name__`, `__package__` 或者 `__file__` 这样的特殊变量。这些变量通常是由编程语言或环境预定义的，用来表示当前模块或执行环境的特定信息。

2. **Function Variables**: 这些是当前在调试会话中执行的函数内部的局部变量。当你在调试时，如果你的断点在某个函数中，这一区域会显示该函数作用域内的所有变量。它们可能包括函数的参数、在函数内部定义的局部变量等。

### 断点调试图标作用解释：
跳转到对应函数：command + 左键点击函数<br>

返回上一级函数：control + "-"<br>

如果代码嵌套的较深，自己无法找到想看的类，可以采用"跳转到对应函数"，在那个函数任意位置打上断点的方式查看。<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/59d8ec1a-89c4-482b-b894-102686493c14" alt="image" width="50%" height="50%">

`<继续>` 的作用是跳到下一个断点。<br>

### 断点调试中justMyCode的设置：
断点调试时还有一个要注意的点，那就是 `launch.json` 的配置，尤其是其中的 `"justMyCode"` 的取值。<br>

🚨🚨🚨"justMyCode" 的作用是控制调试器是否仅停在你自己编写的代码中，当 `"justMyCode": true` 时，调试器会尽量只在你自己编写的代码中停止，而忽略第三方库或框架的代码。这使得调试过程更加集中在你自己的应用程序逻辑上，而不会在不必要的地方停下来。<br>
> 通常笔者debug时都设置的`"justMyCode": true`～

与之相对的，如果你想要进入第三方库的内部查看细节，需要设置 `"justMyCode": false` 。<br>

`launch.json` 打开方式如下：<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/f61ca852-8cb5-499c-a099-91b0a7640130)


`launch.json` 具体内容如下：<br>

```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: 当前文件",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

<br>


## Vscode的2种Debug方式介绍:

### 问题描述:

vscode有2个地方可以点debug，一个位置是文件右上角的"调试python文件"，另一个位置是点击左侧菜单栏"运行和调试"，然后点击调试按钮。这2个debug有什么区别？<br>

为什么修改`launch.json`文件后，只有第2中debug方式有用，第一种debug方式没用应用这个`launch.json`文件。<br>

### 问题解答:

Visual Studio Code (VSCode) 提供了多种方式来调试代码，包括两种你提到的方法。这两种方式虽然都可以启动调试会话，但它们在使用和配置上有所不同：<br>

1. **文件右上角的"调试Python文件"**：
   - 这是一个快速启动当前打开文件进行调试的方式。
   - 它使用的是默认的调试配置，通常是针对单个文件进行调试。
   - 这种方式通常不会读取`launch.json`文件的配置，因为它是为快速和方便设计的。🫠🫠🫠

2. **点击左侧菜单栏"运行和调试"，然后点击调试按钮**：
   - 这种方式更为复杂和灵活，允许你使用`launch.json`文件中的自定义配置。
   - 通过`launch.json`，你可以设置多种调试参数，如环境变量、命令行参数、程序入口等。
   - 当你修改`launch.json`文件时，这些自定义配置会影响这种调试方式，因为它直接使用这个文件来确定调试的参数和行为。

**为什么修改`launch.json`只影响第二种方式**：<br>

- 当你修改`launch.json`时，只有通过"运行和调试"菜单项启动的调试会话才会读取并应用这些设置。这是因为这种方式专门设计来提供更详细的配置和控制。

- 第一种方式（文件右上角的"调试Python文件"）通常旨在提供一个快速和简单的调试选项，不涉及复杂配置，因此它不会读取`launch.json`文件。🙈🙈🙈

如果你需要使用特定的调试配置或者希望调试一个更复杂的项目（例如涉及多个文件或特殊环境的），推荐使用第二种方式并通过`launch.json`来配置你的调试环境。如果只是想快速调试当前文件，第一种方式可能更方便。<br>


## vscode关闭预览模式：

vscode默认单击文件是"预览"(会覆盖原界面显示的文件)，双击文件才会在旁边打开文件；<br>

解决方式如下：<br>

第一步：点击右下角人物头像，然后点击设置：<br>

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/f28d9ddc-e63d-4c7a-a4c8-8bbeccc4ee11)

第二步：搜索框输入以下内容：<br>

```txt
workbench.editor.enablePrevie
```

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/5b929a41-8379-4239-a95d-1fe1ba71f7f6)


第三步：取消勾选，结束！这样就不需要双击才能不覆盖文件了。<br>
<br>

## vscode光标移动--进出函数特别有用：
移动到上一个位置：control - ，注意不是cmd。<br>

上面那部操作的撤销，cmd u ，这时候使用cmd。<br>
<br>

## vscode跳转到当前文件的指定行：
ctrl + g，然后输入想要跳转的行数并回车。

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/943de8c1-512b-4694-b09a-c0c780817703)

<br>

## VScode相对路径无法使用问题：
问题描述：data.txt 明明就在当前文件夹下，但使用相对路径读取就会报错。<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/3e0dc40a-8968-4066-a796-b94e7342d8c0" alt="image" width="50%" height="50%">

解决方式如下：<br>

第一步：进入<拓展>，找到python解释器，选择python解释器的设置；<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/ca68d830-912f-494e-a509-fa7ce5fecea3" alt="image" width="50%" height="50%">

第二步：勾选如下选项(默认是不勾选的)<br>

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/15cad1df-0c0e-45bd-87ea-09764e05f7af)

重新执行read_file.py查看效果：<br>

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/fa24bc98-b915-4c55-aa59-5504b92e4695)

运行成功！<br>

原因解析：因为vscode对工作区特别敏感，点击右上角的 <运行python文件> 定位其实是工作区，不是当前路径。<br>

### 相对路径设置后可能引发的根目录问题：
相对路径设置后会有根目录识别问题，例如，假设你当前目录生成的目录树如下：<br>

```log
.
├── answer
│   ├── eneities
│   │   └── answer_stem.py
│   └── utils
│       └── answer_sorting.py
├── data_output
│   ├── data_makers
│   │   ├── dimension_data_maker.py
│   │   └── sensitive_data_maker.py
│   └── all_data_output.py
├── README.md
├── requirements.txt
└── main.py
```

`all_data_output.py`中部分代码如下：<br>

```python
from data_output.data_makers.dimension_data_maker import DimensionDataMaker
from answer.eneities.answer_stem import AnswerStem
"""
其他代码省略
"""
```

当你直接在当前目录运行 `all_data_output.py` 时，会被提示以下内容：<br>

```log
ModuleNotFoundError: No module named 'data_output'
```

这是因为vscode将执行文件的父目录当作了根目录，检查方法也很简单，在 `import` 前加入以下代码，然后执行文件就行：<br>

```python
import os

# 获取当前脚本文件的绝对路径
current_script_path = os.path.abspath(__file__)

# 提取根目录
root_directory = os.path.dirname(current_script_path)

print("当前文件的根目录是:", root_directory)
```

终端显示：<br>

```log
当前文件的根目录是:/data/nlp/data_output/
ModuleNotFoundError: No module named 'data_output'
```

现在清楚了吧，当根目录处于 `/data/nlp/data_output/` 又怎么能使用 `from data_output...` 这种导入方式呢。解决方法也很简单，在代码上方添加以下代码，为文件指明根目录即可：<br>

```python
import sys 
sys.path.append("/data/nlp/")
```

现在你的文件应该可以正常运行了，但一定要注意，笔者这里这样改是因为纯粹的想要测试项目底层中的某个文件，而不是把 `all_data_output.py` 当作了主文件，主文件依旧是 `main.py`。<br>

再次提醒：一定要注意代码中可导入和可执行的区别，关键在于根目录的确定.<br>

## vscode查找文件时如何设置排除文件：
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/1360ff80-2ee5-4b9f-8417-7f8dcc11e008" alt="image" width="40%" height="40%">
<br>

## Github中MarkDown文档中所用的目录生成方式：

**起因**：Markdown可以使用`[TOC]`自动生成Markdown文件的标题目录，比如在typora等编辑器，但是Github却不支持`[TOC]`标签，所以在Github上使用`[TOC]`无法正确显示目录，所以需要借助vscode的插件实现目录生成。<br>
1. vscode拓展中搜索 `Markdown All in One`； 
2. 点击安装；
3. 在vscode打开需要生成目录的MarkDown文件，然后将光标定位到要生成目录的地方；
4. 使用快捷键 command+shift+P（windows用户ctrl+shift+P），输入以下内容并回车；

```txt
"Markdown All in One: Create Table of Contents"；
```

Ps:由于github无法自动同步目录，需要在本地 `git pull` 拉取代码，然后 `cmd + s` 保存下代码，此时目录会自动更新。然后 `git push` 上传代码即可。<br>

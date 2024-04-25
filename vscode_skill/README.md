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
  - [让vscode同级只有一个文件夹时不合并为一行:](#让vscode同级只有一个文件夹时不合并为一行)
  - [vscode 突然连接不上服务器了（2024年版本 自动更新从1.85-1.86）:](#vscode-突然连接不上服务器了2024年版本-自动更新从185-186)
    - [问题分析:](#问题分析)
    - [解决方案:](#解决方案)
  - [vscode模板设置:](#vscode模板设置)

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


## 让vscode同级只有一个文件夹时不合并为一行:

这个的问题是关于 Visual Studio Code（VSCode）的文件树视图设置。在VSCode中，默认情况下，如果某个文件夹内只有一个子文件夹，这个子文件夹会与父文件夹合并显示在同一行上。这是为了简化文件树视图。<br>

如果你想关闭这个功能，以便即使只有一个子文件夹时，父文件夹和子文件夹也分别显示在不同的行上，你可以更改设置来实现这一点。<br>

以下是更改设置的步骤：<br>

1. 打开 VSCode。
2. 点击左下角的设置图标（通常是一个齿轮），选择“设置”。
3. 在设置搜索栏中，输入“compact folders”。
4. 找到“Explorer: Compact Folders”选项，这个选项控制是否合并只有一个子元素的文件夹。
5. 取消勾选此选项或将其设置为`false`。

完成以上步骤后，即使文件夹中只有一个子文件夹，文件夹视图也不会合并为一行显示。<br>

图示:<br>

![compact floders](./文件树视图.jpg)


## vscode 突然连接不上服务器了（2024年版本 自动更新从1.85-1.86）:

### 问题分析:

这个问题在于你使用 Visual Studio Code 通过 **SSH连接** 到服务器时遇到了GLIBC版本不匹配的问题，新版 VScode(1.86) 需要的GLIBC版本很高，如果你的远程服务器是 ubuntu 20.04 以下版本，则不支持SSH连接。<br>

### 解决方案:

暂不确定vscode是今后一直不再维护，还是后期会修复。但官方也给出了解决方案:<br>

1. 更新GLIBC版本： 首先，尝试更新你的系统的GLIBC版本。这可能需要你升级你的Linux发行版或手动更新GLIBC。请注意，手动更新GLIBC可能会涉及到系统稳定性的风险，因此请确保你了解你所采取的步骤，并在更新之前备份重要数据。(其实不如直接将 ubuntu 18.04更新到 ubuntu 20.04)

2. 使用适用于你系统版本的Visual Studio Code： 如果你的系统版本无法升级GLIBC，尝试使用Visual Studio Code的旧版本，该版本与你的系统GLIBC版本兼容。你可以在 Visual Studio Code的GitHub Release页面 找到以前的版本。

官方原文：<br>

Can I run VS Code Server on older Linux distributions?(我可以使用较旧的 Linux 发行版运行 VS Code Server 吗？)<br>

Starting with VS Code release 1.86, the minimum requirements for the build toolchain of the remote server were raised. The prebuilt servers distributed by VS Code are compatible with Linux distributions based on glibc 2.28 or later, for example, Debian 10, RHEL 8, Ubuntu 20.04.<br>

从 VS Code 1.86 版本开始，远程服务器的构建工具链的最低要求有所提高。VS Code 分布式预构建的服务器与基于 glibc 2.28 或更高版本的 Linux 发行版兼容，例如 Debian 10、RHEL 8、Ubuntu 20.04。<br>

If your setup does not meet these requirements and you are unable to upgrade the Linux distribution, you can downgrade the VS Code client to version 1.85 to continue using Remote Development. You can downgrade the VS Code client on both desktop and web:<br>

如果您的设置不符合这些要求，并且无法升级 Linux 发行版，您可以降级 VS Code 客户端到 1.85 版本，以继续使用 Remote Development。您可以在桌面和 Web 上降级 VS Code 客户端：<br>

- On desktop, you can download the VS Code release 1.85 from [here](https://code.visualstudio.com/updates/v1_85) . Depending on your platform, make sure to disable updates to stay on that version. A good recommendation is to have release 1.85 as a separate installation, set up with Portable Mode . That way, you won't affect your main desktop VS Code version.

- 在桌面方面，您可以从这里下载 VS Code 1.85 版本。根据您的平台，请确保禁用更新以保持在该版本。一个好的建议是使 1.85 版本作为单独的安装，并设置便携模式。这样，您不会影响您的主要桌面 VS Code 版本。

- On web, you can add the following query argument ?vscode-version=0ee08df0cf4527e40edc9aa28f4b5bd38bbff2b2 to use VS Code release 1.85.

- 在 Web 上，您可以添加以下查询参数 ?vscode-version=0ee08df0cf4527e40edc9aa28f4b5bd38bbff2b2 以使用 VS Code 1.85 版本。

结论:<br>

2024 发布的版本1.86连接有问题，需要将vs版本回退到1.85。<br>

验证:<br>

版本回退到 1.85 后，远程连接正常，并且关闭vscode的自动更新选项。<br>

> 版本回退到 1.85 后，远程连接如果不正常，卸载 `Remote SSH` 然后重新安装即可。

关闭vscode的自动更新选项步骤为:<br>

设置-->搜索框输入 "Auto Check Updates"-->取消勾选<br>

设置-->搜索框输入 "Update: Mode" --> 将 default 改为 none <br>


## vscode模板设置:

笔者在写代码时，习惯每次在文件开头加上文件描述之类的信息，但每创建一个文件就要写一次，就显得有些累了。即使复制、粘贴也会显得有些麻烦。<br>

刚好，VS Code可以通过使用“代码片段”（Snippets）功能来实现自定义的代码模板。你可以创建一个特定语言的代码片段，比如Python文件的代码片段，然后定义你希望自动填充的模板代码。<br>

在VS Code中，你可以按下Ctrl+Shift+P（或者在macOS上按下Cmd+Shift+P）来打开命令面板，然后输入“Configure User Snippets”，选择适合自己的选项来创建或编辑你的代码片段。笔者选择的是 `python.json(Python) 现有的代码片段` 。<br>

```txt
Configure User Snippets
```

创建或编辑完代码片段后，当你在Python文件中输入相应的**触发词**（prefix），比如输入"pybase"，然后按下Tab或Enter键，就会自动展开为你定义的模板代码，以此类推。<br>

其实你还没有完全输入 "pybase" 时，例如你只输入了 "pyb"，vscode就会提示你有 "pybase"，此时直接按下Tab或Enter键，vscode就会自动展开为你定义的模板代码。<br>

你可以根据自己的需要添加更多的代码片段，以便快速生成常用的代码结构。以下是笔者自定义的代码模板，读者可参考使用:<br>

```json
{
	// Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"python template": {
        "prefix": "pybase",
        "body": [
            "\"\"\"",
            "Author: peilongchencc@163.com",
            "Description: ",
            "Requirements: ",
            "Time: $CURRENT_YEAR/$CURRENT_MONTH/$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE:$CURRENT_SECOND",
            "Reference Link: ",
            "Notes: ",
            "\"\"\"",
			"import argparse # import部分不需要写在__main__函数下",
            "",
            "def example(args1,args2):",
            "    result = args1**args2",
			"    return result",
			"",
            "if __name__ == '__main__':",
            "    parser = argparse.ArgumentParser('测试argparse的用法') # 此处的作用仅仅是描述 ",
            "    parser.add_argument('-a','--number_a', default=3, type=int, help='乘法a')",
            "    parser.add_argument('-b','--number_b', default=2, type=int, help='乘法b')",
            "    args = parser.parse_args() # 详细的argparse参数用法需要参考自己写的飞书文档\"argparse的使用模版\"",
            "    # 文档中使用方式为 args.train_file ，传参可以用简写，文档中调用只能用全称。",
            "    # 终端运行方式为： python xxx.py -a=4 --number_b=3",
            "    # 终端传参\"=\"后面不能加空格，必须紧跟。",
			"    result = example(args.number_a,args.number_b)",
			"    print(result)",
        ],
        "description": "python文件基本结构",
    },
	"python head": {
        "prefix": "pyhead",
        "body": [
            "# _*_ coding: utf-8 _*_",
            "# @File_Path    :   $TM_FILEPATH",
            "# @Author  :   chenpeilong",
            "# @Email   :   peilongchencc@163.com",
            "# @Time    :   $CURRENT_YEAR/$CURRENT_MONTH/$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE:$CURRENT_SECOND",
            "#Description:",
        ],
        "description": "python文件表头注释",
    },
	"python def": {
        "prefix": "pydef",
        "body": [
            "def example(args1,args2):\n    \"\"\"\n    核心代码部分：\n    \"\"\"",
			"    return",
        ],
        "description": "python函数结构快速调用",
    },
	"python_def_main": {
        "prefix": "pymain",
        "body": [
            "if __name__ == '__main__':",
        ],
        "description": "__main__的快速调用",
    },
    "gpu_use": {
        "prefix": "pygpu",
        "body": [
            "import os",
            "os.environ['CUDA_VISIBLE_DEVICES'] = '1,3' # 设置gpu索引",
        ],
        "description": "设置gpu索引",
    },
}
```
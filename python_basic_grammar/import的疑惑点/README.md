# import 路径的疑惑点解析

```markdown
project_root/
├── folder_1/
│   ├── a.py
│   └── b.py
├── folder_2/
│   └── c.py
├── folder_3/
│   └── folder_4/
│       └── d.py
└──main.py
```

## vscode 和 pycharm 路径解析的区别:

Visual Studio Code (VSCode) 和 PyCharm 在执行 Python 文件时对路径的处理有一些差异，这可能会影响 `from...import...` 操作的执行。这些差异主要表现在: **工作目录的设置**。<br>

**VSCode:** 默认情况下，VSCode 将文件所在的目录作为工作目录。如果你的项目结构需要从不同的目录中导入模块，你可能需要手动设置工作目录，或者调整你的导入语句以匹配当前的工作目录。(vscode中有设置选项，[点击这里了解详情](https://github.com/peilongchencc/Pytool_Code/tree/d16e3a03824dbc6e7c1b50d5f23a770a270908b0/vscode_skill#vscode%E7%9B%B8%E5%AF%B9%E8%B7%AF%E5%BE%84%E6%97%A0%E6%B3%95%E4%BD%BF%E7%94%A8%E9%97%AE%E9%A2%98))<br>

**PyCharm:** PyCharm 通常设置项目的根目录作为工作目录。这意味着无论你在项目中的哪个位置执行代码，PyCharm 都会假定所有的路径是相对于项目根目录的。<br>


## os 和 sys

```python
import sys
import os

# 获取当前脚本的绝对路径
current_script_path = os.path.abspath(__file__)
print(f"当前脚本的绝对路径为:{current_script_path}")

# 获取当前脚本的父目录
parent_directory = os.path.dirname(current_script_path)
print(f"当前脚本的父目录为:{parent_directory}")

# 获取当前脚本的父目录的父目录
parent_directory_of_the_parent_directory = os.path.dirname(os.path.dirname(current_script_path))
print(f"当前脚本的父目录的父目录为:{parent_directory_of_the_parent_directory}")

# 将这个目录添加到 sys.path
# sys.path.append(parent_directory)

# ... ...
# 你的代码
# ... ...
```
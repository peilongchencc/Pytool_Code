# os 和 sys

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
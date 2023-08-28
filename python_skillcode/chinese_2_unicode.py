######################################################################################################################
# 将data中的中文转义为 Unicode 序列，中文将被转义为 Unicode 转义序列（即类似于 \uXXXX 的形式）
# 这样做的目的是为了确保输出的 JSON 数据可以跨平台和跨系统地使用，因为 Unicode 转义序列在不同的编程语言和操作系统中都能正确地解析和显示。
######################################################################################################################

import json

# 原始数据
data = {"name": "张三","isActive": 'true',"friends": [{"name": "李四","isActive": 'false'}]}

# 将data中的中文转义为 Unicode 序列
formatted_data = json.dumps(data, indent=4, ensure_ascii=True).replace('true', 'True').replace('false', 'False')
print(formatted_data)
print(type(formatted_data))

# 只调整数据格式，不改变中文格式。
# formatted_data = json.dumps(data, indent=4, ensure_ascii=False).replace('true', 'True').replace('false', 'False')
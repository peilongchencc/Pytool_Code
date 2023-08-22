data_name = 'data'

# 定义一个空列表用于存储拼接结果
result = []

# 使用 for 循环遍历生成需要的字符串
for i in range(3):
    # 拼接字符串
    each_data_name = f"{data_name}_{str(i)}"
    # 将生成的字符串添加到结果列表中
    result.append(each_data_name)

# 输出结果列表
for s in result:
    print(s)

# 运行方式：
# python 利用for循环产生的数字和字符串拼接.py                                                                                                                                          ─╯

# 终端输出的结果：
# data_0
# data_1
# data_2
data_name = 'financial_question_metadata_new'

# 定义一个空列表用于存储拼接结果
result = []

# 使用 for 循环遍历生成需要的字符串
for i in range(3):
    # 拼接字符串
    string = data_name + '_' + str(i)
    # 将生成的字符串添加到结果列表中
    result.append(string)

# 输出结果列表
for s in result:
    print(s)

# 运行方式：
# python 字符串拼接.py                                                                                                                                         ─╯

# 终端输出的结果：
# financial_question_metadata_new_0
# financial_question_metadata_new_1
# financial_question_metadata_new_2
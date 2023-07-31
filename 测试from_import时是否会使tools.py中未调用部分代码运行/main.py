from tools import Handler
text = '七分宝的收益如何'

personal_information = Handler('007','peilongchencc')

res = personal_information.handle(text)
print(res)

# 终端输出如下：

# 这里是tools.py文件的开头。
# 这里是tools.py文件的结尾。
# 今天是2023-07-31
# 今天是2023-07-31
# Building prefix dict from the default dictionary ...
# Loading model from cache /var/folders/5q/xc9fb7q90qd75nbksrtqwnz40000gn/T/jieba.cache
# Loading model cost 0.437 seconds.
# Prefix dict has been built successfully.
# 007用户，peilongchencc先生/女士您好，您的分词结果是：['七分', '宝', '的', '收益', '如何']

# 结论：
# from import 操作会使tools.py中未调用到函数的部分也运行。
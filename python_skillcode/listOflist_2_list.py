# 测试将 "列表嵌套列表型数据" 转为列表，哪种方式更快。

data = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
# 第1种方式
res = [item for sublist in data for item in sublist]
print(res)

# 第2种方式
# 逻辑：2个list可以直接通过相加的方式合并到其中一个list。
result = []
for item in data:
    result += item

print(result)
"""
结论：第二种方式更快，第一种用了2个for循环，更耗时。
"""
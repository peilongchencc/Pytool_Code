# Python Basci Grammar
介绍 python 基本语法、常见函数的使用与笔者常用的，感觉非常方便的python库。python 类由于其复杂性，单独创建一个文件夹讲解。<br>

## 字典(dict):
python中字典支持以数字作为键，但不推荐这种写法，毕竟我们也代码要考虑可读性，单纯的数字作为 `key` 自己或同时并不能看出代码的含义。<br>
```python
dictionary = {1: "financial", 2: "sale", 3: "insurance"}    # python中字典支持以数字作为键；
print(dictionary)
print(dictionary[1])    # 调用的时候也以数字的方式调用，如果写为 print(dictionary['1']) 会报错。
print(dictionary[2])
```


## join 函数：
在Python中，`join()` 函数是用于将序列中的元素连接为一个字符串的方法。它可以将一个可迭代对象（比如列表、元组、字符串等）中的元素以🗯️**指定的分隔符**🗯️连接起来，生成一个新的字符串。<br>

☪️**可迭代对象的要求：**☪️ 必须每一项都是字符串类型。如果不是，可以借助列表推导式或 `map()` 函数将每一项元素都转为字符串类型，再执行 `json()` 函数。接下来看几个例子：<br>

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
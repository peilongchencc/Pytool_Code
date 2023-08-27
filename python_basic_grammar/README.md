# Python Basci Grammar
介绍 python 基本语法、常见函数的使用与笔者常用的感觉非常方便的python库。python 类由于其复杂性，单独创建一个文件夹讲解。<br>

## 字典(dict):
python中字典支持以数字作为键，但不推荐这种写法，毕竟我们也代码要考虑可读性，单纯的数字作为 `key` 自己或同时并不能看出代码的含义。<br>
```python
dictionary = {1: "financial", 2: "sale", 3: "insurance"}    # python中字典支持以数字作为键；
print(dictionary)
print(dictionary[1])    # 调用的时候也以数字的方式调用，如果写为 print(dictionary['1']) 会报错。
print(dictionary[2])
```

### 查看字典中是否有某个key及该key对应的值：
如果不确定字典中是否有某个key，需要用 `get()` 函数进行判断，不能用 `if item["key_name"]:` 的方式判断，如果字典中没有 `"key_name"` 这个键，使用 `if item["key_name"]:` 运行代码会报错。<br>
```python
data = [{"name":"Tom(汤姆)","score":"640(720)"}, {"name":"Spike(斯派克)"},{"name":"Jerry(杰瑞)","score":"700(720)"}]

for item in data:
    if item.get("score"):
        name = item["name"]
        score = item["score"]
        print(f"{name}的考试成绩为:{score}")    # f-string 不支持 f"...{item["name"]}..." 写法。
    else:
        name = item["name"]
        print(f"没有查询到{name}的考试成绩，TA可能缺考了。")
```




## join 函数：
在Python中，`join()` 函数是用于将序列中的元素连接为一个字符串的方法。它可以将一个可迭代对象（比如列表、元组、字符串等）中的元素以🌵**指定的分隔符**🌵连接起来，生成一个新的字符串。<br>

☪️**可迭代对象的要求：** 必须每一项都是字符串类型。如果不是，可以借助列表推导式或 `map()` 函数将每一项元素都转为字符串类型，再执行 `json()` 函数。接下来看几个例子：<br>

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

## 常见库解释：
### flask
介绍Python Web应用程序框架Flask的安装和使用。<br>

### nginx:
以Nginx在反向代理方面的应用为切入，介绍Nginx的安装和使用。<br>

### time
time库是Python标准库中的一个模块，它提供了处理时间的功能。time 文件夹下是一些常见的time库的用法。<br>
**Ps1**:文章中的时间如果格式化，统一转化为 2022-01-01 12:05:44 形式，原因为：该时间格式可以直接写入mysql，在实际操作中非常方便。<br>
**Ps2**:文章中使用的都是 `time` 模块中的用法，并没有使用利用 `datetime` 等其他时间模块，这样做的好处是：在项目中使用统一的时间获取方式。<br>
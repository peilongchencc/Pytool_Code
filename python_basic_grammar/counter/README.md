# Counter

python中常说的 `Counter` 指的是`collections.Counter`， 它是 Python 中的一个内置类，用于计数可迭代对象中元素的出现次数。<br>

它提供了一种方便的方式来进行计数统计，通常用于处理列表、字符串、元组等可迭代对象中元素的频率分布。以下是 `collections.Counter` 的一些常见用法：<br>

## 创建一个计数器对象:

`Counter` 可以很方便的计算列表中元素的重复数量，用法如下：<br>

```python
from collections import Counter

my_list = ["香蕉", "葡萄", "葡萄", "荔枝", "荔枝", "荔枝", "菠萝", "菠萝", "菠萝", "菠萝"]
counter = Counter(my_list)
print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '葡萄': 2, '香蕉': 1})
print(type(counter))    # <class 'collections.Counter'>
```

生成的计数器用法与python字典类似，但稍微有一点区别，具体的可以参考本文其他内容~<br>

## 访问元素的计数：

```python
from collections import Counter

my_list = ["香蕉", "葡萄", "葡萄", "荔枝", "荔枝", "荔枝", "菠萝", "菠萝", "菠萝", "菠萝"]
counter = Counter(my_list)
# print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '葡萄': 2, '香蕉': 1})

count = counter["葡萄"] # 如果采用字典中没有的内容，例如counter[2]，会返回0。(不会报错)
print(count)    # 2
```

## 访问所有元素的计数：

```python
from collections import Counter

my_list = ["香蕉", "葡萄", "葡萄", "荔枝", "荔枝", "荔枝", "菠萝", "菠萝", "菠萝", "菠萝"]
counter = Counter(my_list)
# print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '葡萄': 2, '香蕉': 1})

count_vals = counter.values()  # 获取所有元素的计数，返回一个迭代器
print(count_vals)   # dict_values([1, 2, 3, 4])，type为<class 'dict_values'>
print(list(count_vals)) # 可以通过list函数转为[1, 2, 3, 4]，type为<class 'list'>
```

## 获取唯一元素的列表：

```python
from collections import Counter

my_list = ["香蕉", "葡萄", "葡萄", "荔枝", "荔枝", "荔枝", "菠萝", "菠萝", "菠萝", "菠萝"]
counter = Counter(my_list)
# print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '葡萄': 2, '香蕉': 1})

count_keys = counter.keys()
print(count_keys)   # dict_keys(['香蕉', '葡萄', '荔枝', '菠萝'])，type为<class 'dict_keys'>
print(list(count_keys)) # 可以通过list函数转为['香蕉', '葡萄', '荔枝', '菠萝']，type为<class 'list'>
```

## 获取最常见的元素及其计数：

```python
from collections import Counter

my_list = ["香蕉", "葡萄", "葡萄", "荔枝", "荔枝", "荔枝", "菠萝", "菠萝", "菠萝", "菠萝"]
counter = Counter(my_list)
# print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '葡萄': 2, '香蕉': 1})

most_common = counter.most_common(2)  # 获取出现频率最高的前两个元素及其计数
print(most_common)  # [('菠萝', 4), ('荔枝', 3)]，type为<class 'list'>
```
# Counter

python中常说的 `Counter` 指的是`collections.Counter`， 它是 Python 中的一个内置类，用于计数可迭代对象中元素的出现次数。<br>

它提供了一种方便的方式来进行计数统计，通常用于处理列表、字符串、元组等可迭代对象中元素的频率分布。以下是 `collections.Counter` 的一些常见用法：<br>

- [Counter](#counter)
  - [创建一个计数器对象:](#创建一个计数器对象)
  - [访问计数器中某个元素的计数：](#访问计数器中某个元素的计数)
  - [访问计数器中所有元素的计数：](#访问计数器中所有元素的计数)
  - [获取计数器中唯一元素(keys)的列表：](#获取计数器中唯一元素keys的列表)
  - [获取最常见的元素(keys)及其计数：](#获取最常见的元素keys及其计数)
  - [更新计数器：](#更新计数器)
  - [删除计数器中某个元素及其计数：](#删除计数器中某个元素及其计数)
  - [清空计数器：](#清空计数器)
  - [性能问题：](#性能问题)

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

## 访问计数器中某个元素的计数：

```python
from collections import Counter

my_list = ["香蕉", "葡萄", "葡萄", "荔枝", "荔枝", "荔枝", "菠萝", "菠萝", "菠萝", "菠萝"]
counter = Counter(my_list)
# print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '葡萄': 2, '香蕉': 1})

count = counter["葡萄"] # 如果采用字典中没有的内容，例如counter[2]，会返回0。(不会报错)
print(count)    # 2
```

## 访问计数器中所有元素的计数：

```python
from collections import Counter

my_list = ["香蕉", "葡萄", "葡萄", "荔枝", "荔枝", "荔枝", "菠萝", "菠萝", "菠萝", "菠萝"]
counter = Counter(my_list)
# print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '葡萄': 2, '香蕉': 1})

count_vals = counter.values()  # 获取所有元素的计数，返回一个迭代器
print(count_vals)   # dict_values([1, 2, 3, 4])，type为<class 'dict_values'>
print(list(count_vals)) # 可以通过list函数转为[1, 2, 3, 4]，type为<class 'list'>
```

## 获取计数器中唯一元素(keys)的列表：

```python
from collections import Counter

my_list = ["香蕉", "葡萄", "葡萄", "荔枝", "荔枝", "荔枝", "菠萝", "菠萝", "菠萝", "菠萝"]
counter = Counter(my_list)
# print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '葡萄': 2, '香蕉': 1})

count_keys = counter.keys()
print(count_keys)   # dict_keys(['香蕉', '葡萄', '荔枝', '菠萝'])，type为<class 'dict_keys'>
print(list(count_keys)) # 可以通过list函数转为['香蕉', '葡萄', '荔枝', '菠萝']，type为<class 'list'>
```

## 获取最常见的元素(keys)及其计数：

假设你想要获取出现频率最高的前两个元素及其计数，可以使用以下代码：<br>

```python
from collections import Counter

my_list = ["香蕉", "葡萄", "葡萄", "荔枝", "荔枝", "荔枝", "菠萝", "菠萝", "菠萝", "菠萝"]
counter = Counter(my_list)
# print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '葡萄': 2, '香蕉': 1})

most_common = counter.most_common(2)  # 获取出现频率最高的前两个元素及其计数
print(most_common)  # [('菠萝', 4), ('荔枝', 3)]，type为<class 'list'>
```

## 更新计数器：

如果想要更新计数器中的内容，需要使用 `update` 方法。你可以创建另一个计数器对象，然后使用 `update` 方法将其合并到原始计数器中。以下是如何使用 `update` 更新你的计数器的示例：<br>

```python
from collections import Counter

my_list = ["香蕉", "葡萄", "葡萄", "荔枝", "荔枝", "荔枝", "菠萝", "菠萝", "菠萝", "菠萝"]
counter = Counter(my_list)
print("初始计数器:")
print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '葡萄': 2, '香蕉': 1})

# 创建另一个计数器
other_counter = Counter(["苹果", "苹果", "香蕉", "橙子", "橙子", "橙子"])

print("另一个计数器:")
print(other_counter)    # Counter({'橙子': 3, '苹果': 2, '香蕉': 1})

# 使用update方法合并两个计数器
counter.update(other_counter)   # 相同键的计数会相加

print("更新后的计数器:")
print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '橙子': 3, '香蕉': 2, '葡萄': 2, '苹果': 2})
```

使用 `update` 方法后，结果依旧是一个 `Counter` 对象，依旧可以使用之前介绍的计数器方法。<br>

## 删除计数器中某个元素及其计数：

```python
del counter["香蕉"]
print("执行删除后的计数器:")
print(counter)  # Counter({'菠萝': 4, '荔枝': 3, '橙子': 3, '葡萄': 2, '苹果': 2})
```

## 清空计数器：

```python
counter.clear()  # 清空计数器中的所有元素
print("执行清空后的计数器:")
print(counter)  # Counter()
```

## 性能问题：

🚨🚨🚨虽然 `Counter` 是一个很方便的工具，但在处理非常大的数据集时，性能可能会成为问题。如果你需要处理大规模数据集，可能需要考虑其他高性能的数据结构和算法。<br>
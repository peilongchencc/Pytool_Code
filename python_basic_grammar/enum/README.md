# enum
`enum` 是Python中用于创建和管理枚举类型的库，枚举是一种用于表示有限离散值集合的数据类型，它可以让你以更可读和可维护的方式处理常量值。<br>
😀😀😀注意：枚举的成员可以是任何Python对象，包括字符串、元组、自定义对象等。<br>

- [enum](#enum)
  - [`Enum` 类：](#enum-类)
  - [`unique` 装饰器：](#unique-装饰器)

`enum`由 `Enum` 和 `unique` 两部分组成，接下来具体讲讲这两部分的用法：<br>

## `Enum` 类：
`Enum` 是一个基类，你可以继承它来创建自定义的枚举类型。<br>

它允许你定义一组具有唯一标识符的常量值。这些常量值在枚举类型中是有序的，你可以使用它们来表示一组相关的选项或状态。<br>

例如，你可以创建一个表示星期几的枚举：<br>
```python
from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# 使用枚举成员
today = Weekday.WEDNESDAY

# 迭代枚举成员
for day in Weekday:
    print(day)

# 检查值是否是枚举成员
if today == Weekday.WEDNESDAY:
    print("It's Wednesday!")
```
🫠🫠🫠很陌生吧，类竟然可以遍历，但这就是枚举，这就是`Enum`。接下来，我们再多看几个例子～<br>

例如，你可以创建一个颜色枚举来表示不同的颜色：<br>

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
print(Color.GREEN.value)  # 输出: 2
```

然后，你可以通过 `Color.RED`、`Color.GREEN` 和 `Color.BLUE` 来引用这些颜色。<br>

也可以通过以下方式创建：<br>
```python
from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

print(Color.GREEN.value)  # 输出: "green"
```

`enum`可以和类配合使用：<br>
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

from enum import Enum

class People(Enum):
    JOHN = Person("John", 30)
    ALICE = Person("Alice", 25)

print(People.JOHN.value.name)  # 输出: "John"
print(People.ALICE.value.age)   # 输出: 25
```

## `unique` 装饰器：
讲完了 `Enum`，我们再来看一下 `unique` 的用法。`unique` 装饰器用于确保枚举成员的值是唯一的。<br>

如果两个枚举成员具有相同的键，Python会引发`TypeError`。如果两个枚举成员具有相同的值，Python会引发 `ValueError`。通常，我们更常用于判断是否有相同值，毕竟python字典是允许有相同值的，这和 `unique` 是有区别的。<br>

依旧是 `Enum` 中用到的例子：<br>

```python
from enum import Enum, unique

@unique
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
```

在这个示例中，使用 `@unique` 装饰器确保了每个工作日的值是唯一的。<br>

你可以试一下，如果出现了相同的键，终端运行是否会出现`TypeError`。如果出现了相同的值，终端运行是否会出现 `ValueError`。<br>

枚举类型可以使代码更具可读性和可维护性，因为它们允许你以有意义的方式表示常量值，并且不允许值的重复出现。这在需要处理一组预定义选项或状态时非常有用。<br>
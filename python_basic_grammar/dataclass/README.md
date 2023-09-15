# dataclass
在Python中，`dataclass`是一个用于创建具有一些默认功能的类的装饰器。它是Python 3.7及更高版本的标准库中的一部分，旨在简化创建用于存储数据的类。使用`dataclass`可以自动为类生成特殊方法，如`__init__()`、`__repr__()`、`__eq__()`等，这些方法通常需要手动编写。<br>

`dataclass`使得定义包含大量属性的类变得更加简单和清晰。它特别适用于那些主要用于存储数据的简单类，因为它可以自动生成许多繁琐的代码，同时也提高了代码的可读性。<br>
- [dataclass](#dataclass)
  - [简单示例：](#简单示例)
  - [常规类如何改为dataclass类：](#常规类如何改为dataclass类)
  - [dataclass中的类属性和实例属性：](#dataclass中的类属性和实例属性)
  - [@dataclass(frozen=True)的作用：](#dataclassfrozentrue的作用)
  - [`__init__`与`__post_init__` 用法解析：](#__init__与__post_init__-用法解析)


## 简单示例：
以下是一个简单的示例，展示如何使用`dataclass`创建一个包含属性的类：<br>

```python

from dataclasses import dataclass

@dataclass
class MyClass:
    field1: int
    field2: str

# __init__()方法的体现：
obj1 = MyClass(42, "Hello")
obj2 = MyClass(42, "Hello")
obj3 = MyClass(66, "Come on")
print(obj1.field1)  # 输出: 42
print(obj1.field2)  # 输出: 'Hello'

print(obj2.field1)  # 输出: 42
print(obj2.field2)  # 输出: 'Hello'

print(obj3.field1)  # 输出: 66
print(obj3.field2)  # 输出: 'Come on'

# __repr__()方法的体现
print(obj1)  # 输出: MyClass(field1=42, field2='Hello')
print(obj2)  # 输出: MyClass(field1=42, field2='Hello')
print(obj3)  # 输出: MyClass(field1=66, field2='Come on')


# __eq__()方法的体现
print(obj1 == obj2)  # 输出: True
print(obj1 == obj3)  # 输出: False
print(obj2 == obj3)  # 输出: False
```

在这个示例中，我们定义了一个名为 `MyClass` 的数据类，它有两个字段 `field1` 和 `field2`，分别表示整数和字符串类型的数据。由于 `dataclass` 会自动生成`__init__()`、`__repr__()`和`__eq__()`等方法，所以我们可以直接调用这些方法。<br>

💦💦💦当然，这有个前提，你需要知道这些特殊方法是怎么用的🥴🥴🥴如果你不知道，建议先大概浏览下笔者所写的python基础中的python类特殊方法模块。<br>
<br>

## 常规类如何改为dataclass类：
先看一下常规类的写法，然后我们把这个类改为 `dataclass` 形式：<br>
```python
class Car:
    only_one = False        # 是否只有一辆
    def __init__(self, make="Unknown", model="Unknown", year=0):
        self.make = make    # 汽车厂商；
        self.model = model  # 汽车型号；
        self.year = year    # 汽车出厂年份；

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
```

要将该类改为`dataclass`形式，首先需要导入`dataclasses`模块，并使用`@dataclass`装饰器来标记类。然后，可以去掉`__init__`方法，并使用`@dataclass`的参数来定义类的字段。以下是改进后的代码：<br>

```python
from dataclasses import dataclass

@dataclass
class Car:
    only_one: bool = False  # 是否只有一辆
    make: str = "Unknown"   # 汽车厂商
    model: str = "Unknown"  # 汽车型号
    year: int = 0           # 汽车出厂年份

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
```

在上面的代码中，我们使用`@dataclass`装饰器来标记`Car`类，并使用`dataclass`的参数来定义类的字段。这样，Python会自动为我们生成`__init__`方法和其他常见的特殊方法，以及`__repr__`方法用于对象的字符串表示。现在，我们可以创建`Car`对象，初始化字段，以及使用其他方法，就像之前的版本一样，但现在它更具有Pythonic的风格。<br>

🥶🥶🥶相信你已经注意到了，类属性和实例属性混到一起了。不用质疑，这个写法是正确的。在使用`dataclass`定义类时，你只需要在类的主体部分声明类属性🔥🔥🔥，不需要显式定义实例属性。`dataclass`会为你自动生成`__init__()`方法并将类属性变成实例属性🚨🚨🚨。<br>


## dataclass中的类属性和实例属性：
由于`dataclass`将类属性与实例属性混合，所以在调用的时候稍微有一点点不同。<br>

常规情况下，如果没有进行类的实例化，是无法调用实例属性的，只能调用类属性，代码如下：<br>

```python
class Car:
    only_one = False        # 是否只有一辆
    def __init__(self, make="Unknown", model="Unknown", year=0):
        self.make = make    # 汽车厂商；
        self.model = model  # 汽车型号；
        self.year = year    # 汽车出厂年份；

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

# 未实例化
print(Car.only_one) # 输出：False
print(Car.year)     # 输出：AttributeError: type object 'Car' has no attribute 'year'
```

但由于`dataclass`将类属性与实例属性混合，所以我们在没有进行实例化前，也能调用对应的值。当然，前提是你已经设置了默认值。<br>

```python
from dataclasses import dataclass

@dataclass
class Car:
    make: str = "Unknown"
    model: str = "Unknown"
    year: int = 0
    only_one = False

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

# 未实例化
print(Car.only_one) # 输出：False
print(Car.year)     # 输出：0
```

假设你没有设置 `year` 的默认值，在实例化前调用 `year` 则会报错，代码如下：<br>
```python
from dataclasses import dataclass

@dataclass
class Car:
    year: int
    make: str = "Unknown"
    model: str = "Unknown"
    only_one = False

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

# 未实例化
print(Car.only_one) # 输出：False
print(Car.year)     # 输出：AttributeError: type object 'Car' has no attribute 'year'
```

注意：位置参数的定义要在前，默认参数要放后面。例如，下列定义方式会报错❌❌❌❌：<br>
```python
from dataclasses import dataclass

@dataclass
class Car:
    make: str = "Unknown"
    model: str = "Unknown"
    only_one = False
    year: int

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
```

## @dataclass(frozen=True)的作用：

`@dataclass(frozen=True)` 是在创建数据类时使用的一种扩展形式，其中 `frozen=True` 是一个参数，用于使数据类不可变，这意味着一旦创建了一个对象，就不能更改其属性的值。让我们来详细了解这种写法：<br>
> 默认 `@dataclass` 即等于 `@dataclass(frozen=False)`，表示创建的数据类是可变的，允许修改其属性值。

先看一下 `dataclass` 常规情况下如果修改类/实例属性：<br>

```python
from dataclasses import dataclass

@dataclass
class MyClass:
    field1: int
    field2: str

# __init__()方法的体现：
obj1 = MyClass(42, "Hello")
print(obj1.field1)  # 输出：42
obj1.field1 = 999
print(obj1.field1)  # 输出：999
```

看看当 `@dataclass(frozen=True)` 时，同样代码的效果如何～<br>
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class MyClass:
    field1: int
    field2: str

# __init__()方法的体现：
obj1 = MyClass(42, "Hello")
print(obj1.field1)  # 输出：42
obj1.field1 = 999   # 报错：dataclasses.FrozenInstanceError: cannot assign to field 'field1'
print(obj1.field1)
```
直接报错，提示我们属性不可修改‼️‼️‼️<br>


## `__init__`与`__post_init__` 用法解析：

如果你想在`__init__`方法中进行一些初始化操作，你可以在`__post_init__`方法中添加这些操作。`__post_init__`方法会在对象的初始化完成后被调用。以下是如何在`dataclass`中添加初始化操作的示例：<br>

```python
from dataclasses import dataclass

@dataclass
class Car:
    make: str = "Unknown"
    model: str = "Unknown"
    year: int = 0
    only_one = False

    def __post_init__(self):
        # 在这里添加你的初始化操作
        self.start_engine()

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    
my_car = Car("Toyota", "Camry", 2020)

# 终端输出：Engine started.
```

在上面的示例中，我们在`__post_init__`方法中调用了`start_engine()`方法，以在对象初始化后启动引擎。你可以在`__post_init__`方法中执行任何你需要的初始化操作。
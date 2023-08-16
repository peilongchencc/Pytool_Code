# class
## 简单示例：
在Python中，类是一种用来创建对象的蓝图或模板。它们允许定义对象的属性和方法，从而可以创建多个相似的对象。下面是一个简单的Python类的示例：<br>
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make    # 车的厂商；
        self.model = model  # 车的型号；
        self.year = year    # 车的出厂年份；

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
```
在上面的示例中，我们定义了一个名为Car的类。__init__方法是一个特殊的方法，被用来初始化类的实例并设置其属性。在本例中，__init__方法接收make，model和year三个参数，并将它们作为实例的属性进行设置。<br>

start_engine和stop_engine是类的方法，它们用于执行启动和停止引擎的操作。这些方法可以通过类的实例进行调用。<br>

get_info是另一个方法，它返回描述汽车的字符串。注意，方法可以访问实例的属性，例如self.year。<br>

要使用这个类，我们首先需要创建一个类的实例，然后使用实例调用方法。例如：<br>

```python
my_car = Car("Toyota", "Camry", 2020)
my_car.start_engine()
print(my_car.get_info())
my_car.stop_engine()
```
以上代码将创建一个名为my_car的Car类的实例。然后，我们调用start_engine方法启动引擎，使用get_info方法获取关于汽车的信息，并最后调用stop_engine方法停止引擎。<br>


## 不定义__init__创建类：
Python的类可以不定义__init__函数。当没有定义__init__函数时，Python会自动提供一个默认的构造函数。<br>

默认的构造函数不接受任何参数，并且不执行任何操作。它的存在只是为了创建类的实例对象，使你能够访问类的属性和方法。<br>

下面是一个没有自定义__init__函数的示例：<br>
```python
class MyClass:
    def method(self):
        print("Hello")

# 创建类的实例
obj = MyClass()     # 尽管没有自定义的__init__函数，但仍然能够使用类和实例对象。

# 调用类的方法
obj.method()
```

**🥸拓展：对于python 类，无论是否定义 __init__ 函数，同一个类中 method_A 调用 method_B 的方法是一样的：**<br>
```python
class MyClass:
    def method_A(self):
        # 调用method_B
        self.method_B()
        # 执行其他代码

    def method_B(self):
        # 方法B的实现
        pass
```
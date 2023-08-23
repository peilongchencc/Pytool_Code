# class
## 简单示例：
在Python中，类是一种用来创建对象的蓝图或模板。它们允许定义对象的属性和方法，从而可以创建多个相似的对象。下面是一个简单的Python类的示例：<br>
```python
class Car:
    def __init__(self, make, model, year):
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
在上面的示例中，我们定义了一个名为Car的类。__init__方法是一个特殊的方法，被用来初始化类的实例并设置其属性。在本例中，__init__方法接收make，model和year三个参数，并将它们作为实例的属性进行设置。<br>

start_engine和stop_engine是类的方法，它们用于执行启动和停止引擎的操作。这些方法可以通过类的实例进行调用。<br>

get_info是另一个方法，它返回描述汽车的字符串。注意，方法可以访问实例的属性，例如self.year。<br>

要使用这个类，我们首先需要创建一个类的实例，然后使用实例调用方法。例如：<br>

```python
my_car = Car("Toyota", "Camry", 2020)
my_car.start_engine()
print(my_car.get_info())
my_car.stop_engine()

# 输出：
# Engine started.
# 2020 Toyota Camry
# Engine stopped.
```
代码解释：<br>
以上代码将创建一个名为my_car的Car类的实例。然后，我们调用start_engine方法启动引擎，使用get_info方法获取关于汽车的信息，并最后调用stop_engine方法停止引擎。<br>





## 类中调用类内部的方法：
类中调用类内部的方法与调用 **"实例化属性"** 的方法相同，都是加上 self。示例代码如下：<br>
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make    # 车的厂商；
        self.model = model  # 车的型号；
        self.year = year    # 车的出厂年份；

    def start_engine(self):
        print("Engine started.")
        print(self.get_info())      # 调用类内部的get_info方法；

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    
my_car = Car("Toyota", "Camry", 2020)
my_car.start_engine()
my_car.stop_engine()

# 输出：
# Engine started.
# 2020 Toyota Camry
# Engine stopped.
```

## 类中调用类外部的方法：
```python
def slogan():   # 标语；
    print('出入平安')

class Car:
    def __init__(self, make, model, year):
        self.make = make    # 车的厂商；
        self.model = model  # 车的型号；
        self.year = year    # 车的出厂年份；

    def start_engine(self):
        print("Engine started.")
        slogan()

    def stop_engine(self):
        print("Engine stopped.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

# 输出：
# Engine started.
# 出入平安
# 2020 Toyota Camry
# Engine stopped.
```



## 不定义__init__创建类：
Python的类可以不定义__init__函数。当没有定义__init__函数时，Python会自动提供一个默认的构造函数。<br>

默认的构造函数不接受任何参数，并且不执行任何操作。它的存在只是为了创建类的实例对象，使你能够访问类的属性和方法。<br>

下面是一个没有自定义__init__函数的示例：<br>
```python
class MyClass:
    def method(self):   # 虽然没有定义init，但类中的方法第一个参数依旧要为 self。
        print("Hello")

# 创建类的实例
obj = MyClass()         # 尽管没有自定义的__init__函数，但仍然能够使用类和实例对象。

# 调用类的方法
obj.method()            # 输出: hello
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

## python类与装饰器：
这里的装饰器仅罗列：`@staticmethod` 和 `@classmethod` 。<br>
`@staticmethod` 和 `@classmethod` 都能实现 🫥**在不进行实例化的情况下调用类方法。**<br>

### @staticmethod：
在Python中，@staticmethod装饰器用来声明一个静态方法。静态方法是一个属于类而不是实例的方法，因此它可以在类的所有实例之间共享和访问。<br>

静态方法可以通过类名直接调用，而不需要创建类的实例。这使得静态方法非常适用于执行与类特性或类级别操作相关的任务，而不需要访问实例属性。<br>

下面是一个示例，展示了使用@staticmethod装饰器声明和使用静态方法：<br>

```python
class MathUtils:        # 数学方法
    @staticmethod
    def add(x, y):      # 加法；
        return x + y

result = MathUtils.add(5, 3)
print(result)  # 输出：8
```
需要注意的是，🚨🚨🚨静态方法中不能访问类的属性或实例属性，因为它们与实例无关。静态方法仅与类关联，而不与任何特定实例相关联。<br>

因此，静态方法在一些独立于实例的任务中非常有用，例如辅助函数或实用函数。<br>

🟡请记住，如果你的类既包含静态方法又包含实例方法，那么通常会同时定义 __init__ 方法来初始化实例属性。但对于只包含静态方法的类，可以省略 __init__ 方法的定义。<br>

### @classmethod:
在Python中，@classmethod是一个装饰器，用于定义类方法。类方法是绑定到类而不是实例的方法。通过@classmethod装饰器，可以在方法上添加一个特殊的标记，告诉Python解释器将该方法视为类方法，而不是实例方法，🫥**这意味着这个方法可以在没有创建类的实例的情况下被调用。**<br>

类方法具有以下特点： 
1. 类方法的第一个参数是类本身，通常被约定为"cls"。 
2. 类方法可以通过类名或实例调用，但实例调用时会自动将对应的类作为第一个参数传递给方法。 
3. 类方法可以访问类的属性和调用其他类方法。
4. 能以多种方式初始化类对象。


下面是一个示例代码，演示了@classmethod的使用：
```python
class MyClass:
    class_attribute = "Hello"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    @classmethod
    def print_class_attribute(cls):
        print(cls.class_attribute)                          # 调用类属性；

    @classmethod
    def create_instance_with_default(cls, default_value="Default"):
        return cls(instance_attribute=default_value)        # 记住，cls等同于类本身，所以这行代码等同于 MyClass(instance_attribute=default_value)。

# 使用 @classmethod
MyClass.print_class_attribute()  # 输出: Hello

instance = MyClass.create_instance_with_default('peilongchencc')
print(instance.instance_attribute)  # 输出: peilongchencc
```
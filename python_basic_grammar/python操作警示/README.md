# python操作警示：

本文档主要用于记录项目进行中遇到的问题，阻碍点，以及自己的解决方案。<br>

- [python操作警示：](#python操作警示)
  - [类和方法的重复嵌套：](#类和方法的重复嵌套)
  - [类的使用使用意义不明：](#类的使用使用意义不明)
  - [staticmethod、classmethod的过度使用:](#staticmethodclassmethod的过度使用)
  - [数据重复存储：](#数据重复存储)
  - [代码中请添加注释，并注意变量命名：](#代码中请添加注释并注意变量命名)
  - [Debug时不要随意跳出：](#debug时不要随意跳出)
  - [项目测试的环境问题：](#项目测试的环境问题)
  - [对Redis的理解有问题：](#对redis的理解有问题)
  - [写代码更需要考虑耗时的问题。](#写代码更需要考虑耗时的问题)
  - [技术方案要更为详细：](#技术方案要更为详细)


## 类和方法的重复嵌套：

问题描述：<br>

在py文件中，表现形式为：<br>

```log
ClassA-->ClassB-->ClassC-->ClassD-->ClassE-->ClassF
```

类和方法的重复嵌套引起的问题：<br>

1. 理解困难，需要频繁类的定义中跳转查看，时间成本巨大。
2. 重构成本大，由于类的嵌套过深，需要层层拆解才能重构为字典形式。
3. 若转存入Redis，从Redis解析时间消耗大，过深的类嵌套导致pickle.loads需要解析的时间过长。

警示：<br>

python类的嵌套不易超过三层，过深会造成维护困难，他人理解困难等问题。<br>

## 类的使用使用意义不明：

有些情况下，在项目中有大量如下所示的类，作用与字典相同，这种情况使用类的意义不明。<br>

```python
class Fund():
    def __init__(self, id, text, code, type):
        self._id = id
        self._text = text
        self._code = code
        self._type = type
    #end of init

    #getters
    def get_id(self):
        return self._id
    def get_text(self):
        return self._text
    def get_code(self):
        return self._code
    def get_type(self):
        return self._type
```

警示：<br>

字典的使用比这种方式更方便，也更易进行处理操作。<br>

## staticmethod、classmethod的过度使用:

问题描述：<br>

如果你发现项目中运用了大量的staticmethod、classmethod装饰器，即使是简单定义一个方法，也会将方法写成类，使用staticmethod、classmethod装饰器包裹，那这一定是一种不规范的写法。<br>

staticmethod、classmethod过度使用引起的问题:<br>

`@staticmethod` 和 `@classmethod` 都能实现在不进行实例化的情况下调用类方法，但项目中大量的类中只有方法，没有类属性或实例化属性，使用staticmethod、classmethod是没有意义的做法。<br>

装饰器的使用原则一直是：能不用装饰器则不用。<br>

## 数据重复存储：

项目中，如果有多个文件/变量存储的内容相同，只是按照不同的逻辑存储的。这种情况下需要考虑数据所占内存和存储/读取的耗时，如果你是利用Redis存储/读取数据，过多的重复数据只会造成无意义的时间消耗。<br>

## 代码中请添加注释，并注意变量命名：

代码中的变量名不要使用类似"q"这种难以理解的变量名称。<br>

## Debug时不要随意跳出：

应该再细心一点，Debug时不要随意跳出，避免错过代码中的一些关键调用。<br>

## 项目测试的环境问题：

项目的响应时间，要考虑到硬件和系统，如果要测试程序响应时间，需要将项目代码上传至测试服务器运行，一定要把环境拉齐!<br>

## 对Redis的理解有问题：

Redis只能存标准型数据，无法直接存储嵌套型数据。<br>

如果要存储嵌套型数据，需要pickle进行序列化与反序列化。<br>

## 写代码更需要考虑耗时的问题。

## 技术方案要更为详细：

技术方案一定要画图，能细尽可能的细，可读性一定要好。<br>

技术方案的实现可能性如何。<br>

一定要更主动沟通。<br>

仔细考虑是否有考虑不周，遗漏的问题。<br>

能做demo就做demo。<br>

上线怎么上线、开发怎么开发、联调怎么联调、自测怎么自测，需要做哪些准备。<br>
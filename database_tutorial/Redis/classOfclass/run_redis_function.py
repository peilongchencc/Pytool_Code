from get_redis_function import get_classOfclass_data
class C:
    def __init__(self, name):
        self.name = name

class B:
    def __init__(self, name, c_obj):
        self.name = name
        self.c_obj = c_obj

class A:
    def __init__(self, name, b_obj):
        self.name = name
        self.b_obj = b_obj

# 调用的位置才需要导入类的定义：（少一个类的定义都会报错！！！）
get_classOfclass_data()
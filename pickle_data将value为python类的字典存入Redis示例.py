import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

serialized_data = b"\x80\x04\x95)\x00\x00\x00\x00\x00\x00\x00\x8c\b__main__\x94\x8c\aMyClass\x94\x93\x94)\x81\x94}\x94\x8c\x05value\x94K*sb."

my_object = pickle.loads(serialized_data)
print(type(my_object))
print(my_object)
print(my_object.value)
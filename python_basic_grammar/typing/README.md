# typing
`typing` 库是 Python 标准库中的一部分，它在 Python 3.5 版本引入，并用于提供类型提示和类型注解的支持。它的主要作用是帮助开发者在代码中指定变量、函数参数和函数返回值的类型信息，从而提高代码的可读性和可维护性，同时也可以在一些静态类型检查工具（如`mypy`）中进行类型检查。

常见写法为：<br>
```python
from typing import List, Tuple, Any, Union
```
- [typing](#typing)
  - [类型提示：](#类型提示)
    - [Tuple 类型：](#tuple-类型)
    - [Tuple 类型：](#tuple-类型-1)
    - [Any 类型：](#any-类型)
    - [Union 和 Optional 类型：](#union-和-optional-类型)
  - [泛型（Generics）：](#泛型generics)
    - [使用 List 泛型：](#使用-list-泛型)
    - [使用 Dict 泛型：](#使用-dict-泛型)
    - [使用 Callable 泛型：](#使用-callable-泛型)


以下是 `typing` 库的一些主要用法和作用：<br>

## 类型提示：
`typing` 允许你使用类型提示来说明变量的类型，例如 `int`、`str`、`List`、`Tuple` 等。这有助于其他开发者和工具更容易理解代码的意图。<br>

🚨🚨🚨注意，当输入的参数与 `typing` 指定的类型不符时，终端运行时会提示 `TypeError`。<br>

### Tuple 类型：

```python
from typing import List

def process_numbers(numbers: List[int]) -> int:
    total = sum(numbers)
    return total
```

### Tuple 类型：
`typing` 允许你使用 `Tuple` 类型来表示一个具有固定长度和不同类型元素的元组。<br>

```python
from typing import Tuple

def get_name_and_age() -> Tuple[str, int]:
    return ("Alice", 30)

name, age = get_name_and_age()
```

### Any 类型：
`Any` 表示任何类型都可以接受，通常在不确定值的类型时使用，但最好尽量避免使用它，以便能够进行更严格的类型检查。示例：<br>

```python
from typing import Any

def print_value(value: Any) -> None:
    print(value)

print_value(42)
print_value("Hello, World!")
```

### Union 和 Optional 类型：
`typing` 允许你使用 `Union` 和 `Optional` 来表示一个变量可以是多种类型中的一个，或者可以是可选的（即可以为 None）。<br>

`Union` 用于表示一个变量可以是多种类型之一，示例：<br>

```python
from typing import Union

def square_or_double(value: Union[int, float]) -> Union[int, float]:
    if isinstance(value, int):
        return value * value
    elif isinstance(value, float):
        return value * 2

result1 = square_or_double(5)  # 返回 25
result2 = square_or_double(3.5)  # 返回 7.0
```

`Optional` 示例：<br>
```python
from typing import Union, Optional

def process_data(data: Union[str, int]) -> Optional[str]:
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, int):
        return str(data)
    else:
        return None
```
<br>

## 泛型（Generics）：
泛型（Generics）是一种在编程中用于处理不特定类型的数据结构或函数的方式。Python的`typing`库支持泛型，允许你编写更通用和类型安全的代码，特别是当你需要处理各种类型的集合（例如列表、字典、集合）时，泛型非常有用。<br>

泛型允许你在代码中定义参数化的类型，而不是具体指定数据结构中元素的类型。这样，你可以创建更灵活的函数和数据结构，可以适用于不同类型的数据。<br>

下面是一些泛型的示例使用情况：<br>

### 使用 List 泛型：

```python
from typing import List

def get_first_element(sequence: List[T]) -> T:
    return sequence[0]

# 在这个示例中，List[T] 表示一个列表，其中 T 是类型参数，可以代表任何数据类型。
# 调用时，T 会根据传入的列表的元素类型进行推断。

first_element = get_first_element([1, 2, 3])  # first_element 的类型为 int
first_string = get_first_element(["apple", "banana", "cherry"])  # first_string 的类型为 str
```

### 使用 Dict 泛型：

```python
from typing import Dict

def print_key_and_value(d: Dict[K, V]) -> None:
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")

# 在这个示例中，Dict[K, V] 表示一个字典，其中 K 和 V 是类型参数，可以代表任何键和值的数据类型。

data = {"name": "Alice", "age": 30}
print_key_and_value(data)
```

### 使用 Callable 泛型：

```python
from typing import Callable

def apply_function(func: Callable[[A], B], arg: A) -> B:
    return func(arg)

# 在这个示例中，Callable[[A], B] 表示一个可调用对象，接受类型为 A 的参数并返回类型为 B 的结果。

def double(x: int) -> int:
    return x * 2

result = apply_function(double, 5)  # result 的类型为 int
```

通过使用泛型，你可以编写更通用、灵活且类型安全的代码，而不需要重复编写类似的函数或数据结构来处理不同类型的数据。`typing`库的泛型支持使你能够定义具有参数化类型的函数和数据结构，这对于提高代码的可维护性和可读性非常有帮助。<br>

总之，`typing` 库是 Python 中用于提供类型提示和类型注解的强大工具，有助于提高代码的可靠性和可维护性，同时也可以用于进行静态类型检查，以捕获潜在的类型错误。<br>



# yield

## 生成器的常规使用:

```python
def squares_generator(n):
    for i in range(n):
        yield i ** 2

if __name__ == "__main__":
    # 遍历生成器
    for square in squares_generator(5):
        print(square)
```

终端输出:<br>

```txt
0
1
4
9
16
```

## 将生成器的所有结果收集到一个列表中并返回:

```python
def squares_generator(n):
    for i in range(n):
        yield i ** 2

def all_squares(n):
    """将生成器的所有结果收集到一个列表中并返回
    """
    return list(squares_generator(n))

if __name__ == "__main__":
    res = all_squares(6)
    print(type(res))
    print(res)
```

终端输出:<br>

```txt
<class 'list'>
[0, 1, 4, 9, 16, 25]
```

## 返回最后一个生成的结果:

```python
def squares_generator(n):
    for i in range(n):
        yield i ** 2

def last_square(n):
    """遍历生成器生成的所有结果，并在每次迭代中更新 last 变量。最后，函数会返回最后一个生成的结果
    """
    last = None
    for square in squares_generator(n):
        last = square
    return last

if __name__ == "__main__":
    res = last_square(6)
    print(type(res))
    print(res)
```

终端输出:<br>

```txt
<class 'int'>
25
```
# Argparse

## 代码示例:

```python
# arg_test.py
import argparse

def arg_parse():
    """获取终端传参
    """
    parser = argparse.ArgumentParser(description='参数设定')
    parser.add_argument('-p','--path',type=str,help='请传入文件路径')
    parser.add_argument('-n','--number',type=float,help='请传入测试的数字')
    args = parser.parse_args()
    return args

def main(data):
    if not isinstance(data.path, str):
        raise Exception('路径参数不正确，请使用 python 本文件.py -h 查看参数并填写。')
    print(f'输入的路径为：{data.path}')
    assert isinstance(data.number, float),'数字参数不正确，请使用 python 本文件.py -h 查看参数并填写。'
    print(f'数字规范化后的结果为：{data.number:,.2f}')

if __name__ == "__main__":
    # 参数解析
    args = arg_parse()
    main(args)
```

终端输入:<br>

```bash
python arg_test.py --path='xxx' --number=0.123
```

终端输出:<br>

```txt
输入的路径为：xxx
数字规范化后的结果为：0.12
```
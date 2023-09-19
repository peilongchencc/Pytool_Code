# Request

如果你想本地测试自己的服务接口并计算响应时间，可以使用 Python 的 `requests` 库。<br>

运行以下指令安装 `requests` 库：<br>
```bash
pip install requests
```

- [Request](#request)
  - [get方法向接口传数据并计算平均时间：](#get方法向接口传数据并计算平均时间)
  - [post方法向接口传数据并计算平均时间：](#post方法向接口传数据并计算平均时间)
  - [post方法向接口传数据、计算平均时间并查看返回的数据：](#post方法向接口传数据计算平均时间并查看返回的数据)

## get方法向接口传数据并计算平均时间：
以下是接口方法为`get`时的简单示例，说明如何测试 `http://localhost:7711/answer` 接口 500 次，并计算平均响应时间：<br>

```python
import requests
import time

# 测试参数
URL = 'http://localhost:7711/answer'
PARAMS = {
    'question': '定投',
    'intentTags': '',
    'advisorId': 1,
    'labelIds': ''
}
TEST_TIMES = 500

def test_response_time():
    start_time = time.time()
    response = requests.get(URL, params=PARAMS)
    response_time = time.time() - start_time
    
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return None
    return response_time

def main():
    total_response_time = 0
    successful_tests = 0

    for i in range(TEST_TIMES):
        time_taken = test_response_time()
        if time_taken is not None:
            total_response_time += time_taken
            successful_tests += 1

    if successful_tests == 0:
        print("所有测试请求均失败!")
        return

    average_response_time = total_response_time / successful_tests
    print(f"在 {successful_tests} 次成功的请求中，平均响应时间为: {average_response_time:.4f} 秒")

if __name__ == '__main__':
    main()
```

此代码将测试指定的接口500次，计算每次的响应时间，并最后输出平均响应时间。<br>

注意：
1. 为了避免反复创建新连接，可以考虑使用 `requests.Session()` 进行优化。
2. 这只是一个基本示例，你可能需要根据具体的情况进行调整（例如，是否有其他需要的HTTP头，是否需要使用POST而不是GET，是否需要动态生成参数等）。
3. 安装 `requests` 库，如果你还没有的话：`pip install requests`。


## post方法向接口传数据并计算平均时间：
如果你的接口是一个POST方法，那么你需要做以下几个修改：<br>

1. 使用`requests.post()`方法代替`requests.get()`。
2. 将`params`参数更改为`data`或`json`，具体取决于你的API期望的数据格式。

以下是修改后的代码：<br>

```python
import requests
import time

# 测试参数
URL = 'http://localhost:7711/answer'
DATA = {
    'question': '定投',
    'intentTags': '',
    'advisorId': 1,
    'labelIds': ''
}
TEST_TIMES = 10

def test_response_time():
    start_time = time.time()
    # 使用 POST 方法并将数据传给 data 参数
    response = requests.post(URL, data=DATA)
    response_time = time.time() - start_time
    
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return None
    return response_time

def main():
    total_response_time = 0
    successful_tests = 0

    for i in range(TEST_TIMES):
        time_taken = test_response_time()
        if time_taken is not None:
            total_response_time += time_taken
            successful_tests += 1

    if successful_tests == 0:
        print("所有测试请求均失败!")
        return

    average_response_time = total_response_time / successful_tests
    print(f"在 {successful_tests} 次成功的请求中，平均响应时间为: {average_response_time:.4f} 秒")

if __name__ == '__main__':
    main()
```

注意：上述代码假设你的接口接受`x-www-form-urlencoded`格式的数据（这是默认的POST数据格式）。如果你的接口接受JSON格式的数据，你可以将`requests.post(URL, data=DATA)`替换为`requests.post(URL, json=DATA)`。<br>

🌿🌿🌿`x-www-form-urlencoded`格式的数据（这是默认的POST数据格式）是用的最多的格式‼️‼️‼️<br>


## post方法向接口传数据、计算平均时间并查看返回的数据：
要查看每一次的返回结果，你可以直接打印`response.text`或`response.json()`（如果返回的是JSON格式的数据）。<br>

下面是修改后的代码，将每次的返回结果都打印出来：<br>

```python
import requests
import time

# 测试参数
URL = 'http://localhost:7711/answer'
DATA = {
    'question': '定投',
    'intentTags': '',
    'advisorId': 1,
    'labelIds': ''
}
TEST_TIMES = 10

def test_response_time():
    start_time = time.time()
    response = requests.post(URL, data=DATA)
    response_time = time.time() - start_time
    
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return None
    else:
        # 打印每一次的返回结果
        print(f"返回结果：{response.text}")
        
    return response_time

def main():
    total_response_time = 0
    successful_tests = 0

    for i in range(TEST_TIMES):
        time_taken = test_response_time()
        if time_taken is not None:
            total_response_time += time_taken
            successful_tests += 1

    if successful_tests == 0:
        print("所有测试请求均失败!")
        return

    average_response_time = total_response_time / successful_tests
    print(f"在 {successful_tests} 次成功的请求中，平均响应时间为: {average_response_time:.4f} 秒")

if __name__ == '__main__':
    main()
```

上述代码在每次请求成功后，都会打印返回的结果。如果返回的数据是JSON格式，你可以更改`print(f"返回结果：{response.text}")`为`print(f"返回结果：{response.json()}")`，这样会更直观地展示返回的JSON数据。<br>
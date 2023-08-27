# time
time库是Python标准库中的一个模块，它提供了处理时间的功能。下面是一些常见的time库的用法：<br>

**Ps1**：文章中的时间如果格式化，统一转化为 2022-01-01 12:05:44 形式，原因为：该时间格式可以直接写入mysql，在实际操作中非常方便。<br>
**Ps2**：文章中使用的都是 `time` 模块中的用法，并没有使用利用 `datetime` 等其他时间模块，这样做的好处是：在项目中使用统一的时间获取方式。

## **获取当前时间的时间戳：**<br>
```python
import time

current_time = time.time()  # 返回一个浮点数，表示当前时间距离1970年1月1日00:00:00的秒数。
print(current_time)
```
注意⚠️：time.time() 函数返回的是当前时间的时间戳，无法直接返回指定时间的时间戳。要获取指定时间的时间戳，需要借助其他时间模块来实现。

## **获取指定时间的时间戳：**<br>
假设指定的时间为：2022-01-01 12:05:44
```python
import time

date_string = "2022-01-01 12:05:44"
timestamp = time.mktime(time.strptime(date_string, "%Y-%m-%d %H:%M:%S"))

print(timestamp)    # 1641009944.0
```
`time.strptime()` 函数用于将字符串时间转换为 **时间元组** 。时间元组包含了年、月、日、时、分、秒等时间信息。<br>
`'%Y-%m-%d %H:%M:%S'` 指定了字符串时间的格式，与字符串时间的实际格式相匹配。<br>
`time.mktime()` 函数用于将时间元组转换为对应的时间戳。<br>

## **根据时间戳，将时间格式化：**<br>
```python
import time

timestamp = 1641009944.0
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print(formatted_time)   # 2022-01-01 12:05:44
```

`time.localtime()` 用于将时间戳转化为 struct_time 的时间元组形式。用法如下：<br>
```python
import time

timestamp = 1641009944.0
res = time.localtime(timestamp)
print(res)
# 输出：
# time.struct_time(tm_year=2022, tm_mon=1, tm_mday=1, tm_hour=12, tm_min=5, tm_sec=44, tm_wday=5, tm_yday=1, tm_isdst=0)
```

如果时间戳通过 `time.time()` 获取，则表示 **根据时间戳，将当前时间格式化：**<br>
```python
import time
timestamp = time.time()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print(formatted_time)   # 2023-08-15 11:29:22
```

也可以使用更简单的形式，当 `time.localtime()` 无参数时，默认获取的就是当前时间的元组形式。<br>
```python
import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 输出格式为：
# 2023-08-15 10:18:14
```

## **获取当前时间的年份、月份、日期等信息：**<br>
`time.localtime()` 将时间戳转化为了 struct_time 的时间元组形式，可以通过 `struct_time` 的key获取对应的年份、月份、日期。<br>
```python
import time

current_time = time.localtime()
print(current_time)     
# time.struct_time(tm_year=2023, tm_mon=8, tm_mday=15, tm_hour=11, tm_min=36, tm_sec=29, tm_wday=1, tm_yday=227, tm_isdst=0)

year = current_time.tm_year
month = current_time.tm_mon
day = current_time.tm_mday
print(year, month, day) # 2023 8 15
```

## **延时执行程序**<br>
```python
import time

print("Start")
time.sleep(2)   # 程序延时2秒后再执行下方的print("End")。
print("End")
```

## **获取程序执行时间**<br>
🚨🚨🚨如果你想查看某部分代码的时间，最好单独测试，不要整个项目一起查看。服务器性能、服务器负载不平衡都会影响你的时间。如果你是使用 `postman` 测试远程服务器部署的代码，更可能由于网络延迟导致每次测试的时间不一致。<br>
```python
import time
start_time = time.time() 
"""
这里执行一些代码 
"""
end_time = time.time() 
execution_time = end_time - start_time 
print(f"执行时间为：{execution_time} 秒")
```

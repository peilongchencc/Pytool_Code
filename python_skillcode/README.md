# Python Skillcode
python 在各种场景下的应用型代码，方便个人在工作中调用，避免重复编写。<br>

**count_num_of_unique_values_of_dict.py:** 计算字典型数据中 values 的唯一值数量和不同值出现的次数。<br>

**listOflist_2_list.py:** 测试将 "列表嵌套列表型数据" 转为列表，哪种方式更快。<br>
```python
data = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
```

**used_main_function.py:** 偶然间见到的 `if __name__ == '__main__':` 的奇怪用法，记录一下运行方式。<br>
```python
if __name__ == '__main__':
    # 默认运行 if True 条件下的内容，将 if True 修改为 if False 运行 else 部分。
    if True:
        pass
    else:
        pass
```
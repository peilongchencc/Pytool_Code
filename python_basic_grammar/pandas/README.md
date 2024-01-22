# Pandas

## 读取xlsx文件:

问题描述:<br>

根据"意图ID"从`question_data`中的"问句"列找值，将其添加到`answer_data`表。注意，一个"意图ID"可能对应多个"问句"，随机取一个即可。<br>

具体代码实现:<br>

```python
import pandas as pd

question_data = '理财语料库_问句.xlsx'
answer_data = '理财语料库_答案.xlsx'

# 读取文件
df_question = pd.read_excel(question_data, usecols=['问句', '意图ID'])
df_answer = pd.read_excel(answer_data, usecols=['意图ID', '内容'])

# 按 "意图ID" 分组，并随机选择一个 "问句"
grouped = df_question.groupby('意图ID').apply(lambda x: x.sample(1)).reset_index(drop=True)

# 将选择的 "问句" 添加到答案数据中
df_merged = pd.merge(df_answer, grouped, on='意图ID', how='left')

# 显示合并后的 DataFrame 的前几行
# print(df_merged.head(20))

# 选择问句和内容列
df_selected = df_merged[['问句', '内容']]

# 写入txt文件
with open('理财语料库_qa.txt', 'w', encoding='utf-8') as file:
    for index, row in df_selected.iterrows():
        # 去除内容中的换行符
        content = row['内容'].replace('\n', '')
        file.write(f"问题:{row['问句']}\n答案:{content}\n")

print("写入完成")
```

重点解析:<br>

```python
grouped = df_question.groupby('意图ID').apply(lambda x: x.sample(1)).reset_index(drop=True)
```

这行代码的作用是从 `df_question` 数据框中，基于 "意图ID" 列进行分组，并且在每个分组内随机选取一个 "问句"。下面是逐步解析：<br>

1. **`df_question.groupby('意图ID')`**: 这部分是 pandas 的 `groupby` 方法，用于将数据框 `df_question` 按照 "意图ID" 列的值进行分组。这意味着，具有相同 "意图ID" 的所有行将被组合在一起形成一个分组。

2. **`.apply(lambda x: x.sample(1))`**: `apply` 方法对每个分组执行指定的函数。这里的函数是一个 lambda 表达式，它对每个分组应用了 `sample(1)` 方法。`sample(1)` 从每个分组中随机选取一个样本（即一行数据）。由于每个分组代表了一个独特的 "意图ID"，因此这个过程将从每个 "意图ID" 对应的所有 "问句" 中随机选取一个。

3. **`reset_index(drop=True)`**: `reset_index` 方法用于重置数据框的索引。在应用 `groupby` 和 `apply` 后，返回的结果将有一个多级索引（multi-index），其中包括原始的索引和分组键。`reset_index(drop=True)` 将这个多级索引重置为简单的整数索引，并且 `drop=True` 参数确保原来的索引列不会被添加到数据框的列中。

综合来看，这行代码的作用是创建一个新的数据框 `grouped`，其中包含了按 "意图ID" 分组的 `df_question` 数据框中的随机 "问句"。每个 "意图ID" 只对应一个随机选取的 "问句"。<br>
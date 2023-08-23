# NER
记录 NER 任务的各种实现方法。<br>

## 数据集
| 数据集 | 语料 | 文件大小 |
| :------- | :--------- | :---------: |
| **`CNER中文实体识别数据集`** | CNER(12万字) | 1.1MB |

CNER中文实体识别数据集，数据格式类似（真实数据中没有以下数据）：<br>
```json
美	B-LOC
国	I-LOC
的	O
华	B-PER
莱	I-PER
士	I-PER

我	O
跟	O
他	O
```

CNER中文实体识别数据集，标签列表为：<br>
```python
labels = ['B-NAME', 'I-NAME', 'O', 'B-CONT', 'I-CONT', 'B-RACE', 'I-RACE', 'B-TITLE', 'I-TITLE', 'B-EDU', 'I-EDU', 'B-ORG', 'I-ORG', 'B-PRO', 'I-PRO', 'B-LOC', 'I-LOC']
NUM_LABELS = len(labels)    # 17
```

数据集来自徐明大佬的github，链接为：https://github.com/shibing624/nerpy/tree/main<br>
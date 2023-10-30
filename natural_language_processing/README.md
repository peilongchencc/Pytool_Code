# Natural Language Processing
- [Natural Language Processing](#natural-language-processing)
  - [dataset：](#dataset)
  - [文本向量化：](#文本向量化)
    - [自定义jieba词库示例:](#自定义jieba词库示例)
    - [句向量示例:](#句向量示例)

## dataset：
如果数据集较小，会放在项目文件中。如果数据集较大，会放在 dataset 文件夹下。如果遇到项目文件中缺少数据集，请在 dataset 文件夹下寻找对应网盘链接下载。<br>

## 文本向量化：

如果你有一个自定义的词库并希望使用它进行分词，然后为每个token获取向量，你可能需要先使用一个支持自定义词库的中文分词工具，如jieba分词，然后使用transformers库来获取向量。<br>

以下是一个简单的步骤来实现这个流程：<br>

1. 使用jieba分词工具并加载你的自定义词库。
2. 使用jieba进行分词。
3. 使用transformers库中的模型获取每个token的向量。

以下是一个示例代码：<br>

```python
import jieba
from transformers import ElectraModel, ElectraTokenizer
import torch

# 1. 加载自定义词库
jieba.load_userdict('path_to_your_custom_dictionary.txt')

# 2. 使用jieba进行分词
texts = [
    '急性肠胃炎要如何治疗？',
    '盛剑环境的股价太高了。',
    '看图猜一电影名'
]

tokenized_texts = [list(jieba.cut(text)) for text in texts]

# 3. 使用transformers库中的模型获取每个token的向量
MODEL_NAME = "hfl/chinese-electra-180g-base-discriminator"
tokenizer = ElectraTokenizer.from_pretrained(MODEL_NAME)
model = ElectraModel.from_pretrained(MODEL_NAME)

for tokens in tokenized_texts:
    # 将tokens转化为模型所需的input format
    inputs = tokenizer(tokens, return_tensors='pt', padding=True, truncation=True, is_split_into_words=True)
    with torch.no_grad():
        outputs = model(**inputs)
    token_vecs = outputs.last_hidden_state.squeeze().numpy()
    
    for token, vec in zip(tokens, token_vecs):  # 使用zip的目的是为了方便地同时遍历并匹配多个列表的元素。这在处理诸如tokens和它们的向量这样成对的数据时特别有用。
        print(token, vec)
```

请注意以下几点：<br>

- 你需要为`jieba.load_userdict`提供你的自定义词库的路径。
- 当使用`tokenizer`时，由于我们已经预先使用jieba进行了分词，所以需要设置`is_split_into_words=True`来告诉tokenizer输入已经是tokenized的。

通过这种方式，你可以按照自己的自定义词库进行分词，并为每个token获取其向量。<br>

### 自定义jieba词库示例:

当你使用`jieba.load_userdict`加载自定义词库时，词库的格式通常为每行一个词。此外，每一行可以包括以下三部分，由空格分隔：<br>

1. **词语**：这是要添加的自定义词。
2. **权重**（可选）：表示该词在分词中的权重，这是一个用来调整词频的数值。权重越高，该词被分出的可能性越大。如果不提供，jieba会使用默认权重。
3. **词性**（可选）：词的词性标注（如'n'表示名词，'v'表示动词等）。

以下是一个简单的示例：<br>

```
急性肠胃炎 5 n
盛剑环境 5 n
动车票 5 n
```

在上述示例中：<br>

- `急性肠胃炎`、`盛剑环境` 和 `动车票` 是要添加的自定义词。
- `5` 是为每个词设定的权重（这只是一个示例值，实际使用时可能需要根据你的需求进行调整）。
- `n` 表示这些词都是名词。

只有词语是必须的，权重和词性是可选的。如果你只关心分词，并不需要词性标注，你可以省略权重和词性，只列出词语，例如：<br>

```
急性肠胃炎
盛剑环境
动车票
```

然后，你可以使用`jieba.load_userdict('path_to_your_custom_dictionary.txt')`加载这个词库文件，并按照之前提供的示例代码进行分词和向量化操作。<br>

🫠🫠🫠当然，你完全可以只为自定义词库中的词语指定词性，而省略权重。当你这样做时，`jieba`会为这些词分配默认权重。<br>

自定义词库的格式如下：<br>

```
急性肠胃炎 n
盛剑环境 n
动车票 n
```

在这个例子中，`急性肠胃炎`、`盛剑环境` 和 `动车票` 都被指定为名词，但权重没有明确指定，所以`jieba`会使用默认权重。<br>

只需确保词语和词性之间有一个空格来分隔它们，然后你可以正常使用`jieba.load_userdict`来加载这个自定义词库。<br>

### 句向量示例:

```python
from transformers import ElectraModel, ElectraTokenizer

MODEL_NAME = "hfl/chinese-electra-180g-base-discriminator"
tokenizer = ElectraTokenizer.from_pretrained(MODEL_NAME)
model = ElectraModel.from_pretrained(MODEL_NAME)

texts = [
    '急性肠胃炎要如何治疗？',
    '盛剑环境的股价太高了。',
    '看图猜一电影名'
]

vectors = []

for text in texts:
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    vectors.append(outputs.last_hidden_state.mean(dim=1).squeeze().numpy())

print(vectors)
```

上面的代码首先加载了预训练的Electra模型和对应的tokenizer，然后为给定的文本列表提取了向量。每个文本的向量是其所有token的向量的平均值。<br>
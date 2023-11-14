# Natural Language Processing
- [Natural Language Processing](#natural-language-processing)
  - [dataset：](#dataset)
  - [文本向量化：](#文本向量化)
    - [自定义jieba词库示例:](#自定义jieba词库示例)
    - [句向量示例:](#句向量示例)
    - ["hfl/chinese-electra-180g-base-discriminator"模型简介:](#hflchinese-electra-180g-base-discriminator模型简介)
  - [同义词替换构建新语句：](#同义词替换构建新语句)
    - [tensor转list:](#tensor转list)

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

### "hfl/chinese-electra-180g-base-discriminator"模型简介:

`"hfl/chinese-electra-180g-base-discriminator"` 是 Hugging Face Model Hub 上的一个模型。HFL（Hugging Face Lab）的这个模型基于 ELECTRA 架构并专门针对中文进行了预训练。<br>

> 笔者暂时了解到hanlp的相似度模型就是使用"hfl/chinese-electra-180g-base-discriminator"做的文本向量化。

首先，我们来简单介绍一下 ELECTRA：<br>

ELECTRA（Efficiently Learning an Encoder that Classifies Token Replacements Accurately）是一种与BERT相似但更高效的预训练语言模型方法。与BERT的Masked Language Model目标不同，ELECTRA的训练目标是Discriminator，它试图区分"真实"的token和一个生成模型所替代的"假"token。<br>

关于 `"hfl/chinese-electra-180g-base-discriminator"` 的特点：<br>

1. **语言**: 这个模型是专门为中文设计的。这意味着它在各种中文数据集上进行了预训练，包括简体、繁体以及混合的中文文本。
   
2. **模型大小**: "180g" 暗示这是一个相对较小的模型，但它已经足够强大，可以处理大多数NLP任务。较小的模型在推理时速度更快，也更易于部署。

3. **Discriminator**: 这个模型是 ELECTRA 的 Discriminator 版本，意味着它被训练来识别由一个生成模型产生的假token。

4. **来源**: HFL 是 Hugging Face 团队的一个子项目，他们专门致力于各种语言的模型研发。这意味着该模型背后有一定的研究和开发力量，确保其性能和可靠性。

在实际应用中，ELECTRA 通常能够在许多NLP任务上提供与BERT相似或更好的性能，但以更低的计算成本。因此，使用这种中文版本的ELECTRA模型可能会为中文NLP应用带来很好的效果。<br>

## 同义词替换构建新语句：

```python
import hanlp
import itertools

# 分词
Segment = hanlp.load(hanlp.pretrained.tok.FINE_ELECTRA_SMALL_ZH)
Segment.dict_force = None
Segment.dict_combine = {'货币三佳','年收益'}
res = Segment(['卖出货币三佳收益如何？','雪球基金的年收益如何？'])

# 同义词-词典
synonym_dict = {'抛售':'卖出',
                '售出':'卖出',
                '三佳':'货币三佳',
                '组合三佳':'货币三佳',
                '基金三佳':'货币三佳',
                '年收益率':'年收益',
                '年化率':'年收益'}

def get_synonyms(word):
    # 获取给定词的所有同义词
    synonyms = [word]
    for key, value in synonym_dict.items():
        if value == word:
            synonyms.append(key)
    return list(set(synonyms))

def replace_with_synonyms(sentence):
    # 将句子中的词替换为同义词，并返回所有可能的替换后的句子
    word_lists = [get_synonyms(word) for word in sentence]
    """
    原句: '卖出货币三佳收益如何？'
    分词结果: ['卖出', '货币三佳', '收益', '如何', '？']
    word_lists: [['卖出', '抛售', '售出'], ['三佳', '基金三佳', '货币三佳', '组合三佳'], ['收益'], ['如何'], ['？']]
    """
    # 利用排列组合获取最终结果
    combinations = list(itertools.product(*word_lists))
    """
    [('卖出', '三佳', '收益', '如何', '？'), 
     ('卖出', '基金三佳', '收益', '如何', '？'), 
     ('卖出', '货币三佳', '收益', '如何', '？'), 
     ('卖出', '组合三佳', '收益', '如何', '？'), 
     ('抛售', '三佳', '收益', '如何', '？'), 
     ('抛售', '基金三佳', '收益', '如何', '？'), 
     ('抛售', '货币三佳', '收益', '如何', '？'), 
     ('抛售', '组合三佳', '收益', '如何', '？'), 
     ('售出', '三佳', '收益', '如何', '？'), 
     ('售出', '基金三佳', '收益', '如何', '？'), 
     ('售出', '货币三佳', '收益', '如何', '？'), 
     ('售出', '组合三佳', '收益', '如何', '？')]
    """
    # 将分词结果重新组成句子
    replaced_sentences = [''.join(combination) for combination in combinations]
    return replaced_sentences

all_replaced_sentences = []
for sentence in res:
    # 针对每个输入的分词结果，根据同义词库生成多种可能的句子
    all_replaced_sentences.extend(replace_with_synonyms(sentence))

print(all_replaced_sentences)
```

该代码主要实现了以下功能：<br>

1. 使用`hanlp`库对输入的句子进行分词。

2. 根据预定义的同义词词典，对分词后的结果进行替换，生成多种可能的句子组合。

终端显示:<br>

```log
['抛售基金三佳收益如何？', '抛售三佳收益如何？', '抛售组合三佳收益如何？', '抛售货币三佳收益如何？', '卖出基金三佳收益如何？', '卖出三佳收益如何？', '卖出组合三佳收益如何？', '卖出货币三佳收益如何？', '售出基金三佳收益如何？', '售出三佳收益如何？', '售出组合三佳收益如何？', '售出货币三佳收益如何？', '雪球基金的年收益率如何？', '雪球基金的年收益如何？', '雪球基金的年化率如何？']
```

### tensor转list:

```python
import torch

# 创建一个PyTorch张量，形状为[512, 768]
tensor_data = torch.randn(512, 768)

print(f"\ntensor_data为:\n{tensor_data}")

# 将张量转换为Python列表
list_data = tensor_data.tolist()

print(list_data)
```
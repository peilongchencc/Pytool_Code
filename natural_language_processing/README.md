# Natural Language Processing
- [Natural Language Processing](#natural-language-processing)
  - [dataset：](#dataset)
  - ["epoch"、"batch\_size"、"step"这3者是什么，相互之间有什么换算关系吗？](#epochbatch_sizestep这3者是什么相互之间有什么换算关系吗)
    - [我看到很多代码都是一个 "epoch" 结束后更新一次模型，用到 "step" 的情况很少。](#我看到很多代码都是一个-epoch-结束后更新一次模型用到-step-的情况很少)
  - [知识拓展--在NLP领域，什么因素决定了模型的输入长度？](#知识拓展--在nlp领域什么因素决定了模型的输入长度)
    - [为什么chatgpt可以用几千甚至几万长度的输入:](#为什么chatgpt可以用几千甚至几万长度的输入)
  - [文本向量化：](#文本向量化)
    - [自定义jieba词库示例:](#自定义jieba词库示例)
    - [句向量示例:](#句向量示例)
    - ["hfl/chinese-electra-180g-base-discriminator"模型简介:](#hflchinese-electra-180g-base-discriminator模型简介)
  - [同义词替换构建新语句：](#同义词替换构建新语句)
    - [tensor转list:](#tensor转list)
  - [以缓存方式加载模型:](#以缓存方式加载模型)
    - [huggingface 加载缓存模型的路径查看:](#huggingface-加载缓存模型的路径查看)
    - [huggingface 加载缓存模型的文件名:](#huggingface-加载缓存模型的文件名)
  - ["模型压缩时，同等QPS目标下，降低推理显存占用。"这句话中的"QPS"是什么意思？](#模型压缩时同等qps目标下降低推理显存占用这句话中的qps是什么意思)

## dataset：
如果数据集较小，会放在项目文件中。如果数据集较大，会放在 dataset 文件夹下。如果遇到项目文件中缺少数据集，请在 dataset 文件夹下寻找对应网盘链接下载。<br>

## "epoch"、"batch_size"、"step"这3者是什么，相互之间有什么换算关系吗？

在机器学习和深度学习中，"epoch"、"batch_size"和"step"是三个基本且相互关联的概念。下面是它们的定义及相互之间的关系：<br>

1. **Epoch (时代/轮次)**:

- **定义**: 一个epoch指的是整个数据集被遍历一次的过程。简单来说，如果你有1000个样本，并且你已经用这1000个样本训练了你的模型一次，那么就完成了一个epoch。

- **作用**: 多个epochs意味着模型将多次学习整个数据集。通常需要多个epochs来确保模型学习到数据中的模式。

2. **Batch Size (批量大小)**:

- **定义**: Batch size是指在更新模型参数前，你将要喂给模型的样本数量。例如，如果你的batch size是50，这意味着你每次会向模型提供50个样本，然后模型一次性更新一次参数。

- **作用**: 较小的batch size通常会提供更好的训练效果，但可能会更慢，并且训练过程可能不稳定。较大的batch size可以加快训练速度，但可能会导致模型性能略有下降。

3. **Step (步骤/迭代)**:

- **定义**: 一个step是指一次参数更新，在一个batch的数据上进行一次前向和后向传播。简单来说，每处理一个batch的数据并更新一次模型，就完成了一个step。

- **作用**: Steps用来衡量在一个epoch内，模型的更新次数。

**相互之间的换算关系**:

- **步骤数(Steps per Epoch) = 样本总数 / 批量大小 (Total Samples / Batch Size)**。这意味着如果你有1000个样本，并且你的batch size是100，那么每个epoch将有10个steps。

- 在每个epoch结束时，所有的steps加起来就会遍历整个数据集一次。

- 通常情况下，增加epochs的数量会使模型有更多的机会学习数据，而调整batch size会影响模型的学习速度和稳定性。

理解这三个概念及其关系对于设置和调整深度学习模型的训练过程是非常重要的。<br>


### 我看到很多代码都是一个 "epoch" 结束后更新一次模型，用到 "step" 的情况很少。

确实，在某些训练场景中，模型在每个epoch结束后更新是比较常见的做法，尤其是在一些简单的或者传统的机器学习模型中。<br>

这种情况下，模型在看过所有的训练数据后，即完成一个完整的epoch，然后根据这一轮的学习进行一次参数更新。这种方法简单直观，🚨🚨🚨**但在深度学习尤其是在处理大型数据集时，每个epoch更新一次可能不是最有效或最实用的方法。**<br>

对于深度学习，尤其是在大型数据集上训练复杂的神经网络时，通常使用的是基于"step"的更新，即每处理一批数据就更新一次模型（也就是每个step）。这样做的理由包括：<br>

1. **内存限制**: 大型数据集可能无法一次性完全加载到内存中。使用batch size可以有效管理内存使用，同时也允许GPU更高效地进行计算。

2. **更快的收敛**: 通过更频繁地更新（即每个batch后更新而不是每个epoch后更新），模型可以更快地收敛。这意味着模型在学习时可以更快地调整其权重，从而可能在更短的时间内达到较好的性能。

3. **稳定性和性能**: 较小的batch size可以提供更稳定和更好的训练性能，尽管训练时间可能会更长。此外，某些优化算法（如SGD及其变体）在处理每个batch时都需要更新，以保持动态和适应性。

4. **早期停止**: 当使用step更新时，你可以更频繁地监控模型的性能，并在满足某些条件（如验证损失不再改善）时早期停止训练，这有助于避免过拟合。

在实际应用中，是否使用epoch更新还是step更新取决于具体的应用场景、数据集大小、模型复杂性以及计算资源等因素。在某些情况下，研究人员和工程师可能会根据需要在这两种策略之间进行选择和调整。<br>


## 知识拓展--在NLP领域，什么因素决定了模型的输入长度？

在自然语言处理（NLP）领域，模型的输入长度受到多种因素的影响，主要包括以下几点：<br>

1. **模型架构**：不同的NLP模型架构对输入长度有不同的限制。例如，传统的RNN（循环神经网络）在处理长序列时会遇到梯度消失或梯度爆炸的问题，从而限制了它们处理长输入序列的能力。而基于Transformer的模型，如BERT或GPT系列，虽然能够处理相对更长的序列，但它们仍然有固定的最大输入长度限制，这主要由模型的位置编码和内存限制决定。

2. **位置编码**：Transformer模型通过位置编码来捕获序列中单词的顺序信息。在许多模型实现中，位置编码的长度是预先定义的，这直接限制了模型能够处理的最大序列长度。

3. **内存和计算资源**：处理长序列需要大量的内存和计算资源。模型输入长度的增加会导致计算复杂度和内存需求成倍增长，特别是对于基于Transformer的模型，其自注意力机制的计算复杂度和内存需求是输入长度的平方级别。因此，硬件资源的限制也是决定模型输入长度的一个重要因素。

4. **任务需求和数据特性**：不同的NLP任务和数据集特性也会影响模型输入长度的选择。例如，一些任务可能需要分析长文本（如文档分类或问答系统中的文本理解），而其他任务（如情感分析）可能只需要较短的文本片段。此外，数据的语言和结构也会影响到合适的输入长度。

5. **效率和性能平衡**：虽然较长的输入可以提供更多的上下文信息，有助于模型更好地理解文本，但这也可能导致计算效率降低和训练难度增加。因此，在实际应用中，需要在模型性能和计算效率之间找到一个平衡点，这通常通过实验来确定最优的输入长度。

总的来说，模型的输入长度是由模型架构、技术限制、任务需求和效率考虑等多个因素共同决定的。在设计或选择NLP模型时，需要根据具体任务的需求和可用资源来合理设置输入长度。<br>

### 为什么chatgpt可以用几千甚至几万长度的输入:

ChatGPT，基于OpenAI的GPT（Generative Pre-trained Transformer）模型，能够处理几千甚至几万长度的输入，这得益于几个关键技术和设计选择：<br>

1. **稀疏注意力机制**：虽然标准的Transformer模型使用的全自注意力机制限制了它处理长序列的能力（由于内存和计算成本随序列长度平方增长），但通过采用稀疏注意力机制，GPT能够有效地减少计算复杂度和内存使用。稀疏注意力通过仅在序列的子集上执行注意力计算来实现，从而允许模型处理更长的文本序列。

2. **分块处理**：为了处理长文本，ChatGPT可以将输入文本分割成较小的块或片段，这些块可以独立地被模型处理。然后，模型可以通过某种形式的状态管理或上下文融合技术来整合这些块的输出，以生成连贯的回复。这种方法允许模型间接地处理超出其最大输入长度限制的文本。

3. **内存和上下文缓存机制**：某些Transformer模型的变体，如GPT-3及其后续版本，采用了改进的内存管理和上下文缓存机制，使模型能够在处理连续对话或长文本时“记住”先前的上下文。这意味着模型可以在不同时间点访问和参考之前的输入，即使这些输入在一个操作步骤中超过了模型的标准输入限制。

4. **模型和框架优化**：通过软件和硬件优化，如更高效的矩阵乘法操作、更好的内存管理策略和使用专门的硬件（如GPU或TPU），可以进一步提高模型处理长序列的能力。这些优化有助于降低处理长输入时的延迟和资源需求。

5. **动态注意力窗口和层次化注意力**：一些研究提出了动态调整注意力窗口大小的方法，或者通过层次化的注意力结构来有效处理长距离依赖，这些技术可以进一步提升模型处理长序列的能力。

这些技术和设计策略的组合使得ChatGPT能够有效处理长输入序列，即使是几千到几万个字符的长度，从而在多轮对话、长文本理解和生成等任务中表现出色。然而，值得注意的是，处理非常长的输入仍然会受到实际计算资源和效率的限制。<br>


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

## 以缓存方式加载模型:

工作中你可能会遇到要在无法连网的机器上加载 `transformer` 模型的情况，如果你的机器无法自动从 `huggingface` 下列模型，会提示类似以下错误:<br>

```txt
OSError: We couldn't connect to 'https://huggingface.co' to load this file, couldn't find it in the cached files and it looks like hfl/chinese-electra-180g-small-discriminator is not the path to a directory containing a file named config.json.
Checkout your internet connection or see how to run the library in offline mode at 'https://huggingface.co/docs/transformers/installation#offline-mode'.
```

更为复杂的情况为，代码把 `hugging face` 的模型当作模型组件的一部分，你无法显式写入模型路径，只能通过本地缓存加载，此时你就可以使用下列方式:<br>

以下列代码为例:<br>

```python
from transformers import BertModel, BertTokenizer

# 设定模型名称
model_name = "bert-base-uncased"

# 加载分词器和模型
# 这两个函数会首先检查本地缓存中是否有指定的模型和分词器
# 如果没有，它们会从互联网下载并存入本地缓存
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)
```

代码运行后，会在本地 `~/.cache/huggingface/hub/` 路径下生成一个 `models--bert-base-uncased` 文件夹，文件夹下具体的内容为:<br>

> 这里指的是你的电脑能自动从 huggingface 下载模型，如果自动下载模型失败，会生成 `models--bert-base-uncased` 文件夹，但内容为空。

```txt
├── models--bert-base-uncased
│   ├── blobs
│   │   ├── 097417381d6c7230bd9e3557456d726de6e83245ec8b24f529f60198a67b203a
│   │   ├── 45a2321a7ecfdaaf60a6c1fd7f5463994cc8907d
│   │   ├── a661b1a138dac6dc5590367402d100765010ffd6
│   │   └── fb140275c155a9c7c5a3b3e0e77a9e839594a938
│   ├── refs
│   │   └── main
│   └── snapshots
│       └── 1dbc166cf8765166998eff31ade2eb64c8a40076
│           ├── config.json -> ../../blobs/45a2321a7ecfdaaf60a6c1fd7f5463994cc8907d
│           ├── pytorch_model.bin -> ../../blobs/097417381d6c7230bd9e3557456d726de6e83245ec8b24f529f60198a67b203a
│           ├── tokenizer_config.json -> ../../blobs/a661b1a138dac6dc5590367402d100765010ffd6
│           └── vocab.txt -> ../../blobs/fb140275c155a9c7c5a3b3e0e77a9e839594a938
└── version.txt
```

🚨🚨🚨注意:<br>

所有文件都不要修改，文件是含有软链接的，不要修改，`snapshots` 下的文件夹名称(`1dbc166cf...`)也不要修改，虽然你看不懂，但transformer加载模型可识别，不同模型的文件名不一样，但**相同模型在不同机器上缓存的名称是一致的。**<br>

如果你的电脑无法连网，可以找一个可以连网的电脑，运行上述代码，然后将文件完整上传至 `无法连网的那台电脑` ，上传路径为 huggingface 加载缓存模型的路径!<br>

### huggingface 加载缓存模型的路径查看:

如果你不知道个人电脑 huggingface 加载缓存模型的路径，可以运行下列代码:<br>

```python
from transformers.file_utils import default_cache_path

# 打印出 transformers 默认缓存目录的路径
print(default_cache_path)
```

笔者本地运行上述代码后，终端显示:<br>

```txt
/Users/peilongchencc/.cache/huggingface/hub
```

笔者在服务器运行上述代码后，终端显示:<br>

```txt
/root/.cache/huggingface/hub
```

### huggingface 加载缓存模型的文件名:

huggingface 加载缓存模型的文件名与代码的写法有关，假设你使用下列代码:<br>

```python
from transformers import AutoModel

model = AutoModel.from_pretrained("hfl/chinese-electra-180g-small-discriminator")
```

在 `/Users/peilongchencc/.cache/huggingface/hub` 路径下生成的文件夹名称为 `models--hfl--chinese-electra-180g-small-discriminator`，文件夹下具体内容为:<br>

```txt
.
├── models--hfl--chinese-electra-180g-small-discriminator
│   ├── blobs
│   │   ├── 66051e65c65b3ec5e0b437496d1e545c5d8934b4
│   │   ├── 9e26dfeeb6e641a33dae4961196235bdb965b21b
│   │   ├── b8f933dc8a91286e134ef5a2fd969a631f3ca649
│   │   ├── ca4f9781030019ab9b253c6dcb8c7878b6dc87a5
│   │   ├── e7b0375001f109a6b8873d756ad4f7bbb15fbaa5
│   │   └── eba64ab600f7bb029b38ac391b35651e3b55f185
│   ├── refs
│   │   └── main
│   └── snapshots
│       └── 826a243f3f387450ef8d70de9c3d0706d8d8e924
│           ├── added_tokens.json -> ../../blobs/9e26dfeeb6e641a33dae4961196235bdb965b21b
│           ├── config.json -> ../../blobs/b8f933dc8a91286e134ef5a2fd969a631f3ca649
│           ├── special_tokens_map.json -> ../../blobs/e7b0375001f109a6b8873d756ad4f7bbb15fbaa5
│           ├── tokenizer.json -> ../../blobs/eba64ab600f7bb029b38ac391b35651e3b55f185
│           ├── tokenizer_config.json -> ../../blobs/66051e65c65b3ec5e0b437496d1e545c5d8934b4
│           └── vocab.txt -> ../../blobs/ca4f9781030019ab9b253c6dcb8c7878b6dc87a5
└── version.txt
```

## "模型压缩时，同等QPS目标下，降低推理显存占用。"这句话中的"QPS"是什么意思？

在"模型压缩时，同等QPS目标下，降低推理显存占用"这句话中，"QPS"指的是每秒查询量（Queries Per Second）。<br>

它是衡量信息系统处理能力的指标之一，特别是在网络服务和数据库管理领域，用来描述系统每秒可以处理的查询或请求的数量。<br>

在这个上下文中，提到的是在保持每秒处理相同数量的查询（即维持QPS）的同时，通过模型压缩降低模型在进行推理时所需的显存占用。这通常意味着在保持性能的同时优化模型的效率和资源使用。<br>
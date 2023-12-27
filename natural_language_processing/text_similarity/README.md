# 文本相似度
- [文本相似度](#文本相似度)
  - [数据:](#数据)
    - [两个类别相似程度数据表述:](#两个类别相似程度数据表述)
    - [多个类别相似程度数据标注:](#多个类别相似程度数据标注)
  - [训练:](#训练)
    - [问题描述:](#问题描述)
    - [问题解答:](#问题解答)
  - [词向量转化：](#词向量转化)
    - [单一文本转词向量：](#单一文本转词向量)
    - [批量文本转词向量：](#批量文本转词向量)
    - [单一文本转词向量和批量转词向量的区别：](#单一文本转词向量和批量转词向量的区别)
  - [本地应用层实现余弦相似度的计算：](#本地应用层实现余弦相似度的计算)

## 数据:

### 两个类别相似程度数据表述:

创建用于训练中文文本相似度模型的示例数据对时，你需要确保数据反映了各种各样的相似度情况。以下是5对示例数据，包括文本对以及它们的相似度标签（1表示相似，0表示不相似）：<br>

```txt
文本1: "我喜欢吃苹果。"，文本2: "我爱吃苹果。"，相似度: 1
文本1: "明天你有空吗？"，文本2: "你明天有计划吗？"，相似度: 1
文本1: "猫是很可爱的动物。"，文本2: "狗是人类的好朋友。"，相似度: 0
文本1: "我去书店买了一本小说。"，文本2: "我在图书馆借了一本历史书。"，相似度: 0
文本1: "他因为生病没来上班。"，文本2: "他生病了，所以没能来工作。"，相似度: 1
```

### 多个类别相似程度数据标注:

将“相似程度”划分为多个类别时，你可以根据任务的复杂性和具体需求选择类别数。通常，可以分为3到5类，以捕捉不同程度的相似性。以下是一个可能的分类方式及其中文名：<br>

1. **非常相似（极高相似度）**：文本几乎或完全相同，意思和用词极为接近，可以视为同一意思。
2. **相似（高相似度）**：文本在主题或意思上相近，但可能用词、结构或细节有所不同。
3. **部分相似（中等相似度）**：文本在某些方面有共同点，但也有明显的不同之处。
4. **略有相似（低相似度）**：文本之间有一定联系，但差异较大，只在很有限的方面相似。
5. **完全不相似（无相似度）**：文本之间没有明显的相关性或相似之处。


选择具体的类别数和名称取决于你的具体需求和数据的特性。在实际应用中，可能需要根据模型的性能和任务的具体需求进行调整。<br>

例如，如果你的数据或应用场景不需要非常细致的区分，可能只需要3个类别（高相似度、中等相似度、低相似度）。另一方面，如果任务需要非常精细的相似度判断，那么5类或更多类别可能更合适。在确定类别时，也应考虑数据的可用性和平衡性，确保每个类别都有足够的训练样本。<br>


以下是20对使用5类标注方式的中文文本相似度训练示例数据。每对文本后面的数字代表相似程度类别，从1（非常相似）到5（完全不相似）。<br>

```txt
文本1: "今天天气真好。"，文本2: "今天天气真不错。"，标注: 1
文本1: "我喜欢看科幻小说。"，文本2: "科幻小说是我的最爱。"，标注: 1
文本1: "他明天要去北京出差。"，文本2: "他计划明天出差到北京。"，标注: 2
文本1: "猫是非常可爱的宠物。"，文本2: "小猫真是太可爱了。"，标注: 2
文本1: "请问你能把窗户关上吗？"，文本2: "能帮我把窗户关掉吗？"，标注: 1
文本1: "我昨天去图书馆学习了。"，文本2: "昨天我在家里看书。"，标注: 3
文本1: "他很喜欢打篮球。"，文本2: "打篮球是他的爱好。"，标注: 1
文本1: "手机没电了，我得充电。"，文本2: "电池快没了，需要充电了。"，标注: 2
文本1: "这本书我已经读过了。"，文本2: "我之前看过这书。"，标注: 1
文本1: "明天是他的生日。"，文本2: "他的生日在下周。"，标注: 5
文本1: "这道题真难，我解不出来。"，文本2: "这个问题太难了，我不会做。"，标注: 2
文本1: "她决定去旅行放松一下。"，文本2: "她打算出去旅游放松心情。"，标注: 2
文本1: "他是我们班的学习委员。"，文本2: "学习委员是他。"，标注: 1
文本1: "我喜欢热闹的地方。"，文本2: "我更喜欢安静的环境。"，标注: 5
文本1: "这件衣服的质量很差。"，文本2: "这衣服质量不好。"，标注: 1
文本1: "他们正在讨论新项目。"，文本2: "新项目是他们讨论的重点。"，标注: 2
文本1: "她很少来这里。"，文本2: "她经常来这儿。"，标注: 5
文本1: "周末你有什么计划？"，文本2: "你周末打算做什么？"，标注: 2
文本1: "他因为生病没来上课。"，文本2: "他生病了，所以没有来上课。"，标注: 1
文本1: "太阳快下山了。"，文本2: "太阳快要落山了。"，标注: 1
```

这些示例覆盖了从非常相似到完全不相似的不同场景，可以帮助你的模型学习识别不同程度的文本相似性。在实际应用中，你可能需要根据特定任务和数据集的特点调整类别的划分和描述。同时，确保数据集中每个类别都有足够的样本，这对于训练一个均衡且性能良好的模型非常重要。<br>


## 训练:

### 问题描述:

我使用albert进行中文文本相似度计算，但效果不理想，我想要fine-tune一下模型，应该怎么做呢？<br>

### 问题解答:

要使用ALBERT模型进行中文文本相似度计算并进行fine-tuning，你可以按照以下步骤进行：<br>

1. **收集数据**：你需要收集或创建一个中文文本相似度数据集。这个数据集应该包含文本对以及它们的相似度标签（例如，相似、不相似）。

2. **预处理数据**：将你的数据预处理成ALBERT模型能理解的格式。这可能包括文本清洗、分词、转换成模型输入格式等。

3. **下载并加载预训练的ALBERT模型**：你可以从模型库（如Hugging Face Models）中下载预训练的中文ALBERT模型。

4. **模型fine-tuning**：

- **设置训练参数**：选择适当的学习率、批次大小、训练轮次等。

- **模型适配**：根据你的任务调整ALBERT模型的头部（通常是添加一个或多个全连接层来进行分类）。

- **开始fine-tuning**：使用你的数据集对模型进行训练。

5. **评估模型**：在验证集或测试集上评估fine-tuned模型的性能，确保模型泛化能力强，没有过拟合。

6. **应用模型**：将fine-tuned模型部署到实际应用中，进行文本相似度计算。

在整个过程中，你可能需要进行多次实验，调整数据处理方式、模型参数和训练策略，以获得最佳性能。此外，也可以考虑使用更多的数据增强技术或尝试其他预训练语言模型以改善效果。<br>


## 词向量转化：

这里以`albert`模型简单示范一下将文本转化为词向量的方法:<br>

### 单一文本转词向量：

```python
from transformers import BertTokenizer, AlbertModel
import torch
import numpy as np

class Convert_Text_2_Vector:
    
    tokenizer = BertTokenizer.from_pretrained("semantic/clue/albert_chinese_tiny")
    model = AlbertModel.from_pretrained("semantic/clue/albert_chinese_tiny")
    
    def __init__(self):
        pass
    def convert_to_vec(self, user_input):
        inputs = self.tokenizer(user_input, return_tensors='pt')
        with torch.no_grad():
                outputs = self.model(**inputs)
        data = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
        data = data / np.linalg.norm(data, axis=0)
        data = [data.tolist()]  # 数据格式为: [[-0.05411861091852188, 0.048285916447639465, -0.029383817687630653, ...]]
        return data
```

### 批量文本转词向量：

```python
class Convert_Batch_Text_2_Vector:
    """将文本以batch方式转为词向量,注意以batch方向转词向量需要消除padding的影响
    """
    tokenizer = BertTokenizer.from_pretrained("semantic/clue/albert_chinese_tiny")
    model = AlbertModel.from_pretrained("semantic/clue/albert_chinese_tiny")
    
    def __init__(self):
        pass
    def convert_batch_to_embed(self, text_data, batch_size, collection, intentId = None, code = None):
        """将文本以batch方式转为词向量
        Args:
            text_data: 待转化的文本,数据类型要求为list,例如:
                [
                    问句1,
                    问句2,
                    词语1,
                    词语2,
                    ...
                ]
            batch_size: batch大小
            collection: 准备插入的milvus集合
        Return:
            None: 由于执行的是插入操作,无返回值
        """
        # 检查text_data是否是字符串，如果是，则创建一个相应的列表
        if isinstance(text_data, str):
            text_data = [text_data]
        # 获取待转化文本的长度，用于做batch切分
        num_texts = len(text_data)
        
        # 检查intentId是否是单一数字，如果是，则创建一个相应的列表
        if isinstance(intentId, int):
            intentId = [intentId]
        # 当词语或问句没有意图id时，创建一个与文本数量相同的intentId列表，每个元素都为`-1`
        elif intentId is None:
            intentId = [-1] * num_texts
        
        if isinstance(code, str):
            code = [code]
        # 当词语或问句没有wjt_id时
        elif code is None:
            code = ['-1'] * num_texts
        
        print(f"\n开始进行词向量批量转化，并按批次写入Milvus的{collection.name}集合中---\n")
        # 记录词向量转化开始时间
        start_time = time.time() 
        for i in tqdm(range(0, num_texts, batch_size)):
            
            # 将数据拆分
            batch_texts = text_data[i:i + batch_size]
            batch_intentId = intentId[i:i + batch_size]
            batch_code = code[i:i + batch_size]
            
            # 进行token操作
            encoded_texts = self.tokenizer(batch_texts, return_tensors='pt', padding=True)
            with torch.no_grad():
                # 通过模型获取文本的隐藏状态
                last_hidden_state = self.model(**encoded_texts).last_hidden_state
                # 获取注意力掩码
                attention_mask = encoded_texts["attention_mask"]
                # 将隐藏状态与注意力掩码相乘，用于消除padding的影响
                last_hidden_state = last_hidden_state * attention_mask.unsqueeze(-1)
                # 对隐藏状态求和，用于获得整个文本的表示
                sum_hidden_state = last_hidden_state.sum(dim=1).squeeze()
                # 通过注意力掩码的和进行归一化
                output = sum_hidden_state / attention_mask.sum(dim=1, keepdim=True)
                # 转化为numpy数组
                output = output.numpy()
            # 归一化输出向量，以便向量的模长为1
            output = output / np.linalg.norm(output, axis=1, keepdims=True).tolist()
```


### 单一文本转词向量和批量转词向量的区别：

在进行词向量转换时，批量处理和单一文本处理存在一些差异，主要原因在于数据处理和模型输入的需要，批量处理需要进行padding。<br>

1. **批量处理时为什么需要Padding**:

- **统一长度**：深度学习模型通常需要输入数据具有相同的维度。在批量处理时，不同的文本可能有不同的长度，因此为了使它们的长度统一，较短的文本会通过padding（填充）来增加长度，以匹配到批量中最长的文本。

- **效率**：使用相同长度的批量数据可以提高计算效率，因为这允许模型以固定的形状处理多个数据样本，从而更高效地使用计算资源。

- **GPU优化**：在使用GPU进行计算时，具有统一维度的数据可以更好地并行处理，从而提高处理速度。

2. **单一文本处理时为什么不需要Padding**:

- **单个输入**：当只处理一个文本时，不存在长度不一致的问题。模型可以直接根据该文本的实际长度进行处理，无需进行任何填充。

- **灵活性**：单个文本处理更加灵活，不需要考虑与其他文本的长度匹配问题，因此可以直接根据文本本身的长度进行词向量转换。

- **资源利用**：在单个文本处理中，资源利用不是主要考虑因素，因为没有并行处理多个文本的需求。

综上所述，padding主要是为了处理多个文本时，确保它们具有统一的长度，从而便于深度学习模型的高效处理。而在单个文本处理时，由于不存在长度不一致的问题，因此不需要进行padding。<br>

🚀🚀🚀注意:<br>

这两种方式对同一个文本转换成的词向量是相同的，对于同一个文本，无论是单独处理还是作为批量处理的一部分，其生成的词向量通常是相同的。<br>

当然，前提是在两种情况下使用了相同的词向量模型和相同的处理流程。🪴🪴🪴🪴🪴<br>

🚨🚨🚨补充:<br>

进行了padding之后是否需要消除padding的影响，这取决于你使用的模型和应用场景。在某些情况下，padding是必要的，并且其影响是被模型内部处理的；在其他情况下，则可能需要采取措施来减少padding的影响。<br>

## 本地应用层实现余弦相似度的计算：

```python
import sys
import os

# 获取当前脚本的绝对路径
current_script_path = os.path.abspath(__file__)
# 获取当前脚本的父目录的父目录
parent_directory_of_the_parent_directory = os.path.dirname(os.path.dirname(current_script_path))
# 将这个目录添加到 sys.path
sys.path.append(parent_directory_of_the_parent_directory)

from albert_text_vec import Convert_Text_2_Vector

# 词向量转化类的实例化
embed_model = Convert_Text_2_Vector()

# 获取用户数据
usr_text = "定投的优势"
# 将用户数据转为向量
usr_text_vector = embed_model.convert_to_vec(usr_text)

# 获取待比较数据
# to_be_compare_text = "定投的优势是什么"
to_be_compare_text = "单只基金的业绩走势在哪看"
# 将待比较数据转为向量
to_be_compare_text_vector = embed_model.convert_to_vec(to_be_compare_text)


from sklearn.metrics.pairwise import cosine_similarity

# 计算余弦相似度
similarity = cosine_similarity(usr_text_vector, to_be_compare_text_vector)
print("相似度: ", similarity[0][0])
```

如果你没有安装`scikit-learn`，需要运行下列指令先安装:<br>

```bash
conda install scikit-learn
```


在 Milvus 中计算余弦相似度与我这里提供的 Python 代码计算方式可能存在微小差异。这种差异可能源于以下几个方面：<br>

1. **数值精度和浮点运算**：在不同的系统或库中进行浮点数运算时，由于底层实现和数值精度的不同，可能会出现微小的差异。Milvus 可能在内部使用不同的优化和浮点精度设置，这可能导致与 `sklearn` 库的结果略有不同。

2. **索引和搜索策略**：Milvus 使用特定的索引结构来优化搜索。当你在 Milvus 中构建索引并执行搜索时，它可能采用一些近似算法以提高搜索效率，这可能会导致与直接计算余弦相似度的结果有轻微差异。

3. **版本差异**：不同版本的 Milvus 可能在底层实现上有所不同，这也可能会影响计算结果。

总的来说，如果差异不大，这通常是正常的，因为在实际应用中，完全匹配的余弦相似度得分并不总是必需的。实际上，微小的差异通常不会对大多数应用产生重大影响。如果你需要更精确的控制或理解这些差异，可能需要查看 Milvus 的具体实现细节或联系其技术支持。<br>
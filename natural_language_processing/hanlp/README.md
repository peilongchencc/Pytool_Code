# HanLP
由于工作原因，笔者有时会利用 `HanLP` 做一些测试，但也仅仅是做一些测试，所以这里不会详细介绍 `HanLP` 中的模型原理。<br>
- [HanLP](#hanlp)
  - [HanLP的安装：](#hanlp的安装)
    - [Mac安装HanLP](#mac安装hanlp)
  - [分词：](#分词)
    - [模型下载问题：](#模型下载问题)
    - [根据自定义词库分词：](#根据自定义词库分词)
  - [语义文本相似度：](#语义文本相似度)
  - [语义依存分析(sdp):](#语义依存分析sdp)
    - [单个输入的语义依存分析：](#单个输入的语义依存分析)
    - [多个输入的语义依存分析：](#多个输入的语义依存分析)
  - [多任务模型：](#多任务模型)
  - [流水线模式--pipeline：](#流水线模式--pipeline)
    - [分句型pipeline:](#分句型pipeline)
    - [分句函数的具体代码：](#分句函数的具体代码)
    - [列表形式输入：](#列表形式输入)
    - [修改pipeline中插入的hanlp内置函数：](#修改pipeline中插入的hanlp内置函数)
    - [在pipeline插入自定义函数：](#在pipeline插入自定义函数)
    - [分词+语义依存分析的pipeline构建：](#分词语义依存分析的pipeline构建)

`HanLP` 的 `RESTful API` 用法笔者不做介绍，因为 `RESTful API` 有使用次数限制，这里只介绍 `HanLP Native` 形式的使用。<br>

## HanLP的安装：

Ubuntu 系统安装 `HanLP` 很简单，终端运行下列指令即可：<br>

```bash
pip install hanlp
```

### Mac安装HanLP

Mac如果直接使用 `pip install hanlp[full] -U` 指令安装HanLP报错，可以改为使用引号包裹起命令中的参数：<br>

```bash
pip install 'hanlp[full]' -U
```

推测原因为zsh对**方括号**进行了拓展，所以需要利用单引号或双引号将`hanlp[full]`包裹。<br>

## 分词：

标准分词方式参考如下代码，：<br>

```python
import hanlp
Segment = hanlp.load(hanlp.pretrained.tok.FINE_ELECTRA_SMALL_ZH)
res = Segment(['急性肠胃炎要如何治疗？','盛剑环境的股价太高了。'])
print(res)
```

终端效果：<br>

```shell
[['急性', '肠胃炎', '要', '如何', '治疗', '？'], ['盛剑', '环境', '的', '股价', '太', '高', '了', '。']]
```

### 模型下载问题：

需要注意，因为 `hanlp` 的源部署在国外，如果你的代码是在服务器上运行，在用到hanlp模型时，可能出现无法自动下载的情况。<br>

这是因为hanlp的源对你的服务器ip进行了限制，例如阿里云服务器就无法自动下载hanlp模型。<br>


解决方法也很简单：根据终端卡住位置的网址自行下载模型，然后放到终端提示的位置即可。<br>

再次运行代码，程序会帮你自动解压下载的文件。<br>

### 根据自定义词库分词：

如果你想要加入自定义词库，可以通过 `dict_force = None` 参数进行控制，`dict_force = None` 会在统计模型的分词结果上执行**最长匹配**并合并匹配到的词条。<br>

`dict_force = None` 的用法为：当将“美国总统”加入 `dict_combine` 后，会合并['美国', '总统']，而不会合并['美国', '总', '统筹部']为['美国总统', '筹部']。<br>

具体代码示例如下：<br>

```python
import hanlp
Segment = hanlp.load(hanlp.pretrained.tok.FINE_ELECTRA_SMALL_ZH)
Segment.dict_force = None
Segment.dict_combine = {'急性肠胃炎','盛剑环境'}
res = Segment(['急性肠胃炎要如何治疗？','盛剑环境的股价太高了。'])
print(res)
```

终端效果：<br>

```python
[['急性肠胃炎', '要', '如何', '治疗', '？'], ['盛剑环境', '的', '股价', '太', '高', '了', '。']]
```

## 语义文本相似度：

```python
import hanlp
# 语义文本相似度(Semantic text similarity)
HanLP = hanlp.load(hanlp.pretrained.sts.STS_ELECTRA_BASE_ZH)

doc = HanLP([
    ('急性肠胃炎要如何治疗？', '盛剑环境的股价太高了。'),
    ('看图猜一电影名', '看图猜电影'),
    ('无线路由器怎么无线上网', '无线上网卡和无线路由器怎么用'),
    ('北京到上海的动车票', '上海到北京的动车票'),
    ])
print(doc)  # 结果为 list 类型
```
终端效果：<br>
```log
[0.0, 0.9764468669891357, 0.0, 0.003458678722381592]
```

## 语义依存分析(sdp):
`HanLP` 语义依存分析任务的输入必须为分词后的结果，可以为单个输入和多个输入进行语义依存分析任务，终端的输出效果是不一样的。接下来，我依次演示：<br>

### 单个输入的语义依存分析：
```python
import hanlp
# 语义依存分析(Semantic Dependency Parsing)
Segment = hanlp.load(hanlp.pretrained.tok.FINE_ELECTRA_SMALL_ZH)
Segment.dict_force = None
Segment.dict_combine = {'急性肠胃炎'}
res = Segment('急性肠胃炎要如何治疗？')
print(res)  # ['急性肠胃炎', '要', '如何', '治疗', '？']

HanLP = hanlp.load('SEMEVAL16_ALL_ELECTRA_SMALL_ZH')
graphs = HanLP(res)
print(graphs)
print(type(graphs))
```

终端效果：<br>

```shell
['急性肠胃炎', '要', '如何', '治疗', '？']
1       急性肠胃炎      _       _       _       _       _       _       4:Pat   _
2       要      _       _       _       _       _       _       4:mMod  _
3       如何    _       _       _       _       _       _       4:Mann  _
4       治疗    _       _       _       _       _       _       0:Root  _
5       ？      _       _       _       _       _       _       4:mPunc _
<class 'hanlp_common.conll.CoNLLSentence'>
```

相信你已经注意到了，我打印出了 `graphs` 的类型，类型为 `hanlp_common.conll.CoNLLSentence` 类，如果你需要提取需要的内容组成三元组，可以参考 `"分词+语义依存分析的pipeline构建"` 那一节中的内容。<br>

### 多个输入的语义依存分析：

```python
import hanlp
# 语义依存分析(Semantic Dependency Parsing)
Segment = hanlp.load(hanlp.pretrained.tok.FINE_ELECTRA_SMALL_ZH)
Segment.dict_force = None
Segment.dict_combine = {'急性肠胃炎','盛剑环境'}
res = Segment(['急性肠胃炎要如何治疗？','盛剑环境的股价太高了。'])
print(res)  # [['急性肠胃炎', '要', '如何', '治疗', '？'], ['盛剑环境', '的', '股价', '太', '高', '了', '。']]

HanLP = hanlp.load('SEMEVAL16_ALL_ELECTRA_SMALL_ZH')
graphs = HanLP(res)
print(graphs)
print(type(graphs))
print("____________")
```

终端效果：<br>

```shell
[['急性肠胃炎', '要', '如何', '治疗', '？'], ['盛剑环境', '的', '股价', '太', '高', '了', '。']]
[[{'id': 1, 'form': '急性肠胃炎', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(4, 'Pat')], 'misc': None}, {'id': 2, 'form': '要', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(4, 'mMod')], 'misc': None}, {'id': 3, 'form': '如何', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(4, 'Mann')], 'misc': None}, {'id': 4, 'form': '治疗', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(0, 'Root')], 'misc': None}, {'id': 5, 'form': '？', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(4, 'mPunc')], 'misc': None}], [{'id': 1, 'form': '盛剑环境', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(3, 'Desc')], 'misc': None}, {'id': 2, 'form': '的', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(1, 'mAux')], 'misc': None}, {'id': 3, 'form': '股价', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(5, 'Exp')], 'misc': None}, {'id': 4, 'form': '太', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(5, 'mDegr')], 'misc': None}, {'id': 5, 'form': '高', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(0, 'Root')], 'misc': None}, {'id': 6, 'form': '了', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(5, 'mTone')], 'misc': None}, {'id': 7, 'form': '。', 'upos': None, 'xpos': None, 'head': None, 'deprel': None, 'lemma': None, 'feats': None, 'deps': [(5, 'mPunc')], 'misc': None}]]
<class 'list'>
```

## 多任务模型：

直接使用多任务模型，一次运行就可以完成多个任务。需要注意的是‼️‼️‼️：多任务学习的优势在于速度和显存，然而精度往往不如单任务模型。所以，更好的方式是使用HanLP的流水线模式(pipeline)将多个单任务模型组装起来。<br>

多任务模型的调用方式如下：<br>

```python
import hanlp
HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH) # 世界最大中文语料库
res = HanLP(['急性肠胃炎要如何治疗？','盛剑环境的股价太高了。'])
print(res)
```

终端效果：<br>

```txt
{                 
  "tok/fine": [
    ["急性", "肠胃炎", "要", "如何", "治疗", "？"],
    ["盛剑", "环境", "的", "股价", "太", "高", "了", "。"]
  ],
  "tok/coarse": [
    ["急性", "肠胃", "炎", "要", "如何", "治疗", "？"],
    ["盛剑", "环境", "的", "股价", "太", "高", "了", "。"]
  ],
  "pos/ctb": [
    ["JJ", "NN", "VV", "AD", "VV", "PU"],
    ["NR", "NN", "DEG", "NN", "AD", "VA", "SP", "PU"]
  ],
  "pos/pku": [
    ["b", "n", "v", "r", "v", "w"],
    ["nz", "n", "u", "n", "d", "a", "y", "w"]
  ],
  "pos/863": [
    ["a", "n", "v", "r", "v", "w"],
    ["nh", "n", "u", "n", "d", "a", "u", "w"]
  ],
  "ner/msra": [
    [],
    [["盛剑", "PERSON", 0, 1]]
  ],
  "ner/pku": [
    [],
    [["盛剑", "nr", 0, 1]]
  ],
  "ner/ontonotes": [
    [],
    [["盛剑", "PERSON", 0, 1]]
  ],
  "srl": [
    [[["要", "PRED", 2, 3], ["如何治疗", "ARG1", 3, 5]], [["急性肠胃炎", "ARG1", 0, 2], ["如何", "ARGM-ADV", 3, 4], ["治疗", "PRED", 4, 5]]],
    [[["盛剑环境的股价", "ARG0", 0, 4], ["太", "ARGM-ADV", 4, 5], ["高", "PRED", 5, 6]]]
  ],
  "dep": [
    [[2, "amod"], [5, "nsubj"], [5, "mmod"], [5, "advmod"], [0, "root"], [5, "punct"]],
    [[6, "nsubj"], [4, "assmod"], [2, "assm"], [6, "nsubj"], [6, "advmod"], [0, "root"], [6, "dep"], [6, "punct"]]
  ],
  "sdp": [
    [[[2, "Desc"]], [[5, "Pat"]], [[5, "mMod"]], [[5, "Mann"]], [[0, "Root"]], [[5, "mPunc"]]],
    [[[2, "Poss"]], [[4, "Poss"]], [[2, "mAux"]], [[6, "Exp"]], [[6, "mDegr"]], [[2, "Desc"]], [[6, "mTone"]], [[0, "Root"], [6, "mPunc"]]]
  ],
  "con": [
    ["TOP", [["IP", [["NP", [["ADJP", [["JJ", ["急性"]]]], ["NP", [["NN", ["肠胃炎"]]]]]], ["VP", [["VV", ["要"]], ["VP", [["ADVP", [["AD", ["如何"]]]], ["VP", [["VV", ["治疗"]]]]]]]], ["PU", ["？"]]]]]],
    ["TOP", [["CP", [["IP", [["NP", [["NP", [["NR", ["盛剑"]]]], ["NP", [["DNP", [["NP", [["NN", ["环境"]]]], ["DEG", ["的"]]]], ["NP", [["NN", ["股价"]]]]]]]], ["VP", [["ADVP", [["AD", ["太"]]]], ["VP", [["VA", ["高"]]]]]]]], ["SP", ["了"]], ["PU", ["。"]]]]]]
  ]
}
```

## 流水线模式--pipeline：

`pipeline` 模式如果没有指定 `input_key` ，默认将上一步的输出作为输入。参数的传递依靠 `input_key` 和 `ouput_key`，`input_key` 和 `ouput_key` 的变量名可以根据自己的喜好定义。<br>

### 分句型pipeline:

如果你的输入是一个超长的字符串，而你又不知道怎样便捷分句，可以执行以下代码。<br>

```python
import hanlp

HanLP = hanlp.pipeline() \
    .append(hanlp.utils.rules.split_sentence, output_key='sentences') \
    .append(hanlp.load('CTB9_TOK_ELECTRA_SMALL'), output_key='tok') \
    .append(hanlp.load('CTB9_POS_ELECTRA_SMALL'), output_key='pos') \
    .append(hanlp.load('MSRA_NER_ELECTRA_SMALL_ZH'), output_key='ner', input_key='tok') \
    .append(hanlp.load('CTB9_DEP_ELECTRA_SMALL', conll=False), output_key='dep', input_key='tok') \
    .append(hanlp.load('CTB9_CON_ELECTRA_SMALL'), output_key='con', input_key='tok')

# 因为执行了分句，所以输入需要为str
doc = HanLP('急性肠胃炎要如何治疗？盛剑环境的股价太高了。')
print(doc)
# 图形化展示输出
# doc.pretty_print()

# 打印pipeline中间某一步的输出
# print(doc["tok"])
```

终端效果：<br>

```python
{                 
  "sentences": [
    "急性肠胃炎要如何治疗？",
    "盛剑环境的股价太高了。"
  ],
  "tok": [
    ["急性", "肠胃炎", "要", "如何", "治疗", "？"],
    ["盛剑", "环境", "的", "股价", "太", "高", "了", "。"]
  ],
  "pos": [
    ["JJ", "NN", "VV", "AD", "VV", "PU"],
    ["NR", "NN", "DEG", "NN", "AD", "VA", "SP", "PU"]
  ],
  "ner": [
    [],
    [["盛剑", "ORGANIZATION", 0, 1]]
  ],
  "dep": [
    [[2, "amod"], [5, "nsubj"], [5, "mmod"], [5, "advmod"], [0, "root"], [5, "punct"]],
    [[2, "nn"], [4, "assmod"], [2, "assm"], [6, "nsubj"], [6, "advmod"], [0, "root"], [6, "dep"], [6, "punct"]]
  ],
  "con": [
    ["TOP", [["IP", [["NP", [["ADJP", [["_", ["急性"]]]], ["NP", [["_", ["肠胃炎"]]]]]], ["VP", [["_", ["要"]], ["VP", [["ADVP", [["_", ["如何"]]]], ["VP", [["_", ["治疗"]]]]]]]], ["_", ["?"]]]]]],
    ["TOP", [["CP", [["NP", [["DNP", [["NP", [["_", ["盛剑"]], ["_", ["环境"]]]], ["_", ["的"]]]], ["NP", [["_", ["股价"]]]]]], ["VP", [["ADVP", [["_", ["太"]]]], ["VP", [["_", ["高"]]]]]], ["_", ["了"]], ["_", ["。"]]]]]]
  ]
}
```

### 分句函数的具体代码：

```python
import re

_SEPARATOR = r'@'
_RE_SENTENCE = re.compile(r'(\S.+?[.!?])(?=\s+|$)|(\S.+?)(?=[\n]|$)', re.UNICODE)
_AB_SENIOR = re.compile(r'([A-Z][a-z]{1,2}\.)\s(\w)', re.UNICODE)
_AB_ACRONYM = re.compile(r'(\.[a-zA-Z]\.)\s(\w)', re.UNICODE)
_UNDO_AB_SENIOR = re.compile(r'([A-Z][a-z]{1,2}\.)' + _SEPARATOR + r'(\w)', re.UNICODE)
_UNDO_AB_ACRONYM = re.compile(r'(\.[a-zA-Z]\.)' + _SEPARATOR + r'(\w)', re.UNICODE)


def _replace_with_separator(text, separator, regexs):
    replacement = r"\1" + separator + r"\2"
    result = text
    for regex in regexs:
        result = regex.sub(replacement, result)
    return result


def split_sentence(text, best=True):
    text = re.sub(r'([。！？?])([^”’])', r"\1\n\2", text)
    text = re.sub(r'(\.{6})([^”’])', r"\1\n\2", text)
    text = re.sub(r'(…{2})([^”’])', r"\1\n\2", text)
    text = re.sub(r'([。！？?][”’])([^，。！？?])', r'\1\n\2', text)
    for chunk in text.split("\n"):
        chunk = chunk.strip()
        if not chunk:
            continue
        if not best:
            yield chunk
            continue
        processed = _replace_with_separator(chunk, _SEPARATOR, [_AB_SENIOR, _AB_ACRONYM])
        sents = list(_RE_SENTENCE.finditer(processed))
        if not sents:
            yield chunk
            continue
        for sentence in sents:
            sentence = _replace_with_separator(sentence.group(), r" ", [_UNDO_AB_SENIOR, _UNDO_AB_ACRONYM])
            yield sentence
```


### 列表形式输入：

上一节模型输入的限制主要由分句函数决定，分句函数的输入需要是字符串，如果我们去除分句函数，那么可以按照列表的形式传入我们的输入。<br>

```python
import hanlp

HanLP = hanlp.pipeline() \
    .append(hanlp.load('CTB9_TOK_ELECTRA_SMALL'), output_key='tok') \
    .append(hanlp.load('CTB9_POS_ELECTRA_SMALL'), output_key='pos') \
    .append(hanlp.load('MSRA_NER_ELECTRA_SMALL_ZH'), output_key='ner', input_key='tok') \
    .append(hanlp.load('CTB9_DEP_ELECTRA_SMALL', conll=False), output_key='dep', input_key='tok') \
    .append(hanlp.load('CTB9_CON_ELECTRA_SMALL'), output_key='con', input_key='tok')

doc = HanLP(['急性肠胃炎要如何治疗？', '盛剑环境的股价太高了。'])
print(doc)
# 图形化展示输出
# doc.pretty_print()

# 打印pipeline中间某一步的输出
# print(doc["tok"])
```

### 修改pipeline中插入的hanlp内置函数：

以分词为例，在工作中我们经常需要在分词的时候加入自定义词库。如果只使用一个分词模型，加入自定义词库很容易，但如何在pipeline的分词模型中加入自定义词库呢？可以参考以下代码：<br>

> 当你在管道中使用自定义函数时，你只需要将关键字参数(`seg_dict`)传递给它，位置参数（如 `input_list`）会自动由管道进行传递。


```python
import hanlp
segment_dict = {'急性肠胃炎','盛剑环境'}

def segment(input_list,seg_dict):
    Segment = hanlp.load('CTB9_TOK_ELECTRA_SMALL')
    Segment.dict_force = None
    Segment.dict_combine = seg_dict
    res = Segment(input_list)
    return res

HanLP = hanlp.pipeline() \
    .append(segment, output_key='tok', seg_dict=segment_dict) \
    .append(hanlp.load('CTB9_POS_ELECTRA_SMALL'), output_key='pos') \
    .append(hanlp.load('MSRA_NER_ELECTRA_SMALL_ZH'), output_key='ner', input_key='tok') \
    .append(hanlp.load('CTB9_DEP_ELECTRA_SMALL', conll=False), output_key='dep', input_key='tok') \
    .append(hanlp.load('CTB9_CON_ELECTRA_SMALL'), output_key='con', input_key='tok')

doc = HanLP(['急性肠胃炎要如何治疗？', '盛剑环境的股价太高了。'])
print(doc)
# doc.pretty_print()

# 打印pipeline中间某一步的输出
# print(doc["tok"])
```

### 在pipeline插入自定义函数：

加入自定义函数需要注意变量的传递，提取出正确的输入。<br>

```python
import hanlp
segment_dict = {'急性肠胃炎', '盛剑环境'}
my_project_name = "hanlp的pipeline使用测试"

# 自定义一个函数
def custom_function(input_list, pro_name):
    return {
        'my_project_name': f"项目的名称为：{pro_name}",
        'raw_input': input_list  # 返回原始输入
    }

def segment(input_list, seg_dict):
    Segment = hanlp.load('CTB9_TOK_ELECTRA_SMALL')
    Segment.dict_force = None
    Segment.dict_combine = seg_dict
    
    # 获取原始输入
    raw_input = input_list['raw_input']
    segment_result = Segment(raw_input)
    return segment_result

HanLP = hanlp.pipeline() \
    .append(custom_function, output_key='custom_function_result', pro_name=my_project_name)\
    .append(segment, output_key='tok', input_key='custom_function_result', seg_dict=segment_dict) \
    .append(hanlp.load('CTB9_POS_ELECTRA_SMALL'), output_key='pos') \
    .append(hanlp.load('MSRA_NER_ELECTRA_SMALL_ZH'), output_key='ner', input_key='tok') \
    .append(hanlp.load('CTB9_DEP_ELECTRA_SMALL', conll=False), output_key='dep', input_key='tok') \
    .append(hanlp.load('CTB9_CON_ELECTRA_SMALL'), output_key='con', input_key='tok')

doc = HanLP(['急性肠胃炎要如何治疗？', '盛剑环境的股价太高了。'])
print(doc)
print(doc["custom_function_result"]["my_project_name"])
```

终端效果：<br>

```txt
{                 
  "custom_function_result": {
    "my_project_name": "项目的名称为：hanlp的pipeline使用测试",
    "raw_input": ["急性肠胃炎要如何治疗？", "盛剑环境的股价太高了。"]
  },
  "tok": [
    ["急性肠胃炎", "要", "如何", "治疗", "？"],
    ["盛剑环境", "的", "股价", "太", "高", "了", "。"]
  ],
  "pos": [
    ["NN", "VV", "AD", "VV", "PU"],
    ["NR", "DEG", "NN", "AD", "VA", "SP", "PU"]
  ],
  "ner": [
    [],
    [["盛剑环境", "ORGANIZATION", 0, 1]]
  ],
  "dep": [
    [[4, "advmod"], [4, "mmod"], [4, "advmod"], [0, "root"], [4, "punct"]],
    [[3, "assmod"], [1, "assm"], [5, "nsubj"], [5, "advmod"], [0, "root"], [5, "dep"], [5, "punct"]]
  ],
  "con": [
    ["TOP", [["IP", [["NP", [["_", ["急性肠胃炎"]]]], ["VP", [["_", ["要"]], ["VP", [["ADVP", [["_", ["如何"]]]], ["VP", [["_", ["治疗"]]]]]]]], ["_", ["?"]]]]]],
    ["TOP", [["CP", [["NP", [["DNP", [["NP", [["_", ["盛剑环境"]]]], ["_", ["的"]]]], ["NP", [["_", ["股价"]]]]]], ["VP", [["ADVP", [["_", ["太"]]]], ["VP", [["_", ["高"]]]]]], ["_", ["了"]], ["_", ["。"]]]]]]
  ]
}
项目的名称为：hanlp的pipeline使用测试
```

🚨🚨🚨**注意，HanLP的pipeline在构建时，多个参数或输出的写法如下：**<br>

```python
HanLP = hanlp.pipeline() \
    .append(function_1, output_key=('result_1', 'result_2'), input_key=('arg_1', 'arg_2'), seg_dict=segment_dict)
```


### 分词+语义依存分析的pipeline构建：

```python
import hanlp
segment_dict = {'急性肠胃炎','盛剑环境'}

def segment(input_list,seg_dict):
    Segment = hanlp.load('CTB9_TOK_ELECTRA_SMALL')
    Segment.dict_force = None
    Segment.dict_combine = seg_dict
    res = Segment(input_list)
    return res

# pipeline组成为：分词、语义依存分析
HanLP = hanlp.pipeline() \
    .append(segment, output_key='tok', seg_dict=segment_dict) \
    .append(hanlp.load('SEMEVAL16_ALL_ELECTRA_SMALL_ZH'), output_key='sdp')

doc = HanLP(['急性肠胃炎要如何治疗？','盛剑环境的股价太高了。'])
# 提取出我们需要的语义依存分析结果
# print(doc)
need_data = doc['sdp']

# 需要提取的关系
needed_semantic_relation = {
    "Pat": {"mean_zh": "受事", "subject_role": "受事主体", "object_role": "受事客体", "subject_role_id": 1001, "object_role_id": 1002},
    "Exp": {"mean_zh": "当事", "subject_role": "当事主体", "object_role": "当事客体", "subject_role_id": 1003, "object_role_id": 1004},
    "Belg": {"mean_zh": "属事", "subject_role": "属事主体", "object_role": "属事客体", "subject_role_id": 1005, "object_role_id": 1006},
    "Clas": {"mean_zh": "类事", "subject_role": "类事主体", "object_role": "类事客体", "subject_role_id": 1007, "object_role_id": 1008},
    "Cont": {"mean_zh": "客事", "subject_role": "客事主体", "object_role": "客事客体", "subject_role_id": 1009, "object_role_id": 1010},
    "Poss": {"mean_zh": "领事", "subject_role": "领事主体", "object_role": "领事客体", "subject_role_id": 1011, "object_role_id": 1012},
    "Desc": {"mean_zh": "描写角色", "subject_role": "描写主体", "object_role": "描写客体", "subject_role_id": 1013, "object_role_id": 1014},
    "Comp": {"mean_zh": "比较角色", "subject_role": "比较主体", "object_role": "比较客体", "subject_role_id": 1015, "object_role_id": 1016},
    "Mann": {"mean_zh": "方式角色", "subject_role": "方式主体", "object_role": "方式客体", "subject_role_id": 1017, "object_role_id": 1018},
    "eCoo": {"mean_zh": "并列角色", "subject_role": "并列主体", "object_role": "并列客体", "subject_role_id": 1019, "object_role_id": 1020},
    "Quan": {"mean_zh": "数量角色", "subject_role": "数量主体", "object_role": "数量客体", "subject_role_id": 1021, "object_role_id": 1022},
    "Qp": {"mean_zh": "数量组合", "subject_role": "数量组合主体", "object_role": "数量组合客体", "subject_role_id": 1023, "object_role_id": 1024},
    "Host": {"mean_zh": "宿主角色", "subject_role": "宿主主体", "object_role": "宿主客体", "subject_role_id": 1025, "object_role_id": 1026},
    "Time": {"mean_zh": "时间角色", "subject_role": "时间主体", "object_role": "时间客体", "subject_role_id": 1027, "object_role_id": 1028},
    "Loc": {"mean_zh": "空间角色", "subject_role": "空间主体", "object_role": "空间客体", "subject_role_id": 1029, "object_role_id": 1030},
    "Accd": {"mean_zh": "依据角色", "subject_role": "依据主体", "object_role": "依据客体", "subject_role_id": 1031, "object_role_id": 1032},
    "Reas": {"mean_zh": "缘故角色", "subject_role": "缘故主体", "object_role": "缘故客体", "subject_role_id": 1033, "object_role_id": 1034},
    "rReas": {"mean_zh": "反缘故角色", "subject_role": "反缘故主体", "object_role": "反缘故客体", "subject_role_id": 1035, "object_role_id": 1036},
    "mNeg": {"mean_zh": "否定标记", "subject_role": "否定标记主体", "object_role": "否定标记客体", "subject_role_id": 1037, "object_role_id": 1038},
    "Tmod": {"mean_zh": "时间修饰角色", "subject_role": "时间修饰主体", "object_role": "时间修饰客体", "subject_role_id": 1039, "object_role_id": 1040},
    "mTime": {"mean_zh": "时间标记", "subject_role": "时间标记主体", "object_role": "时间标记客体", "subject_role_id": 1041, "object_role_id": 1042},
    "Freq": {"mean_zh": "频率角色", "subject_role": "频率主体", "object_role": "频率客体", "subject_role_id": 1043, "object_role_id": 1044},
    "dExp": {"mean_zh": "嵌套当事", "subject_role": "嵌套当事主体", "object_role": "嵌套当事客体", "subject_role_id": 1045, "object_role_id": 1046}
}


semantic_triples = []
# 按句子获取不同输入的分析结果
for element in need_data:
    # 按分词获取每个分词与其他分词的关系与关系词索引
    for i in element:
        print(i)
        entity_b = i.form                 # 当前词的名称
        # 一个分词可能和多个分词组成关系，i.deps的结果为：[(4, 'Pat'), [6, "Agt"]]
        for each_dep in i.deps:
            entity_a_idx = each_dep[0]-1     # 因HanLP序列后的结果从1开始编号，所以需要-1。
            entity_a = element[entity_a_idx].form
            relation = each_dep[1]
            if relation in needed_semantic_relation:
                mean_zh = needed_semantic_relation[relation]["mean_zh"]
                subject_role = needed_semantic_relation[relation]["subject_role"]
                object_role = needed_semantic_relation[relation]["object_role"]
                subject_role_id = needed_semantic_relation[relation]["subject_role_id"]
                object_role_id = needed_semantic_relation[relation]["object_role_id"]
                # 存入的信息分别为：[实体A，实体B，关系(英文缩写)，关系(中文)，实体A的角色，实体B的角色，实体A的角色对应的id，实体B的角色对应的id]
                triple = [entity_a, entity_b, relation, mean_zh, subject_role, object_role, subject_role_id, object_role_id]
                semantic_triples.append(triple)
    print("----------")
print("每一项数据的内容为：[实体A，实体B，关系(英文缩写)，关系(中文)，实体A的角色，实体B的角色，实体A的角色对应的id，实体B的角色对应的id]")
print(semantic_triples)

# 查看每一项的结果
for x in semantic_triples:
    print(x)
```

终端效果：<br>

```log
1       急性肠胃炎      _       _       _       _       _       _       4:Pat   _
2       要      _       _       _       _       _       _       4:mMod  _
3       如何    _       _       _       _       _       _       4:Mann  _
4       治疗    _       _       _       _       _       _       0:Root  _
5       ？      _       _       _       _       _       _       4:mPunc _
----------
1       盛剑环境        _       _       _       _       _       _       3:Desc  _
2       的      _       _       _       _       _       _       1:mAux  _
3       股价    _       _       _       _       _       _       5:Exp   _
4       太      _       _       _       _       _       _       5:mDegr _
5       高      _       _       _       _       _       _       0:Root  _
6       了      _       _       _       _       _       _       5:mTone _
7       。      _       _       _       _       _       _       5:mPunc _
----------
每一项数据的内容为：[实体A，实体B，关系(英文缩写)，关系(中文)，实体A的角色，实体B的角色，实体A的角色对应的id，实体B的角色对应的id]
[['治疗', '急性肠胃炎', 'Pat', '受事', '受事主体', '受事客体', 1001, 1002], ['治疗', '如何', 'Mann', '方式角色', '方式主体', '方式客体', 1017, 1018], ['股价', '盛剑环境', 'Desc', '描写角色', '描写主体', '描写客体', 1013, 1014], ['高', '股价', 'Exp', '当事', '当事主体', '当事客体', 1003, 1004]]
['治疗', '急性肠胃炎', 'Pat', '受事', '受事主体', '受事客体', 1001, 1002]
['治疗', '如何', 'Mann', '方式角色', '方式主体', '方式客体', 1017, 1018]
['股价', '盛剑环境', 'Desc', '描写角色', '描写主体', '描写客体', 1013, 1014]
['高', '股价', 'Exp', '当事', '当事主体', '当事客体', 1003, 1004]
```

如果你想要更加便于观察结果，可以采用下列代码：<br>

```python
import hanlp
segment_dict = {'急性肠胃炎','盛剑环境'}

def segment(input_list,seg_dict):
    Segment = hanlp.load('CTB9_TOK_ELECTRA_SMALL')
    Segment.dict_force = None
    Segment.dict_combine = seg_dict
    res = Segment(input_list)
    return res

# pipeline组成为：分词、语义依存分析
HanLP = hanlp.pipeline() \
    .append(segment, output_key='tok', seg_dict=segment_dict) \
    .append(hanlp.load('SEMEVAL16_ALL_ELECTRA_SMALL_ZH'), output_key='sdp')

my_data = ['急性肠胃炎要如何治疗？','盛剑环境的股价太高了。']
doc = HanLP(my_data)
# 提取出我们需要的语义依存分析结果
# print(doc)
need_data = doc['sdp']

# 需要提取的关系
needed_semantic_relation = {
    "Pat": {"mean_zh": "受事", "subject_role": "受事主体", "object_role": "受事客体", "subject_role_id": 1001, "object_role_id": 1002},
    "Exp": {"mean_zh": "当事", "subject_role": "当事主体", "object_role": "当事客体", "subject_role_id": 1003, "object_role_id": 1004},
    "Belg": {"mean_zh": "属事", "subject_role": "属事主体", "object_role": "属事客体", "subject_role_id": 1005, "object_role_id": 1006},
    "Clas": {"mean_zh": "类事", "subject_role": "类事主体", "object_role": "类事客体", "subject_role_id": 1007, "object_role_id": 1008},
    "Cont": {"mean_zh": "客事", "subject_role": "客事主体", "object_role": "客事客体", "subject_role_id": 1009, "object_role_id": 1010},
    "Poss": {"mean_zh": "领事", "subject_role": "领事主体", "object_role": "领事客体", "subject_role_id": 1011, "object_role_id": 1012},
    "Desc": {"mean_zh": "描写角色", "subject_role": "描写主体", "object_role": "描写客体", "subject_role_id": 1013, "object_role_id": 1014},
    "Comp": {"mean_zh": "比较角色", "subject_role": "比较主体", "object_role": "比较客体", "subject_role_id": 1015, "object_role_id": 1016},
    "Mann": {"mean_zh": "方式角色", "subject_role": "方式主体", "object_role": "方式客体", "subject_role_id": 1017, "object_role_id": 1018},
    "eCoo": {"mean_zh": "并列角色", "subject_role": "并列主体", "object_role": "并列客体", "subject_role_id": 1019, "object_role_id": 1020},
    "Quan": {"mean_zh": "数量角色", "subject_role": "数量主体", "object_role": "数量客体", "subject_role_id": 1021, "object_role_id": 1022},
    "Qp": {"mean_zh": "数量组合", "subject_role": "数量组合主体", "object_role": "数量组合客体", "subject_role_id": 1023, "object_role_id": 1024},
    "Host": {"mean_zh": "宿主角色", "subject_role": "宿主主体", "object_role": "宿主客体", "subject_role_id": 1025, "object_role_id": 1026},
    "Time": {"mean_zh": "时间角色", "subject_role": "时间主体", "object_role": "时间客体", "subject_role_id": 1027, "object_role_id": 1028},
    "Loc": {"mean_zh": "空间角色", "subject_role": "空间主体", "object_role": "空间客体", "subject_role_id": 1029, "object_role_id": 1030},
    "Accd": {"mean_zh": "依据角色", "subject_role": "依据主体", "object_role": "依据客体", "subject_role_id": 1031, "object_role_id": 1032},
    "Reas": {"mean_zh": "缘故角色", "subject_role": "缘故主体", "object_role": "缘故客体", "subject_role_id": 1033, "object_role_id": 1034},
    "rReas": {"mean_zh": "反缘故角色", "subject_role": "反缘故主体", "object_role": "反缘故客体", "subject_role_id": 1035, "object_role_id": 1036},
    "mNeg": {"mean_zh": "否定标记", "subject_role": "否定标记主体", "object_role": "否定标记客体", "subject_role_id": 1037, "object_role_id": 1038},
    "Tmod": {"mean_zh": "时间修饰角色", "subject_role": "时间修饰主体", "object_role": "时间修饰客体", "subject_role_id": 1039, "object_role_id": 1040},
    "mTime": {"mean_zh": "时间标记", "subject_role": "时间标记主体", "object_role": "时间标记客体", "subject_role_id": 1041, "object_role_id": 1042},
    "Freq": {"mean_zh": "频率角色", "subject_role": "频率主体", "object_role": "频率客体", "subject_role_id": 1043, "object_role_id": 1044},
    "dExp": {"mean_zh": "嵌套当事", "subject_role": "嵌套当事主体", "object_role": "嵌套当事客体", "subject_role_id": 1045, "object_role_id": 1046}
}

semantic_triples = []
# 按句子获取不同输入的分析结果
for idx, element in enumerate(need_data):
    # 按分词获取每个分词与其他分词的关系与关系词索引
    for  i in element:
        entity_b = i.form                 # 当前词的名称
        # 一个分词可能和多个分词组成关系，i.deps的结果为：[(4, 'Pat'), [6, "Agt"]]
        for each_dep in i.deps:
            entity_a_idx = each_dep[0]-1     # 因HanLP序列后的结果从1开始编号，所以需要-1。
            entity_a = element[entity_a_idx].form
            relation = each_dep[1]
            if relation in needed_semantic_relation:
                mean_zh = needed_semantic_relation[relation]["mean_zh"]
                subject_role = needed_semantic_relation[relation]["subject_role"]
                object_role = needed_semantic_relation[relation]["object_role"]
                subject_role_id = needed_semantic_relation[relation]["subject_role_id"]
                object_role_id = needed_semantic_relation[relation]["object_role_id"]
                # 存入的信息分别为：[原句, 实体A，实体B，关系(英文缩写)，关系(中文)，实体A的角色，实体B的角色，实体A的角色对应的id，实体B的角色对应的id]
                triple = [my_data[idx], entity_a, entity_b, relation, mean_zh, subject_role, object_role, subject_role_id, object_role_id]
                semantic_triples.append(triple)

print("每一项数据的内容为：[原句， 实体A，实体B，关系(英文缩写)，关系(中文)，实体A的角色，实体B的角色，实体A的角色对应的id，实体B的角色对应的id]")
# 查看每一项的结果
for item in semantic_triples:
    print(item)
```

终端输出：<br>

```log
每一项数据的内容为：[原句， 实体A，实体B，关系(英文缩写)，关系(中文)，实体A的角色，实体B的角色，实体A的角色对应的id，实体B的角色对应的id]
['急性肠胃炎要如何治疗？', '治疗', '急性肠胃炎', 'Pat', '受事', '受事主体', '受事客体', 1001, 1002]
['急性肠胃炎要如何治疗？', '治疗', '如何', 'Mann', '方式角色', '方式主体', '方式客体', 1017, 1018]
['盛剑环境的股价太高了。', '股价', '盛剑环境', 'Desc', '描写角色', '描写主体', '描写客体', 1013, 1014]
['盛剑环境的股价太高了。', '高', '股价', 'Exp', '当事', '当事主体', '当事客体', 1003, 1004]
```
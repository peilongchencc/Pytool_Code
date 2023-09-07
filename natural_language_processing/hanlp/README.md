# HanLP
由于工作原因，笔者有时会利用 `HanLP` 做一些测试，但也仅仅是做一些测试，所以这里不会详细介绍 `HanLP` 中的模型原理。<br>
- [HanLP](#hanlp)
  - [HanLP的安装：](#hanlp的安装)
  - [分词：](#分词)
    - [根据自定义词库分词：](#根据自定义词库分词)
  - [语义依存分析(sdp):](#语义依存分析sdp)
    - [单个输入的语义依存分析：](#单个输入的语义依存分析)
    - [多个输入的语义依存分析：](#多个输入的语义依存分析)
  - [多任务模型：](#多任务模型)
  - [流水线模式--pipeline：](#流水线模式--pipeline)
    - [分句型pipeline:](#分句型pipeline)
    - [列表形式输入：](#列表形式输入)
    - [修改pipeline中插入的hanlp内置函数：](#修改pipeline中插入的hanlp内置函数)
    - [在pipeline插入自定义函数：](#在pipeline插入自定义函数)

`HanLP` 的 `RESTful API` 用法笔者不做介绍，因为 `RESTful API` 有使用次数限制，这里只介绍 `HanLP Native` 形式的使用。<br>
## HanLP的安装：
Ubuntu 系统安装 `HanLP` 很简单，终端运行下列指令即可：<br>
```shell
pip install hanlp
```
需要注意，因为 `hanlp` 模型的源部署在国外，下载 `hanlp` 的模型时，服务器上可能出现无法自动下载的情况，此时根据运行下列代码时提示的网址自行下载，让后放到代码提示的位置即可

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

## 语义依存分析(sdp):
`HanLP` 语义依存分析任务的输入必须为分词后的结果，可以为单个输入和多个输入进行语义依存分析任务，终端的输出效果是不一样的。接下来，我依次演示：<br>

### 单个输入的语义依存分析：
```python
import hanlp
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
相信你已经注意到了，我打印出了 `graphs` 的类型，类型为 `hanlp_common.conll.CoNLLSentence` 类。

### 多个输入的语义依存分析：
```python
import hanlp
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
`pipeline` 模式如果没有指定 `input_key` ，默认将上一步的输出作为输入。<br>

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
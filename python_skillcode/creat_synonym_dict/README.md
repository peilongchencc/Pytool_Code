# Creat Synonym Dict

## 全局同义词字典+语句专属同义词字典：

```python
# 标准问句结构如下
question_info = {"WJT-1":{"std_question":"卖出盛剑环境，何时钱能到账"},
                 "WJT-2":{"std_question":"亏死了，我卖出盛剑。"},
                 "WJT-3":{"std_question":"昨天卖的盛剑环境为什么今天钱还没到账"}}

# 部分标准问句专属的同义词库
question_synonym_dict = {"WJT-1_synonym_dict":{"卖出":"减仓", "钱":"资金"},
                         "WJT-2_synonym_dict":{"卖出":"割肉"}}

# 全局同义词词库
global_synonym_dict = {"盛剑":"盛剑环境", "盛环":"盛剑环境", "卖出":"卖", "没到账": "没有到账", "未到账": "没有到账"}


word_list = ['盛剑', '卖出','钱']

def get_synonym_in_current_sen(word, que_info, que_syn_dict):
    # 只需要用到question_info的key进行拼接，用于检索。
    for std_k in que_info:
        serach_synonym_key = std_k + "_synonym_dict"
        # 如果当前问句有自己独有的同义词词库，进行词的替换
        if que_syn_dict.get(serach_synonym_key):
            # 查看word在当前标准句中是否有专属的同义词
            if que_syn_dict.get(serach_synonym_key).get(word):
                # word在当前标准句中是有专属的同义词，得到word替换后的同义词
                syn_result = que_syn_dict.get(serach_synonym_key).get(word)
                print(f'当前词为:{word}，{word}在\"{que_info[std_k]["std_question"]}\"中的含义为：{syn_result}')
            else:
                print(f'当前词为:{word}，{word}在\"{que_info[std_k]["std_question"]}\"中没有专属的同义词。')
        else:
            print(f'当前问句没有专属同义词库，可以直接进行全局同义词词库的替换。')

for i in word_list:
    get_synonym_in_current_sen(i, question_info, question_synonym_dict)
    print("_"*30)
```

终端效果：<br>

```log
当前词为:盛剑，盛剑在"卖出盛剑环境，何时钱能到账"中没有专属的同义词。
当前词为:盛剑，盛剑在"亏死了，我卖出盛剑。"中没有专属的同义词。
当前问句没有专属同义词库，可以直接进行全局同义词词库的替换。
______________________________
当前词为:卖出，卖出在"卖出盛剑环境，何时钱能到账"中的含义为：减仓
当前词为:卖出，卖出在"亏死了，我卖出盛剑。"中的含义为：割肉
当前问句没有专属同义词库，可以直接进行全局同义词词库的替换。
______________________________
当前词为:钱，钱在"卖出盛剑环境，何时钱能到账"中的含义为：资金
当前词为:钱，钱在"亏死了，我卖出盛剑。"中没有专属的同义词。
当前问句没有专属同义词库，可以直接进行全局同义词词库的替换。
______________________________
```
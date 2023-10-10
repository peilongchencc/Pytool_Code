# jieba

## jieba安装：

```bash
pip install jieba
```

## 分词示例：

```python
import jieba

text = "我把盛剑环境卖出了，钱何时能到账"
text_segment = jieba.lcut(text)
print(text_segment)
```

终端效果：<br>

```log
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 1.215 seconds.
Prefix dict has been built successfully.
['我', '把', '盛剑', '环境', '卖出', '了', '，', '钱', '何时能', '到', '账']
```

## 临时添加自定义词典：

如果你自定义词汇较少，你可以使用`jieba.add_word()`函数来添加自定义词汇。以下是如何在代码中直接设置分词的示例：<br>

```python
import jieba

# 添加自定义词汇
jieba.add_word("盛剑环境")

text = "我把盛剑环境卖出了，钱何时能到账"
text_segment = jieba.lcut(text)
print(text_segment)
```

终端效果：<br>

```log
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 1.252 seconds.
Prefix dict has been built successfully.
['我', '把', '盛剑环境', '卖出', '了', '，', '钱', '何时能', '到', '账']
```

🚨🚨🚨请注意：`jieba.add_word()`每次只能添加一个词汇，如果要添加多个词汇只能写入多个`jieba.add_word()`。例如：<br>

```python
import jieba

# 添加自定义词汇
jieba.add_word("盛剑环境")
jieba.add_word("到账")

text = "我把盛剑环境卖出了，钱何时能到账"
text_segment = jieba.lcut(text)
print(text_segment)
```

终端效果：<br>

```log
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 1.276 seconds.
Prefix dict has been built successfully.
['我', '把', '盛剑环境', '卖出', '了', '，', '钱', '何时能', '到账']
```

## 以外部文件形式导入自定义词典：

如果你自定义的词汇较多，在代码中添加许多`jieba.add_word()`明显是不合适的。此时你可以使用`jieba.load_userdict()`函数，将自定义词库添加到jieba分词器。以下是`jieba.load_userdict()`使用示例：<br>

1. 首先，创建一个文本文件，比如`custom_dict.txt`，并将你想要添加的自定义词汇以及它们的词性按照以下格式添加到文件中：

```log
创新办 3 i
盛剑环境 n
到账
```

❤️❤️❤️词典格式为：一个词占一行，每一行分三部分：词语、词频（可省略）、词性（可省略），用英文空格隔开，顺序不可颠倒。**词频省略时**jieba自动计算能保证分出该词的词频。<br>

❤️❤️❤️Tips: 笔者经常每行只写一个词，不写词频和词性，毕竟很难确定。<br>

2. 然后，在Python代码中使用`jieba.load_userdict()`加载自定义词库文件：

```python
import jieba

# 加载自定义词库
jieba.load_userdict("custom_dict.txt")

# 用户输入
text = "我把盛剑环境卖出了，钱何时能到账"
text_segment = jieba.lcut(text)
print(text_segment)
```

终端效果：<br>

```log
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 1.284 seconds.
Prefix dict has been built successfully.
['我', '把', '盛剑环境', '卖出', '了', '，', '钱', '何时能', '到账']
```

记得将自定义词库文件的路径替换为你自己的文件路径。添加自定义词库可以帮助jieba分词器更好地处理特定领域或行业的词汇。<br>
import jieba
# 创建一个中文反向同义词字典
reverse_synonym_dict = {
    "快乐": "高兴",
    "喜悦": "高兴",
    "欢欣": "高兴",
    "漂亮": "美丽",
    "俊俏": "美丽",
    "秀丽": "美丽",
    "聪明": "智慧",
    "睿智": "智慧",
    "明智": "智慧",
    # 添加更多的同义词映射
}

"""
# 常规中文同义词字典如下：
synonym_dict = {
    "高兴": ["快乐", "喜悦", "欢欣"],
    "美丽": ["漂亮", "俊俏", "秀丽"],
    "智慧": ["聪明", "睿智", "明智"],
    # 添加更多的词条和其同义词
}
"""

# 替换文本中的同义词为标准词汇
text = "她感到非常快乐和欢欣。"
words = jieba.lcut(text)
print(words)
replaced_text = [reverse_synonym_dict.get(word, word) for word in words]
replaced_text = "".join(replaced_text)
print(replaced_text)

"""
终端输出：
['她', '感到', '非常', '快乐', '和', '欢欣', '。']
她感到非常高兴和高兴。
"""
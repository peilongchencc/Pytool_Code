import jieba
print('这里是tools.py文件的开头。')
current_time = '2023-07-31'

class Handler:
    def __init__(self,id,name) -> None:
        self.id = id
        self.name = name
        self.date = current_time
    
    def handle(self,text):
        print(f'今天是{self.date}')
        print(f'今天是{current_time}')
        result = jieba.lcut(text)
        return f'{self.id}用户，{self.name}先生/女士您好，您的分词结果是：{result}'

print('这里是tools.py文件的结尾。')
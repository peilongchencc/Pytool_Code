# doccano
doccano 是一个开源的文本标注工具，用于人工标注。它提供了用于文本分类、序列标注和序列到序列任务的标注功能。用户可以创建带有情感分析、命名实体识别、文本摘要等标签的数据。只需创建一个项目、上传数据，然后开始进行标注。用户可以在几小时内构建一个数据集。<br>

## 特点：
- Collaborative annotation（协作标注）
- Multi-language support（多语言支持）
- Mobile support（移动端支持）
- Emoji 😄 support（表情符号支持）
- Dark theme（暗黑主题）
- RESTful API

## 要求：
pip (Python 3.8+)<br>

## 安装方式：
> 这里仅介绍虚拟环境安装doccano的方式，docker方式安装doccano请访问github中doccano仓库。<br>

切换到自己的虚拟环境，然后以pip的方式安装doccano:<br>
```shell
pip install doccano
```

如果你使用 `pip install doccano` 指令在安装doccano时报了如下错误：<br>
```shell
Preparing metadata (setup.py) ... error
error: subprocess-exited-with-error
```
运行以下指令即可：<br>
```shell
pip install setuptools-scm
pip install doccano
```



安装后，终端运行以下命令：<br>
```shell
# Initialize database.(初始化数据库)
doccano init
# Create a super user.(创建一个超级管理员，"admin"和"pass"修改为自己的账户名和密码，也可以不修改直接使用下列指令。)
doccano createuser --username admin --password pass
# Start a web server.(启动端口号为8000的web服务)
doccano webserver --port 8000
```

另开一个终端，负责文件的上传和下载：<br>
```shell
# Start the task queue to handle file upload/download.
doccano task
```

现在就可以在下面的网址上操作了～<br>
Go to http://127.0.0.1:8000/. <br>

如果执行 `doccano task` 显示 `pydantic:ConstrainedStr has been removed in V2`，将 `pydantic` 降级到1.8版本就好了。<br>



### 导出文件：
doccano 导出的 JSON 文件中，每个实体和关系都有一个独特的 id 作为标识符。这些 id 是由 doccano 在标注数据的过程中自动生成的，**它们不一定按照顺序排列或者是连续的**。因此，如果你看到的id可能会出现乱序的情况，这并不影响数据的正确性和使用。<br>
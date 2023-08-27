# Pytool_Code
本项目记录常用的python工具型代码，方便在各种项目中调用。🚀🚀🚀当前markdown主要介绍笔者个人配置和解释各文件夹用途。<br>

## 🧑‍💻个人配置：
系统：Ubuntu 18.04<br>
python 版本：Python 3.10.11<br>
python包和环境管理器：Anaconda<br>

## command:
介绍常见的指令，暂时包括：Linux常见指令<br>

## connect_remote_server:
connect_remote_server 记录vscode连接阿里云远程服务器的一些经验，包括如何连接远程服务器，出现的错误和相应的解决方案。<br>

## crontab：
crontab是一个用于在Linux和Unix系统中定期执行任务的命令。它允许你按照特定的时间和日期计划执行脚本、命令或程序。<br>
crontab 文件夹内含 crontab 基础教程和常用的定时任务指令。<br>

## database:
介绍 python 在常见数据库(MySQL、Redis、Neo4j)方面的使用，包括数据库连接、数据存储等代码。<br>

## natural_language_processing:
自然语言处理常见任务相关代码。<br>

## doccano
doccano 是一个开源的文本标注工具，用于人工标注。它提供了用于文本分类、序列标注和序列到序列任务的标注功能。用户可以创建带有情感分析、命名实体识别、文本摘要等标签的数据。只需创建一个项目、上传数据，然后开始进行标注。用户可以在几小时内构建一个数据集。<br>

## git:
git使用教程，包括: git安装、ssh-key生成、建立git仓库、与远程仓库连接、创建git分支、拉取指定分支、合并分支等 git 常规指令介绍与使用。<br>

## python_basic_grammar:
介绍 python 基本语法、常见函数的使用与笔者常用的感觉非常方便的python库。python 类由于其复杂性，在内部单独创建一个文件夹讲解。<br>

## python_skillcode:
python_skillcode 内含 python 在各种场景下的应用型代码；<br>

## restart_server:
设置定时任务，利用 Redis 每周一凌晨2点定时读取数据，如果 Redis 数据获取成功，向 mysql 中的 task_monitor 表写入成功信息。Redis 数据获取失败时，重启3次，如果连续3次重启都失败，向 mysql 中的 task_monitor 表写入失败信息，同时向企业微信个人账号发送报警消息。<br>

## Vscode Skill
本文记录笔者在使用vscode时所遇到的一些问题和解决方案，希望对大家有帮助。<br>

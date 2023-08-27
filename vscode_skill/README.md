# Vscode Skill

## Github中MarkDown文档中所用的目录生成方式：
**起因**：Markdown可以使用`[TOC]`自动生成Markdown文件的标题目录，比如在typora等编辑器，但是Github却不支持`[TOC]`标签，所以在Github上使用`[TOC]`无法正确显示目录，所以需要借助vscode的插件实现目录生成。<br>
1. vscode拓展中搜索 `Markdown All in One`； 
2. 点击安装；
3. 在vscode打开需要生成目录的MarkDown文件，然后将光标定位到要生成目录的地方；
4. 使用快捷键 command+shift+P（windows用户ctrl+shift+P），输入以下内容并回车；
```txt
"Markdown All in One: Create Table of Contents"；
```
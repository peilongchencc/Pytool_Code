# Vscode Skill

## 断点调试：
> 快捷键为 MacOs 版，windows用于请自行百度对应快捷键。

跳转到对应函数：command + 左键点击函数<br>
返回上一级函数：control + "-"<br>
如果代码嵌套的较深，自己无法找到想看的类，可以采用"跳转到对应函数"，在那个函数任意位置打上断点的方式查看。<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/59d8ec1a-89c4-482b-b894-102686493c14)
`<继续>` 的作用是跳到下一个断点。<br>

vscode单击文件是"预览"(会覆盖原文件)，双击文件才会在旁边打开文件；<br>

## Github中MarkDown文档中所用的目录生成方式：
**起因**：Markdown可以使用`[TOC]`自动生成Markdown文件的标题目录，比如在typora等编辑器，但是Github却不支持`[TOC]`标签，所以在Github上使用`[TOC]`无法正确显示目录，所以需要借助vscode的插件实现目录生成。<br>
1. vscode拓展中搜索 `Markdown All in One`； 
2. 点击安装；
3. 在vscode打开需要生成目录的MarkDown文件，然后将光标定位到要生成目录的地方；
4. 使用快捷键 command+shift+P（windows用户ctrl+shift+P），输入以下内容并回车；
```txt
"Markdown All in One: Create Table of Contents"；
```

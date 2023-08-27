# Vscode Skill
本文记录笔者在使用vscode时所遇到的一些问题和解决方案，希望对大家有帮助。<br>

声明：本文所列快捷键为 MacOs 版，windows用于请自行百度对应快捷键。<br>
- [Vscode Skill](#vscode-skill)
  - [断点调试：](#断点调试)
  - [vscode关闭预览模式：](#vscode关闭预览模式)
  - [vscode光标移动--进出函数特别有用：](#vscode光标移动--进出函数特别有用)
  - [vscode跳转到当前文件的指定行：](#vscode跳转到当前文件的指定行)
  - [VScode相对路径无法使用问题：](#vscode相对路径无法使用问题)
  - [Github中MarkDown文档中所用的目录生成方式：](#github中markdown文档中所用的目录生成方式)

## 断点调试：
跳转到对应函数：command + 左键点击函数<br>
返回上一级函数：control + "-"<br>
如果代码嵌套的较深，自己无法找到想看的类，可以采用"跳转到对应函数"，在那个函数任意位置打上断点的方式查看。<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/59d8ec1a-89c4-482b-b894-102686493c14" alt="image" width="50%" height="50%">

`<继续>` 的作用是跳到下一个断点。<br>
<br>

## vscode关闭预览模式：
vscode默认单击文件是"预览"(会覆盖原界面显示的文件)，双击文件才会在旁边打开文件；<br>
解决方式如下：<br>
第一步：点击右下角人物头像，然后点击设置：<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/f28d9ddc-e63d-4c7a-a4c8-8bbeccc4ee11)

第二步：搜索框输入以下内容：<br>
```txt
workbench.editor.enablePrevie
```
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/5b929a41-8379-4239-a95d-1fe1ba71f7f6)


第三步：取消勾选，结束！这样就不需要双击才能不覆盖文件了。<br>
<br>

## vscode光标移动--进出函数特别有用：
移动到上一个位置：control - ，注意不是cmd。<br>
上面那部操作的撤销，cmd u ，这时候使用cmd。<br>
<br>

## vscode跳转到当前文件的指定行：
ctrl + g，然后输入想要跳转的行数并回车。
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/943de8c1-512b-4694-b09a-c0c780817703)

<br>

## VScode相对路径无法使用问题：
问题描述：data.txt 明明就在当前文件夹下，但使用相对路径读取就会报错。<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/3e0dc40a-8968-4066-a796-b94e7342d8c0" alt="image" width="50%" height="50%">

解决方式如下：<br>
第一步：进入<拓展>，找到python解释器，选择python解释器的设置；<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/ca68d830-912f-494e-a509-fa7ce5fecea3" alt="image" width="50%" height="50%">

第二步：勾选如下选项(默认是不勾选的)<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/15cad1df-0c0e-45bd-87ea-09764e05f7af)

重新执行read_file.py查看效果：<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/fa24bc98-b915-4c55-aa59-5504b92e4695)

运行成功！<br>
原因解析：因为vscode对工作区特别敏感，点击右上角的 <运行python文件> 定位其实是工作区，不是当前路径。<br>

## vscode查找文件时如何设置排除文件：
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/1360ff80-2ee5-4b9f-8417-7f8dcc11e008" alt="image" width="40%" height="40%">

## Github中MarkDown文档中所用的目录生成方式：
**起因**：Markdown可以使用`[TOC]`自动生成Markdown文件的标题目录，比如在typora等编辑器，但是Github却不支持`[TOC]`标签，所以在Github上使用`[TOC]`无法正确显示目录，所以需要借助vscode的插件实现目录生成。<br>
1. vscode拓展中搜索 `Markdown All in One`； 
2. 点击安装；
3. 在vscode打开需要生成目录的MarkDown文件，然后将光标定位到要生成目录的地方；
4. 使用快捷键 command+shift+P（windows用户ctrl+shift+P），输入以下内容并回车；
```txt
"Markdown All in One: Create Table of Contents"；
```

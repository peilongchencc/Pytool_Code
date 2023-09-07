# Markdown
- [Markdown](#markdown)
  - [插入单元格：](#插入单元格)
  - [插入表格：](#插入表格)
  - [插入图片：](#插入图片)
  - [控制图片大小：](#控制图片大小)

## 插入单元格：
Markdown通过 ` ``` ` 插入单元格，格式如下，其中 `python` 可以替换为各种语言和文件类型，例如：`txt`、`sql`、`cypher`、`java`、`shell`等等。<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/e9534a48-518a-43b1-a1f4-25ddaf191e04)


效果如下：<br>
```python
print('hello,world.')
```

## 插入表格：
格式如下，需要注意 `|` 和 `-` 都是英文符号：<br>
```txt
学生|成绩|年龄
---|---|---
路人甲 | 88 | 24
路人乙 | 94 | 28
路人丙 | 99 | 30
```
显示的效果如下：<br>
学生|成绩|年龄
---|---|---
路人甲 | 88 | 24
路人乙 | 94 | 28
路人丙 | 99 | 30

**Markdown表格定义规则**：<br>
1. `|` 和 `|` 之间形成单元格。
2. 第一行为表头，内容默认加粗居中。
3. 第二行为 `-` 、 `:`和 `|` 的组合，`---|---` 表示居中对齐，如果想改变对齐的方式，可用 `:` 标记某一列单元格对齐方式。<br>
例如 `:---|---:|---` 表示第一列左对齐，第二列右对齐，第三列居中对齐。<br>
🚨🚨🚨注意：第二行不可省略，否则语法不完整；<br>
4. 其余行是普通单元格。

## 插入图片：
Markdown文档直接图片从粘贴板复制，复制后图片的格式大致如下图：<br>
```shell
![image](https://github.com/peilongchencc/Pytool_Code/......)
```
如果你想要将文档分享给其他人，图片最好不要直接上传本地图片，需要上传到云端，让Markdown查询云端链接。云端的图库有很多，但就笔者个人而言，最方便的方式依旧是：<br>
1.截图要写入Markdown的内容；<br>
2.打开github网页端，找到Markdown文档中要插入的位置；<br>
3.`Command+v` 执行粘贴操作，github会自动将你的图片转为云端，也就是我上面所示的 `https://github.com/peilongchencc/Pytool_Code/......` 部分；<br>
4.commit后，刷新网页查看效果；
现在你就可以看到Markdown中已经插入了图片了，Markdown中图片默认是**左对齐**的。🌿🌿🌿🌿🌿<br>

## 控制图片大小：
有时粘贴入Markdown的图片会显示太大或太小，此时可以使用 `HTML` 语言的方式控制图片大小，将 `![image](https://github.com/peilongchencc/Pytool_Code/......)` 形式改为下列形式即可。<br>
> Markdown本身就是为了简化操作的一种设计，所以这里不介绍太细节的操作，例如控制图片长、宽等操作，只介绍以百分比形式放大或缩小图片。<br>

```shell
<img src="https://github.com/peilongchencc/Pytool_Code/......" alt="image" width="50%" height="50%">
```

# Excel Command

工作中会用到Excel，这里记录一下笔者自己使用Excel的经验。<br>

- [Excel Command](#excel-command)
  - [Mac跳转至文档最后一行：](#mac跳转至文档最后一行)
  - [计算某一列所有数据的平均值:](#计算某一列所有数据的平均值)
  - [统计某一列列所有内容小于等于某个值的个数有多少？](#统计某一列列所有内容小于等于某个值的个数有多少)
  - [计算单元格H11除以5000的结果，结果保留两位小数，以百分比形式呈现:](#计算单元格h11除以5000的结果结果保留两位小数以百分比形式呈现)
  - [统计某一列所有内容大于2000的个数？](#统计某一列所有内容大于2000的个数)
  - [统计某一列所有内容大于等于900，但小于1000的个数：](#统计某一列所有内容大于等于900但小于1000的个数)
  - [某些数据的求和:](#某些数据的求和)
    - [只求和某些单元格的内容：](#只求和某些单元格的内容)

## Mac跳转至文档最后一行：

在 macOS 上使用 WPS Office 查看 Excel 文件时，要跳转至文件的最后一行，你可以按照以下步骤操作：<br>

1. 打开 Excel 文件，确保它在 WPS Office 中处于活动状态。

2. 使用键盘上的快捷键 "Command" (⌘) + "↓"。这将使你光标跳转到工作表的最后一行。

3. 如果你只是想查看最后一行而不是将光标移动到那里，你可以使用快捷键 "Control" + "Command" (⌘) + "↓"，这将在不移动光标的情况下滚动表格以显示最后一行。

这些快捷键应该能够帮助你在 WPS Office 中快速跳转至 Excel 文件的最后一行。如果你使用的是不同版本的 WPS Office 或 macOS，可能会有一些差异，但大多数情况下这些快捷键是通用的。<br>

## 计算某一列所有数据的平均值:

在Excel中计算某一列数据的平均值非常简单，你可以使用内置的AVERAGE函数。假设你要计算的是B列，以下是如何计算B列数据的平均值的步骤：<br>

1. 选中一个空白单元格，这里将显示平均值。

2. 在选中的单元格中输入以下公式：

```log
=AVERAGE(B:B)
```

这个公式的含义是计算B列中所有数据的平均值。<br>

3. 按下Enter键，Excel会立即计算并在选中的单元格中显示B列数据的平均值。

请确保在公式中使用正确的列标识（例如，"B:B"表示整个B列），以确保计算包括所有需要的数据。<br>

🥴🥴🥴如果列中包含空白单元格，Excel会自动忽略它们并计算非空单元格的平均值。<br>

## 统计某一列列所有内容小于等于某个值的个数有多少？

假设你要统计的是B列，要统计B列中小于等于平均值的数据个数，你可以使用COUNTIF函数。以下是如何完成这个任务的步骤：<br>

1. 首先，你已经计算了B列的平均值。如果你还没有，请按照前面的步骤计算平均值，并记住它。

2. 在一个空白单元格中，输入以下公式：

🌿🌿🌿如果你的平均值位于G10单元格，那么你可以使用下面的公式来统计B列中小于等于G10的数据个数：<br>

在一个空白单元格中输入以下公式：

```log
=COUNTIF(B:B, "<=" & G10)
```

要确保在平均值前面加上"&"符号，以将它与COUNTIF函数结合起来。这个公式的含义是统计B列中小于等于平均值的数据个数。<br>

3. 按下Enter键，Excel会立即计算并在选中的单元格中显示小于等于平均值的数据个数。

这样，你就可以得到B列中小于等于平均值的数据的个数。<br>


## 计算单元格H11除以5000的结果，结果保留两位小数，以百分比形式呈现:

要在Excel中计算单元格H11除以5000的结果，并将结果以百分比形式呈现并保留两位小数，可以按照以下步骤操作：<br>

1. 选中你想要显示结果的单元格，比如说A1。

2. 输入以下公式并按Enter键：

```log
=H11/5000
```

3. 然后，选中包含你刚刚输入公式的单元格（在这个例子中是A1），右键单击并选择"格式单元格"。

4. 在"格式单元格"对话框中，选择"百分比"选项，并设置小数位数为2。

5. 单击"确定"按钮。

现在，单元格A1将显示H11除以5000的结果，并以百分比形式呈现，保留两位小数。<br>

## 统计某一列所有内容大于2000的个数？

假设你要统计的是B列，要在Excel中统计B列中所有内容大于2000的个数，你可以使用COUNTIF函数。以下是如何使用COUNTIF函数执行此操作的步骤：<br>

1. 选择一个空的单元格，这里将显示结果。

2. 在选定的单元格中，键入以下公式：

```log
=COUNTIF(B:B,">2000")
```

这个公式告诉Excel数列B中大于2000的单元格的数量。<br>

3. 按Enter键执行公式。

Excel将计算列B中所有大于2000的单元格的数量，并在选定的单元格中显示结果。<br>

请注意，COUNTIF函数的第一个参数是要计算的范围，第二个参数是条件。在这种情况下，范围是列B，条件是大于2000。你可以根据需要更改条件以满足不同的要求。<br>
<br>

## 统计某一列所有内容大于等于900，但小于1000的个数：

在 Excel 中，你可以使用 COUNTIF 函数或 COUNTIFS 函数来统计一个范围内满足一个或多个指定条件的单元格的数量。假设你要统计B列，要统计 B 列中所有大于等于 900 且小于 1000 的数值的个数，你可以使用以下的公式：<br>

使用 COUNTIFS 函数（推荐，当有多个条件需要满足时）：<br>

```log
=COUNTIFS(B:B, ">=900", B:B, "<1000")
```

**在以上的公式中，B:B 代表的是 B 列的所有单元格。`">=900"` 和 `"<1000"` 是要应用的条件。**<br>

将以上公式输入到一个空白单元格中，它将返回 B 列中所有在 900 到 999 之间的值的数量。<br>

🚨🚨🚨请注意，出于性能考虑，最好是指定一个实际的范围而不是整列（例如 B1:B100），尤其是在大型工作表上。例如：<br>

```log
=COUNTIFS(B1:B100, ">=900", B1:B100, "<1000")
```


## 某些数据的求和:

求和需要使用SUM函数，SUM函数可用于对一列或多列数字进行求和。例如，如果你要对B列中第1行到第100行的数字进行求和，可以在一个单元格中输入下列内容：<br>

```log
=SUM(B1:B100)
```

按Enter获取结果。<br>

同样的思路，也可以选择某一行中的连续数据进行求和：<br>

```log
=SUM(K11:AC11)
```

### 只求和某些单元格的内容：

要对某些特定单元格的数据进行求和，你可以使用Excel中的SUM函数，并在该函数中指定要求和的单元格。以下是一些步骤：<br>

1. 打开Excel并导航到包含你要求和的单元格的工作表。

2. 选择一个单元格，这将是你放置求和结果的位置。

3. 在选定的单元格中输入以下公式：

```log
=SUM(A1, B1, C1)
```

这里，A1、B1和C1是你要求和的单元格的引用。你可以根据需要更改这些引用，以包括你要求和的任何其他单元格。<br>

或者在单元格输入 `=SUM(` 然后手动点击要计算的单元格，mac按住`command`键同时选择多个数据。<br>

4. 按Enter键执行公式。Excel将计算所选单元格中指定单元格的总和，并在所选单元格中显示结果。

如果要求和的单元格在不同的行或列中，只需将它们用逗号分隔在SUM函数中即可。你还可以使用冒号来表示范围，例如`SUM(A1:C1)`将对A1、B1和C1中的数据进行求和。这样，你可以根据需要轻松自定义求和的范围。<br>
# 常用 SQL 语句


MySQL支持多种数据类型，可以根据具体需要选择适合的数据类型。以下是常见的MySQL数据类型：<br>

数值类型： - INT（整型） - BIGINT（长整型） - FLOAT（单精度浮点型） - DOUBLE（双精度浮点型） - DECIMAL（高精度浮点型） - TINYINT（小整型）<br>

字符串类型： - VARCHAR（可变长度字符串） - CHAR（固定长度字符串） - TEXT（长文本）<br>

日期和时间类型： - DATE（日期） - TIME（时间） - DATETIME（日期和时间） - TIMESTAMP（时间戳）<br>

布尔类型： - BOOLEAN（布尔值，通常以0或1表示）<br>

二进制类型： - BINARY（二进制数据） - VARBINARY（可变长度二进制数据） - BLOB（二进制大对象）<br>

其他特殊类型： - ENUM（枚举类型，可以从预定义的值列表中选择） - SET（集合类型，可以从预定义的值集合中选择）<br>

以上仅列举了常见的MySQL数据类型，还有其他一些特定的数据类型可以根据需要使用。请注意，在创建表格时，应根据实际需求选择合适的数据类型来存储和处理数据。<br>

注意⚠️⚠️⚠️：ENUM和SET类型是用于在数据库中定义一组预定义的值。这意味着你只能选择列表中定义的值，并不能插入其他值。<br>

ENUM类型：ENUM列定义了一个可以选择的预定义值列表。你可以在创建表格时为ENUM列指定可用值，并且只允许在该列表中选择的值。例如，你可以定义一个ENUM类型的列来表示用户的性别，只允许选择"男"或"女"这两个值。<br>

SET类型：SET列定义了一个可供选择的预定义值集合。与ENUM不同，SET允许你选择多个值。你可以在创建表格时为SET列指定可用的值，并从中选择一个或多个值。例如，你可以定义一个SET类型的列来表示用户的兴趣爱好，可选择的值可以是"足球"、"篮球"、"音乐"、"旅行"等。<br>

当使用ENUM和SET时，确保你确实只需要从预定义的值列表中选择值。如果你需要存储不受限制的值，应该使用其他适合的数据类型，如VARCHAR或TEXT。<br>










假设现在有一个 "qa_information" 的表，"qa_information" 中有很多字段，例如 "id"、"question"、"answer"、"undate_time"。如果想要将其中 "question" 字段的所有内容提取出来需要使用以下指令：<br>
```sql
SELECT question FROM qa_information;
```
如果想要只抽取10条数据，可以使用指令：<br>
```sql
SELECT question FROM qa_information LIMIT 10;
```
这个查询语句将🔥🔥🔥**按照默认的排序规则**抽取出 "qa_information" 表的前10条记录。<br>
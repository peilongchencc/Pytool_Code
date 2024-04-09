# sql_basic

本章介绍SQL语法基础。<br>
- [sql\_basic](#sql_basic)
  - [创建表(CREATE TABLE)：](#创建表create-table)
  - [查看表中所有内容(SELECT-FROM)：](#查看表中所有内容select-from)
  - [查看表中部分内容(LIMIT),所有字段或部分字段内容：](#查看表中部分内容limit所有字段或部分字段内容)
  - [根据表中某个字段排序，查看表中部分内容(ORDER BY-DESC)：](#根据表中某个字段排序查看表中部分内容order-by-desc)
  - [WHERE关键词执行条件检索：](#where关键词执行条件检索)
  - [LIKE运算符结合通配符执行模糊搜索：](#like运算符结合通配符执行模糊搜索)
  - [COUNT函数统计满足特定条件的行数:](#count函数统计满足特定条件的行数)
    - [示例 1：统计表中的所有行数](#示例-1统计表中的所有行数)
    - [示例 2：统计满足条件的行数](#示例-2统计满足条件的行数)
    - [示例 3：统计特定列的非NULL值数量](#示例-3统计特定列的非null值数量)
  - [向表中写入内容(INSERT INTO)：](#向表中写入内容insert-into)
  - [更新表中的内容(UPDATE)：](#更新表中的内容update)
  - [删除表中的内容(DELETE)：](#删除表中的内容delete)
  - [删除表(DROP TABLE)：](#删除表drop-table)
  - [表格创建、数据插入、数据更新SQL语句完整示例及解释:](#表格创建数据插入数据更新sql语句完整示例及解释)

## 创建表(CREATE TABLE)：

要创建一个MySQL数据库中的表格，需要使用 `CREATE TABLE` 语句。以下是一个示例代码来创建一个名为 `"task_monitor"` 的表格，其中包括 `"task_id"`、`"task_description"`、 `"task_command"` 、`task_status`、 `task_status`、 `task_execution_time`、 `log_path` 这六个列：<br>

```sql
CREATE TABLE task_monitor (
    task_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '任务的唯一ID',
    task_description VARCHAR(255) COMMENT '任务描述',
    task_command VARCHAR(255) COMMENT '执行的命令',
    task_status ENUM('成功', '失败') COMMENT '任务状态',
    task_execution_time DATETIME COMMENT '任务执行的时间',
    log_path VARCHAR(255) COMMENT '日志文件的路径'
);
```

如果要在 Navicat 中使用，先点击查询，然后点击 `"+"` 号，新建查询，选择对应的数据库即可。<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/6943e85a-8fbd-42b9-9196-bfef558c780a" alt="image" width="70%" height="70%">

相信大家已经注意到了，对于不同的列，我使用了不同的数据类型，这是因为MySQL支持多种数据类型，可以根据具体需要选择适合的数据类型。以下是常见的MySQL数据类型：<br>

🥷🥷🥷🥷🥷🥷简单了解以下内容即可，需要的时候再返回这里看，刚开始一下子记住不现实。🌿🌿🌿🌿🌿<br>

**数值类型**： - `INT`（整型） - `BIGINT`（长整型） - `FLOAT`（单精度浮点型） - `DOUBLE`（双精度浮点型） - `DECIMAL`（高精度浮点型） - `TINYINT`（小整型）<br>

**字符串类型**： - `VARCHAR`（可变长度字符串） - `CHAR`（固定长度字符串） - `TEXT`（长文本）<br>

**日期和时间类型**： - `DATE`（日期） - `TIME`（时间） - `DATETIME`（日期和时间） - `TIMESTAMP`（时间戳）<br>

**布尔类型**： - `BOOLEAN`（布尔值，通常以0或1表示）<br>

**二进制类型**： - `BINARY`（二进制数据） - `VARBINARY`（可变长度二进制数据） - `BLOB`（二进制大对象）<br>

**其他特殊类型**： - `ENUM`（枚举类型，可以从预定义的值列表中选择） - `SET`（集合类型，可以从预定义的值集合中选择）<br>

以上仅列举了常见的MySQL数据类型，还有其他一些特定的数据类型可以根据需要使用。请注意，在创建表格时，应根据实际需求选择合适的数据类型来存储和处理数据。<br>

注意⚠️⚠️⚠️：`ENUM` 和 `SET` 类型是用于在数据库中定义一组预定义的值。这意味着你只能选择列表中定义的值，并不能插入其他值。<br>

**`ENUM` 类型**：`ENUM` 列定义了一个可以选择的预定义值列表。你可以在创建表格时为 `ENUM` 列指定可用值，并且只允许在该列表中选择的值。例如，你可以定义一个ENUM类型的列来表示用户的性别，只允许选择"男"或"女"这两个值。<br>

**`SET` 类型**：`SET` 列定义了一个可供选择的预定义值集合。与 `ENUM` 不同，`SET` 允许你选择多个值。你可以在创建表格时为 `SET` 列指定可用的值，并从中选择一个或多个值。例如，你可以定义一个 `SET` 类型的列来表示用户的兴趣爱好，可选择的值可以是"足球"、"篮球"、"音乐"、"旅行"等。<br>

当使用 `ENUM` 和 `SET` 时，确保你确实只需要从预定义的值列表中选择值。如果你需要存储不受限制的值，应该使用其他适合的数据类型，如 `VARCHAR` 或`TEXT`。<br>

🥷🥷🥷🥷🥷🥷<br>


## 查看表中所有内容(SELECT-FROM)：

要查看某个表中的内容主要使用 `SELECT` 和 `FROM` 关键字。<br>

假设我们要从名为 `task_monitor` 的数据库表中检索所有的列和行:<br>

```sql
SELECT * FROM task_monitor;
```

SQL语句解释：关键字 `"SELECT"` 用于指定要检索的数据，而 `"*"` 表示所有的列。关键字 `"FROM"` 用于指定要从哪个表中检索数据，这里是 `task_monitor` 表。因此，该语句将返回 `task_monitor` 表中的所有数据。<br>

## 查看表中部分内容(LIMIT),所有字段或部分字段内容：

假设我们要从名为 `task_monitor` 的数据库表中检索所有的列和行，然后将前3行内容返回:<br>

```sql
SELECT * FROM task_monitor LIMIT 3;
```

假设我们要从名为 `task_monitor` 的数据库表中检索 `task_command` 列，然后将前3行内容返回:<br>

```sql
SELECT task_command FROM task_monitor LIMIT 3;
```

## 根据表中某个字段排序，查看表中部分内容(ORDER BY-DESC)：

如果我们要从名为 `"task_monitor"` 的表中检索数据，并按照 `"task_execution_time"` 字段的降序排列，并只显示前3行：<br>

```sql
SELECT * FROM task_monitor ORDER BY task_execution_time DESC LIMIT 3;
```

SQL语句解释：<br>

`"SELECT "`: 这表示从表中选择所有的列。如果你想选择特定的列，可以将星号 `*` 替换为列名。<br>

`"FROM task_monitor"`: 这表示你从名为 `"task_monitor"` 的表中进行数据检索。`"task_monitor"` 是表的名称，你可以根据自己的表名进行相应替换。<br>

`ORDER BY` 是一个SQL关键字，用于按照特定的列对查询结果进行排序。通过指定一个或多个列作为排序规则，可以控制结果行的顺序。<br>

`"ORDER BY task_execution_time DESC"`: 这表示使用 `"task_execution_time"` 字段对结果进行降序排序。DESC关键字指定降序排序，如果不写，默认为升序（ASC）排序。`ORDER` 表示顺序、排序，`DESCENDING` 表示降序，`ASCENDING` 表示升序，这个命令应该很好理解。<br>

`"LIMIT 3"`: 这表示只返回前3行结果。你可以更改数字来返回所需数量的行数。<br>

综上所述，这个SQL语句的结果将返回 `"task_monitor"` 表中前3个根据 `"task_execution_time"`字段降序排列的记录。<br>


## WHERE关键词执行条件检索：

SQL语句中的**WHERE子句用于筛选从数据库表中检索出的数据，以便只返回符合特定条件的行。它允许你指定一个或多个条件，只有满足这些条件的行才会包含在查询结果中。**<br>

WHERE子句通常与SELECT、UPDATE、DELETE等SQL语句一起使用，以过滤数据。<br>

以下是一些WHERE子句的示例：<br>

1. 使用等于操作符（=）筛选特定值的行：

```sql
SELECT * FROM employees WHERE department = 'HR';
```

这个示例将返回所有在'HR'部门工作的员工的信息。<br>

2. 使用比较操作符筛选行（例如，大于、小于、大于等于、小于等于）：

```sql
SELECT * FROM products WHERE price > 50;
```

这个示例将返回所有价格大于50的产品。<br>

3. 使用逻辑运算符（AND、OR、NOT）组合多个条件：

```sql
SELECT * FROM orders WHERE order_date >= '2023-01-01' AND order_date <= '2023-12-31';
```

这个示例将返回在2023年内下的所有订单。<br>

4. 使用通配符（LIKE）进行模糊搜索：

```sql
SELECT * FROM customers WHERE last_name LIKE 'Smith%';
```

这个示例将返回姓氏以"Smith"开头的所有客户。<br>

5. 使用IN子句筛选多个值：

```sql
SELECT * FROM products WHERE category IN ('Electronics', 'Appliances');
```

这个示例将返回类别为'Electronics'或'Appliances'的产品。<br>

6. 使用IS NULL或IS NOT NULL来筛选空值或非空值：

```sql
SELECT * FROM employees WHERE manager_id IS NULL;
```

这个示例将返回没有经理的员工。<br>

这些示例演示了WHERE子句在SQL中的一些常见用法，但并不局限于此。根据你的需求，可以使用更复杂的条件组合来筛选数据。<br>


## LIKE运算符结合通配符执行模糊搜索：

`LIKE` 是 SQL 中用于执行模糊搜索的关键字。它通常与通配符结合使用，以在文本数据中查找包含特定模式或字符串的行。以下是 `LIKE` 的基本用法：<br>

1. **百分号通配符 `%`：** `%` 是 `LIKE` 中最常用的通配符，表示匹配零个或多个字符。例如，`'%apple%'` 将匹配包含 "apple" 子字符串的任何字符串。

2. **下划线通配符 `_`：** 下划线通配符 `_` 用于匹配单个字符。例如，`'c_t'` 可以匹配 "cat"、"cut"、"cot" 等字符串。

3. **不区分大小写匹配：** 默认情况下，`LIKE` 是不区分大小写的。要进行大小写敏感的匹配，可以使用适当的函数，如 `COLLATE`。

下面是一些示例用法：<br>

查找qa_template表中question字段含有"直播"的数据:<br>

```sql
SELECT * FROM qa_template WHERE question LIKE '%直播%';
```

查找以 "apple" 开头的字符串：<br>

```sql
SELECT * FROM fruits WHERE name LIKE 'apple%';
```

查找包含 "fruit" 的任何字符串：<br>

```sql
SELECT * FROM text_data WHERE content LIKE '%fruit%';
```

查找以 "a" 结尾的三个字符的字符串：<br>

```sql
SELECT * FROM words WHERE word LIKE '__a';
```

查找包含 "cat"、"cut" 或 "cot" 的字符串：<br>

```sql
SELECT * FROM animals WHERE name LIKE 'c_t';
```

大小写敏感匹配示例：<br>

```sql
SELECT * FROM sensitive_data WHERE phrase COLLATE utf8_bin LIKE 'Search';
```

请注意，虽然 `LIKE` 是执行模糊搜索的一种方式，但对于大型数据集，它可能会导致性能问题‼️‼️‼️，因为它需要在文本列上执行全表扫描。在需要高效搜索大量数据时，可能需要考虑使用全文搜索引擎或索引技术。<br>


## COUNT函数统计满足特定条件的行数:

SQL中的COUNT函数用于统计满足特定条件的行数，通常用于聚合查询中。下面是COUNT函数的基本语法和示例：<br>

基本语法：<br>

```sql
SELECT COUNT(column_name) FROM table_name WHERE condition;
```

- `COUNT(column_name)`: 要统计的列名或表达式。通常使用`*`来统计所有行，或者指定列名来统计特定列的非NULL值。

- `table_name`: 要查询的表名。

- `condition`（可选）：用于过滤要计数的行的条件。

### 示例 1：统计表中的所有行数

假设有一个名为"orders"的表，我们要统计其中的所有行数：<br>

```sql
SELECT COUNT(*) FROM orders;
```

这将返回表中的总行数。<br>

### 示例 2：统计满足条件的行数

假设我们要统计"orders"表中"status"字段为"已完成"的订单数量：<br>

```sql
SELECT COUNT(*) FROM orders WHERE status = '已完成';
```

这将返回满足条件的订单数量。<br>

### 示例 3：统计特定列的非NULL值数量

如果要统计某一列的非NULL值数量，可以指定列名作为COUNT的参数。例如，统计"customers"表中"email"列的非NULL值数量：<br>

```sql
SELECT COUNT(email) FROM customers;
```

这将返回"customers"表中"email"列的非NULL值数量。<br>

总之，COUNT函数是SQL中用于统计行数的强大工具，可以根据需要统计所有行或满足特定条件的行。<br>


## 向表中写入内容(INSERT INTO)：

要向MySQL某个表写入内容主要使用 `INSERT INTO` 和 `VALUES` 关键字。<br>

假设我们要向名为 `task_monitor` 的表中写入数据：<br>

```sql
INSERT INTO task_monitor (task_id, task_description, task_command, task_status, task_execution_time, log_path) 
VALUES (1, '任务1', '命令1', '成功', '2022-01-01 12:00:00', '/logs/task1.log');
```


## 更新表中的内容(UPDATE)：

更新MySQL某个表的内容，主要使用 `UPDATE` 、`SET` 和 `WHERE` 关键字。<br>

```sql
UPDATE task_monitor SET task_status = '失败', 
task_execution_time = '2022-01-02 10:00:00' WHERE task_id = 1;
```

SQL语句解释：这个示例将更新 `task_monitor` 表中 `task_id` 为 `1` 的记录的任务状态为 `'失败'`，以及任务执行时间为 `'2022-01-02 10:00:00'`。你可以根据需要更新其他字段的值，并使用 `WHERE` 子句来指定要更新的记录的条件。<br>

🚨🚨🚨注意字段字段之间要用逗号隔开，如：`SET task_status = '失败', task_execution_time = '2022-01-02 10:00:00'` ‼️‼️‼️<br>


再来个例子，假设只想更新这个表中 `'task_command'` 列所有为 `python app.py` 的数据呢？<br>

```sql
UPDATE task_monitor SET task_status = '失败', task_execution_time = '2022-01-02 10:00:00' 
WHERE task_command = 'python app.py';
```

> SQL语句支持断句的，看着怎么方便怎么来即可～

SQL语句解释：这个示例将更新 `task_monitor` 表中 `'task_command'` 列为 `'python app.py'` 的记录的任务状态为 `'失败'`，以及任务执行时间为 `'2022-01-02 10:00:00'`。只有满足 `WHERE` 子句条件的记录会被更新。你可以根据需要更新其他字段的值。<br>


## 删除表中的内容(DELETE)：

删除MySQL某个表的内容，主要使用 `DELETE` 和 `WHERE` 关键字。请谨慎使用，因为删除操作是不可逆的🚨🚨🚨<br>

```sql
DELETE FROM task_monitor WHERE task_id = 1;
```

SQL语句解释：这个示例将删除 `task_monitor` 表中 `task_id` 为 `1` 的记录。你可以根据需要使用不同的条件来删除符合条件的记录。<br>

如果你想删除整个表中的内容，而不是其中的特定记录，可以使用以下语句：<br>

```sql
DELETE FROM task_monitor;
```

这会从数据库中永久删除 `task_monitor` 表中的所有记录。<br>


## 删除表(DROP TABLE)：

要删除某个表，需要使用 `DROP TABLE` 关键字。假设删除 `task_monitor` 表：<br>

```sql
DROP TABLE task_monitor;
```

SQL语句解释：这个示例将从数据库中永久删除 task_monitor 表及其所有数据。请谨慎使用，因为删除操作是不可逆的。在执行此操作之前，确保你没有需要保留的数据。<br>


## 表格创建、数据插入、数据更新SQL语句完整示例及解释:

```sql
CREATE TABLE `image_hold_share`  (
  `id` int(11) AUTO_INCREMENT PRIMARY KEY,
  `image_url` varchar(255) NOT NULL COMMENT '图片链接',
  `url_type` varchar(255) NOT NULL COMMENT '图片地址类型,取值为 "oss" 或 "7min_local"',
  `ocr_fund_code` varchar(255) NULL DEFAULT NULL COMMENT 'ocr识别的基金代码',
  `ocr_hold_share` varchar(255) NULL DEFAULT NULL COMMENT 'ocr识别的持有份额',
  `update_fund_code` varchar(255) NULL DEFAULT NULL COMMENT '持仓部更新的基金代码',
  `update_hold_share` varchar(255) NULL DEFAULT NULL COMMENT '持仓不更新的持有份额',
  `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

# `CHARACTER SET = utf8mb4`：指定了表的字符集是utf8mb4。字符集决定了数据库可以存储哪些字符。utf8mb4是UTF-8的超集，可以存储任何Unicode字符，包括表情符号。
# `COLLATE = utf8mb4_unicode_ci`：指定了表的校对规则是utf8mb4_unicode_ci。校对规则决定了数据库中的字符如何比较。在这个例子中，`_ci`表示大小写不敏感，这意味着在比较字符时，大写和小写字母被认为是相同的。
# `ROW_FORMAT = Dynamic`：指定了表的行格式是动态的。行格式决定了表中行的物理存储。动态行格式允许变长列（如VARCHAR、BLOB和TEXT类型）仅存储必要的空间，从而节省空间并提高性能。
```

上述 SQL 语句创建的表结构，不需要手动传入 `update_time` 的参数值。在这个表结构中，`update_time` 字段已经被设置为在记录被创建时自动填入当前时间戳（`DEFAULT CURRENT_TIMESTAMP`），并且在每次记录被更新时自动更新时间戳（`ON UPDATE CURRENT_TIMESTAMP`）。因此，当你插入或更新表中的记录时，MySQL 会自动管理 `update_time` 字段的值，无需你手动指定。<br>

执行以下语句可将数据插入 `image_hold_share` 表:<br>

```sql
INSERT INTO `image_hold_share` (`image_url`, `url_type`) VALUES ('https://example.com/image1.jpg', 'oss');
INSERT INTO `image_hold_share` (`image_url`, `url_type`) VALUES ('https://example.com/image2.jpg', '7min_local');
INSERT INTO `image_hold_share` (`image_url`, `url_type`, `ocr_fund_code`, `ocr_hold_share`) VALUES ('https://example.com/image3.jpg', 'oss', '123456', '10000');
```

在这些示例中：<br>

- 第一条和第二条插入语句仅填充了必须填写的字段 `image_url` 和 `url_type`。
- 第三条插入语句除了必填字段外，还填充了可选字段 `ocr_fund_code` 和 `ocr_hold_share`。

因为 `create_time` 和 `update_time` 字段有默认值且 `update_time` 在每次更新时自动改变，所以你不需要在插入语句中包含这些字段。<br>

UPDATE语句测试:<br>

```sql
UPDATE `image_hold_share`
SET `update_fund_code` = '654321', `update_hold_share` = '20000'
WHERE `image_url` = 'https://example.com/image2.jpg';
```

这条 SQL 语句的目的是查找 `image_hold_share` 表中 `image_url` 字段值为 `'https://example.com/image2.jpg'` 的记录，并将这些记录的 `update_fund_code` 更新为 `'654321'`，`update_hold_share` 更新为 `'20000'`。<br>

🥴🥴🥴即使原表中对应的 `update_fund_code` 和 `update_hold_share` 字段的值为 `NULL`，它们也可以被更新为新的值。在 SQL 中，`NULL` 表示一个字段没有值。使用 `UPDATE` 语句时，可以将任何字段的值从 `NULL` 更新为一个具体的值，包括数字、字符串或其他数据类型。<br>

删除MySQL某个表的内容，主要使用 `DELETE` 和 `WHERE` 关键字。请谨慎使用，因为删除操作是不可逆的🚨🚨🚨<br>

```sql
DELETE FROM `image_hold_share` WHERE `id` = 2;
```

这条SQL语句的作用是从`image_hold_share`表中删除`id`字段值为2的行。<br>

如果想删除这个表中的所有内容，但不删除表本身。可执行下列语句:<br>

```sql
DELETE FROM `image_hold_share`;
```

如果想要直接删除表和表中的数据，可以执行下列语句:<br>

```sql
DROP TABLE `image_hold_share`;
```

‼️‼️‼️注意：这个示例将从数据库中永久删除 task_monitor 表及其所有数据。请谨慎使用，因为删除操作是不可逆的。在执行此操作之前，确保你没有需要保留的数据。<br>

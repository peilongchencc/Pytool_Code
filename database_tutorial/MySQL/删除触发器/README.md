# 构建删除触发器
- [构建删除触发器](#构建删除触发器)
  - [创建`qa_template_delete`表存储被删除的数据:](#创建qa_template_delete表存储被删除的数据)
  - [创建触发器:](#创建触发器)
  - [确定数据新增还是修改：](#确定数据新增还是修改)
  - [删除触发器的性能：](#删除触发器的性能)

需求: 我创建了`qa_template_delete`表用于存储`qa_template`表被删除的数据，我应该如何构造删除触发器呢？当`qa_template`表有数据被删除时，将数据自动存入`qa_template_delete`表。

## 创建`qa_template_delete`表存储被删除的数据:

```sql
CREATE TABLE `qa_template_delete` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `intentId` int(11) NOT NULL,
  `code` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `question` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `delete_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);
```

## 创建触发器:

要创建一个删除触发器，以便当`qa_template`表中的数据被删除时，这些数据会被自动地存入`qa_template_delete`表，你可以按照以下步骤来操作：

1. **定义触发器的类型和触发事件**：在这种情况下，你需要一个`BEFORE DELETE`或`AFTER DELETE`触发器。通常，`AFTER DELETE`更适合于这种情况，因为它在删除操作完成后触发，确保所有数据都已准确地删除。

2. **指定要执行的操作**：当触发器激活时，你需要从`qa_template`表中取出被删除的行，并将其插入`qa_template_delete`表中。

基于你的表结构，以下是一个创建触发器的示例SQL语句：<br>

```sql
DELIMITER //

CREATE TRIGGER `qa_template_AfterDelete` 
AFTER DELETE ON `qa_template` 
FOR EACH ROW 
BEGIN
    INSERT INTO `qa_template_delete` (`intentId`, `code`, `question`, `delete_time`) 
    VALUES (OLD.`intentId`, OLD.`code`, OLD.`question`, NOW());
END; //

DELIMITER ;
```

在这个触发器中：<br>

- `AFTER DELETE ON qa_template` 表明触发器会在`qa_template`表的记录被删除后触发。
- `FOR EACH ROW` 表示对于每条被删除的记录，触发器都会执行一次。
- `BEGIN ... END;` 包含了当触发器触发时需要执行的语句。
- `INSERT INTO qa_template_delete ...` 是将删除的数据插入到`qa_template_delete`表的语句。
- `OLD.intentId`, `OLD.code`, `OLD.question` 表示被删除行的原始值。
- `NOW()` 函数记录了删除发生的时间。
- `DELIMITER` 在 SQL 中用于改变标准的语句终止符号。在创建存储过程、函数、触发器或事件时，这个命令非常有用。通常，SQL 语句是以分号（`;`）结束的。但是，存储过程或触发器等包含了多个语句，也需要用分号分隔，这可能导致语句解析的混淆。

`DELIMITER //` 将标准的 SQL 分隔符从 `;` 更改为 `//`。在创建一个触发器时，可能需要在触发器的定义内部使用分号来分隔各个 SQL 语句。<br>

在实际部署这个触发器之前，请确保你已经对数据库备份，并充分测试以确保触发器的行为符合你的需求。<br>

## 确定数据新增还是修改：

要从 MySQL 数据库的 `qa_template` 表中获取过去一天更新的数据，并区分数据是新增还是修改了哪个字段，你需要执行以下步骤：<br>

1. **修改 `qa_template` 表结构**：首先，确保你的表中除了 `create_time` 字段外，还有一个 `update_time` 字段。这是因为 `create_time` 只能告诉你记录何时被创建，而 `update_time` 则能告诉你记录上一次何时被更新。如果还没有 `update_time` 字段，需要添加这个字段(`update_time` 字段要设置根据时间戳更新，可以告诉我记录上一次何时被更新。)。

2. **创建触发器（可选）**：如果你希望 `update_time` 字段在每次更新记录时自动变更，可以创建一个数据库触发器来自动更新这个字段。

3. **查询过去一天更新的数据**：使用 SQL 查询来获取 `create_time` 或 `update_time` 在过去一天内的记录。这可以通过类似以下的查询实现：
   ```sql
   SELECT * FROM qa_template 
   WHERE create_time >= CURDATE() - INTERVAL 1 DAY 
   OR update_time >= CURDATE() - INTERVAL 1 DAY;
   ```

4. **区分新增和修改的数据**：要区分哪些数据是新添加的，哪些是被修改的，可以检查 `create_time` 和 `update_time` 字段的值。如果 `create_time` 是在过去一天内，而 `update_time` 要么是空，要么和 `create_time` 相同，那么这条记录很可能是新添加的。如果 `update_time` 是在过去一天内，但 `create_time` 较早，那么这条记录则是被修改的。

5. **确定哪些字段被修改**（如果需要）：这一步比较复杂，💦💦💦因为 MySQL 默认不提供跟踪哪些具体字段被修改的功能。一种解决方法是使用审计日志或更高级的数据库监控工具。或者，你可以在应用层进行处理，比如在更新数据时记录哪些字段发生了变化。

请根据你的具体需求和数据库的设置来调整上述步骤。如果你的应用场景对数据一致性和精确度有较高要求，可能需要更复杂的数据跟踪和管理策略。<br>

## 删除触发器的性能：

在大量数据操作的情况下，在myslq中创建删除触发器会对性能产生影响吗？<br>

在MySQL中，创建和使用删除触发器确实可能会对性能产生影响，尤其是在处理大量数据时。这种影响的程度取决于多个因素：<br>

1. **触发器的复杂性**：如果触发器执行复杂的操作或包含多个SQL语句，它可能会消耗更多的处理时间。

2. **触发频率**：如果触发器在每次删除操作时都会被触发，而删除操作频繁发生，则触发器可能会显著增加数据库的负载。

3. **附加操作**：触发器可能会执行额外的数据库查询、插入、更新或删除操作。这些额外操作会增加数据库服务器的工作量。

4. **锁定和并发**：触发器可能会导致记录被锁定更长时间，从而影响到并发操作的性能。

5. **数据的数量和类型**：处理大量数据或处理某些类型的数据（如大型文本字段或BLOB）可能会使触发器变得更加缓慢。

为了减轻这种影响，可以采取以下措施：<br>

- 确保触发器尽可能高效和简洁。
- 在不影响业务逻辑的情况下，尽量减少触发器中的复杂操作。
- 定期监控和分析数据库性能，以识别可能由触发器引起的瓶颈。
- 考虑在低峰时间执行大批量的删除操作。

如果触发器对性能的影响变得不可接受，可能需要考虑使用其他方法来实现相同的业务逻辑，例如定期批处理作业或应用程序层面的逻辑。<br>
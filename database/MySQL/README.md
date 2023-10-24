# MySQL
MySQL是一种开源的关系型数据库管理系统（RDBMS），广泛用于存储、管理和检索结构化数据。当前大多数公司都会用到MySQL数据库，所以掌握MySQL数据库的使用是必须的。<br>

笔者使用的是Ubuntu 18.04.6系统，就以此讲解 MySQL 数据库的安装、配置信息查看和常规操作。<br>
- [MySQL](#mysql)
  - [服务器安装MySQL数据库：](#服务器安装mysql数据库)
  - [终端MySQL常用指令(开启、关闭、重启、状态指令)：](#终端mysql常用指令开启关闭重启状态指令)
  - [查看MySQL配置信息：](#查看mysql配置信息)
  - [MySQL密码设置：(root账号)](#mysql密码设置root账号)
  - [本地使用 Navicat 远程连接 MySQL ：](#本地使用-navicat-远程连接-mysql-)
  - [常用SQL语句：](#常用sql语句)
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
  - [Python与MySQL：](#python与mysql)
    - [pymysql的安装：](#pymysql的安装)
    - [使用pymysql测试连接MySQL：](#使用pymysql测试连接mysql)
    - [pymysql操作数据库的关键：](#pymysql操作数据库的关键)
    - [创建表：](#创建表)
    - [获取表中的内容：](#获取表中的内容)
  - [pymysql示例：](#pymysql示例)
## 服务器安装MySQL数据库：
MySQL数据库的安装非常简单～<br>
1. 更新系统软件包信息：
```shell
apt update
```

2. 安装MySQL服务器：
```shell
apt install mysql-server
```

## 终端MySQL常用指令(开启、关闭、重启、状态指令)：
MySQL数据库安装后，首先我们要熟悉下MySQL数据库的常用指令。注意⚠️⚠️⚠️：以下指令均在终端使用，而不是在终端进入MySQL服务器后使用。<br>
- 关闭MySQL服务
```shell
service mysql stop
```
- 查看MySQLl状态
```shell
service mysql status
```
- 启动MySQL服务
```shell
service mysql start
```
- 重启MySQL服务
```shell
service mysql restart
```
- 查看端口开放情况和端口对应的pid(查看的是系统监听的所有的端口，MySQL默认开始3306端口，自己注意下是否有开放即可。)
```shell
netstat -ntlp 
```

## 查看MySQL配置信息：
安装MySQL后，可以在终端使用以下指令查看MySQL的具体信息：
```shell
cat /etc/mysql/mysql.conf.d/mysqld.cnf
```
> `/etc/mysql/mysql.conf.d/mysqld.cnf`为MySQL默认的配置文件路径。

由输出信息可以看到MySQl数据库中数据的保存位置；<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/177d581a-3a62-49f2-a05d-af584bff29eb)


## MySQL密码设置：(root账号)
1. 输入以下命令以连接到MySQL服务器：
```shell
sudo mysql -u root    
```
> 因安装时没有要求输入密码，所以此时会直接登录mysql。

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/3130258c-cc03-4030-9651-b0c13f16105d)


2. 在MySQL提示符下，执行以下命令来设置密码：
```shell
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_password';
```
请将 `'new_password'` 替换为你想要设置的新密码，假设我要将密码设置为 `Flameaway3.`，操作如下：<br>
```shell
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Flameaway3.';
```

3. 更新系统权限表：
```shell
FLUSH PRIVILEGES;
```
4. 退出MySQL提示符：
```shell
exit;
```
5. 使用 -p 指令登录：
```shell
mysql -u root -p
```
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/0ac8f06f-97af-4827-9553-535573bc6997)
<br>
<br>

## 本地使用 Navicat 远程连接 MySQL ：
**事件描述**: 我在阿里云服务器上安装了MySQL，我的服务器公网ip为 `8.140.203.xxx` ，我的账号为 `root` ，密码为 `Flameaway3.` ，我如何在本地通过navicat连接到这个MySQL呢？<br>

1. 进入安全组：
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/0d4ee2bc-3bd0-4d27-8b02-eb99797b040c)
<br>

2. 开通3306端口：
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/90199b3e-de4d-457d-ad90-67b7ef6d61e0)
<br>

3. 修改 mysql 配置信息中的bind-address:

`bind-address=127.0.0.1` 表示 MySQL服务对 `127.0.0.1` 地址进行监听，禁止外部远程连接。<br>

需要在mysql配置文件中找到 `bind-address` 行，并将其注释掉或修改为： `bind-address = 0.0.0.0`:<br>
```shell
cat /etc/mysql/mysql.conf.d/mysqld.cnf
``` 
🚀🚀🚀我采用的方式是注释 bind-address行，注释后保存、退出。<br>
<br>
4. 设置root的远程访问权限：
终端连接到MySQL服务器，然后依次运行以下指令即可：
```shell
mysql -u root -p    # 输入密码进行登录；
use mysql;          # 查看mysql数据库；
select host from user where user = 'root';    # 查看root账号的host；
update user set host = '%' where user = 'root';    # 将root账号的host修改为 '%'，允许外部访问；
exit; # 退出 mysql 客户端；
```
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/2e9bc409-f375-408d-9af5-431da62115f1)


5. 重新启动 mysql 并查看3306端口的监听地址：<br>

输入以下命令重启mysql数据库：<br>
```shell
service mysql restart
```
查看端口开放情况和端口对应的pid(也可以使用`netstat -tuln`，后来笔者感觉`netstat -ntlp `指令更方便点。)
```shell
netstat -ntlp 
```

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/4d24c9aa-f7ba-4b1a-9c9a-4c8021b4ea75)

可以看到，端口的状态已经修改~🥴🥴🥴<br>

6. 使用 Navicat 测试是否可以连接到远程的MySQL：
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/cd8936d6-eca9-42a1-806f-845ecf5694b1)

成功连接！现在就可以利用 Navicat 操作 MySQL 数据库了。<br>

## 常用SQL语句：

### 创建表(CREATE TABLE)：
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
<br>
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
<br>


### 查看表中所有内容(SELECT-FROM)：
要查看某个表中的内容主要使用 `SELECT` 和 `FROM` 关键字。<br>

假设我们要从名为 `task_monitor` 的数据库表中检索所有的列和行:<br>
```sql
SELECT * FROM task_monitor;
```
SQL语句解释：关键字 `"SELECT"` 用于指定要检索的数据，而 `"*"` 表示所有的列。关键字 `"FROM"` 用于指定要从哪个表中检索数据，这里是 `task_monitor` 表。因此，该语句将返回 `task_monitor` 表中的所有数据。<br>

### 查看表中部分内容(LIMIT),所有字段或部分字段内容：
假设我们要从名为 `task_monitor` 的数据库表中检索所有的列和行，然后将前3行内容返回:<br>

```sql
SELECT * FROM task_monitor LIMIT 3;
```

假设我们要从名为 `task_monitor` 的数据库表中检索 `task_command` 列，然后将前3行内容返回:<br>

```sql
SELECT task_command FROM task_monitor LIMIT 3;
```

### 根据表中某个字段排序，查看表中部分内容(ORDER BY-DESC)：
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
<br>

### WHERE关键词执行条件检索：

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

### LIKE运算符结合通配符执行模糊搜索：
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

### COUNT函数统计满足特定条件的行数:

SQL中的COUNT函数用于统计满足特定条件的行数，通常用于聚合查询中。下面是COUNT函数的基本语法和示例：<br>

基本语法：<br>

```sql
SELECT COUNT(column_name) FROM table_name WHERE condition;
```

- `COUNT(column_name)`: 要统计的列名或表达式。通常使用`*`来统计所有行，或者指定列名来统计特定列的非NULL值。
- `table_name`: 要查询的表名。
- `condition`（可选）：用于过滤要计数的行的条件。

#### 示例 1：统计表中的所有行数

假设有一个名为"orders"的表，我们要统计其中的所有行数：<br>

```sql
SELECT COUNT(*) FROM orders;
```

这将返回表中的总行数。<br>

#### 示例 2：统计满足条件的行数

假设我们要统计"orders"表中"status"字段为"已完成"的订单数量：<br>

```sql
SELECT COUNT(*) FROM orders WHERE status = '已完成';
```

这将返回满足条件的订单数量。<br>

#### 示例 3：统计特定列的非NULL值数量

如果要统计某一列的非NULL值数量，可以指定列名作为COUNT的参数。例如，统计"customers"表中"email"列的非NULL值数量：<br>

```sql
SELECT COUNT(email) FROM customers;
```

这将返回"customers"表中"email"列的非NULL值数量。<br>

总之，COUNT函数是SQL中用于统计行数的强大工具，可以根据需要统计所有行或满足特定条件的行。<br>

### 向表中写入内容(INSERT INTO)：
要向MySQL某个表写入内容主要使用 `INSERT INTO` 和 `VALUES` 关键字。<br>
假设我们要向名为 `task_monitor` 的表中写入数据：<br>
```sql
INSERT INTO task_monitor (task_id, task_description, task_command, task_status, task_execution_time, log_path) 
VALUES (1, '任务1', '命令1', '成功', '2022-01-01 12:00:00', '/logs/task1.log');
```
<br>

### 更新表中的内容(UPDATE)：
更新MySQL某个表的内容，主要使用 `UPDATE` 、`SET` 和 `WHERE` 关键字。<br>

```sql
UPDATE task_monitor SET task_status = '失败', 
task_execution_time = '2022-01-02 10:00:00' WHERE task_id = 1;
```
SQL语句解释：这个示例将更新 `task_monitor` 表中 `task_id` 为 `1` 的记录的任务状态为 `'失败'`，以及任务执行时间为 `'2022-01-02 10:00:00'`。你可以根据需要更新其他字段的值，并使用 `WHERE` 子句来指定要更新的记录的条件。<br>

🚨🚨🚨注意字段字段之间要用逗号隔开，如：`SET task_status = '失败', task_execution_time = '2022-01-02 10:00:00'` ‼️‼️‼️<br>
<br>

再来个例子，假设只想更新这个表中 `'task_command'` 列所有为 `python app.py` 的数据呢？<br>

```sql
UPDATE task_monitor SET task_status = '失败', task_execution_time = '2022-01-02 10:00:00' 
WHERE task_command = 'python app.py';
```
> SQL语句支持断句的，看着怎么方便怎么来即可～

SQL语句解释：这个示例将更新 `task_monitor` 表中 `'task_command'` 列为 `'python app.py'` 的记录的任务状态为 `'失败'`，以及任务执行时间为 `'2022-01-02 10:00:00'`。只有满足 `WHERE` 子句条件的记录会被更新。你可以根据需要更新其他字段的值。<br>
<br>

### 删除表中的内容(DELETE)：
更新MySQL某个表的内容，主要使用 `DELETE` 和 `WHERE` 关键字。请谨慎使用，因为删除操作是不可逆的🚨🚨🚨<br>

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
<br>

## Python与MySQL：

应用程序(app或网页)获取到的用户输入、用户个人信息等信息都是存入MySQL的，怎么存呢？<br>

肯定是代码配合SQL语句，笔者主用python语言，就介绍一下python与SQL语句的联合使用。<br>

如果你只是在Navicat中操作，也可以从下列python代码中复制自己需要的SQL语句进行使用。<br>

### pymysql的安装：

python连接MySQL的方式有很多，例如 `pymysql`、`mysqlclient`、`aiomysql`。笔者常用的为连接方式为 `pymysql`，以下内容全部以 `pymysql+python`的方式介绍。<br>

pymysql的安装方式很简单，终端运行下列指令即可：<br>

```shell
pip install pymysql
```

### 使用pymysql测试连接MySQL：

首先要确保和MySQL数据库的正常连接才能进行更多的操作，将下列代码中 `host`、`user`、`password`、`database` 改为自己的信息即可。<br>

```python
import pymysql.cursors

try:
    print('----开始尝试连接MySQL----')
    mysql_connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Flameaway3.',
                                     database='irmdata',
                                     port=3306,
                                     cursorclass=pymysql.cursors.DictCursor)
    print('MySQL连接成功!!!')
except:
    print('MySQL连接失败。')
```

如果你是本地连接本地电脑搭建的MySQL数据库，`host` 不需要更改。如果你是本地连接远程服务器的MySQL，需要将 `host` 改为远程服务器对应的 `ip`，例如 `8.140.203.xxx`。

```python
host = '8.140.203.xxx'
```

如果你使用的是阿里云提供的MySQL数据库，那 `host` 改为阿里云提供给你的域名信息即可，类似于：`rdsxxxxxxxx.mysql.rds.aliyuncs.com`。<br>

```python
host = 'rdsxxxxxxxx.mysql.rds.aliyuncs.com'
```

### pymysql操作数据库的关键：

在python中使用pymysql连接MySQL时，`cursor` 是我们操作的基础，`cursor` 是用于执行SQL语句并处理查询结果的对象。<br>

具体来说，`cursor` 对象提供了以下功能：<br>

- 执行SQL语句: 可以使用 `execute()` 方法来执行SQL语句，可以是查询语句或非查询语句（如`INSERT` 、`UPDATE` 等）。
- 处理查询结果：可以使用`fetchone()`、 `fetchall()` 等方法来获取查询结果。`fetchone()` 用于获取一条记录，而 `fetchall()` 用于获取所有记录。还可以使用 `fetchmany()` 来获取指定数量的记录，例如获取SQL语句执行结果中的2条数据，`fetchmany(2)`。
- 控制事务：可以使用commit()方法提交事务或使用rollback()方法回滚事务。
- 获取执行结果信息：可以通过rowcount属性获取受影响的行数。此外，description属性可以获得查询结果集中列的元数据信息。
使用cursor可以灵活地执行SQL语句、处理结果集以及管理事务，进而实现对MySQL数据库的有效操作。<br>

💦💦💦了解pymysql中 `cursor` 的作用后，我们看下 `cursor` 的使用位置：<br>

> 只需要简单看下结构，了解在上一步的基础上扩充了哪些内容即可～🚀 更具体的用法，之后的内容会讲。

```python
import pymysql.cursors

try:
    print('----开始尝试连接MySQL----')
    mysql_connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Flameaway3.',
                                     database='irmdata',
                                     port=3306,
                                     cursorclass=pymysql.cursors.DictCursor)
    print('MySQL连接成功!!!')

    # 创建一个新的cursor对象
    with mysql_connection.cursor() as cursor:
        # 执行SQL命令
        sql = """..."""              # 输入自己的SQL命令；
        cursor.execute(sql)          # execute()方法用于执行SQL语句；
    # 提交更改
    mysql_connection.commit()
    print('SQL命令执行成功~')

except Exception as e:
    print(f'MySQL连接或创建表失败: {e}')

finally:
    # 关闭连接
    mysql_connection.close()
```

### 创建表：

了解了代码结构后，我们看下如何创建表。毕竟数据都存在表中，没有表我们就没有可操作的数据。^_^<br>

```python
import pymysql.cursors

################################################################################
# 注意：task_status 字段为集合，必须选择 ('成功', '失败') 其中一项进行写入。
################################################################################

try:
    print('开始尝试连接mysql----')
    mysql_connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Flameaway3.',
                                     database='irmdata',
                                     port=3306,
                                     cursorclass=pymysql.cursors.DictCursor)
    print('欧吼～mysql连接成功！！！')

    # 创建一个新的cursor对象
    with mysql_connection.cursor() as cursor:
        # 执行SQL命令
        sql = """
        CREATE TABLE task_monitor (
            task_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '任务的唯一ID',
            task_description VARCHAR(255) COMMENT '任务描述',
            task_command VARCHAR(255) COMMENT '执行的命令',
            task_status ENUM('成功', '失败') COMMENT '任务状态',
            task_execution_time DATETIME COMMENT '任务执行的时间',
            log_path VARCHAR(255) COMMENT '日志文件的路径'
        );
        """
        cursor.execute(sql)
    # 提交更改
    mysql_connection.commit()
    print('SQL命令执行成功~')

except Exception as e:
    print(f'mysql连接或创建表失败: {e}')

finally:
    # 关闭连接
    mysql_connection.close()
```

执行上述代码就可以在 `MySQL` 中名 `irmdata` 的 `database` 下创建一个 `task_monitor` 表。<br>

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/940d72e3-e339-4d93-ad33-f0eea9aa4647)

### 获取表中的内容：


## pymysql示例：

```python
from config import Mysql_Server_Config
import pymysql.cursors

# SQL语句:创建语义关系表
# 通过在`mean_en`字段上添加UNIQUE约束，确保了该字段的值在表中不会重复。如果尝试插入一个已经存在的`mean_en`值，将会引发唯一性约束违反的错误。
create_semantic_relation_table = """
CREATE TABLE semantic_relation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mean_en VARCHAR(255) NOT NULL UNIQUE COMMENT '语义关系_英文',
    mean_zh VARCHAR(255) NOT NULL COMMENT '语义关系_中文',
    subject_role VARCHAR(255) NOT NULL COMMENT '语义角色主体',
    object_role VARCHAR(255) NOT NULL COMMENT '语义角色客体',
    relation_id INT NOT NULL COMMENT '语义关系的ID',
    subject_role_id INT NOT NULL COMMENT '语义角色主体的ID',
    object_role_id INT NOT NULL COMMENT '语义角色客体的ID'
);
"""

# SQL语句:获取语义关系表所有数据
fetch_semantic_relation_all_data = """SELECT mean_en FROM semantic_relation"""

# fetch_semantic_relation_info = "SELECT subject_role, object_role FROM semantic_relation WHERE mean_en = %s", (mean_en,)

# SQL语句:删除语义关系表所有数据
drop_semantic_relation_table = """DROP TABLE semantic_relation;"""

def connect_to_mysql():
    """连接mysql
    """
    return pymysql.connect(host=Mysql_Server_Config['host'],
                           user=Mysql_Server_Config['user'],
                           password=Mysql_Server_Config['password'],
                           database=Mysql_Server_Config['database'],
                           port=3306,
                           cursorclass=pymysql.cursors.DictCursor)

def execute_sql_sentence(sql_sentence):
    """执行sql语句
    Args:
        sql_sentence:sql语句,格式如下:(\用于转义)
            \"\"\"SELECT * FROM funds_o_industry_vie LIMIT 3;\"\"\"
    """
    # 连接mysql
    mysql_conn = connect_to_mysql()
    # 创建一个新的cursor对象
    cursor = mysql_conn.cursor()
    # 执行SQL命令
    cursor.execute(sql_sentence)          # execute()方法用于执行SQL语句；
    # 提交更改
    mysql_conn.commit()
    # 关闭连接
    mysql_conn.close()

def fetch_semantic_data(sql_sentence):
    """根据语义关系中的mean_en获取subject_role和object_role的值。
    Args:
        sql_sentence:sql语句,格式如下:(\用于转义)
            \"\"\"SELECT * FROM funds_o_industry_vie LIMIT 3;\"\"\"
    Return:
        result:查询结果。
    """
    # 连接mysql
    mysql_conn = connect_to_mysql()
    # 创建一个新的cursor对象
    cursor = mysql_conn.cursor()
    try:
        # 执行SQL命令,如果也想获取mean_en，添加到sql语句即可，例如"SELECT mean_en, subject_role..."
        cursor.execute(sql_sentence)
        
        # 获取查询结果
        result = cursor.fetchall()
        return result
    finally:
        # 关闭连接
        mysql_conn.close()

def insert_data_into_semantic_relation_table(data):
    """将数据插入<语义关系表>
    Args:
        data:待插入数据,数据格式如下:
        {
            "Pat": {
                "mean_zh": "受事",
                "subject_role": "谓语",
                "object_role": "受事",
                "relation_id": 6001,
                "subject_role_id": 1001,
                "object_role_id": 1002
            }
        }
    """
    # 连接mysql
    mysql_conn = connect_to_mysql()
    # 创建一个新的cursor对象
    cursor = mysql_conn.cursor()

    for key, value in data.items():
        cursor.execute(
            "INSERT INTO semantic_relation (mean_en, mean_zh, subject_role, object_role, relation_id, subject_role_id, object_role_id) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (key, value["mean_zh"], value["subject_role"], value["object_role"], value["relation_id"], value["subject_role_id"], value["object_role_id"])
        )
    # 提交更改
    mysql_conn.commit()
    # 关闭连接
    mysql_conn.close()

if __name__ == "__main__":
    import json

    # 读取JSON文件
    with open('semantic_relation.json', 'r', encoding='utf-8') as file:
        semantic_data = json.load(file)
    # 向mysql的semantic_relation插入数据
    insert_data_into_semantic_relation_table(semantic_data)
```

如果你想要**创建semantic_relation表**，请修改`if __name__ == "__main__":`为以下形式:<br>

```python
if __name__ == "__main__":
    execute_sql_sentence(create_semantic_relation_table)
```

如果你想要从数据库中**获取** 'mean_en'的信息，请修改`if __name__ == "__main__":`为以下形式:<br>

```python
if __name__ == "__main__":
    res = fetch_semantic_data(fetch_semantic_relation_all_data)
    semantic_relation_list = []
    for item in res:
        semantic_relation_list.append(item['mean_en'])
    print(semantic_relation_list)
```

终端输出如下:<br>

```log
['Accd', 'Belg', 'Clas', 'Comp', 'Cons', 'Cont', 'dBelg', 'dClas', 'dCont', 'Desc', 'dExp', 'dPat', 'eCoo', 'eSelt', 'Exp', 'Freq', 'Host', 'Lfin', 'Lini', 'Loc', 'Mann', 'mDir', 'mNeg', 'mRange', 'mTime', 'Pat', 'Poss', 'Prod', 'Qp', 'Quan', 'rCont', 'Reas', 'rExp', 'rPat', 'rReas', 'Time', 'Tmod']
```

如果你想要**删除semantic_relation表**，请修改`if __name__ == "__main__":`为以下形式:<br>

```python
if __name__ == "__main__":
    execute_sql_sentence(drop_semantic_relation_table)
```

🚨🚨🚨请注意:这条语句将删除名为`semantic_relation`的表格及其所有数据和结构。请确保在执行此操作之前备份重要的数据，以防不必要的数据丢失。<br>

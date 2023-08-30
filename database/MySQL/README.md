# MySQL
MySQL是一种开源的关系型数据库管理系统（RDBMS），广泛用于存储、管理和检索结构化数据。当前大多数公司用的都是MySQL数据库，所以掌握MySQL数据库的使用是必须的。<br>

笔者使用的是Ubuntu 18.04.6系统，就以此讲解 MySQL 数据库的安装、配置信息查看和常规操作。<br>
- [MySQL](#mysql)
  - [服务器安装MySQL数据库：](#服务器安装mysql数据库)
  - [终端MySQL常用指令(开启、关闭、重启、状态指令)：](#终端mysql常用指令开启关闭重启状态指令)
  - [查看MySQL配置信息：](#查看mysql配置信息)
  - [MySQL密码设置：(root账号)](#mysql密码设置root账号)
  - [本地使用 Navicat 远程连接 MySQL ：](#本地使用-navicat-远程连接-mysql-)
  - [Python与MySQL：](#python与mysql)
    - [使用pymysql测试连接MySQL：](#使用pymysql测试连接mysql)
    - [pymysql操作数据库的关键：](#pymysql操作数据库的关键)
    - [创建表：](#创建表)
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

## Python与MySQL：
在应用程序中，获取用户输入等信息都是存入MySQL的，怎么存呢？肯定是代码配合SQL语句。笔者主用的python，就介绍一下python与SQL语句的联合使用。如果你只是在Navicat中操作，也可以从下列python代码中复制自己需要的SQL语句进行使用。<br>

python连接MySQL的方式有很多，例如 `pymysql`、`mysqlclient`、`aiomysql`。笔者常用的为连接方式为 `pymysql`，以下内容全部以 `pymysql+python`的方式介绍。<br>
pymysql的安装方式很简单：<br>
```shell
pip install pymysql
```

### 使用pymysql测试连接MySQL：
首先要确保和MySQL数据库的正常连接才能进行更多的操作，将下列代码中 `host`、`user`、`password`、`database` 改为自己的信息即可。<br>
```python
import pymysql.cursors

try:
    print('----开始尝试连接MySQL----')
    tmp_connection = pymysql.connect(host='localhost',
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

了解pymysql中 `cursor` 的作用后，我们看下 `cursor` 的使用位置：<br>
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
要创建一个MySQL数据库中的表格，需要使用 `CREATE TABLE` 语句。以下是一个示例代码来创建一个名为 `"task_monitor"` 的表格，其中包括 `"task_id"`、`"task_description"`、 `"task_command"` 、`task_status`、 `task_status`、 `task_execution_time`、 `log_path` 这六个列：<br>
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

相信大家已经注意到了，我写的大大的注释 `注意：task_status 字段为集合，必须选择 ('成功', '失败') 其中一项进行写入。` ，这是因为MySQL支持多种数据类型，可以根据具体需要选择适合的数据类型。以下是常见的MySQL数据类型：<br>

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
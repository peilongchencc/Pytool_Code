# python sdk of mysql

python连接MySQL的方式有很多，例如 `pymysql`、`aiomysql`、`mysqlclient`。本章主要介绍 `pymysql` 和 `aiomysql` 的使用。<br>

- [python sdk of mysql](#python-sdk-of-mysql)
  - [pymysql--同步 MySQL 客户端/服务器库:](#pymysql--同步-mysql-客户端服务器库)
    - [pymysql的安装：](#pymysql的安装)
    - [使用pymysql测试连接MySQL：](#使用pymysql测试连接mysql)
    - [pymysql操作数据库的关键：](#pymysql操作数据库的关键)
    - [pymysql(非连接池方式)示例：](#pymysql非连接池方式示例)
    - [检查mysql中是否存在某个表](#检查mysql中是否存在某个表)
    - [pymysql连接池示例:](#pymysql连接池示例)
    - [pymysql(连接池方式)代码示例:](#pymysql连接池方式代码示例)
    - [异步编程--aiomysql:](#异步编程--aiomysql)
  - [aiomysql-异步 MySQL 客户端/服务器库:](#aiomysql-异步-mysql-客户端服务器库)
    - [aiomysql的安装:](#aiomysql的安装)
    - [aiomysql使用示例:](#aiomysql使用示例)
      - [配置文件示例(`.env.local`):](#配置文件示例envlocal)
      - [准备sql语句文件:](#准备sql语句文件)
      - [python中sql语句常见的使用方式(可选章节):](#python中sql语句常见的使用方式可选章节)
      - [主程序代码:](#主程序代码)

## pymysql--同步 MySQL 客户端/服务器库:

PyMySQL 是一个 Python 数据库连接库，用于连接 MySQL 数据库。它允许 Python 程序与 MySQL 数据库进行交互，执行查询、插入、更新等操作。PyMySQL 是一个纯 Python 实现，不依赖于 MySQL 客户端库，因此易于安装和使用。<br>

### pymysql的安装：

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

- 控制事务：可以使用 `commit()` 方法提交事务或使用 `rollback()` 方法回滚事务。

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

### pymysql(非连接池方式)示例：

```python
from config import Mysql_Server_Config
import pymysql.cursors

# SQL语句:创建语义关系表
# 通过在`mean_en`字段上添加UNIQUE约束，确保了该字段的值在表中不会重复。如果尝试插入一个已经存在的`mean_en`值，将会引发唯一性约束违反的错误。
# 时间字段格式类似于:"2023-10-25 11:55:26"，如果某一行字段有修改，"modify_time"会自动修改。
create_semantic_relation_table = """
CREATE TABLE semantic_relation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mean_en VARCHAR(255) NOT NULL UNIQUE COMMENT '语义关系_英文',
    mean_zh VARCHAR(255) NOT NULL COMMENT '语义关系_中文',
    subject_role VARCHAR(255) NOT NULL COMMENT '语义角色主体',
    object_role VARCHAR(255) NOT NULL COMMENT '语义角色客体',
    relation_id INT NOT NULL COMMENT '语义关系的ID',
    subject_role_id INT NOT NULL COMMENT '语义角色主体的ID',
    object_role_id INT NOT NULL COMMENT '语义角色客体的ID',
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    modify_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间'
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

### 检查mysql中是否存在某个表

请注意，下列代码省略了 `connect_to_mysql()` 中连接mysql的具体代码，但无关紧要，重要的是其他部分~<br>

```python
if __name__ == "__main__":
    # # 创建语义关系表
    # execute_sql_sentence(create_semantic_relation_table)
    
    # 连接mysql
    mysql_conn = connect_to_mysql()
    # 创建一个新的cursor对象
    mysql_cursor = mysql_conn.cursor()
    
    # 检查是否存在semantic_relation表,有则返回1,无则返回0
    table_exists = mysql_cursor.execute("SHOW TABLES LIKE 'semantic_relation'")

    if table_exists:
        print(f"mysql中存在该表。")
        
        # 如果表存在，删除它
        # mysql_cursor.execute("DROP TABLE semantic_relation")
```

### pymysql连接池示例:

在Python中，`pymysql`是一个用于连接MySQL数据库的库。但是，`pymysql`本身并不提供连接池功能。不过，你可以使用`DBUtils`这个第三方库，它提供了对`pymysql`的连接池支持。以下是一个使用`DBUtils`中的`PooledDB`来创建连接池并从MySQL数据库中获取数据的示例代码：<br>

首先，你需要安装`DBUtils`：<br>

```bash
pip install DBUtils
```

接着，你可以使用如下代码创建连接池并从MySQL数据库中查询数据：<br>

```python
# db_utils.py
import pymysql
from dbutils.pooled_db import PooledDB

# mysql连接配置信息：
Mysql_Server_Config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Flameaway3.',
        'database': 'irmdata',
        'port': 3306
    }

# 创建连接池
mysql_pool = PooledDB(
    creator=pymysql,  # 使用pymysql作为数据库连接库
    maxconnections=None,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，连接池至少创建的空闲的连接，0表示不创建
    maxcached=None,  # 连接池空闲的最多连接数，0和None表示不限制
    maxshared=None,  # 连接池中最多共享的连接数量，0和None表示全部共享
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待
    maxusage=None,  # 一个连接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表
    ping=0,  # ping MySQL服务端，检查是否服务可用
    **Mysql_Server_Config
)

def conn_mysql():
    # 获取mysql连接
    conn = mysql_pool.connection()
    return conn

def fetchall_from_mysql(sql):
    # 连接到mysql
    conn = conn_mysql()
    # 使用 DictCursor 定义游标，以便每一行结果都作为字典返回
    mysql_cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        # 利用游标执行sql语句
        mysql_cursor.execute(sql)
        return mysql_cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        # 关闭游标
        mysql_cursor.close()
        # conn.close()  # 只需要关闭游标，不关闭连接，连接池会负责管理连接的生命周期。

if __name__ == "__main__":
    res = fetchall_from_mysql("SELECT * FROM metadata_test")
    for item in res:
        print(item)
```

终端显示:<br>

```txt
{'id': 1, 'test_data': '黄金', 'create_time': datetime.datetime(2023, 11, 6, 20, 0, 50), 'modify_time': datetime.datetime(2023, 11, 6, 20, 0, 50)}
{'id': 2, 'test_data': '暴涨', 'create_time': datetime.datetime(2023, 11, 6, 20, 1, 15), 'modify_time': datetime.datetime(2023, 11, 6, 22, 42, 51)}
{'id': 3, 'test_data': '军工板块', 'create_time': datetime.datetime(2023, 11, 6, 20, 1, 35), 'modify_time': datetime.datetime(2023, 11, 6, 22, 23, 15)}
{'id': 4, 'test_data': '百货', 'create_time': datetime.datetime(2023, 11, 6, 22, 42, 29), 'modify_time': datetime.datetime(2023, 11, 6, 22, 46, 46)}
```

> 如果某个字段为空，对应的结果为空字符串，而不会直接跳过该字段，类似 `'test_data': ''`。

在其他需要数据库连接的模块中，就可以采用下列方式从mysql连接池获取一条连接进行查询：<br>

```python
from db_utils import fetchall_from_mysql

# 在这个模块中你可以使用 fetchall_from_mysql 函数
# 它将使用 db_utils.py 中定义的连接池
```

这样，你就可以确保在应用的任何地方使用`fetchall_from_mysql`时，都是通过同一个连接池来管理数据库连接。<br>

如果你不想要数据的解决含有字段信息(即字典格式)，可以简单修改`fetchall_from_mysql`中的`mysql_cursor`，参考代码如下:<br>

```python
def fetchall_from_mysql(sql):
    # 连接到mysql
    conn = conn_mysql()
    # 定义游标
    mysql_cursor = conn.cursor()
    try:
        # 利用游标执行sql语句
        mysql_cursor.execute(sql)
        return mysql_cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        # 关闭游标
        mysql_cursor.close()
        # conn.close()  # 只需要关闭游标，不关闭连接，连接池会负责管理连接的生命周期。
```

终端显示:<br>

```txt
(1, '黄金', datetime.datetime(2023, 11, 6, 20, 0, 50), datetime.datetime(2023, 11, 6, 20, 0, 50))
(2, '暴涨', datetime.datetime(2023, 11, 6, 20, 1, 15), datetime.datetime(2023, 11, 6, 22, 42, 51))
(3, '军工板块', datetime.datetime(2023, 11, 6, 20, 1, 35), datetime.datetime(2023, 11, 6, 22, 23, 15))
(4, '百货', datetime.datetime(2023, 11, 6, 22, 42, 29), datetime.datetime(2023, 11, 6, 22, 46, 46))
```

### pymysql(连接池方式)代码示例:

```python
import pymysql
import time
import json
import re
from dbutils.pooled_db import PooledDB

# mysql连接配置信息：
Mysql_IRM_Config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Flameaway3.',
        'database': 'irmdata',
        'port': 3306
    }

# 创建连接池,这里的写法即使因文件内部函数被调用,也不会创建新的连接池,而是复用已有的连接。
mysql_pool = PooledDB(
    creator=pymysql,  # 使用pymysql作为数据库连接库
    maxconnections=None,  # 连接池允许的最大连接数,0和None表示不限制连接数
    mincached=2,  # 初始化时,连接池至少创建的空闲的连接,0表示不创建
    maxcached=None,  # 连接池空闲的最多连接数,0和None表示不限制
    maxshared=None,  # 连接池中最多共享的连接数量,0和None表示全部共享
    blocking=True,  # 连接池中如果没有可用连接后,是否阻塞等待
    maxusage=None,  # 一个连接最多被重复使用的次数,None表示无限制
    setsession=[],  # 开始会话前执行的命令列表
    ping=0,  # ping MySQL服务端,检查是否服务可用
    **Mysql_IRM_Config
)

def conn_mysql():
    # 获取mysql连接
    mysql_conn = mysql_pool.connection()
    return mysql_conn

def current_timestamp():
    """返回当前日期时间的字符串表示形式,格式为: 2023-08-15 11:29:22 """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

####################################################################
# 在MySQL中创建表和删除表
# 注意:
# 在mysql中创建表和删除表最好通过在Navicat或其他MySQL操作台执行，避免创建
# 同名表报错，或无意间删除含有重要数据的表。
# SQL示例--检查表 'my_table' 是否存在: 
# SHOW TABLES LIKE 'my_table'  # 执行后返回的是0/1，即False/True
# SQL示例--删除表 'my_table': 
# DROP TABLE 'my_table'
####################################################################

####################################################################
# 在MySQL中执行插入、更新、删除数据等操作。
####################################################################

def execute_sql_sentence_usual_without_return(sql, params=None, return_affected_rows=False, return_increased_id=False):
    """执行SQL语句,可用于插入、更新、删除等操作。通常无返回值。
    Args:
        sql (str): SQL语句,其中的参数使用%s作为占位符。
        params (tuple, optional): 与SQL语句中的占位符相对应的参数元组。默认为None。
        return_affected_rows(bool): 是否返回受影响的行数,可用户判断更新语句是否成功更新了数据。
        return_increased_id(bool): 返回最近插入行的自增ID, 插入milvus可能需要用到。
    """
    try:
        # 连接池方式连接mysql
        mysql_conn = conn_mysql()
        # 普通游标 mysql_conn.cursor() 返回的结果是元组，不含有键名。如果想要以字典形式返回，需要使用下列形式。
        mysql_cursor = mysql_conn.cursor()

        mysql_cursor.execute(sql, params)
        mysql_conn.commit()
        print("操作成功完成。")
        if return_affected_rows:
            # 返回受影响的行数
            # 需要注意,执行更新操作时,传入的更新数据于原数据相同不会更新,返回值为0。
            return mysql_cursor.rowcount
        if return_increased_id:
            # 获取最近插入行的自增ID, 插入milvus可能需要用到
            mysql_cursor.execute("SELECT LAST_INSERT_ID();")
            inserted_id = mysql_cursor.fetchone()[0]  # 获取返回的ID
            return inserted_id  # 返回获取到的ID
        
    except pymysql.MySQLError as e:
        print(f"执行SQL时出现错误: {e}")
        mysql_conn.rollback()
    finally:
        mysql_cursor.close()
        mysql_conn.close()

####################################################################
# 在MySQL中执行查询操作。
####################################################################

def execute_sql_sentence_with_return(sql, params=None, return_one=False):
    """执行SQL语句,用于查询操作,有返回值。
    Args:
        sql(str): 查询所用SQL语句,其中的参数使用%s作为占位符。例如 sql = "SELECT * FROM image_hold_share WHERE image_url = %s"
        params (tuple, optional): 与SQL语句中的占位符相对应的参数元组。默认为None。
    Returns:
        query_result(list中嵌套dict): 匹配到的数据，可以通过遍历的形式获取匹配到的所有内容。
    """
    try:
        # 连接到mysql
        mysql_conn = conn_mysql()
        # 普通游标 mysql_conn.cursor() 返回的结果是元组，不含有键名。如果想要以字典形式返回，需要使用下列形式。
        mysql_cursor = mysql_conn.cursor(pymysql.cursors.DictCursor)
        mysql_cursor.execute(sql, params)
        if return_one:
            # 获取单条查询结果，可用于检查某一项是否存在于表中
            # 如果没有匹配到结果，会返回 None。
            # 如果有匹配到结果，返回的是字典的结构，例如 {'id':1, 'image_url':'https://be...'}
            query_result = mysql_cursor.fetchone()
        else:
            # (默认)获取全部查询结果，如果没有值返回的是空元组，例如 ()。
            # 如果有匹配到结果，返回的是列表中嵌套字典的结构，例如 [{'id':1, 'image_url':'https://be...'}]
            # 某些键对应的值为空，也会返回内容，只不过是空字符串，例如 'type':''。
            query_result = mysql_cursor.fetchall()
        return query_result
    except pymysql.MySQLError as e:
        print(f"执行SQL时出现错误: {e}")
        mysql_conn.rollback()
    finally:
        mysql_cursor.close()
        mysql_conn.close()


if __name__ == '__main__':
    # UPDATE操作不需要根据 image_url 检查是否已有数据存在，UPDATE操作如果不符合WHERE操作不报错，只是修改的数据行数为0。
    # 构建更新SQL语句
    update_sql = """
        UPDATE image_hold_share
        SET update_fund_code = %s, update_hold_share = %s
        WHERE image_url = %s
    """
    params = ('677777', '', 'https://beta.7min.com.cn/user/file/download/?filePath=/positionimages/202401/20240112102706-1.jpg')
    rtn = execute_sql_sentence_usual_without_return(update_sql, params, return_affected_rows=True)
    print(rtn, type(rtn))   # 1 <class 'int'>
```


### 异步编程--aiomysql:

使用`pymysql`直接进行异步编程是不行的，因为`pymysql`是一个同步的MySQL数据库客户端库，它不支持异步操作。在同步代码中执行数据库查询和其他操作会阻塞当前线程，直到操作完成。这意味着在等待数据库响应期间，程序不能执行其他任务。<br>

异步编程模型允许在等待外部操作（如网络请求、数据库查询等）完成时执行其他任务。这是通过事件循环来实现的，事件循环可以管理多个任务的执行，允许单个线程中并发运行多个任务。<br>

为了实现这种模型，需要使用设计为异步的库，这些库使用`async`和`await`关键字来标记异步操作和等待它们的结果，而不会阻塞事件循环。<br>

因此，要在异步编程中操作MySQL数据库，你需要使用`aiomysql`这样的库。`aiomysql`是基于`PyMySQL`和`asyncio`（Python的异步I/O框架）开发的，提供了异步的数据库操作接口，可以在协程中使用，与`asyncio`的异步编程模型兼容。使用`aiomysql`可以让你的数据库操作非阻塞且高效，特别是在开发高并发的应用时。<br>


## aiomysql-异步 MySQL 客户端/服务器库:

使用`pymysql`直接进行异步编程是不行的，因为`pymysql`是一个同步的MySQL数据库客户端库，它不支持异步操作。在同步代码中执行数据库查询和其他操作会阻塞当前线程，直到操作完成。这意味着在等待数据库响应期间，程序不能执行其他任务。<br>

`aiomysql`是基于`PyMySQL`和`asyncio`（Python的异步I/O框架）开发的，提供了异步的数据库操作接口，可以在协程中使用，与`asyncio`的异步编程模型兼容。使用`aiomysql`可以让你的数据库操作非阻塞且高效，特别是在开发高并发的应用时。<br>

### aiomysql的安装:

```bash
pip install aiomysql
```

### aiomysql使用示例:

#### 配置文件示例(`.env.local`):

```conf
# mysql连接信息
MYSQL_DB_HOST="localhost"
MYSQL_DB_PORT="3306"
MYSQL_DB_USER="root"
MYSQL_DB_PASSWORD="Flameaway3."
# mysql数据库名称
MYSQL_DB_NAME="irmdata"
```

#### 准备sql语句文件:

| 目录                                  | 备注          |
| ------------------------------------ | ------------ |
| university_admission_information.sql | 大学录用信息表  |
| university_major_information.sql     | 大学专业信息表  |

数据展示效果如下:<br>

**大学录用信息表:**<br>

| 大学 | 专业 | 招生人数 |
| --- | --- | --- |
| 北京工业大学 | 数学 | 12 |
| 北京工业大学 | 物理 | 11 |

**大学专业信息表:**<br>

| 大学 | 专业 | 研究方向 |
| --- | --- | --- |
| 北京工业大学 | 数学 | 应用数学 |
| 北京工业大学 | 数学 | 基础数学 |
| 北京工业大学 | 物理 | 应用物理 |

#### python中sql语句常见的使用方式(可选章节):

1. 直接在代码中硬编码：对于一些简单的或者使用频率很高的SQL语句，可以直接在Python代码中以字符串的形式硬编码。这种方法的好处是直观、快捷，但是对于复杂或者数量较多的SQL语句，这种方法会使代码变得难以维护。

2. 使用多行字符串将sql语句转为python变量：Python的多行字符串（triple-quoted string）可以让复杂的SQL语句保持原有的格式，提高了代码的可读性。这对于复杂的SQL查询尤其有用。

可以将sql放入程序代码中,也可以单独为sql文件创建一个 `sql_senteces.py` 脚本,利用 `from xxx import xxx` 的方式使用。<br>

```python
import aiomysql

# 省略

# 创建大学招生信息表
create_table_admission = """
CREATE TABLE IF NOT EXISTS `university_admission_information`  (
    `id` int(11) AUTO_INCREMENT PRIMARY KEY,
    `university_name` varchar(255) NOT NULL COMMENT '大学名称',
    `major` varchar(255) NOT NULL COMMENT '专业名称',
    `num_of_major_admissions` int(11) NULL DEFAULT NULL COMMENT '专业招生人数',
    `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;
"""

async def execute_mysql_command(mysql_pool, sql_sentence):
    # 省略
    pass

if __name__ == "__main__":
    # 省略
    pass

```

3. SQL文件：将SQL语句存储在 `xxx.sql` 文件中，然后在Python代码中读取这些文件。

这种方法的好处是SQL语句和Python代码分离，易于管理和维护，特别是对于非常复杂或数量很多的SQL语句。<br>

对于数据库导出的sql文件,可以直接使用。<br>

🏖️具体如何使用,可以根据项目的具体需求和个人偏好选择最适合的方式。<br>

#### 主程序代码:

```python
"""
File path:multiple_table_join_query_example.py
Author: peilongchencc@163.com
Description: mysql多表联合查询示例
Requirements: 
1. pip install python-dotenv aiomysql
2. 当前目录下创建 `.env.local` 文件,写入配置项
3. 准备好需要的sql脚本
Reference Link: 
Notes: 
aiomysql返回的数据格式由游标决定:
- `async with conn.cursor() as cur:` 返回的结果是元组。
    输出示例: (('北京工业大学', '数学', '应用数学', 12), ('北京工业大学', '数学', '基础数学', 12), ('北京工业大学', '物理', '应用物理', 11))
- `async with conn.cursor(aiomysql.DictCursor) as cur:` 返回的结果是字典。
    输出示例: [{'university_name': '北京工业大学', 'major': '数学', 'research_direction': '应用数学', 'num_of_major_admissions': 12}, {'university_name': '北京工业大学', 'major': '数学', 'research_direction': '基础数学', 'num_of_major_admissions': 12}, {'university_name': '北京工业大学', 'major': '物理', 'research_direction': '应用物理', 'num_of_major_admissions': 11}]
"""
import os
import time
import asyncio
import aiomysql
from dotenv import load_dotenv
load_dotenv('.env.local')

def read_file(file_path):
    """读取文件并将其作为一个字符串返回。
    Args:
        file_path(str):文件路径。
    Return:
        readed_result(str):读取的结果。
    Notes:
    `read()`函数会一次性读取整个文件内容，并将其作为一个字符串（对于文本文件）或字节串（对于二进制文件）返回。
    `readline()`函数从文件中一次读取一行内容，并返回字符串。
    `readlines()`函数一次性读取文件中所有行，并将其存储为列表，列表中的每个元素是文件的一行。
    """
    with open(file_path, "r") as file:
        readed_result = file.read()
    return readed_result

def current_timestamp():
    """返回当前日期时间的字符串表示形式,格式为: 2023-08-15 11:29:22 """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

async def create_mysql_pool():
    """基于aiomysql创建连接池
    """
    try:
        # 从环境变量中获取数据库连接信息
        mysql_db_host = os.getenv("MYSQL_DB_HOST")
        mysql_db_port = int(os.getenv("MYSQL_DB_PORT")) # 字符串要转int,端口号需要int类型
        mysql_db_user = os.getenv("MYSQL_DB_USER")
        mysql_db_password = os.getenv("MYSQL_DB_PASSWORD")
        mysql_db_name = os.getenv("MYSQL_DB_NAME")
        
        # 创建连接池
        mysql_pool = await aiomysql.create_pool(
            host=mysql_db_host,
            port=mysql_db_port,
            user=mysql_db_user,
            password=mysql_db_password,
            db=mysql_db_name,
            minsize=5,
            maxsize=10
        )
        return mysql_pool
    except Exception as e:
        print(f"Error occurred while creating MySQL pool: {e}")

async def execute_mysql_command(sql_sentence):
    """执行非查询的MySQL命令(如INSERT, UPDATE, CREATE)
    Args:
        sql_sentence(str): SQL语句。
    """
    try:
        # 从mysql连接池获取的连接
        mysql_pool = await create_mysql_pool()
        async with mysql_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql_sentence)
                await conn.commit()  # 确保执行了commit操作
    except Exception as e:
        print(f"Error occurred while executing MySQL command: {e}")
        # 如果执行出错，则回滚数据
        await conn.rollback()

async def fetch_data_from_mysql(sql_sentence):
    """从mysql中获取数据,以字典形式(DictCursor)返回每行数据。
    Args:
        sql_sentence(str): SQL查询语句,例如 "SELECT * FROM your_table;"。
    Return:
        fetch_result(list): 查询结果,格式为列表中每一项为字典。
    """
    try:
        # 从mysql连接池获取的连接
        mysql_pool = await create_mysql_pool()
        async with mysql_pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:  # 使用DictCursor
                await cur.execute(sql_sentence)
                # 获取查询结果
                fetch_result = await cur.fetchall()
                return fetch_result
    except Exception as e:
        print(f"Error occurred while fetching data from MySQL: {e}")

async def main():
    # 读取sql文件为字符串
    table_admission = read_file("university_admission_information.sql")
    table_major = read_file("university_major_information.sql")

    # 执行sql语句
    await execute_mysql_command(table_admission)
    await execute_mysql_command(table_major)

    # 执行查询,联合这两个表查询每个专业的招生人数和研究方向。
    query = """
    SELECT a.university_name, a.major, m.research_direction, a.num_of_major_admissions
    FROM university_admission_information a
    JOIN university_major_information m ON a.university_name = m.university_name AND a.major = m.major;
    """
    data = await fetch_data_from_mysql(query)
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
```

终端输出:<br>

```log
[{'university_name': '北京工业大学', 'major': '数学', 'research_direction': '应用数学', 'num_of_major_admissions': 12}, {'university_name': '北京工业大学', 'major': '数学', 'research_direction': '基础数学', 'num_of_major_admissions': 12}, {'university_name': '北京工业大学', 'major': '物理', 'research_direction': '应用物理', 'num_of_major_admissions': 11}]
```

json方式的效果:<br>

```json
[
    {
        "university_name": "北京工业大学",
        "major": "数学",
        "research_direction": "应用数学",
        "num_of_major_admissions": 12
    },
    {
        "university_name": "北京工业大学",
        "major": "数学",
        "research_direction": "基础数学",
        "num_of_major_admissions": 12
    },
    {
        "university_name": "北京工业大学",
        "major": "物理",
        "research_direction": "应用物理",
        "num_of_major_admissions": 11
    }
]
```


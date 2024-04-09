# python sdk of mysql

## aiomysql

### 配置文件示例(`.env.local`):

```conf
# mysql连接信息
MYSQL_DB_HOST="localhost"
MYSQL_DB_PORT="3306"
MYSQL_DB_USER="root"
MYSQL_DB_PASSWORD="Flameaway3."
# mysql数据库名称
MYSQL_DB_NAME="irmdata"
```

### 准备sql语句文件:

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

### python中sql语句常见的使用方式(可选章节):

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

### 主程序代码:

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

async def execute_mysql_command(mysql_pool, sql_sentence):
    """执行非查询的MySQL命令(如INSERT, UPDATE, CREATE)
    """
    async with mysql_pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql_sentence)
            await conn.commit()  # 确保执行了commit操作

async def fetch_data_from_mysql(mysql_pool, sql_sentence):
    """从mysql中获取数据,以字典形式(DictCursor)返回每行数据。
    Args:
        mysql_pool: 从mysql连接池获取的链接。
        sql_sentence(str): SQL查询语句,例如 "SELECT * FROM your_table;"。
    Return:
        fetch_result(list): 查询结果,格式为列表中每一项为字典。
    """
    async with mysql_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:  # 使用DictCursor
            await cur.execute(sql_sentence)
            # 获取查询结果
            fetch_result = await cur.fetchall()
            return fetch_result

async def main():
    # 读取sql文件为字符串
    table_admission = read_file("university_admission_information.sql")
    table_major = read_file("university_major_information.sql")
    
    # 创建mysql连接池
    mysql_pool = await create_mysql_pool()

    # 执行sql语句
    await execute_mysql_command(mysql_pool, table_admission)
    await execute_mysql_command(mysql_pool, table_major)

    # 执行查询,联合这两个表查询每个专业的招生人数和研究方向。
    query = """
    SELECT a.university_name, a.major, m.research_direction, a.num_of_major_admissions
    FROM university_admission_information a
    JOIN university_major_information m ON a.university_name = m.university_name AND a.major = m.major;
    """
    data = await fetch_data_from_mysql(mysql_pool, query)
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


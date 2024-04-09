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

### sql语句文件:

```python
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
# 创建大学专业信息表
create_table_major = """
CREATE TABLE IF NOT EXISTS `university_major_information`  (
    `id` int(11) AUTO_INCREMENT PRIMARY KEY,
    `university_name` varchar(255) NOT NULL COMMENT '大学名称',
    `major` varchar(255) NOT NULL COMMENT '专业名称',
    `research_direction` varchar(255) NULL DEFAULT NULL COMMENT '研究方向',
    `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;
"""

# 向大学招生信息表插入数据
insert_admission_data = """
INSERT INTO `university_admission_information` (`university_name`, `major`, `num_of_major_admissions`) VALUES
('北京工业大学', '数学', 12),
('北京工业大学', '物理', 11);
"""
# 向大学专业信息表插入数据
insert_major_data = """
INSERT INTO `university_major_information` (`university_name`, `major`, `research_direction`) VALUES
('北京工业大学', '数学', '应用数学'),
('北京工业大学', '数学', '基础数学'),
('北京工业大学', '物理', '应用物理');
"""
```

待写入的数据以markdown形式展示的效果如下:<br>

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

### 主程序代码:

```python
"""
Author: peilongchencc@163.com
Description: mysql多表联合查询示例
Requirements: 
1. pip install python-dotenv aiomysql
2. 当前目录下创建 `.env.local` 文件,写入配置项
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
from sql_senteces import create_table_admission,create_table_major,insert_admission_data,insert_major_data
load_dotenv('.env.local')

def current_timestamp():
    """返回当前日期时间的字符串表示形式,格式为: 2023-08-15 11:29:22 """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

async def create_mysql_pool():
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
    """执行非查询的MySQL命令（如INSERT, UPDATE, CREATE）"""
    async with mysql_pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql_sentence)
            await conn.commit()  # 确保执行了commit操作

async def fetch_data_from_mysql(mysql_pool, sql_sentence):
    """从mysql中获取数据,以字典形式返回每行数据。
    Args:
        mysql_pool: 从mysql连接池获取的链接。
        sql_sentence(str): SQL查询语句,例如 "SELECT * FROM your_table;"。
    """
    async with mysql_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:  # 使用DictCursor
            await cur.execute(sql_sentence)
            # 获取查询结果
            result = await cur.fetchall()
            return result

async def main():
    # 创建连接池
    mysql_pool = await create_mysql_pool()

    # 调用建表
    await execute_mysql_command(mysql_pool, create_table_admission)
    await execute_mysql_command(mysql_pool, create_table_major)

    # 调用插入数据
    await execute_mysql_command(mysql_pool, insert_admission_data)
    await execute_mysql_command(mysql_pool, insert_major_data)

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

```txt
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
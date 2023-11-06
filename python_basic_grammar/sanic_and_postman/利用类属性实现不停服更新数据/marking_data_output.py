# marking_data_output.py
import pymysql.cursors

# SQL语句:创建某表
# 时间字段格式类似于:"2023-10-25 11:55:26"，如果某一行字段有修改，"modify_time"会自动修改。
create_semantic_relation_table = """
CREATE TABLE metadata_test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    test_data VARCHAR(255) NOT NULL UNIQUE COMMENT '元数据',
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    modify_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间'
);
"""

# SQL语句:
fetch_semantic_relation_all_data = """SELECT test_data FROM metadata_test"""

# SQL语句:删除某表所有数据
drop_semantic_relation_table = """DROP TABLE metadata_test;"""

def connect_to_mysql():
    """连接mysql
    """
    return pymysql.connect(host='localhost',
                           user='root',
                           password='Flameaway3.',
                           database='irmdata',
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

def refresh_metadata(sql_sentence=fetch_semantic_relation_all_data):
    # 连接mysql
    mysql_conn = connect_to_mysql()
    # 创建一个新的cursor对象
    cursor = mysql_conn.cursor()
    try:
        # 执行SQL命令
        cursor.execute(sql_sentence)
        
        # 获取查询结果
        result = cursor.fetchall()
        return result
    finally:
        # 关闭连接
        mysql_conn.close()
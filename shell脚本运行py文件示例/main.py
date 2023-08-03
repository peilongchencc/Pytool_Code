#####################################################
# 本文件用于将mysql中表格x的时间段A--时间段B的数据存储到本地：
# 输入：
# sql_query_statement = "SELECT * FROM qa_template WHERE create_time >= '2023-07-24 00:00:00' AND create_time < '2023-07-25 00:00:00';" 
# 注意修改sql语句中的 "表名"、"字段名"、"时间间隔"
# 
# 输出：
# download_mysql_data.json，文件中内容类似：
# {"id": 6115, "intentId": 1767, "code": "WJT-8-20230724-1", "question": "\u3010\u667a\u80fd\u6da8\u8dcc\u63d0\u9192\u3011\u53ef\u4ee5\u89e3\u51b3\u4ec0\u4e48\u95ee\u9898", "create_time": "2023-07-24 11:53:02", "sdpTemplateId": -1}
# {"id": 6116, "intentId": 1768, "code": "WJT-8-20230724-2", "question": "\u3010\u6b62\u76c8\u8865\u4ed3\u91cd\u8981\u7b49\u7ea7\u63d0\u9192\u3011\u80fd\u89e3\u51b3\u4ec0\u4e48\u95ee\u9898", "create_time": "2023-07-24 11:53:02", "sdpTemplateId": -1}
# {"id": 6117, "intentId": 134, "code": "WJT-5-20230724-3", "question": "\u5916\u90e8\u6301\u4ed3\u600e\u4e48\u6dfb\u52a0", "create_time": "2023-07-24 11:53:02", "sdpTemplateId": -1}
#####################################################

import json
import pymysql.cursors

def main(sql_query, saved_file_path):
    # 连接数据库
    try:
        print('开始尝试连接自己建立的mysql----')
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Flameaway3.',
            database='example_dataset',
            port=3306,
            cursorclass=pymysql.cursors.DictCursor)
        print('欧吼～自己建立的mysql连接成功！！！')
        print()

    except Exception as e:
        print(f'自己建立的mysql连接失败, 错误详情: {str(e)}')
        exit()

    # 执行SQL查询
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
            
            data = result[:3]   # 取前3条数据测试
            # 逐个写入数据
            with open(saved_file_path, 'a') as file:
                for item in data:
                    # 把每个数据项写为单独的JSON对象
                    json.dump(item, file)
                    # 写入换行符，用于分隔每个JSON对象
                    file.write('\n')

    except Exception as e:
        print(f'SQL查询失败, 错误详情: {str(e)}')

    finally:
        print('SQL操作结束，数据库正常关闭。')
        connection.close()

# SQL查询语句
sql_query_statement = """
    SELECT id, advisorId, function_point, action, DATE_FORMAT(create_time, '%Y-%m-%d %H:%i:%s') as create_time
    FROM access_log
    WHERE create_time >= '2023-07-24 00:00:00' AND create_time < '2023-07-25 00:00:00';
"""
# 保存的文件路径
saved_file_path = 'download_mysql_data.json' # 存到当前目录下；
# 主程序
main(sql_query_statement, saved_file_path)
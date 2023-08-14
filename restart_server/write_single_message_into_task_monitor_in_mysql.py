import pymysql.cursors
from datetime import datetime
import argparse

# 进行命令行参数解析
parser = argparse.ArgumentParser(description='参数设定')
parser.add_argument('-t','--task_status',type=str,help='请传入task_status的值。')
args = parser.parse_args()

# 获取当前时间，并格式化
formatted_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

################################################################################
# 注意：task_status 字段为集合，必须选择 ('成功', '失败') 其中一项进行写入。
################################################################################

# 数据准备
task = {
    "description": "将metadata数据存入redis",
    "command": "python metadata_output.py",
    "status": args.task_status,
    "execution_time": formatted_time,
    "log_path": "/data/peilongchencc/nlp/tools/marking_data_output/get_redis_data.log"
    }

try:
    print('开始尝试连接mysql----')
    tmp_connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Flameaway3.',
                                     database='irmdata',
                                     port=3306,
                                     cursorclass=pymysql.cursors.DictCursor)
    print('欧吼～mysql连接成功！！！')

    # 创建一个新的cursor对象
    with tmp_connection.cursor() as cursor:
        # 插入数据
        sql = """
        INSERT INTO task_monitor (task_description, task_command, task_status, task_execution_time, log_path) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (task["description"], task["command"], task["status"], task["execution_time"], task["log_path"]))
        # 提交更改
        tmp_connection.commit()
    print('SQL命令执行成功~')

except Exception as e:
    print(f'插入数据失败: {e}')

finally:
    # 关闭连接
    tmp_connection.close()

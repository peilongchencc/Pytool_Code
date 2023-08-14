import pymysql.cursors

################################################################################
# 注意：task_status 字段为集合，必须选择 ('成功', '失败') 其中一项进行写入。
################################################################################

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
    tmp_connection.commit()
    print('SQL命令执行成功~')

except Exception as e:
    print(f'mysql连接或创建表失败: {e}')

finally:
    # 关闭连接
    tmp_connection.close()

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
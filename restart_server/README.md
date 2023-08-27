# Restart Server

## 项目描述：
设置定时任务，利用 Redis 每周一凌晨2点定时读取数据，如果 Redis 数据获取成功，向 mysql 中的 task_monitor 表写入成功信息。Redis 数据获取失败时，重启3次，如果连续3次重启都失败，向 mysql 中的 task_monitor 表写入失败信息，同时向企业微信个人账号发送报警消息。<br>
> 项目前提：将数据存入redis，设置过期时间为 "7天+1小时"。

## 个人配置：
系统：Ubuntu 18.04<br>
python 版本：Python 3.10.11<br>

## Redis 配置：
```python
host='localhost',               # 更改为你的 Redis 对应的ip，如果你也是本地，可以使用 localhost；
port = 6379,                    # # 默认，不需要更改；
```

## mysql配置:
```python
host='localhost',               # 更改为你的mysql对应的ip，如果你也是本地，可以使用 localhost；
user='root',                    # 账号名；
password='Flameaway3.',         # 密码；
database='irmdata',             # 数据库名称，根据你自己的需要更改；
port=3306,                      # 默认，不需要更改；
```

## 执行方式：
`crontab -e` 进入 crontab ，输入如下内容：
```shell
# 每周一凌晨2点更新 Redis 数据；
0 2 * * 1 /your_script_path/restart_get_redis.sh >> /your_log_path/get_redis_data.log  2>>/your_errorlog_path/crontab_error.log
```

这段代码用于定时执行一段Python代码，并将输出结果和错误信息保存到日志文件中。<br>
逐行解释下这段代码的含义：<br>
1. `0 2 * * 1` 表示每周一凌晨2点执行一次任务。
2. `/your_script_path/restart_get_redis.sh`：这是要执行的shell脚本。
4. `>> /your_log_path/get_redis_data.log`：这是将脚本的输出结果追加到指定的文件中。>>表示追加，如果文件不存在则会创建一个新文件。
5. `2>>/your_errorlog_path/crontab_error.log`：这是将脚本的错误信息追加到指定的文件中。2>>表示将标准错误输出重定向到文件中。
所以，这段代码的作用是每周一凌晨2点执行一次指定的shell脚本，并将输出结果追加到 `/your_log_path/get_redis_data.log` 文件中，同时将错误信息追加到 `/your_errorlog_path/crontab_error.log` 文件中。
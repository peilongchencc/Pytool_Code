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
# Pytool_Code
本项目记录常用的python工具型代码，方便在各种项目中调用。<br>

## 个人配置：
系统：Ubuntu 18.04<br>
python 版本：Python 3.10.11<br>

## crontab：
crontab是一个用于在Linux和Unix系统中定期执行任务的命令。它允许你按照特定的时间和日期计划执行脚本、命令或程序。<br>
crontab 文件夹内含 crontab 基础教程和常用的定时任务指令。<br>

## restart_server:
设置定时任务，利用 Redis 每周一凌晨2点定时读取数据，如果 Redis 数据获取成功，向 mysql 中的 task_monitor 表写入成功信息。Redis 数据获取失败时，重启3次，如果连续3次重启都失败，向 mysql 中的 task_monitor 表写入失败信息，同时向企业微信个人账号发送报警消息。<br>

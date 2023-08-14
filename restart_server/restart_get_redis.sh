#!/bin/bash

# 激活conda脚本，需要改为你自己的conda脚本；
source /root/anaconda3/etc/profile.d/conda.sh

# 激活conda虚拟环境
conda activate your_virtual_environment_name

counter=0

echo -e "开始尝试获取redis数据\n"
while [ $counter -lt 4 ]; do                                            # 检查 counter 的值是否小于 4
    python /your_script_path/get_redis_data.py >> /your_log_path/get_redis_data.log                      # 运行的文件如果不在当前目录下，要写成路径；get_redis_data.py运行成功不会有输出项，如果失败会将内容追加到get_redis_data.log文件中；
    if [ $? -eq 0 ]; then                                               # 如果命令执行成功
        # 向mysql写入成功信息；
        python /your_file_path/write_single_message_into_task_monitor_in_mysql.py --task_status="成功" >> /your_log_path/get_redis_data.log     # 注意：task_status 字段为集合，必须选择 ('成功', '失败') 其中一项进行写入。
        echo "已成功向 mysql-irmdata-task_monitor写入数据。"
        exit 0                                                          # 退出shell脚本，不再执行下方所有命令。
    else
        let counter++
        if [ $counter -lt 4 ]; then
            echo -e "服务启动失败, 即将进行第 $counter 次重启尝试。\n"        # 输出失败提示，-e 参数是为了让 echo 命令正确解释 "\n"。
            sleep 5                                                     # 等待5秒
        fi
    fi
done

if [ $counter -eq 4 ]; then                                             # 检查 counter 的值是否为 4
    # 向mysql写入成功信息；
    python /your_file_path/write_single_message_into_task_monitor_in_mysql.py --task_status="失败" >> /your_log_path/get_redis_data.log
    python /your_file_path/send_alarm_2_wechat.py                                       # 向企业微信发送报警信息
fi

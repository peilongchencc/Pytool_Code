import requests
import json
from datetime import datetime

def send_order_error_message(content, phone_num_list):
    web_hook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxx"  # xxxxxx 是你自己的key；
                                                                                # 微信提供了很多种形式的接口，自己选择一种适合自己的就好；
    # 为content注明事件发生的事件
    content += f"发生时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    # 发送的 "消息主体"
    body = {
        "msgtype": "text",
        "text": {
            "content": content,
            "mentioned_mobile_list": phone_num_list    # 填写信息接收人手机号。
        }
    }
    
    # 消息头
    headers = {
        "Content-Type": "application/json;charset=utf-8"
    }
    
    # 创建post请求
    response = requests.post(web_hook, data=json.dumps(body), headers=headers)
    
    # 检查post连接状态
    if response.status_code == 200:
        print('消息发送成功')
        print(f'返回的状态信息为:{response.text}\nerrcode表示\"返回码\",0表示正常。errmsg:表示对返回码的文本描述内容。')
    else:
        print('消息发送失败')

content = "报警信息提醒：\ntools文件夹下Redis数据刷新失败\n"         # 企业微信显示的错误信息，数据类型:String。
phone_num_list = ["156..."]                  # 如果要通知多个人，将手机号采用英文逗号间隔即可，例如 ["138...","133...","133..."]。
# 调用示例
send_order_error_message(content, phone_num_list)
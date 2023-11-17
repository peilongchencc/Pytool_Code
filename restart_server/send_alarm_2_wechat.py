import argparse
import requests
import json
from datetime import datetime

def arg_parse():
    """获取终端传参
    Args:
        依靠终端传入
    Return:
        args:参数类, 通过 '.xxx' 的方式调用对应参数
    Example:
        终端的输入请参考:
        ```bash
        python xxx.py --content="错误信息" --phone_num_list="156...,186..."
        ```
    """
    parser = argparse.ArgumentParser(description='参数设定')
    parser.add_argument('-c','--content',type=str,help='请传入待通知信息')
    parser.add_argument('-p','--phone_num_list',type=str,help='请传入待通知人手机号,用逗号分隔多个手机号')
    args = parser.parse_args()
    return args

def send_order_error_message(content, phone_num):
    """通过手机号在企业微信群中@某人发送消息
    Args:
        content(str): 信息
        pyhone(str): 手机号,用逗号分隔多个手机号, 例如: "156...,186..."
    Return:
        无返回值,执行发送信息操作
    """

    # 将手机号转为list形式
    phone_num_list = phone_num.split(',')
    
    web_hook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e210dc0a-4346-40dc-a415-6a37e822xxx"  
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

if __name__ == "__main__":
    # 获取终端传参
    args = arg_parse()
    # 调用示例
    content = args.content                  # 企业微信显示的错误信息, 例如:content="报警信息提醒：\nzip失败，请检查日志以查找问题。\n"         
    phone_num_list = args.phone_num_list    # 如果要通知多个人，将手机号采用英文逗号间隔即可，例如 "156...,186..."
    send_order_error_message(content, phone_num_list)  
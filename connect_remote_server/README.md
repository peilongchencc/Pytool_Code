# connect_remote_server
记载 vscode 连接阿里云远程服务器的一些经验，包括如何连接远程服务器，出现的错误和相应的解决方案。<br>

## 进入实例：
进入个人阿里云主界面后点击相应实例名，然后点击控制台即可进入自己选择的实例～<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/1f4715ed-7157-453c-84f8-d20a61600dbb)

## workbench连接阿里云服务器：
可以通过密码连接阿里云服务器，也可以通过密钥连接阿里云服务器，这里先介绍一下通过密码连接阿里云服务器。<br>
1. 点击远程连接
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/3dc2c8bb-ea73-493f-b833-22613a26cd37)

2. 现在，你应该能看到以下界面，点击"立即登录"即可

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/61e0dc5f-cc77-43a3-b911-8812c7f5b59e)

3. 选择"密码认证"，然后输入个人用户名和密码，点击"确认"

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/a27ea891-09c3-4072-90de-af2acfd20c9b)

现在，你应该已经进入了阿里云服务器界面了。但我不得不提醒你，通过这种方式操作很不方便，且相应速度很慢，最好的方式还是通过IDE或终端的方式连接阿里云服务器，简洁、速度快🚀🚀🚀<br>

## 通过ssh密钥连接--创建密钥对：

### 重置实例密码：(可选)
如果你忘记了自己阿里云服务器的密码，可以通过实例的主界面点击 `重置实例密码` 重新设置密码，可以参考以下图片：<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/dcc47e26-439d-45e8-a2ab-3f244b08a780)

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/e399da7d-93f4-4e4f-8170-b603d8777cac)




## Could not establish connection to "xxx.xxx.xxx.xxx": Cannot read properties of undefined (reading 'replace').
情况描述：使用终端连接远程服务器正常，但使用 vscode 连接远程服务器时，出现错误提示:
```txt
Could not establish connection to "xxx.xxx.xxx.xxx": Cannot read properties of undefined (reading 'replace').
```
解决方案：
1. 点击 vscode 中的拓展模块；
2. 点击远程连接的插件，我使用的是 Remote Explorer；
3. 将 Remote 版本切换为 "预发布" 版本；("预览"-->"预发布")

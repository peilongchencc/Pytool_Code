# connect_remote_server
记载 vscode 连接阿里云远程服务器的一些经验，包括如何连接远程服务器，出现的错误和相应的解决方案。<br>


## Could not establish connection to "xxx.xxx.xxx.xxx": Cannot read properties of undefined (reading 'replace').
情况描述：使用终端连接远程服务器正常，但使用 vscode 连接远程服务器时，出现错误提示:
```txt
Could not establish connection to "xxx.xxx.xxx.xxx": Cannot read properties of undefined (reading 'replace').
```
解决方案：
1. 点击 vscode 中的拓展模块；
2. 点击远程连接的插件，我使用的是 Remote Explorer；
3. 将 Remote 版本切换为 "预发布" 版本；("预览"-->"预发布")
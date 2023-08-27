# MySQL
## 安装mysql：
1. 更新系统软件包信息：
```shell
apt update
```

2. 安装MySQL服务器：
```shell
apt install mysql-server
```

## mysql常用指令(开启、关闭、重启、状态指令)：
- 关闭mysql服务
```shell
service mysql stop
```
- 查看mysql状态
```shell
service mysql status
```
- 启动mysql服务
```shell
service mysql start
```
- 重启mysql服务
```shell
service mysql restart
```
- 查看端口开放情况和端口对应的pid(查看的是系统监听的所有的端口)
```shell
netstat -ntlp 
```

## 查看mysql配置信息：
安装mysql后mysql配置的文件路径为：
```shell
cat /etc/mysql/mysql.conf.d/mysqld.cnf
```

由输出信息可以看到数据库中数据的保存位置；
[图片]

## mysql密码设置：--root账号
输入以下命令以连接到MySQL服务器：
```shell
sudo mysql -u root    
```
> 因安装时没有要求输入密码，所以此时会直接登录mysql。


在MySQL提示符下，执行以下命令来设置密码：
```shell
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_password';
```
请将 `'new_password'` 替换为你想要设置的新密码，假设我要将密码设置为 `Flameaway3.`，操作如下：<br>
```shell
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Flameaway3.';
```

更新系统权限表：
```shell
FLUSH PRIVILEGES;
```
退出MySQL提示符：
```shell
exit;
```
使用 -p 指令登录：
mysql -u root -p
[图片]

## 使用 navicat 远程连接 mysql ：
事件描述：
我在我的服务器上安装了mysql，我的服务器公网ip为 8.140.203.136 ，我的账号为 root ，密码为 Flameaway3. ，我如何在另一台电脑上通过navicat连接到这个mysql呢？

1. 进入安全组：
[图片]

2. 开通3306端口：
注意，如果是常规的 sanic 或 flask 起的服务，只需要进行到这里即可。
[图片]

3. 修改 mysql 配置信息中的bind-address:
bind-address=127.0.0.1 表示 MySQL服务对127.0.0.1地址进行监听，禁止外部远程连接。

需要在mysql配置文件中找到bind-address行，并将其注释掉或修改为： bind-address = 0.0.0.0
cat /etc/mysql/mysql.conf.d/mysqld.cnf    # 安装mysql后的默认路径；mysql配置文件路径；
 
我采用的方式是注释 bind-address行，注释后保存、退出。

4. 设置root的远程访问权限：
依次运行如下指令即可：
mysql -u root -p    # 输入密码进行登录；
use mysql;          # 调用mysql数据库；
select host from user where user = 'root';    # 查看root账号的host；
update user set host = '%' where user = 'root';    # 将root账号的host修改为 '%'，允许外部访问；
[图片]

重新启动 mysql 并查看3306端口的监听地址：
# 重启mysql服务
service mysql restart
[图片]
可以看到，端口已修改；

navicat测试连接：
[图片]

创建自己需要的数据库：

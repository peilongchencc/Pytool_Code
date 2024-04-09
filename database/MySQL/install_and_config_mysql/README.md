# install and config mysql

本章介绍安装和配置mysql，并实现本地(Navicat)连接远程服务器的mysql。<br>
- [install and config mysql](#install-and-config-mysql)
  - [服务器安装MySQL数据库：](#服务器安装mysql数据库)
  - [终端MySQL常用指令(开启、关闭、重启、状态指令)：](#终端mysql常用指令开启关闭重启状态指令)
  - [查看MySQL配置信息：](#查看mysql配置信息)
  - [MySQL密码设置：(root账号)](#mysql密码设置root账号)
  - [本地使用 Navicat 远程连接 MySQL ：](#本地使用-navicat-远程连接-mysql-)

## 服务器安装MySQL数据库：

MySQL数据库的安装非常简单～<br>

1. 更新系统软件包信息：
```shell
apt update
```

2. 安装MySQL服务器：
```shell
apt install mysql-server
```

## 终端MySQL常用指令(开启、关闭、重启、状态指令)：

MySQL数据库安装后，首先我们要熟悉下MySQL数据库的常用指令。注意⚠️⚠️⚠️：以下指令均在终端使用，而不是在终端进入MySQL服务器后使用。<br>

- 关闭MySQL服务

```shell
service mysql stop
```

- 查看MySQLl状态

```shell
service mysql status
```

- 启动MySQL服务

```shell
service mysql start
```

- 重启MySQL服务

```shell
service mysql restart
```

- 查看端口开放情况和端口对应的pid(查看的是系统监听的所有的端口，MySQL默认开始3306端口，自己注意下是否有开放即可。)

```shell
netstat -ntlp 
```

## 查看MySQL配置信息：

安装MySQL后，可以在终端使用以下指令查看MySQL的具体信息：

```shell
cat /etc/mysql/mysql.conf.d/mysqld.cnf
```

> `/etc/mysql/mysql.conf.d/mysqld.cnf`为MySQL默认的配置文件路径。

由输出信息可以看到MySQl数据库中数据的保存位置；<br>

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/177d581a-3a62-49f2-a05d-af584bff29eb)


## MySQL密码设置：(root账号)

1. 输入以下命令以连接到MySQL服务器：

```shell
sudo mysql -u root    
```

> 因安装时没有要求输入密码，所以此时会直接登录mysql。

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/3130258c-cc03-4030-9651-b0c13f16105d)


2. 在MySQL提示符下，执行以下命令来设置密码：

```shell
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_password';
```

请将 `'new_password'` 替换为你想要设置的新密码，假设我要将密码设置为 `Flameaway3.`，操作如下：<br>

```shell
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Flameaway3.';
```

3. 更新系统权限表：

```shell
FLUSH PRIVILEGES;
```

4. 退出MySQL提示符：

```shell
exit;
```

5. 使用 -p 指令登录：

```shell
mysql -u root -p
```

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/0ac8f06f-97af-4827-9553-535573bc6997)
<br>
<br>

## 本地使用 Navicat 远程连接 MySQL ：

**事件描述**: 我在阿里云服务器上安装了MySQL，我的服务器公网ip为 `8.140.203.xxx` ，我的账号为 `root` ，密码为 `Flameaway3.` ，我如何在本地通过navicat连接到这个MySQL呢？<br>

1. 进入安全组：

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/0d4ee2bc-3bd0-4d27-8b02-eb99797b040c)
<br>

2. 开通3306端口：

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/90199b3e-de4d-457d-ad90-67b7ef6d61e0)
<br>

3. 修改 mysql 配置信息中的bind-address:

`bind-address=127.0.0.1` 表示 MySQL服务对 `127.0.0.1` 地址进行监听，禁止外部远程连接。<br>

需要在mysql配置文件中找到 `bind-address` 行，并将其注释掉或修改为： `bind-address = 0.0.0.0`:<br>

```shell
cat /etc/mysql/mysql.conf.d/mysqld.cnf
``` 

🚀🚀🚀我采用的方式是注释 bind-address行，注释后保存、退出。<br>
<br>

4. 设置root的远程访问权限：

终端连接到MySQL服务器，然后依次运行以下指令即可：<br>

```shell
mysql -u root -p    # 输入密码进行登录；
use mysql;          # 查看mysql数据库；
select host from user where user = 'root';    # 查看root账号的host；
update user set host = '%' where user = 'root';    # 将root账号的host修改为 '%'，允许外部访问；
exit; # 退出 mysql 客户端；
```

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/2e9bc409-f375-408d-9af5-431da62115f1)


5. 重新启动 mysql 并查看3306端口的监听地址：<br>

输入以下命令重启mysql数据库：<br>

```shell
service mysql restart
```

查看端口开放情况和端口对应的pid(也可以使用`netstat -tuln`，后来笔者感觉`netstat -ntlp `指令更方便点。)<br>

```shell
netstat -ntlp 
```

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/4d24c9aa-f7ba-4b1a-9c9a-4c8021b4ea75)

可以看到，端口的状态已经修改~🥴🥴🥴<br>

6. 使用 Navicat 测试是否可以连接到远程的MySQL：

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/cd8936d6-eca9-42a1-806f-845ecf5694b1)

成功连接！现在就可以利用 Navicat 操作 MySQL 数据库了。<br>

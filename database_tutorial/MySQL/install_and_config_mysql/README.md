# install and config mysql

本章介绍安装和配置mysql，并实现本地(Navicat)连接远程服务器的mysql。<br>
- [install and config mysql](#install-and-config-mysql)
  - [服务器安装MySQL数据库：](#服务器安装mysql数据库)
  - [终端MySQL常用指令(开启、关闭、重启、状态指令)：](#终端mysql常用指令开启关闭重启状态指令)
  - [查看MySQL配置信息：](#查看mysql配置信息)
  - [MySQL密码设置：(root账号)](#mysql密码设置root账号)
  - [如果密码设置好了，但无法登录mysql，信息如下:](#如果密码设置好了但无法登录mysql信息如下)
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

## 如果密码设置好了，但无法登录mysql，信息如下:

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/vanna# mysql -u root -p
Enter password: 
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/vanna# cat /etc/mysql/mysql.conf.d/mysqld.cnf
#
# The MySQL database server configuration file.
#
# One can use all long options that the program supports.
# Run program with --help to get a list of available options and with
# --print-defaults to see which it would actually understand and use.
#
# For explanations see
# http://dev.mysql.com/doc/mysql/en/server-system-variables.html

# Here is entries for some specific programs
# The following values assume you have at least 32M ram

[mysqld]
#
# * Basic Settings
#
user            = mysql
# pid-file      = /var/run/mysqld/mysqld.pid
socket  = /var/run/mysqld/mysqld.sock
# port          = 3306
# datadir       = /var/lib/mysql


# If MySQL is running as a replication slave, this should be
# changed. Ref https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmpdir
# tmpdir                = /tmp
#
# Instead of skip-networking the default is now to listen only on
# localhost which is more compatible and is not less secure.
#bind-address           = 127.0.0.1
#mysqlx-bind-address    = 127.0.0.1
#
# * Fine Tuning
#
key_buffer_size         = 16M
# max_allowed_packet    = 64M
# thread_stack          = 256K

# thread_cache_size       = -1

# This replaces the startup script and checks MyISAM tables if needed
# the first time they are touched
myisam-recover-options  = BACKUP

# max_connections        = 151

# table_open_cache       = 4000

#
# * Logging and Replication
#
# Both location gets rotated by the cronjob.
#
# Log all queries
# Be aware that this log type is a performance killer.
# general_log_file        = /var/log/mysql/query.log
# general_log             = 1
#
# Error log - should be very few entries.
#
log_error = /var/log/mysql/error.log
#
# Here you can see queries with especially long duration
# slow_query_log                = 1
# slow_query_log_file   = /var/log/mysql/mysql-slow.log
# long_query_time = 2
# log-queries-not-using-indexes
#
# The following can be used as easy to replay backup logs or for replication.
# note: if you are setting up a replication slave, see README.Debian about
#       other settings you may need to change.
# server-id             = 1
# log_bin                       = /var/log/mysql/mysql-bin.log
# binlog_expire_logs_seconds    = 2592000
max_binlog_size   = 100M
# binlog_do_db          = include_database_name
# binlog_ignore_db      = include_database_name
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/vanna#
```

错误信息提示“无法通过socket '/tmp/mysql.sock' 连接到本地MySQL服务器”，这通常意味着MySQL服务没有运行，或者配置文件中的socket路径不正确。如果MySQL服务器正在运行，可以确认配置文件的socket路径:<br>

**确认配置文件的socket路径**：<br>

你的配置文件指定了socket文件的路径为`/var/run/mysqld/mysqld.sock`，而你的错误信息显示尝试连接到`/tmp/mysql.sock`。你需要确保客户端使用的socket路径与服务器配置中的一致。可以在启动MySQL客户端时明确指定socket路径：<br>

```bash
mysql -u root -p --socket=/var/run/mysqld/mysqld.sock
```

此时输入密码大概率就可以登录了，示例如下:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/vanna# mysql -u root -p --socket=/var/run/mysqld/mysqld.sock
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.36-0ubuntu0.22.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> exit;
Bye
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/vanna# mysql -u root -p
Enter password: 
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/vanna# 
```

如果想要 **永久设置默认的Socket路径** 可以使用以下方法:<br>

修改你的 `~/.my.cnf` 配置文件（如果文件不存在则创建），为MySQL客户端设置默认的socket路径。添加以下内容：<br>

```bash
[client]
socket=/var/run/mysqld/mysqld.sock
```

这样，每次使用MySQL客户端时，都会自动使用这个socket路径。<br>

你可以使用以下命令来检查文件的内容确保配置是正确的：<br>

```bash
cat ~/.my.cnf
```

这应该会显示：<br>

```bash
[client]
socket=/var/run/mysqld/mysqld.sock
```

如果一切设置正确，现在你应该能够直接通过`mysql -u root -p`命令连接到MySQL服务器，而不会再出现之前的错误。<br>

之前是通过`cat /etc/mysql/mysql.conf.d/mysqld.cnf`这样看mysql信息的，按你这样改冲突吗？<br>

不会冲突。你通过`cat /etc/mysql/mysql.conf.d/mysqld.cnf`查看的配置文件主要是用于配置MySQL服务器端的设置，而`~/.my.cnf`文件中的配置是用于客户端的设置。这两个文件的作用是分开的：<br>

1. **服务器端配置（`mysqld.cnf`）**：

这个文件中的设置影响MySQL服务器的行为，比如它的数据存储位置、端口、最大连接数、日志文件位置等。这里面的`socket`配置指定了服务器监听的本地socket文件路径，这是服务器端特有的配置。<br>

2. **客户端配置（`.my.cnf`）**：

在`~/.my.cnf`中的配置主要影响MySQL客户端的行为，比如连接MySQL时使用的用户名、密码、默认使用的数据库、socket路径等。这里的`socket`配置告诉MySQL客户端默认连接到哪个socket文件。<br>

通过将`socket=/var/run/mysqld/mysqld.sock`添加到你的`~/.my.cnf`文件的`[client]`部分，你实际上是在告诉MySQL客户端默认使用哪个socket文件来连接服务器，这并不会影响服务器本身的配置。<br>

因此，这两者之间是不会冲突的，而是各自作用于不同的方面——一个是服务器端，一个是客户端。这样的设置是推荐的做法，可以帮助确保客户端和服务器之间的连接配置正确无误。<br>


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

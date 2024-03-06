# 源码编译，安装python3.10.11：(全局安装，不会只在虚拟环境安装)

因代码中使用的是 python 3.10 的语法，但阿里云自带的 python 版本只有 python 2.7 和 python 3.8，且不允许通过 conda 的方式安装，所以此处采用源码编译的方式安装。<br>

🚨🚨🚨注意：源码编译安装 python 非常容易出错，出错需要重复安装，注意一定要按照流程！<br>

以下指令都在终端运行，且需要在root账号使用。<br>

> 注意：pip install python 这个指令是错误的，pip 只能安装python的依赖，不能安装python。

1. 进入/usr/local目录：

```bash
cd /usr/local
```

2. 下载 python3.10.11 源代码包：

```bash
wget https://www.python.org/ftp/python/3.10.11/Python-3.10.11.tgz
```

3. 解压Python源代码包：：

```bash
tar -xf Python-3.10.11.tgz
```

4. 进入解压后的目录：

```bash
cd Python-3.10.11
```

5. 使系统获取最新的各种包的信息：

> 如果后期发现自己编译的python忘记了某个库，直接从这一步开始操作即可。但一定要注意将目录切换到python安装目录。‼️
> 在编译的python中添加了python模块，已有的虚拟环境可以直接使用。✅

```bash
sudo apt update
```

6. 配置安装选项：

终端分别运行以下代码，避免丢失模块；<br>

```bash
# 常见项
sudo apt install libssl-dev
sudo apt-get install libffi-dev
# 可选项
sudo apt-get install libsqlite3-dev     # 安装 SQLite3 开发库，避免 `_sqlite3` 模块导入错误
sudo apt-get install libbz2-dev
sudo apt-get install liblzma-dev
./configure --prefix=/usr/local --with-zlib --with-ssl   # 依旧是终端输入；
                                                         # 等待时间漫长；
```

7. 编译源代码：

```bash
make
```

8. 安装python：

```bash
sudo make install
```

9. 查看python路径：--whereis python

![](./where_is_python.jpg)

10. 建立软链接：(软链接并不会写入某个文件，只是一种形式)

使用如下指令实现：<br>

```bash
sudo ln -s /usr/local/bin/python3.10 /usr/local/bin/python
```

11. 查看效果：

```bash
python -V
```

![](./python_version.jpg)

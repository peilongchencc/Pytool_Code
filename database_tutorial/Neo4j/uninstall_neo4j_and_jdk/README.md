# uninstall_neo4j_and_jdk

本章介绍Neo4j和JDK的卸载。<br>
- [uninstall\_neo4j\_and\_jdk](#uninstall_neo4j_and_jdk)
  - [卸载Neo4j：](#卸载neo4j)
  - [为不同用户设置不同JDK：](#为不同用户设置不同jdk)
  - [卸载JDK：](#卸载jdk)

## 卸载Neo4j：

如果你是按照我的方式(安装包)安装的Neo4j，卸载非常简单，只需要2步：<br>

1. 删除`/opt`路径下的Neo4j文件;
2. 删除`~/.bashrc`文件中NEO4J_HOME的环境变量即可；


如果你是通过其他方式安装的Neo4j，要完全卸载 Neo4j 数据库，你可以按照以下步骤进行操作：<br>

1. **停止 Neo4j 服务**：

在终端中运行以下命令，以确保 Neo4j 服务器已停止运行：<br>

```bash
sudo service neo4j stop
```

2. **卸载 Neo4j 软件包**：

使用以下命令卸载 Neo4j 软件包：<br>

```bash
sudo apt-get remove neo4j
```

3. **删除配置文件和数据**：

删除 Neo4j 的配置文件和数据目录，以确保所有数据都被清除。默认情况下，这些文件位于 `/etc/neo4j/` 和 `/var/lib/neo4j/` 目录中。你可以使用以下命令删除这些目录：<br>

```bash
sudo rm -rf /etc/neo4j/
sudo rm -rf /var/lib/neo4j/
```

4. **删除 Neo4j 用户和组**：

Neo4j 安装通常会创建一个系统用户和组。你可以使用以下命令删除它们：<br>

```bash
sudo userdel neo4j
sudo groupdel neo4j
```

5. **清除其他残留文件**：

你可能还需要检查其他可能残留的配置文件或日志文件，并删除它们。<br>

6. **卸载 Java**（可选）：

如果你的系统上安装了 Neo4j 之前的 Java 版本，你可以选择卸载它们，或者保留它们，具体取决于你的需求。<br>

完成上述步骤后，Neo4j 就会被完全卸载并清除了与其相关的文件和配置。请务必小心操作，并确保备份任何重要数据，因为这些步骤将永久删除与 Neo4j 相关的所有内容。<br>


## 为不同用户设置不同JDK：

不同用户可以设置不同的JDK版本，例如：root用户使用JDK 11，普通用户使用JDK 8。具体的操作如下：<br>

1. **配置默认 Java 版本**。假设你想要配置root用户默认使用的JDK版本为11。使用以下命令查看系统上所有的 Java 版本：

```bash
sudo update-alternatives --config java
```

在出现的列表中，选择 Java 11（它应该有一个编号，`*`开头的是当前所用的Java版本）。按照指示输入相应的数字(类似0，1，2)，然后按 Enter。<br>

2. **配置默认 Javac 版本**（这是 Java 的编译器）。与配置 Java 命令类似：

```bash
sudo update-alternatives --config javac
```

再次在列表中选择 Java 11。<br>

3. **设置 `JAVA_HOME` 环境变量**。编辑 `/root/.bashrc`或`/etc/profile` 文件：

> 在`.bashrc`中设置环境变量是一种很好的习惯，无论你采用那种防止设置环境变量，一定要注意不要将你的环境变量写的太分散，否则后续想要修改非常麻烦。<br>
> 今天在`/root/.bashrc`中写环境变量，明天在`/etc/profile`中写环境变量，后天在`/etc/environment`中写环境变量，这种方式是非常不可取的。❌❌❌<br>


```bash
vim /root/.bashrc
```

在文件的末尾添加以下行：<br>

```
JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
```

然后保存并关闭文件。<br>

为了让这个变更生效，需要使用以下命令：<br>

```bash
source /root/.bashrc
```

如果你修改的是`/etc/profile`文件，生效指令类似：<br>

```bash
source /etc/profile
```

## 卸载JDK：

假设你的系统中有多个jdk，你想要删除 `java-1.8.0-openjdk-amd64`，可以参考如下方式：<br>

1. 终端输入以下指令查看jdk信息：<br>

```bash
update-java-alternatives --list
```

由下图可知，你的系统中同时存在jdk8和jdk11。<br>

```log
java-1.11.0-openjdk-amd64      1111       /usr/lib/jvm/java-1.11.0-openjdk-amd64
java-1.8.0-openjdk-amd64       1081       /usr/lib/jvm/java-1.8.0-openjdk-amd64
```

2. 使用`apt-get`卸载Java 8的OpenJDK包。执行以下命令：

```bash
sudo apt-get purge openjdk-8-jre openjdk-8-jre-headless openjdk-8-jdk openjdk-8-jdk-headless
```

3. 删除任何相关的未使用的依赖包：

```bash
sudo apt-get autoremove
```

4. 更新软件包列表：

```bash
sudo apt-get update
```

5. 为了确保Java 8已完全从你的系统中删除，你可以检查`/usr/lib/jvm/`目录下的内容。执行以下命令：

```bash
ls /usr/lib/jvm/
```

确保`java-1.8.0-openjdk-amd64`目录不再存在。<br>

6. 你还可以再次运行`update-java-alternatives --list`命令来确保Java 8不再列出。

执行上述步骤后，Java 8的OpenJDK应该已从你的Ubuntu 18.04系统中完全删除。<br>

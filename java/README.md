## java

## 安装java:

Turns out java has been moved into brew core recently, so the correct command as of August 2022 is:<br>

> 现在通过brew安装java会自动安装javaJDK。

```bash
brew install java
```

Then check your installation by running<br>

```bash
java -version
```

If the result does not looks like this:<br>

```txt
openjdk 18.0.2 2022-07-19
OpenJDK Runtime Environment Homebrew (build 18.0.2+0)
OpenJDK 64-Bit Server VM Homebrew (build 18.0.2+0, mixed mode, sharing)
```

but like this:<br>

```txt
The operation couldn’t be completed. Unable to locate a Java Runtime.
Please visit http://www.java.com for information on installing Java.
```

Then you also need to create a symlink for the system Java wrappers to find this JDK:<br>

```bash
sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk \
     /Library/Java/JavaVirtualMachines/openjdk.jdk
```

![java安装](./java安装.jpg)


### Java环境变量配置:

运行以下指令查看本机java安装路径:<br>

```bash
/usr/libexec/java_home
```

![java_home_path](./java_home_path.jpg)

根据自己的shell类型，修改配置文件。假设你使用的`zsh`，运行以下指令:<br>

```bash
vim ~/.zshrc
```

在文件末尾添加以下指令:<br>

> 注意修改为你自己上一步查看到的java安装路径。

```bash
# 设置java环境变量
export JAVA_HOME="/opt/homebrew/Cellar/openjdk/21.0.1/libexec/openjdk.jdk/Contents/Home"
```

添加好后，关闭 `.zshrc` 文件，运行下列指令激活环境配置:<br>

```bash
source ~/.zshrc
```

运行下列指令检查java环境变量是否配置正确:<br>

> 最好重启终端后尝试。

```bash
echo $JAVA_HOME
```

这应该会显示你之前设置的路径。<br>


## 安装maven：

Java通常通过Maven或Gradle这样的构建工具来管理依赖项。这里介绍Maven安装第三方库的方式：<br>

```bash
brew install maven
```

### 测试Maven：

终端尝试运行以下指令检查java和maven的安装:<br>

```bash
mvn --version
```


我使用的mac，vscode帮我安装依赖的时候，提示以下信息：

```txt
Command failed: mvn --version
The JAVA_HOME environment variable is not defined correctly,
this environment variable is needed to run this program.
```

我在zsh界面运行`mvn --version`显示如下：

```txt
Apache Maven 3.9.6 (bc0240f3c744dd6b6ec2920b3cd08dcc295161ae)
Maven home: /opt/homebrew/Cellar/maven/3.9.6/libexec
Java version: 21.0.1, vendor: Homebrew, runtime: /opt/homebrew/Cellar/openjdk/21.0.1/libexec/openjdk.jdk/Contents/Home
Default locale: zh_CN_#Hans, platform encoding: UTF-8
OS name: "mac os x", version: "14.1.2", arch: "aarch64", family: "mac"
```

这是因为vscode运行的不是我的zsh环境吗？我应该怎样让vscode运行zsh环境呢？

### 使用Maven来管理依赖

1. **创建一个Maven项目**：
   - 在包含你的 `Demo.java` 的目录中，创建一个新文件，命名为 `pom.xml`。
   - 在 `pom.xml` 文件中，你需要定义项目的基础结构和依赖项。这个文件告诉Maven如何构建你的项目。

2. **在 `pom.xml` 中添加依赖**：
   你需要添加以下依赖项到你的 `pom.xml` 文件中：

   ```xml
   <dependencies>
       <!-- fastjson -->
       <dependency>
           <groupId>com.alibaba</groupId>
           <artifactId>fastjson</artifactId>
           <version>1.2.75</version> <!-- 请使用最新的版本号 -->
       </dependency>

       <!-- Aliyun SDK -->
       <dependency>
           <groupId>com.aliyun</groupId>
           <artifactId>aliyun-java-sdk-core</artifactId>
           <version>4.5.10</version> <!-- 请使用最新的版本号 -->
       </dependency>

       <!-- Apache Commons Codec -->
       <dependency>
           <groupId>commons-codec</groupId>
           <artifactId>commons-codec</artifactId>
           <version>1.15</version> <!-- 请使用最新的版本号 -->
       </dependency>
   </dependencies>
   ```

3. **构建项目**：
   在终端中，导航到包含 `pom.xml` 的目录，然后运行：
   ```bash
   mvn clean install
   ```

4. **运行Java程序**：
   在Maven成功构建项目后，你可以使用以下命令来运行你的程序：
   ```bash
   java -cp target/classes com.yourpackage.Demo
   ```
   请将 `com.yourpackage.Demo` 替换成你的 `Demo.java` 的实际包路径。

### 注意事项
- 确保你的 `Demo.java` 文件位于正确的目录结构中，这是Maven项目的要求。例如，如果你的包是 `com.yourpackage`，那么你的Java文件应该在 `src/main/java/com/yourpackage/` 目录下。
- 依赖的版本

号可能会随时间变化，请查找相应库的最新版本号。
- 由于代码中涉及到阿里云的服务，你需要确保已经有了有效的阿里云账号并且已经获取了相应的AK（Access Key）和SK（Secret Key）。

如果你不熟悉Maven的使用或者在使用过程中遇到任何困难，可以查阅Maven的官方文档或相关的Java开发资源。


## java

Turns out java has been moved into brew core recently, so the correct command as of August 2022 is:<br>

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

[java安装](./java安装.jpg)
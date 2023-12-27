# dotenv
`python-dotenv` 是一个用于管理环境变量的Python库。通过使用这个库，你可以从 `.env` 文件中加载环境变量，使得你可以在开发过程中轻松地切换配置而不必更改代码。这种方法也有助于保护敏感信息，如数据库凭据，使其不会被直接写入到代码中。<br>

- [dotenv](#dotenv)
  - [使用方法:](#使用方法)
    - [`.env.local` 文件中的内容:](#envlocal-文件中的内容)
    - [总结:](#总结)
  - [`.gitignore`忽略所有 `.env` 文件的方式:](#gitignore忽略所有-env-文件的方式)
    - [重要提示:](#重要提示)
  - [在Sanic或Flask中使用:](#在sanic或flask中使用)
    - [步骤概述:](#步骤概述)
    - [注意事项:](#注意事项)
  - [`.env`文件中数据的格式:](#env文件中数据的格式)


## 使用方法:

1. **安装**: 通过运行下列代码来安装这个库。

```bash
pip install python-dotenv
```

2. **创建 `.env.local` 文件**: 

通常，环境变量文件命名为 `.env`，但你可以命名为 `.env.local` 或其他名称。在这个文件中，你可以**定义键值对**，如数据库连接信息和其他配置项。<br>

对于不同的开发阶段（本地测试，线上测试，和正式发布），你可以为每个环境创建不同的`.env`文件。这样，你可以为每个环境指定不同的配置，而不会相互干扰。以下是一些建议的文件名和它们的用途:<br>

**本地测试**:<br>

- 文件名: `.env.local` 或 `.env.development`
- 用途: 用于本地开发和测试。通常包含数据库的本地路径，日志级别为debug等。

**线上测试**:<br>

- 文件名: `.env.test` 或 `.env.staging`
- 用途: 用于模拟生产环境的测试环境。通常包含指向测试数据库的路径，可能的错误跟踪服务，日志级别可能是info。

**正式发布**:<br>

- 文件名: `.env.production`
- 用途: 用于实际的生产环境。包含实际的API密钥，数据库凭证，日志级别可能是warning或error。

3. **加载 `.env.local` 文件**: 在你的Python脚本或应用的入口点，使用以下代码加载环境变量：

```python
from dotenv import load_dotenv
load_dotenv('.env.local')  # 或者使用 load_dotenv() 来加载默认的 '.env' 文件
```

### `.env.local` 文件中的内容:

在你的 `.env.local` 文件中，你可以定义需要的环境变量。如果你想要配置MySQL数据库连接，你可能需要定义以下变量：<br>

```plaintext
DB_HOST=localhost
DB_USER=myuser
DB_PASS=mypassword
DB_NAME=mydatabase
```

这些变量之后可以在你的Python代码中通过 `os.getenv` 方法来获取，例如：<br>

```python
import os

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')
```

假设你没有加载 `.env.local` 文件，使用下列代码，直接使用 `os` 调用环境变量中的配置，终端将显示:<br>

```python
import os

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')

print(f"mysql的配置信息为:\n主机:{db_host}, 用户:{db_user}")
```

```txt
mysql的配置信息为:
主机:None, 用户:None
```

以 `.env.local` 文件中的内容为例，如果你加载了 `.env.local` 文件，使用 `os` 调用环境变量中的配置，终端将显示:<br>

```python
import os
from dotenv import load_dotenv

load_dotenv('.env.local')  # 或者使用 load_dotenv() 来加载默认的 '.env' 文件

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')

print(f"mysql的配置信息为:\n主机:{db_host}, 用户:{db_user}")
```

```txt
mysql的配置信息为:
主机:localhost, 用户:myuser
```

### 总结:

- **安全性**: 不要将 `.env.local` 文件提交到你的代码仓库中，特别是如果它包含敏感信息。通常，你应该将 `.env` 文件添加到 `.gitignore` 中以避免意外提交。

- **灵活性**: 你可以根据需要在 `.env.local` 文件中定义任何数量的环境变量，这使得它非常适合管理应用的配置和敏感数据。

- **实践**: 使用环境变量是一种很好的实践，特别是在管理数据库连接字符串、API密钥和其他可能在不同环境下变化的配置时。


## `.gitignore`忽略所有 `.env` 文件的方式:

如果你想要忽略所有以 `.env` 开头的文件，无论它们位于项目的哪个部分，你可以在 `.gitignore` 文件中添加以下规则：<br>

```plaintext
.env*
```

这将会匹配 `.env`、`.env.local`、`.env.production` 等等任何以 `.env` 开头的文件。<br>

### 重要提示:

- 在添加任何规则之前，请确保 `.gitignore` 文件本身已经被提交到了你的Git仓库中。

- 如果之前不小心提交了 `.env` 文件，仅仅是添加 `.gitignore` 规则是不够的。你需要从Git历史中移除这些文件。可以使用 `git rm --cached file_name` 命令来移除文件，并随后提交这个更改。

- 定期检查你的Git状态（使用 `git status` 命令）以确保没有敏感文件被不小心包含在内。

通过正确设置 `.gitignore`，你可以有效地防止敏感配置信息被意外提交到版本控制系统中，从而保护你的项目安全。<br>


## 在Sanic或Flask中使用:

在使用Sanic、Flask或任何其他Python框架时，你通常只需要在程序的入口点，也就是启动服务的地方，调用一次 `load_dotenv('.env.local')`。<br>

这样，`python-dotenv` 库会读取 `.env.local` 文件并将其中的变量加载到环境中。之后，你可以在程序的任何地方使用 `os.getenv()` 来访问这些变量。<br>

### 步骤概述:

1. **在程序入口点加载环境变量**:

在你启动Sanic服务的Python脚本中，添加以下代码：<br>

```python
from dotenv import load_dotenv
load_dotenv('.env.local')
```

这会在程序开始运行时加载 `.env.local` 文件中的环境变量。<br>

2. **在程序的其他部分访问环境变量**:

在程序的其他文件和模块中，当你需要访问环境变量时，只需使用以下代码：<br>

```python
import os
some_variable = os.getenv('SOME_VARIABLE')
```

这里的 `'SOME_VARIABLE'` 是你在 `.env.local` 文件中定义的变量名。<br>

### 注意事项:

- 确保在调用任何需要环境变量的代码之前加载了环境变量。通常，这意味着在程序的最开始就调用 `load_dotenv()`。

- 如果你的应用是在多个进程或工作线程中运行的，只要每个进程/线程都是从同一入口点启动的，每个进程/线程都将自动具有相同的环境变量。

- 为了安全和避免敏感信息泄露，确保 `.env.local` 文件不会被提交到版本控制系统，如Git。

通过这种方式，你可以简化配置管理，使你的Sanic应用更安全、更灵活，同时也更易于维护。<br>

## `.env`文件中数据的格式:

`.env`文件通**常用于存储配置变量，如数据库设置、API密钥等**，以方便开发和生产环境中的使用。这个文件的格式是由简单的键值对组成的，每个键值对设置一行。格式通常如下所示：<br>

```txt
KEY1=value1
KEY2=value2
# 这是注释
KEY3=value3
```

这里的“KEY1”、“KEY2”和“KEY3”是变量名，而“value1”、“value2”和“value3”是相应的值。你可以根据需要添加任意数量的键值对。<br>

🐳🐳🐳注意，`.env`文件中通常不包含空格，如果值中包含空格，可以用引号将值括起来，如`KEY="value with space"`。也请注意，`.env`文件中的注释可以用`#`符号来标记。<br>
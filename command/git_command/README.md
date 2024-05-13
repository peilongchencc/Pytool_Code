# Git Command
- [Git Command](#git-command)
  - [git安装/更新：](#git安装更新)
  - [创建git仓库：](#创建git仓库)
    - [将空文件夹变成Git仓库：](#将空文件夹变成git仓库)
    - [将非空文件夹变成Git仓库:](#将非空文件夹变成git仓库)
    - [将git仓库变为普通文件夹：](#将git仓库变为普通文件夹)
  - [设置git仓库信息(个人、远程仓库)：](#设置git仓库信息个人远程仓库)
  - [git分支：](#git分支)
    - [分支创建：](#分支创建)
    - [查看分支：](#查看分支)
    - [查看当前分支的上游分支：`git branch -vv`](#查看当前分支的上游分支git-branch--vv)
    - [切换分支：](#切换分支)
    - [修改分支名称：](#修改分支名称)
    - [合并分支：](#合并分支)
      - [分支a中的内容：](#分支a中的内容)
      - [分支b中的内容：](#分支b中的内容)
      - [将分支b的内容合并到分支a上：](#将分支b的内容合并到分支a上)
    - [删除分支：](#删除分支)
      - [删除本地分支:](#删除本地分支)
      - [删除远程分支:](#删除远程分支)
  - [文件忽略".gitignore"](#文件忽略gitignore)
  - [Git操作常见流程：](#git操作常见流程)
  - [修改git仓库信息：](#修改git仓库信息)
    - [删除remote记录：](#删除remote记录)
    - [`git init`创建非master的分支名：](#git-init创建非master的分支名)
  - [git 和 github、gitlab 的区别：](#git-和-githubgitlab-的区别)
  - [git clone 的使用：](#git-clone-的使用)
    - [git clone 和 git pull 的区别：(含部分 git fetch讲解)](#git-clone-和-git-pull-的区别含部分-git-fetch讲解)
    - [git clone 拉取远程仓库指定分支：](#git-clone-拉取远程仓库指定分支)
  - [git pull 的作用:](#git-pull-的作用)
    - [问题描述:](#问题描述)
    - [问题解答:](#问题解答)
    - [更详细的示例:](#更详细的示例)
    - [将不同分支的内容上传到不同的远程仓库:](#将不同分支的内容上传到不同的远程仓库)

## git安装/更新：
要使用git指令，首先要确保Ubuntu上安装了Git。你可以在终端中运行以下命令检查是否已安装Git：<br>

```bash
git --version
```

如果尚未安装，可以使用以下命令安装Git：<br>

```bash
sudo apt update
sudo apt install git
```

如果你之前已经安装了Git，它会被更新到最新的可用版本。Ubuntu 18.04软件仓库中的Git版本是2.17.1，无法更新到更新版本。🫠🫠🫠<br>

🧜‍♂️🧜‍♂️🧜‍♂️注意：`git` 命令只能在 `git` 仓库中使用（除了 `git init` 初始化命令），`git` 仓库外无法使用 `git` 指令。<br>


接下来，你可以按照以下步骤将文件夹变成Git仓库：<br>
<br>

## 创建git仓库：
git仓库的创建是针对文件夹(或路径)下的所有内容，常见的有2种情况，一种是将空文件夹变成Git仓库，另一种是将非空文件夹变成Git仓库。接下来，我分别讲解：<br>

### 将空文件夹变成Git仓库：

1. 创建一个空文件夹，或者如果已经有一个空文件夹，跳过此步骤。

```bash
mkdir my_empty_folder
```

2. 进入该文件夹：

```bash
cd my_empty_folder
```

3. 初始化Git仓库：

```bash
git init
```

现在，你的空文件夹已经变成了一个Git仓库。<br>

### 将非空文件夹变成Git仓库:

1. 如果文件夹中已经有内容，你需要进入该文件夹：

```bash
cd my_folder_with_content
```

2. 初始化Git仓库：

```bash
git init
```

3. 将文件夹中的所有文件和文件夹添加到Git仓库的暂存区（注意：这会将所有内容添加到暂存区，包括子文件夹和文件）：

```bash
git add .
```

4. 提交更改到Git仓库：

```bash
git commit -m "Initial commit"
```

现在，你的文件夹中的内容已经被提交到了Git仓库中。<br>

🌿🌿🌿请注意，现在你只是在本地操作，还无法将你的操作同步到远程仓库(github或gitlab平台)。如果要同步，需要用到 `git push` 将本地代码推送到远程，但使用 `git push` 前需要首先配置一些基本信息。<br>

### 将git仓库变为普通文件夹：
要将某个文件夹的Git仓库状态取消，使其变为正常文件夹，你可以按照以下步骤操作：<br>

🚨🚨🚨**注意：执行这些步骤将会删除Git历史记录和版本控制信息，所以请在操作之前确保你不再需要这些信息。**<br>

1. 打开终端。

2. 使用 `cd` 命令导航到包含你想要取消Git仓库状态的文件夹的目录。例如，如果你的项目文件夹在 `~/my_project`，可以执行以下命令：

```bash
cd ~/my_project
```

3. 确保你在项目文件夹内，然后运行以下命令来删除Git仓库信息：

```bash
rm -rf .git
```

这将删除包含Git版本控制信息的 `.git` 文件夹。<br>

4. 你的项目文件夹现在已经不再是一个Git仓库，它变为了一个普通的文件夹。如果你此时执行git指令，将提示以下信息：

```log
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
```

请注意，执行这些步骤后，你将失去Git版本控制的所有优势，包括历史记录和版本管理。🔥🔥🔥确保你已经备份了任何重要的文件或历史记录，以防需要在将来恢复它们。🔥🔥🔥<br>
<br>

## 设置git仓库信息(个人、远程仓库)：

1. 获取github或gitlab的仓库信息。

> 笔者以当前仓库为例，读者注意修改为自己的仓库信息。

```bash
git@github.com:peilongchencc/Pytool_Code.git
```

2. 在终端中运行以下命令，为当前git仓库创建远程连接，并且将它们关联起来：

```bash
git remote add origin git@github.com:peilongchencc/Pytool_Code.git
```

其中`origin`是一个常用的默认远程仓库名称，但你也可以选择其他名称。当你想要删除远程仓库链接时，可以通过远程仓库名称删除。<br>

git仓库允许一个仓库配置多个远程链接，方便在`git push`的时候同时推送到多个远程仓库，但不允许出现相同的远程仓库名称，例如你已经有了一个`origin`，就不能在当前git仓库再添加一个名为`origin`的远程仓库。🐳🐳🐳<br>

3. 验证远程仓库是否成功关联，可以使用以下命令：

```bash
git remote -v
```

这将列出所有与你的本地仓库关联的远程仓库。如果一切正常，你应该能够看到你刚刚添加的远程仓库URL。<br>

4. 设置个人信息：

我们要提交信息，管理员肯定需要看到我们的个人信息，知道是谁提交的内容，所以需要设置个人信息。<br>

参考以下指令，然后将 `"Your_username"` 、 `"Your_email"` 替换为个人信息，然后运行指令，即可全局设置个人信息:<br>

```bash
git config --global user.name "Your_username"
git config --global user.email "Your_email"
```

例如:<br>

```bash
git config --global user.name "peilongchencc"
git config --global user.email "peilongchencc@163.com"
```

这样，只要是当前系统的git仓库都会绑定当前个人信息，效果如下：<br>

```log
root@iZ2zea5v77oawjy2qz7cxxx:/data# git config --global user.name
peilongchencc
root@iZ2zea5v77oawjy2qz7cxxx:/data# git config --global user.email
peilongchencc@163.com
```

5. 现在，你可以将本地的更改推送到远程仓库：

```bash
git push
```
🚨🚨🚨注意：`git push` 是将当前分支的内容推送到远程仓库对应的分支，如果不确定自己要推送的分支，应该在 `git push` 前通过以下指令查一下当前所处的分支：<br>
```bash
git branch -a
```
> 带`*`的为当前所处的分支，如果想要退出当前界面，按字母`q`退出～

🚀🚀🚀你可能也见过以下这种写法，这种写法表示将 `分支A` 的内容推送到远程仓库`origin`，在你的git仓库链接了多个远程仓库时更实用：<br>
```bash
git push origin 分支A的名称
```

<br>

## git分支：
Git分支是Git版本控制系统中的一个重要概念，Git分支是树🌲结构，它允许你在代码库中创建不同的分支，以便并行开发、测试和管理代码的不同版本。分支可以帮助开发团队更有效地协作，同时保持代码的稳定性。<br>
> Git分支，每次commit是一个树的节点

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/5ccf44ce-a66b-46ff-9261-16d5aa58fba3" alt="image" width="70%" height="70%">

### 分支创建：
创建分支一定要考虑清楚是从哪个分支延伸出来的‼️‼️如果你是想在`main`分支上延伸一个树杈进行操作，那一定要在`main`分支执行创建并切换到新分支的指令。<br>

1. 打开终端，并进入Git仓库所在的目录。

2. 使用以下指令查看当前Git仓库有哪些分支： 

```bash
git branch -a
```

🔥🔥🔥该指令会列出当前Git仓库的所有分支，本地分支+远程分支，你当前所在的分支前面会显示一个星号 (*) 。<br>

3. 切换到基底分支：

再次提醒，一定要想清楚分支从哪个分支延伸出来的🚨 假设你现在位于`release`分支，你想要在`main`分支基础上创建新分支，那就执行以下指令：<br>
```bash
git checkout main
```

4. 此时已切换到main分支，可以使用以下命令来创建并切换到新分支，其中`branch_new`是创建的新分支的名称：

```shell
git checkout -b branch_new
```

或者在较新版本的Git中使用：<br>
```shell
git switch -c branch_new
```

5. 现在，你已经在名为`branch_new`的新分支上，可以通过以下指令确认：

```bash
git branch -a
```

### 查看分支：

如果你使用的最新版Git版本，可以使用以下指令查看当前所在分支：<br>
> 终端会直接输出当前所在分支名称。

```bash
git branch --show-current
```

因为笔者使用的是ubuntu 18.04系统，Git版本是2.17.1，所以笔者经常用的指令为：<br>
> 查看分支的指令有很多，只有以下指令会显示 **包括git远程仓库分支的所有分支**(强烈推荐这种查看git分支的方式)

```shell
git branch -a
```

终端将输出类似如下内容:<br>

```log
* branch_a
  branch_b
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/branch_a
```

🥷🥷🥷<br>
其中星号 (*) 开头的分支为我们当前所在分支， `remotes/` 开头的部分为远程仓库分支，你可能已经注意到了 `remotes/` 开头部分并没有 `branch_b` 的内容，那是因为 `branch_b` 是在本地创建的，还没有和远程仓库同步(即没有`git push`过)。<br>

### 查看当前分支的上游分支：`git branch -vv`

```txt
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/chatgpt-webui# git branch -vv
* custom 4719c2c [origin/custom] requirements.txt添加loguru
  main   d582566 [origin/main] update 1106
```

该指令用于当你有其他上游分支的时候进行同步操作。<br>


### 切换分支：
前面已经讲过 `git checkout` 的用法了，这里再补充一点:<br>

`git checkout` 可以切换到远程仓库对应的分支，假设你使用 `git clone` 拉取了某个远程仓库的代码，由于 **`git clone` 默认拉取的是远程仓库主分支的内容** 。此时你本地`git branch -a`应该显示类似如下内容:<br>
> `git clone`操作，后面的内容会讲～

```log
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/test
  remotes/origin/release
  remotes/origin/master
```

😵‍💫😵‍💫😵‍💫有人可能会问，"我本地是否能切换到远程仓库对应的release分支？"，答案是可以，和常规切换分支的操作是一样的，直接使用以下指令即可：<br>

```bash
git checkout release
```

特别提醒，一定要注意指令的正确使用，千万不要使用以下指令：<br>

```bash
git checkout -b release
```

这样只会创建一个与远程仓库`release`重名的分支，并不是同步了远程仓库的`release`分支内容，这样会引起大问题，一定要注意‼️‼️‼️<br>

### 修改分支名称：

🚨🚨🚨注意：在执行以下步骤之前，请确保你的Git版本在2.28.0或更高版本，因为较早的版本可能不支持更改默认分支名称。<br>

假设你要将分支的名称从 "master" 更改为 "test"，你可以按照以下步骤进行操作：<br>

1. 确定当前所处分支，你可以使用以下命令来查看当前所在的分支：：

```bash
git branch -a
```
如果 "master" 分支是当前分支，会显示一个星号 (*) 在其旁边。

2. 如果你不在 "master" 分支上，需要切换到 "master" 分支：

```bash
git checkout master
```

3. 现在，你可以将 "master" 分支重命名为 "test" 分支。你可以使用以下命令：

```bash
git branch -m master test
```

4. 再次查看下当前所在的分支名：

```bash
git branch -a
```

此时当前分支应该会显示为"test"，且会显示一个星号 (*) 在其旁边。<br>

### 合并分支：
假设我们现在有2个分支，`branch_a`和`branch_b`。<br>

#### 分支a中的内容：
`branch_a`的目录树结构如下：<br>
```log
.
├── push.sh
└── segment
    └── sanic_server.py
```

`branch_a`中`push.sh`内容如下：<br>
```bash
git add .
git commit -m "更新分支a"
git push
```

`branch_a`中`sanic_server.py`内容如下：<br>
```python
from sanic import Sanic
from sanic.response import json
import jieba

app = Sanic("jieba-segment")


@app.route("/seg_ment", methods=["POST"])
async def seg_ment(request):
    """分词API"""
    text = request.form.get("user_input")    # postman 测试时字段的名称需要对应，此处写"user_input"，postman写"input"就会报错。
    if not text:
        return json({"error": "缺少 \"user_input\" parameter"}, status=400) # \ 用于转义
    # 进行jieba分词处理
    text_segment = jieba.lcut(text)
    return json({"用户输入的分词结果为：": text_segment})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

#### 分支b中的内容：
`branch_b`的目录树结构如下：<br>
```log
.
├── push.sh
└── segment
    ├── data.txt
    └── sanic_server.py
```

`branch_b`中`push.sh`内容如下：<br>
```bash
git add .
git commit -m "更新分支b"
git push
```

`branch_b`中`data.txt`内容如下：<br>
```txt
牙疼吃什么药？
肠胃炎属于神经性疾病吗？
```

`branch_b`中`sanic_server.py`内容如下：<br>
```python
from sanic import Sanic
from sanic.response import json
import jieba

app = Sanic("jieba-segment")


@app.route("/segment", methods=["POST"])
async def segment(request):
    """分词API"""
    text = request.form.get("user_input")    # postman 测试时字段的名称需要对应，此处写"user_input"，postman写"input"就会报错。
    if not text:
        return json({"error": "缺少 \"user_input\" parameter"}, status=400) # \ 用于转义

    text_segment = jieba.lcut(text)
    return json({"用户输入的分词结果为：": text_segment})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

#### 将分支b的内容合并到分支a上：

1. 终端输入以下指令，确保自己在要接受合并的分支上：<br>
```bash
git checkout branch_a
```

2. 运行以下指令将 `branch_b` 合并到 `branch_a` 上：<br>
```bash
git merge branch_b
```


🚀🚀🚀现在，`branch_b` 中的内容会合并到 `branch_a` 中：<br>

`branch_b` 中有但 `branch_a` 中没有的文件会进行添加(文件显示绿色🌿🌿🌿)。<br>

对于 `branch_b` 和 `branch_a` 中都有的文件，如果没有更改，没有变化。<br>

如果 `branch_b` 相较于 `branch_a` 在同一文件有修改，这就会引发代码合并冲突。Git会尝试自动合并更改，但无法确定应该使用哪一组更改(文件显示为红色🚨🚨🚨)。在这种情况下，你需要手动解决冲突。<br>

🥴🥴🥴打开包含冲突的文件。文件中会有特殊标记来表示冲突的地方，通常看起来像这样：<br>

```txt
采用当前更改|采用传入的更改|保留双方更改|比较变更
<<<<<<< HEAD(当前更改)
//当前分支的代码
=======
//传入分支的代码
>>>>>>> branch_b(传入的更改)
```

你可以选择点击 `采用当前更改|采用传入的更改|保留双方更改|比较变更` 中的任意一项，也可以在当前界面找到 `在合并编辑器中解析` 进行操作。<br>
***

例如，你可以看到`branch_a`的目录树变为如下结构：<br>
> 多了 `segment/data.txt` 文件。

```log
.
├── push.sh
└── segment
    ├── data.txt
    └── sanic_server.py
```

其他内容根据文件颜色解决冲突，冲突解决后，运行以下指令提交到远程即可：<br>
```bash
git add .
git commit -m "将branch_b合并到branch_a"
git push
```

此时，可能会出现以下提示:<br>
```log
fatal: The current branch branch_a has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin branch_a
```

这表示你当前分支在远程仓库没有对应的分支，表示你是第一次`git push`这个分支。<br>

按照提示，终端执行以下指令就好：<br>

```bash
git push --set-upstream origin branch_a
```

现在，我们已经完成了将 `branch_b` 的内容合并到 `branch_a` 上的全部过程。需要注意的是，将 `branch_b` 的内容合并到 `branch_a` 上，`branch_b` 的内容是不会变化的，你可以运行以下指令切换到 `branch_b` 查看，会发现 `branch_b` 并没有变化：<br>

```bash
git checkout branch_b
```

### 删除分支：

#### 删除本地分支:
通常，我们在执行完分支合并后，会将分支删除，如果此时你想要将 `branch_b` 分支删除，可以终端运行以下指令：<br>
```bash
git branch -d branch_b
```

如果 "新拓展的分支" 还没有和 "其他分支 " 合并，此时若要删除，需要终端使用以下指令删除 "新拓展的分支":<br>
```bash
git branch -D branch_b
```

#### 删除远程分支:

如果这个分支已经向远程仓库提交过，要删除远程仓库的这个分支，需要使用`git push`命令，并指定删除的目标。假设远程仓库名为`origin`，可以这样删除`branch_b`分支：<br>

```bash
git push origin --delete branch_b
```
> 在任何分支都可以执行上述操作～🐳🐳🐳

这个命令会告诉远程仓库删除名为`branch_b`的分支。<br>

请注意，删除远程分支需要相应的权限，如果你没有权限删除远程分支，需要联系仓库的管理员或拥有者进行操作。<br>

最终，通过执行上述步骤，你将删除本地分支和远程分支中的`branch_b`分支。请谨慎操作，因为删除分支可能会导致数据丢失。<br>
<br>


## 文件忽略".gitignore"
`.gitignore` 文件用于告诉Git版本控制系统哪些文件或目录应该被忽略，执行 `git push` 时不被推送到远程仓库。<br>

下面是一些关于如何使用`.gitignore` 文件的示例以及一些常见的用例：

1. 忽略特定文件：

```bash
# 忽略一个特定文件
filename.txt
```

2. 忽略特定目录：

```bash
# 忽略一个特定目录
/myfolder/
```

3. 使用通配符：

```bash
# 忽略所有 .log 文件
*.log

# 忽略所有 .txt 文件
*.txt

# 忽略所有 .pdf 文件
*.pdf
```

4. 忽略所有文件夹下的特定文件或目录：

```bash
# 忽略所有目录下的 .DS_Store 文件（通常在 macOS 上生成）
**/.DS_Store

# 忽略所有目录下的 node_modules 目录
**/node_modules/
```

5. 使用注释：

```bash
# 这是一条注释，不会影响 .gitignore 的规则

# 忽略所有日志文件
*.log
```

6. 强制包括某些文件或目录：

```bash
# 忽略所有 .log 文件，但包括 error.log 文件
*.log
!error.log
```

7. 使用多个`.gitignore` 文件：

你可以选择在根目录使用一个`.gitignore` 文件，也可以选择在不同的子目录中使用多个`.gitignore` 文件，每个文件针对特定目录或子项目进行规则设置。<br>

示例中的规则会告诉Git在提交和跟踪更改时要忽略指定的文件或目录。当你在项目目录中创建或编辑`.gitignore` 文件后，Git将自动遵循这些规则。确保将`.gitignore` 文件包含在版本控制中，以便与团队共享。<br>

总之，`.gitignore` 文件是一个非常有用的工具，可以帮助你维护干净和有序的版本控制仓库，同时排除不必要的文件和目录。<br>
<br>

‼️‼️‼️请注意，如果你已经将要忽略的文件夹(假设为`.vscode`文件夹)提交到远程仓库，你现在想要去除`.vscode`文件夹的追踪，你可以使用以下命令来执行这些操作：<br>

在 `.gitignore` 文件中，添加以下行来指定忽略 `.vscode` 文件夹：<br>

```bash
# 去除 .vscode 文件夹的追踪
.vscode/
```

终端执行以下指令，去除 `.vscode` 文件夹的追踪:<br>

```bash
git checkout your_git_branch
git rm -r --cached .vscode/
git commit -m "去除 .vscode 文件夹的追踪"
git push
```

这将删除远程仓库中的 `.vscode` 文件夹，并确保以后不再跟踪它。注意将 `your_git_branch` 替换为你的分支名。<br>
<br>

## Git操作常见流程：
1. `git init`初始化或`git clone`一个git仓库。(`git clone`操作，后面的内容会讲～)
2. 编写自己的代码/文件。
3. 依次运行以下指令：

```bash
# 运行本脚本，需要终端先执行以下指令：
# chmod +x ./push_commit_to_git.sh
git add .
git commit -m "更新代码"
git push
```

笔者通常是将上述内容写入一个`sh脚本`，假设`sh脚本`在当前路径下，且名为`push_commit_to_git.sh`，笔者编辑完代码后，会直接运行以下指令：<br>

```bash
./push_commit_to_git.sh
```

这样就可以一键提交到远程～非常便捷。<br>

请记住，如果要运行上述`sh脚本`，首先要运行下列指令为`sh脚本`开启运行权限：<br>

```bash
chmod +x ./push_commit_to_git.sh
```

<br>

## 修改git仓库信息：
我们在使用git时，可能会由于各种情况需要修改git仓库的信息，这里就讲述下修改常见信息的方式：<br>

### 删除remote记录：
git仓库允许一个仓库配置多个远程链接，方便在`git push`的时候同时推送到多个远程仓库。<br>

你可以通过以下指令，查看自己定义的远程仓库名称：<br>
```bash
git remote -v
```

终端将显示类似如下信息：<br>
```log
origin  git@github.com:peilongchencc/Pytool_Code.git (fetch)
origin  git@github.com:peilongchencc/Pytool_Code.git (push)
```

回想一下，我在介绍设置remote的时候提到过，`origin`是远程仓库名称，我们通过远程仓库名称删除remote记录。假设我们要删除名为`origin`的远程仓库:<br>
```log
git remote remove origin
```

假设我们要删除名为`master`的远程仓库:<br>
```log
git remote remove master
```

如果想要关联一个新的远程库，重新使用 `git remote add` 添加即可：<br>
```bash
git remote add origin git@github.com:peilongchencc/Pytool_Code.git
```

记得 `origin` 是远程仓库名称，可以自定义修改～🐳🐳🐳<br>

### `git init`创建非master的分支名：
Git 2.28.0版本前，使用 `git init` 创建git仓库时，默认生成的分支名为"master"。Git 2.28.0版本引入了一个新的默认分支名称，称为"main"。<br>


不过，你可以根据需要重命名默认分支，或者使用其他分支名称来初始化仓库，具体操作取决于你的偏好和需求。例如，你可以使用以下命令初始化一个仓库并指定不同的默认分支名称：<br>

```bash
git init --initial-branch=yourbranchname
```

这将创建一个新的Git仓库并将默认分支设置为"yourbranchname"。<br>
<br>


## git 和 github、gitlab 的区别：

git 是一个版本控制软件，github 是一个代码托管平台。github 或 gitlab 可以使用 git 进行代码的版本控制，可以执行修改代码、切换分支、查看不同代码版本、分享代码、提交bug等操作。<br>


## git clone 的使用：

`git clone`是一个用于复制（克隆）Git仓库的命令。它允许你从远程或本地仓库创建一个本地副本，这样你就可以在本地工作、编辑和提交代码，而不需要直接访问原始仓库。这对于协作开发和版本控制非常有用。<br>

要使用`git clone`，请按照以下步骤进行：<br>

1. 打开终端。

2. 导航到你想要克隆仓库的目录：你可以使用`cd`命令来切换到目标目录。例如，如果你想将仓库克隆到你的主目录下，你可以运行以下命令：

```bash
cd ~
```

3. 使用`git clone`命令来克隆仓库。你需要提供仓库的URL。例如，如果你想克隆一个名为 "example-repo" 的仓库，它的URL是 `https://github.com/user/example-repo.git`，你可以运行以下命令：
> 🚨🚨🚨注意：git仓库中不能套着拉取一个git仓库。

```bash
git clone https://github.com/user/example-repo.git
```

如果你要克隆的是本地仓库，你可以提供本地路径，例如：<br>

```bash
git clone /path/to/local/repo
```

4. Git会开始克隆仓库。它将从远程仓库或本地仓库复制所有代码和历史记录到你的本地计算机。

5. 克隆完成后，你可以进入新创建的目录，开始在本地仓库上工作：

```bash
cd example-repo
```

现在，你已经成功克隆了一个Git仓库，并可以在本地进行编辑和提交更改。使用`git pull`命令可以从远程仓库获取最新更新，使用`git push`命令将你的更改推送到远程仓库。<br>

请注意，你需要安装Git并确保在终端中可用才能使用`git clone`命令。在Ubuntu上，你可以使用以下命令安装Git：<br>

```bash
sudo apt update
sudo apt install git
```

然后，你就可以开始使用Git来管理代码仓库了。<br>

### git clone 和 git pull 的区别：(含部分 git fetch讲解)
从字面意思也可以理解，都是往下拉代码，`git clone`是克隆，`git pull` 是拉取，但两者有区别：<br>

`git clone` 是从远程仓库克隆一个库到你的本地，是一个本地从无到有的过程。<br>

`git pull` 是你本地已经有了一个远程仓库的克隆版，此时使用 `git pull` 会从远程仓库获取**当前分支**的所有内容，并merge（合并）到当前分支。<br>

`git pull` 相当于 `git fetch`（拉取代码） + `git merge`。注意⚠️：`git pull` 只拉取当前分支对应的远程分支内容，并不会影响其他分支的内容。🥴🥴🥴<br>

### git clone 拉取远程仓库指定分支：
`git clone` 默认拉取远程仓库的主分支(通常是main或master)，如果要拉取远程仓库某个指定分支，可以使用以下指令：<br>

```bash
git clone -b <branch_name> <remote_repository_url>
```

假设你要拉取 `git@github.com:peilongchencc/Pytool_Code.git` 仓库的 `release` 分支，可以使用以下指令：<br>
```bash
git clone -b release git@github.com:peilongchencc/Pytool_Code.git
```

🚨🚨🚨注意：git仓库中不能套着拉取一个git仓库。<br>


## git pull 的作用:

### 问题描述:

我的git项目有多个分支，不同分支对应的不同的远程仓库，我使用git pull拉取的是所有分支对应的最新代码吗？<br>

### 问题解答:

在 Git 中，默认情况下，`git pull` 命令只会拉取和更新当前活动分支的最新代码，并且它会从该分支关联的远程仓库拉取。<br>

如果你有多个分支，每个分支对应不同的远程仓库，你需要切换到相应的分支并分别执行 `git pull` 命令来更新每个分支的代码。<br>

例如，如果你在 `branchA` 分支上，并且它关联到了远程仓库 `origin`，当你执行 `git pull` 时，Git 会从 `origin` 拉取 `branchA` 的最新改动并合并到你的本地分支。如果你要更新其他分支，如 `branchB`，你需要先切换到那个分支：<br>

```bash
git checkout branchB
```

然后再执行 `git pull` 以拉取和合并远程分支的最新代码。<br>

如果你想要查看或修改某个分支的远程跟踪关系，你可以使用 `git branch -vv` 命令查看所有分支的远程关联情况，或者用 `git remote show [remote-name]` 查看更详细的远程仓库信息。<br>

如果有必要修改某个分支的远程跟踪仓库，你可以使用 `git branch --set-upstream-to` 命令。例如，要将 `branchB` 的远程跟踪设置为远程仓库 `otherRemote` 上的 `branchB`：<br>

```bash
git branch --set-upstream-to=otherRemote/branchB branchB
```

这样设置后，当你在 `branchB` 上执行 `git pull` 时，它会从 `otherRemote` 的 `branchB` 拉取代码。<br>

### 更详细的示例:

假设你项目的git信息如下:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/baidu-hot-search-crawling-code# git branch -a
* main
  master
  remotes/github/main
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/baidu-hot-search-crawling-code# git remote -v
github  git@github.com:peilongchencc/baidu_hot_search.git (fetch)
github  git@github.com:peilongchencc/baidu_hot_search.git (push)
origin  git@gitee.com:beijing-zhixing-qiming/baidu-hot-search-crawling-code.git (fetch)
origin  git@gitee.com:beijing-zhixing-qiming/baidu-hot-search-crawling-code.git (push)
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/baidu-hot-search-crawling-code# 
```

你当前处于 `main` 分支，你想要让 `main` 分支跟踪远程仓库 github 的 main 分支。你需要先设置跟踪关系，然后可以拉取该远程仓库的代码。这里是步骤：<br>

1. **设置本地 `main` 分支跟踪远程 `github` 仓库的 `main` 分支**：

```bash
git branch --set-upstream-to=github/main main
```

`github` 是区别于 `origin` 的远程链接的别名，不要混淆了。‼️‼️‼️<br>

2. **拉取最新的代码**：

```bash
# 只会拉取当前分支的远程代码
git pull
```

这样，你的本地 `main` 分支就会从远程 `github` 仓库的 `main` 分支拉取最新的代码。如果你想要查看当前分支的跟踪情况，可以使用：<br>

```bash
git branch -vv
```

这会显示你本地分支的详细信息，包括它们正在跟踪的远程分支。如果一切设置正确，你应该看到 `main` 分支跟踪 `github/main`。

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/baidu-hot-search-crawling-code# git branch -vv
* main   b3b7188 [github/main] 百度热搜项目提交
  master b8c4bf5 [origin/master] 剔除log文件
```

### 将不同分支的内容上传到不同的远程仓库:

要将你的 `main` 分支的代码上传到 GitHub，你需要使用 `git push` 命令。这个操作不会影响你的 `master` 分支，因为 Git 的推送操作是基于当前分支的，不会影响其他本地分支。<br>

以下是如何上传 `main` 分支到 GitHub 的步骤：<br>

1. **切换到 `main` 分支**（如果你不在该分支上）：

```bash
git checkout main
```

2. **推送 `main` 分支到 GitHub**：

```bash
git push github main
```

这里，`github` 是你的远程仓库的名称，`main` 是要推送的分支名。如果你已经设置了 `main` 分支跟踪 `github` 的 `main` 分支，你也可以简单使用：<br>

```bash
git push
```

这会根据设置的跟踪关系推送到正确的远程分支。<br>

🔥🔥🔥在 Git 中，使用 `git push` 命令时，它 **默认只推送当前分支到该分支跟踪的远程分支** 。这个操作不会影响到 `master` `分支或其他任何分支。master` 分支的代码也不会被推送，除非你切换到 `master` 分支并执行 `git push`（前提是 `master` 分支也设置了相应的跟踪关系）。<br>
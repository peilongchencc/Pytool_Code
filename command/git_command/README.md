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
    - [切换分支：](#切换分支)
    - [修改分支名称：](#修改分支名称)
    - [合并分支：](#合并分支)
      - [分支a中的内容：](#分支a中的内容)
      - [分支b中的内容：](#分支b中的内容)
      - [将分支b的内容合并到分支a上：](#将分支b的内容合并到分支a上)
    - [删除分支：](#删除分支)
      - [删除本地分支:](#删除本地分支)
      - [删除远程分支:](#删除远程分支)
  - [Git操作常见流程：](#git操作常见流程)
  - [修改git仓库信息：](#修改git仓库信息)
    - [删除remote记录：](#删除remote记录)
    - [`git init`创建非master的分支名：](#git-init创建非master的分支名)
  - [git 和 github、gitlab 的区别：](#git-和-githubgitlab-的区别)
  - [git clone 的使用：](#git-clone-的使用)
    - [git clone 和 git pull 的区别：(含部分 git fetch讲解)](#git-clone-和-git-pull-的区别含部分-git-fetch讲解)
    - [git clone 拉取远程仓库指定分支：](#git-clone-拉取远程仓库指定分支)
  - [Git常见场景运用：](#git常见场景运用)
    - [协同工作时，你当前所在的分支被其他人更新，你需要拉取最新的内容再接着自己的工作：](#协同工作时你当前所在的分支被其他人更新你需要拉取最新的内容再接着自己的工作)
      - [git pull 让你选择分支合并方式：](#git-pull-让你选择分支合并方式)
      - [git pull 让你输入合并提交信息：](#git-pull-让你输入合并提交信息)
    - [协同工作时，你在git分支C上工作，但领导突然让你解决分支B的bug，解决完bug，提交分支B后，再完成分支C的工作：](#协同工作时你在git分支c上工作但领导突然让你解决分支b的bug解决完bug提交分支b后再完成分支c的工作)
    - [git如何放弃当前分支上一次提交到现在的所有修改，自上一次提交到现在，你还没有commit过。](#git如何放弃当前分支上一次提交到现在的所有修改自上一次提交到现在你还没有commit过)
    - [你想在当前git仓库回退到上一个版本，且不丢失现在的更改，应该怎么做呢？](#你想在当前git仓库回退到上一个版本且不丢失现在的更改应该怎么做呢)
      - [使用git stash：](#使用git-stash)
      - [使用新的分支:](#使用新的分支)
    - [将git仓库下某个文件夹复制到其他目录，修改好后提交到远程仓库的操作流程：](#将git仓库下某个文件夹复制到其他目录修改好后提交到远程仓库的操作流程)
  - [为什么你把要忽略的内容写入了`.gitignore`，git push时还是把`.gitignore`中的内容上传了？是有什么操作顺序吗？](#为什么你把要忽略的内容写入了gitignoregit-push时还是把gitignore中的内容上传了是有什么操作顺序吗)
    - [原因：](#原因)
    - [解决方案：](#解决方案)

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

***
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
<br>

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

<br>

## Git常见场景运用：
### 协同工作时，你当前所在的分支被其他人更新，你需要拉取最新的内容再接着自己的工作：
问题描述：<br>
"人物A" 正在分支"release"上工作，工作正做了一半。"同事B"告诉"人物A"，他修改了"release"分支的内容，让"人物A"在修改后的基础上操作，"人物A"现在应该怎么做？<br>

解决方案：<br>
在这种情况下，你可以按照以下步骤来处理：

1. **保存当前工作：** 如果你正在进行一项工作，先确保将你当前的工作保存并提交到你的本地分支。使用以下命令来提交你的更改：

```bash
git add .
git commit -m "你的提交消息"
```
这会将你的更改保存到你的本地分支。(不用担心，不会推送到远程‼️‼️‼️)<br>

2. **拉取远程分支：** 你的同事已经修改了远程分支，所以你需要首先将这些修改拉取到你的本地分支，以便与他们的更改同步。使用以下命令来拉取远程分支的最新更改：

```bash
git pull
```

#### git pull 让你选择分支合并方式：
`git pull`将会从远程仓库拉取当前分支("release")的最新内容。如果你是第一次这样操作，会提示你以下内容：<br>
```log
提示：您有偏离的分支，需要指定如何调和它们。您可以在执行下一次
提示：pull 操作之前执行下面一条命令来抑制本消息：
提示：
提示：  git config pull.rebase false  # 合并
提示：  git config pull.rebase true   # 变基
提示：  git config pull.ff only       # 仅快进
提示：
提示：您可以将 "git config" 替换为 "git config --global" 以便为所有仓库设置
提示：缺省的配置项。您也可以在每次执行 pull 命令时添加 --rebase、--no-rebase，
提示：或者 --ff-only 参数覆盖缺省设置。
致命错误：需要指定如何调和偏离的分支。
```

不用太过担忧，终端输入以下指令，然后再次执行`git pull`即可：<br>
```bash
git config --global pull.rebase false 
```

通常大家都是使用的`仅快进`模式，其他模式了解较少，可以自行百度了解。<br>

#### git pull 让你输入合并提交信息：
`git pull`时，也有可能会进入以下界面：<br>
```txt
  GNU nano 2.9.3                                                               /data/Pytool_Code/.git/MERGE_MSG                                                                         

Merge branch 'main' of github.com:peilongchencc/Pytool_Code into main

# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.

                                                                                    [ Read 7 lines ]
^G Get Help     ^O Write Out    ^W Where Is     ^K Cut Text     ^J Justify      ^C Cur Pos      M-U Undo        M-A Mark Text   M-] To Bracket  M-▲ Previous    ^B Back
^X Exit         ^R Read File    ^\ Replace      ^U Uncut Text   ^T To Spell     ^_ Go To Line   M-E Redo        M-6 Copy Text   M-W WhereIs NextM-▼ Next        ^F Forward
```
🫠🫠🫠这表明你正处于一个合并冲突的状态，并且Git已经打开了一个文本编辑器（在这里是`nano`）让你输入合并提交的信息。<br>

以下是你可以采取的步骤：<br>
```txt
1. 在该编辑器中，你可以修改提交信息或者使用默认的提交信息。
2. 如果你想使用默认的提交信息，只需确保不删除任何内容，直接保存并退出即可。
3. 保存并退出`nano`的方法是按下`^O` (这意味着同时按下“Control”和“O”键)。这会询问你是否要写入更改，按“Enter”键确认。
4. 然后按下`^X` (这意味着同时按下“Control”和“X”键)来退出`nano`。
```
完成上述步骤后，你的合并提交就会完成。但是，如果在`git pull`时出现了冲突，你可能需要解决这些冲突才能继续。要检查是否有冲突，可以运行：<br>

```shell
git status
```

如果看到有冲突的文件，需要手动编辑这些文件来解决冲突，然后继续提交。<br>


3. **解决冲突（如果有）：** 如果你和你的同事都在相同的文件或部分进行了更改，可能会发生冲突。Git 会在拉取过程中提示你解决冲突。你需要手动解决这些冲突，并在文件中选择你想要保留的更改。一旦冲突解决完毕，你可以使用以下命令将更改标记为已解决：

```bash
git add 冲突文件名
```

现在，已经同步了"同事B"的操作，也解决了冲突，接下来继续自己的工作，工作完成后正常`commit`和`push`就行。<br>


### 协同工作时，你在git分支C上工作，但领导突然让你解决分支B的bug，解决完bug，提交分支B后，再完成分支C的工作：
你可以先提交分支C的更改，然后切换到分支B解决bug，再推送分支B，最后切换回分支C继续工作。<br>

以下是你可以执行的步骤：<br>

1. **提交分支C的更改：**在分支C上提交你当前的工作。

```bash
git add .
git commit -m "提交分支C的更改"
```

请注意，由于未推送的修改只存在于本地仓库中，如果你切换到其他计算机或者在其他位置上使用git时，这些修改将不可访问。因此，为了确保你的修改的备份和共享，建议你尽快执行git push操作，将修改推送到远程仓库中。<br>

2. **切换到分支B：**切换到分支B以解决bug。

```bash
git checkout 分支B的名称
```

3. **解决bug并提交：**在分支B上解决bug，解决bug后使用以下指令提交更改。

```bash
git add .
git commit -m "修复分支B上的bug"
```

4. **推送分支B：**将分支B的更改推送到远程仓库。

```bash
git push origin 分支B的名称
```

5. **切换回分支C：**切换回分支C以继续工作。

```bash
git checkout 分支C的名称
```

6. **继续分支C的工作：**现在，你可以继续在分支C上工作，并将分支C的更改提交到分支C中。

这种方法允许你在解决分支B上的bug之前保存分支C的更改，并确保你的工作不会丢失。然而，请确保在推送分支B之前，与其他团队成员协调，以避免不必要的冲突和问题。<br>


### git如何放弃当前分支上一次提交到现在的所有修改，自上一次提交到现在，你还没有commit过。
要放弃当前分支上自上次提交到现在的所有修改，首先需要使用 stash 保存修改：<br>
```shell
git stash
```

这会将未提交的修改保存在一个临时区域（stash）中，然后你可以切换到另一个分支，假设切换到 main 分支(要确保你有这个分支):<br>
```shell
git checkout main
```

现在，可通过以下指令删除stash中的保存的修改：<br>
```shell
git stash drop
```

此时已经将 stash 中保存的内容删除了，再切换回原分支就能看到上一次提交到现在的所有修改已经消失了。<br>

### 你想在当前git仓库回退到上一个版本，且不丢失现在的更改，应该怎么做呢？
如果你想在当前git仓库回退到上一个版本，但同时不丢失现在的更改，你可以使用以下的方法：<br>

#### 使用git stash：
这是一个常用的方法，它允许你暂时保存当前的更改，并在需要时重新应用它们。<br>
```shell
git stash              # 暂存当前更改
git reset --hard HEAD^ # 回退到上一个版本
git stash pop          # 重新应用暂存的更改
```

#### 使用新的分支:
你可以创建一个新的分支来保存当前的更改，然后在主分支上回退到上一个版本。<br>
```bash
git branch new-branch     # 创建一个新的分支保存当前的更改
git checkout master       # 切回主分支
git reset --hard HEAD^    # 在主分支上回退到上一个版本
git merge new-branch      # 合并新分支到主分支
```
之后，如果你觉得这个新分支不再需要，你可以删除它：<br>
```bash
git branch -d new-branch   # 删除新分支
```
使用以上任意方法，你都可以回退到上一个版本，同时不丢失现在的更改。根据你的具体需求，选择最适合你的方法。<br>

### 将git仓库下某个文件夹复制到其他目录，修改好后提交到远程仓库的操作流程：

假设你github中名为 `nlp_deploy` 仓库中的文件特别多，出于某种原因，你想要将其中名为 `nlp_server` 的文件夹复制到其他目录，操作完成后再替换原 `nlp_deploy` 仓库下的 `nlp_server` 文件夹，你所属的git分支名为`modify_nlp_server_peilongchencc`。<br>

经过了漫长的时间...现在，你已经将 `nlp_server` 修改完毕，但你迷惑了，不知道具体该怎么操作，那么就可以参考以下流程：<br>

1. 确保 `nudge_new` 中的git分支为 `modify_nlp_server_peilongchencc`：

```bash
git checkout modify_nlp_server_peilongchencc
```

2. 在本地项目根目录中，使用命令行删除旧的 `nlp_server` 文件夹。确保你已经备份了任何重要的数据，因为删除后将无法恢复旧文件夹。

```bash
rm -rf nlp_server/
```

🚨🚨🚨`nlp_server/` 是相对于项目根目录 `nlp_deploy` 的路径。<br>

3. 将你修改后的 `nlp_server` 文件夹从其他目录复制/移动到 `nlp_deploy` 文件夹下 `nlp_server` 的原位置。

4. 接下来，使用以下命令来将新的 `nlp_server` 文件夹添加到 Git 暂存区：

```bash
git add nlp_server/
```

5. 然后提交你的更改：

```bash
git commit -m "更新 nlp_server 文件夹的内容"
```

6. 最后，将更改推送到 GitHub 远程仓库中的 `modify_nlp_server_peilongchencc` 分支：

```bash
git push
```

因为你当前正处于 `modify_nlp_server_peilongchencc` 分支，所以直接运行 `git push` 指令即可。<br>

现在，你已经将包含修改好的 `nlp_server` 文件夹的 `nlp_deploy` 项目推送到远程仓库。🚀🚀🚀<br>
<br>


## 为什么你把要忽略的内容写入了`.gitignore`，git push时还是把`.gitignore`中的内容上传了？是有什么操作顺序吗？
### 原因：
使用 `.gitignore` 文件可以指定要忽略的文件和文件夹，以防止它们被 `Git` 追踪和上传到版本控制系统中。然而，有几个注意事项需要牢记：<br>

`.gitignore` 文件🥶🥶🥶**只对尚未被Git追踪的文件生效**🥶🥶🥶，对已经被Git追踪的文件无效。如果你已经将某些文件提交到了仓库中，然后再将这些文件添加到.gitignore文件中，Git仍然会追踪它们。<br>

如果你已经将某个文件添加到了Git的缓冲区（即使用了"git add"命令），然后将其添加到 `.gitignore` 文件中，这个文件仍然会被Git追踪。<br>

你需要使用"git rm --cached 文件名"命令将其从缓冲区移除。<br>

```shell
git rm --cached 文件名
```

如果你要删除的是文件夹，需要加上 `-r` 参数：<br>

```shell
git rm --cached -r 文件名
```

如果你使用的是 `git add .` 操作，可以使用以下命令：<br>
```shell
git rm --cached .
```

### 解决方案：

假设你已经把某些要忽略的内容上传至 github ，现在的解决方案如下：<br>

1. 进入自己的 `git` 项目目录下。

2. 执行 `git pull` 拉取最新代码，如果你本地没有对应的项目，执行 `git clone` 拉取最新代码也是一样。

3. 将你不想要上传至 github 的内容备份到本项目仓库之外；(可选，如果你本地也不想保留这部分内容，可以直接执行下一步。)

4. 将你不想要上传至 github 的内容删除；

5. 检查 `.gitignore` 中的内容是否正确；

6. 执行 `git add .`,`git commit -m "xxx"`,`git push`操作，现在远程仓库中你不想上传的内容已经删除了。

7. 本地，将刚刚备份的内容移回本仓库；此时你再执行`git add .`,`git commit -m "xxx"`,`git push`操作将不会把对应的内容上传至 github 远程仓库。

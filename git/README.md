# Git
- [Git](#git)
  - [git安装：](#git安装)
  - [创建git仓库：](#创建git仓库)
    - [将空文件夹变成Git仓库：](#将空文件夹变成git仓库)
    - [将非空文件夹变成Git仓库:](#将非空文件夹变成git仓库)
  - [设置git仓库信息：](#设置git仓库信息)
  - [git分支：](#git分支)
    - [分支创建：](#分支创建)
    - [修改分支名称：](#修改分支名称)
  - [修改git仓库信息：](#修改git仓库信息)
    - [删除remote记录：](#删除remote记录)
    - [`git init`创建非master的分支名：](#git-init创建非master的分支名)
  - [协同工作时可能出现的问题及解决方案：](#协同工作时可能出现的问题及解决方案)
  - [git 和 github、gitlab 的区别：](#git-和-githubgitlab-的区别)
  - [git clone 和 git pull 的区别：(含部分 git fetch讲解)](#git-clone-和-git-pull-的区别含部分-git-fetch讲解)
  - [查看当前文件夹对应的远程仓库链接:](#查看当前文件夹对应的远程仓库链接)
  - [查看分支：](#查看分支)
  - [git如何放弃当前分支上一次提交到现在的所有修改，自上一次提交到现在，我还没有commit过。](#git如何放弃当前分支上一次提交到现在的所有修改自上一次提交到现在我还没有commit过)
  - [我想在当前git仓库回退到上一个版本，且不丢失现在的更改，应该怎么做呢？](#我想在当前git仓库回退到上一个版本且不丢失现在的更改应该怎么做呢)
    - [使用git stash：](#使用git-stash)
    - [使用新的分支:](#使用新的分支)
  - [为什么我把要忽略的内容写入了gitignore，git push时还是把gitignore中的内容上传了？是有什么操作顺序吗？](#为什么我把要忽略的内容写入了gitignoregit-push时还是把gitignore中的内容上传了是有什么操作顺序吗)
    - [原因：](#原因)
    - [解决方案：](#解决方案)
  - [git pull 提示以下信息该怎么做：](#git-pull-提示以下信息该怎么做)

## git安装：
要使用git指令，首先要确保Ubuntu上安装了Git。你可以在终端中运行以下命令检查是否已安装Git：<br>

```bash
git --version
```

如果尚未安装，可以使用以下命令安装Git：<br>

```bash
sudo apt update
sudo apt install git
```

🧜‍♂️🧜‍♂️🧜‍♂️注意：`git` 命令只能在 `git` 仓库中使用（除了 `git init` 初始化命令），`git` 仓库外无法使用 `git` 指令。<br>


接下来，您可以按照以下步骤将文件夹变成Git仓库：

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

请注意，现在你只是在本地操作，还无法将你的操作同步到远程仓库(github或gitlab平台)。如果要同步需要用到 `git push` 将本地代码推送到远程，但使用 `git push` 前需要首先配置一些基本信息。<br>

## 设置git仓库信息：
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

git仓库允许一个仓库配置多个远程链接，方便在`git push`的时候同时推送到多个远程仓库，但不允许出现相同的远程仓库名称，例如你已经有了一个`origin`，就不能在当前git仓库再添加一个名为`origin`的远程仓库。<br>

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


## git分支：
git分支，每次commit是一个树的节点，可以将不同的分支合并。<br>

Git分支是Git版本控制系统中的一个重要概念，Git分支是树🌲结构，它允许你在代码库中创建不同的分支，以便并行开发、测试和管理代码的不同版本。分支可以帮助开发团队更有效地协作，同时保持代码的稳定性。
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/5ccf44ce-a66b-46ff-9261-16d5aa58fba3" alt="image" width="70%" height="70%">

### 分支创建：

1. 打开终端，并进入Git仓库所在的目录。

2. 使用以下命令来创建并切换到新分支，其中`branch_new`是创建的新分支的名称：
```shell
git checkout -b branch_new
```

或者在较新版本的Git中使用：<br>
```shell
git switch -c branch_new
```

3. 现在，你已经在名为`branch_new`的新分支上，可以通过以下指令确认：
```bash
git branch -a
```


### 修改分支名称：

🚨🚨🚨注意：在执行以下步骤之前，请确保您的Git版本在2.28.0或更高版本，因为较早的版本可能不支持更改默认分支名称。<br>

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


## 修改git仓库信息：
我们在使用git时，可能会由于各种情况需要修改git仓库的信息，这里就讲述下修改常见信息的方式：<br>

### 删除remote记录：
git仓库允许一个仓库配置多个远程链接，方便在`git push`的时候同时推送到多个远程仓库。<br>

回想一下，我在介绍设置remote的时候提到过，`origin`是远程仓库名称，我们通过远程仓库名称删除remote记录。假设我们要删除名为`origin`的远程仓库:<br>
```log
git remote remove origin
```

假设我们要删除名为`master`的远程仓库:<br>
```log
git remote remove master
```

如果你忘记了自己定义的远程仓库名称，可以通过以下指令查看：<br>
```bash
git remote -v
```

### `git init`创建非master的分支名：
Git 2.28.0版本前，使用 `git init` 创建git仓库时，默认生成的分支名为"master"。Git 2.28.0版本引入了一个新的默认分支名称，称为"main"。<br>


不过，你可以根据需要重命名默认分支，或者使用其他分支名称来初始化仓库，具体操作取决于你的偏好和需求。例如，你可以使用以下命令初始化一个仓库并指定不同的默认分支名称：<br>

```bash
git init --initial-branch=yourbranchname
```

这将创建一个新的Git仓库并将默认分支设置为"yourbranchname"。<br>




## 协同工作时可能出现的问题及解决方案：
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


3. **解决冲突（如果有）：** 如果你和你的同事都在相同的文件或部分进行了更改，可能会发生冲突。Git 会在拉取过程中提示你解决冲突。你需要手动解决这些冲突，并在文件中选择你想要保留的更改。一旦冲突解决完毕，你可以使用以下命令将更改标记为已解决：

```bash
git add 冲突文件名
```

现在，已经同步了"同事B"的操作，也解决了冲突，接下来继续自己的工作，工作完成后正常`commit`和`push`就行。<br>


## git 和 github、gitlab 的区别：
git 是一个版本控制软件，github 是一个代码托管平台。github 或 gitlab 可以使用 git 进行代码的版本控制，可以执行修改代码、切换分支、查看不同代码版本、分享代码、提交bug等操作。

## git clone 和 git pull 的区别：(含部分 git fetch讲解)
从字面意思也可以理解，都是往下拉代码，git clone是克隆，git pull 是拉取。
但是，也有区别：
从远程服务器克隆一个一模一样的版本库到本地,复制的是整个版本库，叫做 clone 。（clone是将一个库复制到你的本地，是一个本地从无到有的过程。）
从远程服务器拉取到一个branch分支的更新到本地，并更新本地库，叫做 pull 。
git pull 是从远程获取最新版本并merge（合并）到本地，更安全一些。
git pull 相当于 git fetch（拉取代码） + git merge /  git rebase (将提交应用到当前分支)。


## 查看当前文件夹对应的远程仓库链接:
```shell
git remote -v
```

## 查看分支：
查看当前所在分支：<br>
> 终端会直接输出当前所在分支名称。

```bash
git branch --show-current
```

查看自己所在的分支与所有分支(包含git远程仓库的分支)？

查看分支的指令有很多，只有以下指令会显示 **包括git远程仓库分支的所有分支：**<br>
```shell
git branch -a
```

## git如何放弃当前分支上一次提交到现在的所有修改，自上一次提交到现在，我还没有commit过。
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

## 我想在当前git仓库回退到上一个版本，且不丢失现在的更改，应该怎么做呢？
如果你想在当前git仓库回退到上一个版本，但同时不丢失现在的更改，你可以使用以下的方法：<br>

### 使用git stash：
这是一个常用的方法，它允许你暂时保存当前的更改，并在需要时重新应用它们。<br>
```shell
git stash              # 暂存当前更改
git reset --hard HEAD^ # 回退到上一个版本
git stash pop          # 重新应用暂存的更改
```

### 使用新的分支:
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

## 为什么我把要忽略的内容写入了gitignore，git push时还是把gitignore中的内容上传了？是有什么操作顺序吗？
### 原因：
使用 `.gitignore` 文件可以指定要忽略的文件和文件夹，以防止它们被 `Git` 追踪和上传到版本控制系统中。然而，有几个注意事项需要牢记：<br>

`.gitignore` 文件🥶🥶🥶**只对尚未被Git追踪的文件生效**🥶🥶🥶，对已经被Git追踪的文件无效。如果你已经将某些文件提交到了仓库中，然后再将这些文件添加到.gitignore文件中，Git仍然会追踪它们。<br>

如果你已经将某个文件添加到了Git的缓冲区（即使用了"git add"命令），然后将其添加到 `.gitignore` 文件中，这个文件仍然会被Git追踪。<br>
你需要使用"git rm --cached 文件名"命令将其从缓冲区移除。<br>
```shell
git rm --cached 文件名
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

## git pull 提示以下信息该怎么做：
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
你正处于一个合并冲突的状态，并且Git已经打开了一个文本编辑器（在这里是`nano`）让你输入合并提交的信息。<br>

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

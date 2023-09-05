# Git
- [Git](#git)
  - [声明：](#声明)
  - [git 和 github、gitlab 的区别：](#git-和-githubgitlab-的区别)
  - [git如何查看自己本地文件夹对应的是哪个远程仓库？](#git如何查看自己本地文件夹对应的是哪个远程仓库)
  - [git如何查看自己所在的分支与所有分支(包含git远程仓库的分支)？](#git如何查看自己所在的分支与所有分支包含git远程仓库的分支)
  - [git如何放弃当前分支上一次提交到现在的所有修改，自上一次提交到现在，我还没有commit过。](#git如何放弃当前分支上一次提交到现在的所有修改自上一次提交到现在我还没有commit过)
  - [我想在当前git仓库回退到上一个版本，且不丢失现在的更改，应该怎么做呢？](#我想在当前git仓库回退到上一个版本且不丢失现在的更改应该怎么做呢)
    - [使用git stash：](#使用git-stash)
    - [使用新的分支:](#使用新的分支)
  - [为什么我把要忽略的内容写入了gitignore，git push时还是把gitignore中的内容上传了？是有什么操作顺序吗？](#为什么我把要忽略的内容写入了gitignoregit-push时还是把gitignore中的内容上传了是有什么操作顺序吗)
    - [原因：](#原因)
    - [解决方案：](#解决方案)
  - [git pull 提示以下信息该怎么做：](#git-pull-提示以下信息该怎么做)

## 声明：
因 git 的作为工具的特性，将 git 置于特定场景下更便于理解 git 的使用，所以本篇教程采用🧜‍♂️🧜‍♂️🧜‍♂️**场景**🧜‍♂️🧜‍♂️🧜‍♂️的形式介绍 git 的使用。

## git 和 github、gitlab 的区别：
git 是一个版本控制软件，github 是一个代码托管平台。github 或 gitlab 可以使用 git 进行代码的版本控制，可以执行修改代码、切换分支、查看不同代码版本、分享代码、提交bug等操作。

## git如何查看自己本地文件夹对应的是哪个远程仓库？
```shell
git remote -v
```

## git如何查看自己所在的分支与所有分支(包含git远程仓库的分支)？
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
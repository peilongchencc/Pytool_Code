# Git常见场景运用：
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
  - [一个项目向github和gitee推送步骤:](#一个项目向github和gitee推送步骤)
    - [前提条件:](#前提条件)
    - [将main分支上传到github:](#将main分支上传到github)
    - [在main分支基础上创建master分支并上传到gitee:](#在main分支基础上创建master分支并上传到gitee)

## 协同工作时，你当前所在的分支被其他人更新，你需要拉取最新的内容再接着自己的工作：

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

### git pull 让你选择分支合并方式：

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

### git pull 让你输入合并提交信息：

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


## 协同工作时，你在git分支C上工作，但领导突然让你解决分支B的bug，解决完bug，提交分支B后，再完成分支C的工作：

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


## git如何放弃当前分支上一次提交到现在的所有修改，自上一次提交到现在，你还没有commit过。

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

## 你想在当前git仓库回退到上一个版本，且不丢失现在的更改，应该怎么做呢？

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

## 将git仓库下某个文件夹复制到其他目录，修改好后提交到远程仓库的操作流程：

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


## 一个项目向github和gitee推送步骤:

### 前提条件:

查看分支信息:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/baidu-hot-search-crawling-code# git branch -a
* main
  remotes/github/main
  remotes/origin/HEAD -> origin/master
  remotes/origin/develop
  remotes/origin/master
```

查看远程仓库信息:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/baidu-hot-search-crawling-code# git remote -v
github  git@github.com:peilongchencc/baidu_hot_search.git (fetch)
github  git@github.com:peilongchencc/baidu_hot_search.git (push)
origin  git@gitee.com:beijing-zhixing-qiming/baidu-hot-search-crawling-code.git (fetch)
origin  git@gitee.com:beijing-zhixing-qiming/baidu-hot-search-crawling-code.git (push)
```

### 将main分支上传到github:

1. 拉取main分支的远程改动:

```bash
git pull github main
```

2. 作出自己的代码改动。

3. 代码改好后，提交代码:

```bash
git push github main
```

### 在main分支基础上创建master分支并上传到gitee:

1. 以main分支为基底，创建新分支:

```bash
git branch -b master
```

github的默认分支是main，gitee的默认分支是master。笔者不想要修改分支名，所以重新创建了个master分支。<br>

2. 拉取远程仓库对应代码:

```bash
git pull origin master
```

3. 可能会出现冲突，进入"变基"模式:

如果你此时查看分支信息，显示如下:<br>

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/baidu-hot-search-crawling-code# git branch -a
* (no branch, rebasing master)
  main
  master
  remotes/github/main
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/baidu-hot-search-crawling-code# git checkout main
.gitignore: needs merge
error: you need to resolve your current index first
```

4. 查看冲突:

```bash
git status
```

```log
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/baidu-hot-search-crawling-code# git status
interactive rebase in progress; onto b8c4bf5
Last command done (1 command done):
   pick 2a7f505 Initial commit
Next commands to do (3 remaining commands):
   pick 36d7594 清空初始文件
   pick b3b7188 百度热搜项目提交
  (use "git rebase --edit-todo" to view and edit)
You are currently rebasing branch 'master' on 'b8c4bf5'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
        both added:      .gitignore
        both added:      README.md

no changes added to commit (use "git add" and/or "git commit -a")
(base) root@iZ2zea5v77oawjy2qz7c20Z:/data/baidu-hot-search-crawling-code# 
```

5. 解决合并冲突:

- **检查冲突文件**：使用编辑器打开冲突文件，您将看到像这样的冲突标记：

   ```
   <<<<<<< HEAD
   [当前分支的版本]
   =======
   [远程分支的版本]
   >>>>>>> [commit ID]
   ```

修改文件，解决冲突，然后保存。<br>

- **标记冲突已解决**：解决完每个冲突后，使用命令 `git add <文件名>` 来标记为已解决。

- **继续或中止 rebase**：解决所有冲突后，可以通过 `git rebase --continue` 继续 rebase 过程。如果遇到困难或想取消整个过程，可以用 `git rebase --abort` 返回到 rebase 之前的状态。

处理这类情况需要细心，确保正确解决所有冲突，以防丢失重要的代码修改。<br>

6. 推送到远程分支:

冲突解决后，检查下没有问题了，就可以使用下列代码进行推送了。<br>

```bash
git push origin master
```
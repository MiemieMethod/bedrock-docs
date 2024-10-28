---
title: 版本控制
mentions:
    - SirLich
    - sermah
description: 控制附加包文件的更改。
---

版本控制是一个逐步备份代码的概念，这样您可以根据需要回滚到特定版本。最基本的版本控制可以通过每天（或每个版本）将您的附加包打包成一个 `.zip` 文件并上传到 Google Drive（或本地保存）来实现。这并不不合理，但它有三个主要的困难，而适当的版本控制系统（VCS）可以解决这些问题：

-   比较版本并不容易
-   实际回滚到之前的版本并不容易
-   对团队协作没有帮助

本教程将教您一个名为 `git` 的工具的基础知识，以及一个免费的在线 git 存储服务 `GitHub`。任何人都可以跟随，但如果您在团队环境中工作或经常因为忘记备份而丢失工作，您将获得最大的收益。

本教程不会直接教授 `git` 或 `GitHub`，因为外部知识来源更适合这样做。重点将是学习基础知识后，如何为 Minecraft 设置这些工具。

## Git

`git` 是一个安装在您计算机上的工具，允许您对文件进行版本控制。您可以使用简短的消息（例如：“修复了龙被驯服后无法飞行的问题”）提交对文件的更改，查看完整的更改列表，并快速跳回特定的更改。

Git 功能强大，是所有主要编程项目的事实标准工具。对于 Minecraft 工作来说，最大的缺点是它 _复杂_。学习时请保持耐心。

要获取 `git` 的完整教程，您可以参考以下 [git 教程。](https://www.atlassian.com/git/tutorials/what-is-git)

## GitHub

GitHub 是您 git 项目的一个版本（`repository`），托管在网上。这允许多个人同时在同一个项目上工作并进行协作。这对于地图制作非常有帮助。通过在 GitHub 上托管，您还可以（可选）将代码公开，使与世界分享您的附加包变得更加容易。

要获取使用 `GitHub` 的完整教程，您可以参考这个 [github 教程](https://guides.github.com/activities/hello-world/)。

## 词汇测验

如果您已经读到这里，希望您有一个 GitHub 账户，并对 `git` 有一些了解。本教程将使用以下术语。如果您不认识这些术语，请自行搜索 :)

-   repository
-   branch
-   commit
-   github
-   git

## 设置 Git

这假设您正在将一个 _现有_ 项目添加到 git。如果您是从头开始，步骤是类似的。

### 结构

使用 `git` 进行附加包开发的一个主要问题是，`git` 通常通过封装一个 _单一_ 文件夹来管理它。当然，在基岩附加包中，资源分散在两个文件夹中：`BP` 和 `RP`。为了解决这个问题，我们将把我们的仓库完全放在 `com.mojang` 文件夹之外，然后使用 Windows 的 `junctions` 来“复制”这些文件夹。

将项目放在单独位置有许多优点：

-   我们可以根据需要包含其他文件，例如配置文件、工具、笔记、.bb 文件等
-   我们可以将 RP 和 BP 合并为一个仓库
-   我们的所有项目可以在一个简单的位置轻松查看，而不是嵌套在 com.mojang 中

### 创建 Git 仓库

选择一个方便的项目位置。我将我的放在 `C:/sirlich/projects`。创建一个以您的地图命名的新文件夹。我们将使用 `wiki` 作为我们的模拟项目名称。

右键单击该文件夹，然后点击“打开 git Bash”。如果此选项未出现，您可以从开始菜单打开 `git bash` 并导航到您的项目文件夹。如果您尚未安装 `git bash`，请现在安装。

输入：`git init`。这将在您的项目中创建一个空的仓库。

### 链接您的现有 RP 和 BP

下一步是让仓库知道您的 RP 和 BP 文件夹。我们将使用 Windows 的符号链接“junctions”。当我们创建一个 junction 时，我们实际上是在文件系统中创建一个虫洞，使您的文件看起来像同时存在于两个地方。删除/编辑/添加文件会完美地复制过来。

输入：`mklink /J wiki_RP "C:/path/to/RP/in/com/mojang"`
输入：`mklink /J wiki_BP "C:/path/to/BP/in/com/mojang"`

完成后，您应该在项目文件夹中看到 `wiki_RP` 和 `wiki_BP`，其中包含您所有的资源、现有文件等。

您现在可以将此仓库推送到 `github`，按照上面的教程进行操作。

### 额外文件

由于我们基于符号链接创建了仓库，我们可以在项目文件夹中添加任何我们喜欢的内容，而无需担心破坏 com.mojang 文件夹。我喜欢跟踪 `.bb` 文件、封面艺术文件（`.kra` 等）。

您还可以添加笔记、视频文件或任何其他您想跟踪的内容。

### 使用您的 VCS

在使用 VCS 时需要记住的主要事项：

-   开始工作前始终 `pull`
-   经常提交并 `push`
-   停止工作前始终 `push`
-   如果您的文件损坏得很严重，您可以随时重置到最后一个工作版本。如果您经常提交/推送，希望这不是太久之前的事情。
-   始终，我指的是 `始终`，写好提交信息。当您需要回滚时，这一点至关重要。
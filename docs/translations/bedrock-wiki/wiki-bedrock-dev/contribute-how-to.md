---
title: 如何贡献
hidden: true
mentions:
    - TheItsNameless
    - QuazChick
description: 进行你的第一次贡献！
---

## 关于本指南

本指南将引导你如何开始编辑维基。虽然可以在GitHub网站上“就地”编辑维基，但本指南将教你正确的技巧。这是一项有价值且可转移的技能，将为你提供超越仅仅编辑维基的额外知识。

本文将教你如何使用GitHub Desktop，这是管理本地仓库的最简单方法。虽然可以仅使用Git来完成此操作，但这比使用GitHub Desktop更为复杂，本指南将不涵盖此内容。

如果你已经了解本指南中涵盖的一些步骤，可以随时使用右侧的目录跳到你不熟悉的部分！

如果你想了解更多关于我们华丽的样式功能，请继续阅读我们的[贡献样式指南](/contribute-style)。

## 编辑维基的步骤

要编辑维基，你需要遵循5个主要步骤（下载和设置软件只需在第一次时进行）：

1. 复制仓库
2. 克隆仓库
3. 编辑维基
4. 提交本地更改并与GitHub同步
5. 创建拉取请求

如果你第一次看到这些步骤，可能会觉得有些压倒，但别担心！这非常简单，我们会一步一步引导你。

## 设置软件

要编辑我们的维基，你需要下载并安装以下软件：

- GitHub Desktop
- NodeJS
- Visual Studio Code

如果你想更频繁地编辑维基，可能想开始使用Git，因为它比GitHub Desktop更强大。但别担心，GitHub Desktop对我们来说已经足够了！

### Visual Studio Code

[Visual Studio Code (VSCode)](https://code.visualstudio.com/Download) 是一个很好的环境，用于编辑所有文件、编写代码等。你也可以使用其他编辑器，但在本教程中我们将指导你安装VSCode。

![](/assets/images/contribute/setting_up_software/vscode/vsc_download.png)

#### 安装

前往你保存.exe文件的文件夹，双击它。安装窗口将打开。大多数情况下，你可以点击`下一步`，只需确保在“附加任务”窗口中选择`添加到PATH`。

在最后一页，点击`安装`。

安装完成后，点击`完成`。VSCode现在应该启动。如果没有启动，请手动打开它。

现在你可以自定义VSCode的外观。如果你完成了或不想自定义，点击“下一部分”。

<WikiImage src="/assets/images/contribute/setting_up_software/vscode/vsc_look.png" width="210" />

现在你可以学习一些VSCode的基础知识。如前所述，如果你完成了，点击“下一部分”。

<WikiImage
    src="/assets/images/contribute/setting_up_software/vscode/vsc_fundamentals.png"
    width="210"
/>

在最后一页，如前所述，如果你准备好了，点击“标记完成”。

<WikiImage
    src="/assets/images/contribute/setting_up_software/vscode/vsc_productivity.png"
    width="210"
/>

我们已经完成了VSCode的安装。现在可以关闭它。

### GitHub Desktop

[GitHub Desktop](https://desktop.github.com) 用于下载GitHub仓库，以便你可以在本地编辑它们。你也可以使用Git，一个命令行工具来完成此操作，但这有点复杂，本教程将不涵盖此内容。

![](/assets/images/contribute/setting_up_software/ghdesktop/ghd_download.png)

#### 安装

如前所述，前往你保存.exe文件的文件夹，双击它。安装程序将打开并自动安装GitHub Desktop。完成后，GitHub Desktop将自动启动。

<WikiImage
    src="/assets/images/contribute/setting_up_software/ghdesktop/ghd_install.png"
    width="210"
/>

接下来，它会要求你登录。如果你已经有GitHub账户，点击`登录到GitHub.com`。在浏览器标签中，登录你的账户。如果你没有GitHub账户，点击`创建你的免费账户`并创建一个账户。然后正常继续。

![](/assets/images/contribute/setting_up_software/ghdesktop/ghd_login.png)

现在在GitHub Desktop中，不要更改任何内容，点击“完成”。

![](/assets/images/contribute/setting_up_software/ghdesktop/ghd_configure.png)

现在，你可以关闭GitHub Desktop。

### NodeJS

通过[NodeJS](https://www.nodejs.org)，我们可以在本地查看维基，就像它在网络上显示的一样。这非常适合在推送之前发现拼写错误或错误，以免在合并时出现问题。

![](/assets/images/contribute/setting_up_software/nodejs/njs_download.png)

#### 安装

现在，再次前往你的下载文件夹，双击NodeJS安装文件。对于我们的安装，你不需要更改任何内容。只需确保不添加`本地模块工具`，因为我们不需要它们。在最后一页，点击`安装`。等待安装完成并点击`完成`。

## 设置你的本地环境

现在我们已经安装了所有必要的软件，可以开始为维基做贡献。首先，我们需要设置本地工作环境。别担心，这非常简单。只需按照以下步骤操作：

打开我们的[GitHub仓库](https://github.com/Bedrock-OSS/bedrock-wiki)，点击`复制`。如果你已经复制过了，没问题！继续下面的步骤。

![](/assets/images/contribute/setting_up_local/setup_fork.png)

打开GitHub Desktop，点击`从互联网克隆仓库`。

![](/assets/images/contribute/setting_up_local/setup_clone.png)

现在选择你的复制，并点击“克隆”。你的仓库将自动被克隆。

![](/assets/images/contribute/setting_up_local/setup_clone_2.png)

之后，你将看到克隆的概览。要在其上工作，只需点击“在Visual Studio Code中打开”。VSCode将自动打开我们的维基。如果VSCode询问是否信任该文件夹，请点击`是，我信任作者`。

![](/assets/images/contribute/setting_up_local/setup_vsc.png)

现在你已经成功将维基克隆到本地设备，可以编辑所有文件！

## 提交你的更改

一旦你完成了维基的工作，现在可以直接将你的更改提交并推送到我们的仓库！

切换到GitHub Desktop，你应该能看到你的更改。如果看不到，请确保你已保存文件并在GitHub Desktop中打开了正确的仓库。

确认在GitHub Desktop中的更改后，你可以给你的提交命名和描述（但两者都不是必需的），然后点击`提交到主分支`。

![](/assets/images/contribute/committing_changes/committing.png)

提交更改后，你需要将本地克隆推送到GitHub。只需点击`推送提交到原始远程`。

![](/assets/images/contribute/committing_changes/committing_push.png)

GitHub现在将你的本地克隆发送到他们的服务器。

## 创建拉取请求

现在GitHub已经在他们的服务器上有了你的编辑，你需要创建一个“拉取请求”（PR），以便我们可以合并你的更改。

有很多方法可以做到这一点。现在，只需在GitHub Desktop中点击`创建拉取请求`。

![](/assets/images/contribute/creating_pr/pr.png)

GitHub Desktop将在浏览器中打开你的PR。你可以编辑你的PR，但不需要。所有内容应该已经正确并足够我们合并。只需点击`创建拉取请求`。

![](/assets/images/contribute/creating_pr/pr_2.png)

你完成了！现在轮到我们将你的更改合并到我们的维基中！

## 更新本地环境

由于你不是唯一在维基上工作的人，可能会有一些更改你在本地克隆中没有。要更新你的本地克隆，你需要更新你的复制。别担心，这非常简单！

在浏览器中打开GitHub，打开你的复制。你会看到一个字段，显示你已过期。只需点击`获取上游`，然后点击`获取并合并`。

![](/assets/images/contribute/updating_local/updating.png)

现在在GitHub Desktop中，你需要通过点击`拉取原始`来拉取更新。你的本地克隆应该会自动更新。

![](/assets/images/contribute/updating_local/updating_pull.png)

你的本地克隆现在已是最新的！

### 故障排除

每当其他人更新我们的维基时，都需要执行此过程。如果你忘记这样做，可能会遇到一些问题，例如我们无法自动合并你的PR（当你尝试打开PR时会看到这个问题）。

![](/assets/images/contribute/troubleshooting/merge/merge_merge.png)

如果发生这种情况，别担心。你可以轻松解决这个问题。

#### 修复它

像我们在前一步中所做的那样更新你的复制。之后，你不能直接在GitHub Desktop中拉取更改到你的本地克隆，因为这会导致问题。相反，点击`当前分支`。

![](/assets/images/contribute/troubleshooting/merge/merge_branch.png)

现在点击`选择一个分支进行合并...`。

<WikiImage
    src="/assets/images/contribute/troubleshooting/merge/merge_choose_branch.png"
    width="250"
/>

选择默认分支（它应该已经被选中），然后点击`创建合并提交`。

<WikiImage src="/assets/images/contribute/troubleshooting/merge/merge_commit.png" width="260" />

现在在VSCode中打开。

![](/assets/images/contribute/troubleshooting/merge/merge_open.png)

点击`接受当前更改`，因为你希望更新你的更改，而不是其他人的。此步骤必须针对每个存在的问题执行。如果你不对每个问题执行此操作，我们将无法合并你的PR。

![](/assets/images/contribute/troubleshooting/merge/merge_accept.png)

否则，你可以选择`接受传入更改`以接受其他人所做的更改。然后保存并返回GitHub Desktop。然后你只需点击`继续合并`。

![](/assets/images/contribute/troubleshooting/merge/merge_continue.png)

现在这个问题已解决！你可以安全地继续，提交到你的分支并创建一个PR。

## 结论

现在你已经安装了所有软件，并学习了编辑我们维基所需的所有技能！如果你想了解更多关于样式化你的文章，请阅读我们的指南

<Button link="/contribute-style">如何编辑我们维基上的页面</Button>
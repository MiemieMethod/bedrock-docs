---
标题: Minecraft Beta - 1.16.210.60 (Xbox One/Windows 10/Android)
日期: 2021-02-18T13:46:12Z
更新: 2021-02-18T16:42:07Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360057279331-Minecraft-Beta-1-16-210-60-Xbox-One-Windows-10-Android
哈希:
  update-on-experimental-features: update-onexperimental-features
  technical-fixes-and-changes: technicalfixes-andchanges
---

**在参与Minecraft Beta之前，请阅读以下内容：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**2021年2月18日**

## **关于实验性功能的更新：**

与任何实验一样，事情并不总是如我们所预期的那样！在对发光鱿鱼及其相关功能进行测试时，我们不幸发现了一个问题，导致游戏崩溃的频率远高于我们希望的，因此我们将暂停发光鱿鱼的相关内容，直到解决这些问题。**在本周的测试版中，发光鱿鱼及其相关物品，如发光物品展示框和可染色告示牌已被移除，但我们会很快将它们带回来！**

**这对我已经使用这些功能的世界意味着什么？**

- 包含发光鱿鱼相关物品的箱子 - 新物品从箱子中消失，常规物品不受影响
- 染色告示牌 - 文本上的颜色消失，文本变回黑色
- 应用发光效果和颜色的告示牌 - 告示牌上的文本停止发光，颜色被移除
- 发光鱿鱼 - 游戏中不再出现
- 发光物品展示框 - 变为占位符方块，并显示内容错误，指向'minecraft:glow_frame'

## **漏洞修复**

**性能和稳定性**

- 修复了加载包含幽匿感测体的结构块时可能发生的崩溃（[MCPE-115443](https://bugs.mojang.com/browse/MCPE-115443)）
- 修复了与告示牌交互时可能发生的崩溃（[MCPE-117513](https://bugs.mojang.com/browse/MCPE-117513)）

**常规**

- 将连接时选择是否下载资源包的时间限制从5秒提高到5分钟

**新用户界面**

- 新的成就界面现在默认启用（在VR、PS4或启用旁白的触控设备上除外）

**多人游戏**

- 当您从添加成员界面返回时，游戏内邀请界面现在将刷新

**角色创建器**

- 修复了在应用程序超出上下文时角色创建器的更改丢失的漏洞
- 修复了从“经典皮肤”标签切换到“角色创建器”标签后，按Tab键将导致装备经典皮肤而非角色创建器角色的漏洞
- 如果打开更衣室时没有有效角色，将创建一个新角色

## **技术修复和更改**

**GameTest框架**

- 添加了GameTest框架 **注意：** GameTest在控制台平台上不可用
  - GameTest是一个基于将测试代码与测试结构配对的服务器端测试自动化工具。您可以在为世界启用“启用GameTest框架”实验开关后，通过/gametest命令触发测试

**Android设备**

- 我们对KitKat操作系统或更早版本的Android设备的支持即将结束。有关更多信息，请查看我们的[帮助文章](https://help.minecraft.net/hc/en-us/articles/360045863292-What-are-the-Device-Requirements-to-run-Minecraft-) ，该文章将在更改更广泛推出时进行更新。
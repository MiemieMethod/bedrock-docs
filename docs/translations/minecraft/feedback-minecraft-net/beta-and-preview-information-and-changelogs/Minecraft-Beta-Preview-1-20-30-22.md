---
标题: Minecraft Beta & Preview - 1.20.30.22
日期: 2023-08-17T14:05:41Z
更新: 2023-08-17T14:18:03Z
分类: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/18619357250701-Minecraft-Beta-Preview-1-20-30-22
哈希:
  01H81X5SYBVY1Z7HY8NGCMCQT8: 特性与漏洞修复
  01H81X5SYBGK6777W0X1SD72CM: 更新后的游戏界面
  01H81XGKBVBKQZFVC5BTFVSJNA: 方块
  01H81XGKBV3VRE86D1CSRA6PK1: 稳定性与性能
  01H81XGKBV3ZKD60YK24ADEEB8: 用户界面
  01H81XGKBVYYW10CG5E779B2PQ: 语音合成功能
  01H81XGKBVG56FVRXMV4YP1157: 命令
  01H81XGQT9Q0MG8YS6E2GGHF4W: 游戏规则
  01H81XGTGCD4HVMFJFHTFN8CPE: 游戏玩法
  01H81XGKBV3SM618TT29BDZW84: 技术更新
  01H81XGKBVFW1ZJ6JY5BTDRVNJ: 编辑器
  01H81XGKBVA89420WW9QC5VTEX: 物品
  01H81XGKBVZTZ9WD8X8E725740: 实验性技术特性
  01H81XGKBVW7BJKBXEWZ9PM0XB: API
  01H81XGKBV57RWGBC9FJK20MTC: 图形

**发布时间:** 2023年8月17日

**关于Minecraft预览和Beta的信息:**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量。
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)。
- Beta版可在Android（Google Play）上使用。要加入或退出Beta，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 的详细说明。

![一张Minecraft的截图，展示了校频幽匿感测体和红石为红石灯供电的场景。场景设定在夜晚的樱花树林中。](https://feedback.minecraft.net/hc/article_attachments/18619365356813)

我们在本周的Minecraft预览中准备了一些修复和调整。请在* [bugs.mojang.com](http://bugs.mojang.com/) 上报告并点赞您遇到的任何漏洞，并享受更新！

**关于1.20.20的更新**  
感谢所有参与1.20.20.xx Minecraft预览和Beta的玩家！我们准备了许多令人兴奋的修复和特性，但还没有准备好向所有人发布。因此，我们将继续进行1.20.30.xx预览和Beta，当我们准备好时，将会有一个稍微比平常更大的综合更新。如果您想了解更多即将推出的内容，可以在[这里](https://feedback.minecraft.net/hc/en-us/sections/360001185332)查看所有最近的更新日志。感谢您的耐心等待！

# **特性与漏洞修复**

## **更新后的游戏界面**

**![Minecraft更新后的游戏界面截图](https://feedback.minecraft.net/hc/article_attachments/18619725686029)**

- 游戏界面正在更新，改进了导航、响应式世界组件以及全新的外观和感觉。
- 朋友标签和领域标签现在分开，以便更清晰地分隔功能。
- 创建新世界流程和从模板创建流程也已分开，以便更清晰地进入游戏。
- 游戏界面的工作仍在进行中，因为还有一些功能缺失，但我们非常希望听到您的反馈，欢迎访问 [aka.ms/MinecraftPlayScreens](https://aka.ms/MinecraftPlayScreens)。

## **方块**

- 校频幽匿感测体的紫水晶现在在其活跃阶段与方块的其他部分一起发光 ([MCPE-168813](https://bugs.mojang.com/browse/MCPE-168813)) ([MCPE-169953](https://bugs.mojang.com/browse/MCPE-169953))。
- 使用命令放置的悬挂式告示牌现在具有正确的击中箱 ([MCPE-163456](https://bugs.mojang.com/browse/MCPE-163456))。
- “stained_hardened_clay”方块现在被拆分为独特的实例，即“white_terracotta”、“orange_terracotta”、“magenta_terracotta”、“light_blue_terracotta”、“yellow_terracotta”、“lime_terracotta”、“pink_terracotta”、“gray_terracotta”、“light_gray_terracotta”、“cyan_terracotta”、“purple_terracotta”、“blue_terracotta”、“brown_terracotta”、“green_terracotta”、“red_terracotta”和“black_terracotta”。
  - 命令仍然可以使用“stained_hardened_clay”，但在命令提示中不会建议“stained_hardened_clay”，而是会建议新的名称。
- 第三人称相机不再穿透堆肥桶的下部 ([MCPE-171213](https://bugs.mojang.com/browse/MCPE-171213))。

## **稳定性与性能**

- 修复了基岩专用服务器在加载区块时的内存泄漏 ([BDS-17527](https://bugs.mojang.com/browse/BDS-17527))。

## **用户界面**

- 修复了Android上Joy-Con和Switch Pro控制器的ZL/ZR图标。
- 可以通过点击或鼠标点击重新定位文本框中的光标 ([MCPE-131572](https://bugs.mojang.com/browse/MCPE-131572))。
- 用户界面中的“暂停菜单”已更名为“游戏菜单”。
- 修复了导致地下渐变效果覆盖所有其他HUD元素的分层问题 ([MCPE-159217](https://bugs.mojang.com/browse/MCPE-159217))。

## **语音合成功能**

- 语音合成复述功能现在将朗读安全区域菜单中的指令文本以及确认按钮。

## **命令**

- 在被扁平化之前具有别名的方块现在可以在命令中正确引用。

## **游戏规则**

- 将“recipes unlock”游戏规则更改为默认启用。这意味着在创建新世界时，配方解锁将默认启用，但仍可以在高级设置中关闭。现有世界不受此更改影响。

## **游戏玩法**

- 弩在射击时会损失耐久，而不是在拉弦时 ([MCPE-46490](https://bugs.mojang.com/browse/MCPE-46490))。

# **技术更新**

## **编辑器**

编辑器及其对应的API处于早期开发阶段，并可在Windows PC基岩预览版构建中使用键盘/鼠标。请在社交媒体上标记我们，使用**\#BedrockEditor**。

了解[如何使用](https://aka.ms/LearnEditor)编辑器，加入[GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions)论坛与团队互动，并通过[入门工具包](https://github.com/Mojang/minecraft-editor-extension-starter-kit)和[示例](https://github.com/Mojang/minecraft-editor-extension-samples)开始构建扩展。

本周的修复：

- 对工具模式中的重新加载按钮进行了小幅更新，以重新加载脚本和刷新用户界面。
- IPropertyPane
  - 添加了属性*collapsed*以检查面板是否展开或折叠。
  - 添加了函数*collapse*和*expand*以控制*collapsed*状态。

## **物品**

- 在1.20.30及更高版本的json格式中发布了“minecraft:food”物品组件，退出实验性阶段。
- 在1.20.30及更高版本的json格式中添加了“minecraft:interact_button”物品组件，以启用并设置交互按钮的文本。

# **实验性技术特性**

## **API**

- 修复了使用*defineProperty*重新定义原型属性的问题 ([MCPE-174073](https://bugs.mojang.com/browse/MCPE-174073))。
- ItemStack
  - 添加了*getCanPlaceOn()*和*getCanDestroy()*。
  - 为*amount*属性添加了255的上限 - 超过将抛出错误。
- Entity
  - 添加函数*getProperty(identifier: string): boolean \| number \| string \| undefined* - 获取实体属性。
  - 添加函数*setProperty(identifier: string, value: boolean \| number \| string): void* - 在下一个刻设置实体属性。
  - 添加函数*resetProperty(identifier: string): boolean \| number \| string;* - 在下一个刻将实体属性重置为默认值并返回默认值。
- beforeEvents
  - 添加事件/属性*removeEvent*。
- afterEvents
  - 将事件/属性*removedEvent*重命名为*removeEvent*。
- 类*EntityRemovedAfterEvent*
  - 将字段*removedEntity*重命名为*removedEntityId*: *removedEntityId: string*。
  - 添加字段*typeId: string*。
- 添加类*EntityRemovedBeforeEvent*。
  - 添加字段*removedEntity: Entity*。
- 将*EquipmentSlot*移至*5.0*并将枚举值更改为大写。
- 将*EntityEquippableComponent*移至*5.0*。
- 记分板
  - *setObjectiveAtDisplaySlot*返回类型现在正确设置为*ScoreboardObjective*或undefined。
- 记分板身份
  - *getEntity*返回类型现在正确设置为Entity或undefined。
- *setWeather* API现在可以接受一个可选的持续时间参数来设置天气持续时间。
- 添加只读属性*heightRange: NumberRange* - 获取最小/最大维度高度限制。
- 添加Player.isSleeping和Player.isEmoting。

## **图形**

- 修复了延迟技术预览中手中物品的光照。
- 对点光源贡献进行了优化和修复。
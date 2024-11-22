---
标题: Minecraft Beta - 1.16.230.50 (Xbox One/Windows 10/Android)
日期: 2021-03-25T14:39:20Z
更新: 2021-03-25T15:45:14Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360058571432-Minecraft-Beta-1-16-230-50-Xbox-One-Windows-10-Android
---

**发布于:** 2021年3月25日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版期间无法加入非测试版玩家
- 在测试版中玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

# **新的实验性功能！**

在本周的洞穴与悬崖测试版中，我们添加了发光地衣，并修复了多个漏洞！您需要启用洞穴与悬崖实验性功能切换才能在您的测试版世界中查看这些功能。（您可以在[aka.ms/MCExperimentalToggle](https://aka.ms/MCExperimentalToggle)了解更多关于使用切换的信息。）

您可以在[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)的讨论串中留下对这些功能的反馈，并在[bugs.mojang.com](https://bugs.mojang.com/)搜索和报告您可能遇到的新漏洞。

![glow_lichen_1170_500.jpg](https://feedback.minecraft.net/hc/article_attachments/360090673492/glow_lichen_1170_500.jpg)

## **发光地衣**

- 一种在洞穴中生成的微弱光源
- 可以含水
- 使用剪刀将其收集
- 使用骨粉在方块表面传播
- 发光地衣可以被堆肥化

## **漏洞修复和调整**

**Android**

- 为支持鼠标和键盘的Android设备（Oreo及更新版本）添加了支持
- 某些Android设备不再无法进行多语言输入
- 在某些Android设备上，十字准星位置不再偏移
- 游戏在某些Android设备上不再无法正常关闭
- 修复了某些Android设备上的分辨率问题
- 修复了某些Android设备上的网络问题
- 在某些Android设备上，潜水不再使屏幕变为黑色
- 结构方块现在可以在Android上导出

**通用**

- 粉雪块在被爆炸破坏时不再掉落（[MCPE-118666](https://bugs.mojang.com/browse/MCPE-118666)）
- 修复了多个燃料来源的烧炼行为出现问题的情况（[MCPE-121863](https://bugs.mojang.com/browse/MCPE-121863)）
- 第一人称吃东西的动画现在在帧中居中（[MCPE-116678](https://bugs.mojang.com/browse/MCPE-116678)）
- 第一人称主手防御动画现在正确播放（[MCPE-115536](https://bugs.mojang.com/browse/MCPE-115536)）
- 第一人称主手和副手的盾牌现在是对称的（[MCPE-116736](https://bugs.mojang.com/browse/MCPE-116736)）
- 修复了在织布机中使用与原版资产不同分辨率的图案无法正确显示的问题
- 在切石机中合成（打蜡的）锈蚀切制铜台阶现在产出两个台阶而不是一个（[MCPE-121695](https://bugs.mojang.com/browse/MCPE-121695)）
- 拴绳现在正确附加到山羊上（[MCPE-104161](https://bugs.mojang.com/browse/MCPE-104161)）

**丰饶洞穴方块**

- 杜鹃树叶和盛开的杜鹃树叶在被剪切时现在正确掉落
- 苔藓块现在可以通过发射器正确施肥
- 垂根现在可以正确堆肥
- 小滴叶在被剪切时现在掉落为物品
- 在另一块大滴叶上放置大滴叶会将其高度增加一格
- 使用锹在缠根泥土上会创建草路径方块
- 蜜蜂将盛开的杜鹃花和盛开的杜鹃树叶视为花朵
- 使用拾取方块功能在洞穴藤蔓上或用精准采集附魔工具破坏它们现在会掉落发光浆果

**用户界面**

- 修复了在生成世界时取消加入导致用户卡在进度屏幕的问题（[MCPE-114776](https://bugs.mojang.com/browse/MCPE-114776)）

## **技术修复和更改**

**GameTest框架**

- 添加了维度类
- 添加了World.getDimension
- 更新了GameTest框架接口。请参见下面的列表以获取具体更改：
  - 函数assertEntityPresentInArea(entityIdentifier: string) - 如果在测试区域中不存在与给定标识符匹配的实体，则抛出错误
  - 函数print(text: string) - 将给定文本打印到聊天
  - 函数assertEntityInstancePresent(entity: Entity, position: BlockLocation) - 如果给定实体不在给定方块位置上，则抛出错误
  - \[已移除\] 函数setEntityTamed(entityIdentifier: string, position: BlockLocation) - 被组件函数setTamed(showParticles: bool)替代
- 实体
  - 函数getComponents() - 返回支持的组件数组
  - 函数getComponent(componentIdentifier: string) - 返回与给定标识符匹配的组件
  - 函数hasComponent(componentIdentifier: string) - 如果给定组件存在于实体上并且被支持，则返回true
  - 函数getName() - 返回实体的名称（例如“马”）
  - 添加了颜色、生命、可拴绳和驯化的组件
  - 函数kill() - 杀死实体
- 世界
  - addEventListener(eventName: string, callback: function(entity: Entity) ) - 注册实体事件的事件监听器 支持的事件：
    - “onEntityCreated” - 当实体被创建时触发
    - “onEntityDefinitionTriggered” - 当实体定义事件被触发时触发
- 将/gametest runall重命名为/gametest runset
- 标签参数的默认值现在为“suite:default”

**活动对象**

- ActorDataIDs中的多个枚举被错误地添加，现在正在移除（DEFINE_PROPERTIES，UPDATE_PROPERTIES）
- Catmull-Rom动画在关键帧的时间与其值匹配时将不再出现故障
- 所有使用/schedule命令运行的函数现在将从它们应该的原点运行，而不是从服务器运行

**其他修复**

- 将“Whitelist”的语言使用替换为“AllowList”。专用服务器命令“whitelist”更改为“allowlist”。专用服务器“whitelist.json”文件更改为“allowlist.json”文件。JSON格式保持不变。修改后的说明在bedrock_server_how_to.html中找到
- 修复了query.is_in_ui，使其在数据驱动的生物在用户界面中渲染时可用（query.is_in_ui在生物在用户界面中渲染时返回true，例如在物品栏窗口中）
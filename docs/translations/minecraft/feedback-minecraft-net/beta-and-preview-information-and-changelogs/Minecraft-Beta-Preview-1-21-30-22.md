---
title: Minecraft Beta & Preview - 1.21.30.22
date: 2024-08-07T15:31:19Z
updated: 2024-08-07T16:17:15Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/29067342985101-Minecraft-Beta-Preview-1-21-30-22
hash:
  user-content-features-and-bug-fixes: 特性与漏洞修复
  user-content-blocks: 方块
  user-content-commands: 命令
  user-content-gameplay: 游戏玩法
  user-content-graphical: 图形
  user-content-vanilla-parity: 原版趋同
  user-content-user-interface: 用户界面
  user-content-technical-updates: 技术更新
  user-content-api: API
  user-content-editor: 编辑器
  01J4PQ72ZJJQHZTW0VC2S013SR: 图形-2
  user-content-resource-and-behavior-packs: 资源与行为包
  user-content-experimental-features: 实验性特性
  01J4PQ72ZJ90TMXPV0GQB1SCDB: api-1
---

**发布于:** 2024年8月7日

**关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明

![Minecraft中延迟技术渲染的真实波浪](https://feedback.minecraft.net/hc/article_attachments/29067350121485)

以下是本周预览版和测试版的新内容：

# 特性与漏洞修复

## 方块

- “海绵”方块现在分为独立实例：“海绵”和“湿海绵”
- 彩色火把方块实例“colored_torch_rg”和“colored_torch_bp”现在分为独立实例“colored_torch_red”、“colored_torch_green”、“colored_torch_blue”和“colored_torch_purple”
- 在“minecraft:destructible_by_mining”方块组件中添加了新的实验性字段“item_specific_speeds”

## 命令

- 在`/reload`命令中添加了`all`参数。这会导致玩家退出世界并重新加入，同时重新加载所有行为包和资源包

## 游戏玩法

- 修复了试炼刷怪笼的碰撞形状；现在与普通方块的大小相同（[MCPE-178305](https://bugs.mojang.com/browse/MCPE-178305)）
- 添加了新的死亡消息，当玩家被重锤攻击击败时会显示

## 图形

- 将最大帧率滑块重命名为“帧率限制”，并添加了提示框以更好地描述其用途

## 原版趋同

- 只有一个可能等级的附魔不再在名称中显示其等级“I”
- 许多物品和方块的名称已与Java版保持一致。以下列表详细列出了左侧的旧名称和右侧的新名称：（[MCPE-101388](https://bugs.mojang.com/browse/MCPE-101388)）
  - 书与笔 -\> 书与笔
  - 链头盔 -\> 锁链头盔
  - 链胸甲 -\> 锁链胸甲
  - 链护腿 -\> 锁链护腿
  - 链靴子 -\> 锁链靴子
  - 附魔苹果 -\> 附魔金苹果
  - 熟牛肉 -\> 牛排
  - 西瓜 -\> 西瓜片
  - 闪烁的西瓜 -\> 闪烁的西瓜片
  - 牛奶 -\> 奶桶
  - 种子 -\> 小麦种子
  - 雪 -\> 雪块
  - 顶雪 -\> 雪
  - 草 -\> 矮草丛
  - 双高草 -\> 高草丛
  - 甘蔗 -\> 甘蔗
  - 黏土块 -\> 黏土
  - 黏土 -\> 黏土球
  - 海龟刷怪蛋 -\> 海龟刷怪蛋
  - 海龟蛋 -\> 海龟蛋
  - 红砖块 -\> 红砖块
  - 下界砖块 -\> 下界砖块
  - 红色下界砖 -\> 红色下界砖块
  - 海晶石砖台阶 -\> 海晶石砖台阶
  - 石砖台阶 -\> 石砖台阶
  - 红砖台阶 -\> 红砖台阶
  - 虫蚀石砖 -\> 虫蚀石砖
  - 阳光探测器 -\> 阳光探测器
  - 附魔台 -\> 附魔台
  - 测重压力板（重质） -\> 重质测重压力板
  - 测重压力板（轻质） -\> 轻质测重压力板
  - 开裂的铁砧 -\> 开裂的铁砧
  - 损坏的铁砧 -\> 损坏的铁砧
  - 头颅 -\> 玩家的头
  - 光源方块 -\> 光
- 石匠职业的村民名称已更改为石匠，以与Java版保持一致
- 哞菇现在在光照等级9及以上生成（[MCPE-66830](https://bugs.mojang.com/browse/MCPE-66830)）

## 用户界面

- 在游戏菜单中添加了一个按钮以截取屏幕截图。您可以在个人资料页面的截图库中查看您的截图
  - 我们希望听到您对这个功能的反馈和建议！您可以在这里发送反馈： [aka.ms/MCBedrockScreenshots](https://aka.ms/MCBedrockScreenshots)

# 技术更新

## API

- 修复了@minecraft/server-ui版本1.3.0无法访问的问题

## 编辑器

编辑器及其相应的API仍在早期开发中，现已在Windows PC基岩预览版构建中支持键盘/鼠标操作。请在社交媒体上标记我们，使用 **\#BedrockEditor**。了解 [如何使用](https://learn.microsoft.com/en-us/minecraft/creator/documents/editoroverview?view=minecraft-bedrock-stable) 编辑器，加入 [GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions) 论坛与团队互动，并通过 [入门工具包](https://github.com/Mojang/minecraft-editor-extension-starter-kit) 和 [示例](https://github.com/Mojang/minecraft-editor-extension-samples) 开始构建扩展。

本周更新：

- 在“延迟光照设置”面板中添加了`水`下拉菜单。
- 在文件菜单中添加了`导出`面板，以便在导出到文件之前自定义世界设置。
- 更新了画刷工具，增加了额外功能并提高了性能。
  - 添加了`单块`画刷形状，以便进行更精细的编辑。
  - 添加了`遮罩模式`，以自定义画刷与世界的交互方式。
    - `替换`将创建一个块列表，当刷涂时将被替换。列表中不包含的块将不会受到影响。
    - `遮罩`将创建一个块列表，当刷涂时将被遮罩/忽略。仅不在列表中的块将受到影响。
- 添加了`IRootPropertyPane`和`ISubPanePropertyItem`接口，以提高属性面板API的可用性
  - 将`createPropertyPane`和`removePropertyPane`函数重命名为`IPropertyPane`的`createSubPane`和`removeSubPane`。
  - 为根属性面板标题添加了操作按钮支持。
  - 为子面板添加了视觉自定义支持。
- 添加了尺子工具，用于使用新的客户端小部件框架测量距离。
- 在方块调色板项目中对权重值添加了约束。有效值范围为\[1,100\]。
- 添加了缺失的小部件绑定导出

## 图形

- 修复了导致月亮看起来更暗的漏洞（[MCPE-172971](https://bugs.mojang.com/browse/MCPE-172971)）
- 修复了数据驱动方块的剔除规则未随变换组件旋转的漏洞

## 资源与行为包

- 玩家“helmet_layer_visible”变量现在基于`has_head_gear` Molang查询的结果，玩家和角色渲染控制器的头盔层可见性不再检查头盔的存在。这修复了可附着脚本将“helmet_layer_visible”设置为1.0时的正常工作，并保持了一个修复，防止角色的头发和头盔在生物和南瓜头外部穿透（[MCPE-183058](https://bugs.mojang.com/browse/MCPE-183058)）

# 实验性特性

## API

- ItemUseOnBeforeEvent
  - 向测试版添加了属性`readonly isFirstEvent: boolean`。如果事件是在玩家首次交互按钮按下时触发，则该值为true；如果事件是从按住交互按钮触发，则为false
- ItemUseOnAfterEvent
  - 向测试版添加了属性`readonly isFirstEvent: boolean`。如果事件是在玩家首次交互按钮按下时触发，则该值为true；如果事件是从按住交互按钮触发，则为false

## 图形

- 在延迟技术预览中添加了数据驱动水参数的能力。有关更多信息，请参见更新的创作者门户
- 在延迟技术预览中添加了一项新特性：真实波浪！此新特性必须通过资源包选择加入，默认情况下不会启用。有关更多信息，请参见更新的创作者门户
- 在编辑器的延迟图形设置中添加了水控制选项

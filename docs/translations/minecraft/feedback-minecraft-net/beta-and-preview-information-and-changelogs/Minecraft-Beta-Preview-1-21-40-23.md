---
title: Minecraft Beta & Preview - 1.21.40.23
date: 2024-09-25T15:56:01Z
updated: 2024-09-26T08:56:01Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/30556182663437-Minecraft-Beta-Preview-1-21-40-23
hash:
  h_01J8MYD17GST4R9TGX20PY8NBS: 关于Minecraft预览和测试版的信息
  user-content-experimental-features: 实验性特性
  user-content-items: 物品
  user-content-known-issues: 已知问题
  user-content-stability-and-performance: 稳定性和性能
  user-content-features-and-bug-fixes: 特性和漏洞修复
  user-content-accessibility-features: 辅助功能特性
  user-content-blocks: 方块
  user-content-commands: 命令
  user-content-graphical: 图形
  user-content-trading: 交易
  user-content-user-interface: 用户界面
  user-content-technical-updates: 技术更新
  user-content-add-ons-and-script-engine: 附加包和脚本引擎
  user-content-api: API
  user-content-components: 组件
  user-content-editor: 编辑器
  user-content-entities: 实体
  01J8MY8B19SY1R993MVK1GYXRG: 稳定性和性能-1
  user-content-experimental-technical-features: 实验性技术特性
  01J8MY8B19DN1GCD2NMCZ12P72: 附加包和脚本引擎-1
  user-content-cameras: 摄像机
  01J8MY8B19P51M2W1P8QGJCZWW: 图形-1
---

## **关于Minecraft预览和测试版的信息：**

- 这些进行中的版本可能不稳定，并且可能无法代表最终版本的质量
- Minecraft预览可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ) 
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)  以获取详细说明

 

我们又带来了另一个Minecraft预览和测试版更新！如往常一样，请在 [feedback.minecraft.net](http://feedback.minecraft.net/)  提供任何反馈，并在 [bugs.mojang.com](http://bugs.mojang.com/)  报告您发现的任何漏洞。

 

# 实验性特性

## 物品

- 收纳袋图标现在与Java版匹配（[MCPE-185519](https://bugs.mojang.com/browse/MCPE-185519) ）
- 选中时，空的收纳袋不再显示满度条（[MCPE-185481](https://bugs.mojang.com/browse/MCPE-185481) ）
- 收纳袋染料配方现在在获取染料而非未染变种时解锁
- 收纳袋已去实验化，现在可以在普通游戏中使用
- "minecraft:bundle_interaction"物品组件已去实验化
- "minecraft:bundle_interaction"物品组件已去实验化

## 已知问题

- 放入收纳袋的物品无法在触摸时被选中或移除

## 稳定性和性能

- 在洞穴与山崖更新之前创建的自定义生物群系的世界，其区块中的自定义生物群系将被默认生物群系（主世界的海洋）替换

# 特性和漏洞修复

## 辅助功能特性

- 为市场通行证内容标签和领域内容标签中的物品添加了文本转语音的语音提示

## 方块

- 修复了一个漏洞，导致方块可以放置在宝库方块上，从而引发奇怪的方块行为（[MCPE-186627](https://bugs.mojang.com/browse/MCPE-186627) ）
- 更新了剩余行为包文件中对旧方块名称的引用

## 命令

- 修复了一些命令无法识别某些方块或物品名称的问题

## 图形

- 数据驱动的物品在截图中不再错位（[MCPE-185132](https://bugs.mojang.com/browse/MCPE-185132) ）

## 交易

- 修复了仅使用第二个槽位进行交易时的崩溃问题（[MCPE-186676](https://bugs.mojang.com/browse/MCPE-186676) ）

## 用户界面

- 在新的游戏界面上添加了未读领域故事徽章通知的支持（仅限预览版）
- 非空收纳袋在收纳袋内时现在有满度条（[MCPE-185457](https://bugs.mojang.com/browse/MCPE-185457) ）
- 在新的矿石用户界面编辑世界屏幕中添加了编辑世界缩略图的可能性

# 技术更新

## 附加包和脚本引擎

- "minecraft:looked_at"和"minecraft:home"实体组件中的新测试版选项现在正确要求在根JSON对象中指定"use_beta_features"

## API

- 修复了在无效实体的`onBeforeActorRemove`中调用`getDimension`时可能发生的崩溃

## 组件

- "minecraft:damage_sensor"组件的"deals_damage"字段现在支持三个值：
  - "yes"，接收到的伤害会施加到实体上
  - "no"，接收到的伤害不会施加到实体上
  - "no_but_side_effects_apply"，接收到的伤害不会施加到实体上，但攻击的副作用会施加
    - 这意味着攻击者的武器会失去耐久度，附魔副作用会生效等。
  - 现有内容将自动更新以保持其原始行为

## 编辑器

- 添加了新的空气方块图像，以便在编辑器中选择空气方块时进行可视化。
- 更新了方块选择器模态，以更好地传达当前选定的方块和替换它的方块。
- 修复了导航面板操作栏图标和缺失的本地化文本
- 修复了某些图标主题颜色未正确应用的漏洞

## 实体

- 当使用最低引擎版本为1.17.0或更低的资源包时，马铠现在能正确渲染在马身上（[MCPE-185316](https://bugs.mojang.com/browse/MCPE-185316) ）

## 稳定性和性能

- 自定义生物群系ID现在从30000开始分配，并存储在世界数据的'BiomeIdsTable'中，以便其ID分配在世界持续期间保持不变

# 实验性技术特性

## 附加包和脚本引擎

- 在"minecraft:block_placer"物品组件中添加了"replace_block_item"字段。该字段允许您指定此物品应替换其放置的数据驱动方块所创建的默认物品。要使用此字段，物品的标识符必须与其放置的方块的标识符匹配。该字段是可选的，默认为false。

## 摄像机

- 为焦点目标摄像机实验性切换添加了水平和垂直旋转限制
- 为焦点目标摄像机实验性切换添加了"continue_targeting"布尔值，以跟踪超出设定旋转限制的实体

## 图形

- 修复了点光源阴影的一个漏洞，该漏洞会导致附近表面出现圆圈。因此，点光源阴影的边缘现在是锯齿状的。此问题将在后续更新中解决。

- 添加了在延迟技术预览中数据驱动环境光的能力。当SSR和IBL不可用或不足以在低光条件下照亮金属物体时，环境光用作间接镜面反射的贡献。它还用作环境贡献的最小值，从而避免在没有光源时场景完全黑暗。有关更多信息，请参见创作者门户上的更新文档。

- 对与延迟技术预览相关的JSON文件进行了破坏性架构更改，将`"format_version"`字段提升到根级别。创作者门户上的文档将相应更新。受影响的文件包括：

  - `"atmospherics/atmospherics.json"`
  - `"color_grading/color_grading.json"`
  - `"lighting/global.json"`
  - `"pbr/global.json"`
  - `"point_lights/global.json"`
  - `"water/water.json"`

例如，之前的`"lighting/global.json"`架构为：

``` hljs
{
    "minecraft:lighting_settings": {
        "format_version": "1.21.40",
        ...
    }
}
```

但现在应写为：

``` hljs
{
    "format_version": "1.21.40",
    "minecraft:lighting_settings": {
        ...
    }
}
```
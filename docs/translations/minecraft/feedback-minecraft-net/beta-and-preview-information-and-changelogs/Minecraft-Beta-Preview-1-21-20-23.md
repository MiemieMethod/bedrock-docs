---
标题: Minecraft Beta & 预览 - 1.21.20.23
日期: 2024-07-17T08:58:16Z
更新: 2024-07-17T14:29:39Z
分类: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/28486285876237-Minecraft-Beta-Preview-1-21-20-23
哈希:
  h_01J2ZYHMGZAEFTYY526V9FH6EQ: 特性与漏洞修复
  h_01J2ZYHMH07NTTGQZPGZ01ZQYJ: 辅助功能
  h_01J2ZYHMH06R17WKPXTQD4T4PM: 方块
  h_01J2ZYHMH008CQ0CHFWVE9Q6TC: 游戏提示
  h_01J2ZYHMH0W3TFR5ZXT3VA19HG: 游戏玩法
  h_01J2ZYHMH0443C147D4FMAE244: 文本输入
  h_01J2ZYHMH0TR9JCXWAD0KKHZZH: 用户界面
  h_01J2ZYHMH0W6232JJAFC6KMMEF: 用户界面游戏玩法
  h_01J2ZYHMH0NPYD1ER4ZGV8HXDY: 原版趋同
  h_01J2ZYHMH03HG0M6HB4Y7NSX3F: 技术更新
  h_01J2ZYHMH0YQQ1XG8Z4M107PK8: 编辑器
  h_01J2ZYHMH02QJQTP6Y0A1DTE2A: 实体组件
  h_01J2ZYHMH04QC968S4MRM39D6C: 一般
  h_01J2ZYHMH0W1GV8H6EXQFN4YER: 技术实验性更新
  h_01J2ZYHMH0S16G1HV2Q901CKW1: 创作者相机 - 焦点目标
---

**发布:** 2024年7月17日

**关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明

![一个村民站在用钓鱼碎片制作的饰纹陶罐旁边，旁边有一只拴着的云杉木船在冰湖上。背景中有一个村庄。](https://feedback.minecraft.net/hc/article_attachments/28486269122061)

新的Minecraft预览和Beta版本正在推出，带来了更多调整和漏洞修复！以下是本周的新内容列表：

# 特性与漏洞修复

## 辅助功能

- 修复了Apple Pencil未被识别为有效输入方法的问题 ([MCPE-158895](https://bugs.mojang.com/browse/MCPE-158895))

## 方块

- "light_block_0"及其衍生物现在已定义其方块声音 ([MCPE-183449](https://bugs.mojang.com/browse/MCPE-183449))

## 游戏提示

- 游泳游戏提示现在仅在不在水中呼吸时出现

## 游戏玩法

- 修复了在使用触控控制和自定义相机时输入可能无法按预期工作的实例

## 文本输入

- 修复了在Xbox上先前使用的文本字段内容被带入告示牌的问题 ([MCPE-182645](https://bugs.mojang.com/browse/MCPE-182645))

## 用户界面

- 聊天快速访问历史不再存储重复的聊天条目

## 用户界面游戏玩法

- 修复了快速移动物品堆到非空堆时图标闪烁的问题

## 原版趋同

- 拴绳现在附加在船的前面，而不是中心 ([MCPE-182145](https://bugs.mojang.com/browse/MCPE-182145))

# 技术更新

## 编辑器

编辑器及其对应的API处于早期开发阶段，并可在Windows PC基岩预览构建中使用键盘/鼠标。请在社交媒体上标记我们 **\#BedrockEditor。**

了解 [如何使用](https://aka.ms/LearnEditor) 编辑器，加入 [GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions) 论坛与团队互动，并通过 [入门工具包](https://github.com/Mojang/minecraft-editor-extension-starter-kit) 和 [示例](https://github.com/Mojang/minecraft-editor-extension-samples) 开始构建扩展。

本周更新：

- 更新方块快捷栏以具有非空气默认值
- 为默认快捷栏添加持久性
- 添加 "ExtensionContext.settings.theme"，表示世界内用户界面主题
  - 此特性目前有三个功能：*resolveColorKey(string): Color*，*setCurrentTheme(string): void*，和 *getThemeList(): string\[\]*
  - 目前有一个 "minecraft:default" 主题
  - 未来的工作将添加创建、修改和删除自定义主题的能力，但默认主题将不可修改
- 更新部分PropertyPane API以使用IObservable模式。
  - 添加了一个替代的Property Pane *addVector3* API，利用类型安全的 *IObservable*，可使用 *makeObservable* API创建观察者
    - 为新属性项添加了接口 *IVector3PropertyItem* 和 *IVector3PropertyItemOptions*
    - 将创建属性包Vector3的函数重命名为 *addVector3_deprecated*
  - 添加了一个替代的Property Pane *addBool* API，利用类型安全的 *IObservableProp* 值API
    - 为新属性项添加了接口 *IBoolPropertyItem* 和 *IBoolPropertyItemOptions*
    - 将创建属性包布尔项的函数重命名为 *addBool_deprecated*
  - 将Property Pane addText API转换为使用 *IObservableProp*
  - 为按钮属性项添加了接口 *IButtonPropertyItem* 和 *IButtonPropertyItemOptions*
    - IPropertyPane *addButton* API现在可以接受一个普通函数
    - 移除了 *ButtonVariant* 类型，添加了 *ButtonPropertyItemVariant* 枚举API
  - 将 *EDITOR_PANE_PROPERTY_ITEM_TYPE* 枚举API重命名为 *PropertyItemType*
  - 将属性面板 *addImage* API转换为支持 *IObservable*。还将能够使用自定义图像格式，如图标和方块，作为值使用 *ImageResourceData*
    - 为 *IImagePropertyItemOptions* API添加了 *onClick* 函数和 *alignment* 属性

## 实体组件

- 改进了 "behavior.follow_owner" 传送逻辑：
  - 实体现在可以在传送到其所有者后无缝恢复导航
  - 添加了 "post_teleport_distance" 字段，允许指定实体在传送后距离其所有者的距离
    - 如果未指定值，将使用 "stop_distance" 增加一的值
  - 这些更改仅影响格式版本为1.21.20或以上的实体

## 一般

- 移除了 "假日创作者特性" 实验。使用实验性特性的内容可能无法正常工作。请查看自定义组件，它复制了大部分功能：<https://learn.microsoft.com/en-us/minecraft/creator/documents/customcomponents>

# 技术实验性更新

## 创作者相机 - 焦点目标

- 焦点目标实验现已可用，未来版本将提供更多功能
- 添加了一个新的相机命令，以目标实体并将其保持在屏幕中心
  - 包括从实体中心添加偏移的选项
  - 包括移除目标的选项
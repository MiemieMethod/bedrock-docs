---
标题: Minecraft Beta - 1.17.30.21 (Xbox One/Windows 10/Android)
日期: 2021-08-12T15:10:10Z
更新: 2021-08-12T15:48:38Z
分类: Beta和预览信息及更新日志
标签:
  - beta
  - beta_changelog
  - 洞穴与悬崖
链接: https://feedback.minecraft.net/hc/en-us/articles/4406948851213-Minecraft-Beta-1-17-30-21-Xbox-One-Windows-10-Android
哈希:
  用户界面和HUD: user-interfaceand-hud
  数据驱动方块---实验性特性: data-driven-blocks--experimental-features
---

**发布于:** 2021年8月12日

**在参与Minecraft Beta之前请阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换你的游戏
- 你将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![Screen_Shot_08-11-21_at_11.09_AM.JPG](https://feedback.minecraft.net/hc/article_attachments/4406956022669/Screen_Shot_08-11-21_at_11.09_AM.JPG)

又到了Bedrock Beta更新的时刻！请继续在<https://aka.ms/CavesCliffsFeedback>的讨论中向我们反馈你的意见，并在[https://bugs.mojang.com](https://bugs.mojang.com/)搜索并报告你可能遇到的新漏洞。

# 特性与漏洞修复

## 稳定性与性能

- 修复了在游戏过程中可能发生的多个崩溃
- 修复了下载大型市场世界时可能导致崩溃的问题
- 修复了可能导致崩溃或阻止某些Android 11设备访问或打开世界的问题（[MCPE-137652](https://bugs.mojang.com/browse/MCPE-137652)）

## 原版趋同

- 通过尝试避免在从床上醒来时将玩家放置在造成伤害的方块上，使重生行为与Java版一致
- 通过尝试在玩家从床上醒来时将其放置在进入床的侧面，使重生行为与Java版一致（[MCPE-118654](https://bugs.mojang.com/browse/MCPE-118654)）
- 生物生成器不再发出光（Java趋同）

## 生物

- 靠近细雪并不能保护不死生物免受阳光的灼烧（[MCPE-131005](https://bugs.mojang.com/browse/MCPE-131005)）

## 角色创建器

- 在更衣室的皮肤包描述部分选择“在商店查看包”按钮后不再出现无限加载

## 用户界面和HUD

- 修复了如果在资源包中更改了物品类别文本颜色，则物品类别文本颜色与物品文本颜色不匹配的问题
- 修复了在某些纹理包中，织布机中的图案无法正确显示的问题

# 技术更新

## 数据驱动方块 - 实验性特性

- 添加了BlockPartVisibilityComponent
  - 允许创作者为几何体JSON中列出的每个“骨骼”指定Molang条件，以根据方块状态开启/关闭骨骼
  - 必须开启实验性切换才能使用

## Molang

- 修复了实验性query.bone_orientation_trs以获得正确的平移Y和缩放结果
- 添加了实验性block_neighbor_has_any_tags和block_neighbor_has_all_tags MoLang查询
  - 采用相对方块位置和一组标签
  - 返回0/1
  - 必须开启实验性切换才能使用

## 图形

- 添加了DragonFX材质以支持光线追踪资源的光栅化g-buffer预处理

## 数据驱动物品

- 更新了DamageableItemComponent的文档

## Molang

- 进入包含query.armor_color_slot的自定义资源包的世界时不再发生崩溃（[MCPE-106437](https://bugs.mojang.com/browse/MCPE-106437)）
- 将实验性Molang查询（与活动对象属性无关的）移动到新的“实验性Molang特性”切换中

## 用户界面

- 修复了编辑NPC对话时的控制器支持
- 解析UI JSON字段“ignored”时，如果无效现在会抛出content_error
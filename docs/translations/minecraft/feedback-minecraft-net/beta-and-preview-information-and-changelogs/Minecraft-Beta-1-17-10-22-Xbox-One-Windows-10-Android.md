---
标题: Minecraft Beta - 1.17.10.22 (Xbox One/Windows 10/Android)
日期: 2021-06-09T13:28:27Z
更新: 2021-06-09T15:59:12Z
类别: 测试版和预览信息及更新日志
标签:
  - 测试版
  - 测试版更新日志
  - 洞穴与山崖
链接: https://feedback.minecraft.net/hc/en-us/articles/4402696446989-Minecraft-Beta-1-17-10-22-Xbox-One-Windows-10-Android
---

**发布于:** 2021年6月9日

**请在参与Minecraft测试版之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

又到了更新洞穴与山崖测试版的时间！请继续在[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)的讨论中留下您的反馈，并在[bugs.mojang.com](https://bugs.mojang.com/)搜索并报告您可能遇到的任何新漏洞。

![candles_1170x500.jpg](https://feedback.minecraft.net/hc/article_attachments/4402703422477/candles_1170x500.jpg)

 

 

# **新特性和漏洞修复**

## **蜡烛**

- 蜡烛现在在游戏中可用！
- 可以成群放置，最多四个，并可以使用燧石和钢点燃
- 尝试把一个放在蛋糕上并许个愿吧！
- 蜡烛可以使用蜜脾和线合成
- 在合成网格中与染料结合以合成不同颜色的蜡烛

## **游戏玩法**

- 落下的铁砧和钟乳石在落入液体时现在会对生物造成伤害
- 修复了一个漏洞，导致玩家穿过蜘蛛网时在落地前会受到跌落伤害（[MCPE-121550](https://bugs.mojang.com/browse/MCPE-121550)）
- 使用触控控制器下降穿过细雪现在使用与下降穿过脚手架相同的按钮
- 原版趋同：空铁桶不再可以用来收集鱼

## **生物**

- 美西螈现在仅在完全黑暗中生成
- 铁傀儡和唤魔者在和平难度下不再有时会表现出攻击性（[MCPE-47012](https://bugs.mojang.com/browse/MCPE-47012)）
- 发光鱿鱼在受伤时会变暗以匹配周围的光照水平（[MCPE-121754](https://bugs.mojang.com/browse/MCPE-121754)）
- 当山羊进行冲撞攻击时，生物将不再反击山羊（[MCPE-129619](https://bugs.mojang.com/browse/MCPE-129619)）
- 修复了在分屏时遇到守卫者时可能出现的警告

## **角色创建器**

- 特征物品缩略图现在会保留在特征物品窗口内
- “选择新皮肤”按钮即使在没有导入自定义皮肤时也会显示（[MCPE-128971](https://bugs.mojang.com/browse/MCPE-128971)）
- “选择新皮肤”按钮在选择纤细自定义选项后不再消失
- 修复了导致玩家的头颅在使用表情时无法正常动画的问题（[MCPE-126902](https://bugs.mojang.com/browse/MCPE-126902)）

## **已知问题**

- 使用火焰弹点燃物体（如蜡烛）可能会导致崩溃

 

# **技术更新**

## **MoLang**

- 修复实验性“query.target”以在客户端查询中工作

## **数据驱动方块**

- 更新了“BlockUnwalkableComponent”的文档

## **一般**

- 当自定义配方无效时，玩家将收到内容错误提示
- 将“minecraft:scaffolding_climber”重命名为“minecraft:block_climber”，现在可以处理攀爬脚手架和细雪

## **NPC对话**

- 内容创作者现在可以使用“/dialogue”命令和对话JSON文件为NPC创建多页对话和分支叙事

 

## **游戏测试框架（实验性）**

### **事件**

- 将“World.event.weatherChanged”重命名为“World.event.changeWeather”
- 添加事件“World.event.addEffect” - 当效果应用于实体时触发。
- 添加事件“World.event.createEntity” - 当实体添加到世界时触发。
- 移除函数“World.addEventListener”
- 将函数“getDuration()”更改为属性“duration”
- 将函数“getAmplifier()”更改为属性“amplifier”
- 添加属性“displayName” - 获取效果的显示名称
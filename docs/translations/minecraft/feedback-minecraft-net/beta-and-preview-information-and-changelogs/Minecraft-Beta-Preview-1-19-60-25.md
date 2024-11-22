---
title: Minecraft Beta & Preview - 1.19.60.25
date: 2023-01-05T15:13:07Z
updated: 2023-01-12T10:41:55Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/11995250732557-Minecraft-Beta-Preview-1-19-60-25
---

**发布于：** 2023年1月5日

**关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一张Minecraft截图，展示了一个村庄，里面有一个铁傀儡、一只骆驼和一个放在音符盒上的猪灵的头。](https://feedback.minecraft.net/hc/article_attachments/11996092236685)

以下是本周Minecraft预览版和测试版的新内容！请记得将您的反馈发送至 [aka.ms/MC120Feedback](https://aka.ms/MC120Feedback) 并向 [bugs.mojang.com](http://bugs.mojang.com/) 报告任何漏洞。

 

## 已知问题

- 玩家在使用手柄或鼠标键盘时无法堆叠分开的物品。我们希望尽快解决此问题！  
    

# 实验性功能

## 游戏玩法

- 骆驼不再被可骑乘实体拉入 ([MCPE-163610](https://bugs.mojang.com/browse/MCPE-163610))

## 音符盒

- 现在可以在音符盒上放置生物头颅而无需潜行
  - 这绕过了默认的交互，我们非常希望您对这一变化提供反馈！

触控控制

- 如果不使用经典触控控制，现在会正确显示下车提示  
    

# 功能和漏洞修复

## 方块

- 深红色和扭曲方块集现在具有独特的声音

## 命令

- 修复了使用命令传送玩家到其他维度时可能导致崩溃的问题 ([MCPE-164940](https://bugs.mojang.com/browse/MCPE-164940))

## 命令趋同

- 在没有设置分数的玩家上运行‘/execute if\|unless score’现在将返回false ([MCPE-156279](https://bugs.mojang.com/browse/MCPE-156279))
- ‘/execute if\|unless score’不再接受可能返回多个实体的选择器（例如 @e, @a）

## 一般

- 红石粉现在在放置到地面时会发出声音 ([MCPE-65423](https://bugs.mojang.com/browse/MCPE-65423))
- 玩家现在将正确响应使用 *minecraft:movement* 的速度变化

## 输入

- 修复了一个漏洞，在退出菜单屏幕后，鼠标光标仍然可见且无法用于控制HUD屏幕上的玩家摄像机

## 物品

- 凋零和末影龙刷怪蛋不再在创造模式物品栏中可用，但仍可通过命令获得

## 生物

- 玩家现在可以“获取”铁傀儡、雪傀儡、凋零和末影龙，获得它们各自的刷怪蛋 ([MCPE-164533](https://bugs.mojang.com/browse/MCPE-164533))
- 猪灵现在可以在下界的光照等级高于7的地方再次生成 ([MCPE-165096](https://bugs.mojang.com/browse/MCPE-165096))
- 唤魔者现在在骑乘坐骑或载具时会播放“坐下”动画 ([MCPE-43778](https://bugs.mojang.com/browse/MCPE-43778))

## 粒子效果

- 更新了粒子文档，描述了新材料并在示例资源包中包含了示例粒子

## 性能和稳定性

- 修复了使用“instant_despawn”组件时可能导致崩溃的问题
- 修复了加载活动对象时可能导致崩溃的问题
- 客户端级别区块生成现在由服务器主导，防止客户端生成不必要的区块

## 触控控制

- 解决了在某些设备上按下物品栏按钮可能与世界交互而不是打开物品栏的问题 ([MCPE-154499](https://bugs.mojang.com/browse/MCPE-154499))
- 修复了玩家在一行内容超出屏幕时无法翻页的问题
- 在按住合成物品时添加了多个重复合成的间隔级别
- 移除了在玩家从攻击和建造按钮滑动时的摄像机移动延迟
- 新的触控控制下重新激活了触控聚焦圆圈（不在十字准星模式下）

## 用户界面

- 触控设备上的游戏内吐司通知现在可以被滑动关闭
- Xbox上的触控控制设置部分不再可见

## 原版趋同

- 更改各种方块的地图颜色以匹配Java版 ([MCPE-19228](https://bugs.mojang.com/browse/MCPE-19228))
- 更改青蛙卵的地图颜色以匹配Java版 ([MCPE-159715](https://bugs.mojang.com/browse/MCPE-159715))
- 更改床方块的地图颜色以匹配Java版 ([MCPE-40709](https://bugs.mojang.com/browse/MCPE-40709))
- 更新骷髅/僵尸马和驴/骡的鞍和箱子纹理

## 方块

- 木门、铁门、木活板门、铁活板门和栅栏门现在使用与Java版相同的开关声音
- 更新压力板，使其根据行为具有不同的声音音调，以匹配Java版
- 为木按钮添加了独特的点击声音，以匹配Java版

# 技术更新

## API

- 实体
  - 修复了 *getEffect* 方法可能返回无效效果的漏洞（以及在添加新效果后效果可能变为无效的另一种情况）  
      
- EntityHurtEvent
  - 添加只读属性 *damageSource: EntityDamageSource* - 获取有关伤害来源的信息
  - EntityDamageSource
    - 添加属性 *cause: EntityDamageCause* - 获取伤害原因
    - 添加属性 *damagingEntity?: Entity* - 获取造成伤害的实体
    - 添加属性 *damagingProjectile?: Entity* - 获取造成伤害的投射物实体
    - 添加函数 *applyDamage(amount: number, source?: EntityDamageSource): boolean* - 对实体施加伤害并返回操作结果
  - 维度
    - 添加函数 *fillBlocks(begin: BlockLocation, end: BlockLocation, block: BlockPermutation \| BlockType, options?: BlockFillOptions): number*
      - 用类型为block的方块填充*begin*和*end*之间的区域。返回放置的方块数量
    - 添加新接口 *BlockFillOptions*，其成员 *matchingBlock?: BlockPermutation \| BlockType*
      - 与 *fillBlocks* 一起使用，以应用附加选项，例如仅填充与 *matchingBlock* 匹配的方块
    - 玩家
      - 添加函数 *addLevels(amount: number): number* - 向玩家添加/移除等级并返回玩家当前等级
      - 添加函数 *addExperience(amount: number): number* - 向玩家添加/移除经验并返回玩家当前经验
      - 添加函数 *resetLevel(): void* - 重置玩家的等级
      - 添加函数 *getTotalXp(): number* - 获取玩家的总经验
      - 添加只读属性 *level* - 获取玩家的等级
      - 添加只读属性 *xpEarnedAtCurrentLevel* - 获取玩家在当前等级获得的经验
      - 添加只读属性 *totalXpNeededForNextLevel* - 获取玩家当前等级所需的总经验

## 配方

- 重命名并转换所有锻造台配方以使用新引入的“minecraft:recipe_smithing_transform”配方格式

## 一般

- 为条件添加内容错误，指自定义方块具有变体或属性在非实验性世界中无法加载，适用于JSON格式1.19.60及更高版本
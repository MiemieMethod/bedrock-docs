---
title: Minecraft Beta - 1.18.20.23 (Xbox / Windows / Android)
date: 2022-02-02T14:48:33Z
updated: 2022-02-04T17:45:56Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/4423906361869-Minecraft-Beta-1-18-20-23-Xbox-Windows-Android
---

**发布于：** 2022年2月2日

**请在参与Minecraft测试版之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩过的任何世界无法在游戏的先前版本中打开，因此请复制世界以防止丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox、Windows和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)获取详细说明

![frogspawn.jpg](https://feedback.minecraft.net/hc/article_attachments/4423906675981/frogspawn.jpg)

 

以下是本周测试版的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，网址为[bugs.mojang.com](http://bugs.mojang.com/)。请注意 - Minecraft预览版将收到稍有不同版本的更新 - 有关更多信息，请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)。

# **实验性特性**

## **青蛙**

- 青蛙现在仅在使用跳跃目标时使用跳跃动画
- 青蛙现在使用史莱姆球被诱惑和繁殖
- 蝌蚪的生命值现在为6
- 调整了青蛙在沼泽中的生成，权重为10，群体大小为2-5
- JumpToBlockGoal现在正确地让生物跳到像睡莲这样的较小方块上

## **青蛙卵**

- 青蛙卵现在在被活塞推动时会破坏
- 当其下方的水源被移除时，青蛙卵现在会被摧毁
- 青蛙卵不再因下方有方块而无法孵化
- 青蛙卵现在可以放置在含水方块上
- 青蛙卵不再可以通过'/fill'命令放置在坚固地面上或水下
- 青蛙卵方块现在会被下落的方块摧毁（[MCPE-150781](https://bugs.mojang.com/browse/MCPE-150781)）

## **山羊角**

- 使用山羊角后，现在有一个冷却时间，才能再次使用

# **特性和漏洞修复**

## **自定义皮肤**

- 修复了离开更衣室时自定义皮肤未保存的问题

## **游戏玩法**

- 修复了修补魔咒并不总是正确消耗经验球进行修复的问题（[MCPE-120119](https://bugs.mojang.com/browse/MCPE-120119)）

## **生物**

- 溺尸不再可以在光照等级高于0的地方生成（[MCPE-150148](https://bugs.mojang.com/browse/MCPE-150148)）

## **用户界面**

- 修复了在口袋UI物品栏屏幕上2x2合成网格上方标签被截断的问题（在某些语言中）
- 修复了“创建新世界”选项中的测试版设置在游戏会话之间未持久化的问题

## **原版趋同**

- 炼药锅现在无法被低于流动水的滴水石填充

## **物品**

- 当已装备不同盔甲时，现在可以通过“使用”按钮装备自定义盔甲（[MCPE-125323](https://bugs.mojang.com/browse/MCPE-125323)）

# **技术更新**

## **方块**

- 修复了投射物在钟上以奇怪的方式“反弹”的问题（[MCPE-47847](https://bugs.mojang.com/browse/MCPE-47847)）

## **命令**

- '/tickingarea'命令不再修改带有*tick_world*组件的实体区域

## **Molang**

- 修复了逻辑与在逻辑或之前进行评估，以及比较运算符在相等运算符之前进行评估
  - 这是一个Molang版本更改，仅对使用min_engine_version为1.18.20或更高版本的包中的Molang表达式生效
  - 例如A && B \|\| C现在评估为(A && B) \|\| C，A \< B == C \> D现在评估为(A \< B) == (C \> D)

## **结构生成和活动对象生成**

- 修复了末地水晶在末地尖刺上重复生成的问题（[MCPE-147817](https://bugs.mojang.com/browse/MCPE-147817)）

## **实验性**

- 修复了活动对象属性并不总是从服务器同步到客户端的问题

## **EatMobGoal**

- 当玩家是目标时，EatMobGoal现在无法启动

## **GameTest框架**

- 向量
  - 添加函数length(): number- 返回此向量的长度
  - 添加函数normalized(): Vector- 返回此向量的标准化向量
  - 添加静态函数distance(a:Vector, b:Vector): number- 返回两个向量之间的距离
  - 添加静态函数lerp(a:Vector, b:Vector, t: number): Vector- 返回a和b之间的线性插值，使用t作为控制
  - 添加静态函数slerp(a:Vector, b:Vector, s: number): Vector- 返回a和b之间的球面线性插值，使用s作为控制
  - 添加静态函数cross(a:Vector, b:Vector): Vector- 返回这两个向量的叉积
  - 添加静态函数add(a:Vector, b:Vector): Vector- 返回这两个向量的和
  - 添加静态函数subtract(a:Vector, b:Vector): Vector- 返回这两个向量的差
  - 添加静态函数multiply(a:Vector, b:Vector): Vector- 返回这两个向量的逐分量乘积
  - 添加静态函数divide(a:Vector, b:Vector): Vector- 返回这两个向量的逐分量除法
  - 添加静态函数multiply(a:Vector, b:number): Vector- 返回此向量与标量的乘积
  - 添加静态函数divide(a:Vector, b:number): Vector- 返回此向量与标量的除法
  - 添加静态函数min(a:Vector, b:Vector): Vector- 返回由两个向量的最小分量构成的向量
  - 添加静态函数max(a:Vector, b:Vector): Vector- 返回由两个向量的最大分量构成的向量
- 世界
  - 添加函数playSound(soundName: String, soundOptions: SoundOptions): void- 播放由声音名称指定的声音，位置、俯仰角或音量可在SoundOptions参数中选择性指定
- EntityItemComponent
  - 添加组件EntityItemComponent，可用于从物品实体中获取物品堆栈 – 例如，getComponent(“item”).itemStack

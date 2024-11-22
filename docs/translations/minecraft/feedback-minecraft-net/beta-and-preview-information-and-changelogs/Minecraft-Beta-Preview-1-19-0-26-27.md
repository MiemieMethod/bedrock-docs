---
标题: Minecraft Beta & 预览 - 1.19.0.26/27
日期: 2022-04-20T15:11:51Z
更新: 2022-04-20T16:02:21Z
类别: Beta 和 预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/5661892666253-Minecraft-Beta-Preview-1-19-0-26-27
---

**发布于:** 2022年4月20日

## **关于Minecraft预览和Beta的信息：**

- Beta版本: 1.19.0.26 \| 预览版本: 1.19.0.27
- 尽管预览和Beta之间的版本号不同，但游戏内容没有差异
- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta可在Xbox、Windows 10/11和Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![截图: 一只Minecraft监守者使用其声波远程攻击](https://feedback.minecraft.net/hc/article_attachments/5661785455501/beta_19_3_sonic_attack.jpg)

以下是本周Beta的新内容列表！如往常一样，请搜索并报告您可能发现的任何漏洞，访问 [bugs.mojang.com](http://bugs.mojang.com/) 并发送 [您的反馈](https://aka.ms/MinecraftBetaFeedback)。  
  

# **新特性和漏洞修复**

## **声音**

- 为荒野更新添加了新音乐
- 青蛙现在使用所有受伤声音（[MCPE-152629](https://bugs.mojang.com/browse/MCPE-152629)）
- 蛙明灯现在具有正确的破坏声音（[MCPE-153943](https://bugs.mojang.com/browse/MCPE-153943)）

### **远古城市**

- 灵魂灯笼不再在远古城市的空气方块上生成（[MCPE-153586](https://bugs.mojang.com/browse/MCPE-153586)）
- 城市中心结构现在形成一个完整的强化深板岩矩形（[MCPE-153567](https://bugs.mojang.com/browse/MCPE-153567)）
- 在远古城市的战利品箱中添加了回响碎片
- 更新远古城市结构以匹配Java版本

## **监守者**

- 监守者现在具有声波攻击，可以对其攻击的目标造成远程伤害和击退
- 监守者在有目标时不再“嗅探”
- 如果监守者嗅探到目标，则防止其向下挖掘
- 监守者现在可以被其他生物推开
- 监守者现在会对所有撞到它的生物感到愤怒（[MCPE-153839](https://bugs.mojang.com/browse/MCPE-153839)）
- 修复了在攻击监守者时切换游戏模式导致的崩溃
- 监守者现在给予正确数量的经验（[MCPE-153564](https://bugs.mojang.com/browse/MCPE-153564)）

## **悦灵**

- 悦灵互动提示框现在显示“将物品给悦灵”（[MCPE-153035](https://bugs.mojang.com/browse/MCPE-153035)）

## **方块**

- 凋零现在无法再摧毁强化深板岩（[MCPE-153542](https://bugs.mojang.com/browse/MCPE-153542)）
- 末影龙现在无法再摧毁强化深板岩（[MCPE-153545](https://bugs.mojang.com/browse/MCPE-153545)）
- 强化深板岩已移至创造模式物品栏的自然标签中（[MCPE-153543](https://bugs.mojang.com/browse/MCPE-153543)）

### **泥砖块**

- 泥砖楼梯/台阶/墙现在正确分组（[MCPE-153719](https://bugs.mojang.com/browse/MCPE-153719)）

## **游戏玩法**

- 修复了使用材料还原器时游戏崩溃的问题（教育版功能）
- 修复了在水下从内部破坏光源方块的问题（[MCPE-148393](https://bugs.mojang.com/browse/MCPE-148393)）
- 修复了在使用熔炉时从错误槽位取物品时获得经验的问题（[MCPE-152227](https://bugs.mojang.com/browse/MCPE-152227)）
- 允许红树根和繁殖体可堆肥（[MCPE-153782](https://bugs.mojang.com/browse/MCPE-153782)，[MCPE-153912](https://bugs.mojang.com/browse/MCPE-153912)） 
- 允许大多数植物和树苗可以放置在泥巴和沾泥的红树根上。这包括所有花、树苗、竹子、甘蔗、大型垂滴叶和甜浆果丛（[MCPE-153916](https://bugs.mojang.com/browse/MCPE-153916)）
- 允许红树根穿过雪层生成（[MCPE-153913](https://bugs.mojang.com/browse/MCPE-153913)）
- 蝌蚪现在可以被黏液球吸引

## **触控控制设置**

- 静态摇杆切换不再因移动摇杆切换被禁用而失效（[MCPE-153201](https://bugs.mojang.com/browse/MCPE-153201)）

## **图形**

- 更新船和箱子船的物品图标纹理，使其与Java版一致（[MCPE-153353](https://bugs.mojang.com/browse/MCPE-153353)）

## **村庄**

### **袭击**

- 恶徒现在被允许迁移到其他村庄并进行袭击（[MCPE-151310](https://bugs.mojang.com/browse/MCPE-151310)）

# **技术更新**

## **JSON**

- 修复了导致音乐权重未被使用的问题

## **GameTest框架（实验性）**

- 更新GameTest框架接口以添加只读记分板支持
- 世界
  - scoreboard : 记分板 - 访问世界的记分板
- 实体
  - scoreboard : 记分板标识 - 访问实体的记分板标识
- 记分板 - 表示记分板数据的对象
  - getObjective(objectiveId : 字符串) : 记分板目标 - 获取特定目标（按id）
  - getObjectives : 记分板目标\[\] - 获取所有目标
  - getParticipants : 记分板标识\[\] - 获取所有记分板标识
- 记分板目标 - 表示记分板目标的对象
  - id : 字符串 - （只读）记分板标识符
  - displayName : 字符串 - （只读）记分板显示名称
  - getParticipants : 记分板标识\[\] - 获取所有目标参与者标识
  - getScores : 记分板分数信息\[\] - 获取所有参与者的分数信息
  - getScore(participant : 记分板标识) : 整数 - 获取参与者的分数值
- 记分板标识 - 表示记分板参与者的对象
  - type : 记分板标识类型 - （只读）表示身份类型的枚举
  - id : 整数 - （只读）身份的唯一标识符
  - displayName : 字符串 - （只读）身份的显示名称
  - getEntity : 脚本活动对象 - 获取与身份关联的脚本活动对象句柄
- 记分板标识类型 - 表示身份类型的枚举：.Entity - 实体 .FakePlayer - 虚假身份 .Player - 玩家
- 记分板分数信息 - 目标的分数-身份对
  - participant : 记分板标识 - （只读）参与者
  - score : 整数 - （只读）分数
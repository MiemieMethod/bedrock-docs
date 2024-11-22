---
标题: Minecraft Beta & Preview - 1.19.10.23
日期: 2022-06-15T15:07:23Z
更新: 2022-06-15T16:00:37Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/6944215774349-Minecraft-Beta-Preview-1-19-10-23
---

**发布于:** 2022年6月15日

## **关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![Minecraft截图](https://feedback.minecraft.net/hc/article_attachments/6944013413389/Screenshot_2022-06-14_134716.jpg)

以下是本周测试版的新内容！如往常一样，请在 [bugs.mojang.com](http://bugs.mojang.com/) 搜索并报告您可能发现的任何漏洞，并向我们发送 [您的反馈](https://aka.ms/MinecraftBetaFeedback)。

# **功能和漏洞修复**

## **悦灵**

- 悦灵手持的物品在黑暗中现在会发光 ([MCPE-153533](https://bugs.mojang.com/browse/MCPE-153533))

## **方块**

- 红树木告示牌现在使用红树木板纹理作为破坏粒子 ([MCPE-156568](https://bugs.mojang.com/browse/MCPE-156568))
- 红树胎生苗现在以随机偏移量放置 ([MCPE-153735](https://bugs.mojang.com/browse/MCPE-153735))
- 铁栏杆和玻璃板现在可以连接到红树根 ([MCPE-153871](https://bugs.mojang.com/browse/MCPE-153871))

## **命令**

- 扩展了 '/locate' 命令，增加了定位结构和定位生物群系
  - 请将您对这个更新命令的任何反馈发送至 [aka.ms/MCBetaLocateCommand](https://aka.ms/MCBetaLocateCommand)

## **深暗之域**

### **黑暗**

- 黑暗效果现在在下界和末地维度中有效
- 熔岩和细雪的迷雾现在优先于黑暗和失明的迷雾 ([MCPE-154928](https://bugs.mojang.com/browse/MCPE-154928))

### **幽匿尖啸体**

- 幽匿尖啸体现在可以检测到骑乘所有类型实体的玩家，包括炽足兽、骷髅马、猪和羊驼 ([MCPE-153814](https://bugs.mojang.com/browse/MCPE-153814))

## **游戏玩法**

- 钟在被任何类型的投射物击中时现在会响起
- 当紫水晶块被投射物击中时，现在会播放击中音效 ([MCPE-137090](https://bugs.mojang.com/browse/MCPE-137090))
- 修复了瓶子无法在水上使用和船无法在水上放置的问题 ([MCPE-156451](https://bugs.mojang.com/browse/MCPE-156451))

### **监守者**

- 监守者的受伤动画在基岩版和Java版之间不再不同 ([MCPE-153967](https://bugs.mojang.com/browse/MCPE-153967))

## **常规**

- 修复了某些平坦世界中的一个漏洞，在加载存档时，如果y=0处有基岩，则低于0的地形会被意外移除 ([MCPE-156679](https://bugs.mojang.com/browse/MCPE-156679), [MCPE-156698](https://bugs.mojang.com/browse/MCPE-156698))

## **用户界面**

- 修复了辅助功能设置中通知持续时间标签的拼写错误 ([MCPE-156901](https://bugs.mojang.com/browse/MCPE-156901))

## **红树林沼泽**

- 红树林沼泽现在更加致密，以更接近Java版的表现 ([MCPE-153748](https://bugs.mojang.com/browse/MCPE-153748))
  - 然而，仍需增加水中红树的密度
- 红树林沼泽中的草方块下方现在有泥土方块 ([MCPE-155414](https://bugs.mojang.com/browse/MCPE-155414))

## **生物**

- 修复了一个导致驯服生物在多人世界中穿过下界传送门时消失的漏洞 ([MCPE-88322](https://bugs.mojang.com/browse/MCPE-88322))
- 修改了鳕鱼、河豚、鲑鱼和热带鱼的生命值，使其为3，以匹配Java版
- 修复了一个破坏史莱姆生成行为的问题，导致史莱姆无法在也是史莱姆区块的沼泽生物群系中生成 ([MCPE-156411](https://bugs.mojang.com/browse/MCPE-156411))

### **流浪商人**

- 修复了一个漏洞，导致行商羊驼对攻击流浪商人的实体不再具有攻击性 ([MCPE-94996](https://bugs.mojang.com/browse/MCPE-94996))

## **稳定性**

- 进入硬币启动附加包屏幕时游戏不再崩溃

## **原版趋同**

- 潜影贝的投射物现在在击中时添加“飘浮”效果，而不是“飘浮 II”
- 河豚在食用时现在给予中毒 II 效果，而不是中毒 IV ([MCPE-105392](https://bugs.mojang.com/browse/MCPE-105392))

# **技术更新**

## **组件**

- 修复了一个漏洞，导致“minecraft:angry”组件的拥有者在没有目标时无法向其朋友广播愤怒。具有此组件的生物现在能够在没有目标且组件的“filters”列表为空时变得愤怒 ([MCPE-94996](https://bugs.mojang.com/browse/MCPE-94996))

## **生物**

- 当生物的击中箱超出生物的边界时，现在可以被投射物击中

# **实验性功能**

## **活动对象属性**

- 将 'values' 字段替换为 'range' 字段，该字段仅支持数组JSON类型。为活动对象属性添加了必需的 'type' JSON 字段，支持的值有 'int'、'float'、'bool' 和 'enum'。属性上的 'default' 和 'range' 字段必须与新 'type' 字段中指定的类型匹配

## **常规**

- 值为16的 *block_light_absorption* 组件的方块不再加载失败
- 将组件 'minecraft:ticking' 重命名为 'minecraft:queued_ticking'
- 将 'minecraft:ticking' 组件的字段 'range' 重命名为 'interval_range'，现在以刻为单位描述，而不是秒
- 将方块可燃组件字段 *flame_odds* 和 *burn_odds* 重命名为 *catch_chance_modifier* 和 *destroy_chance_modifier*
- 添加了使用布尔值设置方块可燃组件的能力，以表示默认可燃或不可燃值
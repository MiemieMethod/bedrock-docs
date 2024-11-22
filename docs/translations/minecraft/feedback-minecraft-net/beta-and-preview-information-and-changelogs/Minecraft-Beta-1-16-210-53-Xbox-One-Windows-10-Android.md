---
标题: Minecraft Beta - 1.16.210.53 (Xbox One/Windows 10/Android)
日期: 2020-12-17T16:42:47Z
更新: 2020-12-17T17:29:43Z
分类: Beta和预览信息及更新日志
标签:
  - beta
  - beta_changelog
链接: https://feedback.minecraft.net/hc/en-us/articles/360053980592-Minecraft-Beta-1-16-210-53-Xbox-One-Windows-10-Android
---

**发布于:** 2020年12月17日

**请在参与Minecraft Beta之前阅读：**

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问真实世界，并且在预览Beta期间无法加入非Beta玩家
- 在Beta中玩的任何世界无法在游戏的先前版本中打开，因此请复制世界以防丢失
- Beta版本可能不稳定，并不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出Beta，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

本周的Beta特别酷，因为我们对细雪进行了更改，并修复了一些重要的漏洞！细雪和山羊都是《洞穴与悬崖》特性，可以通过在此Beta的世界设置中使用实验性特性开关来访问。有关开关的更多信息，请访问[aka.ms/MCExperimentalToggle](https://aka.ms/MCExperimentalToggle)。

** **

**实验性洞穴与悬崖特性**

![Screen_Shot_12-15-20_at_02.50_PM_002.JPG](https://feedback.minecraft.net/hc/article_attachments/360079858472/Screen_Shot_12-15-20_at_02.50_PM_002.JPG)  
  

**细雪**

- 当实体在细雪中移动或落在上面时，细雪块现在会发出粒子
- 冻结效果会逐渐作用于玩家和任何在细雪块中的生物
- 被火焰点燃的生物或玩家将解除冻结效果
- 生存模式下的玩家现在可以使用游戏规则开启/关闭冻结伤害，例如："/gamerule freezedamage false"
- 沉入细雪中的生物现在可以在其中导航
- 着火的实体在踏入细雪时火焰会被扑灭
- 红石粉、火把和物品展示框不再可以放置在细雪上
- 重力方块在落到细雪上时不再破坏
- 在细雪块内，第三人称视角不再被推到角色的头部内部
- 在细雪块内生成的生物不再有在地下生成的风险
- 细雪块不再出现在创造模式物品栏中（[MCPE-105407](https://bugs.mojang.com/browse/MCPE-105407)）
- 细雪不再阻挡投射物（[MCPE-104940](https://bugs.mojang.com/browse/MCPE-104940)）
- 轻量级生物现在可以攀爬和在细雪块中导航
- 兔子、蠹虫和末影螨不会掉落通过细雪块
- 现在可以指定一个生物应避免的方块列表
- 山羊在路径规划时足够聪明，能够避免细雪块
- 在细雪中行走的实体将发出正确的脚步声，无论走在什么方块上
- 穿着皮革靴子现在允许实体攀爬细雪块（[MCPE-105410](https://bugs.mojang.com/browse/MCPE-105410)）
- 细雪块具有独特的交互声音
- 当相机在细雪块内时，会在周围渲染迷雾，并在其上渲染覆盖纹理
- 可以使用铁桶拾取和放置细雪
- 细雪块的纹理与普通雪块略有不同
- 实体可以进入细雪块，但在内部移动速度会减慢
  - 下降伤害被忽略
- 皮革靴子使玩家更容易穿越细雪
- 修复了细雪的遮挡；相邻方块在细雪内不再显得透明

**下界环境音**

- 移动设备玩家现在可以在下界体验环境音（[MCPE-74756](https://bugs.mojang.com/browse/MCPE-74756)）
- 确保通过市场更新Minecraft原声音乐包以听到这些新声音！

**一般**

- 潜影盒在炼药锅中未染色时不再丢失其物品栏（[MCPE-108196](https://bugs.mojang.com/browse/MCPE-108196)）
- 为生物下车添加了新逻辑
  - 这还引入了更细粒度的实体高度检查，允许不同高度的实体有不同的下车位置
- 玩家不再从船等可骑乘物体下车到液体（熔岩或水）中
- 添加了F11作为全屏模式的快捷键
- 登录失败现在有更有帮助的错误信息，并提供错误代码

**游戏玩法**

- 在所有使用相同种子的世界中，相同的箱子现在将始终以相同的顺序生成相同的内容（[MCPE-72432](https://bugs.mojang.com/browse/MCPE-72432)）
- 在区块边界放置的双箱子在打开时不会变得部分透明，也不会导致游戏崩溃（[MCPE-106030](https://bugs.mojang.com/browse/MCPE-106030)）
- 金苹果和附魔苹果在选择时现在有彩色快捷栏文本（[MCPE-64427](https://bugs.mojang.com/browse/MCPE-64427)）

**技术**

- 为'/setblock'、'/fill'和'/clone'命令添加了新的斜杠命令选项，以传递要设置在生成方块上的方块状态列表
- 将'可骑乘组件'属性"rotate_rider_by"更改为自定义生物的功能

**图形**

- 添加了迷雾文档
- 向资源包模板添加了"fogs"文件夹
  - 资源包模板：[aka.ms/MinecraftBetaResources](https://aka.ms/MinecraftBetaResources)
  - 行为包模板：（包含文档）：[aka.ms/MinecraftBetaBehaviors](https://aka.ms/MinecraftBetaBehaviors)
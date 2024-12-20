---
标题: Minecraft Beta - 1.11.0.3 (Xbox One/Windows 10/Android)
日期: 2019-02-28T15:40:57Z
更新: 2019-02-28T18:20:31Z
分类: Beta和预览信息与更新日志
标签:
  - beta
  - mcpe
  - bedrock
  - 1.11.0.3
  - 掠夺者袭击
  - 劫掠兽
  - 前哨站
  - 甜浆果
链接: https://feedback.minecraft.net/hc/en-us/articles/360024397612-Minecraft-Beta-1-11-0-3-Xbox-One-Windows-10-Android
---

**2019年2月28日**

**请在参与Minecraft Beta之前阅读：**

- 您将无法访问领域，并且在预览Beta期间无法加入非Beta玩家。特色服务器可能也不可用。
- Beta仅在Xbox One、Windows 10和Android（Google Play）上提供。有关加入或退出Beta的详细说明，请参见[ms/JoinMCBeta](http://aka.ms/JoinMCBeta)。
- Beta版本可能不稳定，且不代表最终版本的质量。请在加入Beta之前备份您的世界。
- 完成的版本可能不会包含Beta中的所有新特性、变更和修复，以保持稳定性，可能会推迟到后续版本。

**已知问题：**

- 如果在末影龙可见时重新加入一个世界，可能会导致世界无法访问。

**新特性：**

- 添加了更多掠夺者袭击特性：
  - 玩家现在可以在进入村庄时触发袭击，前提是有不祥之兆效果。
  - 玩家在击杀灾厄队长时会获得不祥之兆效果。
  - 袭击状态在会话之间被保存和加载。
  - 劫掠兽在袭击中生成时有时会被灾厄者骑乘。
- 袭击现在使用“居民组件”来跟踪袭击者，即使它们未加载。
- 从袭击中生成的掠夺者、卫道士、女巫和劫掠兽会朝向其村庄移动，这由居民组件决定。
- 为掠夺者巡逻队添加了“跟随”行为。
- 为掠夺者前哨站添加了旗帜的最终艺术作品。
- 添加了新的“/mobevent”命令，以启用或禁用诸如袭击等事件。
- 添加了袭击首领条用户界面。
  - 这只是一个占位符，未来更新中将进行更改。

**变更：**

- 以下特性不再需要实验性游戏玩法开关：
  - 劫掠兽
  - 制箭台
  - 锻造台
  - 掠夺者前哨站
  - 新村庄、村民和僵尸村民
  - 甜浆果
- 猫在村庄中的生成方式发生了各种变化：
  - 猫现在根据村庄中的床数量重生。
  - 猫的数量 = 床数量的1/4。
  - 每个村庄的猫总数上限为10只。
- 更新了村庄英雄和不祥之兆效果的艺术作品。
- 砂轮的爆炸抗性现在与石头台阶相匹配 ([MCPE-42293](https://bugs.mojang.com/browse/MCPE-42293))。
- 流浪商人的羊驼现在无法繁殖。
- 流浪商人的羊驼不能生成为幼体变种。
- 流浪商人现在饮用隐身药水以逃避敌对生物。
- 流浪商人在受到投射物和魔法攻击时会隐藏。
- 村民在早晨醒来时会恢复生命。
- 流浪商人的羊驼现在会对敌对其主人的生物吐口水。
  - 玩家造成的伤害会触发羊驼的仇恨，但不会导致商人隐藏。
- 漏斗现在可以用来填充和清空堆肥桶。
- 水的喷溅药水现在可以用来扑灭营火。

**修复：**

- **崩溃/性能**
  - 修复了在Windows 10上启动游戏时发生的崩溃 ([MCPE-42317](https://bugs.mojang.com/browse/MCPE-42317))。
  - 修复了游戏过程中可能发生的多个崩溃。
  - 在下界传送门上使用拾取块不再导致游戏崩溃 ([MCPE-41735](https://bugs.mojang.com/browse/MCPE-41735))。
  - 给玩家一个圆石墙变种不再导致游戏崩溃 ([MCPE-41657](https://bugs.mojang.com/browse/MCPE-41657))。
  - 修复了在Xbox One上登录或退出Xbox Live时可能发生的崩溃。
  - 修复了在连接到服务器时恢复游戏时可能发生的崩溃。
  - 修复了在踩踏南瓜和西瓜茎时可能发生的崩溃。
  - 修复了在Android上暂停和恢复游戏时发生的多个崩溃。

<!-- -->

- **常规**
  - Xbox上的玩家不再被提示登录Xbox Live，如果他们已经登录过。
  - 玩家在生成到世界时不再窒息于地面 ([MCPE-42310](https://bugs.mojang.com/browse/MCPE-42310))。

<!-- -->

- **游戏玩法**
  - 玩家再次可以通过末地折跃门而不窒息，并且不再遇到世界加载问题 ([MCPE-41533](https://bugs.mojang.com/browse/MCPE-41533), [MCPE-40538](https://bugs.mojang.com/browse/MCPE-40538))。
  - 浆果灌木再次变得刺痛 ([MCPE-41277](https://bugs.mojang.com/browse/MCPE-41277), [MCPE-42407](https://bugs.mojang.com/browse/MCPE-42407))。
  - 平滑石头现在可以再次被烧炼 ([MCPE-42331](https://bugs.mojang.com/browse/MCPE-42331))。
  - 烧炼平滑石头现在会给玩家经验 ([MCPE-41551](https://bugs.mojang.com/browse/MCPE-41551))。
  - 修复了村庄未注册上方有台阶和楼梯的床的问题。
  - 使用VR控制器的玩家在游泳后不再飞行 ([MCPE-39833](https://bugs.mojang.com/browse/MCPE-39833))。
  - 精准采集工具现在可以正确使用到最后一次 ([MCPE-41789](https://bugs.mojang.com/browse/MCPE-41789))。
  - 修复了掠夺者和卫道士队长在死亡时未给予不祥之兆的问题 ([MCPE-42330](https://bugs.mojang.com/browse/MCPE-42330))。

<!-- -->

- **世界生成**
  - 更多村庄生成修复：
    - 结构中的下梯子方块不再缺失。
    - 地下室不再有破损的结构和多余的泥土方块。
    - 修复了有时无法正确生成的雪屋样式房屋。
    - 地板不再缺失方块。
    - 动物围栏不再允许动物逃脱。

<!-- -->

- **生物**
  - 村民在下雨时将使用室内可用的工作地点。
  - 袭击者在试图寻找路径到村庄时不再卡住。
  - 在前哨站生成的灾厄队长不再因巡逻行为而离开。
  - 流浪商人现在正确地拿着交易兴趣物品！
  - 生物在离开船后现在会正确旋转 ([MCPE-41341](https://bugs.mojang.com/browse/MCPE-41341))。
  - 从僵尸转化而来的溺尸现在会攻击玩家。
  - 村民不再卡在灯笼上。

<!-- -->

- **方块**
  - 珊瑚植物和海草在支撑方块被移除时现在会破坏。
  - 盔甲架和砂轮现在可以再次合成 ([MCPE-42350](https://bugs.mojang.com/browse/MCPE-42350))。
  - 平滑和雕刻的石英方块不再有方向性放置 ([MCPE-39074](https://bugs.mojang.com/browse/MCPE-39074))。

<!-- -->

- **图形**
  - 修复了钟纹理的渲染问题。
  - 流浪商人不再有两个右脚。

<!-- -->

- **用户界面**
  - 物品现在可以在物品栏和合成网格中正确分割 ([MCPE-42313](https://bugs.mojang.com/browse/MCPE-42313))。
  - 在Xbox One上写书时，键盘不再遮挡文本输入。

<!-- -->

- **命令**
  - 修复了命令建议图标偏移的问题 ([MCPE-41169](https://bugs.mojang.com/browse/MCPE-41169))。

<!-- -->

- **附加包和脚本引擎**
  - "/replaceitem"现在在替换副手槽中的物品时考虑选择器参数。
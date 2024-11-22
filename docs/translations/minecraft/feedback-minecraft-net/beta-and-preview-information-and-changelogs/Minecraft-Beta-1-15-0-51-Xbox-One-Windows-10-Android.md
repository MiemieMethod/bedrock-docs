---
标题: Minecraft Beta - 1.15.0.51  (Xbox One/Windows 10/Android)
日期: 2020-02-12T15:21:43Z
更新: 2020-02-12T17:06:32Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360039727011-Minecraft-Beta-1-15-0-51-Xbox-One-Windows-10-Android
---

**请在参与Minecraft Beta之前阅读**：

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览Beta时无法加入非Beta玩家
- 在Beta中玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- Beta版本可能不稳定，且不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出Beta，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**趋同：**

- 栅栏门现在可以在没有支撑方块的情况下放置
- 受损的弓可以再次用于制作发射器（[MCPE-55861](https://bugs.mojang.com/browse/MCPE-55861)）
- 现在可以通过交互/右键从花盆中移除花朵
- 实现了绑定诅咒
  - 附魔的头颅和方块具有附魔发光效果
- 掉落的物品现在会变成3D模型并旋转
- 河豚在靠近时现在有中间膨胀状态
  - 我们将在未来的更新中更新缺失的声音
- 玩家种植的大型云杉树下现在会生成灰化土
- 改变了末影之眼的爆炸粒子以匹配Java版
- 调整了铁栏杆物品的纹理，使其与Java版匹配（[MCPE-25802](https://bugs.mojang.com/browse/MCPE-25802)）
- 南瓜可以在没有支撑方块的情况下放置
- 被动生物现在会在它们应该生成的方块上生成（[MCPE-47596](https://bugs.mojang.com/browse/MCPE-47596)）
- 凋零在生成动画期间不再破坏黑曜石（[MCPE-59502](https://bugs.mojang.com/browse/MCPE-59502)）
- 玩家在下雨时现在会获得潮涌能量效果（[MCPE-35941](https://bugs.mojang.com/browse/MCPE-35941)）
- 放置在仙人掌方块上的船现在会受到伤害并破坏

**对于地图制作者和附加包创作者：**

- 大多数攻击目标现在是数据驱动的
  - 为新的行为字段添加了新的文档
- 大多数史莱姆和游泳目标现在是数据驱动的
  - 为新的行为字段添加了新的文档
- 树木生成现在是数据驱动的
- 凋零头颅攻击现在是数据驱动的

**修复：**

- **崩溃/性能**
  - 修复了在游戏过程中可能发生的多个崩溃
  - 修复了在某些资源包屏幕上点击“阅读更多”时可能发生的崩溃
  - 修复了不可见潜影盒的问题，这可能在尝试打开或破坏它们时导致崩溃（[MCPE-55894](https://bugs.mojang.com/browse/MCPE-55894)）
  - 修复了在草方块上投放骨粉时可能发生的崩溃（[MCPE-53033](https://bugs.mojang.com/browse/MCPE-53033)）
  - 修复了因火焰蔓延到蜂箱而导致的崩溃

<!-- -->

- **辅助功能**
  - 修复了可能导致复述功能在Xbox One上重复读取文本的错误

<!-- -->

- **游戏玩法**
  - 为制图台中的锁定地图添加了缺失的文本（[MCPE-58527](https://bugs.mojang.com/browse/MCPE-58527)）
  - 玩家现在可以更顺畅地从游泳过渡到在陆地上奔跑
  - 在奔跑时施放钓鱼竿不再减慢玩家速度（[MCPE-56199](https://bugs.mojang.com/browse/MCPE-56199)）
  - “鸣响警报”成就现在仅由敌对生物触发，而不是玩家
  - 玩家在飞行中卸下鞘翅时，击中箱现在会正确重置
  - 现在可以一致地从甜浆果丛中收集正确数量的浆果（[MCPE-47160](https://bugs.mojang.com/browse/MCPE-47160)）
  - 使用Shift/潜行将允许玩家在游泳时正确向下移动
  - 修复了重生位置，使玩家在睡觉后不再醒来时头部卡在方块中
  - 当从另一个维度返回到活动袭击时，袭击条现在会正确显示
  - 修复了在重新加载世界后阻止红石能量通过木桶的问题（[MCPE-46742](https://bugs.mojang.com/browse/MCPE-46742)）
  - 下落的方块（如沙子）在落到收回的活塞上时不再破坏（[MCPE-20109](https://bugs.mojang.com/browse/MCPE-20109)）
  - TNT爆炸时不再掉落为物品
  - 修复了活板门的碰撞形状（[MCPE-13451](https://bugs.mojang.com/browse/MCPE-13451)）
  - 防止在第一人称视角下玩家鞘翅滑翔时旋转（[MCPE-53092](https://bugs.mojang.com/browse/MCPE-53092)）
  - 爆炸现在可以在水中造成伤害
  - 使用鞘翅高速飞行时不再导致声音抖动（[MCPE-19945](https://bugs.mojang.com/browse/MCPE-19945), [MCPE-52931](https://bugs.mojang.com/browse/MCPE-52931)<u>)</u>
  - 生物在仙人掌方块上时会受到伤害，物品会被摧毁（[MCPE-14303](https://bugs.mojang.com/browse/MCPE-14303)）

<!-- -->

- **生物**
  - 增加了铁傀儡的生成率并修改了生成规则（[MCPE-47157](https://bugs.mojang.com/browse/MCPE-47157)）
  - 修复了驯服马的跳跃动画
  - 修复了烈焰人的路径寻找和导航（[MCPE-45469](https://bugs.mojang.com/browse/MCPE-45469)）
  - 修复了一个错误，允许恶魂在难度设置为和平时存在（[MCPE-53383](https://bugs.mojang.com/browse/MCPE-53383)）
  - 修复了一个问题，导致掠夺者队长不具敌意（[MCPE-44987](https://bugs.mojang.com/browse/MCPE-44987)）
  - 修复了一个问题，允许鱼在冰块上方的流动水中生成
  - 狼现在在更多生物群系中生成（[MCPE-49792](https://bugs.mojang.com/browse/MCPE-49792)）
  - 小型生物不再被楼梯方块创建的缝隙卡住
  - 村民在遭到袭击时不再在房子里乱跑
  - 生物不再在进入矿车时开始抖动
  - 守卫者和远古守卫者不再在试图到达水时漂浮在空中（[MCPE-33641](https://bugs.mojang.com/browse/MCPE-33641)）
  - 调整了鱿鱼的生成率和上限
  - 溺尸不再在没有装备三叉戟的情况下掉落三叉戟（[MCPE-32731](https://bugs.mojang.com/browse/MCPE-32731)）
  - 修复了一个错误，阻止猫在玩家的床上睡觉
  - 雪傀儡现在可以在栅栏方块后面尝试向生物发射雪球（[MCPE-24840](https://bugs.mojang.com/browse/MCPE-24840)）
  - 修复了一个错误，允许僵尸村民破坏铁门（[MCPE-43725](https://bugs.mojang.com/browse/MCPE-43725)）
  - 坐着的生物不再滑动并繁殖（[MCPE-62160](https://bugs.mojang.com/browse/MCPE-62160)）

<!-- -->

- **物品**
  - 未装填的弩不再在物品栏中显示错误的图标（[MCPE-53545](https://bugs.mojang.com/browse/MCPE-53545)）

<!-- -->

- **图形**
  - 停止副手盾牌动画和弓动画同时播放（[MCPE-41262](https://bugs.mojang.com/browse/MCPE-41262)）
  - 修复了一个错误，导致Xbox One主机上的立方体贴图无法正确渲染
  - 幼狐持有的物品现在正确渲染（[MCPE-52885](https://bugs.mojang.com/browse/MCPE-52885)）
  - 染色玻璃在地图上现在具有正确的颜色（[MCPE-25702](https://bugs.mojang.com/browse/MCPE-25702)）
  - 装备附魔鞘翅时将显示附魔发光效果（[MCPE-23020](https://bugs.mojang.com/browse/MCPE-23020)）

<!-- -->

- **用户界面**
  - 修复了一个错误，有时会阻止加载屏幕提示正确显示
  - 实体和方块现在在结构方块的预览中一致显示
  - 离开船的提示框现在在各个平台上保持一致
  - 当将骨粉指向草方块或水下方块时，“生长”控制器的提示框现在会显示

<!-- -->

- **命令**
  - 更新了'/scoreboard'命令描述中的语法，使其与其他命令一致
  - 立即效果现在在与'/effect'命令一起使用时使用刻而不是秒（[MCPE-43393](https://bugs.mojang.com/browse/MCPE-43393)）

<!-- -->

- **附加包**
  - 实现了一个修复，以确保玩家的坐骑更新所有骑乘者，以确保所有骑乘者的旋转一致平滑
  - 'delayed_attack'行为不再导致生物在失去目标时冻结
  - 物品标签现在可以在UI中使用'/gamerule' showtags切换
  - 'on_unleash'事件在从栅栏释放时现在正确触发
  - '创建新世界'按钮文本现在使用全局颜色组件

<!-- -->

- **角色创建器**
  - 修复了一个问题，可能导致某些发型下翅膀服装部件消失
  - 修复了默认玩家模型，以克服在角色创建器中选择不同高度和大小时可能出现的一些纹理问题
  - 各种用户界面修复
  - 现在可以通过角色创建器的更衣室查看成就屏幕

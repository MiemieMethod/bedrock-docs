---
标题: Minecraft Beta - 1.14.0.1 (Xbox One/Windows 10/Android)
日期: 2019-10-09T14:01:28Z
更新: 2019-10-09T15:41:22Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360034989811-Minecraft-Beta-1-14-0-1-Xbox-One-Windows-10-Android
---

**在参与Minecraft Beta之前请阅读**：

- 加入测试版将用一个正在开发中的Minecraft版本替换你的游戏
- 你将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)获取详细说明

### **新特性：**

- **新增蜜蜂！**
  - 蜜蜂是可爱、毛茸茸的中立生物
  - 不要伤害它们，它们不想伤害你
  - 如果蜜蜂叮了你，它会把刺留在你身上并最终死去，不会掉落任何东西 :(
  - 蜜蜂喜欢美丽的花朵，终其一生都在从中采集花粉
  - 采集花粉后，蜜蜂会飞回它们的巢穴
  - 蜜蜂通过将花粉带回巢穴来帮助你种植作物
  - 可以用花朵繁殖蜜蜂
  - 如果蜜蜂找不到花蜜，过一段时间后它会回家待一会儿
  - 如果蜜蜂没有巢穴，它会四处游荡，直到找到一个可以使用的巢穴
  - 蜜蜂不喜欢下雨，晚上会睡觉。在这些情况下，它们会回到巢穴

<!-- -->

- **新增蜂箱和蜂巢**
  - 蜂巢自然生成于繁花森林、平原和向日葵平原生物群系中
  - 当蜜蜂访问巢穴并在不被打扰的情况下完成旅程时，蜂蜜的等级会增加
  - 蜂蜜的最大等级为5级
  - 蜂箱由玩家使用蜜脾和木板制作
  - 使用精准采集工具获取存有蜜蜂的方块
  - 蜂巢会被摧毁，除非你使用精准采集
  - 当蜂蜜满时，使用剪刀可以获得蜜脾
  - 当蜂蜜满时，使用瓶子可以获得蜂蜜瓶
  - 营火的烟雾可以让蜜蜂平静——在巢穴/蜂箱下放置一个以保持它们处于放松状态
  - 兼容红石！

<!-- -->

- **新增蜜脾和蜂蜜瓶**
  - 在满蜂蜜的蜂箱或蜂巢上使用空玻璃瓶可以获得蜂蜜瓶！
  - 发射器现在可以将瓶子装满水和蜂蜜
  - 发射器现在可以从蜂巢和蜂箱剪取蜜脾

<!-- -->

- **新增蜜脾块**
  - 一种可以用蜜脾制作的装饰性方块！

<!-- -->

- **新增蜂蜜块**
  - 大幅降低移动速度和跳跃高度，但也减少跌落伤害
  - 你可以“滑”下蜂蜜块的墙面以减缓下落速度（跑酷真棒！）
  - 蜂蜜块的效果可以延续到高于其\< 1个方块的地方
  - 当蜂蜜块被活塞推动时，邻近的方块也会被推动
  - 当蜂蜜块被活塞推动时，顶部的实体也会随之移动
  - 支持粘性方块。使用‘BlockProperty::PreventsJumping’使得路径寻找者在这些方块上不会跳跃，玩家在这些方块上也无法跳跃。还连接了一个级别事件，当被阻止跳跃时会生成地形粒子并播放跳跃阻止的方块声音**

### **更改：**

- 现在可以在北极熊、鹦鹉、豹猫和海豚身上使用拴绳（[MCPE-46866](https://bugs.mojang.com/browse/MCPE-46866)）
- 调整动物掉落的经验值以匹配Java版
  - 大多数动物现在被杀死时会掉落1-3经验值，但海豚现在掉落0经验值

### **此测试版已知问题将在未来更新中修复：**

- 装备的盔甲在玩家角色上不可见

### **修复：**

- **崩溃/性能**
  - 修复了在游戏过程中可能发生的多个崩溃
  - 修复了海带生长导致特定区块出现延迟的问题（[MCPE-50175](https://bugs.mojang.com/browse/MCPE-50175)）

<!-- -->

- **一般**
  - 修复了某些资源包中玻璃的破坏动画
  - 披风在皮肤选择器中现在正确显示
  - 修复了阻止“传送我上去”成就获得的问题（[MCPE-21425](https://bugs.mojang.com/browse/MCPE-21425)）
  - 修复了导致某些皮肤显示为纯白披风的问题（[MCPE-52005](https://bugs.mojang.com/browse/MCPE-52005)）
  - 修复了一个渲染距离问题，可能导致旧风格（有限）世界在玩家在该世界的特定角落登出时无法正确加载
  - 修复了导致某些披风在角色创建器中无法正确缩放到皮肤的问题
  - 修复了导致角色创建器中的某些选择变得无响应的问题
  - 修复了导致在外星世界市场包中显示脚本错误消息的问题

<!-- -->

- **游戏玩法**
  - 矿车的声音现在正确加载和播放
  - 含水方块不再被同一区块中的其他红石电路计时
  - 在触摸屏设备上，盔甲再次可以从创造模式物品栏正确装备（[MCPE-52413](https://bugs.mojang.com/browse/MCPE-52413)）
  - 修复了导致弩在装填后立即发射的问题（[MCPE-52179](https://bugs.mojang.com/browse/MCPE-52179)）
  - 冰霜行者魔咒再次可以正确冻结水（[MCPE-52788](https://bugs.mojang.com/browse/MCPE-52788)）
  - 修复了一个可能导致玩家在创造模式中骑乘实体后从天而降的错误（[MCPE-52957](https://bugs.mojang.com/browse/MCPE-52957)）
  - 箭矢或三叉戟在被盾牌反弹后不再穿过地面（[MCPE-44721](https://bugs.mojang.com/browse/MCPE-44721)）
  - 耕地方块再次在玩家跳跃时恢复为泥土方块
  - 在创造模式中将盔甲放置在盔甲架上不再同时装备在玩家身上

<!-- -->

- **生物**
  - 减少狐狸的攻击半径以匹配Java版
  - 狐狸手持的物品不再隐形（[MCPE-51993](https://bugs.mojang.com/browse/MCPE-51993)）
  - 马现在再次使用正确（更新的）模型
  - 改进了飞行生物的路径寻找准确性

<!-- -->

- **物品**
  - 指南针和时钟在快捷栏中现在再次正确动画化（[MCPE-52901](https://bugs.mojang.com/browse/MCPE-52901)）

<!-- -->

- **用户界面**
  - 装备的地毯在羊驼物品栏中现在再次正确显示

<!-- -->

- **附加包和脚本引擎**
  - 自定义凋零实体创建时，boss生命条现在正确显示
  - 自定义实体在骑乘时再次正确显示生命条
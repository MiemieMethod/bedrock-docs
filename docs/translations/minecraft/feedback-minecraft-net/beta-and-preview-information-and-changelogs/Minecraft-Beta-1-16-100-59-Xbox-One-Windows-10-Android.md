---
标题: Minecraft Beta - 1.16.100.59 (Xbox One/Windows 10/Android)
日期: 2020-10-08T17:29:43Z
更新: 2020-10-08T17:35:35Z
类别: Beta和预览信息及更改日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360050305112-Minecraft-Beta-1-16-100-59-Xbox-One-Windows-10-Android
---

**在参与Minecraft Beta之前请阅读：**

- 加入Beta将会用一个正在开发中的Minecraft版本替换你的游戏
- 你将无法访问Realm，并且在预览Beta期间无法加入非Beta玩家的游戏
- 在Beta期间游玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的备份以防丢失
- Beta构建可能不稳定，并不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出Beta，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**更改**

- 在此Beta中重新启用了RenderDragon

**修复**

**性能和稳定性**

- 修复了游戏过程中发生的多个崩溃
- 修复了在飞行或移动游戏世界时偶尔发生的崩溃

**方块**

- 告示牌不再可以放置在末地烛上
- 只能通过命令获得的方块不再显示占位符提示框（[MCPE-100760](https://bugs.mojang.com/browse/MCPE-100760)）
- 修复了绯红菌索、诡异菌索和下界苗在下界中未生成的问题（[MCPE-100614](https://bugs.mojang.com/browse/MCPE-100614)）
- 从主机版存档转换的墙现在正确连接

**物品**

- 当游戏规则“显示标签”设置为false时，物品锁定图标和提示框不再出现
- 修复了导致某些物品配方在合成窗口中缺失的问题（[MCPE-100257](https://bugs.mojang.com/browse/MCPE-100257)）
- 与盔甲架交互后，盔甲不再卡在快捷栏中（[MCPE-84368](https://bugs.mojang.com/browse/MCPE-84368)）
- 将书与羽毛笔重新添加到创造模式物品栏中（[MCPE-100361](https://bugs.mojang.com/browse/MCPE-100361)）

**用户界面**

- 修复了暂停菜单中的“个人资料”按钮未正确调整大小的问题

**技术更改**

**命令**

- 添加了使用'/camerashake'选择不同震动类型的功能
- 修复了自定义物品未添加到创造模式物品栏的问题，因此无法与命令一起使用
- 修复了使用'/schedule'排队的请求在执行时未清除的问题，并在重新进入存档时执行
- 向'/schedule on_area_loaded'命令添加了一个重载，允许你通过指定中心和半径来跟踪一个圆形区域。还添加了请求队列的序列化
- 修复了'/schedule'命令的问题，该命令在实际加载之前就认为区域已加载，并且现在该命令遵循排队所在的维度

**添加方块**

- 修复了方块同步的问题
- 添加方块内容不允许使用原版方块标识符以避免内容冲突
- 'SetBlockAtPos'不会修改来自传入参数的方块位置

**组件**

- 添加了一个可以通过'give'和'replaceitem'命令应用于物品的物品锁定组件。此组件防止物品从玩家的物品栏中被移除、掉落或合成。使用示例：`/give @s apple 1 0 {"item_lock": {"mode": "lock_in_inventory"}}`
- 添加了一个可以通过'give'和'replaceitem'命令应用于物品的槽位锁定组件。此组件防止物品在玩家的物品栏中的槽位被移动或移除、掉落或合成。使用示例：'/give @s apple 1 0 {"item_lock": {"mode": "lock_in_slot"}}'
- 添加了一个死亡保留组件，可以通过'give'和'replaceitem'命令应用于物品。此组件防止物品在玩家死亡时掉落。使用示例：'/give @s apple 1 0 {"keep_on_death": {}}'

**物品图标组件**

- 物品现在有一种简单的方法设置在用户界面中显示的物品图标
- 组件变量
  - "texture": 用作物品图标的图标图像的完整路径。无默认值
  - "frame": 在运行时执行的Molang脚本，以确定图标的当前帧。可以是常量，默认值为：0
  - "legacy_texture_id": 用于传统物品的纹理名称。无默认值
  - "legacy_frame": 在运行时执行的Molang脚本，以确定图标的当前帧。可以是常量，默认值为：0

**数据驱动方块**

- 添加了BlockDisplayNameComponent，以允许在本地化表中配置显示名称
- 使'entity_collision'和'pick_collision'考虑方块的旋转
- 修复了使用自定义事件生成的生物未运行动画的问题
- 添加了对'on_interact'触发器组件的支持
- 改进了对'on_interact'修改所用物品的支持，例如更改耐久度或设置为另一个物品
- 修复了'on_interact'在事件响应杀死玩家时会重复使用的物品的问题
- 修复了自定义物品在客户端/服务器场景中未正常工作或渲染的问题
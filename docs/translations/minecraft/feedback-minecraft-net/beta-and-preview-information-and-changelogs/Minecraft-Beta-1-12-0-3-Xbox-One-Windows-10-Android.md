---
标题: Minecraft Beta - 1.12.0.3 (Xbox One/Windows 10/Android)
日期: 2019-05-01T15:25:24Z
更新: 2019-05-01T16:25:06Z
分类: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360027543692-Minecraft-Beta-1-12-0-3-Xbox-One-Windows-10-Android
---

**发布于:** 2019年5月1日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问真实世界，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**更改：**

- 主菜单上的“商店”按钮已更名为“市场”

**对于附加包创作者：**

- 行为包模板再次包含“spawn_rules”文件夹
- 行为包模板中添加了配方和物品的JSON文件
- 在[aka.ms/MinecraftAddons](https://aka.ms/MinecraftAddons)获取最新的行为包模板

**修复：**

- **崩溃/性能**
  - 修复了在游戏过程中可能发生的多个崩溃
  - 修复了加载某些市场世界时可能发生的崩溃
  - 改善了村庄和村民工作地点的性能
  - 修复了脚本引擎中出现的内存泄漏

<!-- -->

- **常规**
  - 更新了主菜单的闪烁文本
  - 修复了消耗堆叠中最后一个物品以解锁成就时可能导致成就未解锁的问题

<!-- -->

- **游戏玩法**
  - 玩家模型的手臂和腿不再翻转。哎呀！([MCPE-44718](https://bugs.mojang.com/browse/MCPE-44718))
  - 当满足要求时，讨价还价者成就再次解锁
  - 村民交易现在在适用时正确从第二个槽位中移除物品
  - 持有时，盾牌和三叉戟不再不可见 ([MCPE-44647](https://bugs.mojang.com/browse/MCPE-44647))
  - 玩家在离开船后不再透视世界 ([MCPE-42593](https://bugs.mojang.com/browse/MCPE-42593))

<!-- -->

- **生物**
  - 驯服的燕尾服猫现在使用正确的纹理 ([MCPE-43527](https://bugs.mojang.com/browse/MCPE-43527))
  - 流浪猫不再能够在从1.10版本转换的世界中占用村庄的床 ([MCPE-44299](https://bugs.mojang.com/browse/MCPE-44299))
  - 村民在使用模板世界（包括市场世界）时现在总是生成为V1
  - 女巫在攻击时不再跳跃
  - 修复了各种皮肤包的几何动画问题
  - 刷怪笼中的恶魂旋转模型现在是正确的大小
  - 改善了可变大小生物的路径规划
  - 僵尸和卫道士现在更快地破坏门 :D
  - 修复了流浪商人的灰化土和珊瑚交易
  - 制箭师现在交易16支箭而不是5支
  - 更改了屠夫的熟兔肉交易成本
  - 皮匠的鞍交易从10个绿宝石降低到6个

<!-- -->

- **方块**
  - 流动的熔岩再次在水的冲击下变成圆石 ([MCPE-43990](https://bugs.mojang.com/browse/MCPE-43990))
  - 霜冰块现在可以被破坏 ([MCPE-41256](https://bugs.mojang.com/browse/MCPE-41256))
  - 台阶和其他非实心方块再次阻止草在泥土上生长 ([MCPE-42975](https://bugs.mojang.com/browse/MCPE-42975))
  - 原木再次可以用斧头变成去皮原木 ([MCPE-44680](https://bugs.mojang.com/browse/MCPE-44680))
  - T型交叉口的铁轨再次在红石供电时改变方向 ([MCPE-44735](https://bugs.mojang.com/browse/MCPE-44735))
  - 修复了烟熏炉底部没有正确纹理的问题 ([MCPE-43944](https://bugs.mojang.com/browse/MCPE-43944))
  - 盔甲架再次可以持有盔甲架物品

<!-- -->

- **物品**
  - 配方书中现在正确显示制作彩色旗帜所需的羊毛颜色
  - 修复了多个物品在使用时未损失耐久度的问题

<!-- -->

- **图形**
  - 玩家在第一人称视角下吃食物后，手臂不再位移 ([MCPE-40135](https://bugs.mojang.com/browse/MCPE-40135))
  - 堆肥桶的生长粒子现在出现在正确的位置
  - 修复了多个纹理包中流动的熔岩和水的动画纹理
  - 竹子叶子现在更亮，并与Java版本的纹理匹配 ([MCPE-42635](https://bugs.mojang.com/browse/MCPE-42635))
  - 修复了门和活板门上有时出现的灰色纹理

<!-- -->

- **用户界面**
  - 尝试合并相同物品的堆叠时，触控控制不再交换它们
  - 在触控控制中，切换到和从副手槽位时物品不再丢失 ([MCPE-44706](https://bugs.mojang.com/browse/MCPE-44706))
  - 制图台上的“如何玩”按钮现在指向正确的屏幕
  - 甜浆果在高亮时不再在快捷栏中消失
  - 杀死流浪商人的羊驼不再显示他们的物品栏

<!-- -->

- **命令**
  - 在'/give'命令中移除了“tile”前缀 ([MCPE-44667](https://bugs.mojang.com/browse/MCPE-44667))
  - 在创造模式物品栏中不可用的方块和实体在作为斜杠命令参数时不再需要“minecraft”命名空间
  - 命令现在可以在命令方块上自动完成，而无需以/开头 ([MCPE-44679](https://bugs.mojang.com/browse/MCPE-44679))

<!-- -->

- **附加包和脚本引擎**
  - 'minecraft:entity_use_item'文档现在正确生成
  - 修正了方块事件描述
  - 自定义实体现在正确重新评估当前目标的有效性
  - 'getBlocks'现在返回一个3D数组的方块对象
  - 修复了新'watter_movement'组件中实体的组件名称不正确的问题
  - getBlock和getBlocks现在正确处理在给定活动对象位置（或任何非整数位置）时获取方块

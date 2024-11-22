---
title: Minecraft Beta - 1.12.0.2 (Xbox One/Windows 10/Android)
date: 2019-04-17T14:28:46Z
updated: 2019-04-17T15:57:35Z
categories: Beta和预览信息和更新日志
tags:
  - beta
  - bedrock
  - 1.12.0.02
link: https://feedback.minecraft.net/hc/zh-cn/articles/360027059411-Minecraft-Beta-1-12-0-2-Xbox-One-Windows-10-Android
---

**2019年4月17日**

**在参加Minecraft Beta之前，请阅读：**

- 加入beta测试将用Minecraft的开发中版本替换您的游戏
- 在预览beta测试期间，您将无法访问Realms，并且无法加入非beta测试的玩家
- 在beta测试期间游玩的任何世界无法在游戏的以前版本中打开，请复制世界以防丢失
- Beta构建版本可能不稳定，且不代表最终版本的质量
- Beta测试仅适用于Xbox One、Windows 10和Android（Google Play）。要加入或退出beta测试，请参阅aka.ms/JoinMCBeta获取详细说明

**此beta版本中已知的问题，将在未来更新中修复：**

- 生物头颅几何问题—某些生物如猫和村民在睡眠或坐下时可能头颅错位（[MCPE-44648](https://bugs.mojang.com/browse/MCPE-44648)）
- 三叉戟和盾牌在玩家手持时可能不可见（[MCPE-44647](https://bugs.mojang.com/browse/MCPE-44647)）

**新特性：**

- 物品实例ID现可在客户端和服务器之间同步
- 为命令方块增加了自动完成功能
- 增加了spawnRadius gamerule
  - 玩家可以在他们的世界中指定一个名为spawnRadius的数值。这个概念借鉴了Java Edition的实现方式。它允许玩家指定一个0到32之间的数字，用于创建一个允许生成的区域。因此，spawn radius为27的区域比radius为12的大。玩家将在该半径内的随机位置生成
- 在基岩专用服务器上启用了内容日志记录
- 为命令方块增加了延迟选项
  - 可以使用新字段在命令方块中添加延迟。此延迟的刻数为红石刻

**针对地图制作人员和附加包创建者：**

- 现在可以使用附加包添加新物品
- 世界模板中现在可以启用和禁用生物事件
- 可以添加动画和粒子效果，而无需链接到实体
- 可以通过脚本自定义物品栏、盔甲和手持容器
- 现在可以通过动画事件触发声音效果
- 为脚本API新增了executeCommand
- 为与物品交互的脚本事件添加了Scripting events，例如：
  - 物品被捡起
  - 物品被丢弃
  - 携带中的物品发生变化
- 增加了一次性动画支持，允许在实体上执行单个动画
- 粒子发射器现在可以触发Scripting Events
- 更新了Actor Events的文档，以记录资源包中客户端侧使用的actor events
- 新增区块组件现在使用JSON架构
- 创建了一个查看内容日志错误的屏幕
  - 可以使用Ctrl+H打开日志屏幕，或者通过设置→个人资料打开
- 增加了允许在本地运行静态验证脚本的代码
- 现在可以通过脚本添加自定义区块
  - 这目前仍是一个“进行中”的功能，未来更新将增加更多功能
  - 目前自定义区块只能通过额外的JSON脚本添加
  - 自定义区块只能使用斜杠命令放置

<!-- -->

- **新增数据驱动粒子：**
  - 羊驼唾沫
  - 大型爆炸
  - 彩色火焰
  - 红石粉
  - 下落尘土
  - 熔岩
  - 附魔台
  - 潮涌核心
- **新增数据驱动动画：**
  - 狼
  - 猛咬攻击
  - 箭
  - 潜影弹
  - 弓
  - 水
- **更新文档以包含破坏性变更部分**
- **物品API V0**
  - 基本的与物品相关的事件已暴露给脚本API。这包括：
  - actor_acquired_item
  - actor_carried_item_changed
  - actor_dropped_item
  - actor_use_item
  - actor_equipped_armor
- **物品栏API V0**
  - 基本的物品栏事件已暴露给脚本API。这包括：
  - inventory_container
  - armor_container
  - hand_container（注意手持容器将同时获取主手和副手）
  - hotbar_container
- **区块API V0**
  - 新的区块事件和两个新的API已包含用于查询区块。这包括：
  - APIs
  - getBlock(常加载区域, x, y, z)
  - getBlock(常加载区域, PositionObject)
  - getBlocks(常加载区域, x min, y min, z min, x max, y max, z max)
  - getBlocks(常加载区域, Minimum PositionObject, Maximum PositionObject)
  - Events
  - block_destruction_started
  - block_destruction_stopped
  - piston_moved_block
  - player_destroyed_block
  - player_placed_block
- **executeCommand API**
  - 允许脚本API获取斜杠命令的结果
- **事件数据API**
  - 允许创建者创建事件数据，注册并传递给事件函数
- **更新了演示包**

**修复：**

**崩溃/性能**

- 修复了可能在游戏过程中发生的几个崩溃问题
- 改善了多人游戏中的区块加载性能
- 进一步提高了使用带命令选择器时的性能
- 修复了在Xbox上切换玩家时可能发生的崩溃
- 缓存资源包不再在Nintendo Switch上导致滞后（[MCPE-36976](https://bugs.mojang.com/browse/MCPE-36976)）
- 修复了在某些Windows 10设备上启动游戏时可能发生的崩溃
- 修复了在加入Realm时加载某些互动区块（如床、箱子、熔炉）时可能发生的崩溃
- 修复了在海底神殿中与远古守卫者战斗时可能发生的崩溃
- 修复了携带忠诚附魔的三叉戟投掷时可能发生的崩溃
- 修复了有时在退出游戏时可能发生的崩溃

<!-- -->

- **通用**
  - 当多个运营商尝试调整玩家权限时，玩家权限现在正确应用
  - 射入区块的箭在重新加载世界时保持位置
  - 白天云不再在更改时间时尝试生成过多粒子（[MCPE-39595](https://bugs.mojang.com/browse/MCPE-39595)）
  - 市场资源包在世界编辑菜单中下载后立即应用（[MCPE-33121](https://bugs.mojang.com/browse/MCPE-33121)）
  - '始终白天'切换现在正确动画并显示正确设置（[MCPE-43304](https://bugs.mojang.com/browse/MCPE-43304)）
  - 水流过绳索后不再留下流动的水（[MCPE-36343](https://bugs.mojang.com/browse/MCPE-36343)）
  - 通过命令杀死钓鱼钩后，玩家现在可以再次投掷钓鱼钩，无需双击右键
  - 在Nintendo Switch上调整网络设置时，屏幕阅读器提示不再每次出现
  - 移除了不必要的Xbox Live登录通知

<!-- -->

- **游戏玩法**
  - 市场优惠页面现在可以显示超过25个物品
  - 在村民交易窗口中分布在槽位之间的物品仍然计算为总交易量
  - 现在可以再次在未点亮的红石矿石上放置区块（[MCPE-44305](https://bugs.mojang.com/browse/MCPE-44305)）
  - 世界设置现在在不同Xbox设备之间正确同步
  - 仅参与过袭击的玩家现在在Realms中看到并获得英雄效果
  - 用闪光和滞留药水击中钟后，钟会响
  - 生物刷怪笼现在仅在光照等级低于7时生成生物（[MCPE-42427](https://bugs.mojang.com/browse/MCPE-42427)）
  - 被活塞推动时，可可豆现在会破碎和掉落（[MCPE-41868](https://bugs.mojang.com/browse/MCPE-41868)）
  - 修复了与末地折跃门相关的几个问题。现在使用时应正确传送玩家到安全位置（[MCPE-43176](https://bugs.mojang.com/browse/MCPE-43176)、[MCPE-43177](https://bugs.mojang.com/browse/MCPE-43177)、[MCPE-19699](https://bugs.mojang.com/browse/MCPE-19699)）
  - 效率镐现在以更快的速度破坏浮冰（[MCPE-23648](https://bugs.mojang.com/browse/MCPE-23648)）
  - 被治疗的玩家仍然可以被TNT击退
  - 被治愈的村民现在保留他们的职业（[MCPE-42348](https://bugs.mojang.com/browse/MCPE-42348)）
  - 砂轮现在正确地合并和修复两个损坏的物品
  - 现在可以在触摸设备上使用充能弩与区块互动
  - 只有杀死掠夺者头目时，才会获得不祥之兆效果；使用弓或伤害药水造成非致命伤害时则不会
  - 修复了某些区块在游戏重启前无法放置的各种情况

<!-- -->

- **世界生成**
  - 修复了专用服务器和Realms上可能导致错误区块类型生成的错误
  - 调整了村庄中的工作站数量

<!-- -->

- **生物**
  - 被治愈的村民现在保留他们的职业
  - 卫道士现在可以在袭击期间正确地在地毯上导航
  - 凋零在重新加载世界时不再播放其生成动画（[MCPE-32415](https://bugs.mojang.com/browse/MCPE-32415)）
  - 生物现在不会在酿造台上导航
  - 增加了指示村民不想交易的声音（如在袭击期间）
  - 掠夺者头目即使在世界重新加载时也会正确掉落旗帜
  - 生物现在可以在双台阶上生成（[MCPE-30765](https://bugs.mojang.com/browse/MCPE-30765)）
  - 重新添加了僵尸村民声音
  - 生物在梯子上导航时不再卡住（[MCPE-43034](https://bugs.mojang.com/browse/MCPE-43034)）
  - 增加了新的流浪商人声音
  - 使用标签命令将普通掠夺者转换为头目时，现在会正确显示旗帜
  - 召唤者在“移动到村庄”目标中不再移动过快
  - 正在与玩家交易的村民在袭击钟响时不再逃跑和隐藏
  - 牧师现在可以正确地向他们的工作站导航

<!-- -->

- **区块**
  - 现在不能在潮涌核心区块上放置脚手架（这与Java版本一致）
  - 钟在被玩家击中时现在会向玩家摆动（与Java版本一致）（[MCPE-42469](https://bugs.mojang.com/browse/MCPE-42469)）

<!-- -->

- **物品**
  - 掉落的物品不再阻止在铁轨上放置矿车
  - 从酿造台移除时，空玻璃瓶现在会正确堆叠（[MCPE-42175](https://bugs.mojang.com/browse/MCPE-42175)）
  - 盾牌在物品展示框中不再显得过于明亮（[MCPE-41222](https://bugs.mojang.com/browse/MCPE-41222)）
  - 修复了海草纹理亮度问题（[MCPE-34795](https://bugs.mojang.com/browse/MCPE-34795)）
  - 木桶物品现在在创造模式物品栏中处于正确位置（[MCPE-43946](https://bugs.mojang.com/browse/MCPE-43946)）

<!-- -->

- **图形**
  - 修复了某些村民皮肤上的z-fighting纹理问题
  - 校正了狼上拴绳的位置
  - 音符盒粒子现在正确对应播放的音符
  - 修复了缺失的僵尸村民皮肤
  - 耕地现在具有正确的侧面和底部纹理（[MCPE-42746](https://bugs.mojang.com/browse/MCPE-42746)）
  - 修复了门和活板门的纹理问题（[MCPE-43173](https://bugs.mojang.com/browse/MCPE-43173)）
  - 染色皮革马盔甲颜色不再影响其他马盔甲（[MCPE-43230](https://bugs.mojang.com/browse/MCPE-43230)）

<!-- -->

- **用户界面**
  - 为讲台UI添加了控制器提示
  - 调整了制图UI以适应使用经典UI时的Android屏幕
  - 如果玩家站得太远，村民交易UI现在不再打开和关闭
  - 为讲台UI添加了控制器提示

<!-- -->

- **附加包和脚本引擎**
  - 修复了可能导致玩家漂浮的脚本错误
  - 中键拾取现在在通过附加包添加的非原版实体上正常工作（[MCPE-38205](https://bugs.mojang.com/browse/MCPE-38205)）
  - ScriptAttackComponent和ScriptCollisionBoxComponent现在正确检索更新的数据
  - 在游戏循环中运行的函数现在使用具有游戏大师权限的origin，而不是拥有者权限
    - 为ServerCommandOrigin添加了一个新的构造函数参数，以便Function Manager可以创建一个具有升级权限的实例
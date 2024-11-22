---
标题: Minecraft Beta - 1.16.100.56 (Xbox One/Windows 10/Android)
日期: 2020-09-17T09:26:14Z
更新: 2020-09-18T14:02:15Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360049825031-Minecraft-Beta-1-16-100-56-Xbox-One-Windows-10-Android
哈希:
  技术变更: technicalchanges
---

**发布于:** 2020年9月17日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realms，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

在本周的测试版中，我们修复了几个重要问题，并且还包含了一些内容创作者会发现有用的技术变更！请记得继续向我们发送您的漏洞报告，地址是[bugs.mojang.com](https://bugs.mojang.com/browse/MCPE)!

# **漏洞修复**

**性能和稳定性**

- 修复了在游戏过程中可能发生的多个崩溃
- 修复了Xbox One启动时的崩溃

**成就屏幕**

- 成就屏幕上现在正确显示游戏时间（[MCPE-66331](https://bugs.mojang.com/browse/MCPE-66331)）
- 当启用叙述时，按下游戏手柄的左键可以导航到摘要
- 更新了成就列表和成就奖励的输入说明
- 打开成就详细信息屏幕时，现在会叙述“屏幕”
- 修复了我们计算玩家获得的奖励数量的方式
- 当数据已被获取时，即使在超时后也显示成就
- 使用非主鼠标按钮时不播放点击声音
- 修复了即使没有内容可滚动时滚动条仍然出现的问题
- 在使用游戏手柄时为焦点导航添加了加速
- 在从“全部”标签切换时修复了焦点持久性
- 修复了鼠标“后退按钮”支持，以便从成就屏幕返回
- 修复了Escape按钮支持，以便从成就屏幕返回
- 修复了选项卡的输入说明即使在选中选项卡时仍显示为“打开”的问题

**一般**

- 修复了文本转语音未能读取各种屏幕上的消息
- 修复了使用/clear命令时地图未出现在物品列表中的问题
- 修复了在退出登录提示屏幕后，登录按钮变得无响应的问题

**游戏玩法**

- 圆石现在显示为石制工具的默认材料（[MCPE-71843](https://bugs.mojang.com/browse/MCPE-71843)）
- 减少并重新引入了袭击号角声音的线性衰减（[MCPE-85593](https://bugs.mojang.com/browse/MCPE-85593)）
- 现在在破坏和放置物品展示框时播放正确的声音（[MCPE-98901](https://bugs.mojang.com/browse/MCPE-98901)）

# **技术变更**

**记录物品组件**

- 物品现在可以制作成记录，以在唱片机中播放音乐

**组件变量**

- sound_event：一个字符串值，对应于游戏代码中的声音事件。此字符串必须为以下之一，以便播放音乐：“13”、“cat”、“blocks”、“chirp”、“far”、“mall”、“mellohi”、“stal”、“strad”、“ward”、“11”、“wait”、“pigstep”
- duration：一个浮点值，决定粒子从唱片机方块中生成的持续时间，应大致匹配声音事件的长度
- comparator_signal：一个整数值，表示模拟信号的强度，供比较器方块使用

**示例**

当添加到唱片机方块时，将播放“record.chirp”的声音片段

- 示例1：“minecraft:record”：{ “sound_event”： “chirp”， “duration”： 185.0， “comparator_signal”： 4 }

**物品名称**

- 重命名物品以与Java版物品列表保持一致，详见[这里](https://minecraft.gamepedia.com/Java_Edition_data_value#Items)
- 添加新的BlockRaycastComponent，可以覆盖用于轮廓和射线投射的AABB
- 添加新的BlockCollisionComponent，可以覆盖用于实体碰撞的AABB
- 添加新的BlockPropertyComponent，可以替换blockProperties：Unwalkable、Infiniburn、PreventsJumping、Immovable、BreakOnPush、OnlyPistonPush和BreaksWhenHitByArrow
- 添加新的BlockQueuedTickingComponent，在设定的时间范围内触发方块事件
- 添加新的BlockRandomTickingComponent，随机触发方块事件
- 添加一个旋转组件，允许方块旋转。该组件仅允许轴对齐的旋转
- 添加CraftingTableComponent的基础实现
  - 允许创建自定义合成台
  - 目前仅支持3x3网格

**附加包和脚本引擎**

添加'minecraft:placement_filter'组件，允许您设置此方块可以放置的条件。该组件还将在相邻方块变化时激活，并在不再处于有效位置时弹出其掉落物

- 添加对方块描述符的序列化
- 向方块描述符添加静态anyMatch函数，以比较一组方块描述符：Block*、BlockLegacy或BlockDescriptor

<!-- -->

- 添加一个函数以比较两个方块描述符。这涵盖：匹配方块、任一描述符的任何标签匹配、具有匹配排列的方块状态
- 将方块描述符的BlockLegacy成员变量更改为Block*，以便在延迟方块解析期间设置方块状态并获取设置状态的方块
- 移除所有现有的Block* JSON解析
- 添加单元测试以验证方块描述符的解析和序列化
- 添加单元测试以验证相互比较方块描述符

<!-- -->

- 添加单元测试以验证从设置状态的方块描述符获取方块

**数据驱动方块事件**

- 添加对以下事件响应的解析和执行支持：
  - 添加set_block_at_pos事件响应
  - 生成掉落物
  - 设置方块
- 添加对on_interact触发器组件的支持
  - 添加对on_player_placing触发器组件的支持
  - 还添加了用于获取放置上下文的MoLang查询cardinal_block_face_placed_on和cardinal_player_facing

**数据驱动方块模型**

- 添加新的数据驱动方块细分管道的第一阶段
- 添加“minecraft:geometry”组件，以允许使用方块模型进行渲染
- 添加“minecraft:unit_cube”组件，以允许使用默认单位立方体进行渲染。单位立方体获得一些额外效果，如环境光遮蔽和面移除
- 添加“minecraft:material_instances”组件，以允许在几何文件中将面和材质实例映射到实际材质

**数据驱动方块模型 - 平滑光照**

- 修复了新数据驱动方块的平滑光照和环境光遮蔽

**架构**

- 将allowed_blocks拆分为use_on和dispense_on
- use_on指定实体放置物品允许使用的方块，省略以允许所有方块
- dispense_on指定实体放置物品允许投放的方块，省略以允许所有方块

**执行命令**

- 为物品JSON事件添加对execute_command关键字的支持。它支持字符串和字符串数组格式，其中字符串是要运行的命令。命令在加载时编译，并在add/remove_mob_effect和传送操作之后执行，但在其他事件触发器之前执行。命令将按顺序分段并随机化节点。

**物品**

- 创建RepairableItemComponent，数据驱动物品在游戏中的修复方式。数据在物品JSON文件中的结构如下：

<!-- -->

    { 
    "format_version": "1.16.100", 
    "minecraft:item": { 
    ... 
        "minecraft:repairable": { 
          "repair_items": [ 
            { 
              "items": [ "minecraft:item" ], 
              "repair_amount": "query.max_damage * 0.25" 
            }, 
            { 
              "items": [ "minecraft:item", "minecraft:item2" ], 
              "repair_amount": "context.other->query.remaining_health + 0.05 * context.other->query.max_damage" 
            }, 
            { 
              "items": [ "minecraft:item3" ], 
              "on_repaired": { 
                "event": "repaired", 
                "target": "self" 
              } 
            } 
          ] 
        } 
      }, 
      "events": { 
        "repaired": { 
          "transform_item": { 
            "transform": "item_name" 
          } 
        } 
      } 
    } 
    } 

**运行命令**

- 为实体JSON事件添加对run_command关键字的支持，连同当前的add和remove关键字。它支持字符串和字符串数组格式，其中字符串是要运行的命令。命令将在组件组添加和移除后运行，并将按顺序分段并随机化节点。

更新以下组件以解析和使用方块描述符，而不是Block* 

- BlockBreakSensorComponent
- BlockListEventMap
- BreathableComponent
- BreedableComponent
- BuoyancyComponent
- EntityPlacerItemComponent
- PreferredPathComponent
- SeedItemComponentLegacy

更新以下特性以解析和使用方块描述符，而不是Block* 

- NoSurfaceOreFeature
- OreFeature
- SingleBlockFeature

更新以下目标定义以解析和使用方块描述符，而不是Block* 

- GoalDefinition
- RaidGardenGoal
- VanillaGoalDefinition

更新以下表面代码以解析和使用方块描述符，而不是Block* 

- MesaSurfaceAttributes
- SurfaceMaterialAdjustmentAttributes
- SurfaceMaterialAttributes

更新以下测试以反映更新代码以使用方块描述符的更改 

- BuoyancyComponentServerTests
- FeatureHelperTests
- NoSurfaceOreFeatureTests
- OreFeatureTests
- SingleBlockFeatureTests

更新以下树木以解析和使用方块描述符，而不是Block* 

- 金合欢树冠
- 金合欢树干
- 倒下的树干
- 华丽树冠
- 华丽树干
- 巨型松树冠
- 巨型树冠
- 巨型树干
- 云杉树冠
- 覆盖树冠
- 简单树冠
- 简单树干
- 云杉树冠
- 树木助手
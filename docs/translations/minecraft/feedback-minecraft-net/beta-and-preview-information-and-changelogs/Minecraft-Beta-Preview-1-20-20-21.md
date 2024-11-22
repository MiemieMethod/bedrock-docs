---
title: Minecraft Beta & 预览版 - 1.20.20.21
date: 2023-07-12T13:38:31Z
updated: 2023-09-29T09:35:56Z
categories: Beta和预览版信息与更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/17540689688589-Minecraft-Beta-Preview-1-20-20-21
hash:
  h_01HBG4P6PD67YER1A3KZCBYKRB: features-and-bug-fixes
  h_01HBG4P6PDB4ERR4QTGTXDZ7RV: recipe-book-search
  h_01HBG4P6PD63ADAEPJ5MXPQAK4: recipe-unlocking
  h_01HBG4P6PDE4M82KRN3XHYXJ9T: accessibility-features
  h_01HBG4P6PDGA6PG0TE4QTGW1E1: mobs
  h_01HBG4P6PDPKERN696YMMBJPAB: block-breaking
  h_01HBG4P6PDDFE0AJEMAT34TST3: gameplay
  h_01HBG4P6PDHCPNSEM8QA8TVBT8: graphical
  h_01HBG4P6PDMP5MS44R6WYNFDBR: player
  h_01HBG4P6PD30Z52EYKE47892JB: stability-and-performance
  h_01HBG4P6PDK7SNZ27XTZP2DGVN: storage
  h_01HBG4P6PDBSHCWSV9QNYWSQ2Y: user-interface
  h_01HBG4P6PDDC0X6EZX6SCRG7R9: vibrations
  h_01HBG4P6PDM5DNJYXANGCSJ7KX: technical-updates
  h_01HBG4P6PDX9J7G5N5Y6E9FKM2: add-ons
  h_01HBG4P6PD6R8GWYC7VC0NXR2T: commands
  h_01HBG4P6PDH37PQXARKP23XZ1N: editor
  h_01HBG4P6PDDBQ5GFXSN0AWR8E3: items
  h_01HBG4P6PD7VM84F5WH34ZKM8Z: molang
  h_01HBG4P6PDW3Z0QJ3FZ5CC0YT8: api
  h_01HBG4P6PDZ1BM32S1AZWVQSM7: items-1
  h_01H558MYHH7RM2ZVYE58YYZQB6: block-destroy-time-changes---full-list
  h_01HBG4P6PEW0T7N7EQMR4Z8Y10: ""
  h_01HBG4P6PE14GWXP9DP3VMTA2Y: remaining-parity-breaks
---

**发布于:** 2023年7月12日

**关于Minecraft Preview和Beta的信息:**

- 这些进行中的版本可能不稳定，并且可能无法代表最终版本的质量
- Minecraft Preview可在Xbox、Windows 10/11和iOS设备上使用。更多信息请参见 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上获取。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明。

![一张Minecraft的截图，显示一个村民在房间里用床睡觉，房间里有熔炉和箱子。物品展示框中放置着一个镐和一块深板岩采石区块。](https://feedback.minecraft.net/hc/article_attachments/17540657849869)

 

是时候发布新的Minecraft Preview和Beta了！以下是此次更新中的修复和新增功能列表。请继续向我们提供您的[反馈](https://aka.ms/MC120Feedback)和[漏洞报告](https://bugs.mojang.com/)，祝游戏愉快！

# **功能和漏洞修复**

## **配方书搜索**

- 在生存模式下，配方书搜索已更新，包含以下更改：
  - 搜索将只匹配物品名称中任何单词的开头。例如，搜索“tor”现在将显示 **Tor**ch 和 Redstone **Tor**ch，但不会显示 Daylight Detec**tor**
  - 搜索现在将更好地与配方解锁系统协同工作 - 尚未解锁的配方将在搜索结果中显示。
- 这个更改将使有经验的玩家能够找到他们正在寻找的物品（即使尚未解锁），而不会让新手玩家被他们尚未准备好的配方淹没。
- 这些更改计划同时应用于基岩版和Java版，但还在调整中，我们当然希望听到您的反馈！请在 [aka.ms/MinecraftRecipeSearch](https://aka.ms/MinecraftRecipeSearch) 提交您的想法

## **配方解锁**

- 配方解锁不再是实验性功能，但仍可以按世界开启和关闭
  - 已知问题：创建新世界屏幕中缺少配方解锁选项切换，但可以在创建世界后在编辑世界屏幕中找到并启用。我们希望尽快解决此问题！
- “配方已解锁”消息在暂停菜单中不再可见 ([MCPE-171112](https://bugs.mojang.com/browse/MCPE-171112))
- 染色玻璃板配方现在在获得任何染料时自动解锁 ([MCPE-171118](https://bugs.mojang.com/browse/MCPE-171118))
- 配方解锁通知现在适应不同语言的文本，不再超出屏幕 ([MCPE-171141](https://bugs.mojang.com/browse/MCPE-171141))

## **辅助功能**

- 修复了屏幕朗读在读取配方书文件夹内容时，将文件夹中的第一个项目读作配方书文件夹第一个项目的问题
- 屏幕朗读现在在用户更改滑块和切换开关后立即通知用户

## **生物**

- 骆驼在红沙、可疑沙子和混凝土粉末区块上行走时现在播放与在常规沙子上行走时相同的步伐声 ([MCPE-163497](https://bugs.mojang.com/browse/MCPE-163497))

## **区块破坏**

- 我们已调整188个区块的破坏时间以匹配Java版和我们预期的设计。一些区块因技术原因尚无法更改，黑曜石的破坏速度也未改变，因为我们仍在决定其破坏速度。将更多区块实现一致性使我们的团队更容易保持两个版本的更新。我们也希望这将使社区更容易制作和分享适用于所有平台上所有玩家的指南。
  - 区块破坏时间和更改的完整列表可在此更新日志末尾的 [这里](#block-destroy-time-changes---full-list) 找到

## **游戏玩法**

- 添加了playerssleepingpercentage游戏规则 ([MCPE-114425](https://bugs.mojang.com/browse/MCPE-114425))
  - 零或负值只需要一个玩家睡觉即可跳过夜晚
  - 设置超过100时，夜晚无法跳过
- 修复了在窄屏幕纵横比下，持有的地图未居中的问题
- 现在再次可以在沙子、泥土、沙砾和黏土下水中使用骨粉 ([MCPE-171383](https://bugs.mojang.com/browse/MCPE-171383))
- 修复了在击打潜行按钮时开始游泳可能导致潜行按钮持续被按住，直到游泳结束的问题 ([MCPE-130070](https://bugs.mojang.com/browse/MCPE-130070))
- 药水在向上看时不再被向后投掷 ([MCPE-138995](https://bugs.mojang.com/browse/MCPE-138995))
- Trail Ruins 内的营火不再默认点燃 ([MCPE-170033](https://bugs.mojang.com/browse/MCPE-170033))
- Dispensers 现在可以对粉红色花簇进行施肥 ([MCPE-171560](https://bugs.mojang.com/browse/MCPE-171560))
- 使用镐矿取出的潜影盒不再需要很长时间
- 下落的方块在落在可可豆上时现在会破碎并掉落其物品
- 投射物现在像生物一样沉入顶部雪层

## **图形**

- 修复了在床上睡觉时屏幕淡出的情况，现在不再完全不透明 ([MCPE-171461](https://bugs.mojang.com/browse/MCPE-171461))
- 命名牌的渲染逻辑现在基于摄像机位置而不是玩家位置

## **玩家**

- 修复了玩家首次加入游戏时会暂时消失的问题

## **稳定性和性能**

- 为iOS用户添加了磁盘空间不足的警报
- 修复了iOS上区块JSON加载时的崩溃问题
- 修复了在进入世界时游戏失去焦点可能导致崩溃的问题

## **存储**

- 解决了Xbox上大型世界中的“存储不足”错误和纹理损坏问题 ([MCPE-163050](https://bugs.mojang.com/browse/MCPE-163050))

## **用户界面**

- 荒魔台中的青金石图标现在与锻造桌屏幕中的图标匹配
- 荒魔台屏幕中的大型附魔标签现在不再被物品栏中覆盖的物品遮挡 ([MCPE-154428](https://bugs.mojang.com/browse/MCPE-154428))

## **振动**

- 幽匿感测体和幽匿尖啸体在接收振动时不再有在模拟距离限制内失去振动的风险
- 在潜行时停止使用物品时不再产生振动 ([MCPE-171524](https://bugs.mojang.com/browse/MCPE-171524))
- 监守者现在可以检测到落在地面的物品 ([MCPE-160889](https://bugs.mojang.com/browse/MCPE-160889))
- 幽匿感测体现在在检测到落地物品时向幽匿尖啸体发送信号 ([MCPE-161165](https://bugs.mojang.com/browse/MCPE-161165))

# **技术更新**

- 在文档中更新了Aux-Value到区块状态表，以考虑自创始以来的数据升级
- 在server.properties中添加了server-authoritative-sound布尔值
- 从@minecraft/server中移除了MinecraftEntityTypes，并用@minecraft/vanilla-data中的版本替换
- 将MoonPhase和World.getMoonPhase公开给脚本

## **附加包**

- 当在设置菜单中更改摄像机视角选项但摄像机命令处于活动状态时，显示警告消息
- 将PlacementDirection("*minecraft:placement_direction*")和PlacementPosition("*minecraft:placement_position*")区块特性移出实验性。这些特性可用于"*format_version*" \>= "1.20.20" 的区块

## **命令**

- 修复了在未选择文本框时，控制器右/左D-pad自动完成命令的问题，这也选择了屏幕上的不同UI元素
- "stained_glass"区块现在被分割为独立实例，即 "white_stained_glass", "orange_stained_glass", "magenta_stained_glass", "light_blue_stained_glass", "yellow_stained_glass", "lime_stained_glass", "pink_stained_glass", "gray_stained_glass", "light_gray_stained_glass", "cyan_stained_glass", "purple_stained_glass", "blue_stained_glass", "brown_stained_glass", "green_stained_glass", "red_stained_glass", 和 "black_stained_glass"
  - 命令仍将支持 "stained_glass"，但命令提示中将不再建议使用 "stained_glass"，而是使用新的名称
- "stained_glass_pane"区块现在被分割为独立实例，即 "white_stained_glass_pane", "orange_stained_glass_pane", "magenta_stained_glass_pane", "light_blue_stained_glass_pane", "yellow_stained_glass_pane", "lime_stained_glass_pane", "pink_stained_glass_pane", "gray_stained_glass_pane", "light_gray_stained_glass_pane", "cyan_stained_glass_pane", "purple_stained_glass_pane", "blue_stained_glass_pane", "brown_stained_glass_pane", "green_stained_glass_pane", "red_stained_glass_pane", 和 "black_stained_glass_pane"
  - 命令仍将支持 "stained_glass_pane"，但命令提示中将不再建议使用 "stained_glass_pane"，而是使用新的名称

## **编辑器**

编辑器及其对应的API尚处于早期开发阶段，并可在Windows PC基岩版Preview构建版上使用键盘/鼠标。请在社交媒体上使用 **#BedrockEditor** 标签与我们互动。

了解 [如何使用](https://aka.ms/LearnEditor) 编辑器，加入 [GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions) 论坛与团队交流，并通过 [入门套件](https://github.com/Mojang/minecraft-editor-extension-starter-kit) 和 [示例](https://github.com/Mojang/minecraft-editor-extension-samples) 开始构建扩展。

本周修复：

- 修复了在执行 /reload 命令后工具模式UI未刷新的问题
- 数字输入字段现在如果超出定义范围，会自动调整为最接近的有效数字值
- 修复了UI文本超出面板和容器边界，导致对齐不正确和视觉不一致的问题
- 选择体积和操作工具现在可以透过区块看到

## **物品**

- "*minecraft:entity_placer*" 现在在 "*use_on*" 和 "*dispense_on*" 列表中命名无效区块时会包含错误
- 在json格式1.20.20及更高版本中，已将 "*minecraft:use_animation*" 物品组件从实验性中移出
- 在json格式1.20.20及更高版本中，已将 "*minecraft:allow_off_hand*" 物品组件从实验性中移出
- 在json格式1.20.20及更高版本中，已将 "*minecraft:should_despawn*" 物品组件从实验性中移出
- 在json格式1.20.20及更高版本中，已将 "*minecraft:liquid_clipped*" 物品组件从实验性中移出
- 在json格式1.20.20及更高版本中，已将 "*minecraft:damage*" 物品组件从实验性中移出

## **Molang**

- 重命名了 *block_property* 和 has_block\_*property* 为 *block_state* 和 *has_block_state*
  - 这是一个Molang版本变更，仅对使用最小引擎版本为1.20.20或更高版本的包中的Molang表达式生效

**实验性功能**

- 添加了 *Scoreboard.addScore* 并改进了 *Scoreboard.setScore* 以返回更新后的分数

## **API**

将以下API从Beta移至稳定版：

 

- 将 *Direction* 移至 *1.4.0*
- 将 *EntityDamageSource* 移至 *1.4.0*
- 将 *EntityDieAfterEvent* 移至 *1.4.0*
- 将 *EntityEventOptions* 移至 *1.4.0*
- 将 *EntityHitBlockAfterEvent* 移至 *1.4.0*
- 将 *EntityHitEntityAfterEvent* 移至 *1.4.0*
- 将 *EntityHurtAfterEvent* 移至 *1.4.0*
- 将 *EntityHealthChangedAfterEvent* 移至 *1.4.0*
- 将 *Dimension.getBlockFromRay* 方法移至 *1.4.0*
- 将 *Dimension.getEntitiesFromRay* 方法移至 *1.4.0*
- 将 *Entity.getBlockFromViewDirection* 方法移至 *1.4.0*
- 将 *Entity.getEntitiesFromViewDirection* 方法移至 *1.4.0*
- 将 *BlockRaycastHit* 移至 *1.4.0*
- 将 *BlockRaycastOptions* 移至 *1.4.0*
- 将 *EntityRaycastHit* 移至 *1.4.0*
- 将 *EntityRaycastOptions* 移至 *1.4.0*
- 将 *PressurePlatePushEvent* 移至 *1.4.0*
- 将 *PressurePlatePopEvent* 移至 *1.4.0*
- 将 *TripWireTripEvent* 移至 *1.4.0*
- 将 *TargetBlockHitEvent* 移至 *1.4.0*
  - 即使实体无效，属性 *id* 也可访问
  - 即使实体无效，属性 *typeId* 也可访问
  - 将项目事件 *source* 属性从类型 *Entity* 更改为 *Player*

## **物品**

- 移除了 "*minecraft:animates_in_toolbar*" 组件
- 移除了 "*minecraft:explodable*" 组件
- 额外的伤害悬停文本现在出现在所有具有附加锋利附魔的组件物品上
- "*minecraft:shooter*" 组件现在支持 Quick Charge 附魔与 "*minecraft:enchantable*" 当 "*charge_on_draw*" 为真时
- 为使用 "*minecraft:digger*" 组件的数据驱动物品添加了效率附魔支持
- 从 "*minecraft:wearable*" 组件中移除了非功能性实体槽选项，例如鞍、实体盔甲和箱子
- 具有 "*minecraft:wearable*" 组件的自定义物品在从发射器中掉落时自动装备，与原版盔甲物品保持一致

 

## **方块摧毁时间变化 - 完整列表**

| **基岩ID** | **基岩名称** | **摧毁时间** | **爆炸抗性** |
|----|----|:--:|:--:|
| activator_rail | 激活铁轨 | 0.5 → 0.7 | 0.5 → 0.7 |
| ancient_debris | 远古残骸 |   | 720 → 1200 |
| andesite_stairs | 安山岩楼梯 | 2 → 1.5 |   |
| bamboo | 竹子 | 2 → 1 | 2 → 1 |
| bamboo_block | 竹块 |   | 3 → 2 |
| bamboo_sapling | 竹笋 | 0 → 1 | 0 → 1 |
| bee_nest | 蜂巢 |   | 2.7 → 0.3 |
| beehive | 蜂箱 |   | 5.4 → 0.6 |
| bell | 钟 | 1 → 5 | 3 → 5 |
| big_dripleaf | 大型垂滴叶 | 0 → 0.1 | 0 → 0.1 |
| campfire | 营火 | 5 → 2 | 5 → 2 |
| chain | 锁链 |   | 3 → 6 |
| chiseled_deepslate | 雕纹深板岩 |   | 3.6 → 6 |
| cobbled_deepslate | 深板岩圆石 |   | 3.6 → 6 |
| cobbled_deepslate_double_slab | 深板岩圆石台阶（双层） |   | 3.6 → 6 |
| cobbled_deepslate_slab | 深板岩圆石台阶 |   | 3.6 → 6 |
| cobbled_deepslate_stairs | 深板岩圆石楼梯 |   | 3.6 → 6 |
| cobbled_deepslate_wall | 深板岩圆石墙 |   | 3.6 → 6 |
| composter | 堆肥桶 | 2 → 0.6 | 2 → 0.6 |
| copper_block | 铜块 |   | 3.6 → 6 |
| copper_ore | 铜矿石 |   | 1.8 → 3 |
| coral_block | 珊瑚块（10块） | 7 → 1.5 | 0.9 → 6 |
| coral_fan | 珊瑚扇（5块） |   | 0.9 → 0 |
| coral_fan_dead | 失活的珊瑚扇（5块） |   | 0.9 → 0 |
| coral_fan_hang | 墙上的珊瑚扇（2块） |   | 0.9 → 0 |
| coral_fan_hang2 | 墙上的珊瑚扇（2块） |   | 0.9 → 0 |
| coral_fan_hang3 | 墙上的珊瑚扇（1块） |   | 0.9 → 0 |
| cracked_deepslate_bricks | 裂纹深板岩砖 |   | 3.6 → 6 |
| cracked_deepslate_tiles | 裂纹深板岩瓦 |   | 3.6 → 6 |
| crimson_hyphae | 绯红菌核 | 0.3 → 2 | 0.3 → 2 |
| crimson_stem | 绯红菌柄 |   | 0.3 → 2 |
| cut_copper | 切制铜块 |   | 3.6 → 6 |
| cut_copper_slab | 切制铜台阶 |   | 3.6 → 6 |
| cut_copper_stairs | 切制铜楼梯 |   | 3.6 → 6 |
| deepslate | 深板岩 |   | 3.6 → 6 |
| deepslate_brick_double_slab | 深板岩砖台阶（双层） |   | 3.6 → 6 |
| deepslate_brick_slab | 深板岩砖台阶 |   | 3.6 → 6 |
| deepslate_brick_stairs | 深板岩砖楼梯 |   | 3.6 → 6 |
| deepslate_brick_wall | 深板岩砖墙 |   | 3.6 → 6 |
| deepslate_bricks | 深板岩砖 |   | 3.6 → 6 |
| deepslate_coal_ore | 深层煤矿石 |   | 1.8 → 3 |
| deepslate_copper_ore | 深层铜矿石 |   | 1.8 → 3 |
| deepslate_diamond_ore | 深层钻石矿石 |   | 1.8 → 3 |
| deepslate_gold_ore | 深层金矿石 |   | 1.8 → 3 |
| deepslate_iron_ore | 深层铁矿石 |   | 1.8 → 3 |
| deepslate_lapis_ore | 深层青金石矿石 |   | 1.8 → 3 |
| deepslate_redstone_ore | 深层红石矿石 |   | 1.8 → 3 |
| deepslate_tile_double_slab | 深板岩瓦台阶（双层） |   | 3.6 → 6 |
| deepslate_tile_slab | 深板岩瓦台阶 |   | 3.6 → 6 |
| deepslate_tile_stairs | 深板岩瓦楼梯 |   | 3.6 → 6 |
| deepslate_tile_wall | 深板岩瓦墙 |   | 3.6 → 6 |
| deepslate_tiles | 深板岩瓦 |   | 3.6 → 6 |
| diorite_stairs | 闪长岩楼梯 | 2 → 1.5 |   |
| double_cut_copper_slab | 切制铜台阶（双层） |   | 3.6 → 6 |
| dragon_egg | 龙蛋 |   | 3 → 9 |
| dried_kelp_block | 干海带块 |   | 0.5 → 2.5 |
| end_brick_stairs | 末地石砖楼梯 | 2 → 3 | 6 → 9 |
| end_bricks | 末地石砖 | 0.8 → 3 | 0.8 → 9 |
| exposed_cut_copper_slab | 斑驳切制铜台阶 |   | 3.6 → 6 |
| exposed_copper | 斑驳铜块 |   | 3.6 → 6 |
| exposed_cut_copper | 斑驳切制铜块 |   | 3.6 → 6 |
| exposed_cut_copper_stairs | 斑驳切制铜楼梯 |   | 3.6 → 6 |
| exposed_double_cut_copper_slab | 斑驳切制铜台阶（双层） |   | 3.6 → 6 |
| granite_stairs | 花岗岩楼梯 | 2 → 1.5 |   |
| infested_deepslate | 虫蚀深板岩 |   | 1.8 → 0.75 |
| jukebox | 唱片机 | 0.8 → 2 | 0.8 → 6 |
| lantern | 灯笼 | 5 → 3.5 | 5 → 3.5 |
| lectern | 讲台 | 2 → 2.5 | 2 → 2.5 |
| light_block | 光源方块 |   | 3600000 → 3600000.8 |
| light_gray_candle | 淡灰色蜡烛 | 0 → 0.1 | 0 → 0.1 |
| lightning_rod | 避雷针 |   | 3.6 → 6 |
| lodestone | 磁石 | 2 → 3.5 | 2 → 3.5 |
| magma | 岩浆块 |   | 1.5 → 0.5 |
| monster_egg | 虫蚀块（5块，缺少虫蚀圆石） |   | 1.8 → 0.75 |
| mossy_stone_brick_stairs | 苔石砖楼梯 | 2 → 1.5 |   |
| mud_bricks | 泥砖 | 2 → 1.5 | 2 → 3 |
| mud_brick_slab | 泥砖台阶 | 2 → 1.5 | 6 → 3 |
| mud_brick_double_slab | 泥砖台阶（双层） | 2 → 1.5 | 6 → 3 |
| mud_brick_stairs | 泥砖楼梯 | 2 → 1.5 | 6 → 3 |
| mud_brick_wall | 泥砖墙 | 2 → 1.5 | 6 → 3 |
| netherite_block | 下界合金块 |   | 720 → 1200 |
| oxidized_cut_copper | 氧化切制铜块 |   | 3.6 → 6 |
| oxidized_cut_copper_slab | 氧化切制铜台阶 |   | 3.6 → 6 |
| oxidized_cut_copper_stairs | 氧化切制铜楼梯 |   | 3.6 → 6 |
| oxidized_copper | 氧化铜块 |   | 3.6 → 6 |
| oxidized_double_cut_copper_slab | 氧化切制铜台阶（双层） |   | 3.6 → 6 |
| piston | 活塞 | 0.5 → 1.5 | 0.5 → 1.5 |
| piston_arm_collision | 活塞头 | 0.5 → 1.5 | 0.5 → 1.5 |
| pointed_dripstone | 小型滴水石锥 |   | 1.8 → 3 |
| polished_andesite_stairs | 磨制安山岩楼梯 | 2 → 1.5 |   |
| polished_blackstone | 磨制黑石 | 1.5 → 2 |   |
| polished_blackstone_stairs | 磨制黑石楼梯 | 1.5 → 2 |   |
| polished_blackstone_wall | 磨制黑石墙 | 1.5 → 2 |   |
| polished_deepslate | 磨制深板岩 |   | 3.6 → 6 |
| polished_deepslate_double_slab | 磨制深板岩台阶（双层） |   | 3.6 → 6 |
| polished_deepslate_slab | 磨制深板岩台阶 |   | 3.6 → 6 |
| polished_deepslate_stairs | 磨制深板岩楼梯 |   | 3.6 → 6 |
| polished_deepslate_wall | 磨制深板岩墙 |   | 3.6 → 6 |
| polished_diorite_stairs | 磨制闪长岩楼梯 | 2 → 1.5 |   |
| polished_granite_stairs | 磨制花岗岩楼梯 | 2 → 1.5 |   |
| reinforced_deepslate | 强化深板岩 |   | 720 → 1200 |
| respawn_anchor | 重生锚 |   | 720 → 1200 |
| scaffolding | 脚手架 | 0.6 → 0 | 0.9 → 0 |
| sculk | 幽匿块 | 0.6 → 0.2 | 0.6 → 0.2 |
| sculk_catalyst | 幽匿催发体 |   | 1.8 → 3 |
| sculk_shrieker | 幽匿尖啸体 |   | 1.8 → 3 |
| shulker_box | 潜影盒（16块） | 2.5 → 2 | 2.5 → 2 |
| smooth_quartz_stairs | 平滑石英楼梯 | 0.8 → 2 | 0.8 → 6 |
| smooth_stone | 平滑石头 | 1.5 → 2 |   |
| sniffer_egg | 嗅探兽蛋 | 0.4 → 0.5 | 0.4 → 0.5 |
| soul_campfire | 灵魂营火 | 5 → 2 | 5 → 2 |
| soul_lantern | 灵魂灯笼 | 5 → 3.5 | 5 → 3.5 |
| soul_soil | 灵魂土 | 1 → 0.5 | 1 → 0.5 |
| sticky_piston | 黏性活塞 | 0.5 → 1.5 | 0.5 → 1.5 |
| sticky_piston_arm_collision | 活塞头（黏性） | 0.5 → 1.5 | 0.5 → 1.5 |
| stripped_bamboo_block | 去皮竹块 |   | 3 → 2 |
| stripped_crimson_hyphae | 去皮绯红菌核 | 0.3 → 2 | 0.3 → 2 |
| stripped_crimson_stem | 去皮绯红菌柄 |   | 0.3 → 2 |
| stripped_warped_hyphae | 去皮诡异菌核 | 0.3 → 2 | 0.3 → 2 |
| stripped_warped_stem | 去皮诡异菌柄 |   | 0.3 → 2 |
| sweet_berry_bush | 甜浆果丛 | 0.2 → 0 | 0.2 → 0 |
| turtle_egg | 海龟蛋 | 0.4 → 0.5 | 0.4 → 0.5 |
| undyed_shulker_box | 潜影盒 | 2.5 → 2 | 2.5 → 2 |
| warped_hyphae | 诡异菌核 | 0.3 → 2 | 0.3 → 2 |
| warped_stem | 诡异菌柄 |   | 0.3 → 2 |
| waxed_cut_copper | 涂蜡的切制铜块 |   | 3.6 → 6 |
| waxed_cut_copper_slab | 涂蜡的切制铜台阶 |   | 3.6 → 6 |
| waxed_cut_copper_stairs | 涂蜡的切制铜楼梯 |   | 3.6 → 6 |
| waxed_copper | 涂蜡的铜块 |   | 3.6 → 6 |
| waxed_double_cut_copper_slab | 涂蜡的切制铜台阶（双层） |   | 3.6 → 6 |
| waxed_exposed_copper | 涂蜡的斑驳铜块 |   | 3.6 → 6 |
| waxed_exposed_cut_copper | 涂蜡的斑驳切制铜块 |   | 3.6 → 6 |
| waxed_exposed_cut_copper_slab | 涂蜡的斑驳切制铜台阶 |   | 3.6 → 6 |
| waxed_exposed_cut_copper_stairs | 涂蜡的斑驳切制铜楼梯 |   | 3.6 → 6 |
| waxed_exposed_double_cut_copper_slab | 涂蜡的斑驳切制铜台阶（双层） |   | 3.6 → 6 |
| waxed_oxidized_copper | 涂蜡的氧化铜块 |   | 3.6 → 6 |
| waxed_oxidized_cut_copper | 涂蜡的氧化切制铜块 |   | 3.6 → 6 |
| waxed_oxidized_cut_copper_stairs | 涂蜡的氧化切制铜楼梯 |   | 3.6 → 6 |
| waxed_oxidized_cut_copper_slab | 涂蜡的氧化切制铜台阶 |   | 3.6 → 6 |
| waxed_oxidized_double_cut_copper_slab | 涂蜡的氧化切制铜台阶（双层） |   | 3.6 → 6 |
| waxed_weathered_cut_copper | 涂蜡的锈蚀切制铜块 |   | 3.6 → 6 |
| waxed_weathered_cut_copper_slab | 涂蜡的锈蚀切制铜台阶 |   | 3.6 → 6 |
| waxed_weathered_cut_copper_stairs | 涂蜡的锈蚀切制铜楼梯 |   | 3.6 → 6 |
| waxed_weathered_copper | 涂蜡的锈蚀铜块 |   | 3.6 → 6 |
| waxed_weathered_double_cut_copper_slab | 涂蜡的锈蚀切制铜台阶（双层） |   | 3.6 → 6 |
| weathered_copper | 锈蚀的铜块 |   | 3.6 → 6 |
| weathered_cut_copper | 锈蚀的切制铜块 |   | 3.6 → 6 |
| weathered_cut_copper_slab | 锈蚀的切制铜台阶 |   | 3.6 → 6 |
| weathered_cut_copper_stairs | 锈蚀的切制铜楼梯 |   | 3.6 → 6 |
| weathered_double_cut_copper_slab | 锈蚀的切制铜台阶（双层） |   | 3.6 → 6 |

## **剩余的趋同差异**

**DT - 摧毁时间**  
**ER - 爆炸抗性**

| **基岩ID** | **基岩名称** | **基岩DT** | **Java DT** | **基岩ER** | **Java ER** |
|----|----|:--:|:--:|:--:|:--:|
| cobblestone_wall | 花岗岩墙 | 2 | 1.5 |   |   |
| cobblestone_wall | 砂岩墙 | 2 | 0.8 | 6 | 0.8 |
| cobblestone_wall | 海晶石墙 | 2 | 1.5 |   |   |
| cobblestone_wall | 闪长岩墙 | 2 | 1.5 |   |   |
| cobblestone_wall | 安山岩墙 | 2 | 1.5 |   |   |
| cobblestone_wall | 末地石砖墙 | 2 | 3 | 6 | 9 |
| cobblestone_wall | 石砖墙 | 2 | 1.5 |   |   |
| cobblestone_wall | 苔石砖墙 | 2 | 1.5 |   |   |
| cobblestone_wall | 红砂岩墙 | 2 | 0.8 | 6 | 0.8 |
| stone_block_slab2 | 海晶石砖台阶 | 2 | 1.5 |   |   |
| stone_block_slab2 | 暗海晶石台阶 | 2 | 1.5 |   |   |
| stone_block_slab2 | 海晶石台阶 | 2 | 1.5 |   |   |
| double_stone_block_slab2 | 海晶石砖台阶（双层） | 2 | 1.5 |   |   |
| double_stone_block_slab2 | 暗海晶石台阶（双层） | 2 | 1.5 |   |   |
| double_stone_block_slab2 | 海晶石台阶（双层） | 2 | 1.5 |   |   |
| stone_block_slab3 | 安山岩台阶 | 2 | 1.5 |   |   |
| stone_block_slab3 | 末地石砖台阶 | 2 | 3 | 6 | 9 |
| stone_block_slab3 | 磨制安山岩台阶 | 2 | 1.5 |   |   |
| stone_block_slab3 | 磨制闪长岩台阶 | 2 | 1.5 |   |   |
| stone_block_slab3 | 花岗岩台阶 | 2 | 1.5 |   |   |
| stone_block_slab3 | 闪长岩台阶 | 2 | 1.5 |   |   |
| stone_block_slab3 | 磨制花岗岩台阶 | 2 | 1.5 |   |   |
| double_stone_block_slab3 | 安山岩台阶（双层） | 2 | 1.5 |   |   |
| double_stone_block_slab3 | 末地石砖台阶（双层） | 2 | 3 | 6 | 9 |
| double_stone_block_slab3 | 磨制安山岩台阶（双层） | 2 | 1.5 |   |   |
| double_stone_block_slab3 | 磨制闪长岩台阶（双层） | 2 | 1.5 |   |   |
| double_stone_block_slab3 | 花岗岩台阶（双层） | 2 | 1.5 |   |   |
| double_stone_block_slab3 | 闪长岩台阶（双层） | 2 | 1.5 |   |   |
| double_stone_block_slab3 | 磨制花岗岩台阶（双层） | 2 | 1.5 |   |   |
| stone_block_slab4 | 苔石砖台阶（双层） | 2 | 1.5 |   |   |
| double_stone_block_slab4 | 苔石砖台阶（双层） | 2 | 1.5 |   |   |
| crying_obsidian | 哭泣的黑曜石 | 35 | 50 |   |   |
| monster_egg | 虫蚀圆石 | 0.75 | 1 |   |   |
| obsidian | 黑曜石 | 35 | 50 |   |   |
| quartz_block | 平滑石英块 | 0.8 | 2 | 0.8 | 6 |
| red_sandstone | 平滑红砂岩 | 0.8 | 2 | 0.8 | 6 |
| sandstone | 平滑砂岩 | 0.8 | 2 | 0.8 | 6 |
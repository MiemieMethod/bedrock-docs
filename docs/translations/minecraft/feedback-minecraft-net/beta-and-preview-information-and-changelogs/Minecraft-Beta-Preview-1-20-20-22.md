---
标题: Minecraft Beta & Preview - 1.20.20.22
日期: 2023-07-20T14:49:47Z
更新: 2023-08-04T10:31:08Z
分类: Beta 和预览信息与更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/17785920851725-Minecraft-Beta-Preview-1-20-20-22
---

**发布于:** 2023年7月20日

**关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明。

![一张Minecraft截图，展示了一些兔子和一只北极熊站在雪层上，附近有树木和瀑布。](https://feedback.minecraft.net/hc/article_attachments/17785909268493)

以下是本周Minecraft预览版和测试版的新内容！请继续向我们发送您的 [反馈](https://aka.ms/MC120Feedback) 和 [漏洞报告](https://bugs.mojang.com/)，享受更新！

 

# **新特性和漏洞修复**

## **活动对象**

- 兔子、北极熊和物品不再漂浮在顶部雪块上 ([MCPE-172381](https://bugs.mojang.com/browse/MCPE-172381), [MCPE-173081](https://bugs.mojang.com/browse/MCPE-173081)) 

## **方块**

- 世界中放置的结构空位方块可以再次在持有结构空位方块时被高亮和摧毁 ([MCPE-172429](https://bugs.mojang.com/browse/MCPE-172429)) 

## **游戏玩法**

- 游泳时，呼吸计量器现在在头部高出水面时会重新填充 ([MCPE-170969](https://bugs.mojang.com/browse/MCPE-170969)) 
- 爬行的实验性开关已被移除，爬行通过1个方块的缝隙现在已完全实现

## **配方解锁**

- 现在可以在创建新世界屏幕上启用配方解锁 ([MCPE-172956](https://bugs.mojang.com/browse/MCPE-172956))
- 解锁配方的命令已更新。给玩家一个配方的自动建议现在显示为“player: target”而不是“victim: target” ([MCPE-172402](https://bugs.mojang.com/browse/MCPE-172402)) 

## **稳定性和性能**

- 修复了Xbox上缺失的低磁盘空间警告 

### **辅助功能**

- 文本转语音复述功能现在将在没有互联网连接时打开游戏菜单时读取断开连接消息 

## **用户界面**

- 仅限iOS：修复了多行文本编辑中的一个漏洞，有时在使用空格键重新定位光标后输入的某些文本会被删除 ([MCPE-166152](https://bugs.mojang.com/browse/MCPE-166152)) 
- 在选项 > 订阅中将按钮文本从“管理”更改为“取消” 
- 修复了导致地下渐变效果在快捷栏上方绘制的分层问题 ([MCPE-159217](https://bugs.mojang.com/browse/MCPE-159217))
- 在新的死亡屏幕上添加一个按钮，允许玩家进入游戏菜单以更改设置、离开世界等

# **技术更新**

## **通用**

- 从server.properties中移除了服务器权威声音布尔值 
- 将*DimensionType*暴露给脚本 
- /camera命令不再需要实验性摄像机开关 
  - 注意：摄像机实验仍包含多个示例预设JSON文件供引用
- 将“*minecraft:wearable*”物品组件从实验性中发布到json格式1.20.20及更高版本
- 从数据驱动生物群系实验性开关后暴露以下特性放置规则。这允许创作者将自定义地物附加到生物群系，并定义这些地物放置的规则
  - minecraft:aggregate_feature
  - minecraft:cave_carver_feature
  - minecraft:fossil_feature
  - minecraft:geode_feature
  - minecraft:growing_plant_feature
  - minecraft:multiface_feature
  - minecraft:nether_cave_carver_feature
  - minecraft:ore_feature
  - minecraft:partially_exposed_blob_feature
  - minecraft:scatter_feature
  - minecraft:search_feature
  - minecraft:sequence_feature
  - minecraft:single_block_feature
  - minecraft:snap_to_surface_feature
  - minecraft:structure_template_feature
  - minecraft:surface_relative_threshold_feature
  - minecraft:tree_feature
  - minecraft:underwater_cave_carver_feature
  - minecraft:vegetation_patch_feature
  - minecraft:weighted_random_feature

## **物品**

- 将“*minecraft:digger*”物品组件从实验性中发布到json格式1.20.20及更高版本 
- 在格式1.20.20及更高版本中弃用“*on_dig*”参数

# **实验性技术特性**

## **API**

- 为以下API添加摄像机脚本API： 
  - *setCamera()*：设置摄像机为指定预设
  - *fade()*：开始摄像机渐变
  - *clear()*：清除摄像机上的当前设置
- 将记分板API从测试版发布到V1.4.0
  - 更新*Scoreboard.getObjective*、*getObjectiveAtDisplaySlot*和*clearObjectiveAtDisplaySlot*以返回'\| undefined'
- 移除了在 *@minecraft/server* 中定义的*MinecraftBlockTypes* 
- 将*ItemUseBeforeEvent* 移动到 *1.4.0* 
- 将*ItemUseOnBeforeEvent* 移动到 *1.4.0* 
- 将*ItemUseAfterEvent* 移动到 *1.4.0* 
- 将*ItemUseOnAfterEvent* 移动到 *1.4.0* 
- 将*ItemStartUseOnAfterEvent* 移动到 *1.4.0* 
- 将*ItemStopUseAfterEvent* 移动到 *1.4.0* 
- 将*ItemStopUseOnAfterEvent* 移动到 *1.4.0* 
- 将*ItemCompleteUseAfterEvent* 移动到 *1.4.0* 
- 将*ItemReleaseUseAfterEvent* 移动到 *1.4.0* 
- 将*ItemStartUseAfterEvent* 移动到 *1.4.0* 
- 将*DimensionLocation* 移动到 *1.4.0* 
- 将*PositionInUnloadedChunkError*重命名为*LocationInUnloadedChunkError*并移动到*1.4.0* 
- 将*PositionOutOfWorldBoundariesError*重命名为*LocationOutOfWorldBoundariesError*并移动到*1.4.0* 
  - 将*getSpawnPoint*移动到*1.4.0* 
  - 将*setSpawnPoint*移动到*1.4.0* 
  - 将*getDefaultSpawnLocation*移动到*1.4.0* 
  - 将*setDefaultSpawnLocation*移动到*1.4.0* 
- 将*isValid()*从测试版发布到*1.4.0*，适用于以下类：
  - *Block*
  - *Container*
  - *Entity*
  - *Player*
  - *SimulatedPlayer*
- WorldAfterEvents
  - 移除了*projectileHit*
  - 添加了*projectileHitBlock*
  - 添加了*projectileHitEntity*
- 添加类*ProjectileHitBlockAfterEvent* 导出类:  
  ProjectileHitBlockAfterEvent { readonly dimension: Dimension; readonly hitVector: Vector3; readonly location: Vector3; readonly projectile: Entity; readonly source?: Entity; getBlockHit(): BlockHitInformation; }
- 添加类*ProjectileHitEntityAfterEvent* 导出类:  
  ProjectileHitEntityAfterEvent { readonly dimension: Dimension; readonly hitVector: Vector3; readonly location: Vector3; readonly projectile: Entity; readonly source?: Entity; getEntityHit(): EntityHitInformation; }
- 修复了*ContainerSlot*在某些容器类型中无法正常工作的漏洞 ([MCPE-172782](https://bugs.mojang.com/browse/MCPE-172782))
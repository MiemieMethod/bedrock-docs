# 开启实验性玩法

在Minecraft基岩版中，实验性玩法通常可以在创建世界或编辑世界设置时直接开启。对于Minecraft教育版、基岩版专用服务器，或者已经创建完成且无法通过界面重新设置的世界，往往需要直接编辑`level.dat`。

## 先备份世界

/// warning | 先备份
编辑`level.dat`属于直接修改存档数据。若文件损坏，世界可能无法打开，或者已放置的实验性内容会出现异常。
///

建议先导出世界，或者复制整个世界目录留作备份。

## 通过界面开启

如果世界仍可以正常进入设置界面，优先在创建世界或世界设置中开启实验性玩法，而不要手动改文件。这样最安全，也最不容易留下多余标签。

## 通过NBT编辑器开启

1. 找到目标世界的目录。
2. 打开`level.dat`。
3. 在根标签下创建或编辑`experiments`复合标签。
4. 在`experiments`下为需要的功能创建值为`1`的字节标签。
5. 保存文件并重新打开世界。

不同版本支持的实验性标签名称会变化，下面列出的是近版本中常见的名称：

| 游戏内名称 | NBT名称 |
| --- | --- |
| Render Dragon Features for Creators | `deferred_technical_preview` |
| Villager Trade Rebalancing | `villager_trades_rebalance` |
| Upcoming Creator Features | `upcoming_creator_features` |
| Beta APIs | `gametest` |
| Experimental Creator Camera Features | `experimental_creator_cameras` |
| Data-Driven Jigsaw Structures | `jigsaw_structures` |
| Custom biomes | `data_driven_biomes` |
| Drop 3 2025 | `y_2025_drop_3` |

如果只想启用某一项功能，只需创建对应的字节标签即可。不同版本对同一功能的名称可能略有差异，编辑前应先核对目标版本的内容日志或官方说明。

## 额外标签

有些世界在启用实验性玩法后，还会自动出现以下标签：

- `experiments_ever_used`
- `saved_with_toggled_experiments`

这些标签通常不需要手动创建，但在排查世界状态时可能会看到它们。

## 关闭实验性玩法

理论上可以删除`experiments`复合标签中的对应字节标签来关闭实验性玩法。但这不是官方支持的流程，尤其是在世界已经使用过实验性方块、物品或机制后，关闭它们可能导致世界内容显示为未知方块或产生其他异常。

## 适用范围

教育版、基岩版专用服务器和某些旧世界最常需要这个流程。普通单人世界若还能进入设置界面，仍应优先使用界面完成设置。
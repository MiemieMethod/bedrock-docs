# 存档与内容文件

Minecraft基岩版的存档、附加包和世界模板会在不同平台上使用不同的存储方式。创作者在备份测试世界、迁移开发用世界、检查世界附带的包，或排查导入失败问题时，通常需要先确认文件实际位于何处。

## 存档目录

在Windows版中，基岩版存档通常位于以下目录：

```text
%LOCALAPPDATA%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds\
```

在Android版中，只有将游戏设置中的文件存储位置设为“外部”时，世界目录才会作为普通文件夹暴露给文件管理器。其路径通常为：

```text
Android\data\com.mojang.minecraftpe\files\games\com.mojang\minecraftWorlds
```

如果Android版的文件存储位置为“应用程序”，世界会保存在应用数据中，通常不能直接作为文件夹导出。需要备份或迁移时，应优先使用游戏内导出功能，或先在创建世界前将文件存储位置改为“外部”。

每个世界在`minecraftWorlds`目录中是一个单独文件夹。文件夹名称可能是随机字符串或GUID，不一定与世界名称相同。要确认某个文件夹对应的世界，可以打开其中的{{file|levelname.txt}}查看显示名称。

## 导出文件

基岩版可以通过游戏界面的“导出世界”功能生成`.mcworld`文件。`.mcworld`文件本质上是世界目录的压缩包，适合用于备份、发送给其他设备，或作为开发用测试世界的分发格式。

在Windows版中，导出世界的一般入口如下：

1.  在主界面选择“游戏”。
2.  在世界列表中选择目标世界旁的铅笔图标。
3.  在世界设置的文件管理区域选择“导出世界”。
4.  选择保存位置并确认导出。

将完整世界文件夹手动转换为`.mcworld`时，应压缩世界文件夹中的所有内容，而不是压缩外层的父目录。压缩后可将扩展名从`.zip`改为`.mcworld`。

## Minecraft教育版路径<!-- md:flag edu -->

Minecraft教育版的世界同样存储在`minecraftWorlds`目录中，但各平台路径不同。常见路径如下：

| 平台 | 路径 |
|------|------|
| Chromebook | `Play files\games\com.mojang\minecraftWorlds` |
| iPad | `Minecraft Education Edition\games\com.mojang\minecraftWorlds` |
| macOS | `HD\Users\<用户名>\Library\Application Support\Minecraftpe\Games\com.mojang` |
| Windows桌面版 | `C:\Users\<用户名>\AppData\Roaming\Minecraft Education Edition\games\com.mojang\minecraftWorlds` |
| Windows商店版 | `C:\Users\<用户名>\AppData\Local\Packages\Microsoft.MinecraftEducationEdition_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds` |

某些平台需要先显示隐藏文件，才能看到完整路径。Chromebook还可能需要为Minecraft教育版授予存储权限。

## 与存档结构的关系

文件位置只说明存档在操作系统中的存放地点。关于存档内部的{{file|level.dat}}、{{file|db}}目录、世界资源包和世界行为包等结构，请参阅[存档](../../docs/save/save.md)文档。

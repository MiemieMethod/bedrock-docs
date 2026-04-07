# 存档

**存档（Level）**是Minecraft基岩版中保存一个完整游戏世界全部数据的集合，也常被称为“世界”。存档包含了地形、实体、玩家数据、游戏设置等所有持久化信息。

## 概述

每个存档对应Minecraft中的一个独立世界。当玩家创建新世界或从世界模板导入时，系统会创建一个新的存档。存档数据以文件系统中的目录结构组织，存储在设备的本地存储中。

在不同平台上，存档的默认存放路径不同：

- **Windows**：`%LOCALAPPDATA%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds\`
- **Android**：`/storage/emulated/0/Android/data/com.mojang.minecraftpe/files/games/com.mojang/minecraftWorlds/`

每个存档占据一个以随机字符串命名的子目录。

## 文件结构

存档的目录结构如下：

/// html | div.treeview
- {{file|level.dat}}：存档的核心元数据文件，使用NBT格式存储。
- {{file|level.dat_old}}：`level.dat`的备份副本。
- {{file|levelname.txt}}：存档名称的纯文本文件。
- {{file|world_icon.jpeg}}：存档图标。
- `db/`：LevelDB数据库目录，存放区块和实体等核心世界数据。
- `behavior_packs/`：存档关联的行为包。
- `resource_packs/`：存档关联的资源包。
- {{file|world_behavior_packs.json}}：行为包配置列表。
- {{file|world_resource_packs.json}}：资源包配置列表。
///

## level.dat

`level.dat`是存档的核心元数据文件，采用小端序NBT格式，文件开头有8字节的文件头（4字节的版本号和4字节的NBT数据长度）。该文件记录了：

- **存档名称（LevelName）**：世界的显示名称。
- **游戏模式（GameType）**：默认游戏模式。
- **难度（Difficulty）**：世界难度。
- **种子（RandomSeed）**：世界生成种子。
- **出生点坐标（SpawnX/SpawnY/SpawnZ）**：默认重生位置。
- **游戏规则**：各项游戏规则的当前设置。
- **实验性开关**：各项实验性玩法的启用状态。
- **引擎版本与存储版本**：标记存档的版本兼容信息。

## LevelDB数据库

基岩版使用Google的**LevelDB**作为世界数据的底层存储引擎，与Java版使用的Anvil区域文件格式不同。LevelDB是一个有序键值存储系统，存档中的区块数据、实体数据和方块实体数据都以键值对的形式存储在`db/`目录中。

### 键格式

LevelDB中的键按照不同的数据类型采用不同的编码格式：

- **子区块数据**：键包含区块的X和Z坐标（4字节整数，小端序）、维度ID（主世界省略此字段）、数据类型标记和子区块Y索引。
- **实体和方块实体数据**：键包含区块坐标和对应的数据类型标记。
- **生物群系数据**：键包含区块坐标和生物群系数据类型标记。

### 子区块格式

每个**子区块（Subchunk）**存储一个16×16×16方块范围内的方块数据。子区块使用**调色板（Palette）**压缩存储方块信息：先定义一组方块状态作为调色板条目，然后使用位数组中的索引值引用调色板条目来表示每个位置的方块。

## 玩家数据

玩家数据存储在LevelDB中或以独立文件形式存在。单人游戏中，玩家数据直接记录在`level.dat`的根标签中；多人游戏服务器中，每位玩家的数据以其XUID或唯一标识符为键单独存储在LevelDB中。

## 导入与导出

存档可以通过以下方式进行导入和导出：

- **`.mcworld`文件**：将存档目录压缩为`.mcworld`格式的文件，可以在设备之间传输。双击`.mcworld`文件可以自动导入到Minecraft中。
- **文件复制**：直接复制存档目录到指定路径实现导入。
- **Minecraft Realms**：通过Realms服务上传或下载存档。

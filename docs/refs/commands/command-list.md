# 国际版命令清单

本页基于Microsoft Learn的CommandsReference目录整理国际版命令参考，覆盖2025-02-11版本文档中的82条命令。内容仅描述国际版默认命令集合，不将中国版模组SDK专有指令与旧版废弃语法作为默认结论。

/// note | 范围说明
- 教育版专有命令（如`/ability`、`/immutableworld`、`/wb`）未纳入本清单。<!-- md:flag edu -->
- `gametest`等命令仍依赖实验性能力，版本迁移时应结合[命令版本](version.md)和目标版本更新日志复核。
- 命令名称、语法参数名和权限枚举保持官方英文原样，以降低跨版本比对歧义。
///

## 权限级别对照

| 官方枚举 | 中文说明 |
|---|---|
| `Game Directors` | 游戏指导者 |
| `Admin` | 管理员 |
| `Owner` | 所有者 |
| `Host` | 房主 |
| `Any` | 任意玩家 |

## 命令分类

### 世界编辑

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/clearspawnpoint` | `Game Directors`（游戏指导者） | 是 | `/clearspawnpoint [player: target]` | — | Removes the spawn point for a player. |
| `/clone` | `Game Directors`（游戏指导者） | 是 | `/clone <begin: x y z> <end: x y z> <destination: x y z> [maskMode: maskmode] [cloneMode: clonemode]` | — | Clones a set of blocks from one region to another. |
| `/fill` | `Game Directors`（游戏指导者） | 是 | `/fill <from: x y z> <to: x y z> <tileName: Block> <blockStates: block_state_array> [oldBlockHandling: fillmode]` | — | Fills all or parts of a region with a specific block. |
| `/place` | `Admin`（管理员） | 是 | `/place structure <structure: jigsawstructure> [pos: x y z] [ignoreStartHeight: Boolean] [keepJigsaws: Boolean] [includeEntities: Boolean] [liquidSettings: liquidsettings]` | — | Places a jigsaw structure, feature, or feature rule in the world. |
| `/setblock` | `Game Directors`（游戏指导者） | 是 | `/setblock <position: x y z> <tileName: Block> <blockStates: block_state_array> [oldBlockHandling: setblockmode]` | — | Changes a block to another block. |
| `/setworldspawn` | `Game Directors`（游戏指导者） | 是 | `/setworldspawn [spawnPoint: x y z]` | — | Sets the location where new players or players who die will spawn in the world. |
| `/spawnpoint` | `Game Directors`（游戏指导者） | 是 | `/spawnpoint [player: target] [spawnPos: x y z]` | — | Sets the spawn point for a player. |
| `/spreadplayers` | `Game Directors`（游戏指导者） | 是 | `/spreadplayers <x: rotation> <z: rotation> <spreadDistance: float> <maxRange: float> <victim: target> [maxHeight: rotation]` | — | Teleports entities to random locations. |
| `/structure` | `Game Directors`（游戏指导者） | 是 | `/structure save <name: id> <from: x y z> <to: x y z> [includeEntities: Boolean] [includeBlocks: Boolean]` | — | Saves or loads a structure in the world. |

### 实体管理

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/damage` | `Game Directors`（游戏指导者） | 是 | `/damage <target: target> <amount: int> [cause: damagecause]` | — | Apply damage to the specified entities. |
| `/effect` | `Game Directors`（游戏指导者） | 是 | `/effect <player: target> <Mode: cleareffects> [effect: effect]` | — | Add or clear status effects. |
| `/enchant` | `Game Directors`（游戏指导者） | 是 | `/enchant <player: target> <enchantmentName: enchant> [level: int]` | — | Adds an enchantment to a player's selected item. |
| `/event` | `Game Directors`（游戏指导者） | 是 | `/event entity <target: target> <eventName: entityevents>` | — | Triggers an event for the specified entity or entities. |
| `/kill` | `Game Directors`（游戏指导者） | 是 | `/kill [target: target]` | — | Kills entities like players and mobs. |
| `/playanimation` | `Game Directors`（游戏指导者） | 是 | `/playanimation <entity: target> <animation: id> [next_state: id] [blend_out_time: float] [stop_expression: id] [controller: id]` | — | Makes one or more entities play a one-off animation. |
| `/replaceitem` | `Game Directors`（游戏指导者） | 是 | `/replaceitem <block: replaceitemblock> <position: x y z> <slotType: blockequipmentslot> <slotId: int> <itemName: Item> [amount: int] [data: int] [components: json]` | — | Replaces items in inventories. |
| `/ride` | `Game Directors`（游戏指导者） | 是 | `/ride <riders: target> <mode: ridemodestart> <ride: target> [teleportRules: teleportrules] [howToFill: filltype]` | — | Makes entities ride other entities, stops entities from riding, makes rides evict their riders, or summons rides or riders. |
| `/summon` | `Game Directors`（游戏指导者） | 是 | `/summon <entityType: entitytype> [spawnPos: x y z] [yRot: rotation] [xRot: rotation] [spawnEvent: entityevents] [nameTag: id]` | — | Summons an entity. |
| `/tag` | `Game Directors`（游戏指导者） | 是 | `/tag <entity: target> change <name: tagvalues>` | — | Manages tags stored in entities. |

### 玩家

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/aimassist` | `Game Directors`（游戏指导者） | 是 | `/aimassist <players: target> set [x angle: float] [y angle: float] [max distance: float] [target mode: aimassisttargetmode] [preset id: id]` | — | Enable Aim Assist |
| `/clear` | `Game Directors`（游戏指导者） | 是 | `/clear [player: target] [itemName: Item] [data: int] [maxCount: int]` | — | Clears items from player inventory. |
| `/controlscheme` | `Game Directors`（游戏指导者） | 是 | `/controlscheme <players: target> <set: cameracontrolschemeset> <control scheme: controlscheme>` | — | Sets or clears control schemes for the camera(s) of selected player(s). |
| `/gamemode` | `Game Directors`（游戏指导者） | 是 | `/gamemode <gameMode: gamemode> [player: target]` | — | Sets a player's game mode. |
| `/give` | `Game Directors`（游戏指导者） | 是 | `/give <player: target> <itemName: Item> [amount: int] [data: int] [components: json]` | — | Gives an item to a player. |
| `/hud` | `Game Directors`（游戏指导者） | 是 | `/hud <target: target> <visible: hudvisibility> [hud_element: hudelement]` | — | Configures whether elements of the on-screen display (alternately known as the 'heads up display', or 'HUD') are visible on the screen. |
| `/inputpermission` | `Game Directors`（游戏指导者） | 是 | `/inputpermission <option: option_set> <targets: target> <permission: permission> <state: state>` | — | Optionally enables or disables input permissions for a player. |
| `/teleport` | `Game Directors`（游戏指导者） | 是 | `/teleport <destination: x y z> [checkForBlocks: Boolean]` | — | Teleports entities to specific locations. |
| `/xp` | `Game Directors`（游戏指导者） | 是 | `/xp <amount: int> [player: target]` | — | Adds or removes player experience. |

### 相机

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/camera` | `Game Directors`（游戏指导者） | 是 | `/camera <players: target> attach_to_entity <entity: target>` | — | Transforms the camera for the selected player(s) to a different perspective. |
| `/camerashake` | `Game Directors`（游戏指导者） | 是 | `/camerashake add <player: target> [intensity: float] [seconds: float] [shakeType: camerashaketype]` | — | Applies shaking to the players' camera with specified intensity and duration. |

### 世界设置

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/changesetting` | `Owner`（所有者） | 是 | `/changesetting allowcheats <value: Boolean>` | — | Changes a setting on the dedicated server while it's running. |
| `/daylock` | `Game Directors`（游戏指导者） | 是 | `/daylock [lock: Boolean]` | — | Locks and unlocks the day-night cycle. |
| `/difficulty` | `Game Directors`（游戏指导者） | 是 | `/difficulty <difficulty: difficulty>` | — | Sets the difficulty level (Peaceful, Easy, Normal, Hard) using difficulty enum or integer. |
| `/gamerule` | `Game Directors`（游戏指导者） | 否 | `/gamerule` | — | Sets or queries a game rule value. |
| `/mobevent` | `Game Directors`（游戏指导者） | 是 | `/mobevent <event: mobevent> [value: Boolean]` | — | Controls what mob events are allowed to run. |
| `/tickingarea` | `Game Directors`（游戏指导者） | 是 | `/tickingarea <mode: tickingareamodeadd> <from: x y z> <to: x y z> [name: id] [preload: Boolean]` | — | Add, remove, or list ticking areas. |
| `/time` | `Game Directors`（游戏指导者） | 是 | `/time <mode: timemodeadd> <amount: int>` | — | Changes or queries the world's game time. |
| `/toggledownfall` | `Game Directors`（游戏指导者） | 是 | `/toggledownfall` | — | Toggles the weather. |
| `/weather` | `Game Directors`（游戏指导者） | 是 | `/weather <type: weathertype> [duration: int]` | — | Sets the weather in the environment. |

### 聊天与通信

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/dialogue` | `Game Directors`（游戏指导者） | 是 | `/dialogue open <npc: target> <player: target> [sceneName: id]` | — | Opens NPC dialogue for a player. |
| `/me` | `Any`（任意玩家） | 否 | `/me <message: message_root>` | — | Displays a message about yourself. |
| `/say` | `Game Directors`（游戏指导者） | 否 | `/say <message: message_root>` | — | Sends a message in the chat to other players. |
| `/tell` | `Any`（任意玩家） | 否 | `/tell <target: target> <message: message_root>` | — | Sends a private message to one or more players. |
| `/tellraw` | `Game Directors`（游戏指导者） | 否 | `/tellraw <target: target> <raw json message: json>` | — | Sends a JSON message to players. |
| `/title` | `Game Directors`（游戏指导者） | 是 | `/title <player: target> <clear: titleclear>` | — | Controls the text and behavior for screen titles using plain text. |
| `/titleraw` | `Game Directors`（游戏指导者） | 是 | `/titleraw <player: target> <clear: titlerawclear>` | — | Controls the text and behavior for screen titles using JSON messages. |

### 数据与逻辑

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/execute` | `Game Directors`（游戏指导者） | 是 | `/execute subcommand <origin: target> <chainedCommand: executechainedoption_0>` | — | Executes a command on behalf of one or more entities. |
| `/function` | `Game Directors`（游戏指导者） | 是 | `/function <name: pathcommand>` | — | Runs commands found in the corresponding function file. |
| `/schedule` | `Game Directors`（游戏指导者） | 是 | `/schedule delay add <function: pathcommand> <time: int> [DelayMode: delaymode]` | — | Schedules an action to be executed once an area is loaded, or after a certain amount of time. |
| `/scoreboard` | `Game Directors`（游戏指导者） | 是 | `/scoreboard <category: scoreboardobjectivescategory> add <objective: scoreboardobjectives> <criteria: scoreboardcriteria> [displayName: id]` | — | Tracks and displays scores for various objectives. |
| `/testfor` | `Game Directors`（游戏指导者） | 是 | `/testfor <victim: target>` | — | Counts entities (players, mobs, items, etc.) matching specified conditions. |
| `/testforblock` | `Game Directors`（游戏指导者） | 是 | `/testforblock <position: x y z> <tileName: Block> [blockStates: block_state_array]` | — | Tests whether a certain block is in a specific location. |
| `/testforblocks` | `Game Directors`（游戏指导者） | 是 | `/testforblocks <begin: x y z> <end: x y z> <destination: x y z> [mode: testforblocksmode]` | — | Tests whether the blocks in two regions match. |

### 服务器与管理

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/allowlist` | `Owner`（所有者） | 是 | `/allowlist add <name: id>` | — | Manages the server allowlist. |
| `/deop` | `Admin`（管理员） | 否 | `/deop <player: target>` | — | Revokes operator status from a player. |
| `/kick` | `Game Directors`（游戏指导者） | 否 | `/kick <name: target> <reason: message_root>` | — | Kicks a player from the server. |
| `/list` | `Any`（任意玩家） | 否 | `/list` | — | Lists players on the server. |
| `/op` | `Admin`（管理员） | 否 | `/op <player: target>` | — | Grants operator status to a player. |
| `/packstack` | `Any`（任意玩家） | 否 | `/packstack <stackType: stacktype> [verbose: verbose] [exclude-vanilla: exclude-vanilla]` | — | Prints client or server pack stack to chat |
| `/permission` | `Owner`（所有者） | 是 | `/permission list` | — | Reloads and applies permissions. |
| `/reload` | `Admin`（管理员） | 是 | `/reload [all: reload_all]` | — | Reloads all function and script files from all behavior packs. |
| `/reloadconfig` | `Owner`（所有者） | 是 | `/reloadconfig` | — | Reloads configuration files relating to variables, secrets, permissions, etc. |
| `/reloadpacketlimitconfig` | `Owner`（所有者） | 是 | `/reloadpacketlimitconfig` | — | Reload packet limit config from file |
| `/save` | `Owner`（所有者） | 是 | `/save <mode: savemode>` | — | Control or check how the game saves data to disk. |
| `/sendshowstoreoffer` | `Owner`（所有者） | 是 | `/sendshowstoreoffer <player: target> <redirectType: redirectlocation> <offerId: id>` | 仅BDS可用 | Available on dedicated server only with administrator permissions. |
| `/setmaxplayers` | `Host`（房主） | 是 | `/setmaxplayers <maxPlayers: int>` | — | Sets the maximum number of players for this game session. |
| `/stop` | `Owner`（所有者） | 是 | `/stop` | — | Stops the server. |
| `/transfer` | `Owner`（所有者） | 是 | `/transfer <pfidOrMSA: id> <server: id> [port: int]` | — | Transfers a player to another server. |
| `/wsserver` | `Admin`（管理员） | 是 | `/wsserver <serverUri: rawtext>` | — | Attempts to connect to the websocket server on the provided URL. |

### 脚本

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/gametest` | `Game Directors`（游戏指导者） | 是 | `/gametest <mode: gametestmoderunthis>` | 需要实验性脚本API | [Requires the Beta APIs experiment]. |
| `/script` | `Admin`（管理员） | 是 | `/script <mode: scriptdebugmodedebugger> <action: scriptdebuggerlisten> <port: int>` | — | Debugging options for script within Minecraft. |
| `/scriptevent` | `Game Directors`（游戏指导者） | 是 | `/scriptevent <messageId: id> <message: message_root>` | — | Causes an event to fire within script with the specified message ID and payload. |

### 声音与视觉

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/fog` | `Game Directors`（游戏指导者） | 是 | `/fog <victim: target> <mode: add> <fogId: id> <userProvidedId: id>` | — | Add or remove fog settings file. |
| `/music` | `Game Directors`（游戏指导者） | 是 | `/music queue <trackName: id> [volume: float] [fadeSeconds: float] [repeatMode: musicrepeatmode]` | — | Allows you to control playing music tracks. |
| `/particle` | `Game Directors`（游戏指导者） | 是 | `/particle <effect: id> [position: x y z]` | — | Creates a particle emitter |
| `/playsound` | `Game Directors`（游戏指导者） | 是 | `/playsound <sound: id> [player: target] [position: x y z] [volume: float] [pitch: float] [minimumVolume: float]` | — | Plays a sound. |
| `/stopsound` | `Game Directors`（游戏指导者） | 是 | `/stopsound <player: target> [sound: id]` | — | Stops a sound. |

### 战利品与配方

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/loot` | `Game Directors`（游戏指导者） | 是 | `/loot <target: targetspawn> <position: x y z> <source: sourceloot> <loot_table: id> [<tool>\|mainhand\|offhand: tool]` | — | Drops the given loot table into the specified inventory or into the world. |
| `/recipe` | `Game Directors`（游戏指导者） | 是 | `/recipe <give: give> <player: target> <recipe: unlockablerecipevalues>` | — | Supports unlocking of built-in (vanilla) recipes that a particular player can craft with. |

### 帮助

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/help` | `Any`（任意玩家） | 否 | `/help [command: commandname]` | — | Running `/help` in the chat by itself will list every command you can run. |

### 其他

| 命令 | 权限级别 | 需要作弊 | 首条语法 | 备注 | 官方说明 |
|---|---|---|---|---|---|
| `/locate` | `Game Directors`（游戏指导者） | 是 | `/locate <subcommand: locatesubcommandstructure> <structure: structurefeature> [useNewChunksOnly: Boolean]` | — | Finds the nearest specified biome or structure if it exists in the current dimension. |
| `/project` | `Game Directors`（游戏指导者） | 否 | `/project <subcommand: subcommandexport> <exportType: exporttypes>` | 编辑器相关命令 | This command contains additional tools for managing an Editor project. |
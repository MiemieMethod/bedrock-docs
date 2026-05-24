# 迁移旧版数据驱动文件

很多历史附加包能在旧版本运行，但一升级到新版本就出现“字段无效”“组件不生效”或“行为异常”。这通常不是包整体失效，而是局部JSON结构在新格式版本下发生了迁移。

本页给出一套可执行的迁移流程，帮助你把旧包逐步迁移到新版本，而不是一次性“大改全部文件”。

## 迁移前先做三件事

1. 统计所有JSON文件类型与其当前`format_version`。
2. 先备份项目，再建立一个“迁移分支”。
3. 打开内容日志，保证每次改动后都能立即看到报错。

/// warning | 不要只改版本号
仅把`format_version`改成更高版本，通常不足以完成迁移。很多字段在新版本中改名、改层级或改类型，必须同步改结构。
///

## 常见迁移项速查

下表汇总了旧版附加包中最常见的迁移点，适合作为第一轮排查清单：

| 旧写法 | 新写法 | 说明 |
|---|---|---|
| `minecraft:pick_collision` | `minecraft:aim_collision`→`minecraft:selection_box` | 方块选区组件经历过两次命名迁移。 |
| `minecraft:entity_collision` | `minecraft:block_collision`→`minecraft:collision_box` | 碰撞组件命名与结构先后调整。 |
| `minecraft:explosion_resistance` | `minecraft:destructible_by_explosion` | 从单值组件迁移为新组件结构。 |
| `minecraft:destroy_time` | `minecraft:destructible_by_mining` | 字段语义迁移为`seconds_to_destroy`。 |
| `minecraft:crafting_table.custom_description` | `minecraft:crafting_table.table_name` | 工作台组件字段重命名。 |
| `minecraft:flammable.flame_odds`/`burn_odds` | `catch_chance_modifier`/`destroy_chance_modifier` | 易燃参数命名迁移。 |
| `minecraft:food.saturation_modifier`字符串 | `saturation_modifier`浮点数 | 字段类型迁移，旧字符串枚举不再推荐。 |
| `minecraft:repairable.repair_items`允许字符串项 | 仅保留对象项 | 旧的字符串简写形式被收敛。 |

## 建议的迁移顺序

### 第1步：先迁移“会导致加载失败”的字段

优先处理内容日志中直接报错的字段，包括字段不存在、类型错误、组件名无效等。先让文件恢复可加载状态，再做行为对齐。

### 第2步：再迁移“可加载但语义变化”的字段

这类问题最容易漏测。例如文件不报错，但参数单位、默认值或行为已经变化。建议做一份“行为回归清单”，逐条进游戏验证。

### 第3步：最后处理旧兼容写法

有些旧写法在新版本仍能被兼容解析，但不再是推荐结构。建议在主要功能稳定后再统一整理，避免在排错阶段引入额外变量。

## 验证清单

每次迁移一小批文件后，按以下顺序验证：

1. 内容日志中是否仍有对应字段报错。
2. 游戏内该内容是否能加载并执行基础行为。
3. 与该内容联动的系统是否受影响（例如战利品、配方、函数触发、脚本监听）。
4. 在低配设备或联机环境下是否出现额外异常。

## 迁移策略建议

- 旧项目维护：以“最小改动可运行”为优先，先保留业务逻辑，再逐步清理旧写法。
- 新项目重构：直接采用当前官方参考结构，避免继续积累历史兼容负担。
- 团队协作：为每次迁移记录“旧字段→新字段”对照，降低后续维护成本。

如果你需要先理解`format_version`本身，再回到本页执行迁移，可以先阅读[认识格式版本](format-version.md)。

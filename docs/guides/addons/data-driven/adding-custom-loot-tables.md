# 自定义战利品表

战利品表决定了实体死亡、方块破坏、容器填充、垂钓、装备随机生成等场景中会产出哪些物品。它们属于行为包，通常放在行为包根目录下的`loot_tables`文件夹里。

## 战利品表的用途

战利品表可以在以下场景中被调用：

- **`/loot`命令**：直接给予玩家战利品或向世界投放掉落物
- **容器内容物**：结构文件中的容器（箱子、桶等）可预设战利品表，在玩家首次打开时随机填充
- **方块掉落**：自定义方块通过`loot`字段指定破坏后的掉落
- **垂钓**：钓鱼时从战利品表中随机抽取
- **实体掉落**：实体死亡时通过`minecraft:loot`组件决定掉落
- **实体装备**：通过`minecraft:equipment`组件在生成时随机穿戴装备

## 文件结构

战利品表是行为包中的一个JSON文件。虽然没有强制要求放在特定目录，但建议遵循原版惯例，放在行为包根目录下的`loot_tables`文件夹中。

/// html | div.treeview
- {{file|BP|folder}}
    - {{file|loot_tables|folder}}
        - {{file|entities|folder}}
            - {{file|my_entity.json}}
        - {{file|blocks|folder}}
            - {{file|my_block.json}}
        - {{file|chests|folder}}
            - {{file|my_structure_chest.json}}
///

一张战利品表的根结构只需要一个`pools`数组：

```json title="BP/loot_tables/entities/my_entity.json"
{
    "pools": [
        {
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "minecraft:diamond"
                }
            ]
        }
    ]
}
```

调用这张表每次都会产出1颗钻石。

## 池（Pools）

每个池（pool）是独立的抽奖单元，池与池之间不互相影响，最终掉落物是所有池的产出之和。

战利品表有两种池：**加权随机池**和**分级池**。

### 加权随机池

这是最常见的池类型。`rolls`决定从`entries`中抽取几次，每次按权重随机选取一个条目：

```json
{
    "rolls": {
        "min": 2,
        "max": 4
    },
    "entries": [
        {
            "type": "item",
            "name": "minecraft:golden_apple",
            "weight": 20
        },
        {
            "type": "item",
            "name": "minecraft:name_tag",
            "weight": 30
        },
        {
            "type": "empty",
            "weight": 50
        }
    ]
}
```

`rolls`可以是一个整数，也可以是一个含`min`和`max`的范围对象。每次抽取，条目被选中的概率等于其`weight`除以所有条目权重之和。权重越高，被选中的概率越大。

#### 幸运加成滚动次数

可以通过`bonus_rolls`和`bonus_chance`根据玩家的幸运值增加额外的抽取次数：

```json
"rolls": 1,
"bonus_rolls": 3,
"bonus_chance": 0.095
```

目前，幸运值仅由携带海之眷顾附魔钓竿的玩家垂钓时触发。

#### 条目品质

`quality`属性可以让条目的有效权重随玩家幸运值的变化而变化：

```json
{
    "type": "item",
    "name": "minecraft:diamond",
    "weight": 1,
    "quality": 2
}
```

### 分级池

分级池从`entries`中**恰好选出一个**条目，常用于随机决定实体死亡时掉落的装备品质（皮革→金→锁链→铁→钻石）。

```json
{
    "tiers": {
        "initial_range": 2,
        "bonus_rolls": 3,
        "bonus_chance": 0.095
    },
    "entries": [
        {
            "type": "loot_table",
            "name": "loot_tables/entities/armor_set_leather.json"
        },
        {
            "type": "loot_table",
            "name": "loot_tables/entities/armor_set_gold.json"
        },
        {
            "type": "loot_table",
            "name": "loot_tables/entities/armor_set_chain.json"
        },
        {
            "type": "loot_table",
            "name": "loot_tables/entities/armor_set_iron.json"
        },
        {
            "type": "loot_table",
            "name": "loot_tables/entities/armor_set_diamond.json"
        }
    ]
}
```

分级池通过包含`tiers`属性来激活（而不是`rolls`）：

- `initial_range`：初始索引在1到该值之间随机选取（默认为1，即固定从第1项开始）
- `bonus_rolls`：额外滚动的次数上限
- `bonus_chance`：每次额外滚动成功的概率（0.0～1.0），成功则索引+1

最终索引从1开始计数，如果超出了`entries`的范围，则该池不产出任何物品。

/// warning | 条件在分级池条目中被忽略
分级池中各条目上的`conditions`字段会被忽略，只有池本身的条件才有效。
///

## 条目类型

`entries`数组中每个条目必须有`type`字段。

### 物品条目（`item`）

最基础的条目类型，直接指定要产出的物品：

```json
{
    "type": "item",
    "name": "minecraft:apple",
    "weight": 1
}
```

`name`填写物品的标识符。物品数量默认为1，可通过函数`set_count`修改（见下文）。

### 战利品表条目（`loot_table`）

嵌套调用另一张战利品表，可以构建层级化的战利品系统：

```json
{
    "type": "loot_table",
    "name": "loot_tables/custom/common_drops.json",
    "weight": 1
}
```

`name`填写目标战利品表从行为包根目录开始的相对路径。

### 空条目（`empty`）

被选中时不产出任何物品，用于模拟"什么都没掉"的情况：

```json
{
    "type": "empty",
    "weight": 4
}
```

空条目在加权随机池中很直观：权重比越高，掉落为空的概率越大，读起来比用`set_count: 0`函数更清晰。

## 函数

函数是让战利品表强大的核心。你可以用函数为条目设置物品数量、自定义名称、添加附魔等。函数写在条目的`functions`数组中：

```json
{
    "type": "item",
    "name": "minecraft:dirt",
    "weight": 10,
    "functions": [
        {
            "function": "set_count",
            "count": {
                "min": 16,
                "max": 64
            }
        },
        {
            "function": "set_name",
            "name": "一堆泥土"
        }
    ]
}
```

常用函数一览：

| 函数 | 作用 |
|------|------|
| `set_count` | 设置物品数量（整数或范围对象） |
| `set_name` | 设置物品显示名称 |
| `set_lore` | 设置物品说明文字 |
| `set_damage` | 设置耐久（0.0～1.0，1.0为全新） |
| `set_data` | 设置物品数据值/附加值 |
| `random_aux_value` | 随机设置物品附加值 |
| `enchant_randomly` | 随机附魔 |
| `enchant_with_levels` | 按附魔台等级附魔 |
| `specific_enchants` | 指定附魔类型与等级 |
| `enchant_random_gear` | 随机装备附魔（有概率不附魔） |
| `looting_enchant` | 掠夺附魔增加额外掉落数量 |
| `furnace_smelt` | 若实体在火中死亡则将掉落物烧炼 |
| `set_book_contents` | 设置成书内容 |
| `set_potion` | 设置药水类型 |
| `fill_container` | 填充容器（如潜影盒）的内容 |
| `set_banner_details` | 设置旗帜类型/图案/颜色 |
| `random_dye` | 随机染色可染色物品 |
| `exploration_map` | 设置藏宝图目的地 |
| `explosion_decay` | 爆炸时有概率不掉落 |

各函数的详细用法参见[物品函数](/refs/addon/item-function/)页面。

## 条件

条件（conditions）可以限制某个池或某个条目是否生效。条件写在池或条目的`conditions`数组中：

```json
{
    "conditions": [
        {
            "condition": "killed_by_player"
        },
        {
            "condition": "random_chance_with_looting",
            "chance": 0.025,
            "looting_multiplier": 0.01
        }
    ],
    "rolls": 1,
    "entries": [
        {
            "type": "item",
            "name": "minecraft:iron_ingot",
            "weight": 1
        }
    ]
}
```

常用条件：

| 条件 | 作用 |
|------|------|
| `killed_by_player` | 被玩家（或玩家的宠物）击杀时生效 |
| `random_chance` | 按指定概率随机生效，`chance`为0.0～1.0 |
| `random_chance_with_looting` | 按概率随机生效，携带掠夺附魔时概率提升，`looting_multiplier`控制每级掠夺的加成幅度 |

## 挂接到实体

在实体行为文件的`components`中添加`minecraft:loot`组件即可让实体死亡时使用该战利品表：

```json
"minecraft:loot": {
    "table": "loot_tables/entities/my_entity.json"
}
```

路径从行为包根目录开始。

## 挂接到方块

在方块定义文件的组件中添加`minecraft:loot`组件：

```json
"minecraft:loot": {
    "loot_table": "loot_tables/blocks/my_block.json"
}
```

/// tip | 矿石战利品表进阶
如果你想给矿石方块实现类似原版的精准采集不产出额外物品的效果，请参考[工具破坏与战利品](tool-based-destruction.md)。
///

## 覆盖

战利品表通过路径引用，因此覆盖原版战利品表非常简单：在你的行为包中创建与原版路径完全一致的文件即可。对于行为包优先级较高的包，其文件会覆盖优先级较低包中相同路径的文件。

## 为结构容器添加战利品表

放置在世界中的结构（通过`/structure load`或结构方块放置）内的容器（箱子、桶等）可以绑定战利品表，在玩家第一次打开时随机填充内容。这需要在结构文件的NBT数据中为容器方块实体设置`LootTable`字符串标签。

### 准备工作

首先在行为包的`loot_tables/`目录下（推荐使用`loot_tables/chests/`子目录）创建战利品表文件。然后将结构导出到行为包的`structures/`目录。

### 使用NBT Studio（桌面端）

[NBT Studio](https://github.com/tryashtar/nbt-studio/releases)是一款可编辑结构文件NBT数据的桌面应用程序。

1. 打开NBT Studio，用 ++ctrl+o++ 打开结构文件。
2. 用 ++ctrl+f++ 搜索容器方块（如`chest`）定位到目标容器。
3. 定位至 `block_position_data` > `block_entity_data`，在此节点下新建一个字符串（String）标签。
4. 将标签名设为`LootTable`，值设为战利品表路径（从行为包根目录起，如`loot_tables/chests/my_structure_loot.json`）。
5. 用 ++ctrl+s++ 保存文件。

<!-- 截图：NBT Studio主界面打开结构文件后的树状展示，展示block_position_data > block_entity_data下新增LootTable字符串标签的样子。 -->

### 使用Loot Tabler（浏览器端）

[Loot Tabler](https://mcbe-essentials.github.io/structure-editor/loot-tabler) 是一款无需安装即可使用的在线工具，适合在移动设备上操作。

1. 访问网站，点击"Upload"上传结构文件。
2. 在容器列表中找到目标容器（通过位置坐标等信息定位）。
3. 在"Loot Table"输入框填入战利品表路径。"Loot Table Seed"留空或填`0`可实现每次随机生成，填入特定数值则固定生成结果。
4. 下载修改后的结构文件，放回行为包的`structures/`目录。

/// tip | 移动设备导出结构
Minecraft基岩版移动端原生不支持导出结构到可访问的文件系统位置，可使用[Export Structure Button](https://mcpedl.com/export-structure-button-android-addon/)资源包解决此问题。
///

### 使用拼图处理器（适用于拼图结构）

对于使用拼图结构系统生成的结构，可以通过处理器（processor）将战利品表应用到方块上，无需手动编辑NBT数据：

```json title="minecraft:processor_list"
{
    "processor_type": "minecraft:rule",
    "rules": [
        {
            "block_entity_modifier": {
                "type": "minecraft:append_loot",
                "loot_table": "loot_tables/chests/my_structure_loot.json"
            },
            "input_predicate": {
                "predicate_type": "minecraft:blockstate_match",
                "block": "minecraft:chest",
                "states": {
                    "minecraft:cardinal_direction": "north"
                }
            },
            "output_state": {
                "name": "minecraft:chest",
                "states": {
                    "minecraft:cardinal_direction": "north"
                }
            }
        }
    ]
}
```

由于箱子有4个朝向，你需要为每个朝向各写一条规则。拼图处理器的详细用法请参考[通过结构模板地物生成结构](generating-structures.md)。

### 测试验证

加载结构（`/structure load`），然后打开对应容器，确认内容物与战利品表定义一致。

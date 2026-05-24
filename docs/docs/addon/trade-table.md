# 交易表

**交易表（Trade Table）**是Minecraft基岩版行为包中定义交易实体可提供交易内容的数据文件。交易表描述交易实体向玩家索取的物品、给予的物品、交易次数限制、交易经验和层级解锁条件，主要用于村民、流浪商人和其他具有交易能力的实体。

## 概述

交易表以JSON格式定义。在实体的行为定义中，交易表通常通过`minecraft:economy_trade_table`组件引用；`minecraft:trade_table`组件也可引用交易表，但官方教程将`minecraft:economy_trade_table`描述为当前优先使用的形式。当玩家与拥有交易表的实体交互时，游戏会依据交易表、实体交易经验和交易随机规则生成交易列表。

交易表文件位于行为包的`trading/`目录中。原版经济交易表位于`trading/economy_trades/`目录下，行为包可以通过相同路径覆盖原版交易表，也可以在实体组件中指向自定义路径。

## 基本结构

交易表由多个**层级（Tier）**组成。层级根据交易实体自身的交易经验解锁，而不是根据玩家经验解锁。第一层级始终可用；后续层级通常按`total_exp_required`从低到高排列。交易系统遇到高于实体当前交易经验的层级后，后续层级不会继续检查。

每个层级可以直接包含交易，也可以包含若干**组（Group）**。组用于从一组候选交易中随机选择指定数量的交易。交易项目本身由交易实体需要的物品、给予的物品、最大使用次数、实体获得的交易经验和玩家是否获得经验等数据组成。

```json title="交易表结构概要"
{
  "tiers": [
    {
      "total_exp_required": 0,
      "groups": [
        {
          "num_to_select": 2,
          "trades": [
            {
              "wants": [{"item": "minecraft:wheat", "quantity": 20}],
              "gives": [{"item": "minecraft:emerald"}],
              "max_uses": 16,
              "trader_exp": 2
            }
          ]
        }
      ]
    }
  ]
}
```

## 交易项目

每个交易项目包含以下核心字段。字段的完整类型、默认值和结构见[交易表参考](../../refs/addon/trade-table.md)。

/// define
`wants`

- 玩家需要提供的物品列表，最多两个物品槽位。每个物品指定标识符和数量。槽位内容可以是固定的物品描述符，也可以是**选择（Choice）**。

`gives`

- 玩家会获得的物品列表，仅支持一个槽位。每个物品指定标识符、数量，还可以附加函数修饰（如附魔、地图数据等）。

`max_uses`

- 该交易可使用的最大次数。当次数用尽后，交易会暂时锁定，直到实体进行补货。默认为`7`；设为`0`时交易可见但不可使用；设为负数时交易永不锁定。

`trader_exp`

- 完成该交易时给予实体的交易经验值，用于提升实体的交易等级。默认为`1`。

`reward_exp`

- 完成该交易时玩家是否获得经验球。布尔值，默认为`true`。

`weight`

- 在同一随机候选集合内影响交易被选中的权重。

///

## 选择

**选择（Choice）**是`wants`槽位中物品的一种特殊形式，用于在数个候选物品中随机选取一种作为该槽位的要求。选择在每个实体实例生成交易时一次性确定，之后不再改变。

```json title="选择示例"
{
  "choice": [
    {
      "item": "minecraft:wheat",
      "quantity": 20
    },
    {
      "item": "minecraft:potato",
      "quantity": 15
    }
  ]
}
```

`choice`数组中的每个元素均为普通的物品描述符。当一个`wants`槽位条目同时包含物品字段和`choice`字段时，游戏仅使用`choice`部分，物品字段被忽略。选择不支持嵌套。目前没有为`choice`中各物品设置不同权重的机制，但可通过重复条目来变相增加某一物品被选中的概率。

## 价格乘数

交易物品的`price_multiplier`字段控制价格随供需关系变化而浮动的幅度。该字段可选，默认为`0`。价格乘数仅影响`wants`中**第一个槽位**的物品数量（在新版价格系统中）。

交易价格受以下因素影响而波动：
- 交易需求增加（在同一交易补货之间重复交易导致）；
- 实体近期被治愈（如僵尸村民被治愈）；
- 实体附近存在近期被治愈的同类实体；
- 与拥有"英雄村庄"效果的玩家交易。

需求引发的价格变化遵循如下线性关系（不考虑其他因素时）：

> 总价格 = 基础数量 × (1 + 价格乘数 × 需求量)

当价格乘数为`0`时，大多数情况下价格保持不变。

## 交易等级

交易实体通过积累交易经验来提升等级，每个等级解锁对应层级的交易内容。原版村民拥有5个等级：新手、学徒、老手、专家和大师，分别对应5个主要交易层级。官方教程示例中常见的经验阈值包括`0`、`10`、`70`、`150`和`250`。

交易次数达到`max_uses`后，该交易会锁定，直到交易实体在其工作站补货。`minecraft:trade_resupply`组件负责处理补货逻辑。

## 交易函数

交易项目中的物品可以附加**函数（Function）**来修饰物品属性，函数系统与战利品表共享。常见的交易函数包括：

- **`enchant_with_levels`**：以指定的等级范围进行随机附魔。作用于`gives`中的物品时，还会将第一个`wants`槽位的价格增加对应等级值。
- **`enchant_randomly`**：随机附加一个魔咒。
- **`enchant_book_for_trading`**：为附魔书生成适合交易的魔咒，并根据魔咒等级和属性计算第一个`wants`槽位的价格。该函数专为交易表设计。
- **`set_name`**：设置物品显示名称。
- **`set_lore`**：设置物品说明文字。
- **`set_damage`**：设置物品耐久比例。
- **`set_data`**：设置物品数据值。
- **`exploration_map`**：将地图转换为藏宝图（交易表中仅支持`monument`和`mansion`目的地）。
- **`set_count`**：在交易表中**不可用**；物品数量应通过`quantity`字段控制。

以下函数在交易表中**无效**，不应使用：`set_count`、`furnace_smelt`、`looting_enchant`。以下函数可以出现在`wants`物品上，但不会限制玩家提供物品的属性，因此对限定要求物品无效：`set_name`、`set_lore`、`set_damage`、`set_book_contents`、`random_dye`、`fill_container`。

完整函数说明参见[战利品函数](item-function.md)。

## 覆盖

交易表不依赖标识符注册，而是通过路径引用。因此，可以通过在行为包中放置与原版交易表路径相同的文件来覆盖原版交易表。以下为原版各交易实体对应的交易表路径：

| 交易实体 | 路径 |
|--------|------|
| 石匠 | `BP/trading/economy_trades/stone_mason_trades.json` |
| 农民 | `BP/trading/economy_trades/farmer_trades.json` |
| 渔夫 | `BP/trading/economy_trades/fisherman_trades.json` |
| 屠夫 | `BP/trading/economy_trades/butcher_trades.json` |
| 牧羊人 | `BP/trading/economy_trades/shepherd_trades.json` |
| 皮革匠 | `BP/trading/economy_trades/leather_worker_trades.json` |
| 图书管理员 | `BP/trading/economy_trades/librarian_trades.json` |
| 制图师 | `BP/trading/economy_trades/cartographer_trades.json` |
| 牧师 | `BP/trading/economy_trades/cleric_trades.json` |
| 工具匠 | `BP/trading/economy_trades/tool_smith_trades.json` |
| 武器匠 | `BP/trading/economy_trades/weapon_smith_trades.json` |
| 箭匠 | `BP/trading/economy_trades/fletcher_trades.json` |
| 盔甲匠 | `BP/trading/economy_trades/armorer_trades.json` |
| 流浪商人 | `BP/trading/economy_trades/wandering_trader_trades.json` |

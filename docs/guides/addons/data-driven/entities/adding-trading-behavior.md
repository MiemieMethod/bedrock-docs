# 添加交易行为

想让你的自定义实体可以和玩家做生意吗？这一节就来讲讲怎么给实体加上交易界面。

## 前置知识

在开始之前，你需要了解实体的组件和组件组机制。如果你还不清楚这两个概念，建议先看看[第一个实体](adding-custom-entities.md)里的相关内容，然后再回来。

你还需要准备一张[交易表](../../../../docs/addon/trade-table.md)文件。如果你还没写，可以先随便写一张最简单的：

```json title="BP/trading/my_entity_trades.json"
{
  "tiers": [
    {
      "trades": [
        {
          "wants": [
            {
              "item": "minecraft:emerald",
              "quantity": 1
            }
          ],
          "gives": [
            {
              "item": "minecraft:diamond",
              "quantity": 1
            }
          ],
          "max_uses": 5,
          "trader_exp": 2
        }
      ]
    }
  ]
}
```

这张表定义了一个最简单的交易：玩家用1颗绿宝石换1颗钻石，最多可以做5次。

## 添加交易组件

打开你的实体行为文件，在组件组（`component_groups`）里加一个专门用于交易状态的组，比如叫`wiki:trader`：

```json title="BP/entities/my_entity.json（片段）"
"component_groups": {
  "wiki:trader": {
    "minecraft:trade_table": {
      "display_name": "我的交易者",
      "table": "trading/my_entity_trades.json",
      "new_screen": true
    }
  }
}
```

`display_name`是交易界面顶部显示的标题文字；`table`是交易表文件相对于行为包根目录的路径；`new_screen`设为`true`使用村庄与掠夺版本后的新式交易界面，设为`false`则使用旧式界面。

/// warning | 不要直接放在主组件里
如果你把`minecraft:trade_table`直接放在顶层`components`中，而不是放在组件组里，会导致所有实体的交易界面显示空白。请务必通过组件组来添加这个组件。
///

## 添加必要的AI意向

接下来，在主`components`块（而不是组件组）里加上交易AI意向：

```json title="BP/entities/my_entity.json（片段）"
"components": {
  "minecraft:behavior.trade_with_player": {}
}
```

这个AI意向告诉实体：当玩家试图与它交易时，允许打开交易界面。

### 可选：让实体展示感兴趣的物品

如果你想让实体像村民一样，会把玩家手持的物品拿起来"感兴趣地看一看"，可以再加一个AI意向：

```json
"minecraft:behavior.trade_interest": {
  "within_radius": 6.0,
  "interest_time": 45.0,
  "trigger_chance": 0.1,
  "cooldown": 2.0,
  "carried_item_switch_time": 2.0,
  "cooldown_after_being_attacked": 20.0
}
```

这个是可选的，不影响基本交易功能。

### 可选：补货机制

如果你希望实体能定期补充交易库存（就像村民一样），需要加上：

```json
"minecraft:trade_resupply": {}
```

没有这个组件时，交易次数耗尽后就永远无法再次使用了。

## 在事件中激活组件组

最后，要让实体在生成时自动进入交易状态，需要在`events`中添加：

```json title="BP/entities/my_entity.json（片段）"
"events": {
  "minecraft:entity_spawned": {
    "add": {
      "component_groups": ["wiki:trader"]
    }
  }
}
```

这样实体一生成，`wiki:trader`组件组就会被激活，交易功能就可以正常使用了。

## 完整示例

把以上内容整合在一起，实体行为文件的关键部分长这样：

```json title="BP/entities/my_entity.json"
{
  "format_version": "1.20.0",
  "minecraft:entity": {
    "description": {
      "identifier": "wiki:my_entity",
      "is_summonable": true,
      "is_spawnable": true
    },
    "component_groups": {
      "wiki:trader": {
        "minecraft:trade_table": {
          "display_name": "我的交易者",
          "table": "trading/my_entity_trades.json",
          "new_screen": true
        }
      }
    },
    "components": {
      "minecraft:physics": {},
      "minecraft:behavior.trade_with_player": {
        "priority": 1
      },
      "minecraft:trade_resupply": {}
    },
    "events": {
      "minecraft:entity_spawned": {
        "add": {
          "component_groups": ["wiki:trader"]
        }
      }
    }
  }
}
```

## 进阶：经济交易组件

`minecraft:economy_trade_table`是`minecraft:trade_table`的增强版本，包含了更多与村庄和掠夺版本相关的配置选项，例如声誉、治愈折扣等。它的用法与`minecraft:trade_table`基本相同，主要区别在于附带了更多参数可以调节价格折扣行为和交易解锁时的视觉效果。如果你的实体不需要模拟原版村民的经济系统，使用`minecraft:trade_table`就足够了。

## 测试一下

在游戏中生成你的实体，然后右键（或长按）它，应该就能看到交易界面弹出来了。如果界面是空的，请检查：

1. `trade_table`组件是否在**组件组**里，而不是直接在`components`里。
2. 行为包路径中的交易表文件是否存在。
3. `minecraft:entity_spawned`事件是否正确地添加了`wiki:trader`组件组。

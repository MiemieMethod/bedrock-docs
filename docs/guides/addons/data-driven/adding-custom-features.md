# 自定义地物

地物是世界生成阶段放进地形中的内容，例如树、矿石、花、泉水、结构模板和散植组合。地物定义放在行为包`features`目录，地物规则放在`feature_rules`目录。

## 用结构做第一个地物

先准备结构文件：

/// html | div.treeview
- `demo_BP`
    - `structures`
        - `demo`
            - `balloon.mcstructure`
    - `features`
        - `balloon_feature.json`
    - `feature_rules`
        - `balloon_rule.json`
///

地物文件：

```json title="features/balloon_feature.json"
{
  "format_version": "1.13.0",
  "minecraft:structure_template_feature": {
    "description": {
      "identifier": "demo:balloon_feature"
    },
    "structure_name": "demo:balloon",
    "adjustment_radius": 8,
    "facing_direction": "random",
    "constraints": {
      "unburied": {},
      "block_intersection": {
        "block_allowlist": [
          "minecraft:air"
        ]
      }
    }
  }
}
```

## 添加地物规则

```json title="feature_rules/balloon_rule.json"
{
  "format_version": "1.13.0",
  "minecraft:feature_rules": {
    "description": {
      "identifier": "demo:balloon_rule",
      "places_feature": "demo:balloon_feature"
    },
    "conditions": {
      "placement_pass": "surface_pass",
      "minecraft:biome_filter": [
        {
          "test": "has_biome_tag",
          "operator": "==",
          "value": "forest"
        }
      ]
    },
    "distribution": {
      "iterations": 1,
      "coordinate_eval_order": "zxy",
      "x": 0,
      "y": "query.heightmap(variable.worldx, variable.worldz)",
      "z": 0
    }
  }
}
```

`placement_pass`决定生成阶段，`biome_filter`限制生物群系，`distribution`决定每个区块中尝试放置的位置。官方教程示例使用`query.heightmap(variable.worldx, variable.worldz)`把结构放到地表高度。

## 控制密度

不要一开始就把`iterations`设得很高。地物会参与世界生成，过多结构可能导致卡顿或过密。先用明显结构和较高概率确认规则生效，再逐步降低到合理密度。

## 地物类型怎么选

- 单方块：用`single_block_feature`。
- 矿石：用`ore_feature`。
- 结构：用`structure_template_feature`。
- 随机选一个子地物：用`weighted_random_feature`。
- 批量散布：用`scatter_feature`。
- 按顺序依赖放置：用`sequence_feature`。

复杂世界生成通常是多个简单地物组合起来的，不必把所有逻辑塞进一个文件。

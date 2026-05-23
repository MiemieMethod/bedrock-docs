# 方块状态与置换

方块状态让一个方块标识符可以表达多种不同形态，而置换则让不同的状态组合对应不同的组件配置。这一页教你如何定义和使用它们。

## 声明方块状态

自定义方块状态在行为包方块文件的 `description.states` 字段中定义：

```json title="BP/blocks/my_block.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:my_block",
            "states": {
                "wiki:is_on": [false, true],
                "wiki:mode": ["idle", "active", "broken"],
                "wiki:level": {
                    "values": { "min": 0, "max": 7 }
                }
            }
        }
    }
}
```

/// note | 状态命名
自定义状态名必须包含命名空间前缀（如 `wiki:`），以避免与原版状态冲突。
///

### 状态类型

| 类型 | 写法示例 | 限制 |
|------|---------|------|
| 布尔值 | `[false, true]` | 2个值 |
| 整数数组 | `[0, 1, 2, 3]` | 最多16个值 |
| 字符串数组 | `["north", "south", "east", "west"]` | 最多16个值 |
| 整数范围 | `{"values": {"min": 0, "max": 7}}` | 最多16个值（含首尾） |

每个状态最多只能有**16个**有效取值。如果你需要更多组合，可以将多个状态组合使用——参见本页末尾的[规避状态上限](#规避状态上限)。

## 编写置换

置换是一系列带条件的组件覆盖，放在 `permutations` 数组中。只有条件为真的那些置换才会应用到当前方块上：

```json title="BP/blocks/my_light.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:my_light",
            "states": {
                "wiki:is_on": [false, true]
            }
        },
        "components": {
            "minecraft:material_instances": {
                "*": { "texture": "wiki:light_off" }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('wiki:is_on') == true",
                "components": {
                    "minecraft:light_emission": 15,
                    "minecraft:material_instances": {
                        "*": { "texture": "wiki:light_on" }
                    }
                }
            }
        ]
    }
}
```

置换中的组件会**覆盖**基础组件中同名的条目。同一个状态组合下，多个条件都为真时，后面的置换覆盖前面的。

/// warning | 置换数量上限
单个方块所有状态取值组合（即置换总数）上限为**65,536**（16位），整个世界的所有自定义方块置换总数上限同样是65,536，超出时会输出警告但不报错。
///

## 在Molang中读取状态

在置换条件、几何体骨骼可见性等Molang表达式中，使用 `q.block_state()` 查询当前状态值：

```molang
q.block_state('wiki:is_on') == true
q.block_state('wiki:mode') == 'active'
q.block_state('wiki:level') >= 4
```

也可以在组合条件中用 `&&`（与）和 `||`（或）：

```molang
q.block_state('wiki:mode') == 'active' && q.block_state('wiki:level') >= 4
```

## 通过命令操作状态

放置方块时指定状态：

```mcfunction
/setblock ~ ~ ~ wiki:my_light ["wiki:is_on"=true]
```

测试特定状态的方块（`testforblock` 命令中）：

```mcfunction
/testforblock ~ ~ ~ wiki:my_light ["wiki:is_on"=true]
```

在 `/execute if block` 中同样支持状态过滤：

```mcfunction
/execute if block ~ ~ ~ wiki:my_light["wiki:is_on"=true] run say 灯是亮的
```

## 通过脚本API操作状态 <!-- md:flag vanilla -->

### 读取状态

```js
const block = dimension.getBlock(location);
const state = block.permutation.getState("wiki:is_on");
console.log(`is_on: ${state}`);
```

### 设置状态

```js
const block = dimension.getBlock(location);
block.setPermutation(
    block.permutation.withState("wiki:is_on", true)
);
```

`withState` 不修改原有置换对象，而是返回一个新的置换对象。

### 构造置换

如果需要将方块切换到完全不同的置换：

```js
import { BlockPermutation } from "@minecraft/server";

const newPermutation = BlockPermutation.resolve("wiki:my_light", {
    "wiki:is_on": true,
    "wiki:mode": "active"
});
block.setPermutation(newPermutation);
```

## 规避状态上限

每个状态最多16个值的限制有时不够用。解决方案是**多状态组合**：两个各有13个值的状态可以产生169种组合，远超单个状态的16种。

例如，需要26种字母状态，可以这样拆分：

```json title="description > states"
"states": {
    "wiki:division": [1, 2],
    "wiki:value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
}
```

然后在置换条件中组合判断：

```molang
q.block_state('wiki:division') == 1 && q.block_state('wiki:value') == 1
```

`division=1, value=1` 到 `division=1, value=13` 表示A～M，`division=2, value=1` 到 `division=2, value=13` 表示N～Z，总共26种，只用了15个不重复值。

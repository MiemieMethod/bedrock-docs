# 物品与方块格式迁移

旧版附加包常见的`1.16.100`至`1.19.40`阶段物品和方块定义，包含许多后来被重命名、压平或移动的字段。维护这些文件时，不要只把`format_version`改成较新的数字，而应先判断每个字段在目标格式中的语义是否已经改变。

/// warning | 本页用于迁移旧包
本页面向旧项目维护和资料辨析，不是新项目的默认写法清单。新建物品和方块时，请优先使用当前教程和当前参考资料。
///

## 迁移前检查

1. 在当前游戏中原样加载旧包，记录内容日志。
2. 确认文件类型和实际`format_version`。
3. 对照当前官方参考、Bedrock Wiki格式历史和样本包确认字段是否仍被接受。
4. 一次只迁移一种文件类型，并在每次迁移后重新测试。

格式版本变化可能是“版本化”的。只有当文件的`format_version`达到对应版本时，某些新解析规则才会生效。相反，低格式版本可能仍使用旧解析逻辑。

## 物品迁移要点

### `minecraft:durability`

旧物品格式中，耐久组件曾出现`max_damage`字段。迁移到新格式时，应使用`max_durability`表达最大耐久。

```json title="旧写法"
"minecraft:durability": {
  "max_damage": 100
}
```

```json title="迁移后"
"minecraft:durability": {
  "max_durability": 100
}
```

### `minecraft:food`

旧资料中可能使用字符串形式的`saturation_modifier`，例如`"poor"`、`"normal"`或`"supernatural"`。较新的物品组件使用数值表达饱和度修饰符。迁移时不要机械替换为任意数字，应根据当前物品组件参考重新确认设计目标。

### `minecraft:repairable`

旧格式允许`repair_items`中出现较简单的字符串数组写法。迁移时应改为对象形式，明确可修复物品和修复量。

## 方块迁移要点

### 创造菜单分类

旧方块组件`minecraft:creative_category`后来被移入描述信息中的`menu_category`。迁移时应把分类信息放入`description.menu_category`，并结合当前格式检查`category`、`group`和`is_hidden_in_commands`。

```json title="较新描述位置"
"description": {
  "identifier": "example:custom_block",
  "menu_category": {
    "category": "construction",
    "group": "itemGroup.name.construction"
  }
}
```

### 碰撞与选择框

旧资料中常见以下名称迁移链：

| 旧名称 | 中间名称 | 较新名称 | 用途 |
|--------|----------|----------|------|
| `minecraft:pick_collision` | `minecraft:aim_collision` | `minecraft:selection_box` | 玩家准星选择范围。 |
| `minecraft:entity_collision` | `minecraft:block_collision` | `minecraft:collision_box` | 实体碰撞范围。 |

旧对象中的`enabled`字段也可能在后续格式中改为直接使用布尔值表达启用或禁用。迁移时应确认目标组件允许布尔简写还是对象写法。

### 破坏时间与爆炸抗性

早期方块使用`minecraft:destroy_time`表达开采耗时，使用`minecraft:explosion_resistance`表达爆炸抗性。较新格式分别使用：

- `minecraft:destructible_by_mining`
- `minecraft:destructible_by_explosion`

```json title="较新开采组件"
"minecraft:destructible_by_mining": {
  "seconds_to_destroy": 1.5
}
```

```json title="较新爆炸组件"
"minecraft:destructible_by_explosion": {
  "explosion_resistance": 3.0
}
```

这些组件在当前参考中还支持布尔简写。使用`false`通常表示不可由对应方式摧毁，使用`true`表示采用默认行为；精确行为应以目标版本参考和实际测试为准。

### 亮度组件

旧方块亮度字段经历过多次命名变化：

| 旧名称 | 较新名称 | 说明 |
|--------|----------|------|
| `minecraft:block_light_absorption` | `minecraft:block_light_filter`，后为`minecraft:light_dampening` | 控制光线穿过方块时被阻挡的程度。 |
| `minecraft:block_light_emission` | `minecraft:light_emission` | 控制方块发出的光照。 |

迁移时还要注意数值单位变化。旧资料中发光强度可能使用`0.0`至`1.0`的小数，而较新组件通常使用`0`至`15`的光照等级。

### 其他常见压平

一些旧组件曾允许对象包裹单个字段，后续格式改为直接使用该字段值：

| 组件 | 旧对象字段 | 迁移方向 |
|------|------------|----------|
| `minecraft:loot` | `loot_table` | 直接使用战利品表路径字符串。 |
| `minecraft:breathability` | `breathing_type` | 直接使用`"solid"`或`"air"`。 |
| `minecraft:destroy_time` | `destroy_time` | 迁移到`minecraft:destructible_by_mining`。 |
| `minecraft:display_name` | `display_name` | 直接使用本地化键。 |
| `minecraft:friction` | `friction` | 直接使用数值，并确认目标格式的取值含义。 |
| `minecraft:geometry` | `geometry` | 直接使用几何体标识符。 |
| `minecraft:map_color` | `map_color` | 直接使用颜色值。 |

### `minecraft:part_visibility`

旧版本中，`minecraft:part_visibility`组件使用`rules`数组来描述各部分的显示条件：

```json title="旧写法"
"minecraft:part_visibility": {
  "rules": [
    { "bone": "wing", "value": "q.is_flying" }
  ]
}
```

较新格式将`rules`更名为`conditions`，并改为对象形式：

```json title="迁移后"
"minecraft:part_visibility": {
  "conditions": {
    "wing": "q.is_flying"
  }
}
```

### `minecraft:crafting_table`

1.19.10前，自定义工作台使用`custom_description`字段描述界面标题：

```json title="旧写法"
"minecraft:crafting_table": {
  "custom_description": "我的工作台",
  "crafting_tags": ["my_table"]
}
```

1.19.10起，`custom_description`更名为`table_name`：

```json title="迁移后"
"minecraft:crafting_table": {
  "table_name": "我的工作台",
  "crafting_tags": ["my_table"]
}
```

### `minecraft:friction`的取值方向

旧版方块格式中，`minecraft:friction`的值含义与1.19.20之后发生了反转。旧格式的值表示**摩擦力本身**（值越大越滑），而1.19.20起，值表示**阻力系数**（值越小越滑，与Java版语义对齐）。原版冰块在旧格式中为约`0.98`，迁移后约为`0.02`。迁移时务必通过实际游戏测试验证效果，而不能直接照搬旧数值。

## 不建议自动批量替换

旧字段名称和新字段名称之间并不总是一一等价。某些字段还伴随单位、默认值、实验性状态或取值范围变化。自动批量替换可能让文件通过语法检查，却在游戏内表现不同。

较安全的做法是按组件逐项迁移，并把内容日志、当前参考和实际游戏表现一起作为判断依据。

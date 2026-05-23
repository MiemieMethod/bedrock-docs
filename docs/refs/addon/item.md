# 物品定义

本页列出行为包`items/`目录中物品定义文件的主要结构、常用物品组件、使用优先级和原版物品标签。物品定义用于声明一个可被命令、配方、战利品表、实体装备、容器和脚本等系统引用的物品。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 物品定义文件的格式版本。官方示例使用`1.20.20`；较新的组件或字段可能要求更高版本。 |
| `minecraft:item` | 对象 | 未设置 | 物品定义对象，包含`description`和`components`。 |

## `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 物品的赋命名空间标识符。自定义物品应使用自己的命名空间，不应使用`minecraft`命名空间。 |
| `menu_category` | 对象 | 未设置 | 控制物品在创造模式物品栏中的分类、组和命令可见性。 |

### `menu_category`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `category` | 字符串 | `items` | 物品所在的创造模式分类。官方参考将默认值列为`items`。 |
| `group` | 字符串 | 未设置 | 物品所在的创造模式物品组。组名最长为256个字符。 |
| `is_hidden_in_commands` | 布尔值 | `false` | 是否在命令中隐藏该物品。未设置时，命令默认可以使用该物品。 |

## `components`

`components`是物品组件集合。每个组件以组件标识符为键，值为布尔值、数值、字符串、对象或数组，具体形态由组件决定。

组件字段、依赖关系和已弃用项详见[物品组件](item-component.md)。

| 组件 | 用途 |
| --- | --- |
| `minecraft:allow_off_hand` | 控制物品是否可放入副手槽位。 |
| `minecraft:block_placer` | 使物品可在使用时放置方块。 |
| `minecraft:bundle_interaction` | 启用收纳袋式交互和工具提示。 |
| `minecraft:can_destroy_in_creative` | 控制物品是否可在创造模式中破坏方块。 |
| `minecraft:compostable` | 使物品可用于堆肥桶，并定义增加堆肥层的概率。 |
| `minecraft:cooldown` | 为物品使用添加冷却。 |
| `minecraft:damage` | 定义物品攻击时的额外伤害。 |
| `minecraft:damage_absorption` | 使穿戴的物品吸收原本会作用于穿戴者的伤害。 |
| `minecraft:digger` | 将物品配置为工具，使其更快破坏特定方块。 |
| `minecraft:display_name` | 设置物品显示名。 |
| `minecraft:durability` | 设置物品耐久，并允许在铁砧、砂轮或工作台中合并。 |
| `minecraft:durability_sensor` | 使物品在受到耐久损耗时触发效果。 |
| `minecraft:dyeable` | 使物品可像皮革盔甲一样被染色。 |
| `minecraft:enchantable` | 定义可应用于该物品的魔咒类型。 |
| `minecraft:entity_placer` | 使物品可在世界中放置实体。 |
| `minecraft:fire_resistant` | 控制掉落物是否免疫火和熔岩燃烧。 |
| `minecraft:food` | 使物品可被玩家食用。 |
| `minecraft:fuel` | 使物品可作为熔炉燃料。 |
| `minecraft:glint` | 控制物品是否显示附魔光效。 |
| `minecraft:hand_equipped` | 控制物品在玩家手中是否按工具方式渲染。 |
| `minecraft:hover_text_color` | 设置鼠标悬停时物品名的颜色。 |
| `minecraft:icon` | 设置物品在界面等位置使用的图标。 |
| `minecraft:interact_button` | 控制触摸控制中的交互按钮是否显示及显示文本。 |
| `minecraft:kinetic_weapon` | 使物品造成动能伤害及相关效果。 |
| `minecraft:liquid_clipped` | 控制物品使用时是否与液体方块交互。 |
| `minecraft:max_stack_size` | 设置物品最大堆叠数量。 |
| `minecraft:piercing_weapon` | 使物品沿使用者视线方向对直线上的实体造成伤害。 |
| `minecraft:projectile` | 将物品定义为可由发射器射出或可被`minecraft:shooter`使用的弹射物。 |
| `minecraft:rarity` | 设置基础稀有度，并影响鼠标悬停时物品名的颜色。 |
| `minecraft:record` | 使物品可作为唱片播放音乐。 |
| `minecraft:repairable` | 定义可用于修复该物品的物品及修复量。 |
| `minecraft:seed` | 使物品可作为种子种植。 |
| `minecraft:shooter` | 使物品可发射弹射物，行为类似弓或弩。 |
| `minecraft:should_despawn` | 控制物品实体是否会自然消失。 |
| `minecraft:stacked_by_data` | 控制附加值不同的同类物品是否可以堆叠。 |
| `minecraft:storage_item` | 使物品可保存关联动态容器的数据。 |
| `minecraft:storage_weight_limit` | 设置存储物品可容纳的最大重量。 |
| `minecraft:storage_weight_modifier` | 修改存储物品的重量计算。 |
| `minecraft:swing_duration` | 设置开采或攻击时播放挥动动画的持续时间。 |
| `minecraft:swing_sounds` | 覆盖使用者挥动时发出的声音。 |
| `minecraft:tags` | 为物品附加标签。 |
| `minecraft:throwable` | 使物品可像雪球或末影珍珠一样被玩家投掷。 |
| `minecraft:use_animation` | 指定玩家使用物品时播放的动画。 |
| `minecraft:use_modifiers` | 设置与发射、投掷、食物等组件配合使用时的使用时长。 |
| `minecraft:wearable` | 使物品可被玩家穿戴到指定装备槽位。 |

Microsoft Learn还列出`minecraft:chargeable`、`minecraft:custom_components`、`minecraft:render_offsets`、`minecraft:use_duration`和`minecraft:weapon`等内部或已弃用项，并说明它们不适合作为自定义内容中的普通物品组件使用。

## 使用优先级

当一个物品同时具有多种使用行为时，游戏按固定顺序尝试触发行为：

1. “对方块使用”行为优先执行，`minecraft:entity_placer`先尝试放置实体，随后`minecraft:block_placer`尝试放置方块。
2. 普通“使用”行为随后执行，例如`minecraft:food`、`minecraft:wearable`、`minecraft:shooter`和`minecraft:throwable`。
3. 当物品具有发射器行为时，`minecraft:projectile`先尝试从发射器射出，随后`minecraft:entity_placer`尝试生成实体。

/// warning | 多重行为
同一物品若同时尝试触发多个组件行为，可能出现非预期结果。设计物品时应避免在一个物品上叠加彼此竞争的使用行为。
///

## 原版物品标签

`minecraft:tags`可以为物品添加标签。创作者可以定义自己的标签，但只有原版物品标签可以使用`minecraft:`命名空间。

| 类别 | 标签 |
| --- | --- |
| 盔甲 | `minecraft:is_armor`、`minecraft:horse_armor`、`minecraft:nautilus_armor`、`minecraft:harness` |
| 食物 | `minecraft:is_meat`、`minecraft:is_cooked`、`minecraft:is_food` |
| 猪灵交易 | `minecraft:piglin_loved`、`minecraft:piglin_repellents` |
| 锻造台 | `minecraft:transformable_items`、`minecraft:transform_materials`、`minecraft:transform_templates` |
| 硫磺立方体原型 | `minecraft:sulfur_cube_archetype_bouncy`、`minecraft:sulfur_cube_archetype_regular`、`minecraft:sulfur_cube_archetype_slow_flat`、`minecraft:sulfur_cube_archetype_fast_flat`、`minecraft:sulfur_cube_archetype_light`、`minecraft:sulfur_cube_archetype_fast_sliding`、`minecraft:sulfur_cube_archetype_slow_sliding`、`minecraft:sulfur_cube_archetype_sticky`、`minecraft:sulfur_cube_archetype_high_resistance`、`minecraft:sulfur_cube_archetype_explosive` |
| 品质 | `minecraft:chainmail_tier`、`minecraft:copper_tier`、`minecraft:diamond_tier`、`minecraft:golden_tier`、`minecraft:iron_tier`、`minecraft:leather_tier`、`minecraft:netherite_tier`、`minecraft:stone_tier`、`minecraft:wooden_tier` |
| 工具 | `minecraft:digger`、`minecraft:is_axe`、`minecraft:is_hoe`、`minecraft:is_pickaxe`、`minecraft:is_shears`、`minecraft:is_shovel`、`minecraft:is_spear`、`minecraft:is_sword`、`minecraft:is_tool`、`minecraft:is_trident` |
| 盔甲纹饰 | `minecraft:trimmable_armors`、`minecraft:trim_materials`、`minecraft:trim_templates` |
| 木质集合 | `minecraft:boat`、`minecraft:boats`、`minecraft:chest_boat`、`minecraft:crimson_stems`、`minecraft:door`、`minecraft:hanging_actor`、`minecraft:hanging_sign`、`minecraft:logs`、`minecraft:logs_that_burn`、`minecraft:mangrove_logs`、`minecraft:planks`、`minecraft:sign`、`minecraft:warped_stems`、`minecraft:wooden_slabs` |
| 杂项 | `minecraft:arrow`、`minecraft:banner`、`minecraft:coals`、`minecraft:egg`、`minecraft:is_fish`、`minecraft:lectern_books`、`minecraft:is_minecart`、`minecraft:music_disc`、`minecraft:sand`、`minecraft:soul_fire_base_blocks`、`minecraft:spawn_egg`、`minecraft:stone_bricks`、`minecraft:stone_crafting_materials`、`minecraft:stone_tool_materials`、`minecraft:vibration_damper`、`minecraft:wool`、`minecraft:bookshelf_books`、`minecraft:decorated_pot_sherds`、`minecraft:metal_nuggets` |

## 示例

```json title="items/example_item.json"
{
  "format_version": "1.20.20",
  "minecraft:item": {
    "description": {
      "identifier": "example:example_item",
      "menu_category": {
        "category": "items",
        "group": "itemGroup.name.misc"
      }
    },
    "components": {
      "minecraft:max_stack_size": 64,
      "minecraft:icon": {
        "texture": "example_item"
      },
      "minecraft:display_name": {
        "value": "item.example:example_item"
      }
    }
  }
}
```

## 原版示例清单

Microsoft Learn的物品清单页面列出了一组可查看JSON片段的原版物品示例，主要包括苹果、熟食、种子、鱼类、炖菜等食物与材料。该清单适合作为组件组合的参考示例，不应视为完整的物品注册表。

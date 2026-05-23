# 自定义盔甲

本篇将带你创建一套完整的自定义盔甲，包含四件套的物品定义、纹理映射、附着物定义以及套装效果。

## 盔甲纹理

基岩版盔甲纹理由两张PNG文件组成：

- `custom_1.png`：头盔、胸甲、靴子的纹理
- `custom_2.png`：护腿的纹理

将两张纹理文件放入`RP/textures/models/armor/`目录：

/// html | div.treeview
- {{file|RP}}
    - {{file|textures}}
        - {{file|models}}
            - {{file|armor}}
                - {{file|custom_1.png}}
                - {{file|custom_2.png}}
///

<!-- 截图：以原版钻石盔甲纹理为参考，展示 custom_1.png（128×64 或 64×32）的布局标注图 -->

## 物品定义

为四件盔甲分别创建物品JSON文件。以头盔为例：

```json title="BP/items/custom_helmet.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:custom_helmet",
            "menu_category": {
                "category": "equipment",
                "group": "minecraft:itemGroup.name.helmet"
            }
        },
        "components": {
            "minecraft:icon": "wiki:custom_helmet",
            "minecraft:max_stack_size": 1,
            "minecraft:wearable": {
                "slot": "slot.armor.head",
                "protection": 3
            },
            "minecraft:durability": {
                "max_durability": 364
            },
            "minecraft:enchantable": {
                "slot": "armor_head",
                "value": 10
            },
            "minecraft:repairable": {
                "repair_items": [
                    {
                        "items": ["minecraft:diamond"],
                        "repair_amount": "context.other->q.remaining_durability + 0.05 * context.other->q.max_durability"
                    }
                ]
            }
        }
    }
}
```

四件套的差异如下：

| 部件 | 标识符 | `slot` | `protection` | `max_durability` | 附魔`slot` | 菜单组 |
|------|--------|--------|--------------|------------------|-----------|--------|
| 头盔 | `wiki:custom_helmet` | `slot.armor.head` | 3 | 364 | `armor_head` | `minecraft:itemGroup.name.helmet` |
| 胸甲 | `wiki:custom_chestplate` | `slot.armor.chest` | 8 | 528 | `armor_torso` | `minecraft:itemGroup.name.chestplate` |
| 护腿 | `wiki:custom_leggings` | `slot.armor.legs` | 6 | 496 | `armor_legs` | `minecraft:itemGroup.name.leggings` |
| 靴子 | `wiki:custom_boots` | `slot.armor.feet` | 3 | 430 | `armor_feet` | `minecraft:itemGroup.name.boots` |

## 注册图标

```json title="RP/textures/item_texture.json"
{
    "texture_data": {
        "wiki:custom_helmet":     { "textures": "textures/items/custom_helmet" },
        "wiki:custom_chestplate": { "textures": "textures/items/custom_chestplate" },
        "wiki:custom_leggings":   { "textures": "textures/items/custom_leggings" },
        "wiki:custom_boots":      { "textures": "textures/items/custom_boots" }
    }
}
```

## 附着物定义

附着物（attachable）负责将盔甲纹理渲染到玩家身上。在资源包中为每件盔甲创建附着物JSON文件：

```json title="RP/attachables/custom_helmet.json"
{
    "format_version": "1.10.0",
    "minecraft:attachable": {
        "description": {
            "identifier": "wiki:custom_helmet",
            "materials": {
                "default": "armor",
                "enchanted": "armor_enchanted"
            },
            "textures": {
                "default": "textures/models/armor/custom_1",
                "enchanted": "textures/misc/enchanted_item_glint"
            },
            "geometry": {
                "default": "geometry.humanoid.armor.helmet"
            },
            "scripts": {
                "parent_setup": "v.chest_layer_visible = 0.0; v.head_layer_visible = 1.0; v.leg_layer_visible = 0.0; v.boot_layer_visible = 0.0; v.leg_layer_2_visible = 0.0;"
            },
            "render_controllers": ["controller.render.armor"]
        }
    }
}
```

护腿附着物使用`custom_2`纹理，且`parent_setup`将`leg_layer_visible`设为1.0，其他层设为0.0。四件的模板说明：

| 部件 | 几何体 | 纹理文件 | 可见层变量 |
|------|--------|----------|-----------|
| 头盔 | `geometry.humanoid.armor.helmet` | `custom_1` | `v.head_layer_visible = 1.0` |
| 胸甲 | `geometry.humanoid.armor.chestplate` | `custom_1` | `v.chest_layer_visible = 1.0` |
| 护腿 | `geometry.humanoid.armor.leggings` | `custom_2` | `v.leg_layer_visible = 1.0` |
| 靴子 | `geometry.humanoid.armor.boots` | `custom_1` | `v.boot_layer_visible = 1.0` |

其中护腿还需额外设置`v.leg_layer_2_visible = 1.0`。

## 显示名称

```lang title="RP/texts/zh_CN.lang"
item.wiki:custom_helmet=定制头盔
item.wiki:custom_chestplate=定制胸甲
item.wiki:custom_leggings=定制护腿
item.wiki:custom_boots=定制靴子
```

## 套装效果

基岩版没有原生套装效果API，但可以通过命令+刻检测实现：当玩家穿戴全套时，给予持续状态效果。

### 方法一：`tick.json`命令轮询

在行为包的`functions/`目录创建检测函数：

```mcfunction title="BP/functions/armor_set.mcfunction"
# 检测穿戴全套自定义盔甲，施加效果
effect @a[
    hasitem=[
        {item: wiki:custom_helmet,    slot: slot.armor.head},
        {item: wiki:custom_chestplate, slot: slot.armor.chest},
        {item: wiki:custom_leggings,   slot: slot.armor.legs},
        {item: wiki:custom_boots,      slot: slot.armor.feet}
    ]
] strength 2 0 true
```

```json title="BP/functions/tick.json"
{
    "values": ["armor_set"]
}
```

`tick.json`里的函数每刻执行一次，`duration 2`搭配每刻刷新，使效果持续不中断。

关于附着物更高级的用法（如在手持时显示3D模型），参见[物品附着物](item-attachables.md)。
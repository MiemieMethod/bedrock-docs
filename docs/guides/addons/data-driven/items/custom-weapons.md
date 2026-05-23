# 自定义武器

本篇将带你制作一把具有独特伤害、耐久、附魔属性的自定义近战武器——以剑为例，你可以举一反三制作任意近战武器。

## 物品定义

```json title="BP/items/my_sword.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:my_sword",
            "menu_category": {
                "category": "equipment",
                "group": "minecraft:itemGroup.name.sword"
            }
        },
        "components": {
            "minecraft:max_stack_size": 1,
            "minecraft:hand_equipped": true,
            "minecraft:damage": 10,
            "minecraft:durability": {
                "max_durability": 600
            },
            "minecraft:enchantable": {
                "slot": "sword",
                "value": 10
            },
            "minecraft:repairable": {
                "repair_items": [
                    {
                        "items": ["minecraft:stick"],
                        "repair_amount": "context.other->q.remaining_durability + 0.05 * context.other->q.max_durability"
                    }
                ]
            },
            "minecraft:icon": "wiki:my_sword"
        }
    }
}
```

各组件解析：

/// define
`minecraft:max_stack_size: 1`

- 武器通常不堆叠，设为1。

`minecraft:hand_equipped: true`

- 第三人称时以工具形式（横持/竖立）渲染，而非平放在手心。

`minecraft:damage: 10`

- 额外攻击伤害，在物品提示中显示为"+10 攻击伤害"。游戏基础攻击伤害为1，故实际伤害约为11。

`minecraft:durability.max_durability`

- 物品最大耐久值。每次攻击实体消耗2点耐久，归零后物品损坏。

`minecraft:enchantable`

- `slot: "sword"`表示可附加剑类魔咒（锋利、击退等），`value: 10`为附魔质量（铁武器标准值为14，钻石为10，金为22）。

`minecraft:repairable`

- 使用木棍在铁砧修复，修复量的Molang表达式：当前耐久 + 5%最大耐久。
///

## 注册图标

```json title="RP/textures/item_texture.json"
{
    "texture_data": {
        "wiki:my_sword": {
            "textures": "textures/items/my_sword"
        }
    }
}
```

将剑的图标PNG放在`RP/textures/items/my_sword.png`。

## 定义显示名称

```lang title="RP/texts/zh_CN.lang"
item.wiki:my_sword=魔法之剑
```

## 添加工具功能

通过`minecraft:digger`，可以让武器像特定工具一样快速破坏某些方块（例如让剑快速斩断蜘蛛网和竹子）：

```json title="components 中添加"
"minecraft:digger": {
    "use_efficiency": true,
    "destroy_speeds": [
        {
            "block": "minecraft:web",
            "speed": 15
        },
        {
            "block": "minecraft:bamboo",
            "speed": 10
        }
    ]
}
```

## 添加工具标签

通过`tag:`前缀组件，可为物品赋予工具类标签，让它具备特定工具的原版交互行为：

```json
"tag:minecraft:is_axe": {},
"tag:minecraft:is_sword": {}
```

/// note | 已知标签效果
- `minecraft:is_axe`：可以去除原木表皮（右键原木变木材）
- `minecraft:is_hoe`：可以耕地（右键泥土变耕地）
///

## 合成配方

```json title="BP/recipes/my_sword.json"
{
    "format_version": "1.26.10",
    "minecraft:recipe_shaped": {
        "description": {
            "identifier": "wiki:my_sword"
        },
        "tags": ["crafting_table"],
        "pattern": [
            "E",
            "E",
            "#"
        ],
        "key": {
            "#": { "item": "minecraft:stick" },
            "E": { "item": "minecraft:ender_eye" }
        },
        "result": {
            "item": "wiki:my_sword"
        },
        "unlock": [
            { "item": "minecraft:ender_eye" }
        ]
    }
}
```

## 脚本击中效果

如果想在击中实体时触发额外效果（如点燃、传送、额外伤害），可以使用`onHitEntity`自定义组件事件：

```js title="BP/scripts/sword_effects.js"
import { system } from "@minecraft/server";

const SwordFireComponent = {
    onHitEntity({ hitEntity, hadEffect }) {
        if (hadEffect && hitEntity.isValid()) {
            hitEntity.setOnFire(3);
        }
    },
};

system.beforeEvents.startup.subscribe(({ itemComponentRegistry }) => {
    itemComponentRegistry.registerCustomComponent(
        "wiki:sword_fire",
        SwordFireComponent
    );
});
```

```json title="BP/items/my_sword.json (components 中添加)"
"wiki:sword_fire": {}
```

关于脚本事件的完整说明，参见[物品事件](item-events.md)。关于耐久的详细管理方式，参见[物品耐久](item-durability.md)。
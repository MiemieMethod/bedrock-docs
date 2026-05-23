# 自定义食物

本篇教程将带你创建一种可以食用的自定义物品，并在食用后给予玩家状态效果——类似金苹果的效果系统。

## 物品定义

在行为包中创建物品JSON文件：

```json title="BP/items/magic_mushroom.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:magic_mushroom",
            "menu_category": {
                "category": "items",
                "group": "minecraft:itemGroup.name.miscFood"
            }
        },
        "components": {
            "minecraft:icon": "wiki:magic_mushroom",
            "minecraft:food": {
                "nutrition": 4,
                "saturation_modifier": 0.6
            },
            "minecraft:use_animation": "eat",
            "minecraft:use_modifiers": {
                "use_duration": 1.6,
                "movement_modifier": 0.35
            },
            "minecraft:tags": {
                "tags": [
                    "minecraft:is_food"
                ]
            },
            "wiki:food_effects": [
                { "name": "night_vision", "duration": 600, "amplifier": 0 },
                { "name": "speed",        "duration": 200, "amplifier": 1 }
            ]
        }
    }
}
```

`minecraft:food`组件让物品可以被食用，`minecraft:use_modifiers`控制食用所需时长与移动速度惩罚，`minecraft:use_animation`则控制进食动画：

/// define
`nutrition`

- 食用后恢复的饥饿值（半个饥饿鸡腿=1）。

`saturation_modifier`

- 饱和度修正值，实际恢复的饱和度 = `nutrition × saturation_modifier × 2`。

`can_always_eat`

- 是否在饥饿值满时也能食用，默认为`false`（但目前基岩版存在漏洞，自定义食物总是可以食用）。

`using_converts_to`

- 食用完成后将当前物品替换为指定物品标识符（例如碗食物食完后保留碗）。
///

## 注册图标

```json title="RP/textures/item_texture.json"
{
    "texture_data": {
        "wiki:magic_mushroom": {
            "textures": "textures/items/magic_mushroom"
        }
    }
}
```

## 脚本：食用时给予效果

自定义状态效果需要通过脚本组件实现。在行为包中创建脚本文件：

```js title="BP/scripts/food_effects.js"
import { system } from "@minecraft/server";

/**
 * 自定义组件：食用时给予效果列表
 * 参数格式: [{ name, duration, amplifier }]
 */
const ItemFoodEffectsComponent = {
    onConsume({ source }, { params }) {
        for (const { name, duration, amplifier } of params) {
            source.addEffect(name, duration, { amplifier });
        }
    },
};

system.beforeEvents.startup.subscribe(({ itemComponentRegistry }) => {
    itemComponentRegistry.registerCustomComponent(
        "wiki:food_effects",
        ItemFoodEffectsComponent
    );
});
```

在`manifest.json`的`modules`中引用脚本入口，并将此脚本文件加入入口模块（或通过入口文件`import`）。

`onConsume`事件在`use_duration`完成、物品真正被消耗时触发。`source`是食用物品的玩家，`params`是从JSON组件读取的参数——在这里就是效果数组。

## 定义显示名称

```lang title="RP/texts/zh_CN.lang"
item.wiki:magic_mushroom=魔法蘑菇
```

## 测试

在创意模式或通过命令`/give @s wiki:magic_mushroom`获取物品，然后按住使用键（右键/长按）食用，食用完成后即可观察到速度与夜视效果。

/// tip | 常见问题
如果食用后没有效果，请确认：
1. 行为包已启用脚本API（`manifest.json`的`modules`包含`type: "script"`的模块）
2. `@minecraft/server`版本不低于2.0.0
3. 自定义组件标识符在JSON与脚本中完全一致
///
# 物品附着物

**附着物**是资源包中的一种定义文件，用于在玩家或其他实体手持、穿戴某种物品或方块时，将一个自定义几何体与纹理渲染到该实体上。附着物是让自定义工具、武器与穿戴物显示为3D模型的核心技术。

根据最新版Microsoft Learn“Using Attachables”和Bedrock Wiki原文，当前仍有两种主流做法：

1. 通过**绑定（binding）**把模型绑定到装备槽位对应骨骼。这是原版最常使用、也更推荐的新项目做法。
2. 复制持有者骨架骨骼，并把自定义模型直接挂到目标骨骼。这种做法更适合只面向单一持有者模型的场景。

## 方法一：复制骨架并挂接骨骼

这种方法会把玩家或其他持有者的骨骼复制进附着物几何体，再把自定义模型挂到如`rightItem`之类的目标骨骼上。

### 几何体要求

使用Blockbench创建物品的3D模型几何体，确保：

1. 模型的轴心点（pivot）在骨骼的原点处
2. 模型几何体标识符与附着物定义中引用的标识符一致

导出到`RP/models/entity/my_tool.geo.json`。

### 附着物定义文件

```json title="RP/attachables/my_tool.entity.json"
{
    "format_version": "1.10.0",
    "minecraft:attachable": {
        "description": {
            "identifier": "wiki:my_tool",
            "materials": {
                "default": "entity_alphatest"
            },
            "textures": {
                "default": "textures/entity/my_tool"
            },
            "geometry": {
                "default": "geometry.my_tool"
            },
            "animations": {
                "hold_first_person": "animation.my_tool.hold_first_person",
                "hold_third_person": "animation.my_tool.hold_third_person"
            },
            "scripts": {
                "animate": [
                    { "hold_first_person": "context.is_first_person == 1.0" },
                    { "hold_third_person": "context.is_first_person == 0.0" }
                ]
            },
            "render_controllers": ["controller.render.item_default"]
        }
    }
}
```

附着物标识符通常需要与物品标识符一致，游戏据此确定哪种物品会触发该附着物。Microsoft Learn当前还记录了可选的`item`字段，用于在更复杂场景下单独指定关联物品或附加条件。

### 动画文件

创建动画文件，分别定义第一人称和第三人称时物品的位置、旋转与缩放：

```json title="RP/animations/my_tool.animation.json"
{
    "format_version": "1.8.0",
    "animations": {
        "animation.my_tool.hold_first_person": {
            "loop": true,
            "bones": {
                "my_tool_root": {
                    "rotation": [0, 45, 0],
                    "position": [0, 4, 0]
                }
            }
        },
        "animation.my_tool.hold_third_person": {
            "loop": true,
            "bones": {
                "my_tool_root": {
                    "rotation": [-45, 0, 0],
                    "position": [0, 10, 0]
                }
            }
        }
    }
}
```

## 方法二：使用`q.item_slot_to_bone_name`绑定骨骼

这是Microsoft Learn当前更推荐的新项目方案。该方法通过Molang查询函数自动将附着物绑定到对应槽位的骨骼，无需手动复制完整骨架，特别适用于多槽位或多持有者的通用附着物。

绑定通常写在几何体根骨骼的`binding`字段中：

```json title="RP/models/entity/my_tool.geo.json > bones[0]"
{
    "name": "my_tool_root",
    "binding": "q.item_slot_to_bone_name(context.item_slot)",
    "pivot": [0, 0, 0]
}
```

```json title="附着物 geometry 节"
"geometry": {
    "default": "geometry.my_tool_v2"
},
"scripts": {
    "pre_animation": [
        "v.target_bone = q.item_slot_to_bone_name('slot.weapon.mainhand');"
    ],
    "animate": [
        { "hold_main": "1.0" }
    ]
}
```

`q.item_slot_to_bone_name(slot)`会把当前装备槽位转换为标准骨骼名称，例如主手通常对应`rightItem`，副手通常对应`leftItem`。这使附着物不必为每个槽位硬编码不同骨骼名。

## 文件结构总览

/// html | div.treeview
- {{file|RP}}
    - {{file|attachables}}
        - {{file|my_tool.entity.json}}（附着物定义）
    - {{file|animations}}
        - {{file|my_tool.animation.json}}（附着物动画）
    - {{file|models}}
        - {{file|entity}}
            - {{file|my_tool.geo.json}}（附着物几何体）
    - {{file|textures}}
        - {{file|entity}}
            - {{file|my_tool.png}}（物品图标及模型纹理）
///

## 盔甲附着物

盔甲也是附着物的一种典型应用场景，但使用固定的原版几何体（`geometry.humanoid.armor.*`）而非自定义几何体。关于盔甲附着物的详细写法，参见[自定义盔甲](custom-armor.md)。

/// tip | 调试提示
第一人称持握位置调整需要多次试验。开启内容日志（帮助 > 开启内容日志）可以快速发现附着物定义中的JSON格式错误。
///
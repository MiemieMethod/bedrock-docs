# 物品附着物

**附着物**（attachable）是资源包中的一种定义文件，用于在玩家（或其他实体）手持或穿戴某种物品/方块时，将一个自定义几何体与纹理渲染到该实体上。附着物是让自定义工具、武器显示为3D模型的核心技术。

本篇介绍两种主要方法。

## 方法一：绑定至骨架骨骼

这是最通用的方法：将附着物几何体作为玩家骨架中某根骨骼的子级，从而跟随玩家的手部动画运动。

### 几何体要求

使用Blockbench创建物品的3D模型几何体，确保：

1. 模型的轴心点（pivot）在骨骼的原点处
2. 模型几何体标识符与附着物定义中引用的标识符一致

导出到`RP/models/items/my_tool.geo.json`。

### 附着物定义文件

```json title="RP/attachables/my_tool.json"
{
    "format_version": "1.10.0",
    "minecraft:attachable": {
        "description": {
            "identifier": "wiki:my_tool",
            "materials": {
                "default": "entity_alphatest"
            },
            "textures": {
                "default": "textures/items/my_tool"
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
                    { "hold_first_person": "c.is_first_person" },
                    { "hold_third_person": "!c.is_first_person" }
                ]
            },
            "render_controllers": ["controller.render.item_default"]
        }
    }
}
```

附着物标识符必须与物品标识符**完全一致**，游戏以此关联哪种物品触发哪个附着物。

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

此方法通过Molang查询函数自动将附着物绑定到对应槽位的骨骼，无需手动在玩家几何体中指定父级骨骼——特别适用于多槽位的通用附着物。

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

`q.item_slot_to_bone_name(slot)`返回该槽位对应的标准骨骼名称（如`rightItem`、`leftItem`等），使附着物无需硬编码骨骼名称。

## 文件结构总览

/// html | div.treeview
- {{file|RP}}
    - {{file|attachables}}
        - {{file|my_tool.json}}（附着物定义）
    - {{file|animations}}
        - {{file|my_tool.animation.json}}（附着物动画）
    - {{file|models}}
        - {{file|items}}
            - {{file|my_tool.geo.json}}（附着物几何体）
    - {{file|textures}}
        - {{file|items}}
            - {{file|my_tool.png}}（物品图标及模型纹理）
///

## 盔甲附着物

盔甲也是附着物的一种典型应用场景，但使用固定的原版几何体（`geometry.humanoid.armor.*`）而非自定义几何体。关于盔甲附着物的详细写法，参见[自定义盔甲](custom-armor.md)。

/// tip | 调试提示
第一人称持握位置调整需要多次试验。开启内容日志（帮助 > 开启内容日志）可以快速发现附着物定义中的JSON格式错误。
///
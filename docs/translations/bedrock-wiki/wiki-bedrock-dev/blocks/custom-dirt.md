---
标题: 自定义泥土
分类: 原版再创作
标签:
    - 实验性
    - 简单
提及:
    - Ivyman1992
    - Provedule
    - ThomasOrs
    - QuazChick
    - SmokeyStack
隐藏: true
---

:::tip 格式 & 最低引擎版本 `1.21.40`
本教程假设您对区块有良好的理解。
开始前请查看 [区块指南](/blocks/blocks-intro)、[区块状态](/blocks/block-states) 和 [区块排列](/blocks/block-permutations)。
:::

:::warning EXPERIMENTAL
需要启用 `Holiday Creator Features` 来触发区块事件，并使用区块标签 Molang 查询和 `minecraft:unit_cube` 区块组件。
:::

## 自定义泥土

下面是一个自定义泥土区块的示例。使用锄头可以将此自定义泥土转化为 `wiki:custom_farmland`，使用铲子可以转化为泥土小径。

:::tip
将 `minecraft:is_hoe` 或 `minecraft:is_shovel` 项标签添加到任何自定义工具中，以使它们能够与我们的自定义泥土配合使用！
:::

<Spoiler title="自定义泥土区块 JSON">

<CodeHeader>BP/blocks/custom_dirt.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:custom_dirt",
            "menu_category": {
                "category": "nature"
            }
        },
        "components": {
            "tag:dirt": {},
            "tag:fertilize_area": {},
            "minecraft:unit_cube": {},
            "minecraft:map_color": "#6C5746",
            "minecraft:destructible_by_mining": {
                "seconds_to_destroy": 0.6
            },
            "minecraft:material_instances": {
                "*": {
                    "texture": "custom_dirt"
                }
            },
            // Convert to farmland or dirt path when interacted with
            "minecraft:on_interact": {
                "event": "wiki:transform",
                "condition": "q.block_face && q.equipped_item_any_tag('slot.weapon.mainhand', 'minecraft:is_hoe', 'minecraft:is_shovel')"
            }
        },
        "events": {
            "wiki:transform": {
                "sequence": [
                    {
                        "damage": {
                            "type": "durability",
                            "amount": 1,
                            "target": "item"
                        }
                    },
                    // Transform into farmland (hoe is used)
                    {
                        "condition": "q.equipped_item_any_tag('slot.weapon.mainhand', 'minecraft:is_hoe')",
                        // Play use sound
                        "run_command": {
                            "command": "playsound use.gravel @a ~~~ 1 0.8"
                        },
                        // Replace this block with "wiki:custom_farmland"
                        "set_block": {
                            "block_type": "wiki:custom_farmland"
                        }
                    },
                    // Tranform into path (shovel is used)
                    {
                        "condition": "q.equipped_item_any_tag('slot.weapon.mainhand', 'minecraft:is_shovel')",
                        // Play use sound
                        "run_command": {
                            "command": "playsound use.grass @a ~~~ 1 0.8"
                        },
                        // Replace this block with Dirt Path
                        "set_block": {
                            "block_type": "minecraft:grass_path"
                        }
                    }
                ]
            }
        }
    }
}
```

</Spoiler>

## 自定义农田

农田是一个复杂的区块……它会对水做出反应（当附近有水时改变其纹理），如果水未及时到达，它会干涸并随机变回我们的泥土区块，并且支持在其上方种植作物。

尽管如此，它仅仅是特别的泥土。让我们来了解一下它的工作原理：

- 首先，您需要制作一个基础区块，就像我们的泥土一样。
- 为区块的顶部创建一个“农田”纹理（包括湿和干状态），然后为侧面分配泥土纹理。您还需要制作一个自定义的区块几何体，高度为16×15×16像素，比普通区块少一行。
- 之后，我们可以向区块添加湿度逻辑，以模拟原版功能。

<BButton
    link="https://github.com/Bedrock-OSS/wiki-addon/blob/main/ma-custom_crops/rp/models/blocks/farmland.geo.json"
    color=blue
>下载自定义农田几何体</BButton>

### 农田湿度

原版农田有8个湿度阶段：

- `0` - 显示干燥的顶部纹理，如果不靠近水源，则在随机刻点上衰变为泥土。
- `1-7` - 显示湿润的顶部纹理，如果不靠近水源，则在每个随机刻点后逐渐递减到`0`。
- 如果农田靠近水源，则在随机刻点上将湿度值设置为`7`。

在您的区块中添加一个湿度状态，以开始我们的自定义逻辑。

<CodeHeader>minecraft:block > description</CodeHeader>

```json
"states": {
    "wiki:moisture": {
        "values": { "min": 0, "max": 7 }
    }
}
```

以下排列在 `wiki:moisture` 值不为 `0` 时将顶部纹理设置为湿润。

<CodeHeader>minecraft:block</CodeHeader>

```json
"permutations": [
    {
        "condition": "q.block_state('wiki:moisture')",
        "components": {
            "minecraft:material_instances": {
                "*": {
                    "texture": "custom_dirt",
                    "render_method": "alpha_test"
                },
                "up": {
                    "texture": "custom_farmland_wet",
                    "render_method": "alpha_test"
                }
            }
        }
    }
]
```

### 水分管理

每个随机刻点，我们的农田应触发一个事件以确定区块当前的湿度状态。

<CodeHeader>minecraft:block</CodeHeader>

```json
"components": {
  ...
    "minecraft:random_ticking": {
        "on_tick": {
            "event": "wiki:set_moisture"
        }
    }
},
"events": {
    "wiki:set_moisture": {
        // If near water, sets `wiki:moisture` to `7`, else takes 1 away from current value to count down to `0` (dry).
        "set_block_state": {
            "wiki:moisture": "q.block_neighbor_has_any_tag(4,0,0,'water') || q.block_neighbor_has_any_tag(3,0,0,'water') || q.block_neighbor_has_any_tag(2,0,0,'water') || q.block_neighbor_has_any_tag(1,0,0,'water') || q.block_neighbor_has_any_tag(-1,0,0,'water') || q.block_neighbor_has_any_tag(-2,0,0,'water') || q.block_neighbor_has_any_tag(-3,0,0,'water') || q.block_neighbor_has_any_tag(-4,0,0,'water') || q.block_neighbor_has_any_tag(4,0,-4,'water') || q.block_neighbor_has_any_tag(3,0,-4,'water') || q.block_neighbor_has_any_tag(2,0,-4,'water') || q.block_neighbor_has_any_tag(1,0,-4,'water') || q.block_neighbor_has_any_tag(0,0,-4,'water') || q.block_neighbor_has_any_tag(-1,0,-4,'water') || q.block_neighbor_has_any_tag(-2,0,-4,'water') || q.block_neighbor_has_any_tag(-3,0,-4,'water') || q.block_neighbor_has_any_tag(-4,0,-4,'water') || q.block_neighbor_has_any_tag(4,0,-3,'water') || q.block_neighbor_has_any_tag(3,0,-3,'water') || q.block_neighbor_has_any_tag(2,0,-3,'water') || q.block_neighbor_has_any_tag(1,0,-3,'water') || q.block_neighbor_has_any_tag(0,0,-3,'water') || q.block_neighbor_has_any_tag(-1,0,-3,'water') || q.block_neighbor_has_any_tag(-2,0,-3,'water') || q.block_neighbor_has_any_tag(-3,0,-3,'water') || q.block_neighbor_has_any_tag(-4,0,-3,'water') || q.block_neighbor_has_any_tag(4,0,-2,'water') || q.block_neighbor_has_any_tag(3,0,-2,'water') || q.block_neighbor_has_any_tag(2,0,-2,'water') || q.block_neighbor_has_any_tag(1,0,-2,'water') || q.block_neighbor_has_any_tag(0,0,-2,'water') || q.block_neighbor_has_any_tag(-1,0,-2,'water') || q.block_neighbor_has_any_tag(-2,0,-2,'water') || q.block_neighbor_has_any_tag(-3,0,-2,'water') || q.block_neighbor_has_any_tag(-4,0,-2,'water') || q.block_neighbor_has_any_tag(4,0,-1,'water') || q.block_neighbor_has_any_tag(3,0,-1,'water') || q.block_neighbor_has_any_tag(2,0,-1,'water') || q.block_neighbor_has_any_tag(1,0,-1,'water') || q.block_neighbor_has_any_tag(0,0,-1,'water') || q.block_neighbor_has_any_tag(-1,0,-1,'water') || q.block_neighbor_has_any_tag(-2,0,-1,'water') || q.block_neighbor_has_any_tag(-3,0,-1,'water') || q.block_neighbor_has_any_tag(-4,0,-1,'water') || q.block_neighbor_has_any_tag(4,0,1,'water') || q.block_neighbor_has_any_tag(3,0,1,'water') || q.block_neighbor_has_any_tag(2,0,1,'water') || q.block_neighbor_has_any_tag(1,0,1,'water') || q.block_neighbor_has_any_tag(0,0,1,'water') || q.block_neighbor_has_any_tag(-1,0,1,'water') || q.block_neighbor_has_any_tag(-2,0,1,'water') || q.block_neighbor_has_any_tag(-3,0,1,'water') || q.block_neighbor_has_any_tag(-4,0,1,'water') || q.block_neighbor_has_any_tag(4,0,2,'water') || q.block_neighbor_has_any_tag(3,0,2,'water') || q.block_neighbor_has_any_tag(2,0,2,'water') || q.block_neighbor_has_any_tag(1,0,2,'water') || q.block_neighbor_has_any_tag(0,0,2,'water') || q.block_neighbor_has_any_tag(-1,0,2,'water') || q.block_neighbor_has_any_tag(-2,0,2,'water') || q.block_neighbor_has_any_tag(-3,0,2,'water') || q.block_neighbor_has_any_tag(-4,0,2,'water') || q.block_neighbor_has_any_tag(4,0,3,'water') || q.block_neighbor_has_any_tag(3,0,3,'water') || q.block_neighbor_has_any_tag(2,0,3,'water') || q.block_neighbor_has_any_tag(1,0,3,'water') || q.block_neighbor_has_any_tag(0,0,3,'water') || q.block_neighbor_has_any_tag(-1,0,3,'water') || q.block_neighbor_has_any_tag(-2,0,3,'water') || q.block_neighbor_has_any_tag(-3,0,3,'water') || q.block_neighbor_has_any_tag(-4,0,3,'water') || q.block_neighbor_has_any_tag(4,0,4,'water') || q.block_neighbor_has_any_tag(3,0,4,'water') || q.block_neighbor_has_any_tag(2,0,4,'water') || q.block_neighbor_has_any_tag(1,0,4,'water') || q.block_neighbor_has_any_tag(0,0,4,'water') || q.block_neighbor_has_any_tag(-1,0,4,'water') || q.block_neighbor_has_any_tag(-2,0,4,'water') || q.block_neighbor_has_any_tag(-3,0,4,'water') || q.block_neighbor_has_any_tag(-4,0,4,'water') ? 7 : q.block_state('wiki:moisture') ? q.block_state('wiki:moisture') - 1"
    },
    // Triggers the event which decays farmland into dirt if dry.
    "trigger": "wiki:try_decay"
},
"wiki:try_decay": {
    "sequence": [
        {
            "condition": "!q.block_state('wiki:moisture')",
            "trigger": "wiki:decay"
        }
    ]
},
// Tranform block into `wiki:custom_dirt` when dry or trampled.
"wiki:decay": {
    "set_block": {
        "block_type": "wiki:custom_dirt"
    }
}
```

这是我们农田区块的复杂部分，水的检测。在原版 Minecraft 中，如果水正位于所有区块的正中间，水可以在一个巨大的9x9方块范围内湿润农田。我们在这里为与农田区块相同的Y轴水平或高1的每个相对坐标复制了这种行为。例如，`q.block_neighbor_has_any_tag(-3,0,4,'water')` 表示如果我们的农田区块在东向3块，南向4块处有一个具有 `water` 标签的区块，则 `wiki:moisture` 状态将为 `7`。`||` 代表“或”，这意味着我们可以在这些相对坐标中的任何一个位置拥有一个水区块。

### 踩踏

如果我们的自定义农田被踩踏，它应该有机会衰变。

<CodeHeader>minecraft:block</CodeHeader>

```json
"components": {
    ...
    "minecraft:on_fall_on": {
        "min_fall_distance": 1,
        "event": "wiki:trample"
    }
},
"events": {
    ...
    // 50% chance for farmland to decay if trampled.
    "wiki:trample": {
        "randomize": [
            {
                "weight": 1
            },
            {
                "weight": 1,
                "trigger": "wiki:decay"
            }
        ]
    }
}
```

这里是完整的 `wiki:custom_farmland` JSON 供参考。

<Spoiler title="自定义农田区块 JSON">

<CodeHeader>BP/blocks/custom_farmland.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:custom_farmland",
            "menu_category": {
                "category": "nature"
            },
            "states": {
                "wiki:moisture": {
                    "values": { "min": 0, "max": 7 }
                }
            }
        },
        "components": {
            "minecraft:map_color": "#0A5E20",
            "minecraft:geometry": "geometry.farmland",
            "minecraft:light_dampening": 0,
            "minecraft:destructible_by_mining": {
                "seconds_to_destroy": 0.6
            },
            "minecraft:selection_box": {
                "origin": [-8, 0, -8],
                "size": [16, 15, 16]
            },
            "minecraft:collision_box": {
                "origin": [-8, 0, -8],
                "size": [16, 15, 16]
            },
            "minecraft:material_instances": {
                "*": {
                    "texture": "custom_dirt",
                    "render_method": "alpha_test"
                },
                "up": {
                    "texture": "custom_farmland",
                    "render_method": "alpha_test"
                }
            },
            "minecraft:random_ticking": {
                "on_tick": {
                    "event": "wiki:set_moisture"
                }
            },
            "minecraft:on_fall_on": {
                "min_fall_distance": 1,
                "event": "wiki:trample"
            }
        },
        "events": {
            "wiki:set_moisture": {
                "set_block_state": {
                    "wiki:moisture": "q.block_neighbor_has_any_tag(4,0,0,'water') || q.block_neighbor_has_any_tag(3,0,0,'water') || q.block_neighbor_has_any_tag(2,0,0,'water') || q.block_neighbor_has_any_tag(1,0,0,'water') || q.block_neighbor_has_any_tag(-1,0,0,'water') || q.block_neighbor_has_any_tag(-2,0,0,'water') || q.block_neighbor_has_any_tag(-3,0,0,'water') || q.block_neighbor_has_any_tag(-4,0,0,'water') || q.block_neighbor_has_any_tag(4,0,-4,'water') || q.block_neighbor_has_any_tag(3,0,-4,'water') || q.block_neighbor_has_any_tag(2,0,-4,'water') || q.block_neighbor_has_any_tag(1,0,-4,'water') || q.block_neighbor_has_any_tag(0,0,-4,'water') || q.block_neighbor_has_any_tag(-1,0,-4,'water') || q.block_neighbor_has_any_tag(-2,0,-4,'water') || q.block_neighbor_has_any_tag(-3,0,-4,'water') || q.block_neighbor_has_any_tag(-4,0,-4,'water') || q.block_neighbor_has_any_tag(4,0,-3,'water') || q.block_neighbor_has_any_tag(3,0,-3,'water') || q.block_neighbor_has_any_tag(2,0,-3,'water') || q.block_neighbor_has_any_tag(1,0,-3,'water') || q.block_neighbor_has_any_tag(0,0,-3,'water') || q.block_neighbor_has_any_tag(-1,0,-3,'water') || q.block_neighbor_has_any_tag(-2,0,-3,'water') || q.block_neighbor_has_any_tag(-3,0,-3,'water') || q.block_neighbor_has_any_tag(-4,0,-3,'water') || q.block_neighbor_has_any_tag(4,0,-2,'water') || q.block_neighbor_has_any_tag(3,0,-2,'water') || q.block_neighbor_has_any_tag(2,0,-2,'water') || q.block_neighbor_has_any_tag(1,0,-2,'water') || q.block_neighbor_has_any_tag(0,0,-2,'water') || q.block_neighbor_has_any_tag(-1,0,-2,'water') || q.block_neighbor_has_any_tag(-2,0,-2,'water') || q.block_neighbor_has_any_tag(-3,0,-2,'water') || q.block_neighbor_has_any_tag(-4,0,-2,'water') || q.block_neighbor_has_any_tag(4,0,-1,'water') || q.block_neighbor_has_any_tag(3,0,-1,'water') || q.block_neighbor_has_any_tag(2,0,-1,'water') || q.block_neighbor_has_any_tag(1,0,-1,'water') || q.block_neighbor_has_any_tag(0,0,-1,'water') || q.block_neighbor_has_any_tag(-1,0,-1,'water') || q.block_neighbor_has_any_tag(-2,0,-1,'water') || q.block_neighbor_has_any_tag(-3,0,-1,'water') || q.block_neighbor_has_any_tag(-4,0,-1,'water') || q.block_neighbor_has_any_tag(4,0,1,'water') || q.block_neighbor_has_any_tag(3,0,1,'water') || q.block_neighbor_has_any_tag(2,0,1,'water') || q.block_neighbor_has_any_tag(1,0,1,'water') || q.block_neighbor_has_any_tag(0,0,1,'water') || q.block_neighbor_has_any_tag(-1,0,1,'water') || q.block_neighbor_has_any_tag(-2,0,1,'water') || q.block_neighbor_has_any_tag(-3,0,1,'water') || q.block_neighbor_has_any_tag(-4,0,1,'water') || q.block_neighbor_has_any_tag(4,0,2,'water') || q.block_neighbor_has_any_tag(3,0,2,'water') || q.block_neighbor_has_any_tag(2,0,2,'water') || q.block_neighbor_has_any_tag(1,0,2,'water') || q.block_neighbor_has_any_tag(0,0,2,'water') || q.block_neighbor_has_any_tag(-1,0,2,'water') || q.block_neighbor_has_any_tag(-2,0,2,'water') || q.block_neighbor_has_any_tag(-3,0,2,'water') || q.block_neighbor_has_any_tag(-4,0,2,'water') || q.block_neighbor_has_any_tag(4,0,3,'water') || q.block_neighbor_has_any_tag(3,0,3,'water') || q.block_neighbor_has_any_tag(2,0,3,'water') || q.block_neighbor_has_any_tag(1,0,3,'water') || q.block_neighbor_has_any_tag(0,0,3,'water') || q.block_neighbor_has_any_tag(-1,0,3,'water') || q.block_neighbor_has_any_tag(-2,0,3,'water') || q.block_neighbor_has_any_tag(-3,0,3,'water') || q.block_neighbor_has_any_tag(-4,0,3,'water') || q.block_neighbor_has_any_tag(4,0,4,'water') || q.block_neighbor_has_any_tag(3,0,4,'water') || q.block_neighbor_has_any_tag(2,0,4,'water') || q.block_neighbor_has_any_tag(1,0,4,'water') || q.block_neighbor_has_any_tag(0,0,4,'water') || q.block_neighbor_has_any_tag(-1,0,4,'water') || q.block_neighbor_has_any_tag(-2,0,4,'water') || q.block_neighbor_has_any_tag(-3,0,4,'water') || q.block_neighbor_has_any_tag(-4,0,4,'water') ? 7 : q.block_state('wiki:moisture') ? q.block_state('wiki:moisture') - 1"
                },
                "trigger": "wiki:try_decay"
            },
            "wiki:trample": {
                "randomize": [
                    {
                        "weight": 1
                    },
                    {
                        "weight": 1,
                        "trigger": "wiki:decay"
                    }
                ]
            },
            "wiki:try_decay": {
                "sequence": [
                    {
                        "condition": "!q.block_state('wiki:moisture')",
                        "trigger": "wiki:decay"
                    }
                ]
            },
            "wiki:decay": {
                "set_block": {
                    "block_type": "wiki:custom_dirt"
                }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('wiki:moisture')",
                "components": {
                    "minecraft:material_instances": {
                        "*": {
                            "texture": "custom_dirt",
                            "render_method": "alpha_test"
                        },
                        "up": {
                            "texture": "custom_farmland_wet",
                            "render_method": "alpha_test"
                        }
                    }
                }
            }
        ]
    }
}
```

</Spoiler>
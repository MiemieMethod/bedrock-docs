---
title: NPC对话
category: 一般
tags:
    - 中级
mentions:
    - kyleplo
    - StuartDA
    - MedicalJewel105
    - SirLich
    - solvedDev
    - omuhu
    - Sprunkles137
    - ThomasOrs
    - QuazChick
---

非玩家角色（NPC）是类似村民的实体，可以为其设置对话，包括消息和多个按钮。它们最初是为冒险地图设计的，但随着`/dialogue`命令的引入，现在可以在普通附加包的上下文中使用。

## 对话文件

NPC对话数据存储在对话文件中，这些文件位于行为包根目录下的`dialogue`文件夹中。以下是一个基本的NPC对话文件：

```json title="dialogue/example.diag.json"
{
    "format_version": "1.17",
    "minecraft:npc_dialogue": {
        "scenes": [
            {
                "scene_tag": "example",
                "npc_name": "Steve",
                "text": "Hello"
            }
        ]
    }
}
```

在这个文件中，有一个场景数组。每个场景都是一个单独的对话。你可以将所有对话放在一个文件中，也可以将每个对话放在单独的文件中。每个场景对象内有多个属性可以设置，以控制对话：

#### scene_tag

场景的标识符，用于定位场景。

#### npc_name

NPC的显示名称。可选，如果未指定，将使用NPC实体的名称，默认值为`§eNPC`。

#### text

在对话气泡中显示的文本。可选。

#### on_open_commands

在对话打开时运行的命令字符串数组。可选。

```json title=""
"on_open_commands": [
  "/say Hello"
]
```

#### on_close_commands

在对话关闭时运行的命令字符串数组。可选。

```json title=""
"on_close_commands": [
  "/say Goodbye"
]
```

#### buttons

指定在对话中显示的按钮的对象数组。可选。

```json title=""
"buttons": [
    {
        "name": "按钮一",
        "commands": [
            "/say 按钮一被按下！"
        ]
    },
    {
        "name": "按钮二",
        "commands": [
            "/say 按钮二被按下！",
            "/say 按钮二的附加命令"
        ]
    }
]
```

## 选择玩家

在`on_open_commands`、`on_close_commands`和每个按钮对象的`commands`属性中，可以使用普通选择器，例如`@p`来选择最近的玩家。然而，这些选择器是相对于NPC实体运行的，因此在多人游戏中可能会造成困惑。为了解决这个问题，有一个特殊选择器`@initiator`，它始终选择打开对话的玩家。

```json title=""
"buttons": [
    {
        "name": "请施加漂浮效果",
        "commands": [
            "/effect @initiator levitation"
        ]
    }
]
```

这个选择器**仅**在NPC对话中有效，不能在其他地方使用。

## 翻译

所有将显示给用户的对话属性也可以被翻译：

```json title=""
"npc_name": {
    "rawtext": [
        {
            "translate": "entity.endermite.name"
        }
    ]
}
```

使用的翻译键应在资源包的语言文件中指定。在这种情况下，`entity.endermite.name`将翻译为“末影虫”。

## 打开对话

`/dialogue`命令用于打开和控制对话。该命令的格式如下：`/dialogue open <npc: target> <player: target> [sceneName:string]`

-   `<npc: target>`：指向任何具有`minecraft:npc`组件的实体的选择器，例如原版NPC。这决定了对话命令的执行位置，以及对话中NPC的外观。
-   `<player: target>`：指向将看到对话的玩家的选择器。
-   `[sceneName:string]`：与要显示的对话的`scene_tag`匹配的字符串。可选，如果不存在，将显示NPC最后显示的对话。

例如，以下命令将为最近的玩家打开对话`example`，使用最近的NPC：

```
/dialogue open @e[type=npc,c=1] @p example
```

## 更改对话

`/dialogue`命令也用于更改NPC的对话。与`/dialogue open`命令不同，此命令在玩家手动打开NPC对话之前没有效果。该语法如下：`/dialogue change <npc: target> <sceneName:string> [player: target]`

-   `<npc: target>`：指向要更改对话的NPC的选择器。
-   `<sceneName:string>`：与要显示的对话的`scene_tag`匹配的字符串。
-   `[player: target]`：指向将看到更新对话的玩家的选择器。可选，如果不存在，所有玩家将受到影响。

例如，以下命令将最近NPC的对话更改为`example`，适用于随机玩家。

```
/dialogue change @e[type=npc,c=1] example @r
```

## 完整示例

这个完整示例将创建一个自定义物品，当玩家右键单击/互动时可以传送。该示例的完整源代码可以在[Github](https://github.com/Llama-Studios/dialog-demo)上找到。对于这个演示，请使用页面顶部的清单文件。

### 创建NPC

即使NPC永远不可见，`/dialogue`命令始终需要一个NPC实体。为此，你需要生成NPC并将其放入一个计时区域，以便从任何地方都可以访问：

``` title="functions/setup.mcfunction"
tickingarea add 0 1 0 0 2 0
summon npc "§r" 0 1 0
```

此函数将在0, 0处创建一个计时区域，并在该计时区域的基岩层生成一个没有名称的NPC。你需要运行此函数一次，可以手动运行，或使用`player.json`或`tick.json`。

/// tip

你可以在玩家内部使用`/dialogue`命令触发NPC对话，而无需事先生成NPC。

1. 在玩家的行为中添加`minecraft:npc`组件。
2. 指定来自BP/dialogue文件夹的场景。
3. 从玩家运行`/dialogue`命令，提供`scene_tag`：

///

```
/dialogue open @s @s <scene_tag>
```

#### 优缺点：

-   `+` 如果你只是要运行使用`scene_tags`提供的NPC对话，则无需担心隐藏NPC。
-   `+` 没有NPC意味着你也不需要确保它在“计时区域”内。
-   `-` 由于对话是从玩家触发的，可能会在某些情况下变得不稳定。
-   `-` 其他玩家可以点击玩家，他们将看到此对话。

为避免这种情况，可以将`minecraft:interaction`添加到实体中，这将替代NPC交互。NPC的功能仍然有效，但如果玩家点击另一个玩家，则不会弹出NPC。

```json title=""
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        }
                    ]
                }
            }
        }
    ]
}
```

### 对话文件

此对话文件包含两个对话，每个对话都有两个传送按钮和一个切换按钮。

```json title="dialogue/example.diag.json"
{
    "format_version": "1.17",
    "minecraft:npc_dialogue": {
        "scenes": [
            {
                "scene_tag": "main_teleport_menu",
                "npc_name": "传送",
                "text": "你想传送到哪里？",
                "buttons": [
                    {
                        "name": "区域",
                        "commands": [
                            "/dialogue open @e[type=npc,c=1] @initiator districts_teleport_menu"
                        ]
                    },
                    {
                        "name": "我的基地",
                        "commands": ["/tp @initiator -20 4 -20"]
                    },
                    {
                        "name": "世界重生点",
                        "commands": ["/tp @initiator 0 4 0"]
                    }
                ]
            },
            {
                "scene_tag": "districts_teleport_menu",
                "npc_name": "区域传送",
                "text": "你想传送到哪个区域？",
                "buttons": [
                    {
                        "name": "< 返回",
                        "commands": [
                            "/dialogue open @e[type=npc,c=1] @initiator main_teleport_menu"
                        ]
                    },
                    {
                        "name": "商店区",
                        "commands": ["/tp @initiator 20 4 20"]
                    },
                    {
                        "name": "游戏区",
                        "commands": ["/tp @initiator 20 4 -20"]
                    }
                ]
            }
        ]
    }
}
```

### 创建物品

最后，创建一个物品，当右键单击/互动时将打开对话。该物品使用末影珍珠的纹理，但你可以给它自定义纹理。

#### 物品JSON

```json title="BP/items/teleport_menu.json"
{
    "format_version": "1.21.40",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:teleport_menu",
            "menu_category": {
                "category": "items"
            }
        },
        "components": {
            "minecraft:icon": "ender_pearl",
            "minecraft:glint": true,
            "minecraft:display_name": {
                "value": "传送菜单"
            },
            "minecraft:custom_components": ["wiki:teleport_menu"]
        }
    }
}
```

#### 自定义组件脚本

```js title="BP/scripts/teleportMenu.js"
import { world } from "@minecraft/server";

const TeleportMenuItemComponent = {
    onUse({ source }) {
        source.runCommand("dialogue open @e[type=npc, c=1] @s main_teleport_menu");
    },
};

world.beforeEvents.worldInitialize.subscribe(({ itemComponentRegistry }) => {
    itemComponentRegistry.registerCustomComponent("wiki:teleport_menu", TeleportMenuItemComponent);
});
```

### 测试

完成后，将这些文件与清单一起打包，并导入到Minecraft中。创建一个新的平坦世界，并确保启用作弊和实验。

进入世界后，使用`/function setup`创建计时区域和NPC实体。然后使用`/give @s wiki:teleport_menu`给予自己传送物品。切换到生存模式（NPC对话在创造模式下无效），持有该物品并右键单击。你应该会看到你的对话出现。

## 版权

本教程基于Minecraft创作者文档中的[此页面](https://learn.microsoft.com/minecraft/creator/documents/npcdialogue)。
# NPC对话进阶

NPC（非玩家角色）原本是为冒险地图设计的对话实体，但随着`/dialogue`命令的引入，它在普通附加包中也越来越有用。本文介绍如何通过对话文件和脚本API实现完整的NPC对话系统。

关于NPC的概念介绍，请参考[NPC对话](../../../docs/addon/dialogue.md)文档页。

## 对话文件结构

NPC对话数据存储在行为包根目录下的`dialogue`文件夹中：

```json title="BP/dialogue/example.json"
{
    "format_version": "1.17",
    "minecraft:npc_dialogue": {
        "scenes": [
            {
                "scene_tag": "wiki:example",
                "npc_name": "Steve",
                "text": "你好！"
            }
        ]
    }
}
```

一个文件可以包含多个场景，也可以将每个场景单独放在一个文件中。场景属性如下：

| 属性 | 必须 | 说明 |
|---|---|---|
| `scene_tag` | ✓ | 场景的唯一标识符，用于命令中指定 |
| `npc_name` | 否 | NPC显示名称；不指定则使用实体名称（默认为`§eNPC`）；支持原始文本格式 |
| `text` | 否 | 气泡中显示的文字；支持原始文本格式 |
| `on_open_commands` | 否 | 对话打开时执行的命令数组 |
| `on_close_commands` | 否 | 对话关闭时执行的命令数组 |
| `buttons` | 否 | 按钮列表 |

### 按钮配置

```json
"buttons": [
    {
        "name": "按钮一",
        "commands": [
            "/say 按钮一被按下了！"
        ]
    },
    {
        "name": "按钮二",
        "commands": [
            "/say 按钮二被按下了！",
            "/say 可以执行多条命令"
        ]
    }
]
```

### `@initiator`选择器

在`on_open_commands`、`on_close_commands`和按钮的`commands`中，有一个特殊的选择器`@initiator`，它始终指向打开了当前对话的那个玩家。在多人游戏中这比`@p`更准确：

```json
"buttons": [
    {
        "name": "给我缓降",
        "commands": [
            "/effect @initiator levitation"
        ]
    }
]
```

/// warning | 注意
`@initiator`只在NPC对话的命令中有效，不能在其他地方使用。
///

### 本地化支持

所有显示文字字段都支持原始文本格式，可以引用语言文件中的翻译键：

```json
"npc_name": {
    "rawtext": [
        { "translate": "entity.wiki.guide.name" }
    ]
}
```

## 控制对话的命令

### /dialogue open

打开对话界面：
```
/dialogue open <npc选择器> <玩家选择器> [场景标签]
```

例如让最近的NPC向最近的玩家展示`wiki:example`场景：
```
/dialogue open @e[type=npc,c=1] @p wiki:example
```

### /dialogue change

切换NPC下次被点击时展示的场景：
```
/dialogue change <npc选择器> <场景标签> [玩家选择器]
```

## 准备NPC实体

`/dialogue open`命令需要一个拥有`minecraft:npc`组件的实体。可以使用原版NPC，也可以在自定义实体上添加该组件。

### 方案一：召唤原版NPC

将NPC召唤在一个常加载区域中，使其始终可被选择器访问：

```mcfunction title="BP/functions/setup.mcfunction"
tickingarea add 0 1 0 0 2 0
summon npc "§r" 0 1 0
```

/// tip | 隐藏NPC
可以将NPC传送到地下或地图中不可见的位置，让玩家看不到它，但命令依然能正常引用它。
///

### 方案二：玩家作为NPC

给玩家添加`minecraft:npc`组件，直接用玩家触发对话：

```
/dialogue open @s @s wiki:example
```

**优点**：无需召唤NPC实体，无需常加载区域。

**缺点**：不稳定，可能在某些情况下出现问题；其他玩家点击玩家时也会看到对话。

若要避免其他玩家误触发，在玩家实体中添加：

```json title="BP/entities/player.json > components"
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        { "test": "is_family", "subject": "other", "value": "player" }
                    ]
                }
            }
        }
    ]
}
```

## 完整示例：传送菜单物品

这个示例演示如何用自定义物品打开一个多级传送菜单，结合对话文件和脚本API自定义物品组件。

### 准备工作

运行`/function wiki:setup`初始化常加载区域和NPC实体（如使用方案一）。

### 对话文件

```json title="BP/dialogue/teleport.json"
{
    "format_version": "1.17",
    "minecraft:npc_dialogue": {
        "scenes": [
            {
                "scene_tag": "wiki:main_teleport_menu",
                "npc_name": "传送",
                "text": "你想去哪里？",
                "buttons": [
                    {
                        "name": "分区",
                        "commands": [
                            "/dialogue open @e[type=npc,c=1] @initiator wiki:districts_menu"
                        ]
                    },
                    {
                        "name": "我的基地",
                        "commands": ["/tp @initiator -20 4 -20"]
                    },
                    {
                        "name": "世界出生点",
                        "commands": ["/tp @initiator 0 4 0"]
                    }
                ]
            },
            {
                "scene_tag": "wiki:districts_menu",
                "npc_name": "分区传送",
                "text": "选择目标分区：",
                "buttons": [
                    {
                        "name": "< 返回",
                        "commands": [
                            "/dialogue open @e[type=npc,c=1] @initiator wiki:main_teleport_menu"
                        ]
                    },
                    {
                        "name": "商业区",
                        "commands": ["/tp @initiator 20 4 20"]
                    },
                    {
                        "name": "娱乐区",
                        "commands": ["/tp @initiator 20 4 -20"]
                    }
                ]
            }
        ]
    }
}
```

### 物品定义

```json title="BP/items/teleport_menu.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:teleport_menu",
            "menu_category": { "category": "items" }
        },
        "components": {
            "minecraft:icon": "ender_pearl",
            "minecraft:glint": true,
            "minecraft:display_name": { "value": "传送菜单" },
            "wiki:teleport_menu": {}
        }
    }
}
```

### 脚本API（物品自定义组件）

```js title="BP/scripts/teleportMenu.js"
import { system } from "@minecraft/server";

const ItemTeleportMenuComponent = {
    onUse({ source }) {
        source.runCommand("dialogue open @e[type=npc,c=1] @s wiki:main_teleport_menu");
    }
};

system.beforeEvents.startup.subscribe(({ itemComponentRegistry }) => {
    itemComponentRegistry.registerCustomComponent("wiki:teleport_menu", ItemTeleportMenuComponent);
});
```

### 测试

1. 创建启用作弊和实验性功能的平坦世界
2. 运行`/function wiki:setup`（如使用方案一）
3. 运行`/give @s wiki:teleport_menu`
4. 切换到生存模式（NPC对话在创造模式下不工作）
5. 手持物品并右键点击，查看传送菜单

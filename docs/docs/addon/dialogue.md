# NPC对话

**NPC对话（NPC Dialogue）**是Minecraft基岩版行为包中用于创建非玩家角色交互式对话的系统。NPC对话允许为NPC实体定义多幕对话内容、按钮选项和命令动作。

## 概述

NPC是基岩版中一种特殊的实体类型（`minecraft:npc`），常用于冒险地图和教育场景中为玩家提供信息或引导。NPC对话系统扩展了NPC的交互能力，允许通过行为包中的JSON文件定义复杂的多步对话流程。

NPC对话定义文件位于行为包的`dialogue/`目录中。

## 基本结构

NPC对话文件定义一系列**场景（Scene）**，每个场景对应一幕对话内容：

```json title="NPC对话定义示例"
{
  "format_version": "1.17.0",
  "minecraft:npc_dialogue": {
    "scenes": [
      {
        "scene_tag": "greeting",
        "npc_name": "向导",
        "text": "你好，旅行者！欢迎来到这片土地。你需要什么帮助吗？",
        "buttons": [
          {
            "name": "告诉我更多",
            "commands": ["/dialogue open @s @initiator greeting_detail"]
          },
          {
            "name": "再见",
            "commands": []
          }
        ]
      }
    ]
  }
}
```

## 场景

每个场景包含以下字段：

/// define
`scene_tag`

- 场景的唯一标签标识符，用于通过`/dialogue`命令引用此场景。

`npc_name`

- NPC在此场景中显示的名称。可以使用原始文本格式。

`text`

- 对话文本内容。支持原始文本格式和换行符。

`buttons`

- 对话界面中显示的按钮列表，每个按钮包含名称和点击后执行的命令列表。最多可定义6个按钮。

`on_open_commands`

- 场景打开时自动执行的命令列表。

`on_close_commands`

- 场景关闭时自动执行的命令列表。

///

## 对话命令

NPC对话系统通过`/dialogue`命令进行控制：

| 命令 | 功能 |
|------|------|
| `/dialogue open` | 为指定玩家强制打开指定NPC的对话框，可选指定场景 |
| `/dialogue change` | 更改指定NPC在下次交互时所使用的场景 |

## @initiator选择器

NPC对话系统引入了`@initiator`目标选择器，用于在对话按钮命令中引用发起对话的玩家。`@initiator`仅在NPC对话的命令上下文中有效。

## NPC对话与实体

NPC实体通过在其行为定义中配置对应的对话场景标签来关联对话内容。当玩家与NPC交互时，游戏打开该NPC关联的对话场景。一个NPC可以关联多个场景，通过命令或事件在不同场景之间切换，实现多步骤对话流程。
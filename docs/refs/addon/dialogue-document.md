# 对话定义

本页列出国际版行为包NPC对话定义文件的主要结构。NPC对话定义文件存放于行为包的`dialogue/`目录，根键为`minecraft:npc_dialogue`。

## 对话文件

| 字段 | 类型 | 说明 |
|---|---|---|
| `format_version` | 字符串 | 声明定义文件使用的数据格式版本。应使用`1.20.80`或更高版本。 |
| `minecraft:npc_dialogue` | 对象 | NPC对话定义根对象，包含场景定义。 |

## `minecraft:npc_dialogue`

| 字段 | 类型 | 说明 |
|---|---|---|
| `scenes` | 数组 | 对话场景定义数组。每个对话场景代表NPC的一幕对话交互。 |

## 场景对象

每个场景对象定义对话的一个状态，包含以下字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `scene_tag` | 字符串 | 场景的唯一标识符，用于通过`/dialogue`命令引用此场景。 |
| `npc_name` | 字符串 | NPC在此场景中显示的名称。支持原始文本（Raw Text）格式。 |
| `text` | 字符串 | 对话文本内容。支持原始文本格式。 |
| `buttons` | 数组 | 对话界面中显示的按钮列表。每个按钮包含名称和执行命令。最多可定义6个按钮。 |
| `on_open_commands` | 数组 | 场景打开时自动执行的命令列表。 |
| `on_close_commands` | 数组 | 场景关闭时自动执行的命令列表。 |

## 按钮对象

每个按钮对象定义对话界面中的一个可交互按钮，包含以下字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| `name` | 字符串 | 按钮显示的文本。 |
| `commands` | 数组 | 玩家点击该按钮时执行的命令列表。 |

## 结构示例

```json title="NPC对话定义示例"
{
  "format_version": "1.20.80",
  "minecraft:npc_dialogue": {
    "scenes": [
      {
        "scene_tag": "greeting",
        "npc_name": "向导",
        "text": "你好，旅行者！",
        "buttons": [
          {
            "name": "了解更多",
            "commands": ["/dialogue change @s greeting_detail"]
          },
          {
            "name": "再见",
            "commands": ["/dialogue close @initiator"]
          }
        ]
      },
      {
        "scene_tag": "greeting_detail",
        "npc_name": "向导",
        "text": "欢迎来到这片土地。",
        "buttons": [
          {
            "name": "返回",
            "commands": ["/dialogue change @s greeting"]
          }
        ]
      }
    ]
  }
}
```

## 相关参考

- [NPC对话](../../docs/addon/dialogue.md)
- [NPC](../../docs/general/entity.md)
- [命令](../../docs/general/command.md)
- [原始文本](../../docs/general/raw-text.md)
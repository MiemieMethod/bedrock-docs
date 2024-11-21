---
title: 实体命令
nav_order: 2
tags:
  - 中级
description: 从实体触发斜杠命令。
---

/// details-info | 署名信息
- 该页面翻译自[https://wiki.bedrock.dev/animation-controllers/entity-commands.html](https://wiki.bedrock.dev/animation-controllers/entity-commands.html)
- 该页面仓库地址为[https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/animation-controllers/entity-commands.md](https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/animation-controllers/entity-commands.md)
- 该页面的版本为<!-- md:samp Bedrock-OSS/bedrock-wiki@dded66a13b7daa57de21c828ddae2fc8429a35a9 -->
- 该页面的作者有：
    - <!-- md:samp @SirLich -->
    - <!-- md:samp @solvedDev -->
    - <!-- md:samp @Joelant05 -->
    - <!-- md:samp @destruc7i0n -->
    - <!-- md:samp @Dreamedc2015 -->
    - <!-- md:samp @MedicalJewel105 -->
    - <!-- md:samp @aexer0e -->
    - <!-- md:samp @cda94581 -->
    - <!-- md:samp @ThijsHankelMC -->
    - <!-- md:samp @QuazChick -->
///

/// tip | 事件响应
运行实体命令的一个更简单的方法是通过`queue_command`实体事件响应。
///

## 动画控制器

为了触发斜杠命令，我们将使用行为包动画控制器。动画控制器应放置在`animation_controllers/some_controller.json`。你可以在[bedrock.dev的实体事件部分了解更多关于动画控制器的信息](https://bedrock.dev/docs/stable/Entity%20Events)。

简而言之，动画控制器允许我们从行为包触发事件。

-   斜杠命令（如`/say`）
-   Molang（`v.foo += 1;`）
-   实体事件（例如`@s wiki:my_event`）

以下是一个示例动画控制器：

```json title="BP/animation_controllers/entity_commands.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.sirlich_entity_commands": {
      "states": {
        "default": {
          "transitions": [
            {
              "on_summon": "1" //1评估为true
            }
          ]
        },
        "on_summon": {
          "on_entry": ["/say 我被召唤了"]
        }
      }
    }
  }
}
```

此动画控制器将在实体被召唤到世界中时立即运行命令`/say 我被召唤了`。如果你对这个工作原理感到困惑，请查看Molang、动画和实体事件。

简而言之，有`states`，可以在其`on_entry`子句中触发事件。我们使用查询在不同状态之间转移。默认情况下，实体将处于`default`状态，除非定义了`initial_state`值。

/// warning
查询在世界/区块重新加载时会重新运行。这意味着`"/say 我被召唤了"`这行实际上会在每次实体“加载”时运行，而不仅仅是在被召唤时。
///

如果你需要阻止这种情况发生，你需要添加额外的查询，例如`skin_id`查询。第一次实体生成时，检查`skin_id = 0`，然后*同时也*添加一些更高的`skin_id`到实体上，例如`skin_id = 1`。这样，当实体重新加载时，它将无法运行这些命令。文档后面会进一步说明这一点。

## 使用动画控制器

要将此动画控制器添加到我们的实体中，我们可以在实体定义描述中使用以下代码：

```json title="BP/entities/entity_commands.se.json"
"description": {
  "identifier": "wiki:entity_commands",
  "scripts": {
    "animate": [
      "wiki:entity_commands"
    ]
  },
  "animations": {
    "wiki:entity_commands": "controller.animation.wiki_entity_commands"
  }
}
```

如果你对这个步骤感到困惑，请查看[实体事件文档](https://bedrock.dev/r/Entity%20Events)。

## 使用事件触发命令：

动画转移是使用查询创建的。你可以在[这里](https://bedrock.dev/docs/stable/MoLang#List%20of%20Entity%20Queries)阅读关于查询的内容。在我们的第一个示例中，我们的查询只是`true`，这意味着命令会自动运行。我们可以使用更复杂的查询来创建更有趣的效果。一个非常方便的方法是使用组件作为Molang过滤器来触发命令。

我个人喜欢使用[skin_id](https://docs.microsoft.com/en-us/minecraft/creator/reference/content/entityreference/examples/entityproperties/minecraftproperty_skin_id)。

我们可以更新我们的动画控制器以基于`skin_id`触发：

```json title="BP/animation_controllers/entity_commands.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.sirlich_entity_commands": {
      "states": {
        "default": {
          "transitions": [
            {
              "command_example": "q.skin_id == 1"
            },
            {
              "zombies": "q.skin_id == 2"
            }
          ]
        },
        "command_example": {
          "transitions": [
            {
              "default": "q.skin_id != 1"
            }
          ],
          "on_entry": ["/say 命令一！", "@s execute_no_commands"]
        },
        "zombies": {
          "transitions": [
            {
              "default": "q.skin_id != 2"
            }
          ],
          "on_entry": [
            "/say 啊！到处都是僵尸！",
            "/summon minecraft:zombie",
            "/summon minecraft:zombie",
            "/summon minecraft:zombie",
            "/summon minecraft:zombie",
            "@s execute_no_commands"
          ]
        }
      }
    }
  }
}
```

此动画控制器现在有两个命令状态：第一个由`skin_id = 1`触发，第二个由`skin_id = 2`触发。注意使用了`==`和`!=`。`==`用于测试相等，不要使用单个`=`。`!`表示不，因此`!=`用于确保不等于特定值。此外，请注意我在每个命令列表的末尾添加了`@s execute_no_commands`语法。我们稍后将创建`execute_no_commands`，它将允许我们将`skin_id`重置为0，并重新使用我们的命令。

语法是`@s`后跟实体事件的名称。这允许我们在动画控制器内添加/移除组件。

## 设置组件组

回到我们的实体文件中，我们可以使用`skin_id`组件设置`skin_id`。

`skin_id`组件如下所示：

```json title=""
"minecraft:skin_id": {
  "value": 1
}
```

我们可以添加包含skin_ids的组件组：

```json title="BP/entities/entity_commands.se.json"
"component_groups": {
  "execute_no_commands": {
    "minecraft:skin_id": {
      "value": 0
    }
  },
  "command_example": {
    "minecraft:skin_id": {
      "value": 1
    }
  },
  "command_zombies": {
    "minecraft:skin_id": {
      "value": 2
    }
  }
}
```

## 添加事件

现在让我们创建事件，以便我们可以轻松添加这些组：

```json title="BP/entities/entity_commands.se.json"
"events": {
  "minecraft:entity_spawned": {
    "add": {
      "component_groups": [
        "execute_no_commands"
      ]
    }
  },
  "execute_no_commands": {
    "add": {
      "component_groups": [
        "execute_no_commands"
      ]
    }
  },
  "command_example": {
    "add": {
      "component_groups": [
        "command_example"
      ]
    }
  },
  "command_zombies": {
    "add": {
      "component_groups": [
        "command_zombies"
      ]
    }
  }
}
```

## 触发事件

在Minecraft中有很多方法可以触发事件。如前所述，你可以使用动画控制器触发事件。此外，让我们看两个具体示例：

### 互动组件：

此组件将在你点击他时生成僵尸。

```json title="BP/entities/entity_commands.se.json"
"minecraft:interact": {
  "interactions": [{
    "on_interact": {
      "filters": {
        "all_of": [{
            "test": "is_family",
            "subject": "other",
            "value": "player"
          }
        ]
      },
      "event": "command_zombies"
    }
  }]
}
```

### 计时器

此组件将每10秒触发示例命令：

```json title="BP/entities/entity_commands.se.json"
"minecraft:timer": {
  "looping": true,
  "time": 10,
  "time_down_event": {
    "event": "example_command"
  }
}
```

通过将这些（和类似的！）组件添加到我们的实体中，我们可以控制`skin_id`何时更改，从而控制哪些事件运行。

## 回顾：

以下是它的工作原理：

-   使用互动或计时器等组件运行`example_command`。
-   这将添加`example_command`组件组。
-   这将添加`skin_id`组件。
-   这将设置实体的`skin_id`，可以在动画控制器中查询。
-   动画控制器注意到这个`skin_id`，并转移到`example_command`状态。
-   动画控制器运行`/say`命令。
-   动画控制器运行实体事件`@s execute_no_command`。
-   `execute_no_command`事件将`skin_id`设置为0。
-   动画控制器看到这一点，并转移回默认状态。
-   现在动画控制器等待新的`skin_id`。

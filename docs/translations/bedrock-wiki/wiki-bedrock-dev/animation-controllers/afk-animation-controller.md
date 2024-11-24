---
title: AFK检测器
description: 当玩家处于AFK状态时运行命令。
---

/// details-info | 署名信息
- 该页面翻译自[https://wiki.bedrock.dev/animation-controllers/afk-animation-controller.html](https://wiki.bedrock.dev/animation-controllers/afk-animation-controller.html)
- 该页面仓库地址为[https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/animation-controllers/afk-animation-controller.md](https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/animation-controllers/afk-animation-controller.md)
- 该页面的版本为<!-- md:samp Bedrock-OSS/bedrock-wiki@6e3dce1648e897cff9141561e8fa8a5a1befec04 -->
- 该页面的作者有：
    - <!-- md:samp @SirLich -->
    - <!-- md:samp @BlueFrog130 -->
    - <!-- md:samp @SmokeyStack -->
    - <!-- md:samp @Keyyard -->
    - <!-- md:samp @Ultr4Anubis -->
///

### AFK检测器动画控制器

[了解更多关于动画控制器的信息](./animation-controllers-intro.md){ .md-button }

以下是一个可以用来跟踪AFK玩家示例。

```json title="BP/animation_controllers/afk.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.player.afk": {
      "states": {
        "default": {
          "transitions": [
            {
              "stands_still": "!q.is_moving"
            }
          ]
        },
        "stands_still": {
          "on_entry": ["v.afk = q.life_time;"],
          "transitions": [
            {
              "afk": "(q.life_time - v.afk) >= 30 && !q.is_moving"
            },
            {
              "default": "q.is_moving"
            }
          ]
        },
        "afk": {
          "on_entry": ["/tag @s add AFK", "/say 我现在处于 AFK 状态"],
          "animations": ["afk_animation"],
          "transitions": [
            {
              "default": "q.is_moving"
            }
          ],
          "on_exit": ["/tag @s remove AFK", "/say 我不再 AFK"]
        }
      }
    }
  }
}
```

-   `controller.animation.player.afk`当然是标识符。
-   如果[Molang](https://bedrock.dev/r/MoLang)查询`!q.is_moving`返回`false`（玩家没有移动），状态将转移到`stands_still`状态。
-   `stands_still`状态检查玩家在30秒内是否没有移动，如果没有则转移到`afk`，否则返回`default`。
-   当进入`afk`状态时，`on_entry`被触发，将运行以下斜杠命令。
-   `animations`包含在状态激活期间要运行的行为动画的短名称，类似于[资源动画控制器](#animation-controller)。
-   如果玩家再次移动，状态将再次转移到`default`。
    `on_exit`中的命令将被执行。

*[AFK]: Away From Keyboard
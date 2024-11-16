---
title: 重生命令
mentions:
    - SirLich
    - solvedDev
    - Joelant05
    - BlueFrog130
    - SmokeyStack
    - MedicalJewel105
    - cda94581
description: 实体重生时运行命令。
---

<Button link="animation-controllers-intro">了解更多关于动画控制器的信息</Button>

此动画控制器可用于在玩家重生时运行命令，例如重新添加药水效果或给予物品。

只需将以下动画控制器添加到 `player.json` 中，你就完成了！

<CodeHeader>BP/animation_controllers/respawn.ac.json</CodeHeader>

```json
{
    "format_version": "1.10.0",
    "animation_controllers": {
        "controller.animation.death": {
            "initial_state": "initialization",
            "states": {
                "initialization": {
                    "transitions": [
                        {
                            "has_died": "!q.is_alive"
                        }
                    ],
                    "on_exit": ["v.delay = 0.2 + q.life_time;", "/<死亡命令或动画>"]
                },
                "has_died": {
                    "on_exit": ["/<重生命令或动画>"],
                    "transitions": [
                        {
                            "initialization": "q.is_alive && (q.life_time >= v.delay)"
                        }
                    ]
                }
            }
        }
    }
}
```
# 输入键

**输入键（Input Key）**是基岩版用于显示玩家当前输入方式的文本占位符。输入键会根据玩家当前的控制方案自动替换成对应按键、手柄按钮或触摸图标，因此常用于操作提示、引导文本和界面说明。

## 概述

输入键通常写在语言文件中，再由游戏在显示时替换为具体图标或按键名称。例如，在蹦床车厢结束提示里，可以根据平台自动显示“SHIFT”“B”或对应触摸按钮。

<CodeHeader>RP/texts/en_US.lang</CodeHeader>

```lang
action.hint.exit.rollercoaster=Press :_input_key.sneak: to end the ride
```

未定义的输入键会始终显示为`Unassigned`。

## 常见输入键

### 通用输入键

| 名称 | 短代码 |
|---|---|
| 攻击 | `:_input_key.attack:` |
| 使用 | `:_input_key.use:` |
| 聊天 | `:_input_key.chat:` |
| 丢弃 | `:_input_key.drop:` |
| 表情 | `:_input_key.emote:` |
| 跳跃 | `:_input_key.jump:` |
| 潜行 | `:_input_key.sneak:` |
| 疾跑 | `:_input_key.sprint:` |
| 前进 | `:_input_key.forward:` |
| 后退 | `:_input_key.back:` |
| 向左 | `:_input_key.left:` |
| 向右 | `:_input_key.right:` |
| 背包 | `:_input_key.inventory:` |
| 切换物品（左） | `:_input_key.cycleItemLeft:` |
| 切换物品（右） | `:_input_key.cycleItemRight:` |
| 切换视角 | `:_input_key.togglePerspective:` |
| 拾取方块 | `:_input_key.pickItem:` |

### 键盘与鼠标输入键

| 名称 | 短代码 |
|---|---|
| 物品栏槽位1～9 | `:_input_key.hotbar.1:`～`:_input_key.hotbar.9:` |
| 打开命令 | `:_input_key.command:` |
| 打开通知 | `:_input_key.interactwithtoast:` |
| 游戏效果 | `:_input_key.mobEffects:` |
| 复制坐标 | `:_input_key.copyCoordinates:` |
| 复制朝向坐标 | `:_input_key.copyFacingCoordinates:` |

### 控制器输入键

| 名称 | 短代码 |
|---|---|
| 慢速上升 | `:_input_key.flyUpSlow:` |
| 慢速下降 | `:_input_key.flyDownSlow:` |
| 游戏效果/打开通知 | `:_input_key.mobeffectsandinteractwithtoast:` |

## 使用注意事项

- 输入键的显示结果取决于当前输入方案，而不是固定文本。
- 同一个短代码在不同平台上可能显示为不同图标。
- 并非所有文本位置都支持输入键短代码；若场景不支持，通常会直接显示原文或`Unassigned`。

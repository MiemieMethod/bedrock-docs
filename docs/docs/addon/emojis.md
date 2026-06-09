# 表情符号

**表情符号（Emoji）**是基岩版内置的一组Unicode私有使用区（Private Use Area，PUA）字符。游戏会把这些字符渲染为图标或符号，而不是普通文字，因此它们可以在告示牌、书与笔、聊天、物品名称和部分界面文本中充当装饰性或提示性字符。

## 概述

很多位置都支持直接输入短代码，而不必手动粘贴字符本身。若某个输入框不接受短代码，也可以直接复制字符列中的图形字符。

/// danger | Ore UI
表情符号不受Ore UI界面支持。
///

## 常见原版表情符号

### 方块与物品

| 名称 | 短代码 | 字符 |
|---|---|---|
| 木镐 | `:wood_pickaxe:` | `` |
| 木剑 | `:wood_sword:` | `` |
| 工作台 | `:crafting_table:` | `` |
| 熔炉 | `:furnace:` | `` |

### HUD

| 名称 | 短代码 | 字符 |
|---|---|---|
| 护甲 | `:armor:` | `` |
| 准星 | `:tip_crosshair:` | `` |
| 食物 | `:shank:` | `` |
| 生命 | `:heart:` | `` |

### 市集

| 名称 | 短代码 | 字符 |
|---|---|---|
| Minecoin | `:minecoin:` | `` |
| Token | `:token:` | `` |

在非PlayStation设备上，`:minecoin:`和`:token:`通常都会显示为Minecoin表情符号；在PlayStation设备上，两者都会显示为Token表情符号。

### 配方书

| 名称 | 短代码 | 字符 |
|---|---|---|
| 可合成开启 | `:craftable_toggle_on:` | `` |
| 可合成关闭 | `:craftable_toggle_off:` | `` |

### 鼠标

| 名称 | 短代码 | 字符 |
|---|---|---|
| 左键 | `:mouse_left_button:` | `` |
| 右键 | `:mouse_right_button:` | `` |
| 中键 | `:mouse_middle_button:` | `` |
| 按键 | `:mouse_button:` | `` |

### 触摸

| 名称 | 短代码 | 字符 |
|---|---|---|
| 前进 | `:touch_forward:` | `` |
| 左移 | `:touch_left:` | `` |
| 后退 | `:touch_back:` | `` |
| 右移 | `:touch_right:` | `` |
| 跳跃 | `:touch_jump:` | `` |
| 潜行 | `:touch_sneak:` | `` |
| 聊天 | `:touch_chat:` | `` |
| 疾跑 | `:touch_sprint:` | `` |

### 控制器

| 名称 | 短代码 | 字符 |
|---|---|---|
| Xbox A | `:xbox_face_button_down:` | `` |
| Xbox B | `:xbox_face_button_right:` | `` |
| Xbox X | `:xbox_face_button_left:` | `` |
| Xbox Y | `:xbox_face_button_up:` | `` |
| 任天堂Switch A | `:switch_face_button_down:` | `` |
| 任天堂Switch B | `:switch_face_button_right:` | `` |
| PlayStation X | `:ps4_face_button_down:` | `` |
| PlayStation △ | `:ps4_face_button_up:` | `` |

### 其他

| 名称 | 短代码 | 字符 |
|---|---|---|
| 不换行空格 | `:nbsp:` | `` |
| Agent | `:code_builder_button:` | `` |
| 沉浸式阅读器 | `:immersive_reader_button:` | `` |
| 空心星 | `:hollow_star:` | `` |
| 实心星 | `:solid_star:` | `` |
| 相机 | `:camera:` | `` |

## 自定义表情符号

自定义表情符号本质上是替换字体资源中的字形页。最常见的做法是修改`font/glyph_E0.png`和`font/glyph_E1.png`，然后把自己的图案放进对应的字符格中。

如果需要更详细的制作方法，请参见[字体](font.md)。

## 使用注意事项

- 许多输入框只接受字符本身，不接受短代码。
- 不同平台可能会对同一短代码显示出不同图标。
- 这些字符本质上是Unicode私有使用区字符，因此也可以被复制到其他支持相应字体的文本环境中。
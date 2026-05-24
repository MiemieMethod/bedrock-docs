# 颜色代码

**颜色代码（Color Code）**用于控制Endstone插件中的文本颜色与格式。它直接对应Minecraft的`§`格式代码，常用于聊天消息、标题、动作栏和表单提示文本。

## Python

```python
from endstone import ColorFormat

text = (
    ColorFormat.YELLOW
    + "黄色文本"
    + ColorFormat.RESET
    + "，后面恢复默认格式。"
)
```

## C++

```cpp
#include <endstone/endstone.hpp>

auto text = endstone::ColorFormat::Yellow + "黄色文本" + endstone::ColorFormat::Reset;
```

## 常用代码

| 代码 | 名称 |
|------|------|
| `ColorFormat.BLACK` | 黑色 |
| `ColorFormat.DARK_BLUE` | 深蓝色 |
| `ColorFormat.DARK_GREEN` | 深绿色 |
| `ColorFormat.GOLD` | 金色 |
| `ColorFormat.YELLOW` | 黄色 |
| `ColorFormat.AQUA` | 青色 |
| `ColorFormat.RED` | 红色 |
| `ColorFormat.WHITE` | 白色 |
| `ColorFormat.BOLD` | 粗体 |
| `ColorFormat.ITALIC` | 斜体 |
| `ColorFormat.RESET` | 重置 |

## 要点

- 颜色码会持续作用到下一个重置码。
- 组合格式时，通常应在文本末尾追加`RESET`。
- 文本内容来自插件API时，仍应按消息发送位置选择合适的格式层级。

## 参考

- [Endstone命令与文本格式](../../../refs/server/endstone-command-format.md)
- [Endstone API总览](../../../refs/server/endstone-api.md)
- [颜色代码原文](../../../translations/endstone/tutorials/use-color-codes.md)
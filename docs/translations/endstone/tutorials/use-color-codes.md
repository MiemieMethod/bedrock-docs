---
comments: true
---

# 使用颜色代码

颜色代码用于自定义游戏中的文本颜色和格式，例如在标牌、聊天、标题、表单等位置。这些颜色代码由节符号`§`加一个字符组成。每个字符都代表一种颜色或格式选项。Endstone提供了易用的API来处理这类文本。

## 用法

=== ":fontawesome-brands-python: Python"

    此代码展示了在Endstone中使用彩色文本的基本方式：

    ```python
    from endstone import ColorFormat

    my_beautiful_text = f"This is {ColorFormat.YELLOW}yellow, {ColorFormat.AQUA}aqua and {ColorFormat.GOLD}gold{ColorFormat.RESET}."
    ```

    *[Python f字符串]真的很棒。*
    
    !!! tip

        不要忘记用`ColorFormat.RESET`结束彩色文本，它结束所有额外的颜色格式选项并重置它们。 

    [Python f字符串]: https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings

=== ":simple-cplusplus: C++"

    此代码展示了在Endstone中使用彩色文本的基本方式：
    
    ```cpp
    #include <endstone/endstone.hpp>

    auto my_beautiful_text = "This is " + endstone::ColorFormat::DarkGreen + "dark green." + endstone::ColorFormat::Reset;
    ```
    
    !!! tip
    
        不要忘记用`endstone::ColorFormat::Reset`结束彩色文本，它结束所有额外的颜色格式选项并重置它们。 

## 所有颜色和格式代码

<div class="center-table" markdown>

| 代码 |        名称        |
|:----:|:------------------:|
| `§0` |       black        |
| `§1` |     dark_blue      |
| `§2` |     dark_green     |
| `§3` |     dark_aqua      |
| `§4` |      dark_red      |
| `§5` |    dark_purple     |
| `§6` |        gold        |
| `§7` |        gray        |
| `§8` |     dark_gray      |
| `§9` |        blue        |
| `§a` |       green        |
| `§b` |        aqua        |
| `§c` |        red         |
| `§d` |    light_purple    |
| `§e` |       yellow       |
| `§f` |       white        |
| `§g` |   minecoin_gold    |
| `§h` |  material_quartz   |
| `§i` |   material_iron    |
| `§j` | material_netherite |
| `§k` |     obfuscated     |
| `§l` |        bold        |
| `§m` | material_redstone  |
| `§n` |  material_copper   |
| `§o` |       italic       |
| `§p` |   material_gold    |
| `§q` |  material_emerald  |
| `§r` |       reset        |
| `§s` |  material_diamond  |
| `§t` |   material_lapis   |
| `§u` | material_amethyst  |

</div>

# Endstone命令与文本格式

本页列出Endstone教程中公开的命令用法、权限默认值和文本颜色格式。相关内容仅适用于Endstone插件API，不属于BDS原生命令系统。

## 命令用法参数

Endstone命令用法使用尖括号表示必选参数，使用方括号表示可选参数。

| 形式 | 含义 | 示例 |
|------|------|------|
| `<name: type>` | 必须提供的参数 | `/home <name: string>` |
| `[name: type]` | 可以省略的参数 | `/hello [msg: message]` |

自定义枚举参数将可选值写入圆括号，并使用竖线分隔。

| 形式 | 含义 | 示例 |
|------|------|------|
| `(a\|b\|c)<name: EnumType>` | 必选枚举参数 | `/home (add\|list\|del)<action: HomeAction>` |
| `(a\|b\|c)[name: EnumType]` | 可选枚举参数 | `/mode (public\|private)[mode: HomeMode]` |

## 内置参数类型

| 类型 | 别名 | 描述 | 示例值 |
|------|------|------|--------|
| `int` |  | 整数。 | `10` |
| `float` |  | 浮点数。 | `3.14` |
| `bool` |  | 布尔值。 | `true` |
| `target` | `actor`、`entity`、`player` | 目标选择器或玩家名。 | `@e`、`@r`、`Steve` |
| `str` | `string` | 以空格结束的字符串。 | `Hello` |
| `block_pos` | `vec3i` | 三维整数位置。 | `1 2 3` |
| `pos` | `vec3`、`vec3f` | 三维浮点数位置。 | `1.0 2.0 3.0` |
| `message` |  | 直到行尾的消息文本。 | `Hello World!` |
| `json` |  | JSON字符串。 | `{"key":"value"}` |
| `block` |  | 方块类型。 | `wood` |
| `block_states` |  | 方块状态集合。 | `["wood_type"="birch","stripped_bit"=true]` |
| `entity_type` |  | 实体类型。 | `minecraft:creeper` |

/// warning | `message`参数位置
Endstone变更记录指出，若命令用法包含`message`类型参数，该参数必须位于最后，后方不能继续放置其他参数。
///

## 权限默认值

Endstone教程指出，命令默认要求操作员权限。插件若希望改变命令可用范围，应为命令绑定权限并设置默认值。

| Python默认值 | C++默认值 | 含义 |
|--------------|-----------|------|
| `True`或`"true"` | `endstone::PermissionDefault::True` | 所有命令发送者默认拥有该权限。 |
| `False`或`"false"` | `endstone::PermissionDefault::False` | 默认没有命令发送者拥有该权限，除非另行授予。 |
| `"op"` | `endstone::PermissionDefault::Operator` | 只有操作员默认拥有该权限。 |
| `"not_op"` | `endstone::PermissionDefault::NotOperator` | 只有非操作员默认拥有该权限。 |
| `"console"` | `endstone::PermissionDefault::Console` | 只有控制台默认拥有该权限。 |

## 文本颜色与格式代码

Endstone的`ColorFormat`包装了Minecraft文本中的`§`颜色与格式代码。使用颜色后，通常应在文本末尾追加重置代码，避免后续文本继承格式。

| 代码 | 名称 |
|------|------|
| `§0` | `black` |
| `§1` | `dark_blue` |
| `§2` | `dark_green` |
| `§3` | `dark_aqua` |
| `§4` | `dark_red` |
| `§5` | `dark_purple` |
| `§6` | `gold` |
| `§7` | `gray` |
| `§8` | `dark_gray` |
| `§9` | `blue` |
| `§a` | `green` |
| `§b` | `aqua` |
| `§c` | `red` |
| `§d` | `light_purple` |
| `§e` | `yellow` |
| `§f` | `white` |
| `§g` | `minecoin_gold` |
| `§h` | `material_quartz` |
| `§i` | `material_iron` |
| `§j` | `material_netherite` |
| `§k` | `obfuscated` |
| `§l` | `bold` |
| `§m` | `material_redstone` |
| `§n` | `material_copper` |
| `§o` | `italic` |
| `§p` | `material_gold` |
| `§q` | `material_emerald` |
| `§r` | `reset` |
| `§s` | `material_diamond` |
| `§t` | `material_lapis` |
| `§u` | `material_amethyst` |

<!-- md:sortable -->

## 相关教程

- [注册命令（Endstone翻译）](../../translations/endstone/tutorials/register-commands.md)
- [使用颜色代码（Endstone翻译）](../../translations/endstone/tutorials/use-color-codes.md)

# 本地化

本地化就是把游戏内显示文本从“写死的字符串”改成“语言键”。这样同一个包可以根据玩家语言显示不同文本，也能避免实体名、方块名、皮肤包名散落在多个JSON文件里难以维护。

## 创建语言文件

资源包、行为包、世界模板和皮肤包都可能使用`texts`目录。最常见的结构如下：

/// html | div.treeview
- `demo_RP`
    - `texts`
        - `languages.json`
        - `en_US.lang`
        - `zh_CN.lang`
///

`languages.json`列出支持的语言：

```json title="texts/languages.json"
[
  "en_US",
  "zh_CN"
]
```

`en_US.lang`是很多内容的兜底语言文件。请使用UTF-8编码保存，并且不要让编辑器自动把扩展名变成`.txt`。

## 编写.lang

语言文件的基本格式是：

```text title="texts/en_US.lang"
tile.demo:die.name=Die
item.demo:coin=Coin
entity.demo:robot.name=Robot
item.spawn_egg.entity.demo:robot.name=Spawn Robot
```

常用键名如下：

| 内容 | 键名格式 |
|---|---|
| 方块名 | `tile.<identifier>.name=<显示名>` |
| 物品名 | `item.<identifier>=<显示名>` |
| 实体名 | `entity.<identifier>.name=<显示名>` |
| 实体刷怪蛋名 | `item.spawn_egg.entity.<identifier>.name=<显示名>` |
| 世界模板名 | `pack.name=<显示名>` |
| 世界模板描述 | `pack.description=<描述>` |
| 皮肤包名 | `skinpack.<localization_name>=<显示名>` |

官方本地化指南建议给翻译文本补充注释，尤其是要交给翻译流程处理的内容。注释放在值后面，用`###`开始：

```text
quest.demo.welcome=Welcome to the oasis! ###Shown when the player first enters the oasis.
```

## 在内容中引用

有些定义可以直接写显示文本，例如物品的`minecraft:display_name.value`；但更推荐把玩家可见文本放进语言文件。对于方块、实体和刷怪蛋，游戏会按约定键名查找显示名，所以你只要保证标识符一致即可。

## 检查清单

1. `languages.json`是否列出了你创建的语言文件。
2. `.lang`文件是否保存为UTF-8编码。
3. 键名中标识符是否与实体、方块或物品定义完全一致。
4. 等号两侧是否没有多余空格。
5. 如果文本太长，是否在游戏界面中显示完整。

本地化做得越早，后续扩展越轻松。接下来你在实体、方块、物品、世界模板和皮肤包教程里都会继续用到它。
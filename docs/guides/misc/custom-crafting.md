# 自定义合成器

这个方案用漏斗/投掷器布局+`execute if blocks`实现“命令合成台”。

## 搭建思路

每个配方需要两只投掷器：

1. 配方投掷器(放输入布局)
2. 产物投掷器(放输出结果)

再放一只给玩家使用的“合成器投掷器”。

![配方投掷器](../../../assets/images/guides/misc/custom-crafting/recipe.png)
<!-- 图片获取方式：从知识库源文件custom-crafting.md中的recipe.png提取。 -->

![产物投掷器](../../../assets/images/guides/misc/custom-crafting/recipe-output.png)
<!-- 图片获取方式：从知识库源文件custom-crafting.md中的recipe-output.png提取。 -->

## 核心命令

```mcfunction title="BP/functions/wiki/custom_crafting.mcfunction"
execute if blocks <recipe> <recipe> <crafter> masked run clone <recipe_output> <recipe_output> <crafter>
```

- `<recipe>`是配方投掷器坐标。
- `<recipe_output>`是产物投掷器坐标。
- `<crafter>`是玩家交互投掷器坐标。

## 可选体验增强

```mcfunction title="BP/functions/wiki/custom_crafting.sound.mcfunction"
execute if blocks <recipe> <recipe> <crafter> masked positioned <crafter> run playsound smithing_table.use @a[r=7]
execute if blocks <recipe> <recipe> <crafter> masked run clone <recipe_output> <recipe_output> <crafter>
```

![完成布局示意](../../../assets/images/guides/misc/custom-crafting/completed-setup.png)
<!-- 图片获取方式：从知识库源文件custom-crafting.md中的completed-setup.png提取。 -->

/// tip | 延伸方向
如果你要做“可搬运合成器”，建议结合函数和标记实体管理多个`<crafter>`坐标，而不是固定一套坐标。
///

## 继续阅读

- [MBE方块实体](./block-entities.md)
- [FMBE显示实体](./display-entities.md)

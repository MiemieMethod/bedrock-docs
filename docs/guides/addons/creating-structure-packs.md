# 制作结构包

结构包本质上是一个只包含结构文件的行为包。你可以把用结构方块导出的`.mcstructure`文件放进`structures`目录，再通过结构方块、`/structure`命令、地物或脚本复用这些结构。

## 保存结构

在创造模式世界中运行：

```mcfunction
/give @s structure_block
```

放置结构方块并切换到保存模式，调整尺寸和偏移，让选择框包住你要保存的建筑或实体。结构方块会保存方块状态，箱子物品栏、命令方块命令和选区内实体也可以被保存。

结构名称建议只使用小写字母、数字、下划线和短横线。游戏界面常会自动加上`mystructure:`命名空间。

## 导出为.mcstructure

Windows版结构方块界面提供导出按钮，可以把选区导出为`.mcstructure`文件。官方资料中记录的保存模式最大尺寸为X64、Y257、Z64；如果输入更大的值，界面会把它改回允许的最大值。

## 放进行为包

创建行为包结构：

/// html | div.treeview
- `demo_structure_BP`
    - `manifest.json`
    - `structures`
        - `demo`
            - `house.mcstructure`
///

`manifest.json`使用普通行为包清单，模块类型为`data`。

## 加载结构

如果文件位于`structures/demo/house.mcstructure`，可以在游戏中尝试：

```mcfunction
/structure load demo:house ~ ~ ~
```

也可以用结构方块的加载模式导入和加载`.mcstructure`。如果你想让结构自然生成，请继续阅读自定义地物教程，使用`minecraft:structure_template_feature`引用结构。

## 常见用途

- 做地图编辑时快速复制建筑。
- 给函数或命令方块提供可加载的机关。
- 给地物系统提供树、遗迹、热气球等结构模板。
- 给GameTest或脚本测试提供固定场景。

结构包不需要资源包，除非结构中使用了自定义方块、实体外观或其他资源。发布前请在一个全新世界中导入并加载结构，确认所有依赖都被包含。

# 实体持物

本教程介绍如何让自定义实体在手中持有物品，例如让一个战士型实体出生时手持武器。

## 准备模型

首先，你需要在Blockbench中制作一个包含`rightItem`骨骼的模型。该骨骼的轴心点位置决定了物品在手中的位置和朝向，请将其调整到希望实体握住物品的位置。

<!-- 截图：Blockbench中展示rightItem骨骼和轴心点位置的截图。路径：docs/assets/images/guides/addons/data-driven/entities/holding-items/blockbench.png -->

## 装备组件

在实体的行为包定义文件中，添加`minecraft:equipment`组件，并指向一个战利品表文件：

```json title="BP/entities/my_entity.json > minecraft:entity > components"
"minecraft:equipment": {
    "table": "loot_tables/wiki/entities/gear/my_entity.json"
}
```

## 战利品表

为实体创建一个专门用于装备（而非死亡掉落）的战利品表。两者文件名不能相同，否则会产生冲突。

以下战利品表让实体始终持有`wiki:hammer`物品：

```json title="BP/loot_tables/wiki/entities/gear/my_entity.json"
{
    "pools": [
        {
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "wiki:hammer"
                }
            ]
        }
    ]
}
```

这个战利品表只决定实体**手持什么物品**，不影响它死亡时掉落的物品（死亡掉落由另一个单独的战利品表控制，通过`minecraft:loot`组件指定）。

完成以上步骤后，实体在生成时就会手持你指定的物品。

<!-- 截图：游戏内截图，展示实体手持物品的效果。路径：docs/assets/images/guides/addons/data-driven/entities/holding-items/result.png -->

## 常见问题

**问题**：手持物品没有显示出来。

**原因**：实体定义中包含多个几何体变种时，可能存在`rightItem`骨骼未被所有几何体包含的情况。请检查每一个几何体文件，确保每个变种都有`rightItem`骨骼。
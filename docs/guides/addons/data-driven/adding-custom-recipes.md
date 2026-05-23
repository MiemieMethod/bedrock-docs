# 自定义配方

配方属于行为包，放在`recipes`目录中。它可以定义有序合成、无序合成、烧炼、酿造和锻造等规则。最适合作为练习的是有序配方和无序配方。

## 无序配方

无序配方不关心材料摆放位置：

```json title="demo_BP/recipes/coin_from_gold.json"
{
  "format_version": "1.20.10",
  "minecraft:recipe_shapeless": {
    "description": {
      "identifier": "demo:coin_from_gold"
    },
    "tags": [
      "crafting_table"
    ],
    "ingredients": [
      {
        "item": "minecraft:gold_nugget"
      }
    ],
    "result": {
      "item": "demo:coin",
      "count": 1
    }
  }
}
```

## 有序配方

有序配方使用`pattern`和`key`定义形状。官方配方介绍记录，最大合成网格为3×3，超过第三个字符的部分会被忽略。

```json title="demo_BP/recipes/gold_block_from_coins.json"
{
  "format_version": "1.20.10",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "demo:gold_block_from_coins"
    },
    "tags": [
      "crafting_table"
    ],
    "pattern": [
      "CCC",
      "CCC",
      "CCC"
    ],
    "key": {
      "C": {
        "item": "demo:coin"
      }
    },
    "result": {
      "item": "minecraft:gold_block",
      "count": 1
    }
  }
}
```

## 自定义工作台配方

如果你在自定义工作台中使用了`crafting_tags`，配方`tags`里写同一个标签即可：

```json
"tags": [
  "demo_gem_table"
]
```

## 测试和解锁

创建世界时开启行为包，进入后打开对应工作台。如果配方没有出现，先确认：

- 结果物品是否存在。
- `tags`是否包含当前合成界面的标签。
- JSON文件是否位于行为包`recipes`目录。
- 自定义物品或方块是否已经在同一行为包中正确加载。

较新版本支持配方解锁条件。你可以让配方始终解锁，或在玩家获得某个物品、满足某个上下文后解锁；实际发布前请按目标版本测试配方书表现。

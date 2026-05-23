# 自定义战利品表

战利品表用于决定实体死亡、方块破坏、容器填充等场景会产出什么物品。它属于行为包，通常放在`loot_tables`目录下。

## 最小战利品表

```json title="demo_BP/loot_tables/entities/robot.json"
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:diamond"
        }
      ]
    }
  ]
}
```

这张表每次被调用都会产出1个钻石。

## 挂到实体上

在实体行为文件中添加：

```json
"minecraft:loot": {
  "table": "loot_tables/entities/robot.json"
}
```

路径从行为包根目录开始写。

## 权重和次数

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:diamond",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:coal",
          "weight": 4
        }
      ]
    }
  ]
}
```

`rolls`可以是固定数，也可以是范围。`weight`控制同一个池中条目的相对概率；示例中煤炭相对钻石更容易被选中。

## 函数和条件

战利品函数可以改变数量、附魔、名称、耐久等。下面让掉落数量在0到2之间：

```json
"functions": [
  {
    "function": "set_count",
    "count": {
      "min": 0,
      "max": 2
    }
  }
]
```

条件可以限制掉落场景，例如只在被玩家击杀时掉落。官方示例中洞穴蜘蛛的蜘蛛眼池就使用了`killed_by_player`条件。

## 测试建议

战利品表有随机性。测试时请多击杀几次实体，或者临时把`rolls`和`weight`改成确定值。确认能掉落后，再恢复概率设计。

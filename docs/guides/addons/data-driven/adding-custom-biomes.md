# 自定义生物群系

生物群系决定地表材料、气候、标签、部分环境表现和哪些地物或生物会在这里出现。基岩版自定义生物群系通常通过行为包替换或部分替换原版生物群系，并可配合资源包客户端生物群系文件设置天空、水色、迷雾和环境声音。

## 替换一个原版生物群系

下面示例改写沙滩的表面材料。它来自官方世界生成概览中的思路：使用行为包生物群系定义替换`minecraft:beach`的一部分生成参数。

```json title="demo_BP/biomes/beach.json"
{
  "format_version": "1.21.110",
  "minecraft:biome": {
    "description": {
      "identifier": "minecraft:beach"
    },
    "components": {
      "minecraft:climate": {
        "downfall": 0.4,
        "snow_accumulation": [0.0, 0.125],
        "temperature": 0.8
      },
      "minecraft:overworld_height": {
        "noise_type": "beach"
      },
      "minecraft:surface_builder": {
        "builder": {
          "type": "minecraft:overworld",
          "sea_floor_depth": 7,
          "sea_floor_material": "minecraft:gravel",
          "foundation_material": "minecraft:stone",
          "mid_material": "demo:white_sand",
          "top_material": "demo:white_sand",
          "sea_material": "minecraft:water"
        }
      },
      "minecraft:tags": {
        "tags": [
          "beach",
          "monster",
          "overworld",
          "warm"
        ]
      }
    }
  }
}
```

这里的`demo:white_sand`必须已经是可用方块。否则生物群系加载或生成可能失败。

## 用标签连接地物

地物规则可以通过`has_biome_tag`检测生物群系标签：

```json
"minecraft:biome_filter": [
  {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "beach"
  }
]
```

因此，设计自定义生物群系时要认真规划标签。标签不仅方便地物规则，也会影响一些生成和分类逻辑。

## 测试建议

世界生成内容只会影响新生成区块。测试时请新建世界，或传送到从未加载过的远处区域。已经生成过的区块不会因为你修改生物群系JSON就自动重做地形。

如果只是想改天空、水色、迷雾或环境声音，请优先查看客户端生物群系和迷雾定义；不要为了视觉效果随意替换服务端生物群系。
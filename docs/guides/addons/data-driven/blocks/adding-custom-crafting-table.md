# 自定义工作台

自定义工作台的关键不是“长得像工作台”，而是“配方只在指定的合成界面可用”。基岩版方块可以通过`minecraft:crafting_table`组件声明合成标签，配方再用同一个标签限制可用位置。

## 创建工作台方块

```json title="demo_BP/blocks/gem_table.json"
{
  "format_version": "1.21.80",
  "minecraft:block": {
    "description": {
      "identifier": "demo:gem_table"
    },
    "components": {
      "minecraft:destructible_by_mining": {
        "seconds_to_destroy": 2.0
      },
      "minecraft:crafting_table": {
        "table_name": "container.demo.gem_table",
        "crafting_tags": [
          "demo_gem_table"
        ]
      },
      "minecraft:material_instances": {
        "*": {
          "texture": "gem_table",
          "render_method": "opaque"
        }
      }
    }
  }
}
```

`crafting_tags`最多可以包含64个标签，每个标签最多64个字符。配方只要声明了对应标签，就能在这个工作台里出现。

## 添加纹理和名称

```json title="demo_RP/textures/terrain_texture.json"
{
  "resource_pack_name": "demo_RP",
  "texture_name": "atlas.terrain",
  "texture_data": {
    "gem_table": {
      "textures": "textures/blocks/gem_table"
    }
  }
}
```

```text title="demo_RP/texts/en_US.lang"
tile.demo:gem_table.name=Gem Table
container.demo.gem_table=Gem Table
```

## 创建专用配方

```json title="demo_BP/recipes/gem_from_diamond.json"
{
  "format_version": "1.20.10",
  "minecraft:recipe_shapeless": {
    "description": {
      "identifier": "demo:gem_from_diamond"
    },
    "tags": [
      "demo_gem_table"
    ],
    "ingredients": [
      {
        "item": "minecraft:diamond"
      }
    ],
    "result": {
      "item": "minecraft:emerald",
      "count": 1
    }
  }
}
```

现在这条配方只会出现在带有`demo_gem_table`标签的合成表中，而不会污染原版工作台。

## 测试

1. 用`/give @s demo:gem_table`取得方块。
2. 放置并打开它。
3. 放入钻石，检查是否能合成绿宝石。
4. 再打开原版工作台，确认这条配方不会在那里出现。

如果配方不显示，检查工作台`crafting_tags`和配方`tags`是否完全一致。

# 第一个方块

这一页创建一个最小的自定义骰子方块。它能放置在世界中，并使用资源包中的纹理显示。

## 行为包定义

创建文件：

```json title="demo_BP/blocks/die.json"
{
  "format_version": "1.21.80",
  "minecraft:block": {
    "description": {
      "identifier": "demo:die"
    },
    "components": {
      "minecraft:destructible_by_mining": {
        "seconds_to_destroy": 1.5
      },
      "minecraft:destructible_by_explosion": {
        "explosion_resistance": 3.0
      },
      "minecraft:map_color": "#ffffff",
      "minecraft:material_instances": {
        "*": {
          "texture": "die_1",
          "render_method": "opaque"
        }
      }
    }
  }
}
```

`identifier`是方块真正的标识符。`minecraft:material_instances`中的`die_1`不是文件路径，而是资源包纹理图集中的纹理短名。

## 资源包纹理

把16×16像素图片放到：

```text
demo_RP/textures/blocks/die_1.png
```

再创建或编辑：

```json title="demo_RP/textures/terrain_texture.json"
{
  "resource_pack_name": "demo_RP",
  "texture_name": "atlas.terrain",
  "padding": 8,
  "num_mip_levels": 4,
  "texture_data": {
    "die_1": {
      "textures": "textures/blocks/die_1"
    }
  }
}
```

## 本地化

```text title="demo_RP/texts/en_US.lang"
tile.demo:die.name=Die
```

## 获取并测试

进入世界后运行：

```mcfunction
/give @s demo:die
```

如果物品栏里出现方块但放下后纹理异常，检查`terrain_texture.json`中的短名是否和`minecraft:material_instances`一致。若命令提示未知物品或方块，优先检查行为包是否启用、方块JSON路径是否正确。

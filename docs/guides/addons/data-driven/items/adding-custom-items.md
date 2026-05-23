# 第一个物品

这一页创建一个名为`demo:coin`的普通物品。它不能吃、不能穿、不能放置，只用于学习物品定义、图标图集和本地化。

## 行为包物品

```json title="demo_BP/items/coin.json"
{
  "format_version": "1.20.30",
  "minecraft:item": {
    "description": {
      "identifier": "demo:coin",
      "category": "Items"
    },
    "components": {
      "minecraft:max_stack_size": 64,
      "minecraft:icon": {
        "texture": "demo:coin"
      },
      "minecraft:display_name": {
        "value": "item.demo:coin"
      }
    }
  }
}
```

`minecraft:icon.texture`引用的是物品纹理图集里的键，不是图片路径。

## 资源包图标

把图标放入：

```text
demo_RP/textures/items/coin.png
```

再创建：

```json title="demo_RP/textures/item_texture.json"
{
  "resource_pack_name": "demo_RP",
  "texture_data": {
    "demo:coin": {
      "textures": "textures/items/coin"
    }
  }
}
```

## 本地化

```text title="demo_RP/texts/en_US.lang"
item.demo:coin=Coin
```

## 测试

进入世界运行：

```mcfunction
/give @s demo:coin 16
```

如果物品能获得但图标是紫黑棋盘格，检查资源包是否启用、`item_texture.json`是否在`textures`目录下、图标键是否与`minecraft:icon.texture`一致。如果显示名没有变化，检查`minecraft:display_name.value`和语言文件键名。

## 下一步

给物品添加配方，让它能被合成；或者制作附着物，让它在玩家手中显示三维模型。

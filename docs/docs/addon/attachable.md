# 附着物

**附着物（Attachable）**是Minecraft基岩版资源包中定义装备物品外观的一种定义类型。附着物将物品与几何体模型、纹理、动画等渲染资源关联，使得物品在被玩家穿戴或手持时能够在玩家模型上显示自定义的视觉效果。

## 概述

在基岩版中，当玩家手持物品或穿戴盔甲时，这些物品的三维外观由附着物系统控制。附着物定义文件的结构与客户端实体定义文件非常相似，同样包含几何体、纹理、动画、渲染控制器等字段。区别在于附着物不描述一个独立的实体，而是依附于穿戴该物品的实体（通常是玩家）上进行渲染。

附着物定义文件位于资源包的`attachables/`目录中。

## 基本结构

附着物定义文件遵循以下基本结构：

```json title="附着物定义示例"
{
  "format_version": "1.10.0",
  "minecraft:attachable": {
    "description": {
      "identifier": "命名空间:物品标识符",
      "materials": {
        "default": "armor",
        "enchanted": "armor_enchanted"
      },
      "textures": {
        "default": "textures/models/armor/custom_armor",
        "enchanted": "textures/misc/enchanted_item_glint"
      },
      "geometry": {
        "default": "geometry.custom_armor"
      },
      "render_controllers": ["controller.render.armor"],
      "animations": {},
      "scripts": {}
    }
  }
}
```

## 标识符关联

附着物的标识符需要与其对应的物品的赋命名空间标识符一致。当游戏渲染玩家手持或穿戴某物品时，引擎会查找与该物品标识符匹配的附着物定义，并据此渲染物品的外观。

对于原版物品，可以通过创建同标识符的附着物定义来覆盖其默认外观。

## 附着物与盔甲

自定义盔甲是附着物最典型的应用场景。通过附着物定义，开发者可以为自定义盔甲指定专属的模型和纹理，而非使用原版的盔甲纹理。

盔甲附着物通常使用`armor`和`armor_enchanted`两种材质，后者用于显示附魔光泽。渲染控制器中通过Molang查询`query.is_enchanted`判断是否应用附魔材质。

## 附着物与手持物品

手持物品（如工具和武器）也可以通过附着物系统自定义其三维外观。手持物品的附着物通过动画和脚本的`scripts.animate`字段控制其在第一人称和第三人称视角下的位置和动画。

## 纹理与几何体

附着物使用的纹理和几何体与客户端实体使用的格式完全相同。几何体文件使用标准的模型格式，纹理使用标准的PNG图片。多个附着物可以共享同一个几何体和纹理文件。
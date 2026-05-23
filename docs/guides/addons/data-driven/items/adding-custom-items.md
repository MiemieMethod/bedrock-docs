# 第一个物品

欢迎来到自定义物品系列教程！本篇将带你从零创建一个能进入创造模式物品栏、能在生存模式合成的基础物品。

## 注册物品

物品的核心定义位于行为包的`items`文件夹下。每个`.json`文件对应一种物品，其顶层结构包含两部分：`description`（描述）和`components`（组件）。

```json title="BP/items/custom_item.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:custom_item",
            "menu_category": {
                "category": "items",
                "group": "minecraft:itemGroup.name.miscellaneous"
            }
        },
        "components": {}
    }
}
```

/// note | `components`不能省略
即使暂时不添加任何组件，`components`对象也必须存在，否则游戏将无法加载该物品。
///

`menu_category`控制物品在创造模式物品栏中的位置：

/// define
`category` <!-- md:flag required -->

- 决定物品出现在哪个大分类下，可选值有`"construction"`、`"equipment"`、`"items"`、`"nature"`和`"none"`。

`group`

- 决定物品归属于哪个可折叠的子分组（如石剑、木剑等共同收纳在剑组中）。省略时物品单独列出。可用分组列表参见[创造分组枚举](../../../../refs/tables/items/creative_groups.md)。

`is_hidden_in_commands`

- 设为`true`时，该物品在命令自动补全列表中不显示。默认为`false`。
///

## 添加组件

现在，让我们为物品添加几个常用组件，赋予它真正的属性：

```json title="BP/items/custom_item.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:custom_item",
            "menu_category": {
                "category": "items"
            }
        },
        "components": {
            "minecraft:max_stack_size": 16,
            "minecraft:icon": "wiki:custom_item",
            "minecraft:display_name": {
                "value": "item.wiki:custom_item"
            }
        }
    }
}
```

更多可用组件详见[物品组件概览](item-components.md)。

## 注册图标纹理

仅将PNG文件放入`RP/textures/items/`还不够——需要在资源包的`item_texture.json`中将图标短名映射到图片路径：

```json title="RP/textures/item_texture.json"
{
    "texture_data": {
        "wiki:custom_item": {
            "textures": "textures/items/custom_item"
        }
    }
}
```

`minecraft:icon`组件中填写的`"wiki:custom_item"`就是这里`texture_data`中的键名（短名），而值`"textures/items/custom_item"`是不含扩展名的图片路径。

## 定义显示名称

在资源包的语言文件中添加本地化条目：

```lang title="RP/texts/zh_CN.lang"
item.wiki:custom_item=自定义物品
```

如果你的`minecraft:display_name.value`是`"item.wiki:custom_item"`，游戏就会在这里查找该键对应的翻译文字。

## 添加配方

让物品可以在生存模式合成，在行为包中创建一份配方文件：

```json title="BP/recipes/custom_item.json"
{
    "format_version": "1.26.10",
    "minecraft:recipe_shapeless": {
        "description": {
            "identifier": "wiki:custom_item"
        },
        "tags": ["crafting_table"],
        "ingredients": [
            { "item": "minecraft:stick" },
            { "item": "minecraft:stick" }
        ],
        "result": {
            "item": "wiki:custom_item",
            "count": 1
        },
        "unlock": [
            { "item": "minecraft:stick" }
        ]
    }
}
```

## 文件结构汇总

/// html | div.treeview
- `wiki_BP`
    - `items`
        - `custom_item.json`
    - `recipes`
        - `custom_item.json`
- `wiki_RP`
    - `textures`
        - `items`
            - `custom_item.png`
        - `item_texture.json`
    - `texts`
        - `zh_CN.lang`
///

到这里你已经掌握了：

- [x] 物品定义的基本格式
- [x] `menu_category`的配置方式
- [x] 图标短名与`item_texture.json`的关系
- [x] 语言文件的本地化方式
- [x] 无序配方的写法

接下来可以继续阅读[物品组件概览](item-components.md)，了解所有可用组件的功能与用法。
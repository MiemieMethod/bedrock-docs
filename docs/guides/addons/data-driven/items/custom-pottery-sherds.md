# 自定义陶片

陶片（pottery sherd）是可以用于合成装饰陶罐的物品。自定义陶片需要在物品上添加特定标签，并在客户端实体中注册图案纹理。

## 物品定义

自定义陶片的关键在于添加`minecraft:decorated_pot_sherds`标签：

```json title="BP/items/my_sherd.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:my_sherd",
            "menu_category": {
                "category": "items"
            }
        },
        "components": {
            "minecraft:icon": "wiki:my_sherd",
            "minecraft:tags": {
                "tags": [
                    "minecraft:decorated_pot_sherds"
                ]
            }
        }
    }
}
```

有了`minecraft:decorated_pot_sherds`标签，该物品便可以被放入装饰陶罐的合成格，使陶罐侧面显示对应图案。

## 注册图标

```json title="RP/textures/item_texture.json"
{
    "texture_data": {
        "wiki:my_sherd": {
            "textures": "textures/items/my_sherd"
        }
    }
}
```

## 图案纹理

陶罐侧面显示的图案来自一张单独的纹理，需要注册到客户端实体`decorated_pot`中：

### 注册图案纹理

在资源包中创建或编辑玩家文件（或通过附加文件包含）来覆盖装饰陶罐的客户端实体定义，在其`textures`字段中添加自定义图案：

```json title="RP/entity/decorated_pot.entity.json（节选）"
{
    "format_version": "1.10.0",
    "minecraft:client_entity": {
        "description": {
            "identifier": "minecraft:decorated_pot",
            "textures": {
                "default": "textures/entity/decorated_pot/decorated_pot_base",
                "cracked": "textures/entity/decorated_pot/decorated_pot_cracked",
                "wiki_sherd": "textures/entity/decorated_pot/my_sherd_pattern"
            }
        }
    }
}
```

/// warning | 注意
直接覆盖原版`decorated_pot.entity.json`会替换原版定义，请确保保留原版所有纹理条目，仅追加自定义纹理。否则原版图案将失效。
///

### 图案纹理文件

将图案纹理PNG放在相应路径：

```
RP/textures/entity/decorated_pot/my_sherd_pattern.png
```

图案纹理的尺寸和布局应与原版陶片图案纹理一致（16×16或更高分辨率的等比放大版本）。

<!-- 截图：展示原版陶片图案纹理（textures/entity/decorated_pot/*.png）的布局，标注图案区域 -->

## 显示名称

陶片的显示名称键名格式略有不同，需使用`item.<id>.name`：

```lang title="RP/texts/zh_CN.lang"
item.wiki:my_sherd.name=神秘陶片
```

## 测试

通过`/give @s wiki:my_sherd`获取陶片，然后在合成台中将4块砖（brick）和陶片按如下布局合成装饰陶罐：

```
    [陶片]
[砖]      [砖]
    [砖]
```

放置后观察陶罐侧面是否显示自定义图案。
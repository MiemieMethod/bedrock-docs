---
title: Minecraft Beta & Preview - 1.21.40.22
date: 2024-09-18T13:35:17Z
updated: 2024-09-18T13:47:03Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/30356048742413-Minecraft-Beta-Preview-1-21-40-22
---

**发布时间：** 2024年9月18日

**关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)获取详细说明

![p21U4_3_opt2.jpg](https://feedback.minecraft.net/hc/article_attachments/30356044598541)

是时候进行新的Minecraft预览版和测试版了！你会兴奋地知道，附加包现在可以染色；启用附加包实验来测试这一功能！我们始终希望听到你的反馈，请通过 <https://aka.ms/mcbundlesfeedback>告诉我们你的想法，并在 [bugs.mojang.com](http://bugs.mojang.com/)报告任何漏洞。

# 实验性功能

## 物品

- 附加包现在可以使用染料染成16种不同的颜色

# 功能和漏洞修复

## Android

- 修复了在某些游戏手柄上使用模拟触发器时的双重输入问题 ([MCPE-175113](https://bugs.mojang.com/browse/MCPE-175113))

## 游戏玩法

- 玩家被重锤的猛击攻击击杀时，现在会收到正确的死亡信息 ([MCPE-185952](https://bugs.mojang.com/browse/MCPE-185952))
- 修复了可能导致玩家无法正确重生的问题 ([MCPE-186324](https://bugs.mojang.com/browse/MCPE-186324))
- TNT爆炸不再重置其他掉落的被激活TNT的动量。这应该修复与TNT炮相关的任何问题 ([MCPE-181055](https://bugs.mojang.com/browse/MCPE-181055))

## 生物

- 旋风人如果在蜂蜜块上方，则不再能跳离玩家 ([MCPE-176991](https://bugs.mojang.com/browse/MCPE-176991))
- 由下界传送门生成的僵尸猪灵现在在使用传送门之前有15秒的冷却时间

## 生物群系

- 跳跃提升现在增加旋风人可以跳跃的高度 ([MCPE-176922](https://bugs.mojang.com/browse/MCPE-176922))
- 修复了矿车意外停止并且只能向一个方向推动的问题 ([MCPE-185643](https://bugs.mojang.com/browse/MCPE-185643))
- 更新了蝙蝠在世界中生成的规则：
  - 蝙蝠现在可以在任何高度生成，只要该区域被覆盖且足够黑暗
  - 蝙蝠必须在以下方块之一上生成：石头、花岗岩、闪长岩、安山岩、凝灰岩或深板岩
  - 因此，蝙蝠现在可能会在地表上方生成

## 领域

- 添加了一个新的领域事件。你能找出它是什么吗？

## 用户界面

- 在创造模式中，单击摧毁现在可以与摇杆/十字准星控制一起使用，而不会导致方块出现故障 ([MCPE-181789](https://bugs.mojang.com/browse/MCPE-181789))
- 修复了领域邀请链接可能溢出文本框的漏洞
- 在从配方界面丢弃相同物品后，物品不再卡在合成网格中 ([MCPE-73593](https://bugs.mojang.com/browse/MCPE-73593))
- 修复了在某些情况下新床界面不会完全朗读的问题（仅限预览版）
- 修复了实验性床界面在禁用屏幕动画时缺少覆盖层的漏洞（仅限预览版） ([MCPE-184090](https://bugs.mojang.com/browse/MCPE-184090))
- 当使用游戏手柄选择附加包中的物品时，从附加包中取出功能现在优先于清空快捷栏 ([MCPE-186359](https://bugs.mojang.com/browse/MCPE-186359))
- 物品栏界面不再在提示框中显示物品类别，除非配方书搜索界面实际可见 ([MCPE-128464](https://bugs.mojang.com/browse/MCPE-128464))
- 在使用触控控制的交换跳跃和潜行选项时，潜行按钮在你靠近按下时不再闪烁 ([MCPE-159557](https://bugs.mojang.com/browse/MCPE-159557))

## 原版趋同

- 相同的磁石指针物品现在可以堆叠到64个，匹配Java版 ([MCPE-109595](https://bugs.mojang.com/browse/MCPE-109595))

# 技术更新

## API

- 修复了一些情况下`entityRemove`世界事件有时不会被触发
- 将`getRedstonePower`从`beta`移动到`1.15.0`

## 方块

- 更新了拼图方块
  - 修复了按下“完成”时方块数据不会保存的漏洞 ([MCPE-181405](https://bugs.mojang.com/browse/MCPE-181405))
  - 更新了拼图方块用户界面
  - 添加了选择优先级和放置优先级字段

## 相机

- `minecraft:follow_orbit`预设不再处于实验性切换后面

## 组件

- 将“minecraft:redstone_conductivity”组件移出即将到来的创作者功能实验，适用于格式版本1.21.30及以上

## 实体组件

- “behavior.jump_around_target”不再能被位于蜂蜜块上的实体使用 ([MCPE-176991](https://bugs.mojang.com/browse/MCPE-176991))
- 跳跃提升现在增加实体在使用“behavior.jump_around_target”时的跳跃高度 ([MCPE-176922](https://bugs.mojang.com/browse/MCPE-176922))
- 风弹现在使用`minecraft:explode`组件，而不是`minecraft:wind_burst`。
- 扩展了`minecraft:explode`，新增以下字段：
  - `damage_scaling`：应用于爆炸对实体造成的伤害的缩放因子。值为0时，爆炸不会造成任何伤害。负值会使爆炸治愈实体
  - `toggles_blocks`：如果为真，爆炸将切换爆炸半径内的方块
  - `knockback_scaling`：应用于爆炸造成的击退力的缩放因子
  - `particle_effect`：要使用的粒子效果的名称。接受的字符串为`wind_burst`或`breeze_wind_burst`。所有其他输入将使用默认的爆炸粒子
  - `sound_effect`：爆炸触发时播放的声音效果的名称
  - `negates_fall_damage`：定义爆炸是否应对碰撞点上方的玩家应用跌落伤害抵消
  - `allow_underwater`：如果为真，爆炸将影响水下的方块和实体

## 图形

- 从基础游戏版本1.21.40开始，将不再加载内置的biomes_client.json文件。其他包中的该文件将继续加载。水和迷雾设置现在在资源包中的单独client_biome.json文件中。当biomes_client.json和单独的client_biome.json文件指定竞争值时，来自创作者内容的加载biomes_client.json将优先

## 方块

- 修复了旧方块ID错误覆盖来自blocks.json格式版本1.21.20或更高的新方块ID数据的漏洞 ([MCPE-186255](https://bugs.mojang.com/browse/MCPE-186255))
- 更新了行为包颜色配方文件中对旧方块名称的引用
- 更新了行为包地物文件中对旧方块名称的引用
- 更新了生物群系定义文件中对旧方块名称的引用

# 技术实验性更新

## 附加包和脚本引擎

- 添加对具有“minecraft:block_placer”物品组件的自定义物品的支持，以使用引用的“block”作为物品的图标
  - 如果指定了“minecraft:icon”组件，则将覆盖“block”图标
  - 需要“即将到来的创作者功能”切换。必须使用物品json版本`1.21.40`或更高

## API

- 将`PlayerInteractWithBlockBeforeEvent`和`PlayerInteractWithBlockAfterEvent`从`beta`移动到`1.15.0`
- 将`PlayerInteractWithEntityBeforeEvent`和`PlayerInteractWithEntityAfterEvent`从`beta`移动到`1.15.0`
- 添加枚举`PlatformType`导出枚举PlatformType { Console = 'Console', Desktop = 'Desktop', Mobile = 'Mobile', } 类`ScriptClientSystemInfo`
  - 添加字段`platformType`
  - 添加字段`maxRenderDistance`

## 相机

- 向“新第三人称预设”实验性切换添加相机相对移动
  - 相机相对移动在任何继承自`minecraft:follow_orbit`并将`align_camera_and_target_forward`设置为`false`的相机上启用

## 图形

- 更新了一些Deferred Technical Preview资源包的JSON架构。创作者必须将他们的包更新为新格式。创作者学习门户上的文档将相应更新
  - 将`lighting/global.json`的内容拆分为3个文件：`lighting/global.json`、`point_lights/global.json`和`pbr/global.json`。它们分别包含方向光+自发光去饱和、点光源颜色和MERS回退
  - `lighting/global.json`的架构现在被包装在一个新的`"minecraft:lighting_settings"`对象中，并且还需要一个`"description"`对象，包含一个`"identifier"`字符串，以作为设置的唯一名称。`"format_version"`字段也已修改为需要一个字符串，而不是整数数组，并且必须使用版本`"1.21.40"`
  - 大气散射文件的文件路径已重新定位到`atmospherics/atmospherics.json`
  - `atmospherics/atmospherics.json`的架构现在被包装在一个新的`"minecraft:atmosphere_settings"`对象中，并且还需要一个`"description"`对象，包含一个`"identifier"`字符串，以作为设置的唯一名称。它还需要一个`"format_version"`字符串，必须是版本`"1.21.40"`
  - `color_grading/color_grading.json`的架构现在需要一个`"format_version"`字符串，必须是版本`"1.21.40"`
  - `water/water.json`的架构现在需要一个`"format_version"`字符串，必须是版本`"1.21.40"`

``` code-line
"lighting/global.json"
{
    "minecraft:lighting_settings": {
        "format_version": "1.21.40",
        "description": {
            "identifier": string
        },
        "directional_lights": {
            "sun": {
                "illuminance": float,
                "color": RGB color
            },
            "moon": {
                "illuminance": float,
                "color": RGB color
            },
            "orbital_offset_degrees": float
        },
        "emissive": {
            "desaturation": float
        }
    }
}
"point_lights/global.json"
{
    "minecraft:point_light_settings": {
        "format_version": "1.21.40",
        "colors": {
            "minecraft:block_name": RGB color,
            ...
        }
    }
}
"pbr/global.json"
{
    "minecraft:pbr_fallback_settings": {
        "format_version": "1.21.40",
        "blocks": {
            "global_metalness_emissive_roughness_subsurface": RGBA color
        },
        "actors": {
            "global_metalness_emissive_roughness_subsurface": RGBA color
        },
        "particles": {
            "global_metalness_emissive_roughness_subsurface": RGBA color
        },
        "items": {
            "global_metalness_emissive_roughness_subsurface": RGBA color
        }
    }
}
"atmospherics/atmospherics.json"
{
    "minecraft:atmosphere_settings": {
        "format_version": "1.21.40",
        "description": {
            "identifier": string
        },
        ...
    }
}
"color_grading/color_grading.json"
{
    "minecraft:color_grading_settings": {
        "format_version": "1.21.40",
        "description": {
            "identifier": string
        },
        ...
    }
}
"water/water.json"
{
    "minecraft:water_settings": {
        "format_version": "1.21.40",
        "description": {
            "identifier": string
        },
        ...
    }
}
```

## Molang

添加了`query.client_max_render_distance`。它返回当前客户端的最大渲染距离（以区块为单位）。仅在客户端（资源包）上可用
# 使用并自定义延迟渲染<!-- md:flag vanilla -->

国际版的新主线图形能力现在以Vibrant Visuals和PBR资源包为中心。旧文档里常说的“延迟渲染技术预览”仍有兼容性价值，但新项目应尽量按Vibrant Visuals资源包思路组织文件。

这一页先做一个最小PBR包，再说明如何逐步加入光照、天空、水和色彩设置。

## 准备资源包

先准备一个普通资源包，并在`manifest.json`中加入`"pbr"`功能声明。Microsoft Learn的Vibrant Visuals资源包文档要求`min_engine_version`至少为`[1, 21, 120]`。

```json
{
  "format_version": 1,
  "header": {
    "name": "guide.pbr_pack.name",
    "description": "guide.pbr_pack.description",
    "uuid": "00000000-0000-0000-0000-000000000001",
    "version": [1, 0, 0],
    "min_engine_version": [1, 21, 120]
  },
  "modules": [
    {
      "type": "resources",
      "uuid": "00000000-0000-0000-0000-000000000002",
      "version": [1, 0, 0]
    }
  ],
  "capabilities": [
    "pbr"
  ]
}
```

/// warning | `pbr`和`raytraced`
官方文档建议Vibrant Visuals资源包使用`"pbr"`。带`"raytraced"`能力的旧RTX包也能激活Vibrant Visuals，但RTX受设备限制更大，新包不建议只按RTX思路制作。
///

## 给一个方块添加PBR纹理

以铁块为例，在`textures\blocks`中放置颜色纹理和MER纹理：

/// html | div.treeview
- RP
    - textures
        - blocks
            - {/{file|iron_block.png}}
            - {/{file|iron_block_mer.png}}
            - {/{file|iron_block.texture_set.json}}
///

`iron_block.texture_set.json`可以这样写：

```json
{
  "format_version": "1.16.100",
  "minecraft:texture_set": {
    "color": "iron_block",
    "metalness_emissive_roughness": "iron_block_mer"
  }
}
```

MER纹理的通道含义如下：

| 通道 | 含义 | 越亮表示 |
| --- | --- | --- |
| 红色 | 金属度 | 越像金属 |
| 绿色 | 自发光 | 越亮、越发光 |
| 蓝色 | 粗糙度 | 越粗糙、反射越模糊 |

如果面向Vibrant Visuals并需要次表面散射，可以把`metalness_emissive_roughness`改为`metalness_emissive_roughness_subsurface`并提供RGBA图像；其中Alpha通道表示次表面散射。不要在同一个纹理集中同时定义MER和MERS。

## 启用图形模式

在正式版支持Vibrant Visuals的环境中：

1. 打开**Settings**。
2. 进入**Video**。
3. 在**Graphics Mode**中勾选**Vibrant Visuals**。
4. 进入世界并启用你的资源包。

在仍使用技术预览开关的环境中：

1. 创建世界时打开实验性玩法中的**Render Dragon Features for Creators**。
2. 启用PBR资源包。
3. 进世界后到视频设置中勾选**Deferred Technical Preview**。

/// note | 技术预览硬件要求
官方旧文档说明延迟渲染不要求光线追踪显卡；Windows上的现代GPU大多可尝试。Android端曾要求GLES3.1设备并运行Android9或更高系统。实际可用性以当前游戏版本显示的图形选项为准。
///

## 加入全局光照

光照设置可放在`lighting\global.json`。下面的例子只保留最基本结构：

```json
{
  "format_version": "1.21.70",
  "minecraft:lighting_settings": {
    "description": {
      "identifier": "guide:default_lighting"
    },
    "directional_lights": {
      "orbital": {
        "sun": {
          "illuminance": 100000.0,
          "color": "#FFFFFF"
        },
        "moon": {
          "illuminance": 0.27,
          "color": "#DDE8FF"
        },
        "orbital_offset_degrees": 0.0
      }
    },
    "ambient": {
      "illuminance": 0.02,
      "color": "#FFFFFF"
    },
    "sky": {
      "intensity": 1.0
    }
  }
}
```

太阳照度可以按现实值写得很高，因为管线会通过色调映射和自动曝光处理高动态范围。调试时每次只改一组参数，例如只改太阳颜色或只改环境光亮度。

/// note | 生物群系光照覆盖
Microsoft Learn说明，自基岩版1.21.90起，`lighting\global.json`不会覆盖内置原版包的每生物群系光照；若要覆盖这类光照，应在`lighting`目录中创建多个光照JSON文件并分配给对应生物群系。
///

## 用关键帧控制一天变化

支持`optkeyframe`的字段可以从单个值改成按时间插值的对象。关键帧键从`0`到`1`，官方文档中`0.0`和`1.0`代表正午，`0.25`代表日落，`0.5`代表午夜，`0.75`代表日出。

```json
"illuminance": {
  "0.0": 100000.0,
  "0.25": 20000.0,
  "0.5": 1.0,
  "0.75": 20000.0,
  "1.0": 100000.0
}
```

## 继续扩展

完成最小PBR包后，可以逐步添加：

- `local_lighting\local_lighting.json`：给火把、灯笼或自定义发光方块指定静态光或点光源颜色。
- `pbr\global.json`：给没有纹理集的方块、实体、粒子和物品提供统一PBR后备值。
- `atmospherics\atmospherics.json`：控制天空、大气散射和地平线颜色。
- `water\water.json`：控制水体粒子浓度、波浪和焦散。
- `color_grading\*.json`：控制饱和度、对比度、增益、偏移和色调映射。

每加一种文件都先用小范围世界测试。渲染问题常常来自数值范围或资源包栈覆盖，而不是语法错误。

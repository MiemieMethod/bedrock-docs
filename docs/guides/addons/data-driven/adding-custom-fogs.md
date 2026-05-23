# 自定义迷雾

迷雾定义属于资源包，放在`fogs`目录中。它可以控制空气、水、天气、熔岩和粉雪等环境中的距离迷雾，也可以为光线追踪或鲜艳视觉相关效果提供体积迷雾参数。

## 创建迷雾文件

```json title="demo_RP/fogs/demo_blue.json"
{
  "format_version": "1.16.100",
  "minecraft:fog_settings": {
    "description": {
      "identifier": "demo:blue_fog"
    },
    "distance": {
      "air": {
        "fog_start": 0.25,
        "fog_end": 0.75,
        "fog_color": "#88AAFF",
        "render_distance_type": "render"
      },
      "water": {
        "fog_start": 0,
        "fog_end": 40,
        "fog_color": "#3355AA",
        "render_distance_type": "fixed",
        "transition_fog": {
          "init_fog": {
            "fog_start": 0,
            "fog_end": 2,
            "fog_color": "#88AAFF",
            "render_distance_type": "fixed"
          },
          "min_percent": 0.25,
          "mid_seconds": 5,
          "mid_percent": 0.6,
          "max_seconds": 30
        }
      }
    }
  }
}
```

`render_distance_type`为`render`时，开始和结束值会按当前渲染距离比例计算；为`fixed`时，值按方块距离计算。

`fog_start`是迷雾开始出现的位置，`fog_end`是迷雾完全不透明的位置，`fog_color`是迷雾颜色。建议先给`fog_color`设置明显的十六进制颜色，确认迷雾确实被加载后再细调。

/// note | 水下过渡
`transition_fog`只适用于`water`迷雾。玩家进入水中时，游戏会从`init_fog`逐渐过渡到当前水下迷雾；`min_percent`、`mid_seconds`、`mid_percent`和`max_seconds`用于控制这个过渡进度。
///

## 应用迷雾

测试时可以使用`/fog`命令把迷雾加入玩家的迷雾栈。示例：

```mcfunction
/fog @s push demo:blue_fog demo_test
```

同一个玩家可以被推入多个命令层迷雾。游戏会从命令层顶部向下查找字段；如果上层迷雾没有设置某个字段，就继续使用下层迷雾、生物群系迷雾、默认数据或引擎默认值。移除时使用同一个用户提供ID：

```mcfunction
/fog @s remove demo_test
```

如果只想弹出命令层顶部匹配`demo_test`的那一项，也可以使用：

```mcfunction
/fog @s pop demo_test
```

迷雾也可以由生物群系或功能域等系统应用。不同来源会组成活动迷雾栈；某个字段未设置时，游戏会使用下一个较低优先级迷雾的值。

## 绑定到生物群系

如果迷雾用于生物群系视觉效果，需要在资源包根目录的`biomes_client.json`中引用它：

```json title="demo_RP/biomes_client.json"
{
  "biomes": {
    "default": {
      "fog_identifier": "demo:blue_fog"
    }
  }
}
```

为某个具体生物群系设置迷雾时，把`default`替换为该生物群系的客户端条目即可。`default`条目会作为数据默认层参与迷雾栈，不会阻止具体生物群系设置覆盖它已经定义的字段。

## 添加体积迷雾

如果目标资源包需要光线追踪或鲜艳视觉相关效果，可以在同一个迷雾文件中添加`volumetric`对象：

```json title="demo_RP/fogs/demo_blue.json"
{
  "format_version": "1.16.100",
  "minecraft:fog_settings": {
    "description": {
      "identifier": "demo:blue_fog"
    },
    "volumetric": {
      "density": {
        "air": {
          "max_density": 0.01,
          "zero_density_height": 150,
          "max_density_height": 50
        },
        "water": {
          "max_density": 0.25,
          "uniform": true
        }
      },
      "media_coefficients": {
        "air": {
          "scattering": [0.02, 0.02, 0.02],
          "absorption": [0.0, 0.0, 0.0]
        },
        "water": {
          "scattering": [0.01811, 0.02126, 0.027953],
          "absorption": [0.2, 0.07874, 0.083465]
        }
      }
    }
  }
}
```

`density`控制雾对光线的遮蔽强度。`media_coefficients`控制光线在空气、水和云等介质中的散射与吸收。对于普通距离迷雾，先只写`distance`就足够；需要体积效果时再加入`volumetric`，这样更容易排查问题。

## 常见调整

- 空气迷雾：调`air.fog_start`和`air.fog_end`。
- 水下迷雾：调`water`，必要时使用`transition_fog`控制进入水中的过渡。
- 天气迷雾：调`weather`。
- 熔岩迷雾：调`lava`和`lava_resistance`。
- 粉雪迷雾：调`powder_snow`。
- 体积迷雾：先调`density.*.max_density`，再调`media_coefficients`。

如果你修改后完全看不到效果，先检查三个位置：文件是否在资源包`fogs/`目录下，`description.identifier`是否带有命名空间，`/fog`命令或`biomes_client.json`引用的标识符是否与文件中一致。

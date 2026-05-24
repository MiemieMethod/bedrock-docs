# 自定义粒子

自定义粒子适合制作魔法、烟雾、火花、气泡、环境氛围、实体状态和命中特效。粒子文件属于资源包，放在`particles`目录中，并通过粒子标识符被命令、实体动画、动画控制器或脚本API调用。

## 准备文件

资源包中的最小结构如下：

/// html | div.treeview
- `demo_RP`
    - `manifest.json`
    - `particles`
        - `colored_smoke.json`
    - `textures`
        - `particle`
            - `particles.png`
///

粒子定义中的`identifier`才是调用粒子时使用的名称。文件名和子目录只负责组织文件，不会自动成为粒子标识符。

## 编写基础粒子

下面的示例创建一个短暂的彩色烟雾粒子。它使用一次性发射器、点形状、动态运动、公告板外观和颜色渐变。

```json title="particles/colored_smoke.json"
{
  "format_version": "1.10.0",
  "particle_effect": {
    "description": {
      "identifier": "demo:colored_smoke",
      "basic_render_parameters": {
        "material": "particles_blend",
        "texture": "textures/particle/particles"
      }
    },
    "components": {
      "minecraft:emitter_rate_instant": {
        "num_particles": 8
      },
      "minecraft:emitter_lifetime_once": {
        "active_time": 0.1
      },
      "minecraft:emitter_shape_point": {
        "direction": [0, 1, 0]
      },
      "minecraft:particle_lifetime_expression": {
        "max_lifetime": "math.random(0.8, 1.4)"
      },
      "minecraft:particle_initial_speed": "math.random(0.6, 1.2)",
      "minecraft:particle_motion_dynamic": {
        "linear_acceleration": [0, 0.6, 0],
        "linear_drag_coefficient": 1.5
      },
      "minecraft:particle_appearance_billboard": {
        "size": [
          "0.15 + variable.particle_age * 0.25",
          "0.15 + variable.particle_age * 0.25"
        ],
        "facing_camera_mode": "lookat_xyz",
        "uv": {
          "texture_width": 128,
          "texture_height": 128,
          "uv": [0, 24],
          "uv_size": [8, 8]
        }
      },
      "minecraft:particle_appearance_tinting": {
        "color": {
          "gradient": {
            "0.0": "#66AAFFFF",
            "0.7": "#AA66AA88",
            "1.0": "#00000000"
          },
          "interpolant": "variable.particle_age / variable.particle_lifetime"
        }
      }
    }
  }
}
```

粒子中的距离使用米，时间使用秒，速度使用米每秒，加速度使用米每二次方秒。旋转和三角函数使用度。

## 选择材质

常用材质有三种：

| 材质 | 适用场景 |
| --- | --- |
| `particles_alpha` | 像素只有完全透明或不透明两类结果，适合边缘明确的粒子。 |
| `particles_blend` | 支持普通透明混合，适合烟雾、气泡和柔和光效。 |
| `particles_add` | 使用加法混合，适合火花、魔法、发光和能量效果。 |

如果粒子完全不可见，优先检查材质、纹理路径、UV区域和资源包是否启用。

## 用命令测试

进入启用资源包的世界后，可以使用`/particle`测试粒子：

```mcfunction
/particle demo:colored_smoke ~ ~1 ~
```

粒子是客户端效果。命令在服务端执行，而粒子资源在客户端解析；当标识符不存在、资源包未启用或纹理缺失时，服务端不一定能给出有用错误。调试时应同时查看内容日志。

## 挂接到实体

若要在实体动画或动画控制器中播放粒子，先在客户端实体定义中注册短名称：

```json title="client_entity片段"
"particle_effects": {
  "smoke": "demo:colored_smoke"
}
```

然后在动画时间轴中触发：

```json title="animation片段"
"particle_effects": {
  "0.0": [
    {
      "effect": "smoke"
    }
  ]
}
```

也可以在动画控制器状态中持续播放。状态进入时会启动粒子效果，状态退出时仍在持续的效果会被终止：

```json title="animation_controller片段"
"particle_effects": [
  {
    "effect": "smoke",
    "locator": "head"
  }
]
```

`locator`引用客户端实体定义和几何体中的定位器。未设置定位器时，粒子通常从实体原点播放。

## 调整粒子行为

制作粒子时可以按下列顺序排查和调参：

1. 先让粒子在命令中可见，确认标识符、材质、纹理和UV正确。
2. 再调整发射率和生命周期，决定粒子数量与持续时间。
3. 调整发射器形状和初始速度，决定粒子从哪里出现、向哪里扩散。
4. 调整运动组件，加入加速度、阻力、旋转或碰撞。
5. 调整公告板、颜色、透明度和翻书动画，使视觉效果符合预期。
6. 最后接入实体动画、动画控制器、事件或脚本API。

## 建议使用Snowstorm

手写粒子JSON容易在组件名、UV、颜色和Molang表达式上出错。Snowstorm能实时预览发射器、粒子寿命、运动、纹理、颜色和翻书动画，适合先制作效果，再把JSON放回资源包。

## 延伸阅读

- [粒子](../../../docs/addon/particle.md)
- [粒子发射器](../../../docs/addon/particle-emitter.md)
- [粒子定义](../../../refs/addon/particle.md)
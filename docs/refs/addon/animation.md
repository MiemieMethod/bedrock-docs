# 动画定义

本页列出国际版资源包和行为包`animations/`目录中动画定义文件的主要结构。资源包动画用于客户端实体模型的骨骼变换；行为包动画可用于服务端逻辑，不直接产生视觉模型运动。本页不包含中国版网易ModSDK接口。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 动画定义文件使用的格式版本。官方参考建议使用`1.8.0`或更高版本。 |
| `animations` | 对象 | 未设置 | 动画定义字典。键为动画标识符，值为动画对象。 |

## 动画对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `loop` | 布尔值或字符串 | 未设置 | 控制动画是否循环，或是否在播放结束后保持最后一帧。可取`true`（循环）、`false`（停止）或字符串`"hold_on_last_frame"`（停留在最后一帧）。 |
| `animation_length` | 数值 | 未设置 | 动画长度，单位为秒。若未设置，则由最大关键帧或事件时间点自动计算。 |
| `anim_time_update` | Molang表达式 | 未设置 | 控制动画时间如何更新。默认为`query.anim_time + query.delta_time`，即按秒数推进。原版四足动物行走动画常使用`query.modified_distance_moved`按移动距离推进动画。 |
| `start_delay` | Molang表达式 | 未设置 | 动画首次播放前等待的秒数。该表达式在动画开始前求值一次，仅在动画被要求从头重新播放时才重新求值。循环动画如需每次循环间有延迟，应使用`loop_delay`。 |
| `loop_delay` | Molang表达式 | 未设置 | 每次循环后等待的秒数。仅对循环动画有效，每次循环结束后求值一次。 |
| `blend_weight` | Molang表达式 | 未设置 | 动画的融合权重。 |
| `override_previous_animation` | 布尔值 | `false` | 设为`true`时，在应用本动画前将所有骨骼重置到几何体定义中的默认姿势，而非在前序动画结果上叠加。 |
| `bones` | 对象 | 未设置 | 按骨骼名称索引的骨骼变换定义。 |
| `timeline` | 对象 | 未设置 | 按时间点触发的Molang表达式或服务端动作。 |
| `particle_effects` | 对象 | 未设置 | 按时间点触发的粒子特效。 |
| `sound_effects` | 对象 | 未设置 | 按时间点触发的音效。 |

## 骨骼变换

`bones`对象的键为模型骨骼名称。每个骨骼支持以下字段：

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `position` | Molang表达式、数组或关键帧对象 | 骨骼位置变换，对应x、y、z三轴偏移。 |
| `rotation` | Molang表达式、数组或关键帧对象 | 骨骼旋转变换，对应x、y、z三轴旋转角度。 |
| `scale` | Molang表达式、数组或关键帧对象 | 骨骼缩放变换，对应x、y、z三轴缩放比例。 |
| `relative_to` | 对象 | 指定变换参考空间。当前支持将`rotation`设为字符串`"entity"`，使骨骼旋转相对于实体自身而非父骨骼。 |

`position`、`rotation`和`scale`各有三种写法：

- **Molang表达式**：单个表达式，应用于所有轴（`scale`）或写法上等同于x轴（`position`、`rotation`）。
- **三元素数组**：`[x, y, z]`，每个元素可为数值或Molang表达式。
- **关键帧对象**：键为秒数时间戳，值为以下两种之一：
  - **三元素数组**：该时间点的数值。
  - **关键帧详情对象**：包含`lerp_mode`（插值模式，可选）、`pre`（关键帧前取值数组，可选）和`post`（关键帧后取值数组，可选）。

```json title="骨骼变换示例"
{
  "rotation": [
    "math.cos(query.anim_time * 38.17) * 80.0",
    0.0,
    0.0
  ]
}
```

```json title="关键帧写法示例"
{
  "rotation": {
    "0.0": [0.0, 0.0, 0.0],
    "0.5": {
      "lerp_mode": "catmullrom",
      "pre": [0.0, 45.0, 0.0],
      "post": [0.0, 45.0, 0.0]
    },
    "1.0": [0.0, 0.0, 0.0]
  }
}
```

## 粒子特效与音效时间轴

`particle_effects`对象按动画时间点触发粒子特效。键为秒数形式的时间点，值可为单个粒子效果对象或粒子效果对象数组。粒子效果对象包含以下字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `effect` | 字符串 | 未设置 | 客户端实体定义`description.particle_effects`中声明的粒子短名称。 |
| `locator` | 字符串 | 未设置 | 可选。粒子发射器跟随的定位器短名称。 |
| `pre_effect_script` | Molang表达式 | 未设置 | 可选。发射器启动时执行的表达式，可为粒子定义初始化变量。 |
| `bind_to_actor` | 布尔值 | `true` | 设为`false`时，粒子效果以世界坐标生成，不绑定到实体。默认绑定到实体。 |

动画时间轴触发的粒子特效属于即发即忘效果。若需要随状态持续并在状态退出时结束，通常应使用动画控制器状态中的`particle_effects`。

`sound_effects`使用相似的时间点结构触发音效。每个时间点的值为包含`effect`字段的对象，`effect`对应实体资源定义文件中列出的音效名称。

## 求值规则

- 每帧开始时，实体骨架会先重置到几何体定义中的默认姿势。
- 动画按挂接顺序应用到骨骼上。
- 位置、旋转和缩放的x、y与z通道先分别累积，再转换为最终变换。
- 关键帧默认使用线性插值；当关键帧详情对象中指定`lerp_mode`为`"catmullrom"`时，使用Catmull-Rom样条插值。
- 关键帧的`pre`和`post`分别控制关键帧前后的切线取值，用于调整曲线形状。

## 示例

```json title="quadruped.animation.json节选"
{
  "format_version": "1.8.0",
  "animations": {
    "animation.quadruped.walk": {
      "anim_time_update": "query.modified_distance_moved",
      "loop": true,
      "bones": {
        "leg0": {
          "rotation": [
            "math.cos(query.anim_time * 38.17) * 80.0",
            0.0,
            0.0
          ]
        }
      }
    }
  }
}
```

## 挂接位置

动画标识符通常在客户端实体定义或行为包实体定义的`description.animations`中映射为短名称，并在`scripts.animate`或`animate`中播放。动画控制器状态中的`animations`数组也使用这些短名称。

## 相关参考

- [客户端实体定义](client-entity.md)
- [动画控制器](animation-controller.md)
- [粒子定义](particle.md)
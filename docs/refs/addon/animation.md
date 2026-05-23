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
| `loop` | 布尔值或字符串 | 未设置 | 控制动画是否循环，或是否在播放结束后保持最后一帧。 |
| `animation_length` | 数值 | 未设置 | 动画长度，单位为秒。 |
| `anim_time_update` | Molang表达式 | 未设置 | 控制动画时间如何更新。原版四足动物行走动画常使用`query.modified_distance_moved`按移动距离推进动画。 |
| `bones` | 对象 | 未设置 | 按骨骼名称索引的骨骼变换定义。 |
| `timeline` | 对象 | 未设置 | 按时间点触发的Molang表达式或服务端动作。 |
| `particle_effects` | 对象 | 未设置 | 按时间点触发的粒子特效。 |
| `sound_effects` | 对象 | 未设置 | 按时间点触发的音效。 |

## 骨骼变换

`bones`对象的键为模型骨骼名称。每个骨骼可定义`position`、`rotation`和`scale`三类变换。变换值通常使用三元素数组表示x、y和z通道，也可在通道中写入Molang表达式。

```json title="骨骼变换示例"
{
  "rotation": [
    "math.cos(query.anim_time * 38.17) * 80.0",
    0.0,
    0.0
  ]
}
```


## 粒子特效与音效时间轴

`particle_effects`对象按动画时间点触发粒子特效。键为秒数形式的时间点，值可为单个粒子效果对象或粒子效果对象数组。粒子效果对象通常包含以下字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `effect` | 字符串 | 未设置 | 客户端实体定义`description.particle_effects`中声明的粒子短名称。 |
| `locator` | 字符串 | 未设置 | 可选。粒子发射器跟随的定位器短名称。 |
| `pre_effect_script` | Molang表达式 | 未设置 | 可选。发射器启动时执行的表达式，可为粒子定义初始化变量。 |

动画时间轴触发的粒子特效属于即发即忘效果。若需要随状态持续并在状态退出时结束，通常应使用动画控制器状态中的`particle_effects`。

`sound_effects`使用相似的时间点结构触发音效短名称。

## 求值规则

- 每帧开始时，实体骨架会先重置到几何体定义中的默认姿势。
- 动画按挂接顺序应用到骨骼上。
- 位置、旋转和缩放的x、y与z通道先分别累积，再转换为最终变换。
- 当前官方动画参考记录关键帧仅支持线性插值。关键帧的`pre`和`post`设置用于控制关键帧前后的取值。

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

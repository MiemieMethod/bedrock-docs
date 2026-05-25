# 动画控制器

本页列出国际版资源包和行为包`animation_controllers/`目录中动画控制器定义文件的主要结构。动画控制器使用状态机决定何时播放哪些动画，也可以在动画控制器状态中引用其他动画控制器。本页不包含中国版网易ModSDK接口。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 动画控制器文件使用的格式版本。官方参考建议使用`1.10.0`或更高版本。 |
| `animation_controllers` | 对象 | 未设置 | 动画控制器定义字典。键为控制器标识符，值为控制器对象。 |

## 控制器对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `initial_state` | 字符串 | `default` | 控制器开始运行时进入的状态名称。未设置时通常使用`default`状态。 |
| `states` | 对象 | 未设置 | 状态定义字典。键为状态名称，值为状态对象。 |

## 状态对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `animations` | 数组 | 未设置 | 当前状态播放的动画或动画控制器短名称。数组元素可为字符串，或为“短名称到Molang表达式”的对象以指定融合权重。 |
| `transitions` | 数组 | 未设置 | 状态转移列表。数组元素为“目标状态到Molang表达式”的对象。 |
| `blend_transition` | 数值或对象 | 未设置 | 离开当前状态时的融合时长，单位为秒。数值形式指定固定秒数的线性融合；对象形式为以时间戳为键、以融合系数为值的重映射曲线，可实现自定义融合曲线。 |
| `blend_via_shortest_path` | 布尔值 | `false` | 设为`true`时，过渡到其他状态时各欧拉轴将沿最短旋转路径进行融合，而非直接按数值插值。 |
| `variables` | 对象 | 未设置 | 当前状态可供被引用动画使用的变量定义。 |
| `particle_effects` | 数组 | 未设置 | 状态进入时启动的粒子特效列表，状态退出时终止仍在持续的效果。 |
| `sound_effects` | 数组 | 未设置 | 状态进入时触发的音效列表。 |
| `on_entry` | 数组 | 未设置 | 进入该状态时执行的字符串数组，每个字符串可以是Molang表达式或以`/`开头的命令（斜杠命令）。 |
| `on_exit` | 数组 | 未设置 | 离开该状态时执行的字符串数组，格式与`on_entry`相同。 |

## 状态转移

`transitions`按数组顺序求值。每个转移包含一个目标状态和一个Molang条件表达式；条件返回非`0`值时立即切换到对应目标状态。每帧最多处理一个转移，因此列表中靠前的转移具有更高优先级。

```json title="状态转移示例"
{
  "default": {
    "animations": [
      "base_pose",
      "walk"
    ],
    "transitions": [
      { "angry": "query.is_angry" },
      { "tired": "variable.is_tired" }
    ],
    "blend_transition": 0.2
  }
}
```


## 状态效果

动画控制器状态可以通过`particle_effects`启动实体粒子特效。数组中的每一项包含以下字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `effect` | 字符串 | 未设置 | 客户端实体定义`description.particle_effects`中声明的粒子短名称。 |
| `locator` | 字符串 | 未设置 | 可选。粒子发射器跟随的定位器短名称。 |
| `pre_effect_script` | Molang表达式 | 未设置 | 可选。发射器启动时执行的表达式，可为粒子定义初始化变量。 |
| `bind_to_actor` | 布尔值 | `true` | 设为`false`时，粒子效果以世界坐标生成，不绑定到实体。默认绑定到实体。 |

与动画时间轴中的粒子不同，状态粒子会在进入状态时启动，并在离开状态时自动结束仍未自行终止的发射器。

## 变量定义

`variables`对象用于将Molang值注入到当前状态引用的动画中，以覆盖动画内部的默认求值。每个键为变量名（如`variable.foo`），值为包含以下字段的对象：

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `input` | Molang表达式 | 变量的输入源表达式。 |
| `remap_curve` | 对象 | 可选。以时间戳字符串为键、以目标值为值的重映射曲线。若设置，则在`input`结果上应用该曲线映射后再赋值。 |

## 示例

```json title="动画控制器示例"
{
  "format_version": "1.17.30",
  "animation_controllers": {
    "controller.animation.my_mob.move": {
      "initial_state": "moving",
      "states": {
        "moving": {
          "animations": [
            "wag_tail",
            "wiggle_ears",
            { "walk": "query.modified_move_speed" }
          ],
          "transitions": [
            { "grazing": "query.is_grazing" }
          ]
        },
        "grazing": {
          "animations": [ "grazing" ],
          "transitions": [
            { "moving": "query.all_animations_finished" }
          ]
        }
      }
    }
  }
}
```

## 挂接位置

动画控制器标识符通常在客户端实体定义或行为包实体定义的`description.animations`中映射为短名称，再在`scripts.animate`或`animate`中执行。控制器状态中的`animations`字段使用实体定义中的短名称，而不是直接使用全局动画标识符。

## 相关参考

- [动画定义](animation.md)
- [客户端实体定义](client-entity.md)
- [粒子定义](particle.md)
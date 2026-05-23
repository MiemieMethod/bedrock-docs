# JSON UI文件

本页列出国际版资源包`ui/`目录中JSON UI文件的主要结构和常用字段。资料来自Microsoft Learn的JSON UI参考。本页不包含中国版ModSDK UI接口、旧版中国版MC Studio界面工程格式或Ore UI。

/// warning | 枚举取值
Microsoft Learn本批次JSON UI参考列出了字段结构，但部分枚举表导出为`undefined`，没有公开具体取值。因此，本页不臆造枚举值；需要确定具体取值时，应结合目标版本的原版资源包、实际客户端测试和后续官方参考更新。
///

## 文件清单

| 文件 | 类型 | 描述 |
| --- | --- | --- |
| `ui/_ui_defs.json` | UI定义列表 | 列出需要加载的UI屏幕文件。 |
| `ui/_global_variables.json` | 全局变量表 | 定义跨屏幕复用的变量。 |
| `ui/*.json` | 屏幕文件 | 定义命名空间、控件、变量、绑定和交互映射。 |

## `_ui_defs.json`

`_ui_defs.json`用于声明游戏应加载的UI文件。`ui_defs`中的路径相对于资源包根目录，通常以`ui/`开头。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `ui_defs` | 字符串数组 | 未设置 | 需要加载的UI JSON文件路径列表。 |

```json title="ui/_ui_defs.json"
{
  "ui_defs": [
    "ui/my_screen.json",
    "ui/my_common_elements.json"
  ]
}
```

## `_global_variables.json`

`_global_variables.json`定义可被多个UI屏幕引用的全局变量。变量名必须以`$`开头。颜色值通常使用由`0.0`到`1.0`范围数值组成的RGB或RGBA数组。

| 示例变量 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `$background_color` | 值 | 未设置 | 背景颜色等全局颜色变量。 |
| `$button_text_color` | 值 | 未设置 | 按钮文本颜色等全局颜色变量。 |
| `$highlight_color` | 值 | 未设置 | 高亮颜色等全局颜色变量。 |

```json title="ui/_global_variables.json"
{
  "$button_text_color": [
    1,
    1,
    1
  ],
  "$background_color": [
    0.2,
    0.2,
    0.2,
    0.8
  ],
  "$highlight_color": [
    1,
    0.84,
    0
  ]
}
```

## 屏幕文件

屏幕文件定义完整界面布局。根对象中的`namespace`提供命名空间，其他键通常定义控件。控件名可以使用`@`语法继承其他命名空间或同一命名空间中的基控件。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `namespace` | 字符串 | 未设置 | 当前UI文件的命名空间。其他文件可以使用`namespace.element_name`语法引用其中的控件。 |
| 控件名 | 对象 | 未设置 | UI控件定义。键名可使用`element@base`形式表示继承。 |

```json title="ui/my_screen.json"
{
  "namespace": "my_screen",
  "main_panel": {
    "type": "panel",
    "size": [ "100%", "100%" ],
    "controls": [
      {
        "title_label": {
          "type": "label",
          "text": "Hello"
        }
      }
    ]
  }
}
```

## 控件字段

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `type` | 选项 | 未设置 | 控件类型，决定控件的渲染和行为。 |
| `controls` | 对象数组 | 未设置 | 子控件列表。 |
| `variables` | 对象 | 未设置 | 控件局部变量或带条件的变量项。 |
| `bindings` | 对象数组 | 未设置 | 数据绑定列表。 |
| `button_mappings` | 对象数组 | 未设置 | 输入按钮到动作按钮的映射列表。 |
| `visible` | 布尔值 | 未设置 | 控件默认是否可见。 |
| `enabled` | 布尔值 | 未设置 | 控件是否启用并可交互。 |
| `ignored` | 布尔值 | 未设置 | 为`true`时，控件在布局或渲染中被忽略。 |
| `alpha` | 数值 | 未设置 | 控件不透明度，`0.0`为完全透明，`1.0`为完全不透明。 |
| `propagate_alpha` | 布尔值 | 未设置 | 是否将透明度传播到子控件。 |
| `color` | 数值数组 | 未设置 | 应用于控件的颜色，通常为RGB数组。 |
| `grayscale` | 布尔值 | 未设置 | 是否以灰度渲染控件。 |
| `layer` | 整数 | 未设置 | 渲染图层。数值较大的控件通常位于较小图层上方。 |
| `renderer` | 字符串 | 未设置 | 自定义渲染器名称，例如原版资源中可见的物品或玩家渲染器。 |
| `factory` | 字符串 | 未设置 | 用于动态创建控件的工厂配置。 |
| `anchor_from` | 选项 | 未设置 | 父控件上用于定位的锚点。 |
| `anchor_to` | 选项 | 未设置 | 当前控件上用于对齐的锚点。 |
| `offset` | 数组 | 未设置 | 相对于锚点的位置偏移，通常为`[x,y]`。 |
| `size` | 数组 | 未设置 | 控件尺寸。元素可为像素数值、百分比字符串或特殊尺寸值。 |
| `min_size` | 数组 | 未设置 | 控件最小尺寸。 |
| `max_size` | 数组 | 未设置 | 控件最大尺寸。 |
| `keep_ratio` | 布尔值 | 未设置 | 缩放时是否保持宽高比例。 |
| `allow_clipping` | 布尔值 | 未设置 | 是否允许控件被父控件裁切。 |
| `clip_pixelperfect` | 布尔值 | 未设置 | 是否使用像素精确裁切。 |
| `clips_children` | 布尔值 | 未设置 | 是否将子控件裁切在当前控件范围内。 |
| `orientation` | 选项 | 未设置 | 栈面板等控件排列子控件的方向。 |
| `grid_dimension_binding` | 字符串 | 未设置 | 用于决定网格尺寸的绑定。 |
| `grid_item_template` | 整数 | 未设置 | 网格项目使用的模板控件。 |
| `grid_rescaling_type` | 选项 | 未设置 | 网格调整单元格尺寸的方式。 |
| `collection_name` | 字符串 | 未设置 | 网格或栈面板项目使用的集合名称。 |
| `texture` | 字符串 | 未设置 | 图片纹理路径，相对于资源包纹理目录。 |
| `uv` | 数组 | 未设置 | 纹理采样起始UV坐标。 |
| `uv_size` | 数组 | 未设置 | 纹理采样区域尺寸。 |
| `bilinear` | 布尔值 | 未设置 | 是否对纹理使用双线性过滤。 |
| `fill` | 选项 | 未设置 | 图片是否填充容器。 |
| `tiled` | 布尔值 | 未设置 | 渲染时是否平铺纹理。 |
| `nine_slice_top` | 整数 | 未设置 | 九切片顶部尺寸。 |
| `nine_slice_right` | 整数 | 未设置 | 九切片右侧尺寸。 |
| `nine_slice_buttom` | 整数 | 未设置 | 九切片底部尺寸。字段名按Microsoft Learn源文件保留。 |
| `nine_slice_left` | 整数 | 未设置 | 九切片左侧尺寸。 |
| `text` | 字符串 | 未设置 | 标签等控件显示的文本，可使用本地化键。 |
| `text_alignment` | 选项 | 未设置 | 文本在控件内的水平对齐方式。 |
| `font_type` | 选项 | 未设置 | 文本渲染使用的字体。 |
| `font_size` | 选项 | 未设置 | 文本渲染使用的字号。 |
| `font_scale_factor` | 数值或布尔值 | 未设置 | 字号缩放因子。Microsoft Learn表格将其类型列为布尔值，但说明为乘数。 |
| `shadow` | 布尔值 | 未设置 | 是否在文本后渲染阴影。 |
| `place_holder_text` | 字符串 | 未设置 | 输入框为空时显示的占位文本。 |
| `text_box_name` | 字符串 | 未设置 | 文本框名称标识。 |
| `max_length` | 整数 | 未设置 | 文本输入最大字符数。 |
| `virtual_keyboard_buffer_control` | 布尔值 | 未设置 | 是否使用虚拟键盘缓冲控件。 |
| `focus_enabled` | 布尔值 | 未设置 | 控件是否可以接收焦点。 |
| `default_focus_precedence` | 布尔值 | 未设置 | 控件接收默认焦点的优先设置。 |
| `focus_change_up` | 字符串 | 未设置 | 向上导航时转移焦点的目标控件。 |
| `focus_change_down` | 字符串 | 未设置 | 向下导航时转移焦点的目标控件。 |
| `focus_change_left` | 字符串 | 未设置 | 向左导航时转移焦点的目标控件。 |
| `focus_change_right` | 字符串 | 未设置 | 向右导航时转移焦点的目标控件。 |
| `always_handle_pointer` | 布尔值 | 未设置 | 是否始终处理指针事件。 |
| `consume_event` | 布尔值 | 未设置 | 是否消耗输入事件。 |
| `prevent_touch_input` | 布尔值 | 未设置 | 是否阻止触摸输入。 |
| `modal` | 布尔值 | 未设置 | 控件是否作为模态覆盖层。 |
| `locked_control` | 布尔值 | 未设置 | 控件锁定时显示的控制项。 |
| `animation_reset_name` | 字符串 | 未设置 | 要重置到的动画状态名称。 |
| `anims` | 字符串数组 | 未设置 | 应用于控件的动画引用。 |
| `scroll_view_port` | 字符串 | 未设置 | 滚动视图的视口控件引用。 |
| `scroll_content` | 字符串 | 未设置 | 可滚动内容控件引用。 |
| `scroll_box_and_track_panel` | 字符串 | 未设置 | 包含滚动条滑块和轨道的面板引用。 |
| `scrollbar_box` | 字符串 | 未设置 | 滚动条滑块控件引用。 |
| `scrollbar_track` | 字符串 | 未设置 | 滚动条轨道控件引用。 |
| `scrollbar_touch_button` | 布尔值 | 未设置 | 滚动条是否响应触摸按钮。 |
| `scroll_speed` | 选项 | 未设置 | 滚动视图的滚动速度。 |
| `jump_to_bottom_on_update` | 布尔值 | 未设置 | 内容更新时是否自动滚动到底部。 |
| `slider_range` | 数值 | 未设置 | 滑块范围。 |
| `slider_steps` | 数值 | 未设置 | 滑块离散步数。 |
| `slider_select_on_hover` | 字符串 | 未设置 | 悬停时是否改变滑块值。 |
| `tts_control_type_order_priority` | 字符串 | 未设置 | 文本转语音朗读顺序优先级。 |
| `tts_ignore_count` | 布尔值 | 未设置 | 文本转语音计数时是否忽略该控件。 |
| `tts_skip_message` | 布尔值 | 未设置 | 文本转语音朗读时是否跳过该控件。 |

## `bindings`

`bindings`用于将控件属性连接到游戏数据或其他控件属性。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `binding_name` | 字符串 | 未设置 | 绑定的数据源名称，例如以`#`开头的游戏数据名。 |
| `binding_name_override` | 字符串 | 未设置 | 将绑定值写入的控件属性。 |
| `binding_type` | 选项 | 未设置 | 绑定类型。 |
| `binding_condition` | 选项 | 未设置 | 绑定求值条件。 |
| `binding_collection_name` | 字符串 | 未设置 | 使用集合绑定时的集合名称。 |
| `source_control_name` | 字符串 | 未设置 | 视图绑定中的源控件名称。 |
| `source_property_name` | 字符串 | 未设置 | 源控件属性名。 |
| `target_property_name` | 字符串 | 未设置 | 目标控件属性名。 |

## `button_mappings`

`button_mappings`用于把输入按钮映射到界面动作。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `from_button_id` | 字符串 | 未设置 | 触发动作的输入按钮。 |
| `to_button_id` | 字符串 | 未设置 | 要触发的动作按钮。 |
| `mapping_type` | 选项 | 未设置 | 按钮映射类型。 |
| `input_mode_condition` | 选项 | 未设置 | 映射生效所需的输入模式。 |

## `controls`

`controls`数组中的每一项通常是一个仅包含一个键值对的对象。键名为子控件名称，值为控件对象。Microsoft Learn将键名模式列为`[a-zA-Z0-9_.:@]+`；其中`.`、`:`和`@`可用于命名空间引用或继承语法。

```json
{
  "controls": [
    {
      "child_label@common.label": {
        "text": "Example"
      }
    }
  ]
}
```

## `variables`

`variables`用于为控件提供局部变量或条件化变量。Microsoft Learn本批次参考只公开了变量项中的`requires`字段。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `requires` | 布尔值或表达式 | 未设置 | 变量项生效所需满足的条件。 |

## 相关参考

- [JSON UI](../../docs/general/json-ui.md)
- [资源包](../../docs/addon/resource-pack.md)
- [字体](../../docs/addon/font.md)

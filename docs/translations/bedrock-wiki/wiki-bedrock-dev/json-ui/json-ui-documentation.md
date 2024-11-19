---
title: JSON UI 文档
category: 文档
nav_order: 1
mentions:
 - KalmeMarq
 - SirLich
 - solvedDev
 - Joelant05
 - GTB3NW
 - stirante
 - sermah
 - MedicalJewel105
 - tinedpakgamer
 - LeGend077
 - TheDataLioness
 - shanewolf38
 - JosiahDZD
 - Tcbdxh
 - inotflying
 - TheItsNameless
 - SmokeyStack
 - Gotemba912
 - QuazChick
 - 1cce
description: JSON UI 的文档。
---

## UI 元素

### 元素类型

| 名称 | 描述 | 允许的属性 |
| - | - | - |
| panel | 一个容器，类似于 HTML 中的 `<div>` | [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| stack_panel | 类似于 `panel`，但根据 `orientation` 属性值堆叠其子元素 | [Stack Panel](../json-ui/json-ui-documentation.md#stack-panel) <br> [Collection](../json-ui/json-ui-documentation.md#collection) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| collection_panel | 类似于 `stack_panel`，但没有 `orientation` 属性 | [Collection](../json-ui/json-ui-documentation.md#collection) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| grid | 元素的网格 | [Grid](../json-ui/json-ui-documentation.md#grid) <br> [Collection](../json-ui/json-ui-documentation.md#collection) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| label | 文本元素 | [Text](../json-ui/json-ui-documentation.md#text) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| image | 精灵元素。绘制纹理。 | [Sprite](../json-ui/json-ui-documentation.md#sprite) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| input_panel | 接受输入的 `panel` | [Input](../json-ui/json-ui-documentation.md#input) <br> [Focus](../json-ui/json-ui-documentation.md#focus) <br> [Sound](../json-ui/json-ui-documentation.md#sound) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| button | 一个按钮，可以有 4 种状态（默认、悬停、按下和锁定） | [Button](../json-ui/json-ui-documentation.md#button) <br> [Input](../json-ui/json-ui-documentation.md#input) <br> [Focus](../json-ui/json-ui-documentation.md#focus) <br> [Sound](../json-ui/json-ui-documentation.md#sound) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| toggle | 一个切换按钮，有 2 种状态（选中或未选中）。每种状态有悬停和锁定变体 | [Toggle](../json-ui/json-ui-documentation.md#toggle) <br> [Input](../json-ui/json-ui-documentation.md#input) <br> [Focus](../json-ui/json-ui-documentation.md#focus) <br> [Sound](../json-ui/json-ui-documentation.md#sound) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| dropdown | 用于下拉菜单的切换按钮 | [Dropdown](../json-ui/json-ui-documentation.md#dropdown) <br> [Toggle](../json-ui/json-ui-documentation.md#toggle) <br> [Input](../json-ui/json-ui-documentation.md#input) <br> [Focus](../json-ui/json-ui-documentation.md#focus) <br> [Sound](../json-ui/json-ui-documentation.md#sound) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| slider | 范围输入元素 | [Slider](../json-ui/json-ui-documentation.md#slider) <br> [Input](../json-ui/json-ui-documentation.md#input) <br> [Focus](../json-ui/json-ui-documentation.md#focus) <br> [Sound](../json-ui/json-ui-documentation.md#sound) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| slider_box | 用于更改滑块值的滑块按钮 | [Slider Box](../json-ui/json-ui-documentation.md#slider-box) <br> [Input](../json-ui/json-ui-documentation.md#input) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| edit_box | 文本字段元素。默认是单行 | [Text Edit](../json-ui/json-ui-documentation.md#text-edit) <br> [Button](../json-ui/json-ui-documentation.md#button) <br> [Input](../json-ui/json-ui-documentation.md#input) <br> [Focus](../json-ui/json-ui-documentation.md#focus) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| scroll_view | 创建一个可滚动的面板元素 | [Scroll View](../json-ui/json-ui-documentation.md#scroll-view) <br> [Input](../json-ui/json-ui-documentation.md#input) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| scrollbar_track | 滚动条轨道 | [Input](../json-ui/json-ui-documentation.md#input) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) |
| scrollbar_box | 滚动条的“拇指”/按钮。可拖动的滚动手柄。默认是垂直方向的 | [Input](../json-ui/json-ui-documentation.md#input) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) |
| factory | 元素生成器 | [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) |
| screen | 屏幕元素 | [Screen](../json-ui/json-ui-documentation.md#screen) [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| custom | 在代码中创建的特殊渲染器元素，因为它对 JSON UI 来说太复杂 | [Custom Render](../json-ui/json-ui-documentation.md#custom-render) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| selection_wheel | | [Selection Wheel](../json-ui/json-ui-documentation.md#selection-wheel) <br> [Input](../json-ui/json-ui-documentation.md#input) <br> [Focus](../json-ui/json-ui-documentation.md#focus) <br> [Sound](../json-ui/json-ui-documentation.md#sound) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |

#### 旧版元素类型（不再工作）

| 名称 | 描述 | 允许的属性 |
| - | - | - |
| tab | 在添加切换按钮之前制作标签页的方式 | [Tab](../json-ui/json-ui-documentation.md#tab-legacy) <br> [Button](../json-ui/json-ui-documentation.md#button) <br> [Input](../json-ui/json-ui-documentation.md#input) <br> [Focus](../json-ui/json-ui-documentation.md#focus) <br> [Sound](../json-ui/json-ui-documentation.md#sound) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| carousel_label | | [Carousel Text](../json-ui/json-ui-documentation.md#carousel-text-legacy) <br> [Text](../json-ui/json-ui-documentation.md#text) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| grid_item | 一个 `panel`，但专门作为网格的项目/子项 | [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |
| scrollbar | | [Input](../json-ui/json-ui-documentation.md#input) <br> [Focus](../json-ui/json-ui-documentation.md#focus) <br> [Control](../json-ui/json-ui-documentation.md#control) <br> [Layout](../json-ui/json-ui-documentation.md#layout) <br> [Data Binding](../json-ui/json-ui-documentation.md#data-binding) |

## 属性

### 控件

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| visible | boolean | `true` | UI 元素是否可见 |
| enabled | boolean | `true` | 如果为 true，并且 UI 元素或其任何子元素处于锁定状态，则它们将处于锁定状态 |
| layer | int | `0` | 相对于父元素的 Z-索引/层级（类似于 CSS 中的 zindex）。较高的层级将渲染在上方 |
| alpha | float | `1.0` | 元素的 Alpha/透明度。它只会影响 UI 元素，其子元素不受影响。如果你希望 Alpha 同时应用于父元素和子元素，请使用 `propagate_alpha` |
| propagate_alpha | boolean | `false` | 如果 `alpha` 不仅应用于父元素（如果可能），还应用于其所有子元素 |
| clips_children | boolean | `false` | 在视觉上和交互上剪切 UI 元素边界之外的所有内容 |
| allow_clipping | boolean | `true` | 是否允许 UI 元素的 `clips_children` 属性生效。否则，它不会有任何效果 |
| clip_offset | Vector [x, y] | `[0, 0]` | 剪切的起始偏移 |
| clip_state_change_event | string | | |
| enable_scissor_test | boolean | | [https://www.khronos.org/opengl/wiki/Scissor_Test](https://www.khronos.org/opengl/wiki/Scissor_Test) |
| property_bag | object | | [Property bag](../json-ui/json-ui-documentation.md#property-bag) 包含更多与数据相关的属性/变量，而不是 UI 元素的结构和外观 |
| selected | boolean | | 如果文本框默认被选中 |
| use_child_anchors | boolean | `false` | 使用 UI 元素子元素的 `anchor_from` 和 `anchor_to` |
| controls | array | | 用于向元素添加子元素 |
| anims | string[] | | 动画名称的数组 |
| disable_anim_fast_forward | boolean | | |
| animation_reset_name | string | | |
| ignored | boolean | `false` | 是否忽略 UI 元素 |
| variables | array or object | | 一系列更改变量值的条件 |
| modifications | array | | 允许修改资源包的 UI 文件（原版资源包在最底层） |
| grid_position | Vector [row, column] | | 元素在网格中的位置。这也允许修改硬编码网格的特定网格项 |
| collection_index | int | | 元素在合集中的索引 |

#### 旧版（不再工作）

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| z_order | int | 0 | `layer` 属性的第一个版本 |
| scroll_report | string[] | | 当滚动面板内容更改时通知的控件名称数组 |
| alignment | enum | | 可能的值： <br> `top_left` <br> `top_middle` <br> `top_right` <br> `left_middle` <br> `center` <br> `right_middle` <br> `bottom_left` <br> `bottom_middle` <br> `bottom_right` |

### 布局

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| size | Vector [width, height] | `["default", "default"]` | UI 元素的大小。 <br> 可能的值： <br> `"default"`（默认值为 `"100%"`） <br> `0`（像素数值） <br> `"0px"`（像素数值。与 0 相同，但以字符串形式表示，并在末尾添加 px。当你想要将基于百分比的值与特定像素数相加或相减时使用。例如 `"75% + 12px"`） <br> `"0%"`（相对于父元素的百分比） <br> `"0%c"`（相对于元素子元素总宽度/高度的百分比） <br> `"0%cm"`（相对于该元素最大可见子元素的宽度/高度的百分比） <br> `"0%sm"`（相对于兄弟元素的宽度/高度的百分比） <br> `"0%y"`（元素的高度百分比） <br> `"0%x"`（元素的宽度百分比） <br> `"fill"`（扩展到父元素剩余的宽度/高度） |
| max_size | Vector [width, height] | `["default", "default"]` | UI 元素可拥有的最大大小 |
| min_size | Vector [width, height] | `["default", "default"]` | UI 元素可拥有的最小大小 |
| offset | Vector [x, y] | `[0, 0]` | UI 元素相对于父 UI 元素的位置。基于左上角，坐标 [0, 0] 从屏幕左上角开始。 <br> `10` - 像素 <br> `"10px"` - 像素 <br> `"50%"` - 父元素的宽度/高度 <br> `"50%x"` - 元素的宽度 <br> `"50%y"` - 元素的高度 |
| anchor_from | enum | `center` | 父元素中的锚点。 <br> 可能的值： <br> `top_left` <br> `top_middle` <br> `top_right` <br> `left_middle` <br> `center` <br> `right_middle` <br> `bottom_left` <br> `bottom_middle` <br> `bottom_right` |
| anchor_to | enum | `center` | 元素中的锚点。 <br> 可能的值： <br> `top_left` <br> `top_middle` <br> `top_right` <br> `left_middle` <br> `center` <br> `right_middle` <br> `bottom_left` <br> `bottom_middle` <br> `bottom_right` |
| inherit_max_sibling_width | boolean | `false` | 使用兄弟元素的最大宽度 |
| inherit_max_sibling_height | boolean | `false` | 使用兄弟元素的最大高度 |
| use_anchored_offset | boolean | | |
| contained | boolean | | |
| draggable | enum | | 使元素可以通过光标拖动。元素应该能够接受输入才能被拖动（如 `input_panel`、`button` 等），并且必须具有所需的按钮映射。 <br> 可能的值：`vertical`，`horizontal` 和 `both` |
| follows_cursor | boolean | `false` | 跟随光标 |

### 数据绑定

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| bindings | Vector of [binding object](../json-ui/json-ui-documentation.md#data-binding-array-object) | | 绑定并处理元素中的硬编码值 |

#### 数据绑定数组对象

数据绑定允许将硬编码值/变量绑定到元素属性。

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| ignored | boolean | `false` | 是否忽略绑定 |
| binding_type | enum | | 可能的值： <br> `global` <br> `view` <br> `collection` <br> `collection_details` <br> `none` |
| binding_name | string | | 存储数据绑定名称或与其相关的条件 |
| binding_name_override | string | | 将 `binding_name` 中存储的值应用于的 UI 元素属性的名称 |
| binding_collection_name | string | | 要使用的项目合集的名称 |
| binding_collection_prefix | string | | |
| binding_condition | enum | | 数据绑定发生的条件。 <br> 可能的值： <br> `always` <br> `always_when_visible` <br> `visible` <br> `once` <br> `none` <br> `visibility_changed` |
| source_control_name | string | | 要观察其属性值的 UI 元素的名称 |
| source_property_name | string | | 存储在 `source_control_name` 中引用的 UI 元素的属性值 |
| target_property_name | string | | 将 `source_property_name` 中存储的值应用到的 UI 元素属性 |
| resolve_sibling_scope | boolean | | 如果为 `true`，允许选择同一控件中的兄弟元素而不是其子元素，适用于 `source_control_name` |

### 栈面板

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| orientation | enum | `vertical` | `stack_panel` 内部元素堆叠的方向。 <br> 可能的值： <br> `vertical` <br> `horizontal` |

### 网格

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | - | - |
| grid_dimensions | Vector [rows, columns] | | 网格的列数和行数 |
| maximum_grid_items | int | | 网格将生成的最大项目数 |
| grid_dimension_binding | string | | 网格维度的绑定名称 |
| grid_rescaling_type | enum | | 网格重新缩放的方向。 <br> 可能的值： <br> `vertical` <br> `horizontal` <br> `none` |
| grid_fill_direction | enum | | 可能的值： <br> `vertical` <br> `horizontal` <br> `none` |
| grid_item_template | string | | 一个能够处理合集的元素 <br> （例如 `"common.container_item"`，`"container_items"`，`"inventory_items"` 等） |
| precached_grid_item_count | int | | |

### 文本

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| text | string | | 文本内容 |
| color | Vector [r, g, b] | `[1.0, 1.0, 1.0]` | 文本颜色。RGB 值从 0.0 到 1.0 |
| locked_color | Vector [r, g, b] | | 当父元素的 `enabled: false` 时的文本颜色 |
| shadow | boolean | `false` | 文本阴影 |
| hide_hyphen | boolean | `false` | 隐藏由换行引起的连字符 |
| notify_on_ellipses | string[] | | 当文本出现或失去省略号时通知的控件名称数组 |
| enable_profanity_filter | boolean | `false` | 是否应对“脏”词进行审查 |
| locked_alpha | float | | 当父元素的 `enabled: false` 时标签的 Alpha/透明度 |
| font_size | enum | `normal` | 文本大小。 <br> 可能的值： <br> `small` <br> `normal` <br> `large` <br> `extra_large` |
| font_scale_factor | float | `1.0` | 文本的缩放 |
| localize | boolean | `false` | 是否应将 `text` 翻译 |
| line_padding | number | | 行间距 |
| font_type | enum | `default` | 文本的字体。 <br> 可能的值： <br> `default` <br> `rune` <br> `unicode` <br> `smooth` <br> `MinecraftTen` <br> 或任何其他自定义字体 |
| backup_font_type | enum | `default` | 如果 `font_type` 无效，将使用的字体 |
| text_alignment | enum | | 文本对齐方向。如果未定义，它将根据 `anchor_from` 和 `anchor_to` 自动调整 |

#### 旧版（不再工作）

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| wrap | boolean | `false` | 如果文本大于元素的宽度，则将文本换行 |
| clip | boolean | `false` | |

使用 `notify_on_ellipses`。主要用于硬编码文本。

```json title="RP/ui/example_file.json"
{
 "label": {
 ...
 "notify_on_ellipses": [
 "my_button"
 ]
 },

 "my_button": {
 ...
 "bindings": [
 {
 "binding_type": "view",
 "source_property_name": "#using_ellipses",
 "target_property_name": "#visible"
 }
 ]
 }
}
```

### 精灵图

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| texture | string | | 从资源包根目录开始的图片路径。（例如 `"textures/ui/White"`） |
| allow_debug_missing_texture | boolean | `true` | 如果未找到纹理，则显示缺失纹理 |
| uv | Vector [u, v] | | 纹理映射的起始位置 |
| uv_size | Vector [width, height] | | 纹理映射的大小 |
| texture_file_system | string | `InUserPackage` | 获取纹理的来源。 <br> 可能的值： <br> `InUserPackage` <br> `InAppPackage` <br> `RawPath` <br> `RawPersistent` <br> `InSettingsDir` <br> `InExternalDir` <br> `InServerPackage` <br> `InDataDir` <br> `InUserDir` <br> `InWorldDir` <br> `StoreCache` <br> 用法未知 |
| nineslice_size | int, Vector [x, y] 或 Vector [x0, y0, x1, y1] | | 九宫切片。将纹理分成 9 片的方法。当调整大小时，角落保持不变，其余部分会拉伸 |
| tiled | boolean 或 enum | | 如果 UI 元素的大小大于纹理大小，纹理是否会平铺。 <br> 可能的值： <br> `true`/`false` <br> `x` <br> `y` |
| tiled_scale | Vector [sX, sY] | `false` | 平铺纹理的缩放 |
| clip_direction | enum | | `clip_ratio` 的起始点位置。如果为 `down`，图像将从底部开始出现。 <br> 可能的值： <br> `left` <br> `right` <br> `up` <br> `down` <br> `center` |
| clip_ratio | float | | 剪切的程度。从 0.0 到 1.0 |
| clip_pixelperfect | boolean | | 如果剪切应尽可能像素精确 |
| keep_ratio | boolean | `true` | 调整图像大小时保持比例 |
| bilinear | boolean | `false` | 调整图像大小时使用双线性函数 |
| fill | boolean | `false` | 将图像拉伸到指定大小 |
| $fit_to_width | boolean | | |
| zip_folder | string | | |
| grayscale | boolean | `false` | 以黑白显示图像 |
| force_texture_reload | boolean | | 当纹理路径更改时重新加载图像 |
| base_size | Vector [width, height] | | |

要使用剪切，将 `#*_ratio` 绑定名称绑定到带有绑定条件 `"always"` 的 `#clip-ratio` 属性。熔炉 UI 中的进度箭头和燃料图像就是这样工作的。

### 输入

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| button_mappings | Vector of [mapping object](../json-ui/json-ui-documentation.md#button-mapping-array-object) | | |
| modal | boolean | | |
| inline_modal | boolean | | |
| always_listen_to_input | boolean | | |
| always_handle_pointer | boolean | | |
| always_handle_controller_direction | boolean | | |
| hover_enabled | boolean | | |
| prevent_touch_input | boolean | | |
| consume_event | boolean | | |
| consume_hover_events | boolean | | |
| gesture_tracking_button | string | | |

#### 按钮映射数组对象

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| ignored | boolean | `false` | 是否忽略映射 |
| from_button_id | string | | 触发事件的动作 ID |
| to_button_id | string | | 事件触发时要执行的动作 ID |
| mapping_type | enum | | 可能的值： <br> `global` <br> `pressed` <br> `double_pressed` <br> `focused` |
| scope | enum | | 可能的值： <br> `view` <br> `controller` |
| input_mode_condition | enum | | 可能的值： <br> `not_gaze` <br> `not_gamepad` <br> `gamepad_and_not_gaze` |
| ignore_input_scope | boolean | | |
| consume_event | boolean | | |
| handle_select | boolean | | |
| handle_deselect | boolean | | |
| button_up_right_of_first_refusal | boolean | | |

### 焦点

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| default_focus_precedence | int | | |
| focus_enabled | boolean | | 是否可以使用箭头键或控制器聚焦元素 |
| focus_wrap_enabled | boolean | | |
| focus_magnet_enabled | boolean | | |
| focus_identifier | string | | 此元素的焦点标识符 |
| focus_change_down | string | | 当按下 `button.menu_down` 时，将接收焦点的可聚焦元素的标识符（`focus_identifier`）。如果希望阻止焦点从底部溢出，请使用 `FOCUS_OVERRIDE_STOP` |
| focus_change_up | string | | 当按下 `button.menu_up` 时，将接收焦点的可聚焦元素的标识符（`focus_identifier`）。如果希望阻止焦点从顶部溢出，请使用 `FOCUS_OVERRIDE_STOP` |
| focus_change_left | string | | 当按下 `button.menu_left` 时，将接收焦点的可聚焦元素的标识符（`focus_identifier`）。如果希望阻止焦点从左侧溢出，请使用 `FOCUS_OVERRIDE_STOP` |
| focus_change_right | string | | 当按下 `button.menu_right` 时，将接收焦点的可聚焦元素的标识符（`focus_identifier`）。如果希望阻止焦点从右侧溢出，请使用 `FOCUS_OVERRIDE_STOP` |
| focus_mapping | array | | |
| focus_container | boolean | | |
| use_last_focus | boolean | | |
| focus_navigation_mode_left | enum | | 可能的值：`none` <br> `stop` <br> `custom` <br> `contained` |
| focus_navigation_mode_right | enum | | 可能的值：`none` <br> `stop` <br> `custom` <br> `contained` |
| focus_navigation_mode_down | enum | | 可能的值：`none` <br> `stop` <br> `custom` <br> `contained` |
| focus_navigation_mode_up | enum | | 可能的值：`none` <br> `stop` <br> `custom` <br> `contained` |
| focus_container_custom_left | Vector of [focus container custom object](../json-ui/json-ui-documentation.md#focus-container-custom-array-object) | | |
| focus_container_custom_right | Vector of [focus container custom object](../json-ui/json-ui-documentation.md#focus-container-custom-array-object) | | |
| focus_container_custom_down | Vector of [focus container custom object](../json-ui/json-ui-documentation.md#focus-container-custom-array-object) | | |
| focus_container_custom_up | Vector of [focus container custom object](../json-ui/json-ui-documentation.md#focus-container-custom-array-object) | | |

#### 焦点容器自定义数组对象

| 属性名称 | 类型 | 描述 |
| - | :-: | - |
| other_focus_container_name | string | 当按下 `button.menu_left`、`button.menu_right`、`button.menu_up` 或 `button.menu_down` 时，将接收焦点的 UI 控件的名称 |
| focus_id_inside | string | `focus_identifier`，将接收焦点的 `other_focus_container_name` 中的可聚焦子控件的标识符 |

```json title="RP/ui/example_file.json"
...
{
 "other_panel": {
 ...
 "focus_container": true,
 "controls": [
 ...
 ]
 }
},
{
 "input_panel": {
 ...
 "focus_container_custom_up": [
 {
 "other_focus_container_name": "other_panel" // 当此容器的焦点在 `button.menu_up` 结束时，将接收焦点的对象名称
 }
 ]
 }
}
...
```

### 按钮

| 属性名称 | 类型 | 默认值 | 描述 |
| - | :-: | :-: | - |
| default_control | string | | 仅在默认状态下显示的子控件名称 |
| hover_control | string | | 仅在悬停状态下显示的子控件名称 |
| pressed_control | string | | 仅在按下状态下显示的子控件名称 |
| locked_control | string | | 仅在锁定状态下显示的子控件名称 |

### 切换

| Property Name | Type | Default Value | Description |
| - | :-: | :-: | - |
| radio_toggle_group | boolean | | |
| toggle_name | string | | 切换组的标识符。它可以是自定义的。 |
| toggle_default_state | boolean | | |
| toggle_group_forced_index | int | | 切换组中切换的索引 |
| toggle_group_default_selected | int | | 切换组中默认选择的切换索引 |
| reset_on_focus_lost | boolean | | |
| toggle_on_hover | string | | |
| toggle_on_button | string | | |
| toggle_off_button | string | | |
| enable_directional_toggling | boolean | | |
| toggle_grid_collection_name | string | | 切换所属的合集名称 |
| checked_control | string | | 仅在选中状态下显示的子控件名称 |
| unchecked_control | string | | 仅在未选中状态下显示的子控件名称 |
| checked_hover_control | string | | 仅在选中悬停状态下显示的子控件名称 |
| unchecked_hover_control | string | | 仅在未选中悬停状态下显示的子控件名称 |
| checked_locked_control | string | | 仅在选中锁定状态下显示的子控件名称 |
| unchecked_locked_control | string | | 仅在未选中锁定状态下显示的子控件名称 |
| checked_locked_hover_control | string | | 仅在选中锁定悬停状态下显示的子控件名称 |
| unchecked_locked_hover_control | string | | 仅在未选中锁定悬停状态下显示的子控件名称 |

### 硬编码切换

在某些屏幕中，导航标签组有其映射的默认选中标签，如设置或背包。
我猜这些值是正确的。

```json
$search_index - $construction_index
$survival_layout_index - $construction_index
$recipe_book_layout_index - $equipment_index
$creative_layout_index - $items_index
```

在设置和背包中有一些必选的切换，尽管在没有开发版本和打开断言诊断时无法获得警告，但它们确实存在并由一个名为 _ScreenView::\_passViewCommand::<lambda_6d65fd272578d43f1becb6eada4ff32c>::()::<lambda_2ab071547c9a470558c54e4d3cddb5f2>::operator()_ 的函数控制，当你完全修改这些屏幕时，可能会遇到此断言。

例如，在设置中是无障碍功能，在背包中，建筑、装备、物品和自然标签是必需的。

### 下拉菜单

| Property Name | Type | Default Value | Description |
| - | :-: | :-: | - |
| dropdown_name | string | | 下拉菜单的标识符 |
| dropdown_content_control | string | | 将作为根内容面板的子控件名称 |
| dropdown_area | string | | 将作为内部内容的子控件名称 |

### 声音

| Property Name | Type | Description |
| - | :-: | - |
| sound_name | string | 在按下事件触发时播放的 `RP/sounds/sound_definitions.json` 文件中定义的声音名称 |
| sound_volume | float | 声音的音量 |
| sound_pitch | float | 声音的音调 |
| sounds | Vector of [sound object](../json-ui/json-ui-documentation.md#sound-array-object) | 在按下事件触发时播放的声音数组 |

#### 声音数组对象

| Property Name | Type | Description |
| - | :-: | - |
| sound_name | string | 在按下事件触发时播放的 `RP/sounds/sound_definitions.json` 文件中定义的声音名称 |
| sound_volume | float | 声音的音量 |
| sound_pitch | float | 声音的音调 |
| min_seconds_between_plays | float | 声音可再次播放前的等待秒数 |

### 合集

| Property Name | Type | Description |
| - | :-: | - |
| collection_name | string | 要使用的合集名称 |

### 文本编辑

| Property Name | Type | Default Value | Description |
| - | :-: | :-: | - |
| text_box_name | string | | 文本框的标识符 |
| text_edit_box_grid_collection_name | string | | `edit_box` 所属的合集名称 |
| constrain_to_rect | boolean | | |
| enabled_newline | boolean | | 允许多行文本 |
| text_type | enum | | 用户在文本字段中允许输入的字符类型。<br> 可能的值：<br> `ExtendedASCII`<br> `IdentifierChars`<br> `NumberChars` |
| max_length | int | | 文本字段中允许的最大字符数 |
| text_control | string | | 将用于显示文本的子控件名称 |
| place_holder_control | string | | 将用于显示占位文本的子控件名称 |
| can_be_deselected | boolean | | |
| always_listening | boolean | | |
| virtual_keyboard_buffer_control | string | | |

### 滑块

| Property Name | Type | Default Value | Description |
| - | :-: | :-: | - |
| slider_track_button | string | | 滑块轨道的动作 ID |
| slider_small_decrease_button | string | | 减小滑块的动作 ID |
| slider_small_increase_button | string | | 增大滑块的动作 ID |
| slider_steps | int | | 滑块有多少步（或值） |
| slider_direction | enum | | 滑块移动的方向。<br> 可能的值：<br> `vertical`<br> `horizontal` |
| slider_timeout | number | | |
| slider_collection_name | string | | 滑块所属的合集名称 |
| slider_name | string | | 滑块的标识符 |
| slider_select_on_hover | boolean | | 悬停时聚焦滑块 |
| slider_selected_button | string | | 滑块选中时的动作 ID |
| slider_deselected_button | string | | 滑块取消选中时的动作 ID |
| slider_box_control | string | | 将作为滑块滑块的子控件名称 |
| background_control | string | | 将作为滑块背景的子控件名称 |
| background_hover_control | string | | 悬停时将作为滑块背景的子控件名称 |
| progress_control | string | | 将作为滑块进度背景覆盖的子控件名称 |
| progress_hover_control | string | | 悬停时将作为滑块进度背景覆盖的子控件名称 |

### 滑块滑块

| Property Name | Type | Default Value | Description |
| - | :-: | :-: | - |
| default_control | string | | 默认状态下显示的子控件名称 |
| hover_control | string | | 悬停状态下显示的子控件名称 |
| locked_control | string | | 锁定状态下显示的子控件名称 |

### 滚动视图

| Property Name | Type | Default Value | Description |
|-|:-:|:-:|-|
| scrollbar_track_button | string | | 轨道按钮的动作 ID |
| scrollbar_touch_button | string | | 触摸输入的动作 ID |
| scroll_speed | number | | 滚动速度 |
| gesture_control_enabled | boolean | | |
| always_handle_scrolling | boolean | | |
| touch_mode | boolean | | |
| scrollbar_box | string | | 将作为滚动条滑块行为的子 UI 元素或嵌套 UI 元素的名称。 |
| scrollbar_track | string | | 将作为滚动条轨道行为的子 UI 元素或嵌套 UI 元素的名称 |
| scroll_view_port | string | | 将作为视口行为的子 UI 元素的名称 |
| scroll_content | string | | 将作为内容根父级行为的子 UI 元素的名称 |
| scroll_box_and_track_panel | string | | 将包含滚动条和轨道控件的子 UI 元素的名称 |
| jump_to_bottom_on_update | boolean | | 当滚动面板有更新时跳转到底部。例如，向其中添加更多子项。 |

### 自定义渲染

| Property Name | Type | Description |
| - | :-: | - |
| renderer | enum | 可能的值：<br> `hover_text_renderer`<br> `3d_structure_renderer`<br> `splash_text_renderer`<br> `ui_holo_cursor`<br> `trial_time_renderer`<br> `panorama_renderer`<br> `actor_portrait_renderer`<br> `banner_pattern_renderer`<br> `live_player_renderer`<br> `web_view_renderer`<br> `hunger_renderer`<br> `bubbles_renderer`<br> `mob_effects_renderer`<br> `cursor_renderer`<br> `progress_indicator_renderer`<br> `camera_renderer`<br> `horse_jump_renderer`<br> `armor_renderer`<br> `horse_heart_renderer`<br> `heart_renderer`<br> `hotbar_cooldown_renderer`<br> `hotbar_renderer`<br> `hud_player_renderer`<br> `live_horse_renderer`<br> `holographic_postrenderer`<br> `enchanting_book_renderer`<br> `debug_screen_renderer`<br> `gradient_renderer`<br> `paper_doll_renderer`<br> `name_tag_renderer`<br> `flying_item_renderer`<br> `inventory_item_renderer`<br> `credits_renderer`<br> `vignette_renderer`<br> `progress_bar_renderer`<br> `debug_overlay_renderer`<br> `background_renderer`<br> `bohr_model_renderer`<br> `experience_renderer`（旧版，不再使用）<br> `menu_background_renderer`（旧版，不再使用） |

#### 渲染器

| Renderer Name | Description |
| - | - |
| `flying_item_renderer` | 当你将物品从一个槽位移动到另一个槽位时的飞行物品 |
| `inventory_item_renderer` | 渲染一个物品图标。仅在游戏内屏幕中工作 |
| `credits_renderer` | 制作人员名单和结束诗 |
| `vignette_renderer` | 一种渐晕效果 |
| `name_tag_renderer` | 类似于玩家头顶的玩家名或给动物使用名字标签时其上方的名称 |
| `paper_doll_renderer` | 一个皮肤模型 |
| `debug_screen_renderer` | 测试版/预览版中出现的调试文本 |
| `enchanting_book_renderer` | 附魔台的书。当有物品需要附魔时打开 |
| `gradient_renderer` | 绘制一个渐变 |
| `live_horse_renderer` | 马/驴/羊驼等模型 |
| `live_player_renderer` | 玩家模型 |
| `hud_player_renderer` | 模仿玩家行为的玩家模型 |
| `hotbar_renderer` | 获取每个槽位的快捷栏槽位图像 |
| `hotbar_cooldown_renderer` | 绘制物品冷却 |
| `heart_renderer` | 绘制玩家生命值 |
| `horse_heart_renderer` | 绘制马/驴/...的生命值 |
| `armor_renderer` | 绘制玩家护甲 |
| `horse_jump_renderer` | 绘制马跳跃进度条 |
| `hunger_renderer` | 绘制玩家饥饿度 |
| `bubbles_renderer` | 绘制呼吸气泡 |
| `mob_effects_renderer` | 绘制应用于玩家的效果 |
| `cursor_renderer` | 绘制屏幕中心的十字准星 |
| `progress_indicator_renderer` | 未使用 |
| `camera_renderer` | 用于相机物品 |
| `web_view_renderer` | 显示网站视图 |
| `banner_pattern_renderer` | 渲染旗帜 |
| `actor_portrait_renderer` | 绘制头像 |
| `trial_time_renderer` | 在游戏试用版中渲染剩余时间以便继续使用世界 |
| `progress_bar_renderer` | 绘制一个进度条。它有多种类型 |
| `3d_structure_renderer` | 渲染结构方块结构 |
| `splash_text_renderer` | 从 `splashes.json` 文件中获取并渲染一个随机的开场文本 |
| `hover_text_renderer` | 绘制工具提示 |
| `ui_holo_cursor` | |
| `panorama_renderer` | 不是出现在菜单背后的全景图，而是商店世界的全景图。 |

#### 特定属性

| Property Name | Type | Renderer | Description |
| - | :-: | - | - |
| gradient_direction | enum | `gradient_renderer` | 可能的值：<br> `vertical`<br> `horizontal` |
| color1 | Vector [r, g, b, a] | `gradient_renderer` | |
| color2 | Vector [r, g, b, a] | `gradient_renderer` | |
| text_color | Vector [r, g, b, a] | `name_tag_renderer` | |
| background_color | Vector [r, g, b, a] | `name_tag_renderer` | |
| primary_color | Vector [r, g, b, a] | `progress_bar_renderer` | |
| secondary_color | Vector [r, g, b, a] | `progress_bar_renderer` | |
| camera_tilt_degrees | number | `paper_doll_renderer` | |
| starting_rotation | number | `paper_doll_renderer` | |
| use_selected_skin | boolean | `paper_doll_renderer` | |
| use_uuid | boolean | `paper_doll_renderer` | |
| use_skin_gui_scale | boolean | `paper_doll_renderer` | |
| use_player_paperdoll | boolean | `paper_doll_renderer` | |
| rotation | enum | `paper_doll_renderer` 和 `panorama_renderer` | 可能的值：<br> `auto`<br> `gesture_x`<br> `custom_y` |
| end_event | string | `credits_renderer` | |

### 屏幕

| Property Name | Type | Description |
| - | :-: | - |
| render_only_when_topmost | boolean | 仅当屏幕堆栈中是最顶层的屏幕时才渲染 |
| screen_not_flushable | boolean | |
| always_accepts_input | boolean | |
| render_game_behind | boolean | 不阻止下面的屏幕接收用户输入 |
| absorbs_input | boolean | |
| is_showing_menu | boolean | |
| is_modal | boolean | 它是一个屏幕模态 |
| should_steal_mouse | boolean | 捕获光标并隐藏它 |
| low_frequency_rendering | boolean | 使用更少的内存来渲染屏幕 |
| screen_draws_last | boolean | 它是最后一个被绘制/渲染的屏幕 |
| vr_mode | boolean | |
| force_render_below | boolean | 在屏幕堆栈中当前屏幕下方渲染底部屏幕 |
| send_telemetry | boolean | |
| close_on_player_hurt | boolean | 当玩家受到伤害时关闭屏幕 |
| cache_screen | boolean | |
| load_screen_immediately | boolean | |
| gamepad_cursor | boolean | |
| gamepad_cursor_deflection_mode | boolean | |
| should_be_skipped_during_automation | boolean | |

### 选轮

| Property Name | Type | Description |
| - | :-: | - |
| inner_radius | number | |
| outer_radius | number | |
| state_controls | string[] | |
| slice_count | integer | |
| button_name | string | |
| iterate_left_button_name | string | |
| iterate_right_button_name | string | |
| initial_button_slice | integer | |

### TTS

| Property Name | Type | Description |
| - | :-: | - |
| tts_name | string | |
| tts_control_header | string | |
| tts_section_header | string | |
| tts_control_type_order_priority | integer | |
| tts_index_priority | integer | |
| tts_toggle_on | string | 由 `toggle` 类型使用 |
| tts_toggle_off | string | 由 `toggle` 类型使用 |
| tts_override_control_value | string | |
| tts_inherit_siblings | boolean | |
| tts_value_changed | string | |
| ttsSectionContainer | boolean | |
| tts_ignore_count | boolean | |
| tts_skip_message | boolean | |
| tts_value_order_priority | integer | |
| tts_play_on_unchanged_focus_control | boolean | |
| tts_ignore_subsections | boolean | |
| text_tts | string | |
| use_priority | boolean | 是否使用 `priority` 属性来确定每个子控件的 TTS 优先级 |
| priority | boolean | 元素在 TTS 中的优先级顺序/索引 |

### 标签（旧版）

| Property Name | Type | Default Value | Description |
| - | :-: | :-: | - |
| tab_index | int | | 标签组中标签的 ID |
| tab_group | int | | 标签所属的组的 ID |
| tab_control | string | | 标签激活时将显示的控件名称 |

### 轮播文本（旧版）

| Property Name | Type | Default Value | Description |
| - | :-: | :-: | - |
| always_rotate | boolean | | |
| rotate_speed | number | | |
| hover_color | Vector [r, g, b, a], | | 元素悬停时的 `颜色` |
| hover_alpha | float | | 元素悬停时的 `透明度` |
| pressed_color | Vector [r, g, b, a], | | 元素按下时的 `颜色` |
| pressed_alpha | float | | 元素按下时的 `透明度` |

## 属性附加信息

### 锚点属性

锚点允许元素对齐到某个点，位置、大小、缩放、动画等将以该点为变换基准。
在 JSON UI 中，有两个属性 `anchor_from` 和 `anchor_to` 共同实现这一点。

大多数人通过给它们相同的值来使用它们：

```json title="RP/ui/example_file.json"
{
 "element": {
 "anchor_from": "top_left",
 "anchor_to": "top_left"
 }
}
```

<WikiImage
	src="../assets/images/json-ui/json-ui-documentation/anchor_same_value.png"
	alt="锚点具有相同值"
	pixelated
	width=782
/>

然而，当它们具有不同的值时会发生什么？让我们看看当 `anchor_from: center` 和 `anchor_to: top_left` 时会发生什么。这是展示实际发生情况的最佳示例。

```json title="RP/ui/example_file.json"
{
 "element": {
 "anchor_from": "center",
 "anchor_to": "top_left"
 }
}
```

<WikiImage
	src="../assets/images/json-ui/json-ui-documentation/anchor_center_top_left.png"
	alt="锚点从中心到左上角"
	pixelated
	width=782
/>

元素的左上点位于父元素的中心点。

另一个示例：

<WikiImage
	src="../assets/images/json-ui/json-ui-documentation/anchor_ce_rm_tm_tl.png"
	alt="锚点从中心到右中部和锚点从上中部到左上角"
	pixelated
	width=782
/>

蓝色框的左上点位于父元素的上中点。至于黑色框，右中点位于父元素的中心。

基本上 `anchor_to` 是将要附加到父元素中 `anchor_from` 的元素的锚点。

### 变量属性

| Name | Type | Description |
| - | :-: | - |
| `requires` | string | 条件，决定是否应用以下变量值。接受 `$variables`，但不接受 `#bindings`。 |

如果你只有一个变量需要使用，应该仅使用 `"variables": {}`

```json title="RP/ui/example_file.json"
{
 "element": {
 ...
 "size": "$el_size",
 "$el_size|default": ["100%", 20],
 "variables": {
 "requires": "$var_condition",
 "$el_size": ["100%", 30]
 }
 }
}
```

如果有多个变量，请使用 `"variables": [{}]`

```json title="RP/ui/example_file.json"
{
 "element": {
 ...
 "size": "$el_size",
 "offset": "$el_offset",
 "$el_offset|default": [0, 40],
 "$el_size|default": ["100%", 20],
 "variables": [
 {
 "requires": "$var_condition",
 "$el_size": ["100%", 30]
 },
 {
 "requires": "$other_var_condition",
 "$el_offset": [0, 15],
 "$el_size": ["90%", 35]
 }
 ]
 }
}
```

## 属性包

| Name | Type | Requirements | Description |
| - | :-: | - | - |
| #filtered_light_multiplier | float | type[custom]<br>renderer[inventory_item_renderer] | |
| #banner_patterns | string | type[custom]<br>renderer[inventory_item_renderer] | |
| #banner_colors | string | type[custom]<br>renderer[inventory_item_renderer] | |
| #item_id_aux | int | type[custom]<br>renderer[inventory_item_renderer] | |
| #item_custom_color | int | type[custom]<br>renderer[inventory_item_renderer] | |
| #disabled_filter_visible | boolean | type[custom]<br>renderer[inventory_item_renderer] | |
| #item_pickup_time | float | type[custom]<br>renderer[inventory_item_renderer] | |
| #look_at_cursor | boolean | type[custom]<br>renderer[hud_player_renderer] | |
| entity_type | enum | type[custom]<br>renderer[paper_doll_renderer] | 可能的值：<br> `player`<br> `npc` |
| #skin_idx | int | type[custom]<br>renderer[paper_doll_renderer] | |
| #player_uuid | string | type[custom]<br>renderer[paper_doll_renderer] | |
| #skin_rotation | boolean | type[custom]<br>renderer[paper_doll_renderer] | |
| #custom_rot_y | float | type[custom]<br>renderer[paper_doll_renderer] | |
| #gesture_delta_source | string | type[custom]<br>renderer[paper_doll_renderer] | |
| #gesture_mouse_delta_x | string | type[custom]<br>renderer[paper_doll_renderer] | |
| #pack_id | int | type[custom]<br>renderer[paper_doll_renderer] | |
| #force_skin_update | string | type[custom]<br>renderer[paper_doll_renderer] | |
| #progress_bar_visible | boolean | type[custom]<br>renderer[progress_bar_renderer] | |
| #progress_bar_total_amount | float | type[custom]<br>renderer[progress_bar_renderer] | |
| #progress_bar_current_amount | float | type[custom]<br>renderer[progress_bar_renderer] | |
| is_durability | boolean | type[custom]<br>renderer[progress_bar_renderer] | |
| round_value | boolean | type[custom]<br>renderer[progress_bar_renderer] | |
| #hover_text | string | type[custom]<br>renderer[hover_text_renderer] | |
| #open | boolean | type[custom]<br>renderer[enchanting_book_renderer] | |
| flying_item_count | int | type[custom]<br>renderer[flying_item_renderer] | |
| flying_item_id_aux | int | type[custom]<br>renderer[flying_item_renderer] | |
| flying_item_custom_color | int | type[custom]<br>renderer[flying_item_renderer] | |
| flying_item_origin_position_x | float | type[custom]<br>renderer[flying_item_renderer] | |
| flying_item_origin_position_y | float | type[custom]<br>renderer[flying_item_renderer] | |
| flying_item_origin_scale | float | type[custom]<br>renderer[flying_item_renderer] | |
| flying_item_destination_position_x | float | type[custom]<br>renderer[flying_item_renderer] | |
| flying_item_destination_position_y | float | type[custom]<br>renderer[flying_item_renderer] | |
| flying_item_destination_scale | float | type[custom]<br>renderer[flying_item_renderer] | |
| flying_item_banner_patterns | string | type[custom]<br>renderer[flying_item_renderer] | |
| flying_item_banner_colors | string | type[custom]<br>renderer[flying_item_renderer] | |
| #use_heart_offset | boolean | type[custom]<br>renderer[armor_renderer] | |
| opacity_override | float | type[custom]<br>renderer[vignette_renderer] | |
| #playername | string | type[custom]<br>renderer[name_tag_renderer] | |
| #x_padding | number | type[custom]<br>renderer[name_tag_renderer] | |
| #entity_id | string or int | type[custom]<br>renderer[live_horse_renderer] | |
| #hyperlink | string | type[button] | |
| #anchored_offset_value_x | number | `use_anchored_offset` 属性 | |
| #anchored_offset_value_y | number | `use_anchored_offset` 属性 | |
| #size_binding_x | number | `use_anchored_offset` 属性 | |
| #size_binding_y | number | `use_anchored_offset` 属性 | |
| #has_focus | boolean | type[custom]<br>renderer[3d_structure_renderer] | |
| #block_position | Vector [x, y, z] | type[custom]<br>renderer[3d_structure_renderer] | |
| #top_right_block | Vector [x, y, z] | type[custom]<br>renderer[3d_structure_renderer] | |
| #bottom_left_block | Vector [x, y, z] | type[custom]<br>renderer[3d_structure_renderer] | |
| #include_entities | boolean | type[custom]<br>renderer[3d_structure_renderer] | |
| #remove_blocks | boolean | type[custom]<br>renderer[3d_structure_renderer] | |
| #include_players | boolean | type[custom]<br>renderer[3d_structure_renderer] | |
| #slider_steps | number | type[slider] | |
| #slider_value | number | type[slider] | |
| #property_field | string | type[edit_box] | |
| #hover_slice | int | type[selection_wheel] | |
| #toggle_state | boolean | type[toggle] | |
| #start_selected | boolean | | |
| #tts_dialog_title | string | | |
| #tts_dialog_body | string | | |
| force_update | boolean | | |
| #sub_command | string | | |
| #panel_title | string | | |
| #index | int | | |
| #collection_prefix | string | | |
| #collection_name | string | | |
| #visible | boolean | | |
| #common | Vector [r, g, b, a] | | |
| #uncommon | Vector [r, g, b, a] | | |
| #rare | Vector [r, g, b, a] | | |
| #epic | Vector [r, g, b, a] | | |
| #legendary | Vector [r, g, b, a] | | |
| reset_group | enum | | 可能的值：<br> `video`<br> `audio`<br> `accessibility` |
| #text | string | | |
| timer_duration | number | | |
| #should_host | boolean | | |
| is_local | boolean | | |
| #is_left | boolean | | |
| #is_skins | boolean | | |
| #is_featured | boolean | | |
| #image_name | string | | |
| #is_dropdown | boolean | | |
| #timer_field_count_to_show | number | | |
| #owned_incompatible_prompt_color | Vector [r, g, b] | | |
| #modal_title_text | string | | |
| #modal_label_text | string | | |
| #buttons_visible | boolean | | |
| #no_buttons_visible | boolean | | |
| #single_button_visible | boolean | | |
| #two_buttons_visible | boolean | | |
| is_fixed_inventory | boolean | | |
| experimental_radio_button_state | string | | |
| classic_radio_button_state | string | | |

## 动画

| Animation Property Name | Type | Description |
| - | :-: | - |
| anim_type | enum | 可能的值：<br> `alpha`<br> `clip`<br> `color`<br> `flip_book`<br> `offset`<br> `size`<br> `uv`<br> `wait`<br> `aseprite_flip_book` |
| duration | number | |
| next | string | |
| destroy_at_end | string | |
| play_event | string | |
| end_event | string | |
| start_event | string | |
| reset_event | string | |
| easing | enum | 可能的值：<br> `linear`<br> `spring`<br> `in_quad`<br> `out_quad`<br> `in_out_quad`<br> `in_cubic`<br> `out_cubic`<br> `in_out_cubic`<br> `in_quart`<br> `out_quart`<br> `in_out_quart`<br> `in_quint`<br> `out_quint`<br> `in_out_quint`<br> `in_sine`<br> `out_sine`<br> `in_out_sine`<br> `in_expo`<br> `out_expo`<br> `in_out_expo`<br> `in_circ`<br> `out_circ`<br> `in_out_circ`<br> `in_bounce`<br> `out_bounce`<br> `in_out_bounce`<br> `in_back`<br> `out_back`<br> `in_out_back`<br> `in_elastic`<br> `out_elastic`<br> `in_out_elastic` |
| from | | |
| to | | |
| initial_uv | Vector [u, v] | |
| fps | int | 帧率 |
| frame_count | int | |
| frame_step | number | |
| reversible | boolean | 动画完成后以相反方向运行 |
| resettable | boolean | |
| scale_from_starting_alpha | boolean | |
| activated | boolean | |

有关 `aseprite_flip_book` 动画类型的更多信息，请参阅我们的 [Aseprite 动画](../json-ui/aseprite-animations.md) 页面。

## 全局变量

| 变量 | 备注 |
| - | - |
| $store_disabled | |
| $game_pad | 设备连接了控制器 |
| $mouse | 设备连接了鼠标 |
| $touch | |
| $trial | 游戏处于试用版 |
| $build_platform_UWP | |
| $win10_edition | |
| $ignore_add_servers | |
| $disable_gamertag_controls | |
| $console_edition | |
| $osx_edition | |
| $pocket_edition | |
| $education_edition | |
| $world_archive_support | |
| $file_picking_supported | |
| $desktop_screen | 如果选择了经典用户界面 |
| $pocket_screen | 如果选择了便携式用户界面 |
| $is_holographic | |
| $gear_vr | |
| $oculus_rift | |
| $is_living_room_mode | |
| $is_reality_mode | |
| $realms_beta | |
| $fire_tv | |
| $is_ios | |
| $apple_tv | |
| $is_windows_10_mobile | |
| $image_picking_not_supported | |
| $pre_release | |
| $ios | |
| $is_console | |
| $can_quit | |
| $is_settopbox | |
| $microsoft_os | |
| $apple_os | |
| $google_os | |
| $nx_os | |
| $horizontal_safezone_size | |
| $vertical_safezone_size | |
| $can_splitscreen | |
| $is_secondary_client | |
| $multiplayer_requires_live_gold | |
| $xbox_one | |
| $is_pregame | 如果是游戏外的屏幕。在世界、服务器或Realms中游玩时为游戏中 |
| $is_win10_arm | |
| $vibration_supported | |
| $is_mobile_vr | |
| $is_xboxlive_enabled | |
| $device_must_be_removed_for_xbl_signin | |
| $is_publish | 它是公开的而不是开发者版本 |
| $is_desktop | |
| $is_ps4 | |
| $is_on_3p_server | |
| $ignore_3rd_party_servers | |
| $is_berwick | |

## 硬编码的超链接

`#hyperlink` 不允许自定义URL。以下这些将会有效：

- `http://education.minecraft.net/eula`
- `http://pocketbeta.minecraft.net/p/how-to-join-and-leave-beta.html`
- `http://aka.ms/minecraftrealmsfb`
- `http://aka.ms/minecraftrealmsterms`
- `http://aka.ms/minecraftfb`
- `http://aka.ms/minecraftedusupport`
- `https://aka.ms/blockxboxmessages`
- `http://aka.ms/minecraftfbbeta`
- `https://minecraft.net/attribution`
- `http://aka.ms/mcedulogs`
- `https://minecraft.net/licensed-content/`
- `https://education.minecraft.net/eula`
- `https://aka.ms/mcedulogs`
- `https://aka.ms/minecraftrealmsterms`
- `https://aka.ms/minecraftfb`
- `https://aka.ms/minecraftfbbeta`
- `https://aka.ms/minecraftedusupport`
- `https://itunes.apple.com/us/app/minecraft/id479516143?mt=8`
- `https://account.xbox.com/Settings`
- `https://aka.ms/meeterms`
- `https://aka.ms/privacy`
- `https://aka.ms/MCBanned`
- `https://aka.ms/MCMultiplayerHelp`
- `https://aka.ms/meeeula`
- `https://aka.ms/mee_privacy`
- `https://www.minecraft.net/attribution/?hideChrome`
- `https://aka.ms/switchattribution`
- `https://www.minecraft.net/licensed-content/?hideChrome`
- `https://aka.ms/switchcontent`
- `https://social.xbox.com/changegamertag`

## 硬编码的按钮ID

部分按钮仅在特定屏幕中有效。

### 按钮ID：

- `button.menu_exit`
- `button.menu_cancel` (`Escape`键或控制器 `B`)
- `button.menu_inventory_cancel` (`打开物品栏` 快捷键)
- `button.menu_ok` (`Enter`键)
- `button.menu_select` (鼠标点击)
- `button.controller_select` (控制器 `X`)
- `button.menu_secondary_select`
- `button.controller_secondary_select`
- `button.controller_secondary_select_left`
- `button.controller_secondary_select_right` (控制器 `R3`)
- `button.controller_start`
- `button.menu_up` (`上箭头`键)
- `button.menu_down` (`下箭头`键)
- `button.menu_left` (`左箭头`键)
- `button.menu_right` (`右箭头`键)
- `button.menu_tab_left` (`菜单左标签` 快捷键或控制器 `左肩键`)
- `button.menu_tab_right` (`菜单右标签` 快捷键或控制器 `右肩键`)
- `button.menu_alternate_tab_left`
- `button.menu_alternate_tab_right`
- `button.menu_autocomplete` (使用 `Tab` 键)
- `button.menu_autocomplete_back`
- `button.controller_autocomplete`
- `button.controller_autocomplete_back`
- `button.menu_textedit_up` (使用 `上箭头`键)
- `button.menu_textedit_down` (使用 `下箭头`键)
- `button.controller_textedit_up`
- `button.controller_textedit_down`
- `button.menu_auto_place`
- `button.menu_inventory_drop` (`丢弃物品` 快捷键)
- `button.menu_inventory_drop_all` (`丢弃物品` + `控制键`)
- `button.menu_clear`
- `button.chat` (`打开聊天` 快捷键)
- `button.mobeffects` (`怪物效果` 快捷键)
- `key.emote` (`表情` 快捷键)
- `button.slot1` (表情轮) (`1`键)
- `button.slot2` (表情轮) (`2`键)
- `button.slot3` (表情轮) (`3`键)
- `button.slot4` (表情轮) (`4`键)
- `button.slot5` (表情轮) (`5`键)
- `button.slot6` (表情轮) (`6`键)
- `button.inventory_right` (`鼠标滚轮上滚`)
- `button.inventory_left` (`鼠标滚轮下滚`)
- `button.scoreboard`
- `button.hide_gui` (`F1`键)
- `button.hide_tooltips`
- `button.hide_paperdoll`
- `button.slot0`
- `button.slot1` (`1`键)
- `button.slot2` (`2`键)
- `button.slot3` (`3`键)
- `button.slot4` (`4`键)
- `button.slot5` (`5`键)
- `button.slot6` (`6`键)
- `button.slot7` (`7`键)
- `button.slot8` (`8`键)
- `button.slot9` (`9`键)
- `button.menu_vr_realign`
- `any` (字面意思)

### 特定屏幕按钮ID：

#### 设置 (`ui/settings_screen.json`)

- `button.open_content_log_history`
- `button.clear_content_log_files`
- `button.clear_msa_token_button`
- `button.terms_and_conditions_popup`
- `button.credits`
- `button.unlink_msa`
- `button.attribute_popup`
- `button.licensed_content`
- `button.font_license`
- `button.tos_hyperlink`
- `button.privpol_hyperlink`
- `button.tos_popup`
- `button.privpol_popup`
- `button.binding_button`
- `button.reset_binding`
- `button.reset_keyboard_bindings`
- `button.view_account_errors`

#### 书籍 (`ui/book_screen.json`)

- `button.prev_page`
- `button.next_page`
- `button.book_exit`

#### 聊天 (`ui/chat_screen.json`)

- `button.send`
- `button.chat_autocomplete`
- `button.chat_autocomplete_back`
- `button.chat_previous_message`
- `button.chat_next_message`
- `button.chat_menu_cancel`

#### 命令方块 (`ui/command_block_screen.json`)

- `command_block.input_minimize`
- `button.chat_autocomplete`
- `button.chat_autocomplete_back`

#### 评论 (`ui/comment_screen.json`)

- `button.comment_options_close`
- `button.comment_feed_options_close`
- `button.close_comments`
- `button.comment_next_button`
- `button.comment_prev_button`

#### 制作相关按钮（省略其余重复部分，整体结构保持一致）

#### Play (`ui/play_screen.json`)

- `button.menu_sign_in_to_view_realms`
- `button.menu_realms_world_item_edit`
- `button.menu_realms_feed`
- `button.menu_realms_world_item_remove`
- `button.menu_network_world_item`
- `button.menu_network_server_world_edit`
- `button.connect_to_third_party_server`
- `button.view_third_party_server_offers`
- `button.description_read_toggle`
- `button.news_read_toggle`
- `button.local_world_upload`
- `button.menu_start_local_world`
- `button.convert_legacy_world`
- `button.menu_local_world_item_edit`
- `button.menu_legacy_world_item_delete`
- `button.import_beta_retail_local_world`
- `button.import_beta_retail_legacy_world`
- `button.menu_network_add_friend`
- `button.menu_network_join_by_code`
- `button.menu_quick_play`
- `button.new_world_upload`
- `button.menu_local_world_create`
- `button.create_on_realms_button`
- `button.archived_world_upload`
- `button.menu_import_level`
- `button.menu_sync_legacy_worlds`
- `button.realms_warning_more_info`
- `button.menu_realm_world_trial`
- `button.menu_realm_nintendo_first_realm_purchase_button`
- `button.no_local_worlds_launch_help`
- `button.menu_network_join_by_code_popup_join`
- `button.join_server_anyway`
- `button.cancel_join_server`

### 其他

- `button.try_menu_exit`
- `button.close_dialog`
- `button.menu_play`
- `$play_button_target` (**硬编码**)
- `button.menu_store`
- `button.menu_achievements`
- `button.menu_settings`
- `button.signin`
- `button.menu_skins`
- `button.to_profile_screen`
- `button.menu_courses`
- `button.menu_tutorial`
- `button.featured_world`
- `button.switch_accounts`
- `button.launch_editions`
- `button.edu_feedback`
- `button.edu_resources`
- `button.menu_buy_game`
- `button.menu_invite_notification`
- `button.search`
- `button.hotbar_inventory_button`
- `button.select_offer`
- `button.action_button`
- `button.create_realm`
- `button.switch_accounts`
- `button.hotbar_select`
- `button.hotbar_ok`
- `button.slot_pressed`
- `button.hotbar_inventory_left`
- `button.hotbar_inventory_right`
- `button.hide_gui_all`
- `button.hide_tooltips_hud`
- `button.hide_paperdoll_hud`
- `button.slot_1`
- `button.slot_2`
- `button.slot_3`
- `button.slot_4`
- `button.slot_5`
- `button.slot_6`
- `button.slot_7`
- `button.slot_8`
- `button.slot_9`
- `button.slot_0`
- `button.chat`
- `button.menu_continue`
- `user_confirm_dialog.escape`
- `user_confirm_dialog.left_button`
- `user_confirm_dialog.middle_button`
- `user_confirm_dialog.rightcancel_button`
- `button.view_skin`
- `button.delete_action`
- `button.exit_student`
- `button.play_video`
- `button.menu_store_error`
- `button.left_panel_tab_increment`
- `button.left_panel_tab_decrement`
- `button.right_panel_tab_increment`
- `button.right_panel_tab_decrement`
- `button.layout_increment`
- `button.layout_decrement`
- `button.is_hovered`
- `button.container_take_all_place_all`
- `button.container_take_half_place_one`
- `button.container_auto_place`
- `button.coalesce_stack`
- `button.shape_drawing`
- `button.destroy_selection`
- `button.clear_selected_recipe`
- `button.clear_hotbar_or_remove_one`
- `button.clear_hotbar_or_drop`
- `button.container_reset_held`
- `button.container_auto_place`
- `button.container_slot_hovered`
- `button.button_hovered`
- `button.shift_pane_focus`
- `button.focus_left`
- `button.focus_right`
- `button.filter_toggle_hovered`
- `button.drop_one`
- `button.cursor_drop_one`
- `button.drop_all`
- `button.cursor_drop_all`
- `button.search_bar_clear`
- `button.search_bar_selected`
- `button.search_bar_deselected`
- `button.menu_leave_screen`
- `button.turn_doll`
- `button.select_skin`
- `button.skin_hovered`
- `button.skin_unhovered`
- `button.leave`
- `button.leave_on_device`
- `button.text_edit_box_selected`
- `button.text_edit_box_deselected`
- `button.text_edit_box_hovered`
- `button.text_edit_box_clear`
- `button.help`
- `button.menu_open_uri`
- `button.no_interaction`
- `button.copy_to_clipboard`
- ...

## 硬编码的合集名称

全部仅在特定屏幕中使用。

### 特定屏幕：

#### 书籍 (`ui/book_screen.json`)

- `book_pages`
- `pick_collection`

#### 捆绑购买警告 (`ui/bundle_purchase_warning_screen.json`)

- `owned_list`
- `unowned_list`

#### 聊天 (`ui/chat_screen.json`)

- `auto_complete`
- `font_colors`
- `host_main_collection`
- `players_collection`
- `host_teleport_collection`
- `host_time_collection`
- `host_weather_collection`

#### 选择Realm (`ui/choose_realm_screen.json`)

- `realms_collection`

#### 硬币购买 (`ui/coin_purchase_screen.json`)

- `coin_purchase_grid`

#### 评论 (`ui/comment_screen.json`)

- `comment_collection`

#### 内容日志历史 (`ui/content_log_history_screen.json`)

- `content_log_message`

#### 创建世界促销 (`ui/create_world_upsell_screen.json`)

- `world_list`
- `realm_list`

#### 自定义模板 (`ui/custom_templates_screen.json`)

- `templates_collection`

#### 动态 (`ui/feed_screen.json`)

- `feed_collection`

#### HUD (`ui/hud_screen.json`)

- `boss_bars`
- `chat_text_grid`
- `hotbar_items`
- `scoreboard_players`
- `scoreboard_scores`
- `left_helper_collection`
- `right_helper_collection`

#### 邀请 (`ui/invite_screen.json`)

- `online_platform_friends`
- `online_linked_account_friends`
- `online_xbox_live_friends`
- `offline_platform_friends`
- `offline_linked_account_friends`
- `offline_xbox_live_friends`

#### 管理动态 (`ui/manage_feed_screen.json`)

- `manage_feed_collection`

#### 清单验证 (`manifest_validation_screen.json`)

- `pack_errors`

#### 怪物效果 (`ui/mob_effects_screen.json`)

- `mob_effects_collection`

#### 游戏菜单 (`ui/pause_screen.json`)

- `players_collection`

#### PDP (`ui/pdp_screen.json`)

- `factory_collection`
- `ratings_star_collection`

#### 权限 (`ui/permissions_screen.json`)

- `players_collection` - 也在 `pause_screen.json` 中使用
- `permissions_collection`

#### Persona (`ui/persona_screen.json`)

- `color_collection`
- `skin_pack_in_grid_item`
- `persona_featured_skin_pack_collection`
- `body_size_collection`
- `arm_size_collection`
- `category_featured_collection`
- `main_featured_collection`
- `profile_featured_collection`
- `custom_section_collection`
- `featured_collection`
- `foobar_collection`
- `emote_collection`

#### Play (`ui/play_screen.json`)

- `friends_network_worlds`
- `cross_platform_friends_network_worlds`
- `lan_network_worlds`
- `personal_realms`
- `friends_realms`
- `servers_network_worlds`
- `third_party_server_network_worlds`
- `server_screenshot_collection`
- `server_games_collection`
- `local_worlds`
- `legacy_worlds`
- `beta_retail_local_worlds`
- `personal_realms`
- `loading_personal_realms`
- `friends_realms`
- `loading_friends_realms`

#### 投资组合 (`ui/portfolio_screen.json`)

- `photos`

#### 进度 (`ui/progress_screen.json`)

- `required_resourcepacks`
- `optional_resourcepacks`

#### Realms待处理邀请 (`ui/realms_pending_invitations_screen.json`)

- `pending_invites_collection`

#### Realms设置 (`ui/realms_settings_screen.json`)

- `additional_realms_subscriptions_collection`
- `realms_branch_collection`
- `realms_backup_collection`
- `members_collection`
- `invited_friends_collection`
- `uninvited_friends_collection`
- `blocked_players_collection`

#### 截图选择器 (`ui/screenshot_picker_screen.json`)

- `screenshotpicker_collection`

#### 服务器表单 (`ui/server_form.json`)

- `custom_form`
- `form_buttons`
- `custom_dropdown`

#### 设置 (`ui/settings_screen.json`)

- `keyboard_standard_collection`
- `keyboard_full_collection`
- `gamepad_collection`
- `languages`
- `realms_plus_subscriptions_collection`
- `additional_realms_subscriptions_collection`
- `#selected_pack_items_global`
- `#available_pack_items_global`
- `#realms_pack_items_global`
- `#unowned_pack_items_global`
- `#invalid_pack_items_global`
- `#selected_pack_items_level`
- `#available_pack_items_level`
- `#realms_pack_items_level`
- `#unowned_pack_items_level`
- `#invalid_pack_items_level`
- `#selected_pack_items_addon`
- `#available_pack_items_addon`
- `#realms_pack_items_addon`
- `#unowned_pack_items_addon`
- `#invalid_pack_items_addon`
- `experimental_toggles`
- `world_panel`
- `world_template_panel`
- `resource_panel`
- `behavior_panel`
- `skin_panel`
- `cache_panel`
- `dependent_packs_panel`
- `dependency_panel`

#### 结构方块 (`ui/structure_editor_screen.json`)

- `save_size_grid`
- `save_offset_grid`
- `load_offset_grid`
- `export_size_grid`
- `export_offset_grid`

#### 种子选择器 (`ui/ugc_viewer_screen.json`)

- `ugc_items`

#### 世界模板 (`ui/world_templates_screen.json`)

- `world_templates`
- `realms_plus_templates`
- `custom_world_templates`
- `#suggested_offers_collection`

#### 铁砧 (`ui/anvil_screen.json`)

- `anvil_input_items`
- `anvil_material_items`
- `anvil_result_items`

#### 信标 (`ui/beacon_screen.json`)

- `beacon_payment_items`
- `speed`
- `haste`
- `resist`
- `jump`
- `strength`
- `regen`
- `extra`
- `confirm`
- `cancel`

#### 酿造台 (`ui/brewing_stand_screen.json`)

- `brewing_fuel_item`
- `brewing_input_item`
- `brewing_result_items`

#### 制图台 (`ui/cartography_screen.json`)

- `cartography_input_items`
- `cartography_additional_items`
- `cartography_result_items`

#### 附魔台 (`ui/enchanting_table_screen.json`)

- `enchanting_input_items`
- `enchanting_lapis_items`
- `#enchant_buttons`

#### 熔炉 (`ui/furnace_screen.json`)

- `furnace_ingredient_items`
- `furnace_fuel_items`
- `furnace_output_items`

#### 砧 (`ui/grindstone_screen.json`)

- `grindstone_input_items`
- `grindstone_additional_items`
- `grindstone_result_items`

#### 织布台 (`ui/loom_screen.json`)

- `loom_input_items`
- `loom_dye_items`
- `loom_material_items`
- `loom_result_items`
- `patterns`

#### 铁匠台 (`ui/smithing_table_screen.json`)

- `smithing_table_input_items`
- `smithing_table_material_items`
- `smithing_table_result_items`

#### 石匠 (`ui/stonecutter_screen.json`)

- `stonecutter_input_items`
- `stonecutter_result_items`
- `stones`

#### 村民交易2 (`ui/trade_2_screen.json`)

- `trade2_ingredient1_item`
- `trade2_ingredient2_item`
- `trade2_result_item`
- `trade_item_1`
- `trade_item_2`
- `sell_item`
- `trades`
- `trade_tiers`

## 硬编码的绑定名称

部分仅在特定屏幕中有效。

### 特定屏幕：

#### 账户转移错误 (`ui/account_transfer_error_screen.json`)

- `#error_title_text`
- `#error_number_label`
- `#error_number`
- `#correlation_id_label`
- `#correlation_id`

#### 添加外部服务器 (`ui/add_external_server_screen.json`)

- `#play_button_enabled`
- `#play_button_disabled`
- `#save_button_enabled`
- `#save_button_disabled`

#### 进行中的临时 (`ui/adhoc_in_progress_screen.json`)

- `#adhoc_title`

#### 认证 (`ui/authentication_screen.json`)

- `#sign_in_visible`
- `#sign_in_ios_visible`
- `#sign_in_button_visible`
- `#sign_in_ios_buttons_visible`
- `#authentication_message`
- `#confirm_button_enabled`
- `#edu_store_visible`
- `#edu_store_purchase_info`
- `#asking_to_buy_visible`
- `#confirming_purchase_visible`
- `#demo_choice_visible`
- `#eula_visible`
- `#popup_text`
- `#popup_message_student_text`
- `#popup_message_student_visible`
- `#generic_popup_link_visible`
- `#trial_purchase_link_visible`
- `#show_popup_dismiss_button`

#### 书籍 (`ui/book_screen.json`)

- `#screenshot_path`
- `#is_photo_page`
- `#is_text_page`
- `#pick_grid_dimensions`
- `#page_number`
- `#title_text_box_item_name`
- `#author_editable`
- `#author_text_box_item_name`
- `#editable`
- `#viewing`
- `#signing`
- `#picking`
- `#exporting`
- `#page_visible`
- `#pick_item_visible`
- `#close_button_visible`
- `#edit_controls_active`
- `#finalize_button_enabled`

#### Braze (`ui/braze_screen.json`)

- `#image_texture`

#### 捆绑购买警告 (`ui/bundle_purchase_warning_screen.json`)

- `#banner_visible`
- `#offer_title`
- `#keyart_path`
- `#keyart_texture_file_system`

#### 聊天 (`ui/chat_screen.json`)

- `#keyboard_being_use`
- `#keyboard_button_focus_override_up`
- `#keyboard_button_focus_override_down`
- `#keyboard_button_visible`
- `#send_button_visible`
- `#send_button_accessibility_text`
- `#chat_visible`
- `#message_text_box_content`
- `#text_edit_box_focus_override_up`
- `#text_edit_box_focus_override_down`
- `#auto_complete_item`
- `#auto_complete_text`
- `#get_grid_size`
- `#chat_title_text`
- `#chat_typeface_visible`

#### 选择Realm (`ui/choose_realm_screen.json`)

- `#realms_grid_dimension`
- `#world_button_focus_identifier`
- `#ten_player_button_visible`
- `#two_player_button_visible`
- `#realms_world_player_count`
- `#realms_game_online`
- `#realms_game_unavailable`
- `#realms_game_offline`

#### 硬币购买 (`ui/coin_purchase_screen.json`)

- `#bonus_coins`
- `#coins_without_bonus`
- `#coin_offer_texture_name`
- `#coin_offer_texture_file_system`
- `#bonus_coins_visible`
- `#price_text`
- `#coins_required_for_purchase`
- `#show_missing_coins`
- `#coin_offer_size`
- `#has_coin_offers`
- `#coin_loading_visible`

#### 命令方块 (`ui/command_block_screen.json`)

- `#maximized_input_visible`
- `#block_type_icon_texture`
- `#close_button_visible_binding_name`
- `#command_impulse_mode`
- `#command_chain_mode`
- `#command_repeat_mode`
- `#block_type_dropdown_toggle_label`
- `#block_type_dropdown_label_color_binding`
- `#block_type_dropdown_enabled`
- `#command_conditional_mode`
- `#command_unconditional_mode`
- `#condition_dropdown_toggle_label`
- `#condition_dropdown_enabled`
- `#command_always_on_mode`
- `#command_needs_redstone_mode`
- `#redstone_dropdown_enabled`
- `#command_hover_note`
- `#execute_on_first_tick_enabled`
- `#command_tick_delay`
- `#command_text_edit`
- `#command_output_text`
- `#previous_block_type_text`
- `#previous_block_type_text_color`
- `#previous_condition_mode_text`
- `#previous_redstone_mode_text`
- `#minimize_button_visible_binding_name`

#### 评论 (`ui/comment_screen.json`)

- `#report_to_club_button_visible_feeditem`
- `#report_to_enforcement_button_visible_feeditem`
- `#delete_button_visible_feeditem`
- `#report_to_club_button_visible_comment`
- `#report_to_enforcement_button_visible_comment`
- `#delete_button_visible_comment`
- `#comment_buttons_visible`
- `#feed_comment_page_collection_length`
- `#comment_content`
- `#is_author_linked_account`
- `#content`
- `#text_visible`
- `#likes_and_comments`
- `#screenshot_texture`
- `#screenshot_texture_source`
- `#textpost_content`
- `#textpost_visible`
- `#comment_text_box`
- `#comment_platform_tag`
- `#comment_gamertag`
- `#likes_and_time_since_comment_post`
- `#author_gamertag`
- `#time_since_feed_post`
- `#author_platform_tag`
- `#author_gamertag`

#### 确认MSA解除绑定 (`ui/confirm_msa_unlink_screen.json`)

- `#unlink_warning_text`
- `#unlink_consequences_acknowledged`
- `#confirm_0`
- `#confirm_0_enabled`
- `#confirm_1`
- `#confirm_1_enabled`
- `#confirm_2`
- `#confirm_2_enabled`
- `#confirm_3`
- `#confirm_3_enabled`

#### 内容日志历史 (`ui/content_log_history_screen.json`)

- `#content_log_text`
- `#messages_size`

#### 创建世界促销 (`ui/create_world_upsell.json`)

- `#realm_button_text`
- `#realm_trial_available`

#### 铁砧 (`ui/anvil_screen.json`)

- `#cost_text`
- `#cost_text_green`
- `#cost_text_red`

#### 信标 (`ui/beacon_screen.json`)

- `#supports_netherite`
- `#extra_image_selection`

#### 酿造台 (`ui/brewing_stand_screen.json`)

- `#empty_bottle_image_visible`
- `#empty_fuel_image_visible`
- `#brewing_bubbles_ratio`
- `#brewing_fuel_ratio`
- `#brewing_arrow_ratio`

#### 制图台 (`ui/cartography_screen.json`)

- `#is_none_mode`
- `#is_clone_mode`
- `#is_rename_mode`
- `#is_basic_map_mode`
- `#is_locator_map_mode`
- `#is_extend_mode`
- `#is_locked_mode`
- `#output_description`

#### 附魔台 (`ui/enchanting_table_screen.json`)

- `#selectable_dust_is_visible`
- `#unselectable_dust_is_visible`
- `#runes`
- `#cost`
- `#unselectable_button_visibility`
- `#selectable_button_visibility`
- `#show_selected_button_highlight`
- `#active_enchant`
- `#inactive_enchant`
- `#input_item_id`
- `#output_item_id`
- `#enchant_hint`
- `#player_level_color`
- `#player_level_info`
- `#enchant_error`

#### 熔炉 (`ui/furnace_screen.json`)

- `#furnace_arrow_ratio`
- `#furnace_flame_ratio`
- `#output_name`

#### 马匹 (`ui/horse_screen.json`)

- `#entity_id`
- `#equip_grid_dimensions`
- `#inv_grid_dimensions`
- `#sadle_slot_centered`
- `#has_saddle_slot`
- `#has_armor_slot`
- `#has_only_armor_slot`
- `#has_only_carpet_slot`
- `#has_armor_and_saddle_slot`
- `#has_carpet_and_saddle_slot`
- `#is_chested`
- `#renderer_tab_toggle`
- `#chest_tab_toggle`

#### 织布台 (`ui/loom_screen.json`)

- `#pattern_cell_background_texture`
- `#container_cell_background_texture`
- `#empty_image_visible`
- `#banner_patterns`
- `#banner_colors`
- `#pattern_selector_total_items`
- `#result_patterns`
- `#result_colors`
- `#is_right_tab_loom`
- `#is_left_tab_patterns`

#### 石匠 (`ui/stonecutter_screen.json`)

- `#stone_cell_background_texture`
- `#container_cell_background_texture`
- `#item_stack_count`
- `#stone_selector_total_items`
- `#has_input_item`
- `#is_right_tab_stonecutter`
- `#is_left_tab_stones`

#### 死亡 (`ui/death_screen.json`)

- `#death_reason_text`
- `#respawn_visible`
- `#quit_enabled`
- `#quit_visible`
- `#buttons_and_deathmessage_visible`

#### 村民交易2 (`ui/trade2_screen.json`)

- `#name_label`
- `#trade_cell_background_texture`
- `#trade_item_count`
- `#single_slash_visible`
- `#double_slash_visible`
- `#second_trade_item_count`
- `#trade_price_different`
- `#trade_cross_out_visible`
- `#padding_around_sell_item`
- `#trade_possible`
- `#trade_toggle_state`
- `#trade_toggle_enabled`
- `#trade_tier_total`
- `#tier_name`
- `#is_tier_unlocked`
- `#is_left_tab_trade`
- `#show_level`
- `#tier_visible`
- `#trade_selector_total`
- `#has_second_buy_item`
- `#exp_bar_visible`
- `#exp_progress`
- `#exp_possible_progress`
- `#trade_details_button_1_visible`
- `#trade_details_button_2_visible`
- `#enchantment_details_button_visible`
- `#item_valid`

### 值取决于所在屏幕：

- `#title_text`
- `#body_text`
- `#hover_text`
- `#cross_out_icon`
- `#is_left_tab_inventory`
- `#selected_hover_text`

### 其他：

- `#tts_dialog_body`
- `#button_enabled`
- `#using_touch`
- `#close_button_visible`

## 设置

### 滑块

| 名称 | 滑块名称 | 值绑定名称 | TTS 值 (`tts_value_changed`) | 滑块文本 | 启用绑定名称 |
| - | - | - | - | - | - |
| 亮度 | `gamma` | `#gamma` | `#gamma_text_value` | `#gamma_slider_label` | `#gamma_enabled` |
| 亮度 (VR) | `vr_gamma` | `#vr_gamma` | `#vr_gamma_text_value` | `#vr_gamma_slider_label` | `#vr_gamma_enabled` |
| HUD 不透明度 | `interface_opacity` | `#interface_opacity` | `#interface_opacity_text_value` | `#interface_opacity_slider_label` | `#interface_opacity_enabled` |
| HUD 不透明度 (分屏) | `splitscreen_interface_opacity` | `#splitscreen_interface_opacity` | `#interface_opacity_text_value` | `#splitscreen_interface_opacity_slider_label` | `#splitscreen_interface_opacity_enabled` |
| 视野 | `field_of_view` | `#field_of_view` | `#field_of_view_text_value` | `#field_of_view_slider_label` | `#field_of_view_enabled` |

### 切换

| 名称 | 切换名称 | 状态绑定名称 | 启用绑定名称 |
| - | - | - | - |
| 翻转 Y 轴 (鼠标) | `keyboard_mouse_invert_y_axis` | `#keyboard_mouse_invert_y_axis` | `#keyboard_mouse_invert_y_axis_enabled` |
| 自动跳跃 (鼠标) | `keyboard_mouse_autojump` | `#keyboard_mouse_autojump` | `#keyboard_mouse_autojump_enabled` |
| 显示完整键盘选项 | `keyboard_show_full_keyboard_options` | `#keyboard_show_full_keyboard_options` | `#keyboard_show_full_keyboard_options_enabled` |
| 隐藏键盘工具提示 | `hide_keyboard_tooltips` | `#hide_keyboard_tooltips` | `#hide_keyboard_tooltips_enabled` |
| 内容文件日志 | `content_log_file` | `#content_log_file` | `#content_log_file_enabled` |
| 内容 GUI 日志 | `content_log_gui` | `#content_log_gui` | `#content_log_gui_enabled` |
| 使用 SSO | `ad_use_single_sign_on` | `#ad_use_single_sign_on` | |
| 自动更新关闭 | `#auto_update_mode_off` | `#auto_update_mode_off` | |
| 自动更新开启（使用移动数据） | `#auto_update_mode_on_with_cellular` | `#auto_update_mode_on_with_cellular` | |
| 仅在 WiFi 上自动更新 | `#auto_update_mode_on_wifi_only` | `#auto_update_mode_on_wifi_only` | |
| 自动更新启用 | `auto_update_enabled` | `#auto_update_enabled` | |
| 跨平台启用 | `crossplatform_toggle` | `#crossplatform_toggle` | `#crossplatform_toggle_enabled` |
| 允许移动数据 | `allow_cellular_data` | `#allow_cellular_data` | `#allow_cellular_data_enabled` |
| Websocket 加密 | `websocket_encryption` | `#websocket_encryption` | `#websocket_encryption_enabled` |
| 仅允许受信任的皮肤 | `only_trusted_skins_allowed` | `#only_trusted_skins_allowed` | `#only_trusted_skins_allowed_enabled` |
| 存储位置外部 | `#storage_location_radio_external` | `#storage_location_radio_external` | `#file_storage_location_enabled` |
| 存储位置应用 | `#storage_location_radio_package` | `#storage_location_radio_package` | `#file_storage_location_enabled` |
| 第一人称视角 | `#thirdperson_radio_first` | `#thirdperson_radio_first` | `#third_person_dropdown_enabled` |
| 第三人称背面视角 | `#thirdperson_radio_third_back` | `#thirdperson_radio_third_back` | `#third_person_dropdown_enabled` |
| 第三人称正面视角 | `#thirdperson_radio_third_front` | `#thirdperson_radio_third_front` | `#third_person_dropdown_enabled` |
| 全屏 | `full_screen` | `#full_screen` | `#full_screen_enabled` |
| 隐藏手部 | `hide_hand` | `#hide_hand` | `#hide_hand_enabled` |
| 隐藏手部 (VR) | `vr_hide_hand` | `#vr_hide_hand` | `#vr_hide_hand_enabled` |
| 隐藏纸娃娃 | `hide_paperdoll` | `#hide_paperdoll` | `#hide_paperdoll_enabled` |
| 隐藏 HUD | `hide_hud` | `#hide_hud` | `#hide_hud_enabled` |
| 隐藏 HUD (VR) | `vr_hide_hud` | `#vr_hide_hud` | `#vr_hide_hud_enabled` |
| 屏幕动画 | `screen_animations` | `#screen_animations` | `#screen_animations_enabled` |
| 水平分屏 | `#split_screen_radio_horizontal` | `#split_screen_radio_horizontal` | `#split_screen_dropdown_enabled` |
| 垂直分屏 | `#split_screen_radio_vertical` | `#split_screen_radio_vertical` | `#split_screen_dropdown_enabled` |
| 显示自动保存图标 | `show_auto_save_icon` | `#show_auto_save_icon` | `#show_auto_save_icon_enabled` |
| 轮廓选择 | `classic_box_selection` | `#classic_box_selection` | `#classic_box_selection_enabled` |
| 轮廓选择 (VR) | `vr_classic_box_selection` | `#vr_classic_box_selection` | `#vr_classic_box_selection_enabled` |
| 在游戏中显示玩家名称 | `ingame_player_names` | `#ingame_player_names` | `#ingame_player_names_enabled` |
| 在游戏中显示玩家名称 (分屏) | `splitscreen_ingame_player_names` | `#splitscreen_ingame_player_names` | `#splitscreen_ingame_player_names_enabled` |
| 视角摇摆 | `view_bobbing` | `#view_bobbing` | `#view_bobbing_enabled` |
| 摄像机抖动 | `camera_shake` | `#camera_shake` | `#camera_shake_enabled` |
| 精美叶子 | `transparent_leaves` | `#transparent_leaves` | `#transparent_leaves_enabled` |
| 精美叶子 (VR) | `vr_transparent_leaves` | `#vr_transparent_leaves` | `#vr_transparent_leaves_enabled` |
| 精美气泡 | `bubble_particles` | `#bubble_particles` | `#bubble_particles_enabled` |
| 渲染云彩 | `render_clouds` | `#render_clouds` | `#render_clouds_enabled` |
| 精美云彩 | `fancy_skies` | `#fancy_skies` | `#fancy_skies_enabled` |
| 平滑光照 | `smooth_lighting` | `#smooth_lighting` | `#smooth_lighting_enabled` |
| 平滑光照 (VR) | `graphics_toggle` | `#graphics_toggle` | `#graphics_toggle_enabled` |
| 图形 | `graphics_toggle` | `#graphics_toggle` | `#graphics_toggle_enabled` |
| 视野 | `field_of_view_toggle` | `#field_of_view_toggle` | `#field_of_view_toggle_enabled` |
| 经典 UI 配置 | `#ui_profile_radio_classic` | `#ui_profile_radio_classic` | `#ui_profile_dropdown_enabled` |
| 口袋 UI 配置 | `#ui_profile_radio_pocket` | `#ui_profile_radio_pocket` | `#ui_profile_dropdown_enabled` |
| 纹素抗锯齿 | `texel_aa` | `#texel_aa` | `#texel_aa_enabled` |
| 3D 渲染 (VR) | `vr_3d_rendering` | `#vr_3d_rendering` | `#vr_3d_rendering_enabled` |
| 镜像纹理 (VR) | `vr_mirror_texture` | `#vr_mirror_texture` | `#vr_mirror_texture_enabled` |
| 手部指针可见 (VR) | `vr_hand_pointer` | `#vr_hand_pointer` | `#vr_hand_pointer_enabled` |
| 手部可见 (VR) | `vr_hands_visible` | `#vr_hands_visible` | `#vr_hands_visible_enabled` |
| 启用自动 TTS | `enable_auto_text_to_speech` | `#enable_auto_text_to_speech` | `#enable_auto_text_to_speech_enabled` |
| 启用 UI TTS | `enable_ui_text_to_speech` | `#enable_ui_text_to_speech` | `#enable_ui_text_to_speech_enabled` |
| 启用聊天 TTS | `enable_chat_text_to_speech` | `#enable_chat_text_to_speech` | `#enable_chat_text_to_speech_enabled` |
| 启用打开聊天消息 | `enable_open_chat_message` | `#enable_open_chat_message` | `#enable_open_chat_message_enabled` |
| 摄像机抖动 | `camera_shake` | `#camera_shake` | `#camera_shake_enabled` |
| 语言 (合集) | `languages` | `#language_initial_selected` | |

## 物品标附值 (`#item_id_aux`)

| 名称 | ID | 标附值 |
| - | :-: | :-: |
| 钻石 | 306 | 20054016 |
| 翡翠 | 519 | 34013184 |
| 黄金锭 | 308 | 20185088 |
| 铁锭 | 307 | 20119552 |
| 下界合金锭 | 616 | 40370176 |
| 旗帜 | 574 | 37617664 |
| 鞍 | 373 | 24444928 |
| 制图台 | -200 | -13107200 |
| 箱子 | 54 | 3538944 |
| 工作台 | 58 | 3801088 |
| 织布机 | -204 | -13369344 |
| 切石机 | -197 | -12910592 |

#### 如何计算区块物品标附值：

标附值 = ID \* 65536

ID = 标附值 / 65536  
65536 = 标附值 / ID  

获取所有物品 ID [在这里](https://docs.microsoft.com/en-us/minecraft/creator/reference/content/addonsreference/examples/addonitems)。
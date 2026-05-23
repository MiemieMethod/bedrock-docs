# 附着物定义

本页列出国际版资源包附着物定义文件的主要结构。附着物定义文件位于`attachables/`目录，根键为`minecraft:attachable`。本页内容基于VisualReference中的`minecraft:actor_resource_definition`系列版本，不包含中国版私有接口。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 附着物定义文件使用的格式版本。 |
| `minecraft:attachable` | 对象 | 未设置 | 附着物定义根对象。 |

## `minecraft:attachable`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 附着物描述对象，声明标识符与渲染资源绑定。 |

## `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 标识符 | 未设置 | 附着物标识符，通常与目标物品标识符对应。 |
| `min_engine_version` | 版本 | 未设置 | 最低引擎版本要求。 |
| `materials` | 对象或字符串 | 未设置 | 材质短名称映射。 |
| `textures` | 对象或字符串 | 未设置 | 纹理短名称映射。 |
| `geometry` | 对象或字符串 | 未设置 | 几何体短名称映射。 |
| `animations` | 对象或字符串 | 未设置 | 动画与动画控制器短名称映射。 |
| `render_controllers` | 字符串数组、对象数组或Molang表达式 | 未设置 | 渲染控制器列表。 |
| `particle_effects` | 对象或字符串 | 未设置 | 粒子特效短名称映射。 |
| `particle_emitters` | 对象或字符串 | 未设置 | 粒子发射器短名称映射。 |
| `sound_effects` | 对象或字符串 | 未设置 | 音效短名称映射。 |
| `scripts` | 对象 | 未设置 | 附着物脚本设置。 |
| `spawn_egg` | 对象 | 未设置 | 刷怪蛋外观字段。 |
| `item` | 对象、字符串或Molang表达式 | 未设置 | 物品筛选条件。 |
| `queryable_geometry` | 字符串 | 未设置 | 可查询几何体键。 |
| `enable_attachables` | 布尔值 | 未设置 | 是否启用附着物层。 |
| `held_item_ignores_lighting` | 布尔值 | 未设置 | 手持物品是否忽略光照。 |
| `hide_armor` | 布尔值 | 未设置 | 是否隐藏盔甲层。 |

## `scripts`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `animate` | 字符串、字符串数组、对象数组或Molang表达式 | 未设置 | 每帧执行的动画条目。 |
| `initialize` | Molang数组或字符串数组 | 未设置 | 初始化脚本。 |
| `parent_setup` | Molang表达式 | 未设置 | 父级挂接初始化脚本。 |
| `pre_animation` | Molang数组或字符串数组 | 未设置 | 动画求值前脚本。 |
| `scale` | Molang表达式 | 未设置 | 整体缩放。 |
| `scaleX`/`scaleY`/`scaleZ` | Molang表达式 | 未设置 | 分轴缩放。 |
| `hide_held_items` | Molang表达式 | 未设置 | 返回非`0`时隐藏手持物品。 |
| `should_update_bones_and_effects_offscreen` | Molang表达式 | 未设置 | 返回非`0`时离屏仍更新骨骼和特效。 |
| `should_update_effects_offscreen` | Molang表达式 | 未设置 | 返回非`0`时离屏仍更新特效。 |
| `variables` | 对象 | 未设置 | 脚本变量可见性设置。 |

`variables`当前常见条目形态为`variable.xxx: "public"`，用于将变量公开给其他活动对象读取。

## `spawn_egg`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `base_color` | 字符串 | 未设置 | 刷怪蛋基色。 |
| `overlay_color` | 字符串 | 未设置 | 刷怪蛋覆盖色。 |
| `texture` | 字符串 | 未设置 | 刷怪蛋纹理。 |
| `texture_index` | 整数 | 未设置 | 刷怪蛋纹理排列值。 |

## 版本兼容性

| 版本 | 主要差异 |
| --- | --- |
| `1.8.0` | 提供附着物与客户端实体的基础渲染资源绑定字段。 |
| `1.10.0` | 补充`item`、`queryable_geometry`与离屏更新脚本字段。 |
| `1.26.0` | 明确`scripts.animate`与脚本数组字段的多形态写法，并补充`hide_held_items`。 |

## 相关参考

- [客户端实体定义](client-entity.md)
- [渲染控制器](render-controller.md)
- [动画定义](animation.md)

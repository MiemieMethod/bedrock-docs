# 自定义方块系列教程

自定义方块从行为包定义开始，再由资源包提供名称、纹理、模型和声音。简单方块可以只使用完整立方体和纹理；复杂方块可以使用自定义几何体、材质实例、碰撞箱、选择箱、破坏时间、亮度和战利品表。

## 入门教程

/// html | div.grid.cards
- :material-cube-outline: **第一个方块**

    ---

    学习 `minecraft:block` 结构、纹理图集和本地化。

    [:octicons-arrow-right-24: 开始](adding-custom-blocks.md)

- :material-table-furniture: **自定义工作台**

    ---

    使用 `minecraft:crafting_table` 组件创建带自定义界面的工作台。

    [:octicons-arrow-right-24: 开始](adding-custom-crafting-table.md)
///

## 外观与渲染

/// html | div.grid.cards
- :material-image: **方块外观**

    ---

    纹理、材质实例、渲染方法、几何体与着色。

    [:octicons-arrow-right-24: 阅读](block-visuals.md)

- :material-palette: **方块着色**

    ---

    `tint_color`、`overlay_color`、`tint_method` 与地图颜色。

    [:octicons-arrow-right-24: 阅读](block-tinting.md)

- :material-animation: **翻书动画纹理**

    ---

    `flipbook_textures.json` 制作逐帧动画纹理。

    [:octicons-arrow-right-24: 阅读](flipbook-textures.md)

- :material-shape: **纹理变种**

    ---

    通过 `variations` 为方块随机分配不同纹理。

    [:octicons-arrow-right-24: 阅读](texture-variation.md)

- :material-eye-off: **方块剔除**

    ---

    在相邻方块时剔除（隐藏）特定面，如玻璃。

    [:octicons-arrow-right-24: 阅读](block-culling.md)

- :material-glass-fragile: **自定义玻璃**

    ---

    `blend` 渲染方法 + 剔除规则完整示例。

    [:octicons-arrow-right-24: 阅读](custom-glass.md)
///

## 状态与行为

/// html | div.grid.cards
- :material-state-machine: **方块状态与置换**

    ---

    声明状态、书写置换条件、Script API 读写与状态上限突破。

    [:octicons-arrow-right-24: 阅读](block-states.md)

- :material-puzzle: **方块萃取**

    ---

    `placement_direction`、`placement_position`、`connection` 与 `multi_block`。

    [:octicons-arrow-right-24: 阅读](block-traits.md)

- :material-code-tags: **自定义组件与事件**

    ---

    注册自定义组件，处理12种事件钩子。

    [:octicons-arrow-right-24: 阅读](block-events.md)

- :material-volume-high: **方块声音**

    ---

    配置 `blocks.json` 音效、`sound_definitions.json` 与 Script API 播放。

    [:octicons-arrow-right-24: 阅读](block-sounds.md)

- :material-tag: **方块标签**

    ---

    使用 `tag:` 前缀与 Molang 查询函数，以及 `minecraft:tags` 组件。

    [:octicons-arrow-right-24: 阅读](block-tags.md)
///

## 朝向与方向

/// html | div.grid.cards
- :material-compass: **方块朝向**

    ---

    轴对齐、方块面依附、4向基本朝向与6向全方向。

    [:octicons-arrow-right-24: 阅读](block-orientation.md)

- :material-compass-rose: **16向朝向**

    ---

    通过自定义状态 + 脚本实现每22.5°一个方向。

    [:octicons-arrow-right-24: 阅读](intercardinal-orientation.md)

- :material-door: **自定义活板门**

    ---

    4方向 × 上下 × 开关的完整活板门示例。

    [:octicons-arrow-right-24: 阅读](custom-trapdoors.md)
///

## 破坏与战利品

/// html | div.grid.cards
- :material-pickaxe: **工具破坏与战利品**

    ---

    `seconds_to_destroy`、工具品质标签与 `match_tool` 战利品条件。

    [:octicons-arrow-right-24: 阅读](tool-based-destruction.md)

- :material-diamond: **矿石战利品表**

    ---

    限制工具掉落、附魔过滤与经验球脚本。

    [:octicons-arrow-right-24: 阅读](ore-loot-tables.md)
///

## 交互与特效

/// html | div.grid.cards
- :material-lightning-bolt: **红石联动**

    ---

    绝缘体、导体、消费者与生产者的完整实现。

    [:octicons-arrow-right-24: 阅读](redstone-blocks.md)

- :material-magic-staff: **方块效果**

    ---

    踩踏、跌落与定时范围效果的脚本实现。

    [:octicons-arrow-right-24: 阅读](applying-effects.md)
///

## 进阶示例

/// html | div.grid.cards
- :material-sprout: **自定义农作物**

    ---

    8阶段生长、随机刻触发与右键收割完整示例。

    [:octicons-arrow-right-24: 阅读](custom-crops.md)

- :material-view-grid-plus: **多方块结构**

    ---

    使用 `minecraft:multi_block` 萃取创建跨多格的方块。

    [:octicons-arrow-right-24: 阅读](multi-blocks.md)
///

## 方块调试重点

- 方块定义放在行为包 `blocks` 目录。
- 纹理短名写在资源包 `textures/terrain_texture.json`。
- 方块显示名写作 `tile.<identifier>.name`。
- 自定义方块需要行为包和资源包同时启用。
- 复杂渲染问题优先检查 `minecraft:geometry` 和 `minecraft:material_instances`。
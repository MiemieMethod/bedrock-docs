# 相机定义

本页列出国际版附加包相机定义中与瞄准辅助有关的JSON文件结构。资料来自Microsoft Learn相机参考；本页不包含中国版网易ModSDK相机接口、JSON UI接口、Minecraft编辑器视图设置或`/camera`命令运行时语法。

/// warning | 范围
本批次CameraReference仅列出瞄准辅助分类和瞄准辅助预设。相机预设、样条相机和相机命令等内容应以其对应参考为准，不能从本页字段推导。
///

## 文件根对象

相机瞄准辅助定义使用独立JSON根对象。Microsoft Learn说明，瞄准辅助分类和瞄准辅助预设均要求`format_version`至少为`1.21.50`。

| 根键 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 文件使用的JSON架构版本。瞄准辅助分类与瞄准辅助预设要求至少为`1.21.50`。 |
| `minecraft:aim_assist_categories` | 对象 | 未设置 | 单个相机瞄准辅助分类定义。 |
| `minecraft:aim_assist_preset` | 对象 | 未设置 | 单个相机瞄准辅助预设定义。 |

## 定义结构对应关系

以下名称来自Microsoft Learn的Camera Definitions页面，用于对应本页后续结构。

| Camera Definitions名称 | 对应结构 |
| --- | --- |
| CameraAimAssistCategoriesDefinition | `minecraft:aim_assist_categories`根对象中的`categories`字段。 |
| CameraAimAssistCategoryDefinition | `categories`数组中的单个分类项。 |
| CameraAimAssistCategoryPriorities | 分类项中的`priorities`对象。 |
| CameraAimAssistPresetDefinition | `minecraft:aim_assist_preset`对象。 |
| Aim Assist Categories | `minecraft:aim_assist_categories`文件根对象。 |
| Aim Assist Preset | `minecraft:aim_assist_preset`文件根对象。 |

## `minecraft:aim_assist_categories`

`minecraft:aim_assist_categories`定义供`minecraft:aim_assist_preset`引用的瞄准辅助分类集合。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `categories` | 对象数组 | 未设置 | 分类列表。每个元素定义一个可在瞄准辅助预设中查找和引用的分类。 |

### 分类项

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `name` | 字符串 | 未设置 | 分类名称，用于瞄准辅助预设查找。 |
| `priorities` | 对象 | 未设置 | 目标选择优先级集合。 |

### `priorities`

`priorities`控制同一分类中不同方块和实体参与瞄准辅助选择时的优先级。Microsoft Learn说明，较大的优先级数值具有更高优先级。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `block_default` | 整数 | 未设置 | 可选。未在`blocks`中列出的方块使用的默认瞄准辅助目标优先级。 |
| `blocks` | 对象 | 未设置 | 可选。方块标识符到瞄准辅助目标优先级的映射。 |
| `entities` | 对象 | 未设置 | 可选。实体标识符到瞄准辅助目标优先级的映射。 |
| `entity_default` | 整数 | 未设置 | 可选。未在`entities`中列出的实体使用的默认瞄准辅助目标优先级。 |

## `minecraft:aim_assist_preset`

`minecraft:aim_assist_preset`定义一个可引用瞄准辅助分类的预设。预设通过赋命名空间标识符区分，并可为徒手、默认物品和特定物品指定分类。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 预设的赋命名空间标识符。命名空间和名称必须使用冒号分隔。 |
| `default_item_settings` | 字符串 | 未设置 | 可选。`item_settings`未匹配到的物品使用的默认瞄准辅助分类。 |
| `hand_settings` | 字符串 | 未设置 | 可选。空手时使用的瞄准辅助分类。 |
| `item_settings` | 对象 | 未设置 | 可选。物品标识符到瞄准辅助分类名称的映射；分类名称应存在于指定的分类定义中。 |
| `exclusion_list` | 对象数组 | 未设置 | 可选。需要从瞄准辅助目标中排除的方块或实体标识符列表。 |
| `liquid_targeting_list` | 对象数组 | 未设置 | 可选。手持时允许通过瞄准辅助选中液体方块的物品标识符列表。 |

/// note | 版本差异
本批次Microsoft Learn页面列出`exclusion_list`字段。官方导出的较新架构还可见`exclusion_settings`结构，用于分别列出方块、方块标签、实体和实体族排除项。编写内容时应以目标游戏版本的架构、内容日志和实际测试结果为准。
///
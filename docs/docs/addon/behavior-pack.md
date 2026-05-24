# 行为包

**行为包（Behavior Pack）**是附加包的一种类型，负责定义Minecraft基岩版游戏的逻辑行为和数据规则。行为包属于服务端内容，在服务端加载和执行，控制着游戏世界中实体、方块、物品等对象的行为方式。

## 概述

行为包可以修改或添加实体的行为定义、方块和物品的属性、配方、战利品表、生成规则、世界生成规则、函数、脚本等。通过行为包，开发者可以创建自定义实体、方块、物品，修改世界生成方式，构建复杂的游戏逻辑。

行为包的清单文件中，模块类型应设置为`data`。如果行为包中包含脚本，则需要额外声明一个类型为`script`的模块。一个行为包通常与一个资源包配对使用，并通过清单文件的依赖字段互相关联。

## 目录结构

一个典型的行为包的文件结构如下：

/// html | div.treeview
- {{file|manifest.json}}：清单文件。
- {{file|contents.json}}：内容文件，列出包内所有资源文件的校验信息。
- {{file|pack_icon.png}}：包图标。
- {{file|folder}}**aim_assist/**：瞄准辅助配置。
    - {{file|folder}}**presets/**：瞄准辅助预设定义文件。
- {{file|folder}}**animation_controllers/**：服务端动画控制器。
- {{file|folder}}**animations/**：服务端动画。
- {{file|folder}}**biomes/**：生物群系定义。
- {{file|folder}}**blocks/**：方块定义。
- {{file|folder}}**cameras/**：摄像机预设。
    - {{file|folder}}**presets/**：摄像机预设定义文件。
- {{file|folder}}**dialogue/**：NPC对话定义。
- {{file|folder}}**dimensions/**：维度定义。详见[维度](dimension.md)。
- {{file|folder}}**entities/**：实体行为定义。
- {{file|folder}}**feature_rules/**：地物规则。
- {{file|folder}}**features/**：地物定义。
- {{file|folder}}**functions/**：函数文件。
    - {{file|json}}**tick.json**：每刻自动执行的函数列表。
- {{file|folder}}**item_catalog/**：合成物品目录。
    - {{file|json}}**crafting_item_catalog.json**：合成界面物品目录配置。
- {{file|folder}}**items/**：物品定义。
- {{file|folder}}**loot_tables/**：战利品表。
- {{file|folder}}**recipes/**：配方定义。
- {{file|folder}}**scripts/**：脚本文件。
- {{file|folder}}**shapes/**：自定义碰撞与交互形状定义。
- {{file|folder}}**spawn_rules/**：生成规则。
- {{file|folder}}**structures/**：结构文件。
- {{file|folder}}**texts/**：本地化文件。
- {{file|folder}}**trading/**：交易表。
- {{file|folder}}**worldgen/**：世界生成相关文件。
    - {{file|folder}}**processors/**：结构处理器定义。
    - {{file|folder}}**structure_sets/**：结构集定义。
    - {{file|folder}}**structures/**：拼图结构定义。
    - {{file|folder}}**template_pools/**：拼图模板池定义。
///

## 与资源包的关系

行为包和资源包在功能上互相补充：行为包定义“做什么”，资源包定义“看起来怎样”。以自定义实体为例，实体的AI行为、组件和事件在行为包中定义，而实体的模型、纹理和动画在资源包中定义。两者通过实体的赋命名空间标识符进行关联。

在清单文件中，行为包可以通过`dependencies`字段声明对特定资源包的依赖。当游戏加载行为包时，会自动加载其依赖的资源包。

## 引擎版本

行为包的清单文件中可以指定**最低引擎版本（Min Engine Version）**，即`min_engine_version`字段。该字段决定了游戏引擎以何种版本的解析逻辑来处理行为包中的内容。不同的引擎版本可能对同一接口的解析方式有所不同，因此正确设置最低引擎版本对于保证行为包的兼容性至关重要。详见[版本](../general/version.md#引擎版本)文档。

## 子包

**子包（Sub-Pack）**是一种在单个附加包内提供多套可选内容的机制。子包允许用户在加载附加包时选择不同的配置，例如不同分辨率的纹理、不同难度的游戏规则等。子包在附加包根目录的`subpacks/`文件夹中定义，每个子包是一个独立的子目录，包含要覆盖的文件。
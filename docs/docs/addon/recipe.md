# 配方

**配方（Recipe）**是Minecraft基岩版中定义物品转化规则的数据驱动系统。配方规定输入材料、输出产物、可用合成站以及**配方书（Recipe Book）**解锁条件等信息，用于工作台、熔炉、酿造台、锻造台等合成或加工界面。

## 概述

配方定义文件以JSON格式编写，存放在行为包的`recipes/`目录中。每个配方文件定义一条或多条合成规则，游戏引擎在加载行为包时读取所有配方定义并注册到合成系统中。

配方通过`description.identifier`字段中的赋命名空间标识符唯一标识。每条配方还会声明一个根对象，例如`minecraft:recipe_shaped`或`minecraft:recipe_furnace`。根对象决定该配方使用的输入、输出和合成站字段。

配方文件的`format_version`用于声明该文件遵循的配方格式。较新的配方格式逐步转向扁平化的物品标识符；`data`等用于表示物品或方块旧式附加值的字段在`1.20.0`及之后的格式版本中已不再工作。

## 配方类型

基岩版支持多种配方类型：

### 有序配方

**有序配方（Shaped Recipe）**要求材料在合成网格中按照特定的排列方式放置。合成网格中每个位置对应的材料由模式（`pattern`）和材料映射（`key`）共同定义。

有序配方的根键为`minecraft:recipe_shaped`。`pattern`以字符串数组表示每一行合成格，`key`将每个非空格字符映射到一个物品或物品标签。空格字符保留为合成格中的空位，不可作为材料键使用。

有序配方可以使用`assume_symmetry`控制是否将水平镜像的模式视为同一配方。该字段未设置时默认按对称配方处理；设置为`false`时，可以分别定义互为镜像的模式并给出不同结果。

### 无序配方

**无序配方（Shapeless Recipe）**不要求材料的排列位置，只要求合成网格中包含指定的全部材料即可。

无序配方的根键为`minecraft:recipe_shapeless`。输入材料由`ingredients`数组给出，每个元素可以指定单个物品，也可以指定物品标签。无序配方不使用`pattern`和`key`。

### 烧炼配方

**烧炼配方（Furnace Recipe）**定义了物品在熔炉、高炉或烟熏炉中的烧炼规则。烧炼配方指定输入物品和输出物品。

烧炼配方的根键为`minecraft:recipe_furnace`。

### 酿造配方

**酿造配方（Brewing Recipe）**定义了酿造台中药水的酿造规则。现行官方参考列出的根键为`minecraft:recipe_brewing_mix`，用于描述基础药水、试剂和输出药水类型之间的混合关系。

旧版官方参考和原版行为包中还存在`minecraft:recipe_brewing_container`，用于描述药水容器类型的转化，例如普通药水与喷溅药水之间的转化。该格式属于兼容性内容，不应替代新的酿造混合配方格式。

### 切石配方

**切石配方（Stonecutting Recipe）**定义了切石机中的方块加工规则。

切石配方在基岩版中通常表现为带有`stonecutter`合成标签的有序配方或无序配方，而不是独立的根对象。

### 锻造配方

**锻造配方（Smithing Recipe）**定义了锻造台中物品的升级、转化或装饰规则。锻造配方主要分为两类：

- **锻造转化配方（Smithing Transform Recipe）**使用`minecraft:recipe_smithing_transform`根键，由模板物品、基底物品、附加材料和结果物品组成。该格式要求`format_version`至少为`1.20.0`。
- **锻造盔甲纹饰配方（Smithing Trim Recipe）**使用`minecraft:recipe_smithing_trim`根键，由纹饰模板、可修饰盔甲和纹饰材料组成。模板、基底和材料既可以指定单个物品，也可以指定物品标签。该格式要求`format_version`至少为`1.20.0`。

锻造转化配方用于保留基底物品属性并生成另一件物品；锻造盔甲纹饰配方用于在保留盔甲其他属性的前提下应用纹饰图案和颜色。

## 根对象与主要字段

不同配方类型使用不同的根对象。官方参考中的主要根对象如下：

| 根对象 | 描述 | 主要字段 |
|--------|------|----------|
| `minecraft:recipe_shaped` | 有序合成配方。 | `description`、`tags`、`pattern`、`key`、`result`、`priority`、`assume_symmetry`、`group`、`unlock` |
| `minecraft:recipe_shapeless` | 无序合成配方。 | `description`、`tags`、`ingredients`、`result`、`priority`、`group`、`unlock` |
| `minecraft:recipe_furnace` | 烧炼或烹饪配方。 | `description`、`tags`、`input`、`output` |
| `minecraft:recipe_brewing_mix` | 酿造混合配方。 | `description`、`tags`、`input`、`reagent`、`output` |
| `minecraft:recipe_smithing_transform` | 锻造转化配方。 | `description`、`tags`、`template`、`base`、`addition`、`result` |
| `minecraft:recipe_smithing_trim` | 锻造盔甲纹饰配方。 | `description`、`tags`、`template`、`base`、`addition` |

## 合成标签

配方定义中包含一个`tags`字段，用于指定该配方可以在哪些合成站中使用。常见的合成标签包括`crafting_table`（工作台）、`furnace`（熔炉）、`blast_furnace`（高炉）、`smoker`（烟熏炉）、`stonecutter`（切石机）、`smithing_table`（锻造台）等。

自定义方块也可以通过声明自定义的合成标签来创建自定义合成站。

## 材料标签

**材料标签（Ingredient Tag）**可以作为有序配方或无序配方的输入。使用标签作为输入时，一个材料槽可以匹配一组物品，而不必为每种物品单独编写一条配方。例如，使用`minecraft:planks`可以匹配所有具有该标签的木板，也可以匹配行为包中正确声明为该标签的自定义木板。

官方参考中列举的常见配方输入标签包括`minecraft:planks`、`minecraft:logs`、`minecraft:wool`、`minecraft:is_tool`、`minecraft:is_armor`、`minecraft:coals`、`minecraft:sand`等。该列表会随游戏版本更新而变化，编写配方时应以当前版本导出的物品标签或官方参考为准。

## 解锁配方

配方支持通过`unlock`字段指定解锁条件。在配方书系统中，只有满足解锁条件的配方才会对玩家可见。解锁条件可以基于玩家的背包内容或其他游戏状态。

官方参考中记录的解锁上下文包括`AlwaysUnlocked`、`PlayerInWater`、`PlayerHasManyItems`和`None`等。解锁条件不会改变配方本身的合成逻辑，但会影响配方在配方书中的出现方式。

# 生成规则

**生成规则（Spawn Rule）**是Minecraft基岩版中控制实体在世界中自然生成的数据驱动系统。生成规则定义了实体的生成条件、生成密度和环境约束，决定了哪些实体在何种条件下可以在世界的哪些位置**自然生成（Naturally Spawn）**。

## 概述

自然生成是指游戏自动在世界中创建实体的过程，区别于玩家手动使用刷怪蛋、命令或出生点放置的实体。生成规则定义文件以JSON格式编写，存放在行为包的`spawn_rules/`目录中。

生成规则通过赋命名空间标识符与对应的实体关联。实体的行为定义、客户端表现和生成规则分别位于不同文件中；其中生成规则只描述实体如何参与自然生成，不描述实体生成后的行为。

生成规则还通过`population_control`指定实体所属的人口控制池。常见池包括`animal`、`water_animal`、`monster`和`cat`。其中`cat`池按照村庄内的猫数量进行限制，行为不同于其他普通人口控制池。

## 结构

生成规则的定义文件根键为`minecraft:spawn_rules`，主要包含以下部分：

### 描述

描述（`description`）声明生成规则适用的实体标识符和人口控制池。`identifier`应与对应实体定义的赋命名空间标识符一致；`population_control`决定该实体参与哪一类生成数量控制。

### 生成条件

生成条件（`conditions`）是一组条件集合，每个条件集合定义一种独立的生成方案。一个实体可以有多个条件集合，每个集合代表一种可能的生成场景。

每个条件集合可以包含以下生成条件组件：

- **生物群系过滤器（Biome Filter）**：指定实体可以生成的生物群系类型或生物群系标签。
- **亮度过滤器（Brightness Filter）**：指定实体可生成的亮度范围，并可按天气修正。
- **延迟过滤器（Delay Filter）**：指定生成条件满足后的延迟生成参数。
- **密度上限（Density Limit）**：限制局部区域内实体数量。
- **困难度过滤器（Difficulty Filter）**：指定在哪些困难度设置下允许生成。
- **距离过滤器（Distance Filter）**：按实体与最近玩家的距离限制生成。
- **高度过滤器（Height Filter）**：指定实体可生成的Y坐标范围。
- **群体（Herd）**：指定一次生成的最小和最大实体数量，并可关联生成事件。
- **权重（Weight）**：指定该生成条件相对于其他条件的选择权重。
- **变种生成（Permute Type）**：指定生成时可按权重替换为其他实体类型。
- **世界年龄过滤器（World Age Filter）**：按世界已经存在的刻数限制生成。
- **生物事件过滤器（Mob Event Filter）**：按世界级生物事件是否激活限制生成。
- **村庄玩家过滤器（Player In Village Filter）**：按玩家是否位于村庄范围附近限制生成。
- **生成事件（Spawn Event）**：在实体生成时触发指定实体事件。
- **持久生成标记**：通过`minecraft:is_persistent`使自然生成出的实体不会自然消失。
- **实验性标记**：通过`minecraft:is_experimental`将生成条件绑定到实验开关。<!-- md:flag experimental -->
- **位置约束**：包括`minecraft:spawns_on_surface`、`minecraft:spawns_underground`、`minecraft:spawns_underwater`、`minecraft:spawns_lava`、`minecraft:spawns_on_block_filter`、`minecraft:spawns_on_block_prevented_filter`、`minecraft:disallow_spawns_in_bubble`等。

旧版组件`minecraft:spawns_above_block_filter`曾用于按生成点上方的方块限制生成。官方参考说明该组件用于`1.17.20`及更早版本，并且在至少`1.18.0`格式版本之后不再工作；新内容不应依赖该组件。

## 与实体定义的关系

生成规则与实体的行为定义是独立的文件。实体的行为定义描述实体的行为和属性，而生成规则描述实体在世界中的自然生成条件。两者通过相同的赋命名空间标识符建立关联。

移除实体的生成规则文件可以阻止该实体在世界中自然生成，但不会影响通过命令、刷怪蛋或脚本放置的实体。

## 与生物群系的关系

生成规则通常通过`minecraft:biome_filter`限定实体出现的生物群系。过滤器可以测试生物群系标签，因此生物群系标签是实体自然生成分布的重要连接点。自定义生物群系若要参与实体自然生成，通常需要具有生成规则所测试的标签，或被生成规则直接引用。

## 参考

生成规则的字段、默认值、人口控制池和官方生成条件组件详见[生成规则参考](../../refs/addon/spawn-rule.md)。

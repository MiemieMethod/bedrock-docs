# 地物

**地物（Feature）**是Minecraft基岩版世界生成系统中的基本装饰单元，用于在世界生成过程中向已生成的地形中放置树木、矿石、水池、植物、岩石等各类自然景观元素。

## 概述

世界生成分为两个主要阶段：地形生成和地物放置。在地形生成阶段，游戏根据噪声函数和生物群系信息创建基础地形轮廓。在地物放置阶段，地物系统在基础地形上按照预定义的规则添加各类装饰元素，使世界更加丰富多样。

地物定义文件以JSON格式编写，存放在行为包的`features/`目录中。地物通过**地物规则（Feature Rule）**来控制其在世界中的放置位置和条件。

## 地物类型

基岩版提供了多种内置地物类型。不同类型的地物并不只是外观不同，其放置成功条件、输入位置处理方式和对其他地物的引用方式也不同。

| 类型 | 作用 |
| --- | --- |
| **单方块地物（Single Block Feature）** | 放置一个方块，或按权重从多个方块中选择一个方块放置。 |
| **矿石地物（Ore Feature）** | 放置模拟矿脉的一组方块；虽然名称为矿石，但可以放置任意方块。 |
| **树地物（Tree Feature）** | 生成由树干、树冠、根系和附属装饰构成的树形结构。 |
| **散植地物（Scatter Feature）** | 在区块或输入位置附近多次尝试放置另一个地物。 |
| **聚合地物（Aggregate Feature）** | 在同一输入位置放置多个地物，放置顺序不保证，适用于互不依赖的地物组合。 |
| **序列地物（Sequence Feature）** | 按顺序放置多个地物，前一地物的输出位置作为后一地物的输入位置。 |
| **加权随机地物（Weighted Random Feature）** | 按权重从候选地物中选择一个进行放置。 |
| **搜索地物（Search Feature）** | 在指定体积中沿某一轴搜索有效位置，再放置被引用的地物。 |
| **结构地物（Structure Template Feature）** | 放置行为包`structures/`目录中的`.mcstructure`结构，并可使用约束控制地形、交叉和埋藏情况。 |
| **多面向地物（Multiface Feature）** | 在地面、墙面或天花板上放置方块，并可向周围扩散。 |
| **生长植物地物（Growing Plant Feature）** | 生成从地面或天花板生长的柱状植物。 |
| **晶洞地物（Geode Feature）** | 生成具有多层方块、裂口和潜在放置物的晶洞结构。 |
| **部分暴露团块地物（Partially Exposed Blob Feature）** | 生成大部分嵌入表面、只允许一侧暴露的方块团块。 |
| **植被斑块地物（Vegetation Patch Feature）** | 生成带有地表替换、深度、半径和附属植被的斑块。 |
| **洞穴雕刻地物（Cave Carver Feature）** | 在世界生成预生成阶段雕刻洞穴，包括主世界、下界和水下变体。 |
| **表面吸附地物（Snap To Surface Feature）** | 将另一个地物的放置位置吸附到地面、天花板或水平表面。 |
| **表面相对阈值地物（Surface Relative Threshold Feature）** | 在估算地表以下达到指定距离时放置另一个地物。 |
| **高度差过滤地物（Height Difference Filter Feature）** | 按周围高度差限制地物是否可以放置。 |

地物定义的主要字段可见[地物定义参考](../../refs/addon/feature.md)。

## 地物规则

**地物规则（Feature Rule）**定义了地物在世界中的放置条件和位置。地物规则文件存放在行为包的`feature_rules/`目录中，以JSON格式编写。

地物规则主要包含以下信息：

- **放置阶段（Placement Pass）**：指定地物在世界生成流程中的放置时机。
- **条件（Conditions）**：指定地物放置所需满足的生物群系过滤器或其他条件。
- **分布（Distribution）**：指定地物在区块中的散植方式，包括水平和垂直方向的坐标分布。
- **关联地物（Places Feature）**：指定由该规则放置的地物标识符。

地物规则的主要字段可见[地物规则参考](../../refs/addon/feature-rule.md)。

### 放置阶段

地物的放置按照预定义的阶段顺序执行。较早阶段保证早于较晚阶段执行，同一阶段内不保证顺序。主要的放置阶段包括：

1. `first_pass`：最早执行的放置阶段。
2. `before_underground_pass`：地下放置阶段之前。
3. `underground_pass`：地下放置阶段。
4. `after_underground_pass`：地下放置阶段之后。
5. `before_surface_pass`：地表放置阶段之前。
6. `surface_pass`：地表放置阶段。
7. `after_surface_pass`：地表放置阶段之后。
8. `before_sky_pass`：空中放置阶段之前。
9. `sky_pass`：空中放置阶段。
10. `after_sky_pass`：空中放置阶段之后。
11. `final_pass`：最后执行的放置阶段。
# 维度

**自定义维度（Custom Dimension）**是附加包在原版三大维度之外扩展世界空间的能力入口。维度定义会影响世界空间的标识、垂直边界和生成器类型，并与生物群系、地物、结构、命令和脚本系统共同组成世界生成与运行时逻辑。

## 国际版维度能力边界<!-- md:flag vanilla -->

### 脚本API维度注册

国际版当前更稳定的扩展方向是**脚本API（Script API）**中的自定义维度注册能力。`@minecraft/server`提供的`DimensionRegistry.registerCustomDimension`可在启动阶段注册自定义维度类型，该能力属于实验性或预发布接口，依赖对应版本和实验性开关。

脚本注册维度通常用于创建由脚本控制的目标空间，例如虚空场景、专用玩法区域或脚本驱动的测试空间。维度中的内容生成、传送入口和运行时维护通常仍需由脚本逻辑配套完成。

### 数据驱动维度定义

国际版行为包可在`dimensions/`目录放置维度定义文件。当前知识库可确认的字段集中在以下范围：

- `description.identifier`：维度赋命名空间标识符。
- `components.minecraft:dimension_bounds`：维度垂直边界。
- `components.minecraft:generation.generator_type`：维度生成器类型。

自动导出的官方参考同时记录了`minecraft:dimension`和`minecraft:dimension_type`两种根对象形态，且部分自动生成词条存在命名不一致。因此，数据驱动维度字段应按目标版本实测，不宜将其视为完全稳定的长期接口。字段级细节见[维度定义](../../refs/addon/dimension.md)。

### 与中国版能力的边界

国际版数据驱动维度不包含中国版`netease:biome_source`、`netease:generator_noise`等专有字段。中国版网易数据驱动维度和模组SDK接口属于独立体系，不能写入国际版行为包维度文件。

## 中国版维度体系<!-- md:flag china -->

中国版自定义维度由网易数据驱动格式与模组SDK运行时接口共同构成。网易数据驱动文件位于`netease_dimension/`目录，根对象与字段命名均不同于国际版。相关实践应参见中国版专用教程与参考，不应与国际版维度定义混用。

## 关联概念

- [生物群系](../general/biome.md)
- [地物](feature.md)
- [生成规则](spawn-rule.md)
- [脚本API](script-api.md)
- [维度](../general/dimension.md)

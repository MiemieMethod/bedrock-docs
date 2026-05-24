# 附加包参考

本节包含附加包相关的API架构和数据格式参考文档。

## 清单与配置

清单文件是每个附加包的核心配置文件。以下文档提供了清单文件各部分的详细架构参考：

- [清单文件架构](manifest-schema.md) - 清单根结构及所有顶层属性，含格式版本3预览差异与`capabilities`取值
- [清单标头](manifest-header.md) - 包身份信息，包括名称、UUID、作用域与版本字段类型
- [清单元数据](manifest-metadata.md) - 可选的包元数据，包括作者和许可证
- [清单模块](manifest-module.md) - 模块声明，定义包的类型和功能
- [清单依赖](manifest-dependency.md) - 依赖声明，包括包依赖和脚本模块依赖
- [包依赖](manifest-pack-dependency.md) - 引用其他附加包的方式
- [原生模块依赖](manifest-native-module-dependency.md) - 声明对脚本API模块的依赖
- [子包配置](manifest-subpack.md) - 子包定义，用于提供不同质量的资源
- [版本格式](semversion.md) - 语义版本号格式
- [皮肤包架构](skin-pack.md) - `skins.json`结构、本地化键命名和皮肤包校验要点
- [世界设置](world-setting.md) - 玩家在世界设置中可配置的选项入口
- [切换设置](world-setting-toggle.md) - 世界设置中的布尔切换项
- [滑块设置](world-setting-slider.md) - 世界设置中的数值滑块项
- [下拉菜单设置](world-setting-dropdown.md) - 世界设置中的下拉菜单项
- [下拉菜单选项](world-setting-dropdown-option.md) - 下拉菜单项中的选项结构
- [标签设置](world-setting-label.md) - 世界设置中的只读标签项

## 实体定义

关于实体的定义和控制相关的参考：

- [实体定义](entity.md)
- [运行时标识符](runtime-identifier.md) - 汇总`runtime_identifier`字段用途、常见标识符效果与风险分级
- [客户端实体定义](client-entity.md) - 列出渲染资源短名称映射、脚本字段、离屏更新字段与刷怪蛋显示字段
- [附着物定义](attachable.md) - 列出`minecraft:attachable`的`description`、脚本、刷怪蛋与资源短名称映射字段
- [动画定义](animation.md) - 列出动画对象、骨骼关键帧、时间轴特效与插值模式
- [动画控制器](animation-controller.md)
- [渲染控制器](render-controller.md) - 列出资源数组、材质映射、覆盖色、UV动画与部件可见性字段
- [粒子定义](particle.md)
- [实体组件](entity-component.md)
- [实体AI意向](entity-ai-goal.md)
- [实体过滤器](entity-filter.md)
- [实体事件与触发器](entity-event.md)
- [生成规则](spawn-rule.md)

## Molang

以下文档汇总Molang函数的官方参考说明，便于在动画、动画控制器、渲染控制器和粒子定义中快速查阅：

- [Molang数学函数](molang-math-function.md) - 汇总`math.`前缀函数及官方说明
- [Molang查询函数](molang-query-function.md) - 汇总`query.`前缀函数及内部或已弃用函数说明

## 其他内容

- [维度定义](dimension.md)
- [生物群系定义](biome.md)
- [客户端生物群系定义](client-biome.md)
- [地物定义](feature.md)
- [地物规则](feature-rule.md)
- [拼图结构](jigsaw-structure.md)
- [模板池](jigsaw-template-pool.md)
- [处理器列表](jigsaw-processor-list.md)
- [结构集](jigsaw-structure-set.md)
- [方块定义](block.md) - 列出行为包方块结构、资源包`blocks.json`、方块引用对象与剔除规则
- [方块组件](block-component.md)
- [方块状态与置换](block-state.md)
- [方块萃取](block-trait.md)
- [体素形状文档](voxel-shape.md)
- [物品定义](item.md)
- [物品组件](item-component.md)
- [JSON UI文件](json-ui.md) - 列出文件结构、常见控件字段、变量、绑定、按钮映射与`modifications`修改操作
- [相机定义](camera.md) - 相机瞄准辅助分类、优先级和预设结构
- [几何体定义](geometry.md) - `minecraft:geometry`的版本差异、骨骼、立方体、逐面UV、定位器约定与物品显示变换
- [纹理集](texture-set.md) - `*.texture_set.json`层字段、约束和资源栈行为
- [光照设置](lighting-settings.md) - `minecraft:lighting_settings`中的环境光、定向光、天空和自发光参数
- [大气散射设置](atmosphere-settings.md) - `minecraft:atmosphere_settings`中的瑞利散射、米氏散射和地平线混合参数
- [色彩分级设置](color-grading-settings.md) - `minecraft:color_grading_settings`中的阴影、中间调、高光和色调映射参数
- [PBR回退设置](pbr-fallback-settings.md) - `minecraft:pbr_fallback_settings`中的方块、物品、活动对象和粒子统一PBR后备值
- [点光设置](point-light-settings.md) - `minecraft:point_light_settings`中的点光颜色参数
- [阴影风格设置](shadow-settings.md) - `minecraft:shadow_settings`中的阴影风格和纹素尺寸参数
- [水体设置](water-settings.md) - `minecraft:water_settings`中的焦散、粒子浓度和水波参数
- [迷雾定义](fog-settings.md)
- [战利品表](loot-table.md) - 汇总池、分层抽取、条件、函数参数与掉落场景兼容性
- [物品函数](item-function.md) - 汇总战利品表与交易表共享的物品函数及其适用边界
- [交易表](trade-table.md) - 汇总层级解锁、交易组抽样、交易物品字段与函数兼容性边界
- [配方](recipe.md) - 汇总所有配方类型的字段架构，含有序、无序、烧炼、酿造、锻造配方
- [对话定义](dialogue-document.md)

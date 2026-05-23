# 附加包参考

本节包含附加包相关的API架构和数据格式参考文档。

## 清单与配置

清单文件是每个附加包的核心配置文件。以下文档提供了清单文件各部分的详细架构参考：

- [清单文件架构](manifest-schema.md) - 清单根结构及所有顶层属性
- [清单标头](manifest-header.md) - 包身份信息，包括名称、UUID和版本
- [清单元数据](manifest-metadata.md) - 可选的包元数据，包括作者和许可证
- [清单模块](manifest-module.md) - 模块声明，定义包的类型和功能
- [清单依赖](manifest-dependency.md) - 依赖声明，包括包依赖和脚本模块依赖
- [包依赖](manifest-pack-dependency.md) - 引用其他附加包的方式
- [原生模块依赖](manifest-native-module-dependency.md) - 声明对脚本API模块的依赖
- [子包配置](manifest-subpack.md) - 子包定义，用于提供不同质量的资源
- [版本格式](semversion.md) - 语义版本号格式
- [世界设置](world-setting.md) - 玩家在世界设置中可配置的选项
- [切换设置](world-setting-toggle.md) - 世界设置中的布尔切换项
- [滑块设置](world-setting-slider.md) - 世界设置中的数值滑块项
- [下拉菜单设置](world-setting-dropdown.md) - 世界设置中的下拉菜单项
- [下拉菜单选项](world-setting-dropdown-option.md) - 下拉菜单项中的选项结构
- [标签设置](world-setting-label.md) - 世界设置中的只读标签项

## 实体定义

关于实体的定义和控制相关的参考：

- [实体定义](entity.md)
- [客户端实体定义](client-entity.md)
- [动画定义](animation.md)
- [动画控制器](animation-controller.md)
- [渲染控制器](render-controller.md)
- [粒子定义](particle.md)
- [实体组件](entity-component.md)
- [实体AI意向](entity-ai-goal.md)
- [实体过滤器](entity-filter.md)
- [实体事件与触发器](entity-event.md)
- [生成规则](spawn-rule.md)

## 其他内容

- [维度定义](dimension.md)
- [生物群系定义](biome.md)
- [地物定义](feature.md)
- [地物规则](feature-rule.md)
- [方块定义](block.md)
- [方块组件](block-component.md)
- [方块状态与置换](block-state.md)
- [方块萃取](block-trait.md)
- [物品定义](item.md)
- [物品组件](item-component.md)
- [JSON UI文件](json-ui.md)
- [相机定义](camera.md) - 相机瞄准辅助分类、优先级和预设结构
- [迷雾定义](fog-settings.md)
- [战利品表](loot-table.md)
- [交易表](trade-table.md)
- [对话定义](dialogue-document.md)

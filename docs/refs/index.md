# 参考

这里是Minecraft基岩版的各类API和开发资源的参考文档。这些文档包含了Minecraft基岩版的各类API接口、命令、网络协议、原版对象信息等内容，以及一些开发资源的使用方法和示例。

## 服务器

- [BDS的server.properties](server/bds-server-properties.md)：列出基岩版专用服务器主要配置项、默认值和取值范围。
- [LeviLamina API模块](server/levilamina-api.md)：概述LeviLamina官方API参考中的模块、适用范围和兼容性提示。
- [Endstone命令与文本格式](server/endstone-command-format.md)：列出Endstone插件命令参数、权限默认值和颜色格式代码。
- [Allay API概览](server/allay-api.md)：概述Allay插件描述文件、命令、事件、调度器、方块、物品、容器、表单和高级自定义内容接口。

## 附加包

- [实体定义](addon/entity.md)：列出行为包实体定义文件的主要结构、描述字段、组件、组件组和事件关系。
- [客户端实体定义](addon/client-entity.md)：列出资源包客户端实体定义的渲染资源绑定、脚本字段和刷怪蛋字段。
- [动画定义](addon/animation.md)：列出资源包和行为包动画定义文件的根字段、动画对象、骨骼变换和挂接位置。
- [动画控制器](addon/animation-controller.md)：列出动画控制器文件的根字段、状态机结构、状态转移和融合字段。
- [渲染控制器](addon/render-controller.md)：列出资源包渲染控制器的资源数组、几何体、材质、纹理和部件可见性字段。
- [粒子定义](addon/particle.md)：列出资源包粒子定义文件的渲染参数、发射器组件、粒子组件、曲线、事件和实体挂接字段。
- [实体组件](addon/entity-component.md)：列出国际版官方实体参考收录的实体组件标识符及用途分类。
- [实体AI意向](addon/entity-ai-goal.md)：列出国际版官方实体参考收录的`minecraft:behavior.*`AI意向组件及用途分类。
- [实体过滤器](addon/entity-filter.md)：列出实体过滤器的基本字段、逻辑组合和官方测试名。
- [实体事件与触发器](addon/entity-event.md)：列出内置实体事件、触发器组件和实体事件响应动作。
- [生成规则](addon/spawn-rule.md)：列出行为包生成规则文件结构、人口控制池、生成条件组件、字段默认值和已弃用项。
- [生物群系定义](addon/biome.md)：列出行为包生物群系定义文件的主要字段、服务端生成组件、替换规则、地表构建器和标签含义。
- [地物定义](addon/feature.md)：列出行为包地物定义文件的主要结构、地物类型、内部类型和散植参数。
- [地物规则](addon/feature-rule.md)：列出行为包地物规则文件的主要字段、放置阶段、生物群系过滤器和散植参数。
- [方块定义](addon/block.md)：列出行为包方块定义文件、资源包`blocks.json`、方块剔除规则和方块物品表现相关字段。
- [方块组件](addon/block-component.md)：列出行为包方块定义可用组件、关键字段、版本要求和内部或已弃用项。
- [方块状态与置换](addon/block-state.md)：列出自定义方块状态、方块置换条件、置换数量限制和原版状态附表入口。
- [方块萃取](addon/block-trait.md)：列出行为包方块定义可用方块萃取、可启用状态和附加字段。
- [物品定义](addon/item.md)：列出行为包物品定义文件的主要结构、常用组件、使用优先级和原版物品标签。
- [物品组件](addon/item-component.md)：列出行为包物品定义可用组件、主要字段、依赖关系和已弃用项。
- [JSON UI文件](addon/json-ui.md)：列出国际版资源包JSON UI的`_ui_defs.json`、`_global_variables.json`、屏幕文件、控件字段、绑定和按钮映射。
- [相机定义](addon/camera.md)：列出国际版相机瞄准辅助分类和瞄准辅助预设的JSON根对象与主要字段。
- [迷雾定义](addon/fog-settings.md)：列出资源包迷雾定义文件的主要字段、距离迷雾类别和体积迷雾类别。
- [战利品表](addon/loot-table.md)：列出行为包战利品表文件的主要字段、池、条目、条件和函数。
- [交易表](addon/trade-table.md)：列出行为包交易表文件的主要字段、层级结构、交易组、交易项目和交易物品。

## 中国版模组SDK

- [世界控制接口](modsdk/world-control.md)：列出中国版模组SDK中与时间、天气、游戏规则、消息和指令相关的运行时接口。

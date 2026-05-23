# 客户端实体定义

**客户端实体（Client Entity）**定义资源包中实体的渲染资源绑定。它不决定实体的服务端逻辑，而是将实体标识符关联到材质、纹理、几何体、动画、动画控制器、渲染控制器、粒子、定位器和刷怪蛋显示方式。

## 文件结构

| 字段 | 类型 | 说明 |
|---|---|---|
| `format_version` | 字符串 | 声明客户端实体定义文件使用的数据格式版本。 |
| `minecraft:client_entity` | 对象 | 客户端实体定义根对象。 |
| `description.identifier` | 字符串 | 与行为包实体定义一致的赋命名空间标识符。 |
| `description.min_engine_version` | 字符串 | 可选。限制此定义可被解析的最低引擎版本。 |
| `description.materials` | 对象 | 将短名称映射到材质标识符。 |
| `description.textures` | 对象 | 将短名称映射到纹理路径。 |
| `description.geometry` | 对象 | 将短名称映射到几何体标识符。 |
| `description.animations` | 对象 | 将短名称映射到动画标识符。 |
| `description.animation_controllers` | 数组 | 声明实体使用的动画控制器。 |
| `description.render_controllers` | 数组 | 声明实体使用的渲染控制器。 |
| `description.particle_effects` | 对象 | 将粒子短名称映射到粒子特效标识符，供动画和动画控制器引用。 |
| `description.locators` | 对象 | 为绳索、粒子、特效等资源提供模型空间定位器。 |
| `description.spawn_egg` | 对象 | 声明刷怪蛋颜色或刷怪蛋纹理。 |

## 粒子与定位器

`description.particle_effects`用于声明实体内部可引用的粒子特效短名称。动画和动画控制器中的`particle_effects`字段使用这些短名称，而不是直接使用粒子特效全局标识符。粒子短名称映射本身不会播放粒子；实际播放由动画时间轴、动画控制器状态、命令或脚本触发。

`description.locators`可将粒子挂接到几何体定位器，使发射器跟随实体骨骼或定位点移动。

## 脚本字段

`scripts.pre_animation`可在动画求值前执行Molang表达式，用于写入变量并供动画和渲染控制器复用。`scripts.scale`可控制实体几何体缩放。客户端实体脚本只影响渲染侧表现，不应被视为服务端行为逻辑。

## 官方主题覆盖

| 主题 | 站内判定 |
|---|---|
| `ClientEntityDocumentationIntroduction` | 客户端实体定义结构、标识符、材质、纹理、几何体、动画、渲染控制器、定位器和刷怪蛋。 |
| `ClientEntityFilters` | 客户端实体资源选择可使用的过滤器结构与逻辑组合。 |
| `DataDrivenSpawning` | 数据驱动生成规则的概念、人口控制池和生成条件组件。 |
| `IDLists` | 实体JSON条目的内部ID列表；通常不直接用于附加包编写。 |

<!-- md:sortable -->

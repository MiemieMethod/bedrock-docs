# 粒子定义

本页列出国际版资源包`particles/`目录中粒子特效定义文件的主要结构。粒子定义使用JSON格式描述一个粒子特效的渲染参数、发射器、粒子运动、粒子外观、曲线、事件和实体挂接行为。本页不包含中国版网易ModSDK粒子接口。

## 文件位置与单位

| 项目 | 说明 |
| --- | --- |
| 文件夹 | 资源包`particles/`目录。文件可位于该目录的任意子目录中，引用时使用粒子标识符而不是文件路径。 |
| 标识符 | `particle_effect.description.identifier`声明的赋命名空间标识符，例如`demo:colored_smoke`。`minecraft`命名空间保留给原版内容。 |
| 距离单位 | 米，等同于方块长度。 |
| 时间单位 | 秒。速度为米每秒，加速度为米每二次方秒。 |
| 角度单位 | 度。粒子Molang中的三角函数也使用度。 |

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 粒子定义文件使用的格式版本。官方示例常使用`1.10.0`。 |
| `particle_effect` | 对象 | 未设置 | 粒子特效定义对象。 |

## `particle_effect`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 粒子特效的标识符和基础渲染参数。必须包含`identifier`和`basic_render_parameters`。 |
| `components` | 对象 | 未设置 | 粒子组件集合。组件控制发射器行为、粒子寿命、运动、碰撞、外观和事件触发。 |
| `curves` | 对象 | 未设置 | 粒子曲线集合。曲线按每个可见粒子的渲染帧求值，并写入同名Molang变量。 |
| `events` | 对象 | 未设置 | 粒子事件集合。事件可播放音效、生成其他粒子特效、执行Molang表达式或按顺序、权重组合其他事件节点。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 粒子特效的赋命名空间标识符。 |
| `basic_render_parameters` | 对象 | 未设置 | 基础渲染参数。必须包含`material`和`texture`。 |

### `basic_render_parameters`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `material` | 字符串 | 未设置 | 粒子使用的材质。该字段决定透明像素、颜色混合和发光类效果的渲染方式。 |
| `texture` | 字符串 | 未设置 | 粒子纹理路径。通常指向资源包中的纹理资源，例如`textures/particle/particles`。 |

| 材质 | 描述 |
| --- | --- |
| `particles_alpha` | Alpha为`0`的像素完全透明，其余有色像素保持不透明。此模式不支持透明度渐变，适合剪影类粒子如树叶、纸片。 |
| `particles_blend` | 启用普通（Alpha）混合模式下的颜色混合和透明度，支持半透明渐变。适合烟雾、水花、血液等需要模糊边界的粒子。 |
| `particles_add` | 启用加法混合模式下的颜色混合和透明度。新像素颜色与后台叠加而不是覆盖，常用于需要发光感的粒子如魔法、闪电、发光尘埃。 |

## 组件概览

粒子系统中的组件分为**粒子发射器**相关组件和单个粒子相关组件。发射器组件决定粒子何时、从哪里、以何种初始方向生成；粒子组件决定已生成粒子的寿命、速度、位置、碰撞、颜色和渲染方式。

| 分类 | 组件 | 用途 |
| --- | --- | --- |
| 发射器初始化 | `minecraft:emitter_initialization` | 在发射器创建时或每次发射器更新时执行Molang表达式。 |
| 发射器本地空间 | `minecraft:emitter_local_space` | 控制实体挂接发射器是否在实体空间中模拟位置、旋转和速度。 |
| 发射率 | `minecraft:emitter_rate_instant` | 发射器激活时一次性生成粒子。 |
| 发射率 | `minecraft:emitter_rate_steady` | 按每秒生成速率持续生成粒子，并限制最大存活粒子数。 |
| 发射率 | `minecraft:emitter_rate_manual` | 仅在被事件或游戏逻辑手动要求时生成粒子，多用于旧版或事件驱动效果。 |
| 发射器寿命 | `minecraft:emitter_lifetime_looping` | 发射器在激活时段和休眠时段之间循环。 |
| 发射器寿命 | `minecraft:emitter_lifetime_once` | 发射器执行一次，在激活时段结束或可生成粒子耗尽后过期。 |
| 发射器寿命 | `minecraft:emitter_lifetime_expression` | 用Molang表达式控制发射器启用和过期。 |
| 发射器寿命 | `minecraft:emitter_lifetime_events` | 在发射器创建、过期、时间线或移动距离达到条件时触发事件。 |
| 发射器形状 | `minecraft:emitter_shape_point` | 从一个点生成粒子。 |
| 发射器形状 | `minecraft:emitter_shape_sphere` | 从球体内部或球面生成粒子。 |
| 发射器形状 | `minecraft:emitter_shape_box` | 从盒体内部或表面生成粒子。 |
| 发射器形状 | `minecraft:emitter_shape_custom` | 用Molang表达式自定义生成位置和方向。 |
| 发射器形状 | `minecraft:emitter_shape_entity_aabb` | 从挂接实体的轴对齐包围盒内部或表面生成粒子。 |
| 发射器形状 | `minecraft:emitter_shape_disc` | 从圆盘内部或边缘生成粒子。 |
| 粒子初始状态 | `minecraft:particle_initial_speed` | 设置粒子初始速度，可为标量或三维向量。 |
| 粒子初始状态 | `minecraft:particle_initial_spin` | 设置粒子初始旋转和旋转速度。 |
| 粒子初始化 | `minecraft:particle_initialization` | 在粒子生成或渲染更新时执行Molang表达式。 |
| 粒子寿命 | `minecraft:particle_lifetime_expression` | 设置粒子最大寿命或提前过期表达式。 |
| 粒子寿命 | `minecraft:particle_lifetime_events` | 在粒子创建、过期或时间线达到条件时触发事件。 |
| 粒子寿命 | `minecraft:particle_expire_if_in_blocks` | 粒子位于指定方块内时过期。 |
| 粒子寿命 | `minecraft:particle_expire_if_not_in_blocks` | 粒子不位于指定方块内时过期。 |
| 粒子寿命 | `minecraft:particle_kill_plane` | 粒子跨越指定平面时过期。 |
| 粒子运动 | `minecraft:particle_motion_dynamic` | 使用速度、加速度和阻力模拟粒子运动。 |
| 粒子运动 | `minecraft:particle_motion_parametric` | 用Molang表达式直接控制粒子相对位置、方向和旋转。 |
| 粒子运动 | `minecraft:particle_motion_collision` | 启用与地形的碰撞、反弹、接触过期和碰撞事件。 |
| 粒子外观 | `minecraft:particle_appearance_billboard` | 将粒子渲染为朝向摄像机、方向或发射器变换的公告板面片。 |
| 粒子外观 | `minecraft:particle_appearance_tinting` | 设置粒子颜色、十六进制颜色或颜色梯度。 |
| 粒子外观 | `minecraft:particle_appearance_lighting` | 使粒子受本地光照条件着色。 |

## 发射器组件

### 初始化与本地空间

| 组件 | 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `minecraft:emitter_initialization` | `creation_expression` | Molang表达式 | `0` | 发射器创建时执行一次，常用于初始化`variable.`变量。 |
| `minecraft:emitter_initialization` | `per_update_expression` | Molang表达式 | `0` | 发射器每次更新时执行。 |
| `minecraft:emitter_local_space` | `position` | 布尔值 | `false` | 为`true`时，粒子位置在实体本地空间中模拟。 |
| `minecraft:emitter_local_space` | `rotation` | 布尔值 | `false` | 为`true`时，粒子旋转在实体本地空间中模拟。`rotation`为`true`且`position`为`false`是无效组合。 |
| `minecraft:emitter_local_space` | `velocity` | 布尔值 | `false` | 为`true`时，将发射器速度加入粒子初始速度。 |

### 发射率

| 组件 | 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `minecraft:emitter_rate_instant` | `num_particles` | 数值或Molang表达式 | `10` | 每次发射器循环开始时一次性生成的粒子数量。 |
| `minecraft:emitter_rate_steady` | `spawn_rate` | 数值或Molang表达式 | `1` | 每秒生成的粒子数量。 |
| `minecraft:emitter_rate_steady` | `max_particles` | 数值或Molang表达式 | `50` | 此发射器同时存在的最大粒子数。 |
| `minecraft:emitter_rate_manual` | `max_particles` | 数值或Molang表达式 | `50` | 手动发射粒子时允许同时存在的最大粒子数。 |

### 发射器寿命

| 组件 | 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `minecraft:emitter_lifetime_looping` | `active_time` | 数值或Molang表达式 | `10` | 每个循环中发射器保持激活的秒数。 |
| `minecraft:emitter_lifetime_looping` | `sleep_time` | 数值或Molang表达式 | `0` | 每个循环中发射器暂停发射的秒数。 |
| `minecraft:emitter_lifetime_once` | `active_time` | 数值或Molang表达式 | `10` | 发射器单次执行时持续发射的秒数。 |
| `minecraft:emitter_lifetime_expression` | `activation_expression` | 数值或Molang表达式 | `1` | 表达式非`0`时发射器处于激活状态。 |
| `minecraft:emitter_lifetime_expression` | `expiration_expression` | 数值或Molang表达式 | `0` | 表达式非`0`时发射器过期。 |
| `minecraft:emitter_lifetime_events` | `creation_event` | 字符串或字符串数组 | 未设置 | 发射器创建时触发的事件名称。 |
| `minecraft:emitter_lifetime_events` | `expiration_event` | 字符串或字符串数组 | 未设置 | 发射器过期时触发的事件名称。该事件不等待已生成粒子全部过期。 |
| `minecraft:emitter_lifetime_events` | `timeline` | 对象 | 未设置 | 按当前循环内的时间点触发事件。键为时间，值为事件名称或事件名称数组。 |
| `minecraft:emitter_lifetime_events` | `travel_distance_events` | 对象 | 未设置 | 发射器移动到指定累计距离时触发事件。 |
| `minecraft:emitter_lifetime_events` | `looping_travel_distance_events` | 数组 | 未设置 | 每移动指定间隔距离后循环触发事件。数组项通常包含`distance`和`effects`。 |

### 发射器形状

| 组件 | 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `minecraft:emitter_shape_point` | `offset` | 三元素数值或Molang数组 | `[0,0,0]` | 粒子生成点相对发射器的位置。 |
| `minecraft:emitter_shape_point` | `direction` | 三元素数值或Molang数组 | 未设置 | 粒子初始方向。 |
| `minecraft:emitter_shape_sphere` | `offset` | 三元素数值或Molang数组 | `[0,0,0]` | 球体中心相对发射器的位置。 |
| `minecraft:emitter_shape_sphere` | `radius` | 数值或Molang表达式 | `1` | 球体半径。 |
| `minecraft:emitter_shape_sphere` | `surface_only` | 布尔值 | `false` | 为`true`时仅从球面生成粒子。 |
| `minecraft:emitter_shape_sphere` | `direction` | 字符串或三元素数组 | `outwards` | 可为`inwards`、`outwards`或自定义方向数组。 |
| `minecraft:emitter_shape_box` | `offset` | 三元素数值或Molang数组 | `[0,0,0]` | 盒体中心相对发射器的位置。 |
| `minecraft:emitter_shape_box` | `half_dimensions` | 三元素数值或Molang数组 | 未设置 | 盒体在x、y、z轴上的半尺寸。 |
| `minecraft:emitter_shape_box` | `surface_only` | 布尔值 | `false` | 为`true`时仅从盒体表面生成粒子。 |
| `minecraft:emitter_shape_box` | `direction` | 字符串或三元素数组 | `outwards` | 可为`inwards`、`outwards`或自定义方向数组。 |
| `minecraft:emitter_shape_custom` | `offset` | 三元素数值或Molang数组 | `[0,0,0]` | 通过表达式计算的粒子生成位置。 |
| `minecraft:emitter_shape_custom` | `direction` | 三元素数值或Molang数组 | `[0,0,0]` | 通过表达式计算的粒子方向。 |
| `minecraft:emitter_shape_entity_aabb` | `surface_only` | 布尔值 | `false` | 为`true`时仅从挂接实体的轴对齐包围盒表面生成粒子。 |
| `minecraft:emitter_shape_entity_aabb` | `direction` | 字符串或三元素数组 | `outwards` | 可为`inwards`、`outwards`或自定义方向数组。 |
| `minecraft:emitter_shape_disc` | `plane_normal` | 字符串或三元素数组 | `[0,1,0]` | 圆盘法线。字符串可为`x`、`y`或`z`。 |
| `minecraft:emitter_shape_disc` | `offset` | 三元素数值或Molang数组 | `[0,0,0]` | 圆盘中心相对发射器的位置。 |
| `minecraft:emitter_shape_disc` | `radius` | 数值或Molang表达式 | `1` | 圆盘半径。 |
| `minecraft:emitter_shape_disc` | `surface_only` | 布尔值 | `false` | 为`true`时仅从圆盘边缘生成粒子。 |
| `minecraft:emitter_shape_disc` | `direction` | 字符串或三元素数组 | `outwards` | 可为`inwards`、`outwards`或自定义方向数组。 |

## 粒子组件

### 初始状态与寿命

| 组件 | 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `minecraft:particle_initial_speed` | 组件值 | 数值、Molang表达式或三元素数组 | `0` | 粒子的初始速度。标量速度沿发射器形状给出的方向应用，数组可直接指定各轴速度。 |
| `minecraft:particle_initial_spin` | `rotation` | 数值或Molang表达式 | `0` | 粒子初始旋转角度，单位为度。 |
| `minecraft:particle_initial_spin` | `rotation_rate` | 数值或Molang表达式 | `0` | 粒子旋转速度，单位为度每秒。 |
| `minecraft:particle_initialization` | `per_render_expression` | Molang表达式 | `0` | 粒子渲染相关更新时执行的表达式。 |
| `minecraft:particle_initialization` | `per_update_expression` | Molang表达式 | `0` | 粒子每次更新时执行的表达式。 |
| `minecraft:particle_lifetime_expression` | `max_lifetime` | 数值或Molang表达式 | 未设置 | 粒子的最大存活时间。 |
| `minecraft:particle_lifetime_expression` | `expiration_expression` | 数值或Molang表达式 | `0` | 表达式非`0`时粒子提前过期。 |
| `minecraft:particle_lifetime_events` | `creation_event` | 字符串或字符串数组 | 未设置 | 粒子创建时触发的事件名称。 |
| `minecraft:particle_lifetime_events` | `expiration_event` | 字符串或字符串数组 | 未设置 | 粒子过期时触发的事件名称。 |
| `minecraft:particle_lifetime_events` | `timeline` | 对象 | 未设置 | 按粒子年龄时间点触发事件。 |
| `minecraft:particle_expire_if_in_blocks` | 组件值 | 字符串数组 | 未设置 | 粒子位于任一指定方块内时过期。方块名通常与`/setblock`可用名称一致并带有`minecraft:`命名空间。 |
| `minecraft:particle_expire_if_not_in_blocks` | 组件值 | 字符串数组 | 未设置 | 粒子不位于任一指定方块内时过期。 |
| `minecraft:particle_kill_plane` | 组件值 | 四元素数值数组 | 未设置 | 粒子跨越平面`A*x+B*y+C*z+D=0`时过期，数组为`[A,B,C,D]`。 |

### 运动与碰撞

| 组件 | 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `minecraft:particle_motion_dynamic` | `linear_acceleration` | 三元素数值或Molang数组 | `[0,0,0]` | 线性加速度，单位为米每二次方秒。例如重力可写为`[0,-9.8,0]`。 |
| `minecraft:particle_motion_dynamic` | `linear_drag_coefficient` | 数值或Molang表达式 | `0` | 线性阻力系数。加速度按`-linear_drag_coefficient*velocity`影响当前速度。 |
| `minecraft:particle_motion_dynamic` | `rotation_acceleration` | 数值或Molang表达式 | `0` | 旋转加速度。 |
| `minecraft:particle_motion_dynamic` | `rotation_drag_coefficient` | 数值或Molang表达式 | `0` | 旋转阻力系数。 |
| `minecraft:particle_motion_parametric` | `relative_position` | 三元素数值或Molang数组 | `[0,0,0]` | 每帧直接设置粒子相对发射器的位置。 |
| `minecraft:particle_motion_parametric` | `direction` | 三元素数值或Molang数组 | 未设置 | 每帧直接设置粒子的方向。 |
| `minecraft:particle_motion_parametric` | `rotation` | 数值或Molang表达式 | `0` | 每帧直接设置粒子的旋转。 |
| `minecraft:particle_motion_collision` | `enabled` | 布尔值或Molang表达式 | `true` | 是否启用碰撞。没有该组件时粒子不进行碰撞。 |
| `minecraft:particle_motion_collision` | `collision_drag` | 数值 | `0` | 粒子接触地形后按每秒速度衰减的阻力。 |
| `minecraft:particle_motion_collision` | `coefficient_of_restitution` | 数值 | `0` | 反弹系数。`0`表示不反弹，`1`表示保留原高度，超过`1`会在反弹中获得能量。 |
| `minecraft:particle_motion_collision` | `collision_radius` | 数值 | 未设置 | 用于减少粒子与环境互相穿透的碰撞半径，官方说明该值必须不大于半个方块。 |
| `minecraft:particle_motion_collision` | `expire_on_contact` | 布尔值 | `false` | 为`true`时，粒子接触地形后过期。 |
| `minecraft:particle_motion_collision` | `events` | 对象或数组 | 未设置 | 碰撞达到条件时触发事件。事件项包含`event`和可选`min_speed`，`min_speed`默认值为`2`。 |

`minecraft:particle_motion_parametric`不适用于手动发射的粒子，也不适用于未在本地空间中模拟的实体挂接粒子发射器。

### 外观

| 组件 | 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| `minecraft:particle_appearance_billboard` | `size` | 二元素数值或Molang数组 | 未设置 | 公告板面片宽度和高度。 |
| `minecraft:particle_appearance_billboard` | `facing_camera_mode` | 字符串 | 未设置 | 公告板朝向模式。可用值见下表。 |
| `minecraft:particle_appearance_billboard` | `direction` | 对象 | 未设置 | 面向模式需要方向时使用的方向设置。 |
| `minecraft:particle_appearance_billboard` | `uv` | 对象 | 未设置 | 纹理区域或翻书动画数据。 |
| `minecraft:particle_appearance_tinting` | `color` | 颜色、数组或对象 | 未设置 | 粒子颜色。可为十六进制字符串、RGB/RGBA数组，或含`gradient`和`interpolant`的梯度对象。 |
| `minecraft:particle_appearance_lighting` | 组件值 | 空对象 | 未设置 | 存在该组件时，粒子会受游戏中的本地光照条件着色。 |

| `facing_camera_mode`值 | 描述 |
| --- | --- |
| `rotate_xyz` | 面片与摄像机对齐，并垂直于视轴。 |
| `rotate_y` | 面片与摄像机对齐，但只绕世界y轴旋转。 |
| `lookat_xyz` | 面片朝向摄像机，并偏向世界y轴向上。 |
| `lookat_y` | 面片朝向摄像机，但只绕世界y轴旋转。 |
| `lookat_direction` | 面片按方向设置朝向。 |
| `direction_x` | 未旋转粒子的x轴沿方向向量，y轴尝试向上。 |
| `direction_y` | 未旋转粒子的y轴沿方向向量，x轴尝试向上。 |
| `direction_z` | 公告板正面沿方向向量，y轴尝试向上。 |
| `emitter_transform_xy` | 粒子面片匹配发射器变换的xy平面。 |
| `emitter_transform_xz` | 粒子面片匹配发射器变换的xz平面。 |
| `emitter_transform_yz` | 粒子面片匹配发射器变换的yz平面。 |

#### `direction`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `mode` | 字符串 | `derive_from_velocity` | 方向来源。可使用`derive_from_velocity`从粒子速度派生方向，或使用`custom_direction`从`custom_direction`字段读取方向。 |
| `min_speed_threshold` | 数值 | `0.01` | `derive_from_velocity`模式下用于设置方向的最小速度阈值。 |
| `custom_direction` | 三元素数值或Molang数组 | 未设置 | `custom_direction`模式下使用的自定义方向向量。 |

#### `uv`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `texture_width` | 整数 | `1` | 用于解释UV坐标的纹理宽度。为`1`时按归一化UV解释；设为真实宽度时可按纹素解释。 |
| `texture_height` | 整数 | `1` | 用于解释UV坐标的纹理高度。 |
| `uv` | 二元素数值或Molang数组 | 未设置 | 使用的纹理区域左上角坐标。 |
| `uv_size` | 二元素数值或Molang数组 | 未设置 | 使用的纹理区域尺寸。 |
| `flipbook` | 对象 | 未设置 | 翻书动画数据。 |

#### `flipbook`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `base_UV` | 二元素数值或Molang数组 | 未设置 | 起始帧纹理区域左上角坐标。 |
| `size_UV` | 二元素数值数组 | `[1,1]` | 每帧纹理区域尺寸。 |
| `step_UV` | 二元素数值数组 | `[0,0]` | 每前进一帧时UV区域移动的距离。 |
| `frames_per_second` | 数值 | `0` | 默认每秒帧数。 |
| `max_frame` | 数值或Molang表达式 | 未设置 | 最大帧号，首帧为`1`。 |
| `stretch_to_lifetime` | 布尔值 | `false` | 为`true`时调整播放速度以匹配粒子寿命。 |
| `loop` | 布尔值 | `false` | 为`true`时动画到达末尾后循环。 |

## 颜色

颜色字段可使用以下形式：

| 形式 | 示例 | 描述 |
| --- | --- | --- |
| 十六进制RGB | `"#ff6600"` | 使用`#RRGGBB`表示不透明颜色。 |
| 十六进制ARGB | `"#ffff6600"` | 使用`#AARRGGBB`表示带Alpha通道的颜色。 |
| RGB数组 | `[1,0.4,0]` | 通道值范围为`0`到`1`。 |
| RGBA数组 | `[1,0.4,0,0.75]` | 第四个通道为不透明度。 |
| 梯度对象 | `{ "gradient": ["#ff6600", "#000000"], "interpolant": "variable.particle_age / variable.particle_lifetime" }` | 使用`interpolant`在颜色数组或按数值键索引的颜色映射之间插值。 |

## 曲线

`curves`对象用于定义插值曲线。每条曲线在每个粒子的每个渲染帧求值，结果写入与曲线键同名的Molang变量。曲线允许通过时间或其他Molang表达式平滑地改变粒子属性，例如从创建到消亡时改变粒子大小、颜色或速度。文档要求曲线变量名以`variable.`开头，例如`variable.size_curve`。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `type` | 字符串 | 未设置 | 曲线类型。可为`linear`、`bezier`、`bezier_chain`或`catmull_rom`。不同类型提供不同的光滑程度和控制精度。 |
| `input` | 数值或Molang表达式 | 未设置 | 曲线输入值。常见写法为`variable.particle_age / variable.particle_lifetime`（从`0`到`1`的归一化粒子生命周期）。也可使用`variable.particle_age`（秒为单位的绝对时间）或其他表达式。 |
| `horizontal_range` | 数值或Molang表达式 | `1` | 将输入映射到`0`至该值之间。该字段对`bezier_chain`无效，且文档标记为已弃用。 |
| `nodes` | 数组或对象 | 未设置 | 曲线控制节点。`linear`、`bezier`和`catmull_rom`可使用均匀分布的节点数组；`bezier_chain`使用按输入值索引的节点对象，键值为输入值（`0.0`至`1.0`）。 |

| 曲线类型 | 描述 | 用途 |
| --- | --- | --- |
| `linear` | 分段线性曲线，节点在应用`input`和`horizontal_range`后均匀分布于`0`至`1`。相邻节点之间为直线插值。 | 简单的分段动画，如粒子大小突然变化。 |
| `bezier` | 四节点贝塞尔曲线，首末节点为`0`和`1`处的取值，中间两个节点形成斜率控制点。提供平滑的三次样条曲线。 | 自然的曲线变化，如加速减速动画。 |
| `catmull_rom` | 通过除首末节点外所有节点的曲线。首末节点不作为曲线经过点，而用于形成相邻点的斜率。 | 多点平滑曲线，适合多段控制。 |
| `bezier_chain` | 多段贝塞尔链。每个节点可声明取值（`value`）、左斜率（`left_slope`）、右斜率（`right_slope`）或统一斜率（`slope`）。节点会在解析前按键排序。 | 复杂的渐变，如多段颜色渐变或分段动画。 |

### 曲线示例

```json title="线性曲线"
"curves": {
  "variable.size_curve": {
    "type": "linear",
    "input": "variable.particle_age / variable.particle_lifetime",
    "nodes": [0.1, 0.5, 0.1]
  }
}
```

```json title="贝塞尔链曲线"
"curves": {
  "variable.color_curve": {
    "type": "bezier_chain",
    "input": "variable.particle_age / variable.particle_lifetime",
    "nodes": {
      "0.0": { "value": 1.0, "slope": 0.0 },
      "0.5": { "value": 2.0, "slope": 1.0 },
      "1.0": { "value": 0.0, "slope": -1.0 }
    }
  }
}
```

## 事件

`events`对象声明可由发射器寿命、粒子寿命、碰撞等组件触发的事件。事件节点可以直接执行动作，也可以通过`sequence`按顺序执行多个节点，或通过`randomize`按权重选择一个节点。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `sequence` | 数组 | 未设置 | 按顺序执行的事件节点数组。 |
| `randomize` | 数组 | 未设置 | 按权重选择的事件节点数组。每项可包含`weight`。 |
| `particle_effect` | 对象 | 未设置 | 生成其他粒子特效或在目标发射器上手动发射粒子。 |
| `sound_effect` | 对象 | 未设置 | 播放关卡音效事件。 |
| `expression` | Molang表达式 | `0` | 在触发事件的发射器上执行的表达式。 |
| `log` | 字符串 | 空字符串 | 调试用日志文本。日志会连同粒子特效名称和事件位置写入内容日志。 |

### `particle_effect`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `effect` | 字符串 | 未设置 | 要生成或手动发射的粒子特效标识符。 |
| `type` | 字符串 | 未设置 | 生成方式。可为`emitter`、`emitter_bound`、`particle`或`particle_with_velocity`。 |
| `pre_effect_expression` | Molang表达式 | `0` | 事件触发后在新发射器上执行一次的表达式。该表达式不能访问触发事件的发射器Molang数据。 |

| `type`值 | 描述 |
| --- | --- |
| `emitter` | 在事件世界位置创建一个新的发射器。该发射器为即发即忘效果。 |
| `emitter_bound` | 与`emitter`相似；如果触发事件的发射器绑定到活动对象或定位器，新发射器也绑定到相同活动对象或定位器。 |
| `particle` | 在`effect`对应的发射器上手动发射一个粒子；如发射器不存在则创建发射器。目标效果通常需要使用`minecraft:emitter_rate_manual`。 |
| `particle_with_velocity` | 与`particle`相似，但新粒子继承触发粒子的速度。 |

### `sound_effect`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `event_name` | 字符串 | 未设置 | 要播放的关卡音效事件名称。 |

## 粒子Molang变量

粒子系统允许大多数字段使用Molang表达式。除通用Molang能力外，粒子上下文提供以下变量。这些变量对发射器和粒子的Molang表达式均可访问，但在不同上下文中代表不同的值。

| 变量 | 类型 | 描述 |
| --- | --- | --- |
| `variable.emitter_age` | 数值 | 当前发射器循环开始后经过的时间（秒）。 |
| `variable.emitter_lifetime` | 数值 | 当前发射器循环持续的时间（秒）。发射器寿命组件决定该值。 |
| `variable.emitter_random_1` | 数值 | 当前发射器循环内保持不变的`0.0`至`1.0`随机数。整个循环期间该值固定，不随帧变化。 |
| `variable.emitter_random_2` | 数值 | 当前发射器循环内保持不变的第二个随机数。 |
| `variable.emitter_random_3` | 数值 | 当前发射器循环内保持不变的第三个随机数。 |
| `variable.emitter_random_4` | 数值 | 当前发射器循环内保持不变的第四个随机数。 |
| `variable.entity_scale` | 数值 | 粒子特效挂接到实体时，该值为实体的缩放系数。未挂接时该值为`1.0`。 |
| `variable.particle_age` | 数值 | 粒子已存活的时间（秒）。粒子生成时为`0.0`，每帧递增。 |
| `variable.particle_lifetime` | 数值 | 粒子的总寿命（秒）。粒子寿命组件决定该值。 |
| `variable.particle_random_1` | 数值 | 粒子生命周期内保持不变的`0.0`至`1.0`随机数。 |
| `variable.particle_random_2` | 数值 | 粒子生命周期内保持不变的第二个随机数。 |
| `variable.particle_random_3` | 数值 | 粒子生命周期内保持不变的第三个随机数。 |
| `variable.particle_random_4` | 数值 | 粒子生命周期内保持不变的第四个随机数。 |

### 自定义Molang变量

可以通过`minecraft:emitter_initialization`和`minecraft:particle_initialization`组件设置自定义变量。这些组件允许使用`creation_expression`和`per_update_expression`来初始化和维护自定义变量。例如：

```json
"minecraft:emitter_initialization": {
  "creation_expression": "variable.my_speed = 2.0; variable.my_color = 1.0;"
},
"minecraft:particle_initialization": {
  "creation_expression": "variable.particle_color_variance = variable.particle_random_1 * 0.2;"
}
```

### 曲线变量

曲线定义在`curves`对象中的变量会在每个渲染帧被求值并写入对应的Molang变量。例如，如果定义了`variable.size_gradient`曲线，该变量可在`minecraft:particle_appearance_billboard`的`size`字段中直接使用。

## 实体挂接

粒子特效可以与实体关联，从而跟随实体运动并响应实体的动画和状态。实体挂接粒子通常用于角色增强效果、伤害反馈、法术效果、周期环境效果等场景。

### 定位器

**定位器（Locator）**是粒子特效绑定到几何体中的具体位置。实体可在几何体中声明定位器，粒子发射器可跟随指定定位器的位置和方向。定位器随几何体动画而改变位置，从而实现粒子跟随手部、头部、特定部位的效果。

### 实体资源定义中的粒子

| 位置 | 字段 | 类型 | 描述 |
| --- | --- | --- | --- |
| 客户端实体定义`minecraft:client_entity.description` | `particle_effects` | 对象 | 将实体内部短名称映射到粒子特效标识符。例如`{ "flame_effect": "minecraft:flame_particle" }`。该映射本身不会播放粒子；粒子需由动画或动画控制器触发。 |
| 客户端实体定义`minecraft:client_entity.description` | `locators` | 对象 | 将定位器短名称映射到几何体中的定位器名称。例如`{ "left_hand": "geometry.humanoid.left_hand" }`。粒子可使用这些短名称在指定位置生成。 |

### 动画控制器中的粒子

动画控制器状态可在进入时启动粒子效果，在退出时终止效果。这用于状态相关的效果，如攻击时的冲击波、施法时的光环等。

```json
"states": {
  "attack": {
    "particle_effects": [
      {
        "effect": "attack_effect"
      }
    ],
    "transitions": [
      { "idle": "!query.is_attacking" }
    ]
  }
}
```

### 动画时间线中的粒子

动画可在时间轴的特定时间点触发即发即忘粒子特效。这用于特定动作瞬间的效果，如剑击时的刀光、脚步着地时的尘埃等。

```json
"animations": {
  "attack": {
    "animation_length": 1.0,
    "particle_effects": {
      "0.3": [
        { "effect": "sword_slash" }
      ],
      "0.7": [
        { "effect": "impact_spark" }
      ]
    }
  }
}
```

### 粒子效果事件

粒子效果项通常包含以下字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `effect` | 字符串 | 未设置 | 客户端实体`description.particle_effects`中声明的粒子短名称。 |
| `locator` | 字符串 | 未设置 | 可选。粒子发射器跟随的定位器短名称。未设置时粒子在实体原点生成。 |
| `pre_effect_script` | Molang表达式 | 未设置 | 可选。发射器启动时执行的Molang表达式。常用于根据实体状态设置粒子颜色、缩放等变量。 |

### 示例

以下为火焰型生物的粒子挂接示例：

```json
{
  "format_version": "1.8.0",
  "minecraft:client_entity": {
    "description": {
      "identifier": "minecraft:blaze",
      "particle_effects": {
        "flame": "minecraft:mobflame_emitter",
        "attack_spark": "minecraft:attack_spark"
      },
      "locators": {
        "left_hand": "geometry.humanoid.left_hand",
        "right_hand": "geometry.humanoid.right_hand"
      }
    }
  }
}
```

```json
{
  "format_version": "1.8.0",
  "animation_controllers": {
    "controller.animation.blaze.flame": {
      "states": {
        "default": {
          "transitions": [ { "attacking": "query.is_charged" } ]
        },
        "attacking": {
          "particle_effects": [
            { "effect": "flame" }
          ],
          "transitions": [ { "default": "!query.is_charged" } ]
        }
      }
    }
  }
}
```

## 示例

```json title="particles/basic_flame.json"
{
  "format_version": "1.10.0",
  "particle_effect": {
    "description": {
      "identifier": "demo:basic_flame",
      "basic_render_parameters": {
        "material": "particles_alpha",
        "texture": "textures/particle/particles"
      }
    },
    "components": {
      "minecraft:emitter_rate_instant": {
        "num_particles": 1
      },
      "minecraft:emitter_lifetime_expression": {
        "activation_expression": 1,
        "expiration_expression": 0
      },
      "minecraft:emitter_shape_sphere": {
        "radius": 0.025,
        "direction": [0, 0, 0]
      },
      "minecraft:particle_lifetime_expression": {
        "max_lifetime": "math.random(0.6, 2.0)"
      },
      "minecraft:particle_appearance_billboard": {
        "size": [
          "(0.1 + variable.particle_random_1 * 0.1) - (0.1 * variable.particle_age)",
          "(0.1 + variable.particle_random_1 * 0.1) - (0.1 * variable.particle_age)"
        ],
        "facing_camera_mode": "lookat_xyz",
        "uv": {
          "texture_width": 128,
          "texture_height": 128,
          "uv": [0, 24],
          "uv_size": [8, 8]
        }
      }
    }
  }
}
```

## 相关页面

- [粒子](../../docs/addon/particle.md)
- [粒子发射器](../../docs/addon/particle-emitter.md)
- [Molang](../../docs/general/molang.md)
- [客户端实体定义](client-entity.md)
- [动画定义](animation.md)
- [动画控制器](animation-controller.md)
# 认识Molang

Molang是基岩版附加包里最常见的“小公式”。当JSON字段不能只写死一个值，而是要根据实体状态、动画时间、方块状态或随机数变化时，你通常会遇到Molang。

你不需要把Molang当成一门大型编程语言。更合适的理解是：它在游戏需要某个值时快速算出这个值，然后把结果交给动画、粒子、渲染控制器、方块置换或实体组件使用。

## 第一个表达式

```molang
query.health < 5 ? 1 : 0
```

这条表达式的意思是：如果当前实体生命值小于5，返回1；否则返回0。在很多条件位置，1会被当成真，0会被当成假。

如果要让一个值随时间周期变化，可以用数学函数：

```molang
math.sin(query.life_time * 360) * 40
```

`query.life_time`会随着实体存在时间增长，`math.sin`会产生正负往复变化，所以这类表达式很适合做摇摆、呼吸、闪烁等效果。

## 写在什么地方

Molang通常写在资源包或行为包的JSON文件里。常见位置包括：

- 动画文件：控制骨骼的位置、旋转和缩放。
- 动画控制器：决定状态什么时候转移。
- 渲染控制器：选择几何体、材质、纹理或控制模型部件可见性。
- 粒子特效：控制粒子寿命、大小、速度和发射条件。
- 实体定义：预先计算变量，或在部分组件字段中返回数值。
- 方块定义：在方块置换条件中判断方块状态。

不要假设同一个表达式在所有地方都能使用。每个位置能读取的查询函数、变量和资源类型都可能不同。

## 常用作用域

| 写法 | 含义 | 示例 |
|------|------|------|
| `query.`或`q.` | 游戏提供的只读查询。 | `q.is_on_ground` |
| `variable.`或`v.` | 当前实体上的变量，可读写。 | `v.timer = (v.timer ?? 0) + q.delta_time` |
| `temp.`或`t.` | 本次表达式求值中的临时变量，可读写。 | `t.speed = q.ground_speed * 1.2` |
| `context.`或`c.` | 当前上下文提供的只读变量。 | `c.item_slot` |

`query`最常见，因为它能读取实体状态、时间、位置和渲染上下文。`variable`适合保存实体还存在时需要复用的状态，但它不会保存到存档里；重新进入世界或实体被卸载后，变量需要重新初始化。`temp`适合中间计算，不要把它当成长期存储。`context`由具体调用位置提供，不能写入。

## 简单表达式和复杂表达式

只有一条表达式时，通常不要写分号：

```molang
math.cos(q.anim_time * 38) * 80
```

如果你要写多条语句，每条语句都要用分号结束，并用`return`明确返回结果：

```molang
t.wave = math.sin(q.anim_time * 360);
t.scale = 1.0 + t.wave * 0.2;
return t.scale;
```

如果复杂表达式没有执行`return`，结果会是0。这是很多“表达式看起来写了很多，但游戏里没有效果”的原因。

## 条件和默认值

Molang的逻辑写法和很多编程语言相似：

```molang
q.is_sneaking && q.is_using_item
```

`&&`表示并且，`||`表示或者，`!`表示取反。三元表达式写作：

```molang
条件 ? 为真时的值 : 为假时的值
```

如果变量可能还没有初始化，可以用`??`提供默认值：

```molang
v.timer = (v.timer ?? 0) + q.delta_time
```

这表示：如果`v.timer`已经有值，就用原值；如果它还不可用，就先当成0。

## 在实体定义中预先计算

客户端实体定义的`scripts.pre_animation`会在动画和渲染控制器处理前执行。你可以在这里把后面多次使用的值提前算好：

```json
"scripts": {
  "pre_animation": [
    "variable.wing_flap = ((math.sin(query.wing_flap_position * 57.3) + 1) * query.wing_flap_speed);"
  ]
}
```

之后，动画文件就可以直接读取这个变量：

```json
"wing0": {
  "rotation": [0.0, 0.0, "variable.wing_flap - this"]
}
```

这种写法的好处是：同一个复杂计算只需要维护一次，也能让动画文件更容易阅读。

## 在动画中使用

动画文件经常用Molang控制骨骼变换。下面的写法会让头部绕Z轴摆动：

```json
"head": {
  "rotation": [0, 0, "math.sin(query.life_time * 360) * 40"]
}
```

在动画里，`this`表示当前通道原本要写入的值。原版动画常用`- this`或`目标值 - this`抵消已有值或叠加差值。修改原版表达式时，不要随意删掉`this`，否则骨骼姿态可能突然偏移。

## 在动画控制器中使用

动画控制器用Molang决定状态转移。例如：

```json
"transitions": [
  {
    "sitting": "query.is_sitting"
  }
]
```

这表示当`query.is_sitting`为真时，进入`sitting`状态。动画控制器适合处理“什么时候播放哪组动画”。如果你只是想让动画权重随条件变化，也可以在客户端实体定义的`scripts.animate`中传入Molang：

```json
"animate": [
  "look_at_target",
  {
    "move": "query.modified_move_speed"
  },
  {
    "baby_transform": "query.is_baby"
  }
]
```

需要注意：`scripts.animate`里的数值通常控制动画混合权重，不一定会让动画每次从头播放。需要严格重新播放时，优先考虑动画控制器状态。

## 在渲染控制器中使用

渲染控制器可以用Molang选择资源，也可以控制部件可见性：

```json
"part_visibility": [
  { "leg*": "!query.is_sleeping" },
  { "head": "!query.is_sleeping" },
  { "head_sleeping": "query.is_sleeping" }
],
"textures": [ "array.skins[query.variant]" ]
```

这里`query.is_sleeping`控制普通头部和睡眠头部是否可见，`query.variant`从纹理数组中选择皮肤。数组越界不会直接报错：负数会当成0，超过末尾的正数会回绕到数组前面。这个特性可以用来循环资源，但也可能掩盖错误索引。

资源引用必须返回正确类型。写在`textures`里的表达式应返回纹理，写在`geometry`里的表达式应返回几何体，写在`materials`里的表达式应返回材质。

## 在粒子中使用

粒子文件也大量使用Molang。比如下面的片段用随机数决定粒子寿命，并让粒子大小随年龄变化：

```json
"minecraft:particle_lifetime_expression": {
  "max_lifetime": "math.random(0.6, 2.0)"
},
"minecraft:particle_appearance_billboard": {
  "size": [
    "(0.1 + variable.particle_random_1 * 0.1) - (0.1 * variable.particle_age)",
    "(0.1 + variable.particle_random_1 * 0.1) - (0.1 * variable.particle_age)"
  ]
}
```

粒子中的变量和实体动画中的变量不一定相同。复制表达式前，要确认当前粒子组件是否提供这些变量。

## 调试建议

1. 先把表达式改成固定数值，确认文件路径、标识符和调用位置正确。
2. 再逐步加入查询函数和数学运算，每次只改一小段。
3. 多语句表达式一定检查分号和`return`。
4. 对可能未初始化的变量使用`??`。
5. 打开内容日志，优先修复Molang错误和资源引用错误。
6. 升级清单文件的`min_engine_version`后，重新检查复杂条件表达式和方块状态相关查询。

Molang很适合做即时计算，但不适合塞进整套玩法逻辑。把长期状态交给实体组件、事件、动画控制器或脚本API，把Molang留给“这一刻需要算出的值”，会更稳定也更容易排错。

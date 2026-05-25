# 物品组件（中国版）<!-- md:flag china -->

本页列出中国版行为包物品定义中`minecraft:item.components`对象可用的中国版专有物品组件，组件键使用`netease:`命名空间。这些组件由网易维护，仅在中国版中生效；国际版客户端将忽略或对这些组件发出警告。物品定义的根结构见[物品定义](item.md)，国际版物品组件见[物品组件](item-component.md)。

中国版自定义物品除本页所列组件外，还提供针对武器、盔甲、盾牌、桶、弹射物等特定物品类型的专用组件。这些专用组件需在`description.custom_item_type`中声明对应类型后方可使用，此处不作展开。

## 组件一览

| 组件 | 值形态 | 用途 | 主要字段与限制 |
| --- | --- | --- | --- |
| `netease:allow_offhand` | 对象 | 控制物品是否可放入副手槽位。 | `value`为布尔值。副手槽位对部分组件（如`minecraft:foil`、`netease:render_offsets`）不生效，且基岩版原版副手功能较弱，主要用于装饰性展示或脚本逻辑判断。 |
| `netease:cooldown` | 对象 | 为物品使用添加冷却。 | `category`为字符串，相同类别的物品共享同一冷却计时（默认值为`"item"`）；`duration`为冷却时间（整数，单位为刻）。自定义食品的冷却时间应定义在`minecraft:food`中，而非使用此组件。 |
| `netease:customtips` | 对象 | 为物品添加自定义描述信息。 | `value`为字符串，支持格式化代码（如`§8`）；描述显示于物品名称下方。与方块组件`netease:custom_tips`作用相同。 |
| `netease:enchant_material` | 对象 | 控制物品是否可作为附魔台的附魔材料。 | `value`为布尔值，默认`false`。启用后，物品可在附魔台中作为消耗材料。 |
| `netease:fire_resistant` | 对象 | 控制物品掉落物是否免疫火焰和熔岩。 | `value`为布尔值。效果与下界合金一致：掉落物不被火烧毁，掉入熔岩时弹出。 |
| `netease:fuel` | 对象 | 允许物品作为熔炉燃料。 | `duration`为燃烧时长（浮点数，单位为秒）；省略或设为`0`时无燃烧效果。 |
| `netease:show_in_hand` | 对象 | 控制物品手持时是否显示模型或纹理。 | `value`为布尔值。设为`false`时，手持该物品不显示任何模型。 |

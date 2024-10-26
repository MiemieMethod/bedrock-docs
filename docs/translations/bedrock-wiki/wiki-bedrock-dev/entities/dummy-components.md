---
标题：虚拟组件
类别：文档
提及：
    - SirLich
    - jigarbov
    - MedicalJewel105
    - StealthyExpertX
    - TheItsNameless
描述：虚拟组件是“无用”的组件，仅用于数据存储。
---

:::警告 废弃警告

“虚拟组件”是一个较旧的概念，主要被[实体属性](https://learn.microsoft.com/en-us/minecraft/creator/documents/introductiontoentityproperties)所取代。您应尽可能考虑使用实体属性。
:::

虚拟组件是“无用”的组件，仅用于数据存储。虚拟组件**不**会单独执行任何操作。它们需要与其他机制配对才能发挥功能。虚拟组件的好处在于它们允许我们在实体上存储信息，并利用这些信息驱动图形/游戏机制。

好的例子包括`variant`和`mark_variant`。这些组件可以设置为整数值。在原版资源包中，这个整数用于选择猫和马的纹理。另一个好的例子是`is_tamed`，它用于马来处理是否可以骑乘。

虚拟组件的优点在于它们允许我们保存有关实体的数据，然后使用Molang查询这些数据。

## 整数虚拟组件

整数虚拟组件设置为整数值，这允许您存储数字，例如1、10或1423。这些整数可以通过查询读取。整数虚拟组件是最有用的。

## 位虚拟组件

位虚拟组件存储单个位的信息。即`True`或`False`。例如`is_tamed`，它可以是`False`（未添加到实体）或`True`（已添加到实体）。

## 虚拟组件

| 类型      | 查询                                                         | 组件                          | 备注                                                                                                                             |
|-----------|---------------------------------------------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **整数**   | q.variant                                                     | minecraft:variant            |                                                                                                                                   |
| **整数**   | q.mark_variant                                                | minecraft:mark_variant       |                                                                                                                                   |
| **整数**   | q.skin_id                                                     | minecraft:skin_id            |                                                                                                                                   |
| **整数\*** | 过滤器如：“test”:“is_color”，颜色如下提供。                 | minecraft:color              | 也在材料中设置颜色。                                                                                                           |
| **整数\*** | 无已知过滤器，但可以与“has_component”一起使用               | minecraft:color2             | 也在材料中设置颜色。                                                                                                           |
| 位       | q.is_illager_captain                                          | minecraft:is_illager_captain |                                                                                                                                   |
| 位       | q.is_baby                                                     | minecraft:is_baby            | 禁用`minecraft:breedable`的使用                                                                                                 |
| 位       | q.is_sheared                                                  | minecraft:is_sheared         |                                                                                                                                   |
| 位       | q.is_saddled                                                  | minecraft:is_saddled         |                                                                                                                                   |
| 位       | q.is_tamed                                                    | minecraft:is_tamed           |                                                                                                                                   |
| 位       | q.is_chested                                                  | minecraft:is_chested         | 死亡时将掉落箱子                                                                                                              |
| 位       | q.is_powered                                                  | minecraft:is_charged         |                                                                                                                                   |
| 位       | q.is_stunned                                                  | minecraft:is_stunned         |                                                                                                                                   |
| 位       | q.can_climb                                                   | minecraft:can_climb          | 允许实体爬梯子                                                                                                                  |
| 位       | q.can_fly                                                     | minecraft:can_fly            | 标记实体可以飞行，路径查找器不会限制在需要下方有实心方块的路径上。                                                             |
| 位       | q.can_power_jump                                              | minecraft:can_power_jump     | 允许实体像原版中的马一样进行强力跳跃。                                                                                           |
| 位       | q.is_ignited                                                  | minecraft:is_ignited         |                                                                                                                                   |
| 位       | q.out_of_control                                              | minecraft:out_of_control     | 新增，用于代码中的硬编码船只移动/粒子效果，以及Molang查询。可能是安全的。                                                     |
| 位   | q.has_any_family('monster')                            | minecraft:type_family         | 可以使用家族类型并返回来自家族（如“monster”）的位值，值为真或假。

### color和color2组件的颜色

-   黑色
-   蓝色
-   棕色
-   青色
-   灰色
-   绿色
-   浅蓝色
-   浅绿色
-   品红
-   橙色
-   粉色
-   紫色
-   红色
-   银色
-   白色
-   黄色
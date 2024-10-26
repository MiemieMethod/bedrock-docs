---
标题：命名空间
提及：
    - SirLich
    - MedicalJewel105
描述：命名空间是标识内容所有权的标识符，它们有助于避免命名冲突的发生。
---

命名空间是标识内容所有权的标识符。你可以将它们视为文件夹。命名空间有助于避免命名冲突的发生。

在附加包创建中，命名空间本质上可以被视为“冒号左侧的部分”。例如，`minecraft` 是 `minecraft:zombie` 的命名空间。其一般形式为 `namespace:name`。

为了具体说明命名空间为何有用，假设你创建了一个新的生物。你将其命名为 `minecraft:shark`，而不知道你应该为自定义内容创建自己的命名空间。明年，Mojang 决定将鲨鱼添加到游戏中！现在就出现了命名冲突，因为存在两个 `minecraft:shark` 的定义。你的附加包将会崩溃。

如果你使用的是 `your_namespace:shark`，则不会发生命名冲突。

## 选择命名空间

合适的命名空间是独特的。像 `mob`、`cars`、`content` 或 `custom` 这样的命名空间是**不好的**选择，因为其他开发者可能会与你使用相同的命名空间。

合适的命名空间应该简短。你将会频繁使用你的命名空间，因此越短越好。`george_carlin_the_comedian` 由于这个原因将是一个糟糕的命名空间。

对于个人项目，我建议使用你玩家名称的简便版本，而对于商业项目，我建议使用公司名称的合适版本。

一些好的示例：

-   `gcarlin`
-   `sirlich`
-   `cubeworld`
-   `bworks`

**切勿使用** `minecraft` 或 `minecon` 作为命名空间，除非编辑原版文件。这不仅是个糟糕的主意，而且 Minecraft 保留了这些命名空间，甚至无法使用。

## 在哪里使用命名空间？

简而言之，你应该尽可能多地使用命名空间。

首先，当向游戏添加自定义实体时，你应该使用命名空间。

`sirlich:shark` 比 `shark` 更好。

你还应该在组件和事件中使用命名空间。就像 Mojang 使用 `minecraft:pig_saddled` 一样，你应该使用 `namespace:my_mob_event` 和 `namespace:my_component_group`。

在动画控制器、渲染控制器和动画中也应该使用命名空间。

例如：`controller.animation.namespace.entity_name.action` 比 `controller.animation.my_action` 更好。

## 不要在何处使用命名空间。

实际的文件结构不需要命名空间。

`animations/namespace/my_entity/animation` 比 `animations/my_entity/animation` 更令人困惑。
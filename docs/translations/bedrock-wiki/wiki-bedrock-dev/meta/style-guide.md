---
title: 风格指南
mentions:
    - SirLich
    - solvedDev
    - MedicalJewel105
    - ChibiMango
    - zheaEvyline
description: 官方支持的基岩版维基附加包创建风格指南。
---

本文档将介绍官方支持的基岩版维基附加包创建风格指南。该指南旨在促进附加包创建的最佳实践，并为每个人提供一致的格式。

:::tip
风格指南是一个不断发展的文档，随着附加包创建的演变而演变。如果你认为某些内容需要更新或更改，请与我们联系！
:::

## 文件夹结构

- 文件路径中不得包含空格。`使用下划线`。
- 标识符、文件名或文件夹名中不得使用大写字母。'BP' 和 'RP' 文件夹名可以使用大写字母。
- 任何路径的总字符长度不得超过 80 个字符（控制台限制）。
- 内容文件夹应使用一致的复数形式：保持名称要么全部为复数，要么全部为单数，不要混合使用。例如：

✅️ 一致：
```
BP/functions/abilities/ice_blast.mcfunction
BP/functions/events/player/on_death.mcfunction
BP/functions/events/world/on_initialise.mcfunction
BP/functions/quests/jungle/1.mcfunction
```
- 所有内容文件夹 `abilities`、`events` 和 `quests` 都是复数形式。
- `events` 文件夹中的内容文件夹也保持一致，因为 `player` 和 `world` 都是单数。

❌️ 不一致：
```
BP/functions/ability/ice_blast.mcfunction
BP/functions/event/players/on_death.mcfunction
BP/functions/event/world/on_initialise.mcfunction
BP/functions/quests/jungle/1.mcfunction
```
- 只有 `quests` 内容文件夹是复数形式，而 `ability` 和 `event` 是单数。
- 此外，在 `event` 文件夹中，`players` 文件夹是复数，而 `world` 是单数。

## 标识符

请勿使用以数字开头的标识符，尤其是仅为数字的标识符。这适用于实体、组件组、事件以及任何其他需要 `namespace:name` 对的内容。

## 文件和文件夹名称

| 概念                | 示例标识符               |
| ------------------- | ------------------------ |
| 行为包              | dragons_BP               |
| 资源包              | dragons_RP               |
| 几何体              | dragon.geo.json          |
| 动画                | dragon.animation.json    |
| 动画控制器         | dragon.ac.json           |
| RP 实体             | dragon.ce.json<br>*(ce: 客户端实体)*|
| BP 实体             | dragon.se.json<br>*(se: 服务器实体)*|
| 物品 1.16.100+      | dragon_tooth.item.json   |
| BP 物品             | dragon_tooth.item.bp.json|
| RP 物品             | dragon_tooth.item.rp.json|
| 渲染控制器         | dragon.rc.json           |
| 战利品表            | dragon.loot.json         |
| 配方                | dragon_saddle.recipe.json|
| 生成规则            | dragon.spawn.json        |
| 交易表              | dragon.trade.json        |
| 粒子                | dragon_magic.particle.json|
| 纹理                | dragon.png               |
| 游戏测试            | dragonTest.js            |

## 命名空间

合适的命名空间应对你或你的团队独特。像 `mob`、`cars`、`content` 或 `custom` 这样的命名空间是 **不好的** 命名空间，因为其他开发者可能会使用与你相同的命名空间。

`minecraft` 和 `minecon` 是保留的。请勿使用这些。

对于个人项目，使用你玩家名称的方便版本；对于团队项目，使用你团队名称的合适版本。

当多个开发者共同在一个项目上工作时，命名空间应始终共享。如果需要注明贡献，请使用子索引：`minetite.wiki:dragon`

命名空间的使用场合：

- 实体
- 粒子
- 组件组
- 事件

命名空间不应使用的场合：

- 不要在任何文件夹路径或文件名中包含你的命名空间

## 子索引

子索引是使用 `.` 来分隔链式概念。子索引应按从大到小的顺序排列：

✔️ `animation.controller.dragon.flying.taking_off`

❌ `animation.controller.dragon_take_off_flying`

使用子索引时，使用 `_` 作为空格，而不是另一个 `.`。

✔️ `animation.controller.dragon.flying.taking_off`

❌ `animation.controller.dragon.flying.taking.off`

你可以在实体中使用子索引：
`wiki:dragon.drake`

## 组和事件应相辅相成

| 组        | 事件                  |
| --------- | --------------------- |
| wiki:wild | ✔️ wiki:become_wild   |
| wiki:wild | ❌ wiki:wild          |
| wiki:tame | ✔️ wiki:on_tame       |
| wiki:tame | ❌ wiki:tame          |

## 短名称应为通用

短名称是特定于文件的标识符，用于在标识符和可读名称之间进行映射。它们非常方便，因为它们允许我们重用动画控制器和渲染控制器。因此，你的短名称应为通用。

✔️ `"sit": "animation.dragon.sit"`

❌ `"dragon_sitting": "animation.dragon.sit"`

当我们制作这种形式的短名称时，我们可以使用通用的 "sit" 动画控制器来适用于所有这些，因为我们可以使用 `sit` 短名称来播放坐下动画。

## 函数

1. **函数应嵌套。** 你可以将函数放入文件夹中以实现这一点。
    - ✅️ `function teleport/zone/hell`
    - ❌ `function teleport_hellzone`

2. **函数文件/文件夹名称必须遵循 `action_object` 结构。** 意味着动词应始终在主语之前。
    - ✅️ `add_all`
    - ✅️ `shuffle_position`
    - ❌️ `all_add`
    - ❌️ `position_shuffle`

### 函数中的注释

- 当处理包含许多命令的函数时，使用多个哈希符号在注释中指示不同的标题级别是很有帮助的。
- *可选地*，为了进一步区分这些级别，你可以应用不同的样式：
    - 级别 1 标题 - **# 大写字母**
    - 级别 2 标题 - **## 标题大小写**
    - 级别 3 标题 - **### 句子大小写**
- 尽量避免使用超过三个标题级别或过多的标题，因为这可能会使代码显得杂乱。供你参考，见下面的示例文件：

<Spoiler title="示例函数文件">

<CodeHeader>BP/functions/abilities/fire_trail.mcfunction</CodeHeader>

```yaml
# 玩家物品掉落时

## 给予效果
### 火焰抗性
execute at @e [type=item, name="Fire Trail Ability"] run effect @p [r=3] fire_resistance 10 255
### 速度
execute at @e [type=item, name="Fire Trail Ability"] run effect @p [r=3] speed 10 1 true

## 添加粒子时间 (10秒)
execute at @e [type=item, name="Fire Trail Ability"] run scoreboard players set @p [r=3] abilities.fire_trail 200

## 删除物品
kill @e [type=item, name="Fire Trail Ability"]


# 实体计时器

## 发出粒子轨迹
execute at @a [scores={abilities.fire_trail=1..}] run particle minecraft:basic_flame_particle ~~~

## 倒计时
scoreboard players remove @a [scores={abilities.fire_trail=1..}] abilities.fire_trail 1
```

</Spoiler>

请注意，在级别 1 标题前使用两行空格，在级别 2 标题前使用一行空格，以提高可读性。

这一做法有助于创建一致的格式，使每个人都能更容易遵循，并在你的函数中保持统一性。

## 记分板和标签

- 记分板目标应使用 `snake_case` 命名，而记分板虚拟玩家名称应使用 **PascalCase**。这种区分使得在输入记分板命令时更容易区分两者。
- 标签应使用 `camelCase`，因为它们通常表示状态或条件，并与变量名称的常见约定保持一致。

**示例标签名称：**

- `admin`
- `inNether`
- `isFlying`
- `abilityFireTrail`
- `abilityWallClimb`

*仅限字母数字字符。*

**示例虚拟玩家名称：**

- `AlivePlayer`
- `ZombieHorse`
- `OresEmerald`
- `OresDiamond`
- `OresDeepslateDiamond`

*仅限字母数字字符。*

**示例目标名称：**

- `ticks`
- `entity_timer`
- `abilities.fire_trail`
- `abilities.wall_climb`
- `abilities.ice_blast`

*仅限 **小写** 字母数字字符、下划线 (`_`) 和点 (`.`)。*

对于目标，可以使用点表示法 (`dot.notation`) 来表示组或类别。然而，应谨慎使用，以避免杂乱并保持可读性。

## 尽可能将动画文件分组

示例：

<CodeHeader></CodeHeader>

```json
{
    "format_version": "1.8.0",
    "animations": {
        "animation.dragon.sit": {...},
        "animation.dragon.fly": {...},
        "animation.dragon.roar": {...},
  }
}
```

## 按路径而不是名称拆分纹理

✔️ `textures/dragon/red`

❌ `textures/dragon_red_skin`

✔️ `textures/npc/dragon_hunter/archer`

❌ `textures npc/dragon_hunter_archer`

## .lang 文件注释

针对本地化者的注释应始终是行内的，格式如下：

`the.key=字符串<\t>## 注释，供本地化者使用。`

`<\t>` 代表一个制表符。

单独的行注释可用于组织目的，但不应存储本地化关键的信息。

## 讨论时的缩写

| 缩写   | 概念                            |
| ------ | -------------------------------- |
| BP     | 行为包                          |
| RP     | 资源包                          |
| FP     | 函数包                          |
| VRP    | 香草资源包                      |
| VBP    | 香草行为包                      |
| AC     | 动画控制器                     |
| RPAC   | 资源包动画控制器               |
| BPAC   | 行为包动画控制器               |
| BB     | Blockbench                      |
| BDS    | 基岩专用服务器                  |
| FPV    | 第一人称视角                    |
| RD     | 渲染龙                          |
| VSCode | Visual Studio Code               |
| SP     | 皮肤包                          |

## 块/物品格式顺序

块和物品应遵循以下格式顺序。这特别有助于理解文件中后面出现的组件将应用于块的变体。

### 块

-   format_version
-   minecraft:block
    -   description
        -   identifier
        -   menu_category
        -   states
        -   traits
    -   components
    -   permutations
        -   condition
        -   components

### 物品

-   format_version
-   minecraft:item
    -   description
        -   identifier
        -   menu_category
    -   components

## 自定义组件变量名称

自定义组件的变量名称应使用 PascalCase，并以 BlockComponent 或 ItemComponent 作为后缀。例如，`MeltableBlockComponent` 而不是 `meltable`。这有助于区分我们在 `registerCustomComponent` 中使用的内容和在其他地方使用的值。
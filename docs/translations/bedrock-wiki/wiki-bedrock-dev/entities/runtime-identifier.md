---
title: 运行时标识符
category: 文档
mentions:
    - MedicalJewel105
    - aexer0e
    - Luthorius
    - SirLich
    - TheDoctor15
    - ChibiMango
    - stirante
    - epxzzy
    - IlkinQafarov
    - TheItsNameless
    - SmokeyStack
    - ThomasOrs
    - Goatfu
    - MRBBATES1
description: runtime_identifier 是一个可选参数，位于实体行为文件的描述中，用于模仿原版实体的硬编码元素。
---

`runtime_identifier` 是一个可选参数，位于实体行为文件的描述中，用于模仿原版实体的硬编码元素。它接受原版Minecraft的标识符，例如 `minecraft:shulker`。

<CodeHeader>行为实体描述</CodeHeader>

```json
"description": {
    "identifier": "wiki:my_box",
    "runtime_identifier": "minecraft:shulker", // 这是运行时标识符。它将为该实体添加Shulker的硬编码行为。
    "is_spawnable": true,
    "is_summonable": true,
    "is_experimental": false
}
```

:::tip
重要的是要记住，`runtime_identifier` 仅会解析实体的硬编码属性。这意味着使用100%数据驱动的生物作为运行时标识符不会为您的实体添加任何新属性。此外，一些实体的运行时可能会覆盖在组件部分中找到的属性，即使它们已被添加，例如Shulker实体的碰撞盒大小。
:::

:::warning
并非所有运行时ID/效果都在此提及。尝试自己进行实验以发现新的运行时ID/效果，并考虑将它们添加到此处。
:::

## 已知的运行时标识符效果：

-   所有运行时ID将实体的名称更改为其使用的运行时ID实体的名称。

### minecraft:area_effect_cloud

-   使实体破坏。

---

### minecraft:armor_stand

-   禁用实体阴影。
-   拳击实体将使其立即消失。
-   可以在实体上放置/移除装备。
-   使实体在死亡时掉落一个盔甲架物品。

---

### minecraft:arrow

-   为投射物实体添加面朝玩家的动画。
-   禁用死亡动画、声音和粒子效果。
-   使实体的阴影变小，但不会消失。
-   不能与之互动。
-   如果通过蛋或/summon命令生成，当玩家与实体接触时，会给予玩家一支箭，然后实体会自我移除。
-   运动物理和击退效果类似于箭。

---

### minecraft:axolotl
-   不影响任何游泳/移动/重力行为。
-   与热带鱼相同，不同的变体和标记变体值会给出不同的桶名称，例如 `成年白化轴鳍桶` 或 `幼年黄色轴鳍桶`。
年龄：成年，幼年
颜色变体：白化，野生，黄色，青色，蓝色。

---

### minecraft:bee

-   为实体添加蜜蜂声音。

---

### minecraft:blaze

-   添加烈焰燃烧声效和粒子效果。
-   实体将像烈焰一样飞行（即使您没有飞行行为）。

---

### minecraft:boat

-   骑乘时添加口袋船用户界面。
-   防止实体旋转。
-   实体具有固体、船形的碰撞盒。

---

### minecraft:chest_minecart

-   使实体破坏。
-   拳击实体将使其消失。
-   生成方式奇怪。
-   掉落箱子和矿车。

---

### minecraft:chicken

-   破坏一些动画。
-   更新移动速度。
-   实体将缓慢下落，但仍然会受到坠落伤害。
-   生成时没有装备（如果有的话）。

---

### minecraft:cod

-   使实体在不在水中时翻滚。
-   与水桶互动将给予您一桶鳕鱼，但当桶中的鳕鱼被放置时，将放置桶装实体而不是鳕鱼。
-   赋予实体特殊的游泳和重力行为。

---

### minecraft:command_block_minecart

-   使实体破坏。
-   拳击实体将使其消失。
-   生成方式奇怪。
-   掉落矿车。

---

### minecraft:cow

-   破坏一些动画。
-   更新移动速度。
-   生成时没有装备（如果有的话）。

---

### minecraft:dolphin

-   添加 `minecraft:movement.dolphin` 组件。

---

### minecraft:donkey

-   更改纹理、模型和动画为驴的样式。

---

### minecraft:dragon_fireball

-   完全破坏您的实体。
-   发出龙火球轨迹粒子。

---

### minecraft:egg

-   为投射物实体添加面朝玩家的动画。
-   使实体破坏。
-   使用其生成蛋生成此类实体时，它将在玩家位置生成，而不是您放置的位置。它还会朝向天空。

---

### minecraft:elder_guardian

-   更改纹理、模型和动画为老守卫的样式。
-   更改一些行为。

---

### minecraft:ender_crystal

-   实体将固定在其生成的方块中心。
-   除非被传送，实体将始终保持其位置。
-   可以放置在任何表面上。
-   将始终被其他实体推动。
-   不能配置为受到伤害。
-   不能改变其朝向。
-   可以复活末影龙。
-   将在生成时带有火焰。

---

### minecraft:ender_dragon

-   为实体添加末影龙死亡效果。
-   继承末影龙的碰撞盒。
-   摧毁碰撞盒内的方块，包括实体下方的方块。为了防止它掉落到基岩上，可以在其下方添加一个不可破坏的方块，移除实体的重力或禁用 `mobGriefing` 游戏规则。
-   对碰撞盒内2个方块范围内的玩家造成伤害。
-   增加渲染距离。
-   只能通过 /kill 杀死。

---

### minecraft:ender_pearl

-   破坏实体的行为。
-   当实体受到伤害时生成粒子。

---

### minecraft:endermite

-   当实体受到伤害时生成粒子。
-   导致旋转故障。
-   破坏一些动画。

---

### minecraft:evocation_fang

-   在接触时对实体造成伤害。
-   完全禁用碰撞。

---

### minecraft:falling_block

-   使实体破坏并使其下落。
-   当实体接触地面时，它将没有任何动画地消失。只掉落相思木按钮。
-   移除效果的能力。

### minecraft:horse

-   更改纹理、模型和动画为马的样式。

---

### minecraft:iron_golem

-   允许发起攻击（攻击造成增加的击退并垂直放大）。
-   加速手臂和腿的动画（可以手动修复，约1/4速度）。
-   可能与村庄/村民逻辑相互作用不佳。

---

### minecraft:llama_spit

-   添加羊驼吐口水的粒子效果。

---

### minecraft:minecart

-   禁用实体阴影。
-   使实体在死亡时掉落一个矿车。
-   防止实体旋转。

---

### minecraft:npc

-   在创造模式下，拳击实体将使其立即消失。
-   在生存或冒险模式下，拳击实体不会造成伤害，也不会施加击退。
-   在所有模式下忽略 `minecraft:health` 组件。

---

### minecraft:panda

-   允许 `q.is_grazing` 和 `q.sit_mount` 与 `minecraft:behavior.random_sitting` 组件一起工作。

---

### minecraft:parrot

-   使翅膀拍打动画能够工作。
-   使生物缓慢下落。
-   使其对音乐唱片跳舞。

---

### minecraft:piglin

-   允许 `minecraft:celebrate_hunt` 功能（激活 `q.is_celebrating`）。

---

### minecraft:player

-   激活 `q.movement_direction`。

---

### minecraft:pufferfish

-   使实体在不在水中时翻滚。
-   与水桶互动将给予您一桶河豚，但当桶中的河豚被放置时，将放置桶装实体而不是河豚。
-   赋予实体特殊的游泳和重力行为。

---

### minecraft:salmon

-   使实体在不在水中时翻滚。
-   与水桶互动将给予您一桶鲑鱼，但当桶中的鲑鱼被放置时，将放置桶装实体而不是鲑鱼。
-   赋予实体特殊的游泳和重力行为。

---

### minecraft:sheep

-   允许 `q.is_grazing` 与 `behavior.eat_block` 组件一起工作。

---

### minecraft:shulker

非常适合模仿方块，只要玩家处于冒险模式。

-   固体碰撞盒为1x1x1。
-   实体将固定在其生成的方块中心。
-   如果附着的方块被移除，实体将传送到附近的其他无障碍位置。
-   如果实体在非满方块（例如床、台阶等）上生成，它将传送到附近的其他无障碍位置。
-   固体碰撞盒的宽度和高度无法更改。

---

### minecraft:shulker_bullet

-   实体将留下 `minecraft:shulker_bullet` 粒子的轨迹。

---

### minecraft:slime

-   实体在下落时将生成粘液粒子。
-   实体在死亡时将根据变体生成较低级别的粘液（变体1到5作为默认粘液级别，值大于5将作为默认中等粘液）。
-   允许实体同时攻击并激活粘液跳跃机制（没有此标识符，粘液在攻击时无法旋转，实体将直线跳跃直到失去目标）。

---

### minecraft:snowball

-   移除碰撞盒。
-   您无法再与实体互动。
-   在玩家头部生成。
-   实体忽略重力。
-   移除实体阴影。
-   实体只面朝南。
-   不能发出脚步声。

---

### minecraft:spider

-   允许蛛网不减慢实体。

---

### minecraft:skeleton

-   使实体受到治疗效果的伤害，受到瞬间伤害效果的治疗，并对再生和中毒效果免疫。
-   使实体受到附有毁灭附魔的武器造成的增加伤害。
-   如果变体为1或更大，则用近战和远程攻击施加凋零状态效果。

---

### minecraft:stray

-   使实体受到治疗效果的伤害，受到瞬间伤害效果的治疗，并对再生和中毒效果免疫。
-   使实体受到附有毁灭附魔的武器造成的增加伤害。
-   使实体不受冰冻伤害。

---

### minecraft:squid

-   允许使用特殊行为组件（见squid.json）。
-   当实体受到伤害时发出墨水粒子。

---

### minecraft:thrown_trident

-   为投射物实体添加面朝玩家的动画。
-   禁用死亡动画、声音和粒子效果。
-   使实体的阴影变小，但不会消失。
-   不能与之互动。
-   运动物理和击退效果类似于投掷的三叉戟。

---

### minecraft:tropicalfish

-   使实体在不在水中时翻滚。
-   赋予实体特殊的游泳和重力行为。
-   当右键点击水桶时，会给予您一桶热带鱼。如果实体没有任何 `minecraft:variant`、`minecraft:mark_variant`、`minecraft:color` 和 `minecraft:color2`，则将名称设置为白色Kob，这可能是热带鱼的0变体。如果应用了一个或多个上述组件，则将桶的名称更改为其他名称（并且该桶放置的是实体，而不是带有该名称/数据值的热带鱼）。

---

### minecraft:wither_skull_dangerous

-   使实体在死亡时掉落凋零玫瑰。
-   被该实体杀死的任何实体将在其死亡地点放置凋零玫瑰。奇怪的是，僵尸似乎在死亡时掉落凋零玫瑰，而不是在其死亡地点放置。
-   使实体不断生成粒子（生成的粒子的标识符为 `minecraft:basic_smoke_particle`）。
-   使实体不受重力影响（这似乎导致具有 `minecraft:projectile` 的实体以直线移动）。
-   防止实体受到伤害。
-   仅适用于没有AI目标的实体（因此仅对虚拟实体和投射物有用）。

---

### minecraft:xp_orb

-   完全禁用碰撞。
-   与玩家接触时增加经验值。

### minecraft:zombie

-   使实体受到治疗效果的伤害，受到瞬间伤害效果的治疗，并对再生和中毒效果免疫。
-   使实体受到附有毁灭附魔的武器造成的增加伤害。

---

### minecraft:wither

-   死亡时爆炸。

---
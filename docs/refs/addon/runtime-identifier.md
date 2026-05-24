# 运行时标识符

本页整理行为包实体定义`description.runtime_identifier`的用途与已知风险。该字段用于让自定义实体复用原版实体的硬编码运行时逻辑。内容主要来自官方字段说明与EaseCation社区实测资料，结论可能随版本变化。

## 字段位置

| 路径 | 类型 | 说明 |
| --- | --- | --- |
| `minecraft:entity.description.runtime_identifier` | 字符串 | 目标原版实体标识符，例如`minecraft:shulker`。 |

## 使用约束

- 仅复用硬编码行为，不会自动复制目标实体全部数据驱动组件。
- 运行时行为可能覆盖自定义组件效果，例如碰撞箱、旋转或交互能力。
- 社区测试显示，部分标识符在特定版本会出现异常或崩溃，应在目标版本逐项验证。

## 常见标识符效果

| 标识符 | 已知效果摘要 | 风险等级 | 说明 |
| --- | --- | --- | --- |
| `minecraft:shulker` | 1×1×1固体碰撞、附着方块逻辑、位置约束 | 中 | 常用于实体拟态方块，但碰撞箱难以自定义。 |
| `minecraft:ender_crystal` | 附着方块中心、不可调整朝向、始终可穿越、无法受伤 | 中 | 死亡动画与声音被禁用；适合标记用途，但伤害与交互逻辑受限。 |
| `minecraft:parrot` | 翅膀扑动动画、缓慢下落、播放音乐碟时跳舞 | 低 | 通常作为飞行外观辅助；副作用较少。 |
| `minecraft:iron_golem` | 强化攻击（含竖向击退）、手臂与腿部动画加速约4倍 | 中 | 动画需手动校正约为1/4速度；可能与村庄/村民逻辑产生干扰。 |
| `minecraft:armor_stand` | 盔甲交互与装备逻辑、阴影变化 | 中 | 常用于展示实体；战斗行为与普通生物差异大。 |
| `minecraft:arrow` | 抛射物朝向与碰撞逻辑增强 | 中 | 适合弹射物，但交互与死亡表现受限。 |
| `minecraft:thrown_trident` | 抛射物飞行与击退逻辑增强 | 中 | 与`projectile`组件联用时需验证拾取与回收行为。 |
| `minecraft:piglin` | 允许`minecraft:celebrate_hunt`组件正常生效（激活`query.is_celebrating`） | 低 | 适合需要庆祝行为状态的自定义实体。 |
| `minecraft:spider` | 蜘蛛网不会减速实体 | 低 | 适合需要穿越蜘蛛网的实体。 |
| `minecraft:minecart` | 矿车类运动与碰撞特性、阴影变化 | 中 | 轨道行为依赖硬编码，易与自定义移动组件冲突。 |
| `minecraft:boat` | 船类骑乘逻辑、旋转限制、船形碰撞倾向 | 中 | 常用于载具实体；需联动骑乘与移动组件测试。 |
| `minecraft:sheep` | `query.is_grazing`在`behavior.eat_block`中可正常工作 | 低 | 适合需要吃方块与低头动画的实体。 |
| `minecraft:panda` | `query.is_grazing`与`query.sit_mount`在`behavior.random_sitting`中可正常工作 | 低 | 适合需要坐下与进食动画的实体。 |
| `minecraft:zombie` | 亡灵伤害逻辑：治疗药水造成伤害、伤害药水治疗、免疫生命恢复与中毒、受亡灵杀手加成 | 中 | 会全面接管实体的伤害接收逻辑，请在目标版本充分测试。 |
| `minecraft:wither` | 持续生成烟雾粒子（`minecraft:basic_smoke_particle`、`minecraft:wither_boss_invulnerable`）；有目标时实体上浮 | 中 | 持续粒子有一定性能开销；悬浮行为在受控场景中难以抑制。 |
| `minecraft:skeleton` | 亡灵伤害逻辑（同`minecraft:zombie`） | 中 | 治疗药水造成伤害、伤害药水治疗、免疫生命恢复与中毒、受亡灵杀手加成。 |
| `minecraft:wither_skull_dangerous` | 无视重力倾向、附带特定粒子与伤害行为 | 高 | 对伤害与物理系统影响较强，仅建议受控场景使用。 |
| `minecraft:xp_orb` | 与玩家接触时经验交互、碰撞受限 | 中 | 常用于经验机制实体。 |
| `minecraft:area_effect_cloud` | 社区资料记录存在崩溃风险 | 高 | 不建议在生产包中直接使用。 |
| `minecraft:chest_minecart` | 社区资料记录存在崩溃或异常生成风险 | 高 | 不建议在生产包中直接使用。 |

## 非生物运行时标识符提示

非生物运行时标识符常见于抛射物、运输实体和机制实体。与生物实体相比，它们更可能绕过常规行为组件体系，例如：

- 生命值体系被替换为结构完整性或无生命值。
- 服务端可配置行为能力受限。
- 客户端插值、阴影、朝向更新规则不同。

## 教育版相关标识符

`minecraft:agent`、`minecraft:chalkboard`、`minecraft:tripod_camera`等标识符通常用于教育版环境。<!-- md:flag edu -->

在非教育版运行环境中，这类标识符可能不可用或行为不完整。<!-- md:flag edu -->

## 相关参考

- [实体定义](entity.md)
- [客户端实体定义](client-entity.md)
- [实体组件](entity-component.md)

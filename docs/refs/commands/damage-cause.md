# 伤害原因枚举<!-- md:flag vanilla -->

本页汇总`/damage`命令可用的`damagecause`字符串。该参数用于声明损伤来源类型，并影响死亡消息、减伤逻辑与部分行为包响应分支。

## 用法

```mcfunction
/damage <target> <amount> [cause]
/damage <target> <amount> <cause> entity <damager>
```

当`cause`与实体攻击相关时，可追加`entity <damager>`指定损伤来源实体。

## 枚举列表

| 枚举值 | 语义说明 |
|---|---|
| `all` | 匹配所有来源类型（用于过滤而非施加损伤）。 |
| `anvil` | 铁砧损伤。 |
| `attack` | 普通攻击损伤。 |
| `block_explosion` | 方块爆炸损伤。 |
| `campfire` | 营火损伤。 |
| `charging` | 冲锋类损伤。 |
| `contact` | 接触类损伤。 |
| `drowning` | 溺水损伤。 |
| `entity_attack` | 实体近战攻击损伤。 |
| `entity_explosion` | 实体爆炸损伤。 |
| `fall` | 坠落损伤。 |
| `falling_block` | 下落方块损伤。 |
| `fatal` | 致命损伤类型。 |
| `fire` | 火焰损伤。 |
| `fire_tick` | 燃烧持续损伤。 |
| `fireworks` | 烟花损伤。 |
| `fly_into_wall` | 鞘翅撞墙损伤。 |
| `freezing` | 冻伤。 |
| `lava` | 岩浆损伤。 |
| `lightning` | 雷击损伤。 |
| `magic` | 魔法损伤。 |
| `magma` | 岩浆块损伤。 |
| `none` | 无来源类型。 |
| `override` | 覆盖型损伤。 |
| `ram_attack` | 山羊撞击类损伤。 |
| `piston` | 活塞相关损伤。 |
| `projectile` | 弹射物损伤。 |
| `self_destruct` | 自爆类损伤（主要用于爬行者等）。 |
| `sonic_boom` | 音爆损伤。 |
| `soul_campfire` | 灵魂营火损伤。 |
| `stalactite` | 钟乳石损伤。 |
| `stalagmite` | 石笋损伤。 |
| `starve` | 饥饿损伤。 |
| `suffocation` | 窒息损伤。 |
| `suicide` | 自杀损伤。 |
| `temperature` | 温度损伤。 |
| `thorns` | 荆棘反伤。 |
| `void` | 虚空损伤。 |
| `wither` | 凋灵损伤。 |

## 相关参考

- [国际版命令清单](command-list.md)
- [命令版本](version.md)
- [附加包实体损伤来源](../tables/entities/addon_entity_damage_sources.md)
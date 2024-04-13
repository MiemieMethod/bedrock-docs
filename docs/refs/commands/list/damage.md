# `/damage`

> 文档版本：1.21.0.21

`/damage`命令command.damage.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/damage <target:target> <amount:int> [cause:DamageCause]
```

//// html | div.result
command.damage.1.description

///// define
`target`：<!-- md:samp target -->

- 基本类型。command.damage.target.description

`amount`：<!-- md:samp int -->

- 基本类型。command.damage.amount.description

`cause`：<!-- md:samp DamageCause -->

- 枚举类型，可选。command.enum.damagecause.description枚举值如下：

  |值|描述|
  |---|---|
  |`piston`|command.enum.damagecause.piston|
  |`lava`|command.enum.damagecause.lava|
  |`campfire`|command.enum.damagecause.campfire|
  |`fire`|command.enum.damagecause.fire|
  |`anvil`|command.enum.damagecause.anvil|
  |`magma`|command.enum.damagecause.magma|
  |`soul_campfire`|command.enum.damagecause.soul_campfire|
  |`wither`|command.enum.damagecause.wither|
  |`falling_block`|command.enum.damagecause.falling_block|
  |`fireworks`|command.enum.damagecause.fireworks|
  |`thorns`|command.enum.damagecause.thorns|
  |`none`|command.enum.damagecause.none|
  |`sonic_boom`|command.enum.damagecause.sonic_boom|
  |`contact`|command.enum.damagecause.contact|
  |`override`|command.enum.damagecause.override|
  |`entity_attack`|command.enum.damagecause.entity_attack|
  |`projectile`|command.enum.damagecause.projectile|
  |`suffocation`|command.enum.damagecause.suffocation|
  |`fall`|command.enum.damagecause.fall|
  |`starve`|command.enum.damagecause.starve|
  |`ram_attack`|command.enum.damagecause.ram_attack|
  |`fire_tick`|command.enum.damagecause.fire_tick|
  |`stalactite`|command.enum.damagecause.stalactite|
  |`drowning`|command.enum.damagecause.drowning|
  |`block_explosion`|command.enum.damagecause.block_explosion|
  |`entity_explosion`|command.enum.damagecause.entity_explosion|
  |`void`|command.enum.damagecause.void|
  |`self_destruct`|command.enum.damagecause.self_destruct|
  |`magic`|command.enum.damagecause.magic|
  |`charging`|command.enum.damagecause.charging|
  |`stalagmite`|command.enum.damagecause.stalagmite|
  |`fly_into_wall`|command.enum.damagecause.fly_into_wall|
  |`lightning`|command.enum.damagecause.lightning|
  |`freezing`|command.enum.damagecause.freezing|
  |`temperature`|command.enum.damagecause.temperature|



/////

////

///

/// tab | 重载2
```mcfunction
/damage <target:target> <amount:int> <cause:DamageCause> entity <damager:target>
```

//// html | div.result
command.damage.2.description

///// define
`target`：<!-- md:samp target -->

- 基本类型。command.damage.target.description

`amount`：<!-- md:samp int -->

- 基本类型。command.damage.amount.description

`cause`：<!-- md:samp DamageCause -->

- 枚举类型。command.enum.damagecause.description枚举值如下：

  |值|描述|
  |---|---|
  |`piston`|command.enum.damagecause.piston|
  |`lava`|command.enum.damagecause.lava|
  |`campfire`|command.enum.damagecause.campfire|
  |`fire`|command.enum.damagecause.fire|
  |`anvil`|command.enum.damagecause.anvil|
  |`magma`|command.enum.damagecause.magma|
  |`soul_campfire`|command.enum.damagecause.soul_campfire|
  |`wither`|command.enum.damagecause.wither|
  |`falling_block`|command.enum.damagecause.falling_block|
  |`fireworks`|command.enum.damagecause.fireworks|
  |`thorns`|command.enum.damagecause.thorns|
  |`none`|command.enum.damagecause.none|
  |`sonic_boom`|command.enum.damagecause.sonic_boom|
  |`contact`|command.enum.damagecause.contact|
  |`override`|command.enum.damagecause.override|
  |`entity_attack`|command.enum.damagecause.entity_attack|
  |`projectile`|command.enum.damagecause.projectile|
  |`suffocation`|command.enum.damagecause.suffocation|
  |`fall`|command.enum.damagecause.fall|
  |`starve`|command.enum.damagecause.starve|
  |`ram_attack`|command.enum.damagecause.ram_attack|
  |`fire_tick`|command.enum.damagecause.fire_tick|
  |`stalactite`|command.enum.damagecause.stalactite|
  |`drowning`|command.enum.damagecause.drowning|
  |`block_explosion`|command.enum.damagecause.block_explosion|
  |`entity_explosion`|command.enum.damagecause.entity_explosion|
  |`void`|command.enum.damagecause.void|
  |`self_destruct`|command.enum.damagecause.self_destruct|
  |`magic`|command.enum.damagecause.magic|
  |`charging`|command.enum.damagecause.charging|
  |`stalagmite`|command.enum.damagecause.stalagmite|
  |`fly_into_wall`|command.enum.damagecause.fly_into_wall|
  |`lightning`|command.enum.damagecause.lightning|
  |`freezing`|command.enum.damagecause.freezing|
  |`temperature`|command.enum.damagecause.temperature|


`origin`：<!-- md:samp DamageOriginActor -->

- 枚举类型。command.enum.damageoriginactor.description单值枚举，请直接使用`entity`。

`damager`：<!-- md:samp target -->

- 基本类型。command.damage.damager.description


/////

////

///

# /damage

> 文档版本：1.20.80.24

`/damage`命令Apply damage to the specified entities.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/damage <target:target> <amount:int> [cause:DamageCause]
```

//// html | div.result
///// define
`target`: <!-- md:samp target -->

- 基本类型。

`amount`: <!-- md:samp int -->

- 基本类型。

`cause`: <!-- md:samp DamageCause -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`piston`||
|`lava`||
|`campfire`||
|`fire`||
|`anvil`||
|`magma`||
|`soul_campfire`||
|`wither`||
|`falling_block`||
|`fireworks`||
|`thorns`||
|`none`||
|`sonic_boom`||
|`contact`||
|`override`||
|`entity_attack`||
|`projectile`||
|`suffocation`||
|`fall`||
|`starve`||
|`ram_attack`||
|`fire_tick`||
|`stalactite`||
|`drowning`||
|`block_explosion`||
|`entity_explosion`||
|`void`||
|`self_destruct`||
|`magic`||
|`charging`||
|`stalagmite`||
|`fly_into_wall`||
|`lightning`||
|`freezing`||
|`temperature`||



/////

////

///

/// tab | `重载2`
```mcfunction
/damage <target:target> <amount:int> <cause:DamageCause> entity <damager:target>
```

//// html | div.result
///// define
`target`: <!-- md:samp target -->

- 基本类型。

`amount`: <!-- md:samp int -->

- 基本类型。

`cause`: <!-- md:samp DamageCause -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`piston`||
|`lava`||
|`campfire`||
|`fire`||
|`anvil`||
|`magma`||
|`soul_campfire`||
|`wither`||
|`falling_block`||
|`fireworks`||
|`thorns`||
|`none`||
|`sonic_boom`||
|`contact`||
|`override`||
|`entity_attack`||
|`projectile`||
|`suffocation`||
|`fall`||
|`starve`||
|`ram_attack`||
|`fire_tick`||
|`stalactite`||
|`drowning`||
|`block_explosion`||
|`entity_explosion`||
|`void`||
|`self_destruct`||
|`magic`||
|`charging`||
|`stalagmite`||
|`fly_into_wall`||
|`lightning`||
|`freezing`||
|`temperature`||


`origin`: <!-- md:samp DamageOriginActor -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`entity`||


`damager`: <!-- md:samp target -->

- 基本类型。


/////

////

///

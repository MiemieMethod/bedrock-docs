# `/enchant`

> 文档版本：1.20.80.24

`/enchant`命令Adds an enchantment to a player's selected item.

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/enchant <player:target> <enchantmentName:Enchant> [level:int]
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`enchantmentName`: <!-- md:samp Enchant -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`protection`||
|`fire_protection`||
|`feather_falling`||
|`blast_protection`||
|`projectile_protection`||
|`thorns`||
|`respiration`||
|`depth_strider`||
|`aqua_affinity`||
|`sharpness`||
|`smite`||
|`bane_of_arthropods`||
|`knockback`||
|`fire_aspect`||
|`looting`||
|`efficiency`||
|`silk_touch`||
|`unbreaking`||
|`fortune`||
|`power`||
|`punch`||
|`flame`||
|`infinity`||
|`luck_of_the_sea`||
|`lure`||
|`frost_walker`||
|`mending`||
|`binding`||
|`vanishing`||
|`impaling`||
|`riptide`||
|`loyalty`||
|`channeling`||
|`multishot`||
|`piercing`||
|`quick_charge`||
|`soul_speed`||
|`swift_sneak`||


`level`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | 重载2
```mcfunction
/enchant <player:target> <enchantmentId:int> [level:int]
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`enchantmentId`: <!-- md:samp int -->

- 基本类型。

`level`: <!-- md:samp int -->

- 基本类型。


/////

////

///

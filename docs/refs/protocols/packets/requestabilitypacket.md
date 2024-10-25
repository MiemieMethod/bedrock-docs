# <!-- md:samp RequestAbilityPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp RequestAbilityPacket -->数据包，数字ID是`184`。该数据包用于protocol.packet.requestabilitypacket.description

## 结构

```viz
digraph "RequestAbilityPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
6 -> 7
7 -> 8
6 -> 9
9 -> 10
5 -> 11
11 -> 12
12 -> 13
11 -> 14
14 -> 15

0 [label="RequestAbilityPacket",comment="name: \"RequestAbilityPacket\", typeName: \"\", id: 0, branchId: 184, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Ability",comment="name: \"Ability\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Value Type",comment="name: \"Value Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Value Type'",shape=note,comment="name: \"Dependency on 'Value Type'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 6, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="Varible Value",comment="name: \"Varible Value\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="bool",comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Default Value = 0.0",comment="name: \"Default Value = 0.0\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="float",comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 11, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
12 [label="Default Value = false",comment="name: \"Default Value = false\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
13 [label="bool",comment="name: \"bool\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="Varible Value",comment="name: \"Varible Value\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="float",comment="name: \"float\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;8;10;13;15}

}

```

## 字段

```title='RequestAbilityPacket'
[ability][value_type][dependency_on_value_type]
```

/// html | div.result
//// define
Ability：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.requestabilitypacket.ability.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`-1`|protocol.enum.invalid|
  |`Build`|`0`|protocol.enum.build|
  |`Mine`|`1`|protocol.enum.mine|
  |`DoorsAndSwitches`|`2`|protocol.enum.doorsandswitches|
  |`OpenContainers`|`3`|protocol.enum.opencontainers|
  |`AttackPlayers`|`4`|protocol.enum.attackplayers|
  |`AttackMobs`|`5`|protocol.enum.attackmobs|
  |`OperatorCommands`|`6`|protocol.enum.operatorcommands|
  |`Teleport`|`7`|protocol.enum.teleport|
  |`Invulnerable`|`8`|protocol.enum.invulnerable|
  |`Flying`|`9`|protocol.enum.flying|
  |`MayFly`|`10`|protocol.enum.mayfly|
  |`Instabuild`|`11`|protocol.enum.instabuild|
  |`Lightning`|`12`|protocol.enum.lightning|
  |`FlySpeed`|`13`|protocol.enum.flyspeed|
  |`WalkSpeed`|`14`|protocol.enum.walkspeed|
  |`Muted`|`15`|protocol.enum.muted|
  |`WorldBuilder`|`16`|protocol.enum.worldbuilder|
  |`NoClip`|`17`|protocol.enum.noclip|
  |`PrivilegedBuilder`|`18`|protocol.enum.privilegedbuilder|
  |`AbilityCount`|`19`|protocol.enum.abilitycount|



////
//// define
Value Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.requestabilitypacket.value_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unset`|`0`|protocol.enum.unset|
  |`Bool`|`1`|protocol.enum.bool|
  |`Float`|`2`|protocol.enum.float|



////
> 依赖于`Value Type`

///// tab | `Value Type`如果为`1`
```title='if (1)'
[varible_value][default_value_=_0.0]
```

////// html | div.result
/////// define
Varible Value：<!-- md:samp bool -->

- 基本类型。protocol.packet.requestabilitypacket.dependency_on_value_type.if_1.varible_value.description


///////
/////// define
Default Value = 0.0：<!-- md:samp float -->

- 基本类型。protocol.packet.requestabilitypacket.dependency_on_value_type.if_1.default_value_=_0.0.description


///////

//////

/////

///// tab | `Value Type`如果为`2`
```title='if (2)'
[default_value_=_false][varible_value]
```

////// html | div.result
/////// define
Default Value = false：<!-- md:samp bool -->

- 基本类型。protocol.packet.requestabilitypacket.dependency_on_value_type.if_2.default_value_=_false.description


///////
/////// define
Varible Value：<!-- md:samp float -->

- 基本类型。protocol.packet.requestabilitypacket.dependency_on_value_type.if_2.varible_value.description


///////

//////

/////

///


# <!-- md:samp BossEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BossEventPacket -->数据包，数字ID是`74`。该数据包用于protocol.packet.bosseventpacket.description

## 结构

```viz
digraph "BossEventPacket" {
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
6 -> 11
11 -> 12
6 -> 13
13 -> 14
6 -> 15
15 -> 16
5 -> 17
17 -> 18
18 -> 19
5 -> 20
20 -> 21
5 -> 22
22 -> 23
23 -> 24
5 -> 25
25 -> 26
26 -> 27
5 -> 28
28 -> 29
29 -> 30
5 -> 31
31 -> 32
32 -> 33
31 -> 34
34 -> 35
31 -> 36
36 -> 37
5 -> 38
38 -> 39
39 -> 40
38 -> 41
41 -> 42
5 -> 43
43 -> 44
44 -> 45

0 [label="BossEventPacket",comment="name: \"BossEventPacket\", typeName: \"\", id: 0, branchId: 74, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Event Type",comment="name: \"Event Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: BossEventUpdateType\""];
4 [label="int",comment="name: \"int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Event Type'",shape=note,comment="name: \"Dependency on 'Event Type'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="Name",comment="name: \"Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Name of the boss to add\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Health Percent",comment="name: \"Health Percent\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"Health value of the boss\""];
10 [label="float",comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Darken Screen",comment="name: \"Darken Screen\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"A boolean value for whether or not we should darken the screen (has a 0 or 1 value)\""];
12 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Color",comment="name: \"Color\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"color for the boss bar, listed in an enumeration\""];
14 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Overlay",comment="name: \"Overlay\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"overlay for the boss bar, listed in an enumeration\""];
16 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 17, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
18 [label="Player ID",comment="name: \"Player ID\", typeName: \"ActorUniqueID\", id: 18, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
19 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 20, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
21 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 22, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
23 [label="Player ID",comment="name: \"Player ID\", typeName: \"ActorUniqueID\", id: 23, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
24 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 25, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
26 [label="Health Percent",comment="name: \"Health Percent\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
27 [label="float",comment="name: \"float\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="if (5)",shape=diamond,comment="name: \"if (5)\", typeName: \"\", id: 28, branchId: 5, recurseId: -1, attributes: 4, notes: \"\""];
29 [label="Name",comment="name: \"Name\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
30 [label="string",comment="name: \"string\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="if (6)",shape=diamond,comment="name: \"if (6)\", typeName: \"\", id: 31, branchId: 6, recurseId: -1, attributes: 4, notes: \"\""];
32 [label="Darken Screen",comment="name: \"Darken Screen\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
33 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
34 [label="Color",comment="name: \"Color\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
35 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
36 [label="Overlay",comment="name: \"Overlay\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
37 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
38 [label="if (7)",shape=diamond,comment="name: \"if (7)\", typeName: \"\", id: 38, branchId: 7, recurseId: -1, attributes: 4, notes: \"\""];
39 [label="Color",comment="name: \"Color\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
40 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="Overlay",comment="name: \"Overlay\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
42 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
43 [label="if (8)",shape=diamond,comment="name: \"if (8)\", typeName: \"\", id: 43, branchId: 8, recurseId: -1, attributes: 4, notes: \"\""];
44 [label="Player ID",comment="name: \"Player ID\", typeName: \"ActorUniqueID\", id: 44, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
45 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;8;10;12;14;16;19;21;24;27;30;33;35;37;40;42;45}

}

```

## 字段

```title='BossEventPacket'
[target_actor_id][event_type][dependency_on_event_type]
```

/// html | div.result
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.bosseventpacket.target_actor_id.description


////
//// define
Event Type：<!-- md:samp int -->

- 基本类型枚举。protocol.packet.bosseventpacket.event_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Add`|`0`|protocol.enum.add|
  |`PlayerAdded`|`1`|protocol.enum.playeradded|
  |`Remove`|`2`|protocol.enum.remove|
  |`PlayerRemoved`|`3`|protocol.enum.playerremoved|
  |`Update_Percent`|`4`|protocol.enum.update_percent|
  |`Update_Name`|`5`|protocol.enum.update_name|
  |`Update_Properties`|`6`|protocol.enum.update_properties|
  |`Update_Style`|`7`|protocol.enum.update_style|
  |`Query`|`8`|protocol.enum.query|



////
> 依赖于`Event Type`

///// tab | `Event Type`如果为`0`
```title='if (0)'
[name][health_percent][darken_screen][color][overlay]
```

////// html | div.result
/////// define
Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.bosseventpacket.name.descriptionName of the boss to add


///////
/////// define
Health Percent：<!-- md:samp float -->

- 基本类型。protocol.packet.bosseventpacket.health_percent.descriptionHealth value of the boss


///////
/////// define
Darken Screen：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.bosseventpacket.darken_screen.descriptionA boolean value for whether or not we should darken the screen (has a 0 or 1 value)


///////
/////// define
Color：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.bosseventpacket.color.descriptioncolor for the boss bar, listed in an enumeration


///////
/////// define
Overlay：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.bosseventpacket.overlay.descriptionoverlay for the boss bar, listed in an enumeration


///////

//////

/////

///// tab | `Event Type`如果为`1`
```title='if (1)'
[player_id]
```

////// html | div.result
/////// define
Player ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.bosseventpacket.player_id.description


///////

//////

/////

///// tab | `Event Type`如果为`2`
////// define
if (2)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`3`
```title='if (3)'
[player_id]
```

////// html | div.result
/////// define
Player ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.bosseventpacket.player_id.description


///////

//////

/////

///// tab | `Event Type`如果为`4`
```title='if (4)'
[health_percent]
```

////// html | div.result
/////// define
Health Percent：<!-- md:samp float -->

- 基本类型。protocol.packet.bosseventpacket.health_percent.description


///////

//////

/////

///// tab | `Event Type`如果为`5`
```title='if (5)'
[name]
```

////// html | div.result
/////// define
Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.bosseventpacket.name.description


///////

//////

/////

///// tab | `Event Type`如果为`6`
```title='if (6)'
[darken_screen][color][overlay]
```

////// html | div.result
/////// define
Darken Screen：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.bosseventpacket.darken_screen.description


///////
/////// define
Color：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.bosseventpacket.color.description


///////
/////// define
Overlay：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.bosseventpacket.overlay.description


///////

//////

/////

///// tab | `Event Type`如果为`7`
```title='if (7)'
[color][overlay]
```

////// html | div.result
/////// define
Color：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.bosseventpacket.color.description


///////
/////// define
Overlay：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.bosseventpacket.overlay.description


///////

//////

/////

///// tab | `Event Type`如果为`8`
```title='if (8)'
[player_id]
```

////// html | div.result
/////// define
Player ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.bosseventpacket.player_id.description


///////

//////

/////

///


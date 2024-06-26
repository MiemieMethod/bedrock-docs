# <!-- md:samp SetScorePacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp SetScorePacket -->数据包，数字ID是`108`。该数据包用于protocol.packet.setscorepacket.description

## 结构

```viz
digraph "SetScorePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
3 -> 6
6 -> 7
7 -> 11
6 -> 12
12 -> 13
6 -> 14
14 -> 15
6 -> 16
16 -> 17
17 -> 18
16 -> 19
19 -> 20
20 -> 21
21 -> 22
22 -> 23
21 -> 24
24 -> 25
20 -> 26
26 -> 27
27 -> 28
26 -> 29
29 -> 30
20 -> 31
31 -> 32
32 -> 33
31 -> 34
34 -> 35

0 [label="SetScorePacket",comment="name: \"SetScorePacket\", typeName: \"\", id: 0, branchId: 108, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Score Packet Type",comment="name: \"Score Packet Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Score Packet Info",comment="name: \"Score Packet Info\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Id",comment="name: \"Id\", typeName: \"ScoreboardId\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
11 [label="ScoreboardId",comment="name: \"ScoreboardId\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="Objective Name",comment="name: \"Objective Name\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
13 [label="string",comment="name: \"string\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="Score Value",comment="name: \"Score Value\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="int",comment="name: \"int\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="Dependency on 'Is Change Type'",shape=note,comment="name: \"Dependency on 'Is Change Type'\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
17 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
18 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 19, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
20 [label="Dependency on 'Identity Definition Type'",shape=note,comment="name: \"Dependency on 'Identity Definition Type'\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
21 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 21, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
22 [label="Identity Definition Type",comment="name: \"Identity Definition Type\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
23 [label="byte",comment="name: \"byte\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
24 [label="Player Unique Id",comment="name: \"Player Unique Id\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
25 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 26, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
27 [label="Identity Definition Type",comment="name: \"Identity Definition Type\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
28 [label="byte",comment="name: \"byte\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
29 [label="Actor Id",comment="name: \"Actor Id\", typeName: \"ActorUniqueID\", id: 29, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
30 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 31, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
32 [label="Identity Definition Type",comment="name: \"Identity Definition Type\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
33 [label="byte",comment="name: \"byte\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
34 [label="Fake Player Name",comment="name: \"Fake Player Name\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
35 [label="string",comment="name: \"string\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;11;13;15;18;23;25;28;30;33;35}

}

```

## 字段

```title='SetScorePacket'
[score_packet_type][score_packet_info]
```

/// html | div.result
//// define
Score Packet Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.setscorepacket.score_packet_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Change`|`0`|protocol.enum.change|
  |`Remove`|`1`|protocol.enum.remove|



////
```title='Score Packet Info'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.setscorepacket.score_packet_info.array_size.description


/////
```title='示例元素'
[id][objective_name][score_value][dependency_on_is_change_type]
```

///// html | div.result
////// define
Id：[<!-- md:samp ScoreboardId -->](../types/scoreboardid.md)

- 特殊类型。protocol.packet.setscorepacket.score_packet_info.example_element.id.description


//////
////// define
Objective Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.setscorepacket.score_packet_info.example_element.objective_name.description


//////
////// define
Score Value：<!-- md:samp int -->

- 基本类型。protocol.packet.setscorepacket.score_packet_info.example_element.score_value.description


//////
> 依赖于`Is Change Type`

/////// tab | `Is Change Type`如果为`0`
//////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


////////

///////

/////// tab | `Is Change Type`如果为`1`
```title='if (1)'
[dependency_on_identity_definition_type]
```

//////// html | div.result
> 依赖于`Identity Definition Type`

////////// tab | `Identity Definition Type`如果为`1`
```title='if (1)'
[identity_definition_type][player_unique_id]
```

/////////// html | div.result
//////////// define
Identity Definition Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.setscorepacket.score_packet_info.example_element.dependency_on_is_change_type.if_1.dependency_on_identity_definition_type.if_1.identity_definition_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`0`|protocol.enum.invalid|
  |`Player`|`1`|protocol.enum.player|
  |`Entity`|`2`|protocol.enum.entity|
  |`FakePlayer`|`3`|protocol.enum.fakeplayer|



////////////
//////////// define
Player Unique Id：<!-- md:samp varint64 -->

- 基本类型。protocol.packet.setscorepacket.score_packet_info.example_element.dependency_on_is_change_type.if_1.dependency_on_identity_definition_type.if_1.player_unique_id.description


////////////

///////////

//////////

////////// tab | `Identity Definition Type`如果为`2`
```title='if (2)'
[identity_definition_type][actor_id]
```

/////////// html | div.result
//////////// define
Identity Definition Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.setscorepacket.score_packet_info.example_element.dependency_on_is_change_type.if_1.dependency_on_identity_definition_type.if_2.identity_definition_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`0`|protocol.enum.invalid|
  |`Player`|`1`|protocol.enum.player|
  |`Entity`|`2`|protocol.enum.entity|
  |`FakePlayer`|`3`|protocol.enum.fakeplayer|



////////////
//////////// define
Actor Id：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.setscorepacket.score_packet_info.example_element.dependency_on_is_change_type.if_1.dependency_on_identity_definition_type.if_2.actor_id.description


////////////

///////////

//////////

////////// tab | `Identity Definition Type`如果为`3`
```title='if (3)'
[identity_definition_type][fake_player_name]
```

/////////// html | div.result
//////////// define
Identity Definition Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.setscorepacket.score_packet_info.example_element.dependency_on_is_change_type.if_1.dependency_on_identity_definition_type.if_3.identity_definition_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`0`|protocol.enum.invalid|
  |`Player`|`1`|protocol.enum.player|
  |`Entity`|`2`|protocol.enum.entity|
  |`FakePlayer`|`3`|protocol.enum.fakeplayer|



////////////
//////////// define
Fake Player Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.setscorepacket.score_packet_info.example_element.dependency_on_is_change_type.if_1.dependency_on_identity_definition_type.if_3.fake_player_name.description


////////////

///////////

//////////

////////

///////

/////

////

///


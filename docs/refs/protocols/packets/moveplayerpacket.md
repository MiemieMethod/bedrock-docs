# <!-- md:samp MovePlayerPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MovePlayerPacket -->数据包，数字ID是`19`。

## 结构

```viz
digraph "MovePlayerPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10
0 -> 11
11 -> 12
0 -> 13
13 -> 14
0 -> 15
15 -> 16
16 -> 17
15 -> 18
18 -> 19
19 -> 20
18 -> 21
21 -> 22
0 -> 23
23 -> 24

0 [label="MovePlayerPacket",comment="name: \"MovePlayerPacket\", typeName: \"\", id: 0, branchId: 19, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Player Runtime ID",comment="name: \"Player Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Rotation",comment="name: \"Rotation\", typeName: \"Vec2\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="Vec2",comment="name: \"Vec2\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Y-Head Rotation",comment="name: \"Y-Head Rotation\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="float",comment="name: \"float\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Position Mode",comment="name: \"Position Mode\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayerPositionModeComponent::PositionMode\""];
10 [label="byte",comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="On Ground",comment="name: \"On Ground\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="bool",comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Riding Runtime ID",comment="name: \"Riding Runtime ID\", typeName: \"ActorRuntimeID\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
14 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Dependency on 'Position Mode == Teleport'",shape=note,comment="name: \"Dependency on 'Position Mode == Teleport'\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
16 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
17 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 18, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
19 [label="Teleportation Cause",comment="name: \"Teleportation Cause\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="int",comment="name: \"int\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Source Actor Type",comment="name: \"Source Actor Type\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="int",comment="name: \"int\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Tick",comment="name: \"Tick\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"Should be the tick we last processed from PlayerAuthInputPacket or 0 if we're not doing server authoritative movement\""];
24 [label="unsigned varint64",comment="name: \"unsigned varint64\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14;17;20;22;24}

}

```

## 字段

```title='MovePlayerPacket'
[player_runtime_id][position][rotation][y-head_rotation][position_mode][on_ground][riding_runtime_id][dependency_on_position_mode_is_teleport][tick]
```

/// html | div.result
//// define
Player Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。


////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。


////
//// define
Rotation：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 特殊类型。


////
//// define
Y-Head Rotation：<!-- md:samp float -->

- 基本类型。


////
//// define
Position Mode：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Normal`|`0`||
  |`Respawn`|`1`||
  |`Teleport`|`2`||
  |`OnlyHeadRot`|`3`||



////
//// define
On Ground：<!-- md:samp bool -->

- 基本类型。


////
//// define
Riding Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。


////
> 依赖于`Position Mode == Teleport`

///// tab | `Position Mode == Teleport`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Position Mode == Teleport`如果为`1`
```title='if (1)'
[teleportation_cause][source_actor_type]
```

////// html | div.result
/////// define
Teleportation Cause：<!-- md:samp int -->

- 基本类型。


///////
/////// define
Source Actor Type：<!-- md:samp int -->

- 基本类型。


///////

//////

/////
//// define
Tick：<!-- md:samp unsigned varint64 -->

- 基本类型。Should be the tick we last processed from PlayerAuthInputPacket or 0 if we're not doing server authoritative movement


////

///


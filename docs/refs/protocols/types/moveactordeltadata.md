# <!-- md:samp MoveActorDeltaData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MoveActorDeltaData -->类型。

## 结构

```viz
digraph "MoveActorDeltaData" {
rankdir = LR
2
2 -> 3
3 -> 4
2 -> 5
5 -> 6
2 -> 7
7 -> 8
2 -> 9
9 -> 10
2 -> 11
11 -> 12
2 -> 13
13 -> 14
2 -> 15
15 -> 16
2 -> 17
17 -> 18

2 [label="MoveActorDeltaData",comment="name: \"MoveActorDeltaData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"The runtime id of the actor being moved\""];
4 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Header",comment="name: \"Header\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Header containing 9 1-bit booleans describing the rest of the packet. Information provided in supplemental documentation.\""];
6 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="New position X",comment="name: \"New position X\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"If position X bit is true, then this will contain the actor's X coordinate\""];
8 [label="float",comment="name: \"float\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="New position Y",comment="name: \"New position Y\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"If position Y bit is true, then this will contain the actor's Y coordinate\""];
10 [label="float",comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="New position Z",comment="name: \"New position Z\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"If position Z bit is true, then this will contain the actor's Z coordinate\""];
12 [label="float",comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Rotation X",comment="name: \"Rotation X\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"If rotation X bit is true, then this will contain the X rotation of the actor\""];
14 [label="byte",comment="name: \"byte\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Rotation Y",comment="name: \"Rotation Y\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"If rotation Y bit is true, then this will contain the Y rotation of the actor\""];
16 [label="byte",comment="name: \"byte\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Rotation Y Head",comment="name: \"Rotation Y Head\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"If rotation Y Head bit is true, then this will contain a head rotation of the actor if and only if it's a Mob type\""];
18 [label="byte",comment="name: \"byte\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;4;6;8;10;12;14;16;18}

}

```

## 字段

```title='MoveActorDeltaData'
[actorruntimeid][header][new_position_x][new_position_y][new_position_z][rotation_x][rotation_y][rotation_y_head]
```

/// html | div.result
//// define
ActorRuntimeID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。The runtime 'id' of the actor being moved


////
//// define
Header：<!-- md:samp unsigned short -->

- 基本类型。Header containing 9 1-bit booleans describing the rest of the packet. Information prov'id'ed in supplemental documentation.


////
//// define
New position X：<!-- md:samp float -->

- 基本类型。If position X bit is true, then this will contain the actor's X coordinate


////
//// define
New position Y：<!-- md:samp float -->

- 基本类型。If position Y bit is true, then this will contain the actor's Y coordinate


////
//// define
New position Z：<!-- md:samp float -->

- 基本类型。If position Z bit is true, then this will contain the actor's Z coordinate


////
//// define
Rotation X：<!-- md:samp byte -->

- 基本类型。If rotation X bit is true, then this will contain the X rotation of the actor


////
//// define
Rotation Y：<!-- md:samp byte -->

- 基本类型。If rotation Y bit is true, then this will contain the Y rotation of the actor


////
//// define
Rotation Y Head：<!-- md:samp byte -->

- 基本类型。If rotation Y Head bit is true, then this will contain a head rotation of the actor if and only if it's a Mob type


////

///


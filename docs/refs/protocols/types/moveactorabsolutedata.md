# <!-- md:samp MoveActorAbsoluteData -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp MoveActorAbsoluteData -->类型。该类型用于protocol.type.moveactorabsolutedata.description

## 结构

```viz
digraph "MoveActorAbsoluteData" {
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

2 [label="MoveActorAbsoluteData",comment="name: \"MoveActorAbsoluteData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"The runtime id of the actor being moved\""];
4 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Header",comment="name: \"Header\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Header bits describing the status of the actor, see additional documentation in the supplemental documentation folder\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"X/Y/Z coordinates of the position of the actor, each being a 4 byte float\""];
8 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Rotation X",comment="name: \"Rotation X\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"The X rotation of the actor stored as an integer\""];
10 [label="byte",comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Rotation Y",comment="name: \"Rotation Y\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"The Y rotation of the actor stored as an integer\""];
12 [label="byte",comment="name: \"byte\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Rotation Y Head",comment="name: \"Rotation Y Head\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"The head rotation of the actor if and only if it's a Mob type, stored as an integer\""];
14 [label="byte",comment="name: \"byte\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;4;6;8;10;12;14}

}

```

## 字段

```title='MoveActorAbsoluteData'
[actorruntimeid][header][position][rotation_x][rotation_y][rotation_y_head]
```

/// html | div.result
//// define
ActorRuntimeID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.type.moveactorabsolutedata.actorruntimeid.descriptionThe runtime 'id' of the actor being moved


////
//// define
Header：<!-- md:samp byte -->

- 基本类型。protocol.type.moveactorabsolutedata.header.descriptionHeader bits describing the status of the actor, see additional documentation in the supplemental documentation folder


////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.type.moveactorabsolutedata.position.descriptionX/Y/Z coordinates of the position of the actor, each being a 4 byte float


////
//// define
Rotation X：<!-- md:samp byte -->

- 基本类型。protocol.type.moveactorabsolutedata.rotation_x.descriptionThe X rotation of the actor stored as an integer


////
//// define
Rotation Y：<!-- md:samp byte -->

- 基本类型。protocol.type.moveactorabsolutedata.rotation_y.descriptionThe Y rotation of the actor stored as an integer


////
//// define
Rotation Y Head：<!-- md:samp byte -->

- 基本类型。protocol.type.moveactorabsolutedata.rotation_y_head.descriptionThe head rotation of the actor if and only if it's a Mob type, stored as an integer


////

///


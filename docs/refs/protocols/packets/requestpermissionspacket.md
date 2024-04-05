# <!-- md:samp RequestPermissionsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RequestPermissionsPacket -->数据包，数字ID是`185`。

## 结构

```viz
digraph "RequestPermissionsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="RequestPermissionsPacket",comment="name: \"RequestPermissionsPacket\", typeName: \"\", id: 0, branchId: 185, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Player Id's Raw ID",comment="name: \"Target Player Id's Raw ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"mTargetPlayerId is a ActorUniqueID\""];
2 [label="int64",comment="name: \"int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Player Permission Level",comment="name: \"Player Permission Level\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayerPermissionLevel\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Custom Permission Flags",comment="name: \"Custom Permission Flags\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

/// define
RequestPermissionsPacket

Target Player Id's Raw ID：<!-- md:samp int64 -->

- 类型：int64。mTargetPlayerId is a ActorUniqueID

Player Permission Level：<!-- md:samp byte -->

- 类型：byte。enumeration: PlayerPermissionLevel

Custom Permission Flags：<!-- md:samp unsigned short -->

- 类型：unsigned short。


///

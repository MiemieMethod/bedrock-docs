# <!-- md:samp RequestPermissionsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RequestPermissionsPacket -->数据包，数字ID是`185`。该数据包用于protocol.packet.requestpermissionspacket.description

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

```title='RequestPermissionsPacket'
[target_player_ids_raw_id][player_permission_level][custom_permission_flags]
```

/// html | div.result
//// define
Target Player Id's Raw ID：<!-- md:samp int64 -->

- 基本类型。protocol.packet.requestpermissionspacket.target_player_ids_raw_id.descriptionmTargetPlayerId is a ActorUniqueID


////
//// define
Player Permission Level：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.requestpermissionspacket.player_permission_level.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Visitor`|`0`|protocol.enum.visitor|
  |`Member`|`1`|protocol.enum.member|
  |`Operator`|`2`|protocol.enum.operator|
  |`Custom`|`3`|protocol.enum.custom|



////
//// define
Custom Permission Flags：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.requestpermissionspacket.custom_permission_flags.description


////

///


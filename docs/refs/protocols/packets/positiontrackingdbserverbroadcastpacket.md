# <!-- md:samp PositionTrackingDBServerBroadcastPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp PositionTrackingDBServerBroadcastPacket -->数据包，数字ID是`153`。该数据包用于protocol.packet.positiontrackingdbserverbroadcastpacket.description

## 结构

```viz
digraph "PositionTrackingDBServerBroadcastPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 7
0 -> 8
8 -> 9

0 [label="PositionTrackingDBServerBroadcastPacket",comment="name: \"PositionTrackingDBServerBroadcastPacket\", typeName: \"\", id: 0, branchId: 153, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Action",comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Id",comment="name: \"Id\", typeName: \"PositionTrackingId\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
7 [label="PositionTrackingId",comment="name: \"PositionTrackingId\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="Position tracking data",comment="name: \"Position tracking data\", typeName: \"CompoundTag\", id: 8, branchId: 0, recurseId: -1, attributes: 256, notes: \"CompoundTag for record key:version (byte)id (string)positions (list of (int, int, int))dimension (int)status (byte, record status enum)\""];
9 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;7;9}

}

```

## 字段

```title='PositionTrackingDBServerBroadcastPacket'
[action][id][position_tracking_data]
```

/// html | div.result
//// define
Action：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.positiontrackingdbserverbroadcastpacket.action.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Update`|`0`|protocol.enum.update|
  |`Destroy`|`1`|protocol.enum.destroy|
  |`NotFound`|`2`|protocol.enum.notfound|



////
//// define
Id：[<!-- md:samp PositionTrackingId -->](../types/positiontrackingid.md)

- 特殊类型。protocol.packet.positiontrackingdbserverbroadcastpacket.id.description


////
//// define
Position tracking data：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.positiontrackingdbserverbroadcastpacket.position_tracking_data.descriptionCompoundTag for record key:version (byte)'id' (string)positions (list of (int, int, int))dimension (int)status (byte, record status enum)


////

///


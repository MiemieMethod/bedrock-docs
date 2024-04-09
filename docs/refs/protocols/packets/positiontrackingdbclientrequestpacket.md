# <!-- md:samp PositionTrackingDBClientRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PositionTrackingDBClientRequestPacket -->数据包，数字ID是`154`。该数据包用于protocol.packet.positiontrackingdbclientrequestpacket.description

## 结构

```viz
digraph "PositionTrackingDBClientRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="PositionTrackingDBClientRequestPacket",comment="name: \"PositionTrackingDBClientRequestPacket\", typeName: \"\", id: 0, branchId: 154, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Action",comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PositionTrackingDBClientRequestPacket::Action\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Id",comment="name: \"Id\", typeName: \"PositionTrackingId\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="PositionTrackingId",comment="name: \"PositionTrackingId\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='PositionTrackingDBClientRequestPacket'
[action][id]
```

/// html | div.result
//// define
Action：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.positiontrackingdbclientrequestpacket.action.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Query`|`0`|protocol.enum.query|



////
//// define
Id：[<!-- md:samp PositionTrackingId -->](../types/positiontrackingid.md)

- 特殊类型。protocol.packet.positiontrackingdbclientrequestpacket.id.description


////

///


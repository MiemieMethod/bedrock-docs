# <!-- md:samp ServerStatsPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ServerStatsPacket -->数据包，数字ID是`192`。该数据包用于protocol.packet.serverstatspacket.description

## 结构

```viz
digraph "ServerStatsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="ServerStatsPacket",comment="name: \"ServerStatsPacket\", typeName: \"\", id: 0, branchId: 192, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="ServerTime",comment="name: \"ServerTime\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="float",comment="name: \"float\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="NetworkTime",comment="name: \"NetworkTime\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="float",comment="name: \"float\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='ServerStatsPacket'
[servertime][networktime]
```

/// html | div.result
//// define
ServerTime：<!-- md:samp float -->

- 基本类型。protocol.packet.serverstatspacket.servertime.description


////
//// define
NetworkTime：<!-- md:samp float -->

- 基本类型。protocol.packet.serverstatspacket.networktime.description


////

///


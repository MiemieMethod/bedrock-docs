# <!-- md:samp RequestNetworkSettingsPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp RequestNetworkSettingsPacket -->数据包，数字ID是`193`。该数据包用于protocol.packet.requestnetworksettingspacket.description

## 结构

```viz
digraph "RequestNetworkSettingsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="RequestNetworkSettingsPacket",comment="name: \"RequestNetworkSettingsPacket\", typeName: \"\", id: 0, branchId: 193, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="ClientNetworkVersion",comment="name: \"ClientNetworkVersion\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="big endian int",comment="name: \"big endian int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='RequestNetworkSettingsPacket'
[clientnetworkversion]
```

/// html | div.result
//// define
ClientNetworkVersion：<!-- md:samp big endian int -->

- 基本类型。protocol.packet.requestnetworksettingspacket.clientnetworkversion.description


////

///


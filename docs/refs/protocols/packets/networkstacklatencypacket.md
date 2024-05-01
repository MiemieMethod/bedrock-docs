# <!-- md:samp NetworkStackLatencyPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp NetworkStackLatencyPacket -->数据包，数字ID是`115`。该数据包用于protocol.packet.networkstacklatencypacket.description

## 结构

```viz
digraph "NetworkStackLatencyPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="NetworkStackLatencyPacket",comment="name: \"NetworkStackLatencyPacket\", typeName: \"\", id: 0, branchId: 115, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Creation Time",comment="name: \"Creation Time\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Is From Server",comment="name: \"Is From Server\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='NetworkStackLatencyPacket'
[creation_time][is_from_server]
```

/// html | div.result
//// define
Creation Time：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.networkstacklatencypacket.creation_time.description


////
//// define
Is From Server：<!-- md:samp bool -->

- 基本类型。protocol.packet.networkstacklatencypacket.is_from_server.description


////

///


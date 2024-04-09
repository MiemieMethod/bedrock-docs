# <!-- md:samp SetTimePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetTimePacket -->数据包，数字ID是`10`。该数据包用于protocol.packet.settimepacket.description

## 结构

```viz
digraph "SetTimePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetTimePacket",comment="name: \"SetTimePacket\", typeName: \"\", id: 0, branchId: 10, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Time",comment="name: \"Time\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetTimePacket'
[time]
```

/// html | div.result
//// define
Time：<!-- md:samp varint -->

- 基本类型。protocol.packet.settimepacket.time.description


////

///


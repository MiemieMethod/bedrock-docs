# <!-- md:samp TickingAreasLoadStatusPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp TickingAreasLoadStatusPacket -->数据包，数字ID是`179`。该数据包用于protocol.packet.tickingareasloadstatuspacket.description

## 结构

```viz
digraph "TickingAreasLoadStatusPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="TickingAreasLoadStatusPacket",comment="name: \"TickingAreasLoadStatusPacket\", typeName: \"\", id: 0, branchId: 179, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Waiting For Preload",comment="name: \"Waiting For Preload\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="bool",comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='TickingAreasLoadStatusPacket'
[waiting_for_preload]
```

/// html | div.result
//// define
Waiting For Preload：<!-- md:samp bool -->

- 基本类型。protocol.packet.tickingareasloadstatuspacket.waiting_for_preload.description


////

///


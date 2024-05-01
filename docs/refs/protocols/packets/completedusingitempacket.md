# <!-- md:samp CompletedUsingItemPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp CompletedUsingItemPacket -->数据包，数字ID是`142`。该数据包用于protocol.packet.completedusingitempacket.description

## 结构

```viz
digraph "CompletedUsingItemPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="CompletedUsingItemPacket",comment="name: \"CompletedUsingItemPacket\", typeName: \"\", id: 0, branchId: 142, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="short",comment="name: \"short\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Item Use Method",comment="name: \"Item Use Method\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="int",comment="name: \"int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='CompletedUsingItemPacket'
[item_id][item_use_method]
```

/// html | div.result
//// define
Item Id：<!-- md:samp short -->

- 基本类型。protocol.packet.completedusingitempacket.item_id.description


////
//// define
Item Use Method：<!-- md:samp int -->

- 基本类型。protocol.packet.completedusingitempacket.item_use_method.description


////

///


# <!-- md:samp EditorNetworkPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp EditorNetworkPacket -->数据包，数字ID是`190`。该数据包用于protocol.packet.editornetworkpacket.description

## 结构

```viz
digraph "EditorNetworkPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="EditorNetworkPacket",comment="name: \"EditorNetworkPacket\", typeName: \"\", id: 0, branchId: 190, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Binary Payload",comment="name: \"Binary Payload\", typeName: \"CompoundTag\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='EditorNetworkPacket'
[binary_payload]
```

/// html | div.result
//// define
Binary Payload：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.editornetworkpacket.binary_payload.description


////

///


# <!-- md:samp EditorNetworkPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp EditorNetworkPacket -->数据包，数字ID是`190`。该数据包用于protocol.packet.editornetworkpacket.description

## 结构

```viz
digraph "EditorNetworkPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="EditorNetworkPacket",comment="name: \"EditorNetworkPacket\", typeName: \"\", id: 0, branchId: 190, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Route To Manager",comment="name: \"Route To Manager\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="bool",comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Binary Payload",comment="name: \"Binary Payload\", typeName: \"CompoundTag\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='EditorNetworkPacket'
[route_to_manager][binary_payload]
```

/// html | div.result
//// define
Route To Manager：<!-- md:samp bool -->

- 基本类型。protocol.packet.editornetworkpacket.route_to_manager.description


////
//// define
Binary Payload：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.editornetworkpacket.binary_payload.description


////

///


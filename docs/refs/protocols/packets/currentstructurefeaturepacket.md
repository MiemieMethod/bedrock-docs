# <!-- md:samp CurrentStructureFeaturePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp CurrentStructureFeaturePacket -->数据包，数字ID是`314`。该数据包用于protocol.packet.currentstructurefeaturepacket.description

## 结构

```viz
digraph "CurrentStructureFeaturePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="CurrentStructureFeaturePacket",comment="name: \"CurrentStructureFeaturePacket\", typeName: \"\", id: 0, branchId: 314, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Current Structure Feature",comment="name: \"Current Structure Feature\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"The identifier of the Structure Feature that the player is currently occupying. If the player is not occupying a structure then this value is an empty string.\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='CurrentStructureFeaturePacket'
[current_structure_feature]
```

/// html | div.result
//// define
Current Structure Feature：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.currentstructurefeaturepacket.current_structure_feature.descriptionThe 'id'entifier of the Structure Feature that the player is currently occupying. If the player is not occupying a structure then this value is an empty string.


////

///


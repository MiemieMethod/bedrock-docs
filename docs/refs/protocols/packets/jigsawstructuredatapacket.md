# <!-- md:samp JigsawStructureDataPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp JigsawStructureDataPacket -->数据包，数字ID是`313`。该数据包用于protocol.packet.jigsawstructuredatapacket.description

## 结构

```viz
digraph "JigsawStructureDataPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="JigsawStructureDataPacket",comment="name: \"JigsawStructureDataPacket\", typeName: \"\", id: 0, branchId: 313, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Jigsaw Structure Data Tag",comment="name: \"Jigsaw Structure Data Tag\", typeName: \"CompoundTag\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='JigsawStructureDataPacket'
[jigsaw_structure_data_tag]
```

/// html | div.result
//// define
Jigsaw Structure Data Tag：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.jigsawstructuredatapacket.jigsaw_structure_data_tag.description


////

///


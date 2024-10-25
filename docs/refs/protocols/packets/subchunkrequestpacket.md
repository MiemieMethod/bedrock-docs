# <!-- md:samp SubChunkRequestPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp SubChunkRequestPacket -->数据包，数字ID是`175`。该数据包用于protocol.packet.subchunkrequestpacket.description

## 结构

```viz
digraph "SubChunkRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
8 -> 9
9 -> 10

0 [label="SubChunkRequestPacket",comment="name: \"SubChunkRequestPacket\", typeName: \"\", id: 0, branchId: 175, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Dimension Type",comment="name: \"Dimension Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Center Pos",comment="name: \"Center Pos\", typeName: \"SubChunkPos\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="SubChunkPos",comment="name: \"SubChunkPos\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Request Count",comment="name: \"Request Count\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="SubChunk Pos Offset List",comment="name: \"SubChunk Pos Offset List\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
8 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
9 [label="SubChunk Offset Pos",comment="name: \"SubChunk Offset Pos\", typeName: \"SubChunkPacket::SubChunkPosOffset\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="SubChunkPacket::SubChunkPosOffset",comment="name: \"SubChunkPacket::SubChunkPosOffset\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;10}

}

```

## 字段

```title='SubChunkRequestPacket'
[dimension_type][center_pos][request_count][subchunk_pos_offset_list]
```

/// html | div.result
//// define
Dimension Type：<!-- md:samp varint -->

- 基本类型。protocol.packet.subchunkrequestpacket.dimension_type.description


////
//// define
Center Pos：[<!-- md:samp SubChunkPos -->](../types/subchunkpos.md)

- 特殊类型。protocol.packet.subchunkrequestpacket.center_pos.description


////
//// define
Request Count：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.subchunkrequestpacket.request_count.description


////
```title='SubChunk Pos Offset List'
[[example_element]..]
```

//// html | div.result
```title='示例元素'
[subchunk_offset_pos]
```

///// html | div.result
////// define
SubChunk Offset Pos：[<!-- md:samp SubChunkPacket::SubChunkPosOffset -->](../types/subchunkpacket__subchunkposoffset.md)

- 特殊类型。protocol.packet.subchunkrequestpacket.subchunk_pos_offset_list.example_element.subchunk_offset_pos.description


//////

/////

////

///


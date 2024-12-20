# <!-- md:samp NetworkChunkPublisherUpdatePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp NetworkChunkPublisherUpdatePacket -->数据包，数字ID是`121`。该数据包用于protocol.packet.networkchunkpublisherupdatepacket.description

## 结构

```viz
digraph "NetworkChunkPublisherUpdatePacket" {
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
7 -> 10
10 -> 11
11 -> 12

0 [label="NetworkChunkPublisherUpdatePacket",comment="name: \"NetworkChunkPublisherUpdatePacket\", typeName: \"\", id: 0, branchId: 121, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="New position for view",comment="name: \"New position for view\", typeName: \"BlockPos\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="New radius for view",comment="name: \"New radius for view\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Server Built Chunks Size",comment="name: \"Server Built Chunks Size\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Server Built Chunks List",comment="name: \"Server Built Chunks List\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
8 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
11 [label="Chunk Pos",comment="name: \"Chunk Pos\", typeName: \"ChunkPos\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
12 [label="ChunkPos",comment="name: \"ChunkPos\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;9;12}

}

```

## 字段

```title='NetworkChunkPublisherUpdatePacket'
[new_position_for_view][new_radius_for_view][server_built_chunks_size][server_built_chunks_list]
```

/// html | div.result
//// define
New position for view：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.packet.networkchunkpublisherupdatepacket.new_position_for_view.description


////
//// define
New radius for view：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.networkchunkpublisherupdatepacket.new_radius_for_view.description


////
//// define
Server Built Chunks Size：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.networkchunkpublisherupdatepacket.server_built_chunks_size.description


////
```title='Server Built Chunks List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.networkchunkpublisherupdatepacket.server_built_chunks_list.array_size.description


/////
```title='示例元素'
[chunk_pos]
```

///// html | div.result
////// define
Chunk Pos：[<!-- md:samp ChunkPos -->](../types/chunkpos.md)

- 特殊类型。protocol.packet.networkchunkpublisherupdatepacket.server_built_chunks_list.example_element.chunk_pos.description


//////

/////

////

///


# <!-- md:samp ClientCacheMissResponsePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ClientCacheMissResponsePacket -->数据包，数字ID是`136`。该数据包用于protocol.packet.clientcachemissresponsepacket.description

## 结构

```viz
digraph "ClientCacheMissResponsePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6
4 -> 7
7 -> 8

0 [label="ClientCacheMissResponsePacket",comment="name: \"ClientCacheMissResponsePacket\", typeName: \"\", id: 0, branchId: 136, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Missing Blobs",comment="name: \"Missing Blobs\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Number of missing blobs",comment="name: \"Number of missing blobs\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Blob Id",comment="name: \"Blob Id\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Blob Data",comment="name: \"Blob Data\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Subchunk data (see https://gist.github.com/Tomcc/a96af509e275b1af483b25c543cfbf37) plus biome data\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6;8}

}

```

## 字段

```title='ClientCacheMissResponsePacket'
[missing_blobs]
```

/// html | div.result
```title='Missing Blobs'
[number_of_missing_blobs][[example_element]..]
```

//// html | div.result
///// define
Number of missing blobs：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.clientcachemissresponsepacket.number_of_missing_blobs.description


/////
```title='示例元素'
[blob_id][blob_data]
```

///// html | div.result
////// define
Blob Id：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.clientcachemissresponsepacket.blob_id.description


//////
////// define
Blob Data：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.clientcachemissresponsepacket.blob_data.descriptionSubchunk data (see https://gist.github.com/Tomcc/a96af509e275b1af483b25c543cfbf37) plus biome data


//////

/////

////

///


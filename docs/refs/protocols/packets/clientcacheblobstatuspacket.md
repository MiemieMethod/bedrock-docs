# <!-- md:samp ClientCacheBlobStatusPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ClientCacheBlobStatusPacket -->数据包，数字ID是`135`。该数据包用于protocol.packet.clientcacheblobstatuspacket.description

## 结构

```viz
digraph "ClientCacheBlobStatusPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
6 -> 7
7 -> 8
0 -> 9
9 -> 10
10 -> 11
11 -> 12

0 [label="ClientCacheBlobStatusPacket",comment="name: \"ClientCacheBlobStatusPacket\", typeName: \"\", id: 0, branchId: 135, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Number of missing blobs",comment="name: \"Number of missing blobs\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Number of obtained blobs",comment="name: \"Number of obtained blobs\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Missing Blobs",comment="name: \"Missing Blobs\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Blob Id",comment="name: \"Blob Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Obtained Blobs",comment="name: \"Obtained Blobs\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
10 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
11 [label="Blob Id",comment="name: \"Blob Id\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;8;12}

}

```

## 字段

```title='ClientCacheBlobStatusPacket'
[number_of_missing_blobs][number_of_obtained_blobs][missing_blobs][obtained_blobs]
```

/// html | div.result
//// define
Number of missing blobs：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.clientcacheblobstatuspacket.number_of_missing_blobs.description


////
//// define
Number of obtained blobs：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.clientcacheblobstatuspacket.number_of_obtained_blobs.description


////
```title='Missing Blobs'
[[example_element]..]
```

//// html | div.result
```title='示例元素'
[blob_id]
```

///// html | div.result
////// define
Blob Id：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.clientcacheblobstatuspacket.missing_blobs.example_element.blob_id.description


//////

/////

////
```title='Obtained Blobs'
[[example_element]..]
```

//// html | div.result
```title='示例元素'
[blob_id]
```

///// html | div.result
////// define
Blob Id：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.clientcacheblobstatuspacket.obtained_blobs.example_element.blob_id.description


//////

/////

////

///


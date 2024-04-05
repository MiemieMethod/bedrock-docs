# <!-- md:samp CreatePhotoPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CreatePhotoPacket -->数据包，数字ID是`171`。

## 结构

```viz
digraph "CreatePhotoPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="CreatePhotoPacket",comment="name: \"CreatePhotoPacket\", typeName: \"\", id: 0, branchId: 171, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Raw ID",comment="name: \"Raw ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Photo Name",comment="name: \"Photo Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Photo Item Name",comment="name: \"Photo Item Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='CreatePhotoPacket'
[raw_id][photo_name][photo_item_name]
```

/// html | div.result
//// define
Raw ID：<!-- md:samp unsigned int64 -->

- 类型：<!-- md:samp unsigned int64 -->。


////
//// define
Photo Name：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Photo Item Name：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////

///


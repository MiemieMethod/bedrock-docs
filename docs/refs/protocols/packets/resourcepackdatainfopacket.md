# <!-- md:samp ResourcePackDataInfoPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ResourcePackDataInfoPacket -->数据包，数字ID是`82`。

## 结构

```viz
digraph "ResourcePackDataInfoPacket" {
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
0 -> 9
9 -> 10
0 -> 11
11 -> 12
0 -> 13
13 -> 14

0 [label="ResourcePackDataInfoPacket",comment="name: \"ResourcePackDataInfoPacket\", typeName: \"\", id: 0, branchId: 82, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Resource Name",comment="name: \"Resource Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Chunk Size",comment="name: \"Chunk Size\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Number of Chunks",comment="name: \"Number of Chunks\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="File Size",comment="name: \"File Size\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="File Hash",comment="name: \"File Hash\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Is Premium Pack",comment="name: \"Is Premium Pack\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"Do you need an entitlement to use this pack?\""];
12 [label="bool",comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Pack Type",comment="name: \"Pack Type\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PackType\""];
14 [label="byte",comment="name: \"byte\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14}

}

```

## 字段

```title='ResourcePackDataInfoPacket'
[resource_name][chunk_size][number_of_chunks][file_size][file_hash][is_premium_pack][pack_type]
```

/// html | div.result
//// define
Resource Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////
//// define
Chunk Size：<!-- md:samp unsigned int -->

- 基本类型。


////
//// define
Number of Chunks：<!-- md:samp unsigned int -->

- 基本类型。


////
//// define
File Size：<!-- md:samp unsigned int64 -->

- 基本类型。


////
//// define
File Hash：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////
//// define
Is Premium Pack：<!-- md:samp bool -->

- 基本类型。Do you need an entitlement to use this pack?


////
//// define
Pack Type：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`0`||
  |`Addon`|`1`||
  |`Cached`|`2`||
  |`CopyProtected`|`3`||
  |`Behavior`|`4`||
  |`PersonaPiece`|`5`||
  |`Resources`|`6`||
  |`Skins`|`7`||
  |`WorldTemplate`|`8`||
  |`Count`|`9`||



////

///


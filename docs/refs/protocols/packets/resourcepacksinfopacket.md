# <!-- md:samp ResourcePacksInfoPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ResourcePacksInfoPacket -->数据包，数字ID是`6`。该数据包用于protocol.packet.resourcepacksinfopacket.description

## 结构

```viz
digraph "ResourcePacksInfoPacket" {
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
10 -> 11
9 -> 12
12 -> 13
13 -> 14
12 -> 15
15 -> 16
12 -> 17
17 -> 18
12 -> 19
19 -> 20
12 -> 21
21 -> 22
12 -> 23
23 -> 24
12 -> 25
25 -> 26
0 -> 27
27 -> 28
28 -> 29
27 -> 30
30 -> 31
31 -> 32
30 -> 33
33 -> 34
30 -> 35
35 -> 36
30 -> 37
37 -> 38
30 -> 39
39 -> 40
30 -> 41
41 -> 42
30 -> 43
43 -> 44
30 -> 45
45 -> 46
0 -> 47
47 -> 48
48 -> 49
47 -> 50
50 -> 51
51 -> 52
50 -> 53
53 -> 54

0 [label="ResourcePacksInfoPacket",comment="name: \"ResourcePacksInfoPacket\", typeName: \"\", id: 0, branchId: 6, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Resource Pack Required",comment="name: \"Resource Pack Required\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="bool",comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Has Add-on Packs",comment="name: \"Has Add-on Packs\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Has Scripts",comment="name: \"Has Scripts\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Force Server Packs Enabled",comment="name: \"Force Server Packs Enabled\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="bool",comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Behavior Packs",comment="name: \"Behavior Packs\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
10 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
13 [label="ID",comment="name: \"ID\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Version",comment="name: \"Version\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="string",comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Size",comment="name: \"Size\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Content Key",comment="name: \"Content Key\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="string",comment="name: \"string\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Sub Pack Name",comment="name: \"Sub Pack Name\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="string",comment="name: \"string\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Content Identity",comment="name: \"Content Identity\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="string",comment="name: \"string\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Has Scripts",comment="name: \"Has Scripts\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="bool",comment="name: \"bool\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="Resource Packs",comment="name: \"Resource Packs\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
28 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
29 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
31 [label="ID",comment="name: \"ID\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="string",comment="name: \"string\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Version",comment="name: \"Version\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="string",comment="name: \"string\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="Size",comment="name: \"Size\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
36 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="Content Key",comment="name: \"Content Key\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
38 [label="string",comment="name: \"string\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
39 [label="Sub Pack Name",comment="name: \"Sub Pack Name\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
40 [label="string",comment="name: \"string\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="Content Identity",comment="name: \"Content Identity\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
42 [label="string",comment="name: \"string\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
43 [label="Has Scripts",comment="name: \"Has Scripts\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
44 [label="bool",comment="name: \"bool\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
45 [label="Is Ray Tracing Capable",comment="name: \"Is Ray Tracing Capable\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
46 [label="bool",comment="name: \"bool\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
47 [label="CDN URLs",comment="name: \"CDN URLs\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
48 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
49 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
50 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
51 [label="First",comment="name: \"First\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
52 [label="string",comment="name: \"string\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
53 [label="Second",comment="name: \"Second\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
54 [label="string",comment="name: \"string\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;11;14;16;18;20;22;24;26;29;32;34;36;38;40;42;44;46;49;52;54}

}

```

## 字段

```title='ResourcePacksInfoPacket'
[resource_pack_required][has_add-on_packs][has_scripts][force_server_packs_enabled][behavior_packs][resource_packs][cdn_urls]
```

/// html | div.result
//// define
Resource Pack Required：<!-- md:samp bool -->

- 基本类型。protocol.packet.resourcepacksinfopacket.resource_pack_required.description


////
//// define
Has Add-on Packs：<!-- md:samp bool -->

- 基本类型。protocol.packet.resourcepacksinfopacket.has_add-on_packs.description


////
//// define
Has Scripts：<!-- md:samp bool -->

- 基本类型。protocol.packet.resourcepacksinfopacket.has_scripts.description


////
//// define
Force Server Packs Enabled：<!-- md:samp bool -->

- 基本类型。protocol.packet.resourcepacksinfopacket.force_server_packs_enabled.description


////
```title='Behavior Packs'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.resourcepacksinfopacket.behavior_packs.array_size.description


/////
```title='示例元素'
[id][version][size][content_key][sub_pack_name][content_identity][has_scripts]
```

///// html | div.result
////// define
ID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.behavior_packs.example_element.id.description


//////
////// define
Version：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.behavior_packs.example_element.version.description


//////
////// define
Size：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.resourcepacksinfopacket.behavior_packs.example_element.size.description


//////
////// define
Content Key：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.behavior_packs.example_element.content_key.description


//////
////// define
Sub Pack Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.behavior_packs.example_element.sub_pack_name.description


//////
////// define
Content Identity：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.behavior_packs.example_element.content_identity.description


//////
////// define
Has Scripts：<!-- md:samp bool -->

- 基本类型。protocol.packet.resourcepacksinfopacket.behavior_packs.example_element.has_scripts.description


//////

/////

////
```title='Resource Packs'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.resourcepacksinfopacket.resource_packs.array_size.description


/////
```title='示例元素'
[id][version][size][content_key][sub_pack_name][content_identity][has_scripts][is_ray_tracing_capable]
```

///// html | div.result
////// define
ID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.id.description


//////
////// define
Version：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.version.description


//////
////// define
Size：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.size.description


//////
////// define
Content Key：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.content_key.description


//////
////// define
Sub Pack Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.sub_pack_name.description


//////
////// define
Content Identity：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.content_identity.description


//////
////// define
Has Scripts：<!-- md:samp bool -->

- 基本类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.has_scripts.description


//////
////// define
Is Ray Tracing Capable：<!-- md:samp bool -->

- 基本类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.is_ray_tracing_capable.description


//////

/////

////
```title='CDN URLs'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.resourcepacksinfopacket.cdn_urls.array_size.description


/////
```title='示例元素'
[first][second]
```

///// html | div.result
////// define
First：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.cdn_urls.example_element.first.description


//////
////// define
Second：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.cdn_urls.example_element.second.description


//////

/////

////

///


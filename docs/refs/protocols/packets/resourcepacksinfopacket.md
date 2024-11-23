# <!-- md:samp ResourcePacksInfoPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

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
8 -> 9
7 -> 10
10 -> 11
11 -> 12
10 -> 13
13 -> 14
10 -> 15
15 -> 16
10 -> 17
17 -> 18
10 -> 19
19 -> 20
10 -> 21
21 -> 22
10 -> 23
23 -> 24
10 -> 25
25 -> 26
10 -> 27
27 -> 28
10 -> 29
29 -> 30

0 [label="ResourcePacksInfoPacket",comment="name: \"ResourcePacksInfoPacket\", typeName: \"\", id: 0, branchId: 6, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Resource Pack Required",comment="name: \"Resource Pack Required\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="bool",comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Has Add-on Packs",comment="name: \"Has Add-on Packs\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Has Scripts",comment="name: \"Has Scripts\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Resource Packs",comment="name: \"Resource Packs\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
8 [label="Resource Pack Count",comment="name: \"Resource Pack Count\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
11 [label="ID",comment="name: \"ID\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="string",comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Version",comment="name: \"Version\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Size",comment="name: \"Size\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Content Key",comment="name: \"Content Key\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="string",comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Sub Pack Name",comment="name: \"Sub Pack Name\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="string",comment="name: \"string\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Content Identity",comment="name: \"Content Identity\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="string",comment="name: \"string\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Has Scripts",comment="name: \"Has Scripts\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="bool",comment="name: \"bool\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Is Addon Pack",comment="name: \"Is Addon Pack\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"Indicates this pack is part of an Add-On. Helps clients determine if the pack must be downloaded to join the server as Add-On packs are required to play without issues.\""];
26 [label="bool",comment="name: \"bool\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="Is Ray Tracing Capable",comment="name: \"Is Ray Tracing Capable\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
28 [label="bool",comment="name: \"bool\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
29 [label="CDN URL",comment="name: \"CDN URL\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
30 [label="string",comment="name: \"string\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;9;12;14;16;18;20;22;24;26;28;30}

}

```

## 字段

```title='ResourcePacksInfoPacket'
[resource_pack_required][has_add-on_packs][has_scripts][resource_packs]
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
```title='Resource Packs'
[resource_pack_count][[example_element]..]
```

//// html | div.result
///// define
Resource Pack Count：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.resourcepacksinfopacket.resource_packs.resource_pack_count.description


/////
```title='示例元素'
[id][version][size][content_key][sub_pack_name][content_identity][has_scripts][is_addon_pack][is_ray_tracing_capable][cdn_url]
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
Is Addon Pack：<!-- md:samp bool -->

- 基本类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.is_addon_pack.descriptionIndicates this pack is part of an Add-On. Helps clients determine if the pack must be downloaded to join the server as Add-On packs are required to play without issues.


//////
////// define
Is Ray Tracing Capable：<!-- md:samp bool -->

- 基本类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.is_ray_tracing_capable.description


//////
////// define
CDN URL：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepacksinfopacket.resource_packs.example_element.cdn_url.description


//////

/////

////

///


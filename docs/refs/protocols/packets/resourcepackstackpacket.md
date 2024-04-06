# <!-- md:samp ResourcePackStackPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ResourcePackStackPacket -->数据包，数字ID是`7`。

## 结构

```viz
digraph "ResourcePackStackPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
3 -> 6
6 -> 7
7 -> 8
6 -> 9
9 -> 10
6 -> 11
11 -> 12
0 -> 13
13 -> 14
14 -> 15
13 -> 16
16 -> 17
17 -> 18
16 -> 19
19 -> 20
16 -> 21
21 -> 22
0 -> 23
23 -> 27
0 -> 28
28 -> 44

0 [label="ResourcePackStackPacket",comment="name: \"ResourcePackStackPacket\", typeName: \"\", id: 0, branchId: 7, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Texture Pack Required",comment="name: \"Texture Pack Required\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="bool",comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Add-On List",comment="name: \"Add-On List\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="ID",comment="name: \"ID\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Version",comment="name: \"Version\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Sub Pack Name",comment="name: \"Sub Pack Name\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="string",comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Texture Pack List",comment="name: \"Texture Pack List\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
14 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
17 [label="ID",comment="name: \"ID\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="string",comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Version",comment="name: \"Version\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="string",comment="name: \"string\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Sub Pack Name",comment="name: \"Sub Pack Name\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="string",comment="name: \"string\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Base Game Version",comment="name: \"Base Game Version\", typeName: \"BaseGameVersion\", id: 23, branchId: 0, recurseId: -1, attributes: 256, notes: \"For clients to be able to set their stack to the right version.\""];
27 [label="BaseGameVersion",comment="name: \"BaseGameVersion\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="Experiments",comment="name: \"Experiments\", typeName: \"Experiments\", id: 28, branchId: 0, recurseId: -1, attributes: 256, notes: \"Refer to the Experiments type for how to serialize\""];
44 [label="Experiments",comment="name: \"Experiments\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8;10;12;15;18;20;22;27;44}

}

```

## 字段

```title='ResourcePackStackPacket'
[texture_pack_required][add-on_list][texture_pack_list][base_game_version][experiments]
```

/// html | div.result
//// define
Texture Pack Required：<!-- md:samp bool -->

- <!-- md:samp bool -->类型。


////
```title='Add-On List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型。


/////
```title='示例元素'
[id][version][sub_pack_name]
```

///// html | div.result
////// define
ID：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


//////
////// define
Version：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


//////
////// define
Sub Pack Name：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


//////

/////

////
```title='Texture Pack List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型。


/////
```title='示例元素'
[id][version][sub_pack_name]
```

///// html | div.result
////// define
ID：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


//////
////// define
Version：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


//////
////// define
Sub Pack Name：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


//////

/////

////
//// define
Base Game Version：[<!-- md:samp BaseGameVersion -->](../types/basegameversion.md)

- <!-- md:samp BaseGameVersion -->类型。For clients to be able to set their stack to the right version.


////
//// define
Experiments：[<!-- md:samp Experiments -->](../types/experiments.md)

- <!-- md:samp Experiments -->类型。Refer to the Experiments type for how to serialize


////

///


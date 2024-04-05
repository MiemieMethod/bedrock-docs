# <!-- md:samp ItemInstanceUserData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemInstanceUserData -->类型。

## 结构

```viz
digraph "ItemInstanceUserData" {
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
0 -> 13
13 -> 14
14 -> 15
13 -> 16
16 -> 17
17 -> 18

0 [label="ItemInstanceUserData",comment="name: \"ItemInstanceUserData\", typeName: \"\", id: 0, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="User Data Serialization Marker",comment="name: \"User Data Serialization Marker\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"(-1) marking start of data\""];
2 [label="short",comment="name: \"short\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="User Data Serialization Version",comment="name: \"User Data Serialization Version\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently 1\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="User Data Tag(s)",comment="name: \"User Data Tag(s)\", typeName: \"CompoundTag\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"See: @CompoundTag.html#Compound Tag@ .\""];
6 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Can Place On Blocks",comment="name: \"Can Place On Blocks\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"Blocks that this item can be placed on.\""];
8 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
11 [label="Block Raw Name ID",comment="name: \"Block Raw Name ID\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="string",comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Can Destroy Blocks",comment="name: \"Can Destroy Blocks\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"Blocks that this item can destroy.\""];
14 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
17 [label="Block Raw Name ID",comment="name: \"Block Raw Name ID\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="string",comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;9;12;15;18}

}

```

## 字段

/// define
ItemInstanceUserData

User Data Serialization Marker：<!-- md:samp short -->

- 类型：short。(-1) marking start of data

User Data Serialization Version：<!-- md:samp byte -->

- 类型：byte。Currently 1

User Data Tag(s)：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 类型：CompoundTag。See: @CompoundTag.html#Compound Tag@ .

Can Place On Blocks

//// define
Can Place On Blocks数组的大小：<!-- md:samp unsigned int -->

- 类型：unsigned int。


////


//// define
Can Place On Blocks的示例元素

Block Raw Name ID：<!-- md:samp string -->

- 类型：string。


////


Can Destroy Blocks

//// define
Can Destroy Blocks数组的大小：<!-- md:samp unsigned int -->

- 类型：unsigned int。


////


//// define
Can Destroy Blocks的示例元素

Block Raw Name ID：<!-- md:samp string -->

- 类型：string。


////



///

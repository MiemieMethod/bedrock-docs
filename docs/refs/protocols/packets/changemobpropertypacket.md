# <!-- md:samp ChangeMobPropertyPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ChangeMobPropertyPacket -->数据包，数字ID是`182`。

## 结构

```viz
digraph "ChangeMobPropertyPacket" {
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

0 [label="ChangeMobPropertyPacket",comment="name: \"ChangeMobPropertyPacket\", typeName: \"\", id: 0, branchId: 182, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Actor Id",comment="name: \"Actor Id\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Property Name",comment="name: \"Property Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="BoolComponent Value",comment="name: \"BoolComponent Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="StringComponent Value",comment="name: \"StringComponent Value\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="IntComponent Value",comment="name: \"IntComponent Value\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="varint",comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="FloatComponent Value",comment="name: \"FloatComponent Value\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="float",comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12}

}

```

## 字段

```title='ChangeMobPropertyPacket'
[actor_id][property_name][boolcomponent_value][stringcomponent_value][intcomponent_value][floatcomponent_value]
```

/// html | div.result
//// define
Actor Id：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。


////
//// define
Property Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////
//// define
BoolComponent Value：<!-- md:samp bool -->

- 基本类型。


////
//// define
StringComponent Value：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////
//// define
IntComponent Value：<!-- md:samp varint -->

- 基本类型。


////
//// define
FloatComponent Value：<!-- md:samp float -->

- 基本类型。


////

///


# <!-- md:samp UpdateAttributesPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateAttributesPacket -->数据包，数字ID是`29`。

## 结构

```viz
digraph "UpdateAttributesPacket" {
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
6 -> 13
13 -> 14
6 -> 15
15 -> 16
6 -> 17
17 -> 18
18 -> 19
17 -> 20
20 -> 21
21 -> 22
20 -> 23
23 -> 24
20 -> 25
25 -> 26
20 -> 27
27 -> 28
20 -> 29
29 -> 30
20 -> 31
31 -> 32
0 -> 33
33 -> 34

0 [label="UpdateAttributesPacket",comment="name: \"UpdateAttributesPacket\", typeName: \"\", id: 0, branchId: 29, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Attribute List",comment="name: \"Attribute List\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"AttributeData - Helper Struct\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Min Value",comment="name: \"Min Value\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="float",comment="name: \"float\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Max Value",comment="name: \"Max Value\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="float",comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Current Value",comment="name: \"Current Value\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="float",comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Default Value",comment="name: \"Default Value\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="float",comment="name: \"float\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Attribute Name",comment="name: \"Attribute Name\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="string",comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Attribute Modifier",comment="name: \"Attribute Modifier\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
18 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
19 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
21 [label="ID",comment="name: \"ID\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="string",comment="name: \"string\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Name",comment="name: \"Name\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="string",comment="name: \"string\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Amount",comment="name: \"Amount\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="float",comment="name: \"float\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="Operation",comment="name: \"Operation\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: AttributeModifierOperation\""];
28 [label="int",comment="name: \"int\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
29 [label="Operand",comment="name: \"Operand\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: AttributeOperands\""];
30 [label="int",comment="name: \"int\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="isSerializable?",comment="name: \"isSerializable?\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="bool",comment="name: \"bool\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Count of ticks since simulation started",comment="name: \"Count of ticks since simulation started\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="unsigned varint64",comment="name: \"unsigned varint64\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8;10;12;14;16;19;22;24;26;28;30;32;34}

}

```

## 字段

```title='UpdateAttributesPacket'
[target_runtime_id][attribute_list][count_of_ticks_since_simulation_started]
```

/// html | div.result
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- <!-- md:samp ActorRuntimeID -->类型。


////
```title='Attribute List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型。


/////
```title='示例元素'
[min_value][max_value][current_value][default_value][attribute_name][attribute_modifier]
```

///// html | div.result
////// define
Min Value：<!-- md:samp float -->

- <!-- md:samp float -->类型。


//////
////// define
Max Value：<!-- md:samp float -->

- <!-- md:samp float -->类型。


//////
////// define
Current Value：<!-- md:samp float -->

- <!-- md:samp float -->类型。


//////
////// define
Default Value：<!-- md:samp float -->

- <!-- md:samp float -->类型。


//////
////// define
Attribute Name：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


//////
```title='Attribute Modifier'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型。


///////
```title='示例元素'
[id][name][amount][operation][operand][isserializable?]
```

/////// html | div.result
//////// define
ID：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////////
//////// define
Name：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////////
//////// define
Amount：<!-- md:samp float -->

- <!-- md:samp float -->类型。


////////
//////// define
Operation：<!-- md:samp int -->

- <!-- md:samp int -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`OPERATION_ADDITION`|`0`||
  |`OPERATION_MULTIPLY_BASE`|`1`||
  |`OPERATION_MULTIPLY_TOTAL`|`2`||
  |`OPERATION_CAP`|`3`||
  |`TOTAL_OPERATIONS`|`4`||
  |`OPERATION_INVALID`|`TOTAL_OPERATIONS`||



////////
//////// define
Operand：<!-- md:samp int -->

- <!-- md:samp int -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`OPERAND_MIN`|`0`||
  |`OPERAND_MAX`|`1`||
  |`OPERAND_CURRENT`|`2`||
  |`TOTAL_OPERANDS`|`3`||
  |`OPERAND_INVALID`|`TOTAL_OPERANDS`||



////////
//////// define
isSerializable?：<!-- md:samp bool -->

- <!-- md:samp bool -->类型。


////////

///////

//////

/////

////
//// define
Count of ticks since simulation started：<!-- md:samp unsigned varint64 -->

- <!-- md:samp unsigned varint64 -->类型。


////

///


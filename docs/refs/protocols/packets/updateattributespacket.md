# <!-- md:samp UpdateAttributesPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp UpdateAttributesPacket -->数据包，数字ID是`29`。该数据包用于protocol.packet.updateattributespacket.description

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
6 -> 19
19 -> 20
6 -> 21
21 -> 22
22 -> 23
21 -> 24
24 -> 25
25 -> 26
24 -> 27
27 -> 28
24 -> 29
29 -> 30
24 -> 31
31 -> 32
24 -> 33
33 -> 34
24 -> 35
35 -> 36
0 -> 37
37 -> 38

0 [label="UpdateAttributesPacket",comment="name: \"UpdateAttributesPacket\", typeName: \"\", id: 0, branchId: 29, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="RuntimeID",comment="name: \"RuntimeID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"Target Runtime ID\""];
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
13 [label="Default Min Value",comment="name: \"Default Min Value\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="float",comment="name: \"float\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Default Max Value",comment="name: \"Default Max Value\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="float",comment="name: \"float\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Default Value",comment="name: \"Default Value\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="float",comment="name: \"float\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Attribute Name",comment="name: \"Attribute Name\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="string",comment="name: \"string\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Attribute Modifier",comment="name: \"Attribute Modifier\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
22 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
23 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
24 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
25 [label="ID",comment="name: \"ID\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="string",comment="name: \"string\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="Name",comment="name: \"Name\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
28 [label="string",comment="name: \"string\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
29 [label="Amount",comment="name: \"Amount\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
30 [label="float",comment="name: \"float\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="Operation",comment="name: \"Operation\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="int",comment="name: \"int\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Operand",comment="name: \"Operand\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="int",comment="name: \"int\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="isSerializable?",comment="name: \"isSerializable?\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
36 [label="bool",comment="name: \"bool\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="Tick",comment="name: \"Tick\", typeName: \"PlayerInputTick\", id: 37, branchId: 0, recurseId: -1, attributes: 256, notes: \"If this packet is referring to the player or a client predicted vehicle they are in control of, this should be the most recently processed PlayerInputTick from their PlayerAuthInputPacket. Otherwise zero.\""];
38 [label="PlayerInputTick",comment="name: \"PlayerInputTick\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8;10;12;14;16;18;20;23;26;28;30;32;34;36;38}

}

```

## 字段

```title='UpdateAttributesPacket'
[runtimeid][attribute_list][tick]
```

/// html | div.result
//// define
RuntimeID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.updateattributespacket.runtimeid.descriptionTarget Runtime ID


////
```title='Attribute List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.updateattributespacket.attribute_list.array_size.description


/////
```title='示例元素'
[min_value][max_value][current_value][default_min_value][default_max_value][default_value][attribute_name][attribute_modifier]
```

///// html | div.result
////// define
Min Value：<!-- md:samp float -->

- 基本类型。protocol.packet.updateattributespacket.attribute_list.example_element.min_value.description


//////
////// define
Max Value：<!-- md:samp float -->

- 基本类型。protocol.packet.updateattributespacket.attribute_list.example_element.max_value.description


//////
////// define
Current Value：<!-- md:samp float -->

- 基本类型。protocol.packet.updateattributespacket.attribute_list.example_element.current_value.description


//////
////// define
Default Min Value：<!-- md:samp float -->

- 基本类型。protocol.packet.updateattributespacket.attribute_list.example_element.default_min_value.description


//////
////// define
Default Max Value：<!-- md:samp float -->

- 基本类型。protocol.packet.updateattributespacket.attribute_list.example_element.default_max_value.description


//////
////// define
Default Value：<!-- md:samp float -->

- 基本类型。protocol.packet.updateattributespacket.attribute_list.example_element.default_value.description


//////
////// define
Attribute Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.updateattributespacket.attribute_list.example_element.attribute_name.description


//////
```title='Attribute Modifier'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.updateattributespacket.attribute_list.example_element.attribute_modifier.array_size.description


///////
```title='示例元素'
[id][name][amount][operation][operand][isserializable]
```

/////// html | div.result
//////// define
ID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.updateattributespacket.attribute_list.example_element.attribute_modifier.example_element.id.description


////////
//////// define
Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.updateattributespacket.attribute_list.example_element.attribute_modifier.example_element.name.description


////////
//////// define
Amount：<!-- md:samp float -->

- 基本类型。protocol.packet.updateattributespacket.attribute_list.example_element.attribute_modifier.example_element.amount.description


////////
//////// define
Operation：<!-- md:samp int -->

- 基本类型枚举。protocol.packet.updateattributespacket.attribute_list.example_element.attribute_modifier.example_element.operation.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`OPERATION_ADDITION`|`0`|protocol.enum.operation_addition|
  |`OPERATION_MULTIPLY_BASE`|`1`|protocol.enum.operation_multiply_base|
  |`OPERATION_MULTIPLY_TOTAL`|`2`|protocol.enum.operation_multiply_total|
  |`OPERATION_CAP`|`3`|protocol.enum.operation_cap|
  |`TOTAL_OPERATIONS`|`4`|protocol.enum.total_operations|
  |`OPERATION_INVALID`|`TOTAL_OPERATIONS`|protocol.enum.operation_invalid|



////////
//////// define
Operand：<!-- md:samp int -->

- 基本类型枚举。protocol.packet.updateattributespacket.attribute_list.example_element.attribute_modifier.example_element.operand.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`OPERAND_MIN`|`0`|protocol.enum.operand_min|
  |`OPERAND_MAX`|`1`|protocol.enum.operand_max|
  |`OPERAND_CURRENT`|`2`|protocol.enum.operand_current|
  |`TOTAL_OPERANDS`|`3`|protocol.enum.total_operands|
  |`OPERAND_INVALID`|`TOTAL_OPERANDS`|protocol.enum.operand_invalid|



////////
//////// define
isSerializable?：<!-- md:samp bool -->

- 基本类型。protocol.packet.updateattributespacket.attribute_list.example_element.attribute_modifier.example_element.isserializable.description


////////

///////

//////

/////

////
//// define
Tick：[<!-- md:samp PlayerInputTick -->](../types/playerinputtick.md)

- 特殊类型。protocol.packet.updateattributespacket.tick.descriptionIf this packet is referring to the player or a client predicted vehicle they are in control of, this should be the most recently processed PlayerInputTick from their PlayerAuthInputPacket. Otherwise zero.


////

///


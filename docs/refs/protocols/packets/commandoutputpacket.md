# <!-- md:samp CommandOutputPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CommandOutputPacket -->数据包，数字ID是`79`。

## 结构

```viz
digraph "CommandOutputPacket" {
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
16 -> 17
15 -> 18
18 -> 19
19 -> 20
0 -> 21
21 -> 22
22 -> 23
21 -> 24
24 -> 25
25 -> 26

0 [label="CommandOutputPacket",comment="name: \"CommandOutputPacket\", typeName: \"\", id: 0, branchId: 79, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Origin Data",comment="name: \"Origin Data\", typeName: \"CommandOriginData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="CommandOriginData",comment="name: \"CommandOriginData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Output Type",comment="name: \"Output Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CommandOutputType\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Success Count",comment="name: \"Success Count\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Output Messages",comment="name: \"Output Messages\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
8 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
11 [label="Successful?",comment="name: \"Successful?\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="bool",comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Message ID",comment="name: \"Message ID\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Parameters",comment="name: \"Parameters\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
16 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
17 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
19 [label="Param",comment="name: \"Param\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="string",comment="name: \"string\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Dependency on 'Output Type == DataSet'",shape=note,comment="name: \"Dependency on 'Output Type == DataSet'\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
22 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
23 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
24 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 24, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
25 [label="Data Set",comment="name: \"Data Set\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="string",comment="name: \"string\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;9;12;14;17;20;23;26}

}

```

## 字段

```title='CommandOutputPacket'
[origin_data][output_type][success_count][output_messages][dependency_on_output_type_==_dataset]
```

/// html | div.result
//// define
Origin Data：[<!-- md:samp CommandOriginData -->](../types/commandorigindata.md)

- 特殊类型。


////
//// define
Output Type：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`LastOutput`|`1`||
  |`Silent`|`2`||
  |`AllOutput`|`3`||
  |`DataSet`|`4`||



////
//// define
Success Count：<!-- md:samp unsigned varint -->

- 基本类型。


////
```title='Output Messages'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。


/////
```title='示例元素'
[successful][message_id][parameters]
```

///// html | div.result
////// define
Successful?：<!-- md:samp bool -->

- 基本类型。


//////
////// define
Message ID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


//////
```title='Parameters'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。


///////
```title='示例元素'
[param]
```

/////// html | div.result
//////// define
Param：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////////

///////

//////

/////

////
> 依赖于`Output Type == DataSet`

///// tab | `Output Type == DataSet`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Output Type == DataSet`如果为`1`
```title='if (1)'
[data_set]
```

////// html | div.result
/////// define
Data Set：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


///////

//////

/////

///


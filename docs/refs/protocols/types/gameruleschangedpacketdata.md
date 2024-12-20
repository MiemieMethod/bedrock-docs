# <!-- md:samp GameRulesChangedPacketData -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp GameRulesChangedPacketData -->类型。该类型用于protocol.type.gameruleschangedpacketdata.description

## 结构

```viz
digraph "GameRulesChangedPacketData" {
rankdir = LR
1
1 -> 2
2 -> 3
3 -> 4
2 -> 5
5 -> 6
6 -> 7
5 -> 8
8 -> 9
5 -> 10
10 -> 11
10 -> 16
10 -> 17
5 -> 12
12 -> 13
13 -> 14
14 -> 15

1 [label="GameRulesChangedPacketData",comment="name: \"GameRulesChangedPacketData\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="Rules List",comment="name: \"Rules List\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
3 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
6 [label="Rule Name",comment="name: \"Rule Name\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
7 [label="string",comment="name: \"string\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="Can Be Modified By Player",comment="name: \"Can Be Modified By Player\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="bool",comment="name: \"bool\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="Rule Type",comment="name: \"Rule Type\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="Dependency on 'Rule Type'",shape=note,comment="name: \"Dependency on 'Rule Type'\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
13 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 13, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
14 [label="Rule Value",comment="name: \"Rule Value\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="bool",comment="name: \"bool\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;4;7;9;11;16;17;15}

}

```

## 字段

```title='GameRulesChangedPacketData'
[rules_list]
```

/// html | div.result
```title='Rules List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.gameruleschangedpacketdata.rules_list.array_size.description


/////
```title='示例元素'
[rule_name][can_be_modified_by_player][rule_type][dependency_on_rule_type]
```

///// html | div.result
////// define
Rule Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.gameruleschangedpacketdata.rules_list.example_element.rule_name.description


//////
////// define
Can Be Modified By Player：<!-- md:samp bool -->

- 基本类型。protocol.type.gameruleschangedpacketdata.rules_list.example_element.can_be_modified_by_player.description


//////
```title='Rule Type'
[unsigned_varint][unsigned_varint][unsigned_varint]
```

////// html | div.result
```title='unsigned varint'

```

/////// html | div.result

///////
```title='unsigned varint'

```

/////// html | div.result

///////
```title='unsigned varint'

```

/////// html | div.result

///////

//////
> 依赖于`Rule Type`

/////// tab | `Rule Type`如果为`1`
```title='if (1)'
[rule_value]
```

//////// html | div.result
///////// define
Rule Value：<!-- md:samp bool -->

- 基本类型。protocol.type.gameruleschangedpacketdata.rules_list.example_element.dependency_on_rule_type.if_1.rule_value.description


/////////

////////

///////

/////

////

///


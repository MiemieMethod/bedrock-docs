# <!-- md:samp UnlockedRecipesPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UnlockedRecipesPacket -->数据包，数字ID是`199`。

## 结构

```viz
digraph "UnlockedRecipesPacket" {
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

0 [label="UnlockedRecipesPacket",comment="name: \"UnlockedRecipesPacket\", typeName: \"\", id: 0, branchId: 199, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Packet Type",comment="name: \"Packet Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Unlocked Recipes List",comment="name: \"Unlocked Recipes List\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Recipe",comment="name: \"Recipe\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8}

}

```

## 字段

```title='UnlockedRecipesPacket'
[packet_type][unlocked_recipes_list]
```

/// html | div.result
//// define
Packet Type：<!-- md:samp unsigned int -->

- 基本类型。


////
```title='Unlocked Recipes List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。


/////
```title='示例元素'
[recipe]
```

///// html | div.result
////// define
Recipe：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


//////

/////

////

///


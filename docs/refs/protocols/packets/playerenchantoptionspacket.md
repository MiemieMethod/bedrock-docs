# <!-- md:samp PlayerEnchantOptionsPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PlayerEnchantOptionsPacket -->数据包，数字ID是`146`。该数据包用于protocol.packet.playerenchantoptionspacket.description

## 结构

```viz
digraph "PlayerEnchantOptionsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6
4 -> 7
7 -> 35
4 -> 36
36 -> 37
4 -> 38
38 -> 39

0 [label="PlayerEnchantOptionsPacket",comment="name: \"PlayerEnchantOptionsPacket\", typeName: \"\", id: 0, branchId: 146, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Options",comment="name: \"Options\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Cost",comment="name: \"Cost\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Enchants",comment="name: \"Enchants\", typeName: \"ItemEnchants\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
35 [label="ItemEnchants",comment="name: \"ItemEnchants\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
36 [label="Enchant Name",comment="name: \"Enchant Name\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
37 [label="string",comment="name: \"string\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
38 [label="Enchant Net Id",comment="name: \"Enchant Net Id\", typeName: \"TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>\", id: 38, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
39 [label="TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>",comment="name: \"TypedServerNetId<struct RecipeNetIdTag,unsigned int,0>\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6;35;37;39}

}

```

## 字段

```title='PlayerEnchantOptionsPacket'
[options]
```

/// html | div.result
```title='Options'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.playerenchantoptionspacket.options.array_size.description


/////
```title='示例元素'
[cost][enchants][enchant_name][enchant_net_id]
```

///// html | div.result
////// define
Cost：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.playerenchantoptionspacket.options.example_element.cost.description


//////
////// define
Enchants：[<!-- md:samp ItemEnchants -->](../types/itemenchants.md)

- 特殊类型。protocol.packet.playerenchantoptionspacket.options.example_element.enchants.description


//////
////// define
Enchant Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.playerenchantoptionspacket.options.example_element.enchant_name.description


//////
////// define
Enchant Net Id：[<!-- md:samp TypedServerNetId&lt;struct RecipeNetIdTag,unsigned int,0&gt; -->](../types/typedservernetid_struct_recipenetidtag,unsigned_int,0_.md)

- 特殊类型。protocol.packet.playerenchantoptionspacket.options.example_element.enchant_net_id.description


//////

/////

////

///


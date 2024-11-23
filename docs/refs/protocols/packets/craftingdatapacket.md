# <!-- md:samp CraftingDataPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp CraftingDataPacket -->数据包，数字ID是`52`。该数据包用于protocol.packet.craftingdatapacket.description

## 结构

```viz
digraph "CraftingDataPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6
0 -> 7
7 -> 8
8 -> 9
7 -> 10
10 -> 11
11 -> 25
0 -> 26
26 -> 27
27 -> 28
26 -> 29
29 -> 30
30 -> 38
0 -> 39
39 -> 40
40 -> 41
39 -> 42
42 -> 43
43 -> 55
0 -> 56
56 -> 57

0 [label="CraftingDataPacket",comment="name: \"CraftingDataPacket\", typeName: \"\", id: 0, branchId: 52, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Crafting Entries",comment="name: \"Crafting Entries\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Crafting Entry",comment="name: \"Crafting Entry\", typeName: \"CraftingDataEntry\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="CraftingDataEntry",comment="name: \"CraftingDataEntry\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Potion Mixes",comment="name: \"Potion Mixes\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
8 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
11 [label="Potion Mix Entry",comment="name: \"Potion Mix Entry\", typeName: \"PotionMixDataEntry\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
25 [label="PotionMixDataEntry",comment="name: \"PotionMixDataEntry\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="Container Mixes",comment="name: \"Container Mixes\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
27 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
28 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
29 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
30 [label="Container Mix Entry",comment="name: \"Container Mix Entry\", typeName: \"ContainerMixDataEntry\", id: 30, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
38 [label="ContainerMixDataEntry",comment="name: \"ContainerMixDataEntry\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
39 [label="Material Reducers",comment="name: \"Material Reducers\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
40 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
41 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
42 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
43 [label="Material Reducer Entry",comment="name: \"Material Reducer Entry\", typeName: \"MaterialReducerDataEntry\", id: 43, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
55 [label="MaterialReducerDataEntry",comment="name: \"MaterialReducerDataEntry\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
56 [label="Clear Recipes",comment="name: \"Clear Recipes\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
57 [label="bool",comment="name: \"bool\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6;9;25;28;38;41;55;57}

}

```

## 字段

```title='CraftingDataPacket'
[crafting_entries][potion_mixes][container_mixes][material_reducers][clear_recipes]
```

/// html | div.result
```title='Crafting Entries'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.craftingdatapacket.crafting_entries.array_size.description


/////
```title='示例元素'
[crafting_entry]
```

///// html | div.result
////// define
Crafting Entry：[<!-- md:samp CraftingDataEntry -->](../types/craftingdataentry.md)

- 特殊类型。protocol.packet.craftingdatapacket.crafting_entries.example_element.crafting_entry.description


//////

/////

////
```title='Potion Mixes'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.craftingdatapacket.potion_mixes.array_size.description


/////
```title='示例元素'
[potion_mix_entry]
```

///// html | div.result
////// define
Potion Mix Entry：[<!-- md:samp PotionMixDataEntry -->](../types/potionmixdataentry.md)

- 特殊类型。protocol.packet.craftingdatapacket.potion_mixes.example_element.potion_mix_entry.description


//////

/////

////
```title='Container Mixes'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.craftingdatapacket.container_mixes.array_size.description


/////
```title='示例元素'
[container_mix_entry]
```

///// html | div.result
////// define
Container Mix Entry：[<!-- md:samp ContainerMixDataEntry -->](../types/containermixdataentry.md)

- 特殊类型。protocol.packet.craftingdatapacket.container_mixes.example_element.container_mix_entry.description


//////

/////

////
```title='Material Reducers'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.craftingdatapacket.material_reducers.array_size.description


/////
```title='示例元素'
[material_reducer_entry]
```

///// html | div.result
////// define
Material Reducer Entry：[<!-- md:samp MaterialReducerDataEntry -->](../types/materialreducerdataentry.md)

- 特殊类型。protocol.packet.craftingdatapacket.material_reducers.example_element.material_reducer_entry.description


//////

/////

////
//// define
Clear Recipes：<!-- md:samp bool -->

- 基本类型。protocol.packet.craftingdatapacket.clear_recipes.description


////

///


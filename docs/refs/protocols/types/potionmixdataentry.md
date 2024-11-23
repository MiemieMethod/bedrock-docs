# <!-- md:samp PotionMixDataEntry -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp PotionMixDataEntry -->类型。该类型用于protocol.type.potionmixdataentry.description

## 结构

```viz
digraph "PotionMixDataEntry" {
rankdir = LR
12
12 -> 13
13 -> 14
12 -> 15
15 -> 16
12 -> 17
17 -> 18
12 -> 19
19 -> 20
12 -> 21
21 -> 22
12 -> 23
23 -> 24

12 [label="PotionMixDataEntry",comment="name: \"PotionMixDataEntry\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
13 [label="From Potion: Input - Potion Id",comment="name: \"From Potion: Input - Potion Id\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="varint",comment="name: \"varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="From Item Aux",comment="name: \"From Item Aux\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="varint",comment="name: \"varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Reagent Item Id",comment="name: \"Reagent Item Id\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="varint",comment="name: \"varint\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Reagent Item Aux",comment="name: \"Reagent Item Aux\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="varint",comment="name: \"varint\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="To Potion: Output - Potion Id",comment="name: \"To Potion: Output - Potion Id\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="varint",comment="name: \"varint\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="To Item Aux",comment="name: \"To Item Aux\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="varint",comment="name: \"varint\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;14;16;18;20;22;24}

}

```

## 字段

```title='PotionMixDataEntry'
[from_potion:_input_potion_id][from_item_aux][reagent_item_id][reagent_item_aux][to_potion:_output_potion_id][to_item_aux]
```

/// html | div.result
//// define
From Potion: Input - Potion Id：<!-- md:samp varint -->

- 基本类型。protocol.type.potionmixdataentry.from_potion:_input_potion_id.description


////
//// define
From Item Aux：<!-- md:samp varint -->

- 基本类型。protocol.type.potionmixdataentry.from_item_aux.description


////
//// define
Reagent Item Id：<!-- md:samp varint -->

- 基本类型。protocol.type.potionmixdataentry.reagent_item_id.description


////
//// define
Reagent Item Aux：<!-- md:samp varint -->

- 基本类型。protocol.type.potionmixdataentry.reagent_item_aux.description


////
//// define
To Potion: Output - Potion Id：<!-- md:samp varint -->

- 基本类型。protocol.type.potionmixdataentry.to_potion:_output_potion_id.description


////
//// define
To Item Aux：<!-- md:samp varint -->

- 基本类型。protocol.type.potionmixdataentry.to_item_aux.description


////

///


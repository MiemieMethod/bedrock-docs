# <!-- md:samp InventoryTransactionPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp InventoryTransactionPacket -->数据包，数字ID是`30`。该数据包用于protocol.packet.inventorytransactionpacket.description

## 结构

```viz
digraph "InventoryTransactionPacket" {
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
8 -> 9
7 -> 10
10 -> 11
11 -> 12
10 -> 13
13 -> 14
14 -> 15
13 -> 16
16 -> 17
17 -> 18
0 -> 19
19 -> 20
0 -> 21
21 -> 52

0 [label="InventoryTransactionPacket",comment="name: \"InventoryTransactionPacket\", typeName: \"\", id: 0, branchId: 30, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Raw Id (32 bit signed)",comment="name: \"Raw Id (32 bit signed)\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Dependency on 'above ID (the legacy request ID) nonzero'",shape=note,comment="name: \"Dependency on 'above ID (the legacy request ID) nonzero'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
4 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
5 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 6, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="Legacy Set Item Slots",comment="name: \"Legacy Set Item Slots\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"Only matters when ItemStackNetManager is enabled\""];
8 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
11 [label="Container Enum",comment="name: \"Container Enum\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="byte",comment="name: \"byte\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Slot vector",comment="name: \"Slot vector\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
14 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
17 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="byte",comment="name: \"byte\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Transaction Type",comment="name: \"Transaction Type\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="mTransaction->mTransaction",comment="name: \"mTransaction->mTransaction\", typeName: \"InventoryTransaction\", id: 21, branchId: 0, recurseId: -1, attributes: 256, notes: \"Our ComplexInventoryTransaction contains an InventoryTransaction within it\""];
52 [label="InventoryTransaction",comment="name: \"InventoryTransaction\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;9;12;15;18;20;52}

}

```

## 字段

```title='InventoryTransactionPacket'
[raw_id][dependency_on_above_id_nonzero][transaction_type][mtransaction->mtransaction]
```

/// html | div.result
//// define
Raw Id (32 bit signed)：<!-- md:samp varint -->

- 基本类型。protocol.packet.inventorytransactionpacket.raw_id.description


////
> 依赖于`above ID (the legacy request ID) nonzero`

///// tab | `above ID (the legacy request ID) nonzero`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `above ID (the legacy request ID) nonzero`如果为`1`
```title='if (1)'
[legacy_set_item_slots]
```

////// html | div.result
```title='Legacy Set Item Slots'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.inventorytransactionpacket.dependency_on_above_id_nonzero.if_1.legacy_set_item_slots.array_size.description


////////
```title='示例元素'
[container_enum][slot_vector]
```

//////// html | div.result
///////// define
Container Enum：<!-- md:samp byte -->

- 基本类型。protocol.packet.inventorytransactionpacket.dependency_on_above_id_nonzero.if_1.legacy_set_item_slots.example_element.container_enum.description


/////////
```title='Slot vector'
[array_size][[example_element]..]
```

///////// html | div.result
////////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.inventorytransactionpacket.dependency_on_above_id_nonzero.if_1.legacy_set_item_slots.example_element.slot_vector.array_size.description


//////////
```title='示例元素'
[slot]
```

////////// html | div.result
/////////// define
Slot：<!-- md:samp byte -->

- 基本类型。protocol.packet.inventorytransactionpacket.dependency_on_above_id_nonzero.if_1.legacy_set_item_slots.example_element.slot_vector.example_element.slot.description


///////////

//////////

/////////

////////

///////

//////

/////
//// define
Transaction Type：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.packet.inventorytransactionpacket.transaction_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NormalTransaction`|`0`|protocol.enum.normaltransaction|
  |`InventoryMismatch`|`1`|protocol.enum.inventorymismatch|
  |`ItemUseTransaction`|`2`|protocol.enum.itemusetransaction|
  |`ItemUseOnEntityTransaction`|`3`|protocol.enum.itemuseonentitytransaction|
  |`ItemReleaseTransaction`|`4`|protocol.enum.itemreleasetransaction|



////
//// define
mTransaction->mTransaction：[<!-- md:samp InventoryTransaction -->](../types/inventorytransaction.md)

- 特殊类型。protocol.packet.inventorytransactionpacket.mtransaction-&gt;mtransaction.descriptionOur ComplexInventoryTransaction contains an InventoryTransaction within it


////

///


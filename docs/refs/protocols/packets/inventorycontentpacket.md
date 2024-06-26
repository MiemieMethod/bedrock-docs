# <!-- md:samp InventoryContentPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp InventoryContentPacket -->数据包，数字ID是`49`。该数据包用于protocol.packet.inventorycontentpacket.description

## 结构

```viz
digraph "InventoryContentPacket" {
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

0 [label="InventoryContentPacket",comment="name: \"InventoryContentPacket\", typeName: \"\", id: 0, branchId: 49, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Inventory Id",comment="name: \"Inventory Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Slots",comment="name: \"Slots\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Item stack",comment="name: \"Item stack\", typeName: \"NetworkItemStackDescriptor\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
8 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8}

}

```

## 字段

```title='InventoryContentPacket'
[inventory_id][slots]
```

/// html | div.result
//// define
Inventory Id：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.inventorycontentpacket.inventory_id.description


////
```title='Slots'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.inventorycontentpacket.slots.array_size.description


/////
```title='示例元素'
[item_stack]
```

///// html | div.result
////// define
Item stack：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。protocol.packet.inventorycontentpacket.slots.example_element.item_stack.description


//////

/////

////

///


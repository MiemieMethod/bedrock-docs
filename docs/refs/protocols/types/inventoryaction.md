# <!-- md:samp InventoryAction -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp InventoryAction -->类型。

## 结构

```viz
digraph "InventoryAction" {
rankdir = LR
28
28 -> 29
29 -> 44
28 -> 45
45 -> 46
28 -> 47
47 -> 48
28 -> 49
49 -> 50

28 [label="InventoryAction",comment="name: \"InventoryAction\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
29 [label="Source",comment="name: \"Source\", typeName: \"InventorySource\", id: 29, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
44 [label="InventorySource",comment="name: \"InventorySource\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
45 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
46 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
47 [label="From Item Descriptor",comment="name: \"From Item Descriptor\", typeName: \"NetworkItemStackDescriptor\", id: 47, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
48 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
49 [label="To Item Descriptor",comment="name: \"To Item Descriptor\", typeName: \"NetworkItemStackDescriptor\", id: 49, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
50 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;44;46;48;50}

}

```

## 字段

```title='InventoryAction'
[source][slot][from_item_descriptor][to_item_descriptor]
```

/// html | div.result
//// define
Source：[<!-- md:samp InventorySource -->](../types/inventorysource.md)

- 特殊类型。


////
//// define
Slot：<!-- md:samp unsigned varint -->

- 基本类型。


////
//// define
From Item Descriptor：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。


////
//// define
To Item Descriptor：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 特殊类型。


////

///


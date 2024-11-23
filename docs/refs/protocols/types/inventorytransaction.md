# <!-- md:samp InventoryTransaction -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp InventoryTransaction -->类型。该类型用于protocol.type.inventorytransaction.description

## 结构

```viz
digraph "InventoryTransaction" {
rankdir = LR
22
22 -> 23
23 -> 24
24 -> 25
23 -> 26
26 -> 27
27 -> 51

22 [label="InventoryTransaction",comment="name: \"InventoryTransaction\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
23 [label="Actions",comment="name: \"Actions\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
24 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
25 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
27 [label="Action",comment="name: \"Action\", typeName: \"InventoryAction\", id: 27, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
51 [label="InventoryAction",comment="name: \"InventoryAction\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;25;51}

}

```

## 字段

```title='InventoryTransaction'
[actions]
```

/// html | div.result
```title='Actions'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.inventorytransaction.actions.array_size.description


/////
```title='示例元素'
[action]
```

///// html | div.result
////// define
Action：[<!-- md:samp InventoryAction -->](../types/inventoryaction.md)

- 特殊类型。protocol.type.inventorytransaction.actions.example_element.action.description


//////

/////

////

///


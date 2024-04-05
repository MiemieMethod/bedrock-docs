# <!-- md:samp InventoryTransaction -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp InventoryTransaction -->类型。

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

/// define
InventoryTransaction

Actions

//// define
Actions数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Actions的示例元素

Action：[<!-- md:samp InventoryAction -->](../types/inventoryaction.md)

- 类型：InventoryAction。


////



///

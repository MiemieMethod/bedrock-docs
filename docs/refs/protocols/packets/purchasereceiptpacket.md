# <!-- md:samp PurchaseReceiptPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp PurchaseReceiptPacket -->数据包，数字ID是`92`。该数据包用于protocol.packet.purchasereceiptpacket.description

## 结构

```viz
digraph "PurchaseReceiptPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6

0 [label="PurchaseReceiptPacket",comment="name: \"PurchaseReceiptPacket\", typeName: \"\", id: 0, branchId: 92, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Purchase Receipts",comment="name: \"Purchase Receipts\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Proof of Purchase",comment="name: \"Proof of Purchase\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6}

}

```

## 字段

```title='PurchaseReceiptPacket'
[purchase_receipts]
```

/// html | div.result
```title='Purchase Receipts'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.purchasereceiptpacket.purchase_receipts.array_size.description


/////
```title='示例元素'
[proof_of_purchase]
```

///// html | div.result
////// define
Proof of Purchase：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.purchasereceiptpacket.purchase_receipts.example_element.proof_of_purchase.description


//////

/////

////

///


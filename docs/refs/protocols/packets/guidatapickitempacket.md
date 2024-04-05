# <!-- md:samp GuiDataPickItemPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp GuiDataPickItemPacket -->数据包，数字ID是`54`。

## 结构

```viz
digraph "GuiDataPickItemPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="GuiDataPickItemPacket",comment="name: \"GuiDataPickItemPacket\", typeName: \"\", id: 0, branchId: 54, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Item Name",comment="name: \"Item Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Item Effect Name",comment="name: \"Item Effect Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Slot",comment="name: \"Slot\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="int",comment="name: \"int\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='GuiDataPickItemPacket'
[item_name][item_effect_name][slot]
```

/// html | div.result
//// define
Item Name：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Item Effect Name：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Slot：<!-- md:samp int -->

- 类型：<!-- md:samp int -->。


////

///


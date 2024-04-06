# <!-- md:samp OpenSignPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp OpenSignPacket -->数据包，数字ID是`303`。

## 结构

```viz
digraph "OpenSignPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="OpenSignPacket",comment="name: \"OpenSignPacket\", typeName: \"\", id: 0, branchId: 303, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Pos",comment="name: \"Pos\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Is Front Side",comment="name: \"Is Front Side\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='OpenSignPacket'
[pos][is_front_side]
```

/// html | div.result
//// define
Pos：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- <!-- md:samp NetworkBlockPosition -->类型。


////
//// define
Is Front Side：<!-- md:samp bool -->

- <!-- md:samp bool -->类型。


////

///


# <!-- md:samp AnvilDamagePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AnvilDamagePacket -->数据包，数字ID是`141`。

## 结构

```viz
digraph "AnvilDamagePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="AnvilDamagePacket",comment="name: \"AnvilDamagePacket\", typeName: \"\", id: 0, branchId: 141, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Damage Amount",comment="name: \"Damage Amount\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Block Position",comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='AnvilDamagePacket'
[damage_amount][block_position]
```

/// html | div.result
//// define
Damage Amount：<!-- md:samp byte -->

- 基本类型。


////
//// define
Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。


////

///


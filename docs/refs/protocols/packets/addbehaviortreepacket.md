# <!-- md:samp AddBehaviorTreePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AddBehaviorTreePacket -->数据包，数字ID是`89`。该数据包用于protocol.packet.addbehaviortreepacket.description

## 结构

```viz
digraph "AddBehaviorTreePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="AddBehaviorTreePacket",comment="name: \"AddBehaviorTreePacket\", typeName: \"\", id: 0, branchId: 89, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Behavior Tree Structure (JSON)",comment="name: \"Behavior Tree Structure (JSON)\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='AddBehaviorTreePacket'
[behavior_tree_structure]
```

/// html | div.result
//// define
Behavior Tree Structure (JSON)：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.addbehaviortreepacket.behavior_tree_structure.description


////

///


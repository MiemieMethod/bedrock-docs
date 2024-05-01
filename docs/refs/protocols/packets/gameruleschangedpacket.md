# <!-- md:samp GameRulesChangedPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp GameRulesChangedPacket -->数据包，数字ID是`72`。该数据包用于protocol.packet.gameruleschangedpacket.description

## 结构

```viz
digraph "GameRulesChangedPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="GameRulesChangedPacket",comment="name: \"GameRulesChangedPacket\", typeName: \"\", id: 0, branchId: 72, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Rules Data",comment="name: \"Rules Data\", typeName: \"GameRulesChangedPacketData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="GameRulesChangedPacketData",comment="name: \"GameRulesChangedPacketData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='GameRulesChangedPacket'
[rules_data]
```

/// html | div.result
//// define
Rules Data：[<!-- md:samp GameRulesChangedPacketData -->](../types/gameruleschangedpacketdata.md)

- 特殊类型。protocol.packet.gameruleschangedpacket.rules_data.description


////

///


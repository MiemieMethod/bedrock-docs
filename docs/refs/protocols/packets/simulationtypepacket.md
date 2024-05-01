# <!-- md:samp SimulationTypePacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp SimulationTypePacket -->数据包，数字ID是`168`。该数据包用于protocol.packet.simulationtypepacket.description

## 结构

```viz
digraph "SimulationTypePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SimulationTypePacket",comment="name: \"SimulationTypePacket\", typeName: \"\", id: 0, branchId: 168, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Sim Type",comment="name: \"Sim Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SimulationTypePacket'
[sim_type]
```

/// html | div.result
//// define
Sim Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.simulationtypepacket.sim_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Game`|`0`|protocol.enum.game|
  |`Editor`|`1`|protocol.enum.editor|
  |`Test`|`2`|protocol.enum.test|
  |`INVALID`|`3`|protocol.enum.invalid|



////

///


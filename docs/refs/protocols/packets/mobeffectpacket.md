# <!-- md:samp MobEffectPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MobEffectPacket -->数据包，数字ID是`28`。该数据包用于protocol.packet.mobeffectpacket.description

## 结构

```viz
digraph "MobEffectPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10
0 -> 11
11 -> 12
0 -> 13
13 -> 14

0 [label="MobEffectPacket",comment="name: \"MobEffectPacket\", typeName: \"\", id: 0, branchId: 28, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MobEffectPacket::Event\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Effect ID",comment="name: \"Effect ID\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Effect Amplifier",comment="name: \"Effect Amplifier\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="varint",comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Show Particles",comment="name: \"Show Particles\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="bool",comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Effect Duration Ticks",comment="name: \"Effect Duration Ticks\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="varint",comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Tick",comment="name: \"Tick\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14}

}

```

## 字段

```title='MobEffectPacket'
[target_runtime_id][event_id][effect_id][effect_amplifier][show_particles][effect_duration_ticks][tick]
```

/// html | div.result
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.mobeffectpacket.target_runtime_id.description


////
//// define
Event ID：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.mobeffectpacket.event_id.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`0`|protocol.enum.invalid|
  |`Add`|`1`|protocol.enum.add|
  |`Update`|`2`|protocol.enum.update|
  |`Remove`|`3`|protocol.enum.remove|



////
//// define
Effect ID：<!-- md:samp varint -->

- 基本类型。protocol.packet.mobeffectpacket.effect_id.description


////
//// define
Effect Amplifier：<!-- md:samp varint -->

- 基本类型。protocol.packet.mobeffectpacket.effect_amplifier.description


////
//// define
Show Particles：<!-- md:samp bool -->

- 基本类型。protocol.packet.mobeffectpacket.show_particles.description


////
//// define
Effect Duration Ticks：<!-- md:samp varint -->

- 基本类型。protocol.packet.mobeffectpacket.effect_duration_ticks.description


////
//// define
Tick：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.mobeffectpacket.tick.description


////

///


# <!-- md:samp MovementEffectPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp MovementEffectPacket -->数据包，数字ID是`318`。该数据包用于protocol.packet.movementeffectpacket.description

## 结构

```viz
digraph "MovementEffectPacket" {
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

0 [label="MovementEffectPacket",comment="name: \"MovementEffectPacket\", typeName: \"\", id: 0, branchId: 318, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Effect ID",comment="name: \"Effect ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Effect Duration",comment="name: \"Effect Duration\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Tick",comment="name: \"Tick\", typeName: \"PlayerInputTick\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"If this packet is referring to the player or a client predicted vehicle they are in control of, this should be the most recently processed PlayerInputTick from their PlayerAuthInputPacket. Otherwise zero.\""];
8 [label="PlayerInputTick",comment="name: \"PlayerInputTick\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='MovementEffectPacket'
[target_runtime_id][effect_id][effect_duration][tick]
```

/// html | div.result
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.movementeffectpacket.target_runtime_id.description


////
//// define
Effect ID：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.movementeffectpacket.effect_id.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`INVALID`|`-1`|protocol.enum.invalid|
  |`GLIDE_BOOST`|`0`|protocol.enum.glide_boost|
  |`COUNT`|`1`|protocol.enum.count|



////
//// define
Effect Duration：<!-- md:samp varint -->

- 基本类型。protocol.packet.movementeffectpacket.effect_duration.description


////
//// define
Tick：[<!-- md:samp PlayerInputTick -->](../types/playerinputtick.md)

- 特殊类型。protocol.packet.movementeffectpacket.tick.descriptionIf this packet is referring to the player or a client predicted vehicle they are in control of, this should be the most recently processed PlayerInputTick from their PlayerAuthInputPacket. Otherwise zero.


////

///


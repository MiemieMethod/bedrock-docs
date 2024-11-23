# <!-- md:samp SetActorMotionPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp SetActorMotionPacket -->数据包，数字ID是`40`。该数据包用于protocol.packet.setactormotionpacket.description

## 结构

```viz
digraph "SetActorMotionPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="SetActorMotionPacket",comment="name: \"SetActorMotionPacket\", typeName: \"\", id: 0, branchId: 40, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Motion",comment="name: \"Motion\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Tick",comment="name: \"Tick\", typeName: \"PlayerInputTick\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"If this packet is referring to the player or a client predicted vehicle they are in control of, this should be the most recently processed PlayerInputTick from their PlayerAuthInputPacket. Otherwise zero.\""];
6 [label="PlayerInputTick",comment="name: \"PlayerInputTick\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='SetActorMotionPacket'
[target_runtime_id][motion][tick]
```

/// html | div.result
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.setactormotionpacket.target_runtime_id.description


////
//// define
Motion：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.setactormotionpacket.motion.description


////
//// define
Tick：[<!-- md:samp PlayerInputTick -->](../types/playerinputtick.md)

- 特殊类型。protocol.packet.setactormotionpacket.tick.descriptionIf this packet is referring to the player or a client predicted vehicle they are in control of, this should be the most recently processed PlayerInputTick from their PlayerAuthInputPacket. Otherwise zero.


////

///


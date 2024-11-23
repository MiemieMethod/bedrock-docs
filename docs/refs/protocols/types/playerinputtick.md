# <!-- md:samp PlayerInputTick -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp PlayerInputTick -->类型。该类型用于protocol.type.playerinputtick.description

## 结构

```viz
digraph "PlayerInputTick" {
rankdir = LR
24
24 -> 25
25 -> 26

24 [label="PlayerInputTick",comment="name: \"PlayerInputTick\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
25 [label="Input tick",comment="name: \"Input tick\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \" n server authoritative movement mode the client supplies this in PlayerAuthInputPacket. or any client-bound packets containing a tick, the server should supply the tick value corresponding to the most recently processed PlayerAuthInputPacket. his allows the client to adjust any client predictions made while the packet was in flight. f the packet is being sent to the client but not relating to data of the player or a client-predicted vehicle, it can be zero. t is also acceptable to specify zero for players, although this may lead to minor visual flickers and less smooth application of CorrectPlayerMovePredictionPacket. \""];
26 [label="unsigned varint64",comment="name: \"unsigned varint64\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;26}

}

```

## 字段

```title='PlayerInputTick'
[input_tick]
```

/// html | div.result
//// define
Input tick：<!-- md:samp unsigned varint64 -->

- 基本类型。protocol.type.playerinputtick.input_tick.description n server authoritative movement mode the client supplies this in PlayerAuthInputPacket. or any client-bound packets containing a tick, the server should supply the tick value corresponding to the most recently processed PlayerAuthInputPacket. his allows the client to adjust any client predictions made while the packet was in flight. f the packet is being sent to the client but not relating to data of the player or a client-predicted vehicle, it can be zero. t is also acceptable to specify zero for players, although this may lead to minor visual flickers and less smooth application of CorrectPlayerMovePredictionPacket. 


////

///


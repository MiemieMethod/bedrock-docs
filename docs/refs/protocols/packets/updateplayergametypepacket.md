# <!-- md:samp UpdatePlayerGameTypePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp UpdatePlayerGameTypePacket -->数据包，数字ID是`151`。该数据包用于protocol.packet.updateplayergametypepacket.description

## 结构

```viz
digraph "UpdatePlayerGameTypePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="UpdatePlayerGameTypePacket",comment="name: \"UpdatePlayerGameTypePacket\", typeName: \"\", id: 0, branchId: 151, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Player game type",comment="name: \"Player game type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Target player",comment="name: \"Target player\", typeName: \"ActorUniqueID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Tick",comment="name: \"Tick\", typeName: \"PlayerInputTick\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"Most relevant to supply for transitioning into and out of spectator while in motion\""];
6 [label="PlayerInputTick",comment="name: \"PlayerInputTick\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='UpdatePlayerGameTypePacket'
[player_game_type][target_player][tick]
```

/// html | div.result
//// define
Player game type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.updateplayergametypepacket.player_game_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`-1`|protocol.enum.undefined|
  |`Survival`|`0`|protocol.enum.survival|
  |`Creative`|`1`|protocol.enum.creative|
  |`Adventure`|`2`|protocol.enum.adventure|
  |`Default`|`5`|protocol.enum.default|
  |`Spectator`|`6`|protocol.enum.spectator|
  |`WorldDefault`|`Survival`|protocol.enum.worlddefault|



////
//// define
Target player：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.updateplayergametypepacket.target_player.description


////
//// define
Tick：[<!-- md:samp PlayerInputTick -->](../types/playerinputtick.md)

- 特殊类型。protocol.packet.updateplayergametypepacket.tick.descriptionMost relevant to supply for transitioning into and out of spectator while in motion


////

///


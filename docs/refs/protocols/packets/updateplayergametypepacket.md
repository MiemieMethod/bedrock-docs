# <!-- md:samp UpdatePlayerGameTypePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdatePlayerGameTypePacket -->数据包，数字ID是`151`。

## 结构

```viz
digraph "UpdatePlayerGameTypePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="UpdatePlayerGameTypePacket",comment="name: \"UpdatePlayerGameTypePacket\", typeName: \"\", id: 0, branchId: 151, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Player game type",comment="name: \"Player game type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GameType\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Target player",comment="name: \"Target player\", typeName: \"ActorUniqueID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='UpdatePlayerGameTypePacket'
[player_game_type][target_player]
```

/// html | div.result
//// define
Player game type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`-1`||
  |`Survival`|`0`||
  |`Creative`|`1`||
  |`Adventure`|`2`||
  |`Default`|`5`||
  |`Spectator`|`6`||
  |`WorldDefault`|`Survival`||



////
//// define
Target player：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。


////

///


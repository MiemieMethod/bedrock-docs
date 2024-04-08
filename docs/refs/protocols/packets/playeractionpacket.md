# <!-- md:samp PlayerActionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerActionPacket -->数据包，数字ID是`36`。

## 结构

```viz
digraph "PlayerActionPacket" {
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

0 [label="PlayerActionPacket",comment="name: \"PlayerActionPacket\", typeName: \"\", id: 0, branchId: 36, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Player Runtime ID",comment="name: \"Player Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Action",comment="name: \"Action\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayerActionType\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Block Position",comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Result Pos",comment="name: \"Result Pos\", typeName: \"NetworkBlockPosition\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
8 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Face",comment="name: \"Face\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="varint",comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='PlayerActionPacket'
[player_runtime_id][action][block_position][result_pos][face]
```

/// html | div.result
//// define
Player Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。


////
//// define
Action：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`-1`||
  |`StartDestroyBlock`|`0`||
  |`AbortDestroyBlock`|`1`||
  |`StopDestroyBlock`|`2`||
  |`GetUpdatedBlock`|`3`||
  |`DropItem`|`4`||
  |`StartSleeping`|`5`||
  |`StopSleeping`|`6`||
  |`Respawn`|`7`||
  |`StartJump`|`8`||
  |`StartSprinting`|`9`||
  |`StopSprinting`|`10`||
  |`StartSneaking`|`11`||
  |`StopSneaking`|`12`||
  |`CreativeDestroyBlock`|`13`||
  |`ChangeDimensionAck`|`14`||
  |`StartGliding`|`15`||
  |`StopGliding`|`16`||
  |`DenyDestroyBlock`|`17`||
  |`CrackBlock`|`18`||
  |`ChangeSkin`|`19`||
  |`DEPRECATED_UpdatedEnchantingSeed`|`20`||
  |`StartSwimming`|`21`||
  |`StopSwimming`|`22`||
  |`StartSpinAttack`|`23`||
  |`StopSpinAttack`|`24`||
  |`InteractWithBlock`|`25`||
  |`PredictDestroyBlock`|`26`||
  |`ContinueDestroyBlock`|`27`||
  |`StartItemUseOn`|`28`||
  |`StopItemUseOn`|`29`||
  |`HandledTeleport`|`30`||
  |`MissedSwing`|`31`||
  |`StartCrawling`|`32`||
  |`StopCrawling`|`33`||
  |`StartFlying`|`34`||
  |`StopFlying`|`35`||
  |`ClientAckServerData`|`36`||
  |`Count`|`37`||



////
//// define
Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。


////
//// define
Result Pos：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。


////
//// define
Face：<!-- md:samp varint -->

- 基本类型。


////

///

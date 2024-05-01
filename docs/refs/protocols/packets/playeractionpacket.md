# <!-- md:samp PlayerActionPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PlayerActionPacket -->数据包，数字ID是`36`。该数据包用于protocol.packet.playeractionpacket.description

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
3 [label="Action",comment="name: \"Action\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 特殊类型。protocol.packet.playeractionpacket.player_runtime_id.description


////
//// define
Action：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.playeractionpacket.action.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`-1`|protocol.enum.unknown|
  |`StartDestroyBlock`|`0`|protocol.enum.startdestroyblock|
  |`AbortDestroyBlock`|`1`|protocol.enum.abortdestroyblock|
  |`StopDestroyBlock`|`2`|protocol.enum.stopdestroyblock|
  |`GetUpdatedBlock`|`3`|protocol.enum.getupdatedblock|
  |`DropItem`|`4`|protocol.enum.dropitem|
  |`StartSleeping`|`5`|protocol.enum.startsleeping|
  |`StopSleeping`|`6`|protocol.enum.stopsleeping|
  |`Respawn`|`7`|protocol.enum.respawn|
  |`StartJump`|`8`|protocol.enum.startjump|
  |`StartSprinting`|`9`|protocol.enum.startsprinting|
  |`StopSprinting`|`10`|protocol.enum.stopsprinting|
  |`StartSneaking`|`11`|protocol.enum.startsneaking|
  |`StopSneaking`|`12`|protocol.enum.stopsneaking|
  |`CreativeDestroyBlock`|`13`|protocol.enum.creativedestroyblock|
  |`ChangeDimensionAck`|`14`|protocol.enum.changedimensionack|
  |`StartGliding`|`15`|protocol.enum.startgliding|
  |`StopGliding`|`16`|protocol.enum.stopgliding|
  |`DenyDestroyBlock`|`17`|protocol.enum.denydestroyblock|
  |`CrackBlock`|`18`|protocol.enum.crackblock|
  |`ChangeSkin`|`19`|protocol.enum.changeskin|
  |`DEPRECATED_UpdatedEnchantingSeed`|`20`|protocol.enum.deprecated_updatedenchantingseed|
  |`StartSwimming`|`21`|protocol.enum.startswimming|
  |`StopSwimming`|`22`|protocol.enum.stopswimming|
  |`StartSpinAttack`|`23`|protocol.enum.startspinattack|
  |`StopSpinAttack`|`24`|protocol.enum.stopspinattack|
  |`InteractWithBlock`|`25`|protocol.enum.interactwithblock|
  |`PredictDestroyBlock`|`26`|protocol.enum.predictdestroyblock|
  |`ContinueDestroyBlock`|`27`|protocol.enum.continuedestroyblock|
  |`StartItemUseOn`|`28`|protocol.enum.startitemuseon|
  |`StopItemUseOn`|`29`|protocol.enum.stopitemuseon|
  |`HandledTeleport`|`30`|protocol.enum.handledteleport|
  |`MissedSwing`|`31`|protocol.enum.missedswing|
  |`StartCrawling`|`32`|protocol.enum.startcrawling|
  |`StopCrawling`|`33`|protocol.enum.stopcrawling|
  |`StartFlying`|`34`|protocol.enum.startflying|
  |`StopFlying`|`35`|protocol.enum.stopflying|
  |`ClientAckServerData`|`36`|protocol.enum.clientackserverdata|
  |`Count`|`37`|protocol.enum.count|



////
//// define
Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.playeractionpacket.block_position.description


////
//// define
Result Pos：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.playeractionpacket.result_pos.description


////
//// define
Face：<!-- md:samp varint -->

- 基本类型。protocol.packet.playeractionpacket.face.description


////

///


# <!-- md:samp PacketViolationWarningPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PacketViolationWarningPacket -->数据包，数字ID是`156`。

## 结构

```viz
digraph "PacketViolationWarningPacket" {
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

0 [label="PacketViolationWarningPacket",comment="name: \"PacketViolationWarningPacket\", typeName: \"\", id: 0, branchId: 156, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Violation Type",comment="name: \"Violation Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PacketViolationType\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Violation Severity",comment="name: \"Violation Severity\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PacketViolationSeverity\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Violating packet id",comment="name: \"Violating packet id\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MinecraftPacketIds\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Violation context",comment="name: \"Violation context\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='PacketViolationWarningPacket'
[violation_type][violation_severity][violating_packet_id][violation_context]
```

/// html | div.result
//// define
Violation Type：<!-- md:samp varint -->

- <!-- md:samp varint -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`-1`||
  |`PacketMalformed`|`0`||



////
//// define
Violation Severity：<!-- md:samp varint -->

- <!-- md:samp varint -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`-1`||
  |`Warning`|`0`||
  |`FinalWarning`|`1`||
  |`TerminatingConnection`|`2`||



////
//// define
Violating packet id：<!-- md:samp varint -->

- <!-- md:samp varint -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`KeepAlive`|`0`||
  |`Login`|`1`||
  |`PlayStatus`|`2`||
  |`ServerToClientHandshake`|`3`||
  |`ClientToServerHandshake`|`4`||
  |`Disconnect`|`5`||
  |`ResourcePacksInfo`|`6`||
  |`ResourcePackStack`|`7`||
  |`ResourcePackClientResponse`|`8`||
  |`Text`|`9`||
  |`SetTime`|`10`||
  |`StartGame`|`11`||
  |`AddPlayer`|`12`||
  |`AddActor`|`13`||
  |`RemoveActor`|`14`||
  |`AddItemActor`|`15`||
  |`ServerPlayerPostMovePosition`|`16`||
  |`TakeItemActor`|`17`||
  |`MoveAbsoluteActor`|`18`||
  |`MovePlayer`|`19`||
  |`PassengerJump`|`20`||
  |`UpdateBlock`|`21`||
  |`AddPainting`|`22`||
  |`TickSync`|`23`||
  |`LevelSoundEventV1`|`24`||
  |`LevelEvent`|`25`||
  |`TileEvent`|`26`||
  |`ActorEvent`|`27`||
  |`MobEffect`|`28`||
  |`UpdateAttributes`|`29`||
  |`InventoryTransaction`|`30`||
  |`PlayerEquipment`|`31`||
  |`MobArmorEquipment`|`32`||
  |`Interact`|`33`||
  |`BlockPickRequest`|`34`||
  |`ActorPickRequest`|`35`||
  |`PlayerAction`|`36`||
  |`ActorFall_deprecated`|`37`||
  |`HurtArmor`|`38`||
  |`SetActorData`|`39`||
  |`SetActorMotion`|`40`||
  |`SetActorLink`|`41`||
  |`SetHealth`|`42`||
  |`SetSpawnPosition`|`43`||
  |`Animate`|`44`||
  |`Respawn`|`45`||
  |`ContainerOpen`|`46`||
  |`ContainerClose`|`47`||
  |`PlayerHotbar`|`48`||
  |`InventoryContent`|`49`||
  |`InventorySlot`|`50`||
  |`ContainerSetData`|`51`||
  |`CraftingData`|`52`||
  |`CraftingEvent_Deprecated`|`53`||
  |`GuiDataPickItem`|`54`||
  |`AdventureSettings_Deprecated`|`55`||
  |`BlockActorData`|`56`||
  |`PlayerInput`|`57`||
  |`FullChunkData`|`58`||
  |`SetCommandsEnabled`|`59`||
  |`SetDifficulty`|`60`||
  |`ChangeDimension`|`61`||
  |`SetPlayerGameType`|`62`||
  |`PlayerList`|`63`||
  |`SimpleEvent`|`64`||
  |`LegacyTelemetryEvent`|`65`||
  |`SpawnExperienceOrb`|`66`||
  |`MapData`|`67`||
  |`MapInfoRequest`|`68`||
  |`RequestChunkRadius`|`69`||
  |`ChunkRadiusUpdated`|`70`||
  |`ItemFrameDropItem_Deprecated`|`71`||
  |`GameRulesChanged`|`72`||
  |`Camera`|`73`||
  |`BossEvent`|`74`||
  |`ShowCredits`|`75`||
  |`AvailableCommands`|`76`||
  |`CommandRequest`|`77`||
  |`CommandBlockUpdate`|`78`||
  |`CommandOutput`|`79`||
  |`UpdateTrade`|`80`||
  |`UpdateEquip`|`81`||
  |`ResourcePackDataInfo`|`82`||
  |`ResourcePackChunkData`|`83`||
  |`ResourcePackChunkRequest`|`84`||
  |`Transfer`|`85`||
  |`PlaySound`|`86`||
  |`StopSound`|`87`||
  |`SetTitle`|`88`||
  |`AddBehaviorTree`|`89`||
  |`StructureBlockUpdate`|`90`||
  |`ShowStoreOffer`|`91`||
  |`PurchaseReceipt`|`92`||
  |`PlayerSkin`|`93`||
  |`SubclientLogin`|`94`||
  |`AutomationClientConnect`|`95`||
  |`SetLastHurtBy`|`96`||
  |`BookEdit`|`97`||
  |`NPCRequest`|`98`||
  |`PhotoTransfer`|`99`||
  |`ShowModalForm`|`100`||
  |`ModalFormResponse`|`101`||
  |`ServerSettingsRequest`|`102`||
  |`ServerSettingsResponse`|`103`||
  |`ShowProfile`|`104`||
  |`SetDefaultGameType`|`105`||
  |`RemoveObjective`|`106`||
  |`SetDisplayObjective`|`107`||
  |`SetScore`|`108`||
  |`LabTable`|`109`||
  |`UpdateBlockSynced`|`110`||
  |`MoveDeltaActor`|`111`||
  |`SetScoreboardIdentity`|`112`||
  |`SetLocalPlayerAsInit`|`113`||
  |`UpdateSoftEnum`|`114`||
  |`Ping`|`115`||
  |`BlockPalette`|`116`||
  |`ScriptCustomEvent`|`117`||
  |`SpawnParticleEffect`|`118`||
  |`AvailableActorIDList`|`119`||
  |`LevelSoundEventV2`|`120`||
  |`NetworkChunkPublisherUpdate`|`121`||
  |`BiomeDefinitionList`|`122`||
  |`LevelSoundEvent`|`123`||
  |`LevelEventGeneric`|`124`||
  |`LecternUpdate`|`125`||
  |`VideoStreamConnect_DEPRECATED`|`126`||
  |`AddEntity_DEPRECATED`|`127`||
  |`RemoveEntity_DEPRECATED`|`128`||
  |`ClientCacheStatus`|`129`||
  |`OnScreenTextureAnimation`|`130`||
  |`MapCreateLockedCopy`|`131`||
  |`StructureTemplateDataExportRequest`|`132`||
  |`StructureTemplateDataExportResponse`|`133`||
  |`UNUSED_PLS_USE_ME`|`134`||
  |`ClientCacheBlobStatusPacket`|`135`||
  |`ClientCacheMissResponsePacket`|`136`||
  |`EducationSettingsPacket`|`137`||
  |`Emote`|`138`||
  |`MultiplayerSettingsPacket`|`139`||
  |`SettingsCommandPacket`|`140`||
  |`AnvilDamage`|`141`||
  |`CompletedUsingItem`|`142`||
  |`NetworkSettings`|`143`||
  |`PlayerAuthInputPacket`|`144`||
  |`CreativeContent`|`145`||
  |`PlayerEnchantOptions`|`146`||
  |`ItemStackRequest`|`147`||
  |`ItemStackResponse`|`148`||
  |`PlayerArmorDamage`|`149`||
  |`CodeBuilderPacket`|`150`||
  |`UpdatePlayerGameType`|`151`||
  |`EmoteList`|`152`||
  |`PositionTrackingDBServerBroadcast`|`153`||
  |`PositionTrackingDBClientRequest`|`154`||
  |`DebugInfoPacket`|`155`||
  |`PacketViolationWarning`|`156`||
  |`MotionPredictionHints`|`157`||
  |`TriggerAnimation`|`158`||
  |`CameraShake`|`159`||
  |`PlayerFogSetting`|`160`||
  |`CorrectPlayerMovePredictionPacket`|`161`||
  |`ItemComponentPacket`|`162`||
  |`FilterTextPacket`|`163`||
  |`ClientBoundDebugRendererPacket`|`164`||
  |`SyncActorProperty`|`165`||
  |`AddVolumeEntityPacket`|`166`||
  |`RemoveVolumeEntityPacket`|`167`||
  |`SimulationTypePacket`|`168`||
  |`NpcDialoguePacket`|`169`||
  |`EduUriResourcePacket`|`170`||
  |`CreatePhotoPacket`|`171`||
  |`UpdateSubChunkBlocks`|`172`||
  |`PhotoInfoRequest_DEPRECATED`|`173`||
  |`SubChunkPacket`|`174`||
  |`SubChunkRequestPacket`|`175`||
  |`PlayerStartItemCooldown`|`176`||
  |`ScriptMessagePacket`|`177`||
  |`CodeBuilderSourcePacket`|`178`||
  |`TickingAreasLoadStatus`|`179`||
  |`DimensionDataPacket`|`180`||
  |`AgentAction`|`181`||
  |`ChangeMobProperty`|`182`||
  |`LessonProgressPacket`|`183`||
  |`RequestAbilityPacket`|`184`||
  |`RequestPermissionsPacket`|`185`||
  |`ToastRequest`|`186`||
  |`UpdateAbilitiesPacket`|`187`||
  |`UpdateAdventureSettingsPacket`|`188`||
  |`DeathInfo`|`189`||
  |`EditorNetworkPacket`|`190`||
  |`FeatureRegistryPacket`|`191`||
  |`ServerStats`|`192`||
  |`RequestNetworkSettings`|`193`||
  |`GameTestRequestPacket`|`194`||
  |`GameTestResultsPacket`|`195`||
  |`PlayerClientInputPermissions`|`196`||
  |`ClientCheatAbilityPacket_Deprecated`|`197`||
  |`CameraPresets`|`198`||
  |`UnlockedRecipes`|`199`||
  |`CameraInstruction`|`300`||
  |`CompressedBiomeDefinitionList`|`301`||
  |`TrimData`|`302`||
  |`OpenSign`|`303`||
  |`AgentAnimation`|`304`||
  |`RefreshEntitlementsPacket`|`305`||
  |`PlayerToggleCrafterSlotRequestPacket`|`306`||
  |`SetPlayerInventoryOptions`|`307`||
  |`SetHudPacket`|`308`||
  |`EndId`|`309`||



////
//// define
Violation context：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////

///


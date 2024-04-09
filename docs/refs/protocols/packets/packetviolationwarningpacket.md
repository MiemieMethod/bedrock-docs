# <!-- md:samp PacketViolationWarningPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PacketViolationWarningPacket -->数据包，数字ID是`156`。该数据包用于protocol.packet.packetviolationwarningpacket.description

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

- 基本类型枚举。protocol.packet.packetviolationwarningpacket.violation_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`-1`|protocol.enum.unknown|
  |`PacketMalformed`|`0`|protocol.enum.packetmalformed|



////
//// define
Violation Severity：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.packetviolationwarningpacket.violation_severity.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`-1`|protocol.enum.unknown|
  |`Warning`|`0`|protocol.enum.warning|
  |`FinalWarning`|`1`|protocol.enum.finalwarning|
  |`TerminatingConnection`|`2`|protocol.enum.terminatingconnection|



////
//// define
Violating packet id：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.packetviolationwarningpacket.violating_packet_id.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`KeepAlive`|`0`|protocol.enum.keepalive|
  |`Login`|`1`|protocol.enum.login|
  |`PlayStatus`|`2`|protocol.enum.playstatus|
  |`ServerToClientHandshake`|`3`|protocol.enum.servertoclienthandshake|
  |`ClientToServerHandshake`|`4`|protocol.enum.clienttoserverhandshake|
  |`Disconnect`|`5`|protocol.enum.disconnect|
  |`ResourcePacksInfo`|`6`|protocol.enum.resourcepacksinfo|
  |`ResourcePackStack`|`7`|protocol.enum.resourcepackstack|
  |`ResourcePackClientResponse`|`8`|protocol.enum.resourcepackclientresponse|
  |`Text`|`9`|protocol.enum.text|
  |`SetTime`|`10`|protocol.enum.settime|
  |`StartGame`|`11`|protocol.enum.startgame|
  |`AddPlayer`|`12`|protocol.enum.addplayer|
  |`AddActor`|`13`|protocol.enum.addactor|
  |`RemoveActor`|`14`|protocol.enum.removeactor|
  |`AddItemActor`|`15`|protocol.enum.additemactor|
  |`ServerPlayerPostMovePosition`|`16`|protocol.enum.serverplayerpostmoveposition|
  |`TakeItemActor`|`17`|protocol.enum.takeitemactor|
  |`MoveAbsoluteActor`|`18`|protocol.enum.moveabsoluteactor|
  |`MovePlayer`|`19`|protocol.enum.moveplayer|
  |`PassengerJump`|`20`|protocol.enum.passengerjump|
  |`UpdateBlock`|`21`|protocol.enum.updateblock|
  |`AddPainting`|`22`|protocol.enum.addpainting|
  |`TickSync`|`23`|protocol.enum.ticksync|
  |`LevelSoundEventV1`|`24`|protocol.enum.levelsoundeventv1|
  |`LevelEvent`|`25`|protocol.enum.levelevent|
  |`TileEvent`|`26`|protocol.enum.tileevent|
  |`ActorEvent`|`27`|protocol.enum.actorevent|
  |`MobEffect`|`28`|protocol.enum.mobeffect|
  |`UpdateAttributes`|`29`|protocol.enum.updateattributes|
  |`InventoryTransaction`|`30`|protocol.enum.inventorytransaction|
  |`PlayerEquipment`|`31`|protocol.enum.playerequipment|
  |`MobArmorEquipment`|`32`|protocol.enum.mobarmorequipment|
  |`Interact`|`33`|protocol.enum.interact|
  |`BlockPickRequest`|`34`|protocol.enum.blockpickrequest|
  |`ActorPickRequest`|`35`|protocol.enum.actorpickrequest|
  |`PlayerAction`|`36`|protocol.enum.playeraction|
  |`ActorFall_deprecated`|`37`|protocol.enum.actorfall_deprecated|
  |`HurtArmor`|`38`|protocol.enum.hurtarmor|
  |`SetActorData`|`39`|protocol.enum.setactordata|
  |`SetActorMotion`|`40`|protocol.enum.setactormotion|
  |`SetActorLink`|`41`|protocol.enum.setactorlink|
  |`SetHealth`|`42`|protocol.enum.sethealth|
  |`SetSpawnPosition`|`43`|protocol.enum.setspawnposition|
  |`Animate`|`44`|protocol.enum.animate|
  |`Respawn`|`45`|protocol.enum.respawn|
  |`ContainerOpen`|`46`|protocol.enum.containeropen|
  |`ContainerClose`|`47`|protocol.enum.containerclose|
  |`PlayerHotbar`|`48`|protocol.enum.playerhotbar|
  |`InventoryContent`|`49`|protocol.enum.inventorycontent|
  |`InventorySlot`|`50`|protocol.enum.inventoryslot|
  |`ContainerSetData`|`51`|protocol.enum.containersetdata|
  |`CraftingData`|`52`|protocol.enum.craftingdata|
  |`CraftingEvent_Deprecated`|`53`|protocol.enum.craftingevent_deprecated|
  |`GuiDataPickItem`|`54`|protocol.enum.guidatapickitem|
  |`AdventureSettings_Deprecated`|`55`|protocol.enum.adventuresettings_deprecated|
  |`BlockActorData`|`56`|protocol.enum.blockactordata|
  |`PlayerInput`|`57`|protocol.enum.playerinput|
  |`FullChunkData`|`58`|protocol.enum.fullchunkdata|
  |`SetCommandsEnabled`|`59`|protocol.enum.setcommandsenabled|
  |`SetDifficulty`|`60`|protocol.enum.setdifficulty|
  |`ChangeDimension`|`61`|protocol.enum.changedimension|
  |`SetPlayerGameType`|`62`|protocol.enum.setplayergametype|
  |`PlayerList`|`63`|protocol.enum.playerlist|
  |`SimpleEvent`|`64`|protocol.enum.simpleevent|
  |`LegacyTelemetryEvent`|`65`|protocol.enum.legacytelemetryevent|
  |`SpawnExperienceOrb`|`66`|protocol.enum.spawnexperienceorb|
  |`MapData`|`67`|protocol.enum.mapdata|
  |`MapInfoRequest`|`68`|protocol.enum.mapinforequest|
  |`RequestChunkRadius`|`69`|protocol.enum.requestchunkradius|
  |`ChunkRadiusUpdated`|`70`|protocol.enum.chunkradiusupdated|
  |`ItemFrameDropItem_Deprecated`|`71`|protocol.enum.itemframedropitem_deprecated|
  |`GameRulesChanged`|`72`|protocol.enum.gameruleschanged|
  |`Camera`|`73`|protocol.enum.camera|
  |`BossEvent`|`74`|protocol.enum.bossevent|
  |`ShowCredits`|`75`|protocol.enum.showcredits|
  |`AvailableCommands`|`76`|protocol.enum.availablecommands|
  |`CommandRequest`|`77`|protocol.enum.commandrequest|
  |`CommandBlockUpdate`|`78`|protocol.enum.commandblockupdate|
  |`CommandOutput`|`79`|protocol.enum.commandoutput|
  |`UpdateTrade`|`80`|protocol.enum.updatetrade|
  |`UpdateEquip`|`81`|protocol.enum.updateequip|
  |`ResourcePackDataInfo`|`82`|protocol.enum.resourcepackdatainfo|
  |`ResourcePackChunkData`|`83`|protocol.enum.resourcepackchunkdata|
  |`ResourcePackChunkRequest`|`84`|protocol.enum.resourcepackchunkrequest|
  |`Transfer`|`85`|protocol.enum.transfer|
  |`PlaySound`|`86`|protocol.enum.playsound|
  |`StopSound`|`87`|protocol.enum.stopsound|
  |`SetTitle`|`88`|protocol.enum.settitle|
  |`AddBehaviorTree`|`89`|protocol.enum.addbehaviortree|
  |`StructureBlockUpdate`|`90`|protocol.enum.structureblockupdate|
  |`ShowStoreOffer`|`91`|protocol.enum.showstoreoffer|
  |`PurchaseReceipt`|`92`|protocol.enum.purchasereceipt|
  |`PlayerSkin`|`93`|protocol.enum.playerskin|
  |`SubclientLogin`|`94`|protocol.enum.subclientlogin|
  |`AutomationClientConnect`|`95`|protocol.enum.automationclientconnect|
  |`SetLastHurtBy`|`96`|protocol.enum.setlasthurtby|
  |`BookEdit`|`97`|protocol.enum.bookedit|
  |`NPCRequest`|`98`|protocol.enum.npcrequest|
  |`PhotoTransfer`|`99`|protocol.enum.phototransfer|
  |`ShowModalForm`|`100`|protocol.enum.showmodalform|
  |`ModalFormResponse`|`101`|protocol.enum.modalformresponse|
  |`ServerSettingsRequest`|`102`|protocol.enum.serversettingsrequest|
  |`ServerSettingsResponse`|`103`|protocol.enum.serversettingsresponse|
  |`ShowProfile`|`104`|protocol.enum.showprofile|
  |`SetDefaultGameType`|`105`|protocol.enum.setdefaultgametype|
  |`RemoveObjective`|`106`|protocol.enum.removeobjective|
  |`SetDisplayObjective`|`107`|protocol.enum.setdisplayobjective|
  |`SetScore`|`108`|protocol.enum.setscore|
  |`LabTable`|`109`|protocol.enum.labtable|
  |`UpdateBlockSynced`|`110`|protocol.enum.updateblocksynced|
  |`MoveDeltaActor`|`111`|protocol.enum.movedeltaactor|
  |`SetScoreboardIdentity`|`112`|protocol.enum.setscoreboardidentity|
  |`SetLocalPlayerAsInit`|`113`|protocol.enum.setlocalplayerasinit|
  |`UpdateSoftEnum`|`114`|protocol.enum.updatesoftenum|
  |`Ping`|`115`|protocol.enum.ping|
  |`BlockPalette`|`116`|protocol.enum.blockpalette|
  |`ScriptCustomEvent`|`117`|protocol.enum.scriptcustomevent|
  |`SpawnParticleEffect`|`118`|protocol.enum.spawnparticleeffect|
  |`AvailableActorIDList`|`119`|protocol.enum.availableactoridlist|
  |`LevelSoundEventV2`|`120`|protocol.enum.levelsoundeventv2|
  |`NetworkChunkPublisherUpdate`|`121`|protocol.enum.networkchunkpublisherupdate|
  |`BiomeDefinitionList`|`122`|protocol.enum.biomedefinitionlist|
  |`LevelSoundEvent`|`123`|protocol.enum.levelsoundevent|
  |`LevelEventGeneric`|`124`|protocol.enum.leveleventgeneric|
  |`LecternUpdate`|`125`|protocol.enum.lecternupdate|
  |`VideoStreamConnect_DEPRECATED`|`126`|protocol.enum.videostreamconnect_deprecated|
  |`AddEntity_DEPRECATED`|`127`|protocol.enum.addentity_deprecated|
  |`RemoveEntity_DEPRECATED`|`128`|protocol.enum.removeentity_deprecated|
  |`ClientCacheStatus`|`129`|protocol.enum.clientcachestatus|
  |`OnScreenTextureAnimation`|`130`|protocol.enum.onscreentextureanimation|
  |`MapCreateLockedCopy`|`131`|protocol.enum.mapcreatelockedcopy|
  |`StructureTemplateDataExportRequest`|`132`|protocol.enum.structuretemplatedataexportrequest|
  |`StructureTemplateDataExportResponse`|`133`|protocol.enum.structuretemplatedataexportresponse|
  |`UNUSED_PLS_USE_ME`|`134`|protocol.enum.unused_pls_use_me|
  |`ClientCacheBlobStatusPacket`|`135`|protocol.enum.clientcacheblobstatuspacket|
  |`ClientCacheMissResponsePacket`|`136`|protocol.enum.clientcachemissresponsepacket|
  |`EducationSettingsPacket`|`137`|protocol.enum.educationsettingspacket|
  |`Emote`|`138`|protocol.enum.emote|
  |`MultiplayerSettingsPacket`|`139`|protocol.enum.multiplayersettingspacket|
  |`SettingsCommandPacket`|`140`|protocol.enum.settingscommandpacket|
  |`AnvilDamage`|`141`|protocol.enum.anvildamage|
  |`CompletedUsingItem`|`142`|protocol.enum.completedusingitem|
  |`NetworkSettings`|`143`|protocol.enum.networksettings|
  |`PlayerAuthInputPacket`|`144`|protocol.enum.playerauthinputpacket|
  |`CreativeContent`|`145`|protocol.enum.creativecontent|
  |`PlayerEnchantOptions`|`146`|protocol.enum.playerenchantoptions|
  |`ItemStackRequest`|`147`|protocol.enum.itemstackrequest|
  |`ItemStackResponse`|`148`|protocol.enum.itemstackresponse|
  |`PlayerArmorDamage`|`149`|protocol.enum.playerarmordamage|
  |`CodeBuilderPacket`|`150`|protocol.enum.codebuilderpacket|
  |`UpdatePlayerGameType`|`151`|protocol.enum.updateplayergametype|
  |`EmoteList`|`152`|protocol.enum.emotelist|
  |`PositionTrackingDBServerBroadcast`|`153`|protocol.enum.positiontrackingdbserverbroadcast|
  |`PositionTrackingDBClientRequest`|`154`|protocol.enum.positiontrackingdbclientrequest|
  |`DebugInfoPacket`|`155`|protocol.enum.debuginfopacket|
  |`PacketViolationWarning`|`156`|protocol.enum.packetviolationwarning|
  |`MotionPredictionHints`|`157`|protocol.enum.motionpredictionhints|
  |`TriggerAnimation`|`158`|protocol.enum.triggeranimation|
  |`CameraShake`|`159`|protocol.enum.camerashake|
  |`PlayerFogSetting`|`160`|protocol.enum.playerfogsetting|
  |`CorrectPlayerMovePredictionPacket`|`161`|protocol.enum.correctplayermovepredictionpacket|
  |`ItemComponentPacket`|`162`|protocol.enum.itemcomponentpacket|
  |`FilterTextPacket`|`163`|protocol.enum.filtertextpacket|
  |`ClientBoundDebugRendererPacket`|`164`|protocol.enum.clientbounddebugrendererpacket|
  |`SyncActorProperty`|`165`|protocol.enum.syncactorproperty|
  |`AddVolumeEntityPacket`|`166`|protocol.enum.addvolumeentitypacket|
  |`RemoveVolumeEntityPacket`|`167`|protocol.enum.removevolumeentitypacket|
  |`SimulationTypePacket`|`168`|protocol.enum.simulationtypepacket|
  |`NpcDialoguePacket`|`169`|protocol.enum.npcdialoguepacket|
  |`EduUriResourcePacket`|`170`|protocol.enum.eduuriresourcepacket|
  |`CreatePhotoPacket`|`171`|protocol.enum.createphotopacket|
  |`UpdateSubChunkBlocks`|`172`|protocol.enum.updatesubchunkblocks|
  |`PhotoInfoRequest_DEPRECATED`|`173`|protocol.enum.photoinforequest_deprecated|
  |`SubChunkPacket`|`174`|protocol.enum.subchunkpacket|
  |`SubChunkRequestPacket`|`175`|protocol.enum.subchunkrequestpacket|
  |`PlayerStartItemCooldown`|`176`|protocol.enum.playerstartitemcooldown|
  |`ScriptMessagePacket`|`177`|protocol.enum.scriptmessagepacket|
  |`CodeBuilderSourcePacket`|`178`|protocol.enum.codebuildersourcepacket|
  |`TickingAreasLoadStatus`|`179`|protocol.enum.tickingareasloadstatus|
  |`DimensionDataPacket`|`180`|protocol.enum.dimensiondatapacket|
  |`AgentAction`|`181`|protocol.enum.agentaction|
  |`ChangeMobProperty`|`182`|protocol.enum.changemobproperty|
  |`LessonProgressPacket`|`183`|protocol.enum.lessonprogresspacket|
  |`RequestAbilityPacket`|`184`|protocol.enum.requestabilitypacket|
  |`RequestPermissionsPacket`|`185`|protocol.enum.requestpermissionspacket|
  |`ToastRequest`|`186`|protocol.enum.toastrequest|
  |`UpdateAbilitiesPacket`|`187`|protocol.enum.updateabilitiespacket|
  |`UpdateAdventureSettingsPacket`|`188`|protocol.enum.updateadventuresettingspacket|
  |`DeathInfo`|`189`|protocol.enum.deathinfo|
  |`EditorNetworkPacket`|`190`|protocol.enum.editornetworkpacket|
  |`FeatureRegistryPacket`|`191`|protocol.enum.featureregistrypacket|
  |`ServerStats`|`192`|protocol.enum.serverstats|
  |`RequestNetworkSettings`|`193`|protocol.enum.requestnetworksettings|
  |`GameTestRequestPacket`|`194`|protocol.enum.gametestrequestpacket|
  |`GameTestResultsPacket`|`195`|protocol.enum.gametestresultspacket|
  |`PlayerClientInputPermissions`|`196`|protocol.enum.playerclientinputpermissions|
  |`ClientCheatAbilityPacket_Deprecated`|`197`|protocol.enum.clientcheatabilitypacket_deprecated|
  |`CameraPresets`|`198`|protocol.enum.camerapresets|
  |`UnlockedRecipes`|`199`|protocol.enum.unlockedrecipes|
  |`CameraInstruction`|`300`|protocol.enum.camerainstruction|
  |`CompressedBiomeDefinitionList`|`301`|protocol.enum.compressedbiomedefinitionlist|
  |`TrimData`|`302`|protocol.enum.trimdata|
  |`OpenSign`|`303`|protocol.enum.opensign|
  |`AgentAnimation`|`304`|protocol.enum.agentanimation|
  |`RefreshEntitlementsPacket`|`305`|protocol.enum.refreshentitlementspacket|
  |`PlayerToggleCrafterSlotRequestPacket`|`306`|protocol.enum.playertogglecrafterslotrequestpacket|
  |`SetPlayerInventoryOptions`|`307`|protocol.enum.setplayerinventoryoptions|
  |`SetHudPacket`|`308`|protocol.enum.sethudpacket|
  |`EndId`|`309`|protocol.enum.endid|



////
//// define
Violation context：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.packetviolationwarningpacket.violation_context.description


////

///


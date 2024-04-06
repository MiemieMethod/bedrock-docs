# <!-- md:samp DisconnectPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp DisconnectPacket -->数据包，数字ID是`5`。

## 结构

```viz
digraph "DisconnectPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
6 -> 7
7 -> 8
5 -> 9
9 -> 10

0 [label="DisconnectPacket",comment="name: \"DisconnectPacket\", typeName: \"\", id: 0, branchId: 5, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Reason",comment="name: \"Reason\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Connection::DisconnectFailReason\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Skip Message",comment="name: \"Skip Message\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Skip Message'",shape=note,comment="name: \"Dependency on 'Skip Message'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="Message",comment="name: \"Message\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 9, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
10 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;8;10}

}

```

## 字段

```title='DisconnectPacket'
[reason][skip_message][dependency_on_'skip_message']
```

/// html | div.result
//// define
Reason：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`0`||
  |`CantConnectNoInternet`|`1`||
  |`NoPermissions`|`2`||
  |`UnrecoverableError`|`3`||
  |`ThirdPartyBlocked`|`4`||
  |`ThirdPartyNoInternet`|`5`||
  |`ThirdPartyBadIP`|`6`||
  |`ThirdPartyNoServerOrServerLocked`|`7`||
  |`VersionMismatch`|`8`||
  |`SkinIssue`|`9`||
  |`InviteSessionNotFound`|`10`||
  |`EduLevelSettingsMissing`|`11`||
  |`LocalServerNotFound`|`12`||
  |`LegacyDisconnect`|`13`||
  |`UserLeaveGameAttempted`|`14`||
  |`PlatformLockedSkinsError`|`15`||
  |`RealmsWorldUnassigned`|`16`||
  |`RealmsServerCantConnect`|`17`||
  |`RealmsServerHidden`|`18`||
  |`RealmsServerDisabledBeta`|`19`||
  |`RealmsServerDisabled`|`20`||
  |`CrossPlatformDisabled`|`21`||
  |`CantConnect`|`22`||
  |`SessionNotFound`|`23`||
  |`ClientSettingsIncompatibleWithServer`|`24`||
  |`ServerFull`|`25`||
  |`InvalidPlatformSkin`|`26`||
  |`EditionVersionMismatch`|`27`||
  |`EditionMismatch`|`28`||
  |`LevelNewerThanExeVersion`|`29`||
  |`NoFailOccurred`|`30`||
  |`BannedSkin`|`31`||
  |`Timeout`|`32`||
  |`ServerNotFound`|`33`||
  |`OutdatedServer`|`34`||
  |`OutdatedClient`|`35`||
  |`NoPremiumPlatform`|`36`||
  |`MultiplayerDisabled`|`37`||
  |`NoWiFi`|`38`||
  |`WorldCorruption`|`39`||
  |`NoReason`|`40`||
  |`Disconnected`|`41`||
  |`InvalidPlayer`|`42`||
  |`LoggedInOtherLocation`|`43`||
  |`ServerIdConflict`|`44`||
  |`NotAllowed`|`45`||
  |`NotAuthenticated`|`46`||
  |`InvalidTenant`|`47`||
  |`UnknownPacket`|`48`||
  |`UnexpectedPacket`|`49`||
  |`InvalidCommandRequestPacket`|`50`||
  |`HostSuspended`|`51`||
  |`LoginPacketNoRequest`|`52`||
  |`LoginPacketNoCert`|`53`||
  |`MissingClient`|`54`||
  |`Kicked`|`55`||
  |`KickedForExploit`|`56`||
  |`KickedForIdle`|`57`||
  |`ResourcePackProblem`|`58`||
  |`IncompatiblePack`|`59`||
  |`OutOfStorage`|`60`||
  |`InvalidLevel`|`61`||
  |`DisconnectPacket_DEPRECATED`|`62`||
  |`BlockMismatch`|`63`||
  |`InvalidHeights`|`64`||
  |`InvalidWidths`|`65`||
  |`ConnectionLost`|`66`||
  |`ZombieConnection`|`67`||
  |`Shutdown`|`68`||
  |`ReasonNotSet_DEPRECATED`|`69`||
  |`LoadingStateTimeout`|`70`||
  |`ResourcePackLoadingFailed`|`71`||
  |`SearchingForSessionLoadingScreenFailed`|`72`||
  |`NetherNetProtocolVersion`|`73`||
  |`SubsystemStatusError`|`74`||
  |`EmptyAuthFromDiscovery`|`75`||
  |`EmptyUrlFromDiscovery`|`76`||
  |`ExpiredAuthFromDiscovery`|`77`||
  |`UnknownSignalServiceSignInFailure`|`78`||
  |`XBLJoinLobbyFailure`|`79`||
  |`UnspecifiedClientInstanceDisconnection`|`80`||
  |`NetherNetSessionNotFound`|`81`||
  |`NetherNetCreatePeerConnection`|`82`||
  |`NetherNetICE`|`83`||
  |`NetherNetConnectRequest`|`84`||
  |`NetherNetConnectResponse`|`85`||
  |`NetherNetNegotiationTimeout`|`86`||
  |`NetherNetInactivityTimeout`|`87`||
  |`StaleConnectionBeingReplaced`|`88`||
  |`RealmsSessionNotFound`|`89`||
  |`BadPacket`|`90`||
  |`NetherNetFailedToCreateOffer`|`91`||
  |`NetherNetFailedToCreateAnswer`|`92`||
  |`NetherNetFailedToSetLocalDescription`|`93`||
  |`NetherNetFailedToSetRemoteDescription`|`94`||
  |`NetherNetNegotiationTimeoutWaitingForResponse`|`95`||
  |`NetherNetNegotiationTimeoutWaitingForAccept`|`96`||
  |`NetherNetIncomingConnectionIgnored`|`97`||
  |`NetherNetSignalingParsingFailure`|`98`||
  |`NetherNetSignalingUnknownError`|`99`||
  |`NetherNetSignalingUnicastDeliveryFailed`|`100`||
  |`NetherNetSignalingBroadcastDeliveryFailed`|`101`||
  |`NetherNetSignalingGenericDeliveryFailed`|`102`||
  |`EditorMismatchEditorWorld`|`103`||
  |`EditorMismatchVanillaWorld`|`104`||
  |`WorldTransferNotPrimaryClient`|`105`||
  |`RequestServerShutdown`|`106`||
  |`ClientGameSetupCancelled`|`107`||
  |`ClientGameSetupFailed`|`108`||



////
//// define
Skip Message：<!-- md:samp bool -->

- 基本类型。


////
> 依赖于`Skip Message`

///// tab | `Skip Message`如果为`0`
```title='if (0)'
[message]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


///////

//////

/////

///// tab | `Skip Message`如果为`1`
////// define
if (1)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///


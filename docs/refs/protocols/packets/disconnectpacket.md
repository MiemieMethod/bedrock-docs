# <!-- md:samp DisconnectPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp DisconnectPacket -->数据包，数字ID是`5`。该数据包用于protocol.packet.disconnectpacket.description

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
6 -> 9
9 -> 10
5 -> 11
11 -> 12

0 [label="DisconnectPacket",comment="name: \"DisconnectPacket\", typeName: \"\", id: 0, branchId: 5, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Reason",comment="name: \"Reason\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Skip Message",comment="name: \"Skip Message\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Skip Message'",shape=note,comment="name: \"Dependency on 'Skip Message'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="Message",comment="name: \"Message\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Filtered Message",comment="name: \"Filtered Message\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 11, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
12 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;8;10;12}

}

```

## 字段

```title='DisconnectPacket'
[reason][skip_message][dependency_on_skip_message]
```

/// html | div.result
//// define
Reason：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.disconnectpacket.reason.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`0`|protocol.enum.unknown|
  |`CantConnectNoInternet`|`1`|protocol.enum.cantconnectnointernet|
  |`NoPermissions`|`2`|protocol.enum.nopermissions|
  |`UnrecoverableError`|`3`|protocol.enum.unrecoverableerror|
  |`ThirdPartyBlocked`|`4`|protocol.enum.thirdpartyblocked|
  |`ThirdPartyNoInternet`|`5`|protocol.enum.thirdpartynointernet|
  |`ThirdPartyBadIP`|`6`|protocol.enum.thirdpartybadip|
  |`ThirdPartyNoServerOrServerLocked`|`7`|protocol.enum.thirdpartynoserverorserverlocked|
  |`VersionMismatch`|`8`|protocol.enum.versionmismatch|
  |`SkinIssue`|`9`|protocol.enum.skinissue|
  |`InviteSessionNotFound`|`10`|protocol.enum.invitesessionnotfound|
  |`EduLevelSettingsMissing`|`11`|protocol.enum.edulevelsettingsmissing|
  |`LocalServerNotFound`|`12`|protocol.enum.localservernotfound|
  |`LegacyDisconnect`|`13`|protocol.enum.legacydisconnect|
  |`UserLeaveGameAttempted`|`14`|protocol.enum.userleavegameattempted|
  |`PlatformLockedSkinsError`|`15`|protocol.enum.platformlockedskinserror|
  |`RealmsWorldUnassigned`|`16`|protocol.enum.realmsworldunassigned|
  |`RealmsServerCantConnect`|`17`|protocol.enum.realmsservercantconnect|
  |`RealmsServerHidden`|`18`|protocol.enum.realmsserverhidden|
  |`RealmsServerDisabledBeta`|`19`|protocol.enum.realmsserverdisabledbeta|
  |`RealmsServerDisabled`|`20`|protocol.enum.realmsserverdisabled|
  |`CrossPlatformDisabled`|`21`|protocol.enum.crossplatformdisabled|
  |`CantConnect`|`22`|protocol.enum.cantconnect|
  |`SessionNotFound`|`23`|protocol.enum.sessionnotfound|
  |`ClientSettingsIncompatibleWithServer`|`24`|protocol.enum.clientsettingsincompatiblewithserver|
  |`ServerFull`|`25`|protocol.enum.serverfull|
  |`InvalidPlatformSkin`|`26`|protocol.enum.invalidplatformskin|
  |`EditionVersionMismatch`|`27`|protocol.enum.editionversionmismatch|
  |`EditionMismatch`|`28`|protocol.enum.editionmismatch|
  |`LevelNewerThanExeVersion`|`29`|protocol.enum.levelnewerthanexeversion|
  |`NoFailOccurred`|`30`|protocol.enum.nofailoccurred|
  |`BannedSkin`|`31`|protocol.enum.bannedskin|
  |`Timeout`|`32`|protocol.enum.timeout|
  |`ServerNotFound`|`33`|protocol.enum.servernotfound|
  |`OutdatedServer`|`34`|protocol.enum.outdatedserver|
  |`OutdatedClient`|`35`|protocol.enum.outdatedclient|
  |`NoPremiumPlatform`|`36`|protocol.enum.nopremiumplatform|
  |`MultiplayerDisabled`|`37`|protocol.enum.multiplayerdisabled|
  |`NoWiFi`|`38`|protocol.enum.nowifi|
  |`WorldCorruption`|`39`|protocol.enum.worldcorruption|
  |`NoReason`|`40`|protocol.enum.noreason|
  |`Disconnected`|`41`|protocol.enum.disconnected|
  |`InvalidPlayer`|`42`|protocol.enum.invalidplayer|
  |`LoggedInOtherLocation`|`43`|protocol.enum.loggedinotherlocation|
  |`ServerIdConflict`|`44`|protocol.enum.serveridconflict|
  |`NotAllowed`|`45`|protocol.enum.notallowed|
  |`NotAuthenticated`|`46`|protocol.enum.notauthenticated|
  |`InvalidTenant`|`47`|protocol.enum.invalidtenant|
  |`UnknownPacket`|`48`|protocol.enum.unknownpacket|
  |`UnexpectedPacket`|`49`|protocol.enum.unexpectedpacket|
  |`InvalidCommandRequestPacket`|`50`|protocol.enum.invalidcommandrequestpacket|
  |`HostSuspended`|`51`|protocol.enum.hostsuspended|
  |`LoginPacketNoRequest`|`52`|protocol.enum.loginpacketnorequest|
  |`LoginPacketNoCert`|`53`|protocol.enum.loginpacketnocert|
  |`MissingClient`|`54`|protocol.enum.missingclient|
  |`Kicked`|`55`|protocol.enum.kicked|
  |`KickedForExploit`|`56`|protocol.enum.kickedforexploit|
  |`KickedForIdle`|`57`|protocol.enum.kickedforidle|
  |`ResourcePackProblem`|`58`|protocol.enum.resourcepackproblem|
  |`IncompatiblePack`|`59`|protocol.enum.incompatiblepack|
  |`OutOfStorage`|`60`|protocol.enum.outofstorage|
  |`InvalidLevel`|`61`|protocol.enum.invalidlevel|
  |`DisconnectPacket_DEPRECATED`|`62`|protocol.enum.disconnectpacket_deprecated|
  |`BlockMismatch`|`63`|protocol.enum.blockmismatch|
  |`InvalidHeights`|`64`|protocol.enum.invalidheights|
  |`InvalidWidths`|`65`|protocol.enum.invalidwidths|
  |`ConnectionLost`|`66`|protocol.enum.connectionlost|
  |`ZombieConnection`|`67`|protocol.enum.zombieconnection|
  |`Shutdown`|`68`|protocol.enum.shutdown|
  |`ReasonNotSet_DEPRECATED`|`69`|protocol.enum.reasonnotset_deprecated|
  |`LoadingStateTimeout`|`70`|protocol.enum.loadingstatetimeout|
  |`ResourcePackLoadingFailed`|`71`|protocol.enum.resourcepackloadingfailed|
  |`SearchingForSessionLoadingScreenFailed`|`72`|protocol.enum.searchingforsessionloadingscreenfailed|
  |`NetherNetProtocolVersion`|`73`|protocol.enum.nethernetprotocolversion|
  |`SubsystemStatusError`|`74`|protocol.enum.subsystemstatuserror|
  |`EmptyAuthFromDiscovery`|`75`|protocol.enum.emptyauthfromdiscovery|
  |`EmptyUrlFromDiscovery`|`76`|protocol.enum.emptyurlfromdiscovery|
  |`ExpiredAuthFromDiscovery`|`77`|protocol.enum.expiredauthfromdiscovery|
  |`UnknownSignalServiceSignInFailure`|`78`|protocol.enum.unknownsignalservicesigninfailure|
  |`XBLJoinLobbyFailure`|`79`|protocol.enum.xbljoinlobbyfailure|
  |`UnspecifiedClientInstanceDisconnection`|`80`|protocol.enum.unspecifiedclientinstancedisconnection|
  |`NetherNetSessionNotFound`|`81`|protocol.enum.nethernetsessionnotfound|
  |`NetherNetCreatePeerConnection`|`82`|protocol.enum.nethernetcreatepeerconnection|
  |`NetherNetICE`|`83`|protocol.enum.nethernetice|
  |`NetherNetConnectRequest`|`84`|protocol.enum.nethernetconnectrequest|
  |`NetherNetConnectResponse`|`85`|protocol.enum.nethernetconnectresponse|
  |`NetherNetNegotiationTimeout`|`86`|protocol.enum.nethernetnegotiationtimeout|
  |`NetherNetInactivityTimeout`|`87`|protocol.enum.nethernetinactivitytimeout|
  |`StaleConnectionBeingReplaced`|`88`|protocol.enum.staleconnectionbeingreplaced|
  |`RealmsSessionNotFound_DEPRECATED`|`89`|protocol.enum.realmssessionnotfound_deprecated|
  |`BadPacket`|`90`|protocol.enum.badpacket|
  |`NetherNetFailedToCreateOffer`|`91`|protocol.enum.nethernetfailedtocreateoffer|
  |`NetherNetFailedToCreateAnswer`|`92`|protocol.enum.nethernetfailedtocreateanswer|
  |`NetherNetFailedToSetLocalDescription`|`93`|protocol.enum.nethernetfailedtosetlocaldescription|
  |`NetherNetFailedToSetRemoteDescription`|`94`|protocol.enum.nethernetfailedtosetremotedescription|
  |`NetherNetNegotiationTimeoutWaitingForResponse`|`95`|protocol.enum.nethernetnegotiationtimeoutwaitingforresponse|
  |`NetherNetNegotiationTimeoutWaitingForAccept`|`96`|protocol.enum.nethernetnegotiationtimeoutwaitingforaccept|
  |`NetherNetIncomingConnectionIgnored`|`97`|protocol.enum.nethernetincomingconnectionignored|
  |`NetherNetSignalingParsingFailure`|`98`|protocol.enum.nethernetsignalingparsingfailure|
  |`NetherNetSignalingUnknownError`|`99`|protocol.enum.nethernetsignalingunknownerror|
  |`NetherNetSignalingUnicastDeliveryFailed`|`100`|protocol.enum.nethernetsignalingunicastdeliveryfailed|
  |`NetherNetSignalingBroadcastDeliveryFailed`|`101`|protocol.enum.nethernetsignalingbroadcastdeliveryfailed|
  |`NetherNetSignalingGenericDeliveryFailed`|`102`|protocol.enum.nethernetsignalinggenericdeliveryfailed|
  |`EditorMismatchEditorWorld`|`103`|protocol.enum.editormismatcheditorworld|
  |`EditorMismatchVanillaWorld`|`104`|protocol.enum.editormismatchvanillaworld|
  |`WorldTransferNotPrimaryClient`|`105`|protocol.enum.worldtransfernotprimaryclient|
  |`RequestServerShutdown`|`106`|protocol.enum.requestservershutdown|
  |`ClientGameSetupCancelled`|`107`|protocol.enum.clientgamesetupcancelled|
  |`ClientGameSetupFailed`|`108`|protocol.enum.clientgamesetupfailed|
  |`NoVenue`|`109`|protocol.enum.novenue|
  |`NetherNetSignalingSigninFailed`|`110`|protocol.enum.nethernetsignalingsigninfailed|
  |`SessionAccessDenied`|`111`|protocol.enum.sessionaccessdenied|
  |`ServiceSigninIssue`|`112`|protocol.enum.servicesigninissue|
  |`NetherNetNoSignalingChannel`|`113`|protocol.enum.nethernetnosignalingchannel|
  |`NetherNetNotLoggedIn`|`114`|protocol.enum.nethernetnotloggedin|
  |`NetherNetClientSignalingError`|`115`|protocol.enum.nethernetclientsignalingerror|
  |`SubClientLoginDisabled`|`116`|protocol.enum.subclientlogindisabled|
  |`DeepLinkTryingToOpenDemoWorldWhileSignedIn`|`117`|protocol.enum.deeplinktryingtoopendemoworldwhilesignedin|



////
//// define
Skip Message：<!-- md:samp bool -->

- 基本类型。protocol.packet.disconnectpacket.skip_message.description


////
> 依赖于`Skip Message`

///// tab | `Skip Message`如果为`0`
```title='if (0)'
[message][filtered_message]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.disconnectpacket.dependency_on_skip_message.if_0.message.description


///////
/////// define
Filtered Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.disconnectpacket.dependency_on_skip_message.if_0.filtered_message.description


///////

//////

/////

///// tab | `Skip Message`如果为`1`
////// define
if (1)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///


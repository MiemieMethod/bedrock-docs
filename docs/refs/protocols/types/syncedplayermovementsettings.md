# <!-- md:samp SyncedPlayerMovementSettings -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp SyncedPlayerMovementSettings -->类型。该类型用于protocol.type.syncedplayermovementsettings.description

## 结构

```viz
digraph "SyncedPlayerMovementSettings" {
rankdir = LR
155
155 -> 156
156 -> 157
155 -> 158
158 -> 159
155 -> 160
160 -> 161

155 [label="SyncedPlayerMovementSettings",comment="name: \"SyncedPlayerMovementSettings\", typeName: \"\", id: 155, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
156 [label="Authority Mode",comment="name: \"Authority Mode\", typeName: \"\", id: 156, branchId: 0, recurseId: -1, attributes: 0, notes: \"See explanation of modes in enum table\""];
157 [label="varint",comment="name: \"varint\", typeName: \"\", id: 157, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
158 [label="Rewind History Size",comment="name: \"Rewind History Size\", typeName: \"\", id: 158, branchId: 0, recurseId: -1, attributes: 0, notes: \"When using server authoritative movement mode, this determines the number of ticks the client keeps in history for use in processing corrections. Should at least account for the largest expected round trip latency. In Bedrock this is 40 ticks.\""];
159 [label="varint",comment="name: \"varint\", typeName: \"\", id: 159, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
160 [label="Server Authoritative Block Breaking",comment="name: \"Server Authoritative Block Breaking\", typeName: \"\", id: 160, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
161 [label="bool",comment="name: \"bool\", typeName: \"\", id: 161, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;157;159;161}

}

```

## 字段

```title='SyncedPlayerMovementSettings'
[authority_mode][rewind_history_size][server_authoritative_block_breaking]
```

/// html | div.result
//// define
Authority Mode：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.syncedplayermovementsettings.authority_mode.descriptionSee explanation of modes in enum table枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`LegacyClientAuthoritativeV1`|`0`|protocol.enum.legacyclientauthoritativev1|
  |`ClientAuthoritativeV2`|`1`|protocol.enum.clientauthoritativev2|
  |`ServerAuthoritativeV3`|`2`|protocol.enum.serverauthoritativev3|



////
//// define
Rewind History Size：<!-- md:samp varint -->

- 基本类型。protocol.type.syncedplayermovementsettings.rewind_history_size.descriptionWhen using server authoritative movement mode, this determines the number of ticks the client keeps in history for use in processing corrections. Should at least account for the largest expected round trip latency. In Bedrock this is 40 ticks.


////
//// define
Server Authoritative Block Breaking：<!-- md:samp bool -->

- 基本类型。protocol.type.syncedplayermovementsettings.server_authoritative_block_breaking.description


////

///


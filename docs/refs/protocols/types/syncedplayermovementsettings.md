# <!-- md:samp SyncedPlayerMovementSettings -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp SyncedPlayerMovementSettings -->类型。该类型用于protocol.type.syncedplayermovementsettings.description

## 结构

```viz
digraph "SyncedPlayerMovementSettings" {
rankdir = LR
149
149 -> 150
150 -> 151
149 -> 152
152 -> 153
149 -> 154
154 -> 155

149 [label="SyncedPlayerMovementSettings",comment="name: \"SyncedPlayerMovementSettings\", typeName: \"\", id: 149, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
150 [label="Authority Mode",comment="name: \"Authority Mode\", typeName: \"\", id: 150, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
151 [label="varint",comment="name: \"varint\", typeName: \"\", id: 151, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
152 [label="Rewind History Size",comment="name: \"Rewind History Size\", typeName: \"\", id: 152, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
153 [label="varint",comment="name: \"varint\", typeName: \"\", id: 153, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
154 [label="Server Authoratative Block Breaking",comment="name: \"Server Authoratative Block Breaking\", typeName: \"\", id: 154, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
155 [label="bool",comment="name: \"bool\", typeName: \"\", id: 155, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;151;153;155}

}

```

## 字段

```title='SyncedPlayerMovementSettings'
[authority_mode][rewind_history_size][server_authoratative_block_breaking]
```

/// html | div.result
//// define
Authority Mode：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.syncedplayermovementsettings.authority_mode.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ClientAuthoritative`|`0`|protocol.enum.clientauthoritative|
  |`ServerAuthoritative`|`1`|protocol.enum.serverauthoritative|
  |`ServerAuthoritativeWithRewind`|`2`|protocol.enum.serverauthoritativewithrewind|



////
//// define
Rewind History Size：<!-- md:samp varint -->

- 基本类型。protocol.type.syncedplayermovementsettings.rewind_history_size.description


////
//// define
Server Authoratative Block Breaking：<!-- md:samp bool -->

- 基本类型。protocol.type.syncedplayermovementsettings.server_authoratative_block_breaking.description


////

///


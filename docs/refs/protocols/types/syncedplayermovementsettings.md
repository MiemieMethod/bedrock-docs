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
156 [label="Authority Mode",comment="name: \"Authority Mode\", typeName: \"\", id: 156, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
157 [label="varint",comment="name: \"varint\", typeName: \"\", id: 157, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
158 [label="Rewind History Size",comment="name: \"Rewind History Size\", typeName: \"\", id: 158, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
159 [label="varint",comment="name: \"varint\", typeName: \"\", id: 159, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
160 [label="Server Authoratative Block Breaking",comment="name: \"Server Authoratative Block Breaking\", typeName: \"\", id: 160, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
161 [label="bool",comment="name: \"bool\", typeName: \"\", id: 161, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;157;159;161}

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


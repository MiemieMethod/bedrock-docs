# <!-- md:samp SyncedPlayerMovementSettings -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SyncedPlayerMovementSettings -->类型。

## 结构

```viz
digraph "SyncedPlayerMovementSettings" {
rankdir = LR
147
147 -> 148
148 -> 149
147 -> 150
150 -> 151
147 -> 152
152 -> 153

147 [label="SyncedPlayerMovementSettings",comment="name: \"SyncedPlayerMovementSettings\", typeName: \"\", id: 147, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
148 [label="Authority Mode",comment="name: \"Authority Mode\", typeName: \"\", id: 148, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ServerAuthMovementMode\""];
149 [label="byte",comment="name: \"byte\", typeName: \"\", id: 149, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
150 [label="Rewind History Size",comment="name: \"Rewind History Size\", typeName: \"\", id: 150, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
151 [label="varint",comment="name: \"varint\", typeName: \"\", id: 151, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
152 [label="Server Authoratative Block Breaking",comment="name: \"Server Authoratative Block Breaking\", typeName: \"\", id: 152, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
153 [label="bool",comment="name: \"bool\", typeName: \"\", id: 153, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;149;151;153}

}

```

## 字段

```title='SyncedPlayerMovementSettings'
[authority_mode][rewind_history_size][server_authoratative_block_breaking]
```

/// html | div.result
//// define
Authority Mode：<!-- md:samp byte -->

- <!-- md:samp byte -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ClientAuthoritative`|`0`||
  |`ServerAuthoritative`|`1`||
  |`ServerAuthoritativeWithRewind`|`2`||



////
//// define
Rewind History Size：<!-- md:samp varint -->

- <!-- md:samp varint -->类型。


////
//// define
Server Authoratative Block Breaking：<!-- md:samp bool -->

- <!-- md:samp bool -->类型。


////

///


# <!-- md:samp PlayStatusPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp PlayStatusPacket -->数据包，数字ID是`2`。该数据包用于protocol.packet.playstatuspacket.description

## 结构

```viz
digraph "PlayStatusPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="PlayStatusPacket",comment="name: \"PlayStatusPacket\", typeName: \"\", id: 0, branchId: 2, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Status",comment="name: \"Status\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="big endian int",comment="name: \"big endian int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='PlayStatusPacket'
[status]
```

/// html | div.result
//// define
Status：<!-- md:samp big endian int -->

- 基本类型枚举。protocol.packet.playstatuspacket.status.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`LoginSuccess`|`0`|protocol.enum.loginsuccess|
  |`LoginFailed_ClientOld`|`1`|protocol.enum.loginfailed_clientold|
  |`LoginFailed_ServerOld`|`2`|protocol.enum.loginfailed_serverold|
  |`PlayerSpawn`|`3`|protocol.enum.playerspawn|
  |`LoginFailed_InvalidTenant`|`4`|protocol.enum.loginfailed_invalidtenant|
  |`LoginFailed_EditionMismatchEduToVanilla`|`5`|protocol.enum.loginfailed_editionmismatchedutovanilla|
  |`LoginFailed_EditionMismatchVanillaToEdu`|`6`|protocol.enum.loginfailed_editionmismatchvanillatoedu|
  |`LoginFailed_ServerFullSubClient`|`7`|protocol.enum.loginfailed_serverfullsubclient|
  |`LoginFailed_EditorMismatchEditorToVanilla`|`8`|protocol.enum.loginfailed_editormismatcheditortovanilla|
  |`LoginFailed_EditorMismatchVanillaToEditor`|`9`|protocol.enum.loginfailed_editormismatchvanillatoeditor|



////

///


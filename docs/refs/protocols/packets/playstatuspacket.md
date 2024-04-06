# <!-- md:samp PlayStatusPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayStatusPacket -->数据包，数字ID是`2`。

## 结构

```viz
digraph "PlayStatusPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="PlayStatusPacket",comment="name: \"PlayStatusPacket\", typeName: \"\", id: 0, branchId: 2, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Status",comment="name: \"Status\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayStatus\""];
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

- <!-- md:samp big endian int -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`LoginSuccess`|`0`||
  |`LoginFailed_ClientOld`|`1`||
  |`LoginFailed_ServerOld`|`2`||
  |`PlayerSpawn`|`3`||
  |`LoginFailed_InvalidTenant`|`4`||
  |`LoginFailed_EditionMismatchEduToVanilla`|`5`||
  |`LoginFailed_EditionMismatchVanillaToEdu`|`6`||
  |`LoginFailed_ServerFullSubClient`|`7`||
  |`LoginFailed_EditorMismatchEditorToVanilla`|`8`||
  |`LoginFailed_EditorMismatchVanillaToEditor`|`9`||



////

///


# <!-- md:samp SetMovementAuthorityPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp SetMovementAuthorityPacket -->数据包，数字ID是`319`。该数据包用于protocol.packet.setmovementauthoritypacket.description

## 结构

```viz
digraph "SetMovementAuthorityPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetMovementAuthorityPacket",comment="name: \"SetMovementAuthorityPacket\", typeName: \"\", id: 0, branchId: 319, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="NewAuthMovementMode",comment="name: \"NewAuthMovementMode\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetMovementAuthorityPacket'
[newauthmovementmode]
```

/// html | div.result
//// define
NewAuthMovementMode：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.setmovementauthoritypacket.newauthmovementmode.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`LegacyClientAuthoritativeV1`|`0`|protocol.enum.legacyclientauthoritativev1|
  |`ClientAuthoritativeV2`|`1`|protocol.enum.clientauthoritativev2|
  |`ServerAuthoritativeV3`|`2`|protocol.enum.serverauthoritativev3|



////

///


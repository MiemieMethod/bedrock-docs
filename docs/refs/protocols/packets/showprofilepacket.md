# <!-- md:samp ShowProfilePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ShowProfilePacket -->数据包，数字ID是`104`。该数据包用于protocol.packet.showprofilepacket.description

## 结构

```viz
digraph "ShowProfilePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="ShowProfilePacket",comment="name: \"ShowProfilePacket\", typeName: \"\", id: 0, branchId: 104, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Player XUID",comment="name: \"Player XUID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='ShowProfilePacket'
[player_xuid]
```

/// html | div.result
//// define
Player XUID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.showprofilepacket.player_xuid.description


////

///


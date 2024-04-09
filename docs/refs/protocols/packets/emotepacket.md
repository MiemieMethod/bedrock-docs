# <!-- md:samp EmotePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp EmotePacket -->数据包，数字ID是`138`。该数据包用于protocol.packet.emotepacket.description

## 结构

```viz
digraph "EmotePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10

0 [label="EmotePacket",comment="name: \"EmotePacket\", typeName: \"\", id: 0, branchId: 138, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Actor Runtime Id",comment="name: \"Actor Runtime Id\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Emote Id",comment="name: \"Emote Id\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Xuid",comment="name: \"Xuid\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="PlatformId",comment="name: \"PlatformId\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Flags",comment="name: \"Flags\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: EmotePacket::Flags\""];
10 [label="byte",comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='EmotePacket'
[actor_runtime_id][emote_id][xuid][platformid][flags]
```

/// html | div.result
//// define
Actor Runtime Id：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.emotepacket.actor_runtime_id.description


////
//// define
Emote Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.emotepacket.emote_id.description


////
//// define
Xuid：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.emotepacket.xuid.description


////
//// define
PlatformId：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.emotepacket.platformid.description


////
//// define
Flags：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.emotepacket.flags.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`SERVER_SIDE`|`1 << 0`|protocol.enum.server_side|
  |`MUTE_EMOTE_CHAT`|`1 << 1`|protocol.enum.mute_emote_chat|



////

///


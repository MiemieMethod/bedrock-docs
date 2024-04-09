# <!-- md:samp NpcDialoguePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NpcDialoguePacket -->数据包，数字ID是`169`。该数据包用于protocol.packet.npcdialoguepacket.description

## 结构

```viz
digraph "NpcDialoguePacket" {
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
0 -> 11
11 -> 12

0 [label="NpcDialoguePacket",comment="name: \"NpcDialoguePacket\", typeName: \"\", id: 0, branchId: 169, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Npc Id Raw Id",comment="name: \"Npc Id Raw Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"The ActorUniqueID of the NPC being remote fired\""];
2 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Npc Dialogue Action Type",comment="name: \"Npc Dialogue Action Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: NpcDialoguePacket::NpcDialogueActionType\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dialogue",comment="name: \"Dialogue\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"The text to be displayed to the client\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Scene Name",comment="name: \"Scene Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"The scene the data has been pulled from for the client to reference\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Npc Name",comment="name: \"Npc Name\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"The name of the NPC to be displayed to the client\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Action JSON",comment="name: \"Action JSON\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"The JSON string of the buttons/actions the server can perform. The server is still authoritative on what actions can be performed\""];
12 [label="string",comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12}

}

```

## 字段

```title='NpcDialoguePacket'
[npc_id_raw_id][npc_dialogue_action_type][dialogue][scene_name][npc_name][action_json]
```

/// html | div.result
//// define
Npc Id Raw Id：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.packet.npcdialoguepacket.npc_id_raw_id.descriptionThe ActorUniqueID of the NPC being remote fired


////
//// define
Npc Dialogue Action Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.npcdialoguepacket.npc_dialogue_action_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Open`|`0`|protocol.enum.open|
  |`Close`|`1`|protocol.enum.close|



////
//// define
Dialogue：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.npcdialoguepacket.dialogue.descriptionThe text to be displayed to the client


////
//// define
Scene Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.npcdialoguepacket.scene_name.descriptionThe scene the data has been pulled from for the client to reference


////
//// define
Npc Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.npcdialoguepacket.npc_name.descriptionThe 'name' of the NPC to be displayed to the client


////
//// define
Action JSON：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.npcdialoguepacket.action_json.descriptionThe JSON string of the buttons/actions the server can perform. The server is still authoritative on what actions can be performed


////

///


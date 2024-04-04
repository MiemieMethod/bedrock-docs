# <!-- md:samp NpcDialoguePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NpcDialoguePacket -->数据包，数字ID是`169`。

## 结构

```dot
digraph NpcDialoguePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		12	[comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"NpcDialoguePacket\", typeName: \"\", id: 0, branchId: 169, recurseId: -1, attributes: 0, notes: \"\"",
		label=NpcDialoguePacket];
	1	[comment="name: \"Npc Id Raw Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"The ActorUniqueID of the NPC being \
remote fired\"",
		label="Npc Id Raw Id"];
	0 -> 1;
	3	[comment="name: \"Npc Dialogue Action Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: NpcDialoguePacket::\
NpcDialogueActionType\"",
		label="Npc Dialogue Action Type"];
	0 -> 3;
	5	[comment="name: \"Dialogue\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"The text to be displayed to the client\"",
		label=Dialogue];
	0 -> 5;
	7	[comment="name: \"Scene Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"The scene the data has been pulled from \
for the client to reference\"",
		label="Scene Name"];
	0 -> 7;
	9	[comment="name: \"Npc Name\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"The name of the NPC to be displayed to \
the client\"",
		label="Npc Name"];
	0 -> 9;
	11	[comment="name: \"Action JSON\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"The JSON string of the buttons/actions \
the server can perform. The server is still authoritative on what actions can be performed\"",
		label="Action JSON"];
	0 -> 11;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
}

```

## 字段

/// define
NpcDialoguePacket

Npc Id Raw Id：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。The ActorUniqueID of the NPC being remote fired

Npc Dialogue Action Type：<!-- md:samp varint -->

- 类型：varint。enumeration: NpcDialoguePacket::NpcDialogueActionType

Dialogue：<!-- md:samp string -->

- 类型：string。The text to be displayed to the client

Scene Name：<!-- md:samp string -->

- 类型：string。The scene the data has been pulled from for the client to reference

Npc Name：<!-- md:samp string -->

- 类型：string。The 'name' of the NPC to be displayed to the client

Action JSON：<!-- md:samp string -->

- 类型：string。The JSON string of the buttons/actions the server can perform. The server is still authoritative on what actions can be performed


///

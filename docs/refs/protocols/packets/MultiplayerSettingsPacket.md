# <!-- md:samp MultiplayerSettingsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MultiplayerSettingsPacket -->数据包，数字ID是`139`。

## 结构

```viz
digraph MultiplayerSettingsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"MultiplayerSettingsPacket\", typeName: \"\", id: 0, branchId: 139, recurseId: -1, attributes: 0, notes: \"\"",
		label=MultiplayerSettingsPacket];
	1	[comment="name: \"Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MultiplayerSettingsPacketType\"",
		label=Type];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
MultiplayerSettingsPacket

Type：<!-- md:samp varint -->

- 类型：varint。enumeration: MultiplayerSettingsPacketType


///

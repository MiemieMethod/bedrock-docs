# <!-- md:samp UpdatePlayerGameTypePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdatePlayerGameTypePacket -->数据包，数字ID是`151`。

## 结构

```dot
digraph UpdatePlayerGameTypePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
	}
	0	[comment="name: \"UpdatePlayerGameTypePacket\", typeName: \"\", id: 0, branchId: 151, recurseId: -1, attributes: 0, notes: \"\"",
		label=UpdatePlayerGameTypePacket];
	1	[comment="name: \"Player game type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GameType\"",
		label="Player game type"];
	0 -> 1;
	3	[comment="name: \"Target player\", typeName: \"ActorUniqueID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target player"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
UpdatePlayerGameTypePacket

Player game type：<!-- md:samp varint -->

- 类型：varint。enumeration: GameType

Target player：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。


///

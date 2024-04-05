# <!-- md:samp SetPlayerGameTypePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetPlayerGameTypePacket -->数据包，数字ID是`62`。

## 结构

```viz
digraph SetPlayerGameTypePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"SetPlayerGameTypePacket\", typeName: \"\", id: 0, branchId: 62, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetPlayerGameTypePacket];
	1	[comment="name: \"Player Game Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GameType\"",
		label="Player Game Type"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SetPlayerGameTypePacket

Player Game Type：<!-- md:samp varint -->

- 类型：varint。enumeration: GameType


///

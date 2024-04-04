# <!-- md:samp GameRulesChangedPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp GameRulesChangedPacket -->数据包，数字ID是`72`。

## 结构

```viz
digraph GameRulesChangedPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"GameRulesChangedPacketData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=GameRulesChangedPacketData];
	}
	0	[comment="name: \"GameRulesChangedPacket\", typeName: \"\", id: 0, branchId: 72, recurseId: -1, attributes: 0, notes: \"\"",
		label=GameRulesChangedPacket];
	1	[comment="name: \"Rules Data\", typeName: \"GameRulesChangedPacketData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Rules Data"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
GameRulesChangedPacket

Rules Data：[<!-- md:samp GameRulesChangedPacketData -->](refs/protocols/types/GameRulesChangedPacketData.md)

- 类型：GameRulesChangedPacketData。


///

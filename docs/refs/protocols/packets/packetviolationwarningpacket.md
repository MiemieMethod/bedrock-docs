# <!-- md:samp PacketViolationWarningPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PacketViolationWarningPacket -->数据包，数字ID是`156`。

## 结构

```viz
digraph PacketViolationWarningPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"PacketViolationWarningPacket\", typeName: \"\", id: 0, branchId: 156, recurseId: -1, attributes: 0, notes: \"\"",
		label=PacketViolationWarningPacket];
	1	[comment="name: \"Violation Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PacketViolationType\"",
		label="Violation Type"];
	0 -> 1;
	3	[comment="name: \"Violation Severity\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PacketViolationSeverity\"",
		label="Violation Severity"];
	0 -> 3;
	5	[comment="name: \"Violating packet id\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MinecraftPacketIds\"",
		label="Violating packet id"];
	0 -> 5;
	7	[comment="name: \"Violation context\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Violation context"];
	0 -> 7;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
PacketViolationWarningPacket

Violation Type：<!-- md:samp varint -->

- 类型：varint。enumeration: PacketViolationType

Violation Severity：<!-- md:samp varint -->

- 类型：varint。enumeration: PacketViolationSeverity

Violating packet id：<!-- md:samp varint -->

- 类型：varint。enumeration: MinecraftPacketIds

Violation context：<!-- md:samp string -->

- 类型：string。


///

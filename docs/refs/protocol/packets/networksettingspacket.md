# <!-- md:samp NetworkSettingsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NetworkSettingsPacket -->数据包，数字ID是`143`。

## 结构

```viz
digraph NetworkSettingsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned short\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		4	[comment="name: \"unsigned short\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		8	[comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		10	[comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
	}
	0	[comment="name: \"NetworkSettingsPacket\", typeName: \"\", id: 0, branchId: 143, recurseId: -1, attributes: 0, notes: \"\"",
		label=NetworkSettingsPacket];
	1	[comment="name: \"Compression Threshold\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Determines the smallest size \
of raw network payload to compress. OTE: 0 is disable compression, 1 is compress everything 1 byte or larger (so everything)\"",
		label="Compression Threshold"];
	0 -> 1;
	3	[comment="name: \"CompressionAlgorithm\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PacketCompressionAlgorithm\"",
		label=CompressionAlgorithm];
	0 -> 3;
	5	[comment="name: \"Client Throttle Enabled\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Client Throttle Enabled"];
	0 -> 5;
	7	[comment="name: \"Client Throttle Threshold\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Client Throttle Threshold"];
	0 -> 7;
	9	[comment="name: \"Client Throttle Scalar\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Client Throttle Scalar"];
	0 -> 9;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
}

```

## 字段

/// define
NetworkSettingsPacket

Compression Threshold：<!-- md:samp unsigned short -->

- 类型：unsigned short。Determines the smallest size of raw network payload to compress. OTE: 0 is disable compression, 1 is compress everything 1 byte or larger (so everything)

CompressionAlgorithm：<!-- md:samp unsigned short -->

- 类型：unsigned short。enumeration: PacketCompressionAlgorithm

Client Throttle Enabled：<!-- md:samp bool -->

- 类型：bool。

Client Throttle Threshold：<!-- md:samp byte -->

- 类型：byte。

Client Throttle Scalar：<!-- md:samp float -->

- 类型：float。


///

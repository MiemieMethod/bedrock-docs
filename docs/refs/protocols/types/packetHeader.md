# <!-- md:samp Packet Header -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp Packet Header -->类型。

## 结构

```viz
digraph "Packet Header" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
	}
	0	[comment="name: \"Packet Header\", typeName: \"\", id: 0, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Packet Header"];
	1	[comment="name: \"Packet ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"The first 10 value bits are the packet \
id, the next 2 value bits are the Sender SubClientID, and the next 2 value bits are the Target SubClientID\"",
		label="Packet ID"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
Packet Header

Packet ID：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。The first 10 value bits are the packet 'id', the next 2 value bits are the Sender SubClientID, and the next 2 value bits are the Target SubClientID


///

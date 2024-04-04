# <!-- md:samp LoginPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LoginPacket -->数据包，数字ID是`1`。

## 结构

```dot
digraph LoginPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"big endian int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="big endian int"];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"LoginPacket\", typeName: \"\", id: 0, branchId: 1, recurseId: -1, attributes: 0, notes: \"\"",
		label=LoginPacket];
	1	[comment="name: \"Client Network Version\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Client Network Version"];
	0 -> 1;
	3	[comment="name: \"Connection Request\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"see @connectionRequest.html#\
diagram@\"",
		label="Connection Request"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
LoginPacket

Client Network Version：<!-- md:samp big endian int -->

- 类型：big endian int。

Connection Request：<!-- md:samp string -->

- 类型：string。see @connectionRequest.html#diagram@


///

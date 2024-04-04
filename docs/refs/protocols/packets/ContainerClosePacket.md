# <!-- md:samp ContainerClosePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ContainerClosePacket -->数据包，数字ID是`47`。

## 结构

```dot
digraph ContainerClosePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"ContainerClosePacket\", typeName: \"\", id: 0, branchId: 47, recurseId: -1, attributes: 0, notes: \"\"",
		label=ContainerClosePacket];
	1	[comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\"",
		label="Container ID"];
	0 -> 1;
	3	[comment="name: \"Server Initiated Close\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"True if the server initiated \
the closing\"",
		label="Server Initiated Close"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
ContainerClosePacket

Container ID：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerID

Server Initiated Close：<!-- md:samp bool -->

- 类型：bool。True if the server initiated the closing


///

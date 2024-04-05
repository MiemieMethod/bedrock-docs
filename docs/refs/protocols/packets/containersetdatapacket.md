# <!-- md:samp ContainerSetDataPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ContainerSetDataPacket -->数据包，数字ID是`51`。

## 结构

```viz
digraph ContainerSetDataPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"ContainerSetDataPacket\", typeName: \"\", id: 0, branchId: 51, recurseId: -1, attributes: 0, notes: \"\"",
		label=ContainerSetDataPacket];
	1	[comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\"",
		label="Container ID"];
	0 -> 1;
	3	[comment="name: \"ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ID];
	0 -> 3;
	5	[comment="name: \"Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
ContainerSetDataPacket

Container ID：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerID

ID：<!-- md:samp varint -->

- 类型：varint。

Value：<!-- md:samp varint -->

- 类型：varint。


///

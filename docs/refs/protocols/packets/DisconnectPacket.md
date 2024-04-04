# <!-- md:samp DisconnectPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp DisconnectPacket -->数据包，数字ID是`5`。

## 结构

```viz
digraph DisconnectPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"[No Data]\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
	}
	0	[comment="name: \"DisconnectPacket\", typeName: \"\", id: 0, branchId: 5, recurseId: -1, attributes: 0, notes: \"\"",
		label=DisconnectPacket];
	1	[comment="name: \"Reason\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Connection::DisconnectFailReason\"",
		label=Reason];
	0 -> 1;
	3	[comment="name: \"Skip Message\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Skip Message"];
	0 -> 3;
	5	[comment="name: \"Dependency on 'Skip Message'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Skip Message'",
		shape=note];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	6	[comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	5 -> 6;
	9	[comment="name: \"if (1)\", typeName: \"\", id: 9, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	5 -> 9;
	7	[comment="name: \"Message\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Message];
	6 -> 7;
	7 -> 8;
	9 -> 10;
}

```

## 字段

/// define
DisconnectPacket

Reason：<!-- md:samp varint -->

- 类型：varint。enumeration: Connection::DisconnectFailReason

Skip Message：<!-- md:samp bool -->

- 类型：bool。

Dependency on 'Skip Message'

//// tab | if (0)
///// define
if (0)

Message：<!-- md:samp string -->

- 类型：string。


/////

////

//// tab | if (1)
///// define
if (1)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////



///

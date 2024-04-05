# <!-- md:samp AnimatePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AnimatePacket -->数据包，数字ID是`44`。

## 结构

```viz
digraph AnimatePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		7	[comment="name: \"[No Data]\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		9	[comment="name: \"[No Data]\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		11	[comment="name: \"[No Data]\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		13	[comment="name: \"[No Data]\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		15	[comment="name: \"[No Data]\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		18	[comment="name: \"float\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		21	[comment="name: \"float\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
	}
	0	[comment="name: \"AnimatePacket\", typeName: \"\", id: 0, branchId: 44, recurseId: -1, attributes: 0, notes: \"\"",
		label=AnimatePacket];
	1	[comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: AnimatePacket::Action\"",
		label=Action];
	0 -> 1;
	3	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 3;
	5	[comment="name: \"Dependency on 'Action'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Action'",
		shape=note];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	6	[comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	5 -> 6;
	8	[comment="name: \"if (1)\", typeName: \"\", id: 8, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	5 -> 8;
	10	[comment="name: \"if (3)\", typeName: \"\", id: 10, branchId: 3, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (3)",
		shape=diamond];
	5 -> 10;
	12	[comment="name: \"if (4)\", typeName: \"\", id: 12, branchId: 4, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (4)",
		shape=diamond];
	5 -> 12;
	14	[comment="name: \"if (5)\", typeName: \"\", id: 14, branchId: 5, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (5)",
		shape=diamond];
	5 -> 14;
	16	[comment="name: \"if (128)\", typeName: \"\", id: 16, branchId: 128, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (128)",
		shape=diamond];
	5 -> 16;
	19	[comment="name: \"if (129)\", typeName: \"\", id: 19, branchId: 129, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (129)",
		shape=diamond];
	5 -> 19;
	6 -> 7;
	8 -> 9;
	10 -> 11;
	12 -> 13;
	14 -> 15;
	17	[comment="name: \"Rowing Time\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Rowing Time"];
	16 -> 17;
	17 -> 18;
	20	[comment="name: \"Rowing Time\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Rowing Time"];
	19 -> 20;
	20 -> 21;
}

```

## 字段

/// define
AnimatePacket

Action：<!-- md:samp varint -->

- 类型：varint。enumeration: AnimatePacket::Action

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Dependency on 'Action'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (3)
///// define
if (3)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (4)
///// define
if (4)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (5)
///// define
if (5)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (128)
///// define
if (128)

Rowing Time：<!-- md:samp float -->

- 类型：float。


/////

////

//// tab | if (129)
///// define
if (129)

Rowing Time：<!-- md:samp float -->

- 类型：float。


/////

////



///

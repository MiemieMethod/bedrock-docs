# <!-- md:samp InteractPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp InteractPacket -->数据包，数字ID是`33`。

## 结构

```viz
digraph InteractPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		7	[comment="name: \"[No Data]\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		10	[comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		12	[comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		14	[comment="name: \"float\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
	}
	0	[comment="name: \"InteractPacket\", typeName: \"\", id: 0, branchId: 33, recurseId: -1, attributes: 0, notes: \"\"",
		label=InteractPacket];
	1	[comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InteractPacket::Action\"",
		label=Action];
	0 -> 1;
	3	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 3;
	5	[comment="name: \"Dependency on 'Action == InteractUpdate || Action == StopRiding'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: \
2, notes: \"\"",
		label="Dependency on 'Action == InteractUpdate || Action == StopRiding'",
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
	6 -> 7;
	9	[comment="name: \"Position X\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Position X"];
	8 -> 9;
	11	[comment="name: \"Position Y\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Position Y"];
	8 -> 11;
	13	[comment="name: \"Position Z\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Position Z"];
	8 -> 13;
	9 -> 10;
	11 -> 12;
	13 -> 14;
}

```

## 字段

/// define
InteractPacket

Action：<!-- md:samp byte -->

- 类型：byte。enumeration: InteractPacket::Action

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Dependency on 'Action == InteractUpdate || Action == StopRiding'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Position X：<!-- md:samp float -->

- 类型：float。

Position Y：<!-- md:samp float -->

- 类型：float。

Position Z：<!-- md:samp float -->

- 类型：float。


/////

////



///

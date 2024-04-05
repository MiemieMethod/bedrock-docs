# <!-- md:samp ContainerOpenPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ContainerOpenPacket -->数据包，数字ID是`46`。

## 结构

```viz
digraph ContainerOpenPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		8	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
	}
	0	[comment="name: \"ContainerOpenPacket\", typeName: \"\", id: 0, branchId: 46, recurseId: -1, attributes: 0, notes: \"\"",
		label=ContainerOpenPacket];
	1	[comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\"",
		label="Container ID"];
	0 -> 1;
	3	[comment="name: \"Container Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerType\"",
		label="Container Type"];
	0 -> 3;
	5	[comment="name: \"Position\", typeName: \"NetworkBlockPosition\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 5;
	7	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	0 -> 7;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
ContainerOpenPacket

Container ID：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerID

Container Type：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerType

Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 类型：ActorUniqueID。


///

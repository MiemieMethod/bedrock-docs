# <!-- md:samp MoveActorDeltaData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MoveActorDeltaData -->类型。

## 结构

```viz
digraph MoveActorDeltaData {
	graph [rankdir=LR];
	{
		graph [rank=max];
		4	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		6	[comment="name: \"unsigned short\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		8	[comment="name: \"float\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		10	[comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		12	[comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		14	[comment="name: \"byte\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		16	[comment="name: \"byte\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		18	[comment="name: \"byte\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	2	[comment="name: \"MoveActorDeltaData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=MoveActorDeltaData];
	3	[comment="name: \"ActorRuntimeID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"The runtime id of \
the actor being moved\"",
		label=ActorRuntimeID];
	2 -> 3;
	5	[comment="name: \"Header\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Header containing 9 1-bit booleans describing \
the rest of the packet. Information provided in supplemental documentation.\"",
		label=Header];
	2 -> 5;
	7	[comment="name: \"New position X\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"If position X bit is true, then \
this will contain the actor's X coordinate\"",
		label="New position X"];
	2 -> 7;
	9	[comment="name: \"New position Y\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"If position Y bit is true, then \
this will contain the actor's Y coordinate\"",
		label="New position Y"];
	2 -> 9;
	11	[comment="name: \"New position Z\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"If position Z bit is true, then \
this will contain the actor's Z coordinate\"",
		label="New position Z"];
	2 -> 11;
	13	[comment="name: \"Rotation X\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"If rotation X bit is true, then this \
will contain the X rotation of the actor\"",
		label="Rotation X"];
	2 -> 13;
	15	[comment="name: \"Rotation Y\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"If rotation Y bit is true, then this \
will contain the Y rotation of the actor\"",
		label="Rotation Y"];
	2 -> 15;
	17	[comment="name: \"Rotation Y Head\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"If rotation Y Head bit is true, \
then this will contain a head rotation of the actor if and only if it's a Mob type\"",
		label="Rotation Y Head"];
	2 -> 17;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 16;
	17 -> 18;
}

```

## 字段

/// define
MoveActorDeltaData

ActorRuntimeID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。The runtime 'id' of the actor being moved

Header：<!-- md:samp unsigned short -->

- 类型：unsigned short。Header containing 9 1-bit booleans describing the rest of the packet. Information prov'id'ed in supplemental documentation.

New position X：<!-- md:samp float -->

- 类型：float。If position X bit is true, then this will contain the actor's X coordinate

New position Y：<!-- md:samp float -->

- 类型：float。If position Y bit is true, then this will contain the actor's Y coordinate

New position Z：<!-- md:samp float -->

- 类型：float。If position Z bit is true, then this will contain the actor's Z coordinate

Rotation X：<!-- md:samp byte -->

- 类型：byte。If rotation X bit is true, then this will contain the X rotation of the actor

Rotation Y：<!-- md:samp byte -->

- 类型：byte。If rotation Y bit is true, then this will contain the Y rotation of the actor

Rotation Y Head：<!-- md:samp byte -->

- 类型：byte。If rotation Y Head bit is true, then this will contain a head rotation of the actor if and only if it's a Mob type


///

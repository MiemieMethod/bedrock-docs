# <!-- md:samp MoveActorAbsoluteData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MoveActorAbsoluteData -->类型。

## 结构

```viz
digraph MoveActorAbsoluteData {
	graph [rankdir=LR];
	{
		graph [rank=max];
		4	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		6	[comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		8	[comment="name: \"Vec3\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		10	[comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		12	[comment="name: \"byte\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		14	[comment="name: \"byte\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	2	[comment="name: \"MoveActorAbsoluteData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=MoveActorAbsoluteData];
	3	[comment="name: \"ActorRuntimeID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"The runtime id of \
the actor being moved\"",
		label=ActorRuntimeID];
	2 -> 3;
	5	[comment="name: \"Header\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Header bits describing the status of the \
actor, see additional documentation in the supplemental documentation folder\"",
		label=Header];
	2 -> 5;
	7	[comment="name: \"Position\", typeName: \"Vec3\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"X/Y/Z coordinates of the position \
of the actor, each being a 4 byte float\"",
		label=Position];
	2 -> 7;
	9	[comment="name: \"Rotation X\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"The X rotation of the actor stored as \
an integer\"",
		label="Rotation X"];
	2 -> 9;
	11	[comment="name: \"Rotation Y\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"The Y rotation of the actor stored \
as an integer\"",
		label="Rotation Y"];
	2 -> 11;
	13	[comment="name: \"Rotation Y Head\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"The head rotation of the actor \
if and only if it's a Mob type, stored as an integer\"",
		label="Rotation Y Head"];
	2 -> 13;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
}

```

## 字段

/// define
MoveActorAbsoluteData

ActorRuntimeID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/ActorRuntimeID.md)

- 类型：ActorRuntimeID。The runtime 'id' of the actor being moved

Header：<!-- md:samp byte -->

- 类型：byte。Header bits describing the status of the actor, see additional documentation in the supplemental documentation folder

Position：[<!-- md:samp Vec3 -->](refs/protocols/types/Vec3.md)

- 类型：Vec3。X/Y/Z coordinates of the position of the actor, each being a 4 byte float

Rotation X：<!-- md:samp byte -->

- 类型：byte。The X rotation of the actor stored as an integer

Rotation Y：<!-- md:samp byte -->

- 类型：byte。The Y rotation of the actor stored as an integer

Rotation Y Head：<!-- md:samp byte -->

- 类型：byte。The head rotation of the actor if and only if it's a Mob type, stored as an integer


///

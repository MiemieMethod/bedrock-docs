# <!-- md:samp MovePlayerPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MovePlayerPacket -->数据包，数字ID是`19`。

## 结构

```viz
digraph MovePlayerPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		6	[comment="name: \"Vec2\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec2];
		8	[comment="name: \"float\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		10	[comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		12	[comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		14	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		17	[comment="name: \"[No Data]\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		20	[comment="name: \"int\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		22	[comment="name: \"int\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		24	[comment="name: \"unsigned varint64\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint64"];
	}
	0	[comment="name: \"MovePlayerPacket\", typeName: \"\", id: 0, branchId: 19, recurseId: -1, attributes: 0, notes: \"\"",
		label=MovePlayerPacket];
	1	[comment="name: \"Player Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 3;
	5	[comment="name: \"Rotation\", typeName: \"Vec2\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Rotation];
	0 -> 5;
	7	[comment="name: \"Y-Head Rotation\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Y-Head Rotation"];
	0 -> 7;
	9	[comment="name: \"Position Mode\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayerPositionModeComponent::\
PositionMode\"",
		label="Position Mode"];
	0 -> 9;
	11	[comment="name: \"On Ground\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="On Ground"];
	0 -> 11;
	13	[comment="name: \"Riding Runtime ID\", typeName: \"ActorRuntimeID\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Riding Runtime ID"];
	0 -> 13;
	15	[comment="name: \"Dependency on 'Position Mode == Teleport'\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Position Mode == Teleport'",
		shape=note];
	0 -> 15;
	23	[comment="name: \"Tick\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"Should be the tick we last processed from \
PlayerAuthInputPacket or 0 if we're not doing server authoritative movement\"",
		label=Tick];
	0 -> 23;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	16	[comment="name: \"if (0)\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	15 -> 16;
	18	[comment="name: \"if (1)\", typeName: \"\", id: 18, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	15 -> 18;
	16 -> 17;
	19	[comment="name: \"Teleportation Cause\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Teleportation Cause"];
	18 -> 19;
	21	[comment="name: \"Source Actor Type\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Source Actor Type"];
	18 -> 21;
	19 -> 20;
	21 -> 22;
	23 -> 24;
}

```

## 字段

/// define
MovePlayerPacket

Player Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/ActorRuntimeID.md)

- 类型：ActorRuntimeID。

Position：[<!-- md:samp Vec3 -->](refs/protocols/types/Vec3.md)

- 类型：Vec3。

Rotation：[<!-- md:samp Vec2 -->](refs/protocols/types/Vec2.md)

- 类型：Vec2。

Y-Head Rotation：<!-- md:samp float -->

- 类型：float。

Position Mode：<!-- md:samp byte -->

- 类型：byte。enumeration: PlayerPositionModeComponent::PositionMode

On Ground：<!-- md:samp bool -->

- 类型：bool。

Riding Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/ActorRuntimeID.md)

- 类型：ActorRuntimeID。

Dependency on 'Position Mode == Teleport'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Teleportation Cause：<!-- md:samp int -->

- 类型：int。

Source Actor Type：<!-- md:samp int -->

- 类型：int。


/////

////


Tick：<!-- md:samp unsigned varint64 -->

- 类型：unsigned varint64。Should be the tick we last processed from PlayerAuthInputPacket or 0 if we're not doing server authoritative movement


///

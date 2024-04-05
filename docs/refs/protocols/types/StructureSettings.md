# <!-- md:samp StructureSettings -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StructureSettings -->类型。

## 结构

```viz
digraph StructureSettings {
	graph [rankdir=LR];
	{
		graph [rank=max];
		18	[comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		20	[comment="name: \"bool\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		22	[comment="name: \"bool\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		24	[comment="name: \"bool\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		26	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		28	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		30	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		32	[comment="name: \"byte\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		34	[comment="name: \"byte\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		36	[comment="name: \"byte\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		38	[comment="name: \"float\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		40	[comment="name: \"float\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		42	[comment="name: \"unsigned int\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		44	[comment="name: \"Vec3\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
	}
	16	[comment="name: \"StructureSettings\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=StructureSettings];
	17	[comment="name: \"Structure Palette Name\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Structure Palette Name"];
	16 -> 17;
	19	[comment="name: \"Should ignore entities?\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Should ignore entities?"];
	16 -> 19;
	21	[comment="name: \"Should ignore blocks?\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Should ignore blocks?"];
	16 -> 21;
	23	[comment="name: \"Should Allow Non Ticking Player and Ticking Area Chunks\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, \
notes: \"\"",
		label="Should Allow Non Ticking Player and Ticking Area Chunks"];
	16 -> 23;
	25	[comment="name: \"Structure Size\", typeName: \"NetworkBlockPosition\", id: 25, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Structure Size"];
	16 -> 25;
	27	[comment="name: \"Structure Offset\", typeName: \"NetworkBlockPosition\", id: 27, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Structure Offset"];
	16 -> 27;
	29	[comment="name: \"Last Edit Player\", typeName: \"ActorUniqueID\", id: 29, branchId: 0, recurseId: -1, attributes: 256, notes: \"Player who last \
edited the structure block.\"",
		label="Last Edit Player"];
	16 -> 29;
	31	[comment="name: \"Rotation\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Rotation\"",
		label=Rotation];
	16 -> 31;
	33	[comment="name: \"Mirror\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Mirror\"",
		label=Mirror];
	16 -> 33;
	35	[comment="name: \"Animation Mode\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: AnimationMode\"",
		label="Animation Mode"];
	16 -> 35;
	37	[comment="name: \"Animation Seconds\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Animation Seconds"];
	16 -> 37;
	39	[comment="name: \"Integrity Value\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Integrity Value"];
	16 -> 39;
	41	[comment="name: \"Integrity Seed\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Integrity Seed"];
	16 -> 41;
	43	[comment="name: \"Rotation Pivot\", typeName: \"Vec3\", id: 43, branchId: 0, recurseId: -1, attributes: 256, notes: \"Pivot used to rotate a structure \
around.\"",
		label="Rotation Pivot"];
	16 -> 43;
	17 -> 18;
	19 -> 20;
	21 -> 22;
	23 -> 24;
	25 -> 26;
	27 -> 28;
	29 -> 30;
	31 -> 32;
	33 -> 34;
	35 -> 36;
	37 -> 38;
	39 -> 40;
	41 -> 42;
	43 -> 44;
}

```

## 字段

/// define
StructureSettings

Structure Palette Name：<!-- md:samp string -->

- 类型：string。

Should ignore entities?：<!-- md:samp bool -->

- 类型：bool。

Should ignore blocks?：<!-- md:samp bool -->

- 类型：bool。

Should Allow Non Ticking Player and Ticking Area Chunks：<!-- md:samp bool -->

- 类型：bool。

Structure Size：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Structure Offset：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Last Edit Player：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/actoruniqueid.md)

- 类型：ActorUniqueID。Player who last edited the structure block.

Rotation：<!-- md:samp byte -->

- 类型：byte。enumeration: Rotation

Mirror：<!-- md:samp byte -->

- 类型：byte。enumeration: Mirror

Animation Mode：<!-- md:samp byte -->

- 类型：byte。enumeration: AnimationMode

Animation Seconds：<!-- md:samp float -->

- 类型：float。

Integrity Value：<!-- md:samp float -->

- 类型：float。

Integrity Seed：<!-- md:samp unsigned int -->

- 类型：unsigned int。

Rotation Pivot：[<!-- md:samp Vec3 -->](refs/protocols/types/vec3.md)

- 类型：Vec3。Pivot used to rotate a structure around.


///

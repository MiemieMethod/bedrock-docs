# <!-- md:samp AddActorPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AddActorPacket -->数据包，数字ID是`13`。

## 结构

```viz
digraph AddActorPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		4	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"Vec3\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		10	[comment="name: \"Vec3\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		12	[comment="name: \"Vec2\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec2];
		14	[comment="name: \"float\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		16	[comment="name: \"float\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		19	[comment="name: \"unsigned varint\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		22	[comment="name: \"string\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		24	[comment="name: \"float\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		26	[comment="name: \"float\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		28	[comment="name: \"float\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		30	[comment="name: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class \
std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", typeName: \"\", id: 30, branchId: 0, recurseId: \
-1, attributes: 512, notes: \"\"",
			label="std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_\
ptr<class DataItem,struct std::default_delete<class DataItem> > > >"];
		32	[comment="name: \"PropertySyncData\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=PropertySyncData];
		35	[comment="name: \"unsigned varint\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		38	[comment="name: \"ActorLink\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorLink];
	}
	0	[comment="name: \"AddActorPacket\", typeName: \"\", id: 0, branchId: 13, recurseId: -1, attributes: 0, notes: \"\"",
		label=AddActorPacket];
	1	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	0 -> 1;
	3	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 3;
	5	[comment="name: \"Actor Type\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Actor Type"];
	0 -> 5;
	7	[comment="name: \"Position\", typeName: \"Vec3\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 7;
	9	[comment="name: \"Velocity\", typeName: \"Vec3\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Velocity];
	0 -> 9;
	11	[comment="name: \"Rotation\", typeName: \"Vec2\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Rotation];
	0 -> 11;
	13	[comment="name: \"Y Head Rotation\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Y Head Rotation"];
	0 -> 13;
	15	[comment="name: \"Y Body Rotation\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Y Body Rotation"];
	0 -> 15;
	17	[comment="name: \"Attributes List\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Attributes List"];
	0 -> 17;
	29	[comment="name: \"Actor Data\", typeName: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class \
std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", id: 29, branchId: 0, recurseId: \
-1, attributes: 256, notes: \"\"",
		label="Actor Data"];
	0 -> 29;
	31	[comment="name: \"Synched Properties\", typeName: \"PropertySyncData\", id: 31, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Synched Properties"];
	0 -> 31;
	33	[comment="name: \"Actor Links\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Actor Links"];
	0 -> 33;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 16;
	18	[comment="name: \"Array Size\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	17 -> 18;
	20	[comment="name: \"example element\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	17 -> 20;
	18 -> 19;
	21	[comment="name: \"Attribute Name\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Attribute Name"];
	20 -> 21;
	23	[comment="name: \"Min Value\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Min Value"];
	20 -> 23;
	25	[comment="name: \"Current Value\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Current Value"];
	20 -> 25;
	27	[comment="name: \"Max Value\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Max Value"];
	20 -> 27;
	21 -> 22;
	23 -> 24;
	25 -> 26;
	27 -> 28;
	29 -> 30;
	31 -> 32;
	34	[comment="name: \"Array Size\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	33 -> 34;
	36	[comment="name: \"example element\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	33 -> 36;
	34 -> 35;
	37	[comment="name: \"Link\", typeName: \"ActorLink\", id: 37, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Link];
	36 -> 37;
	37 -> 38;
}

```

## 字段

/// define
AddActorPacket

Target Actor ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/actoruniqueid.md)

- 类型：ActorUniqueID。

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Actor Type：<!-- md:samp string -->

- 类型：string。

Position：[<!-- md:samp Vec3 -->](refs/protocols/types/vec3.md)

- 类型：Vec3。

Velocity：[<!-- md:samp Vec3 -->](refs/protocols/types/vec3.md)

- 类型：Vec3。

Rotation：[<!-- md:samp Vec2 -->](refs/protocols/types/vec2.md)

- 类型：Vec2。

Y Head Rotation：<!-- md:samp float -->

- 类型：float。

Y Body Rotation：<!-- md:samp float -->

- 类型：float。

Attributes List

Attributes List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Attributes List的示例元素

Attribute Name：<!-- md:samp string -->

- 类型：string。

Min Value：<!-- md:samp float -->

- 类型：float。

Current Value：<!-- md:samp float -->

- 类型：float。

Max Value：<!-- md:samp float -->

- 类型：float。

Actor Data：[<!-- md:samp std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > > -->](refs/protocols/types/std::vector<class_std::unique_ptr<class_dataitem,struct_std::default_delete<class_dataitem>_>,class_std::allocator<class_std::unique_ptr<class_dataitem,struct_std::default_delete<class_dataitem>_>_>_>.md)

- 类型：std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >。

Synched Properties：[<!-- md:samp PropertySyncData -->](refs/protocols/types/propertysyncdata.md)

- 类型：PropertySyncData。

Actor Links

Actor Links数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Actor Links的示例元素

Link：[<!-- md:samp ActorLink -->](refs/protocols/types/actorlink.md)

- 类型：ActorLink。


///

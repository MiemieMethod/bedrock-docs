# <!-- md:samp ClientboundDebugRendererPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ClientboundDebugRendererPacket -->数据包，数字ID是`164`。

## 结构

```viz
digraph ClientboundDebugRendererPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		5	[comment="name: \"[No Data]\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		7	[comment="name: \"[No Data]\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		12	[comment="name: \"Vec3\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		14	[comment="name: \"float\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		16	[comment="name: \"float\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		18	[comment="name: \"float\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		20	[comment="name: \"float\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		22	[comment="name: \"unsigned int64\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
	}
	0	[comment="name: \"ClientboundDebugRendererPacket\", typeName: \"\", id: 0, branchId: 164, recurseId: -1, attributes: 0, notes: \"\"",
		label=ClientboundDebugRendererPacket];
	1	[comment="name: \"Debug Marker Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ClientboundDebugRendererPacket::\
Type\"",
		label="Debug Marker Type"];
	0 -> 1;
	3	[comment="name: \"Dependency on 'Debug Marker Type'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Debug Marker Type'",
		shape=note];
	0 -> 3;
	1 -> 2;
	4	[comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	3 -> 4;
	6	[comment="name: \"if (1)\", typeName: \"\", id: 6, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	3 -> 6;
	8	[comment="name: \"if (2)\", typeName: \"\", id: 8, branchId: 2, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (2)",
		shape=diamond];
	3 -> 8;
	4 -> 5;
	6 -> 7;
	9	[comment="name: \"Debug Marker Text\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Debug Marker Text"];
	8 -> 9;
	11	[comment="name: \"Debug Marker Position\", typeName: \"Vec3\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Debug Marker Position"];
	8 -> 11;
	13	[comment="name: \"Debug Marker Color red\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Debug Marker Color red"];
	8 -> 13;
	15	[comment="name: \"Debug Marker Color green\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Debug Marker Color green"];
	8 -> 15;
	17	[comment="name: \"Debug Marker Color blue\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Debug Marker Color blue"];
	8 -> 17;
	19	[comment="name: \"Debug Marker Color alpha\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Debug Marker Color alpha"];
	8 -> 19;
	21	[comment="name: \"Debug Marker Duration Milliseconds\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Debug Marker Duration Milliseconds"];
	8 -> 21;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 16;
	17 -> 18;
	19 -> 20;
	21 -> 22;
}

```

## 字段

/// define
ClientboundDebugRendererPacket

Debug Marker Type：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: ClientboundDebugRendererPacket::Type

Dependency on 'Debug Marker Type'

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

//// tab | if (2)
///// define
if (2)

Debug Marker Text：<!-- md:samp string -->

- 类型：string。

Debug Marker Position：[<!-- md:samp Vec3 -->](refs/protocols/types/vec3.md)

- 类型：Vec3。

Debug Marker Color red：<!-- md:samp float -->

- 类型：float。

Debug Marker Color green：<!-- md:samp float -->

- 类型：float。

Debug Marker Color blue：<!-- md:samp float -->

- 类型：float。

Debug Marker Color alpha：<!-- md:samp float -->

- 类型：float。

Debug Marker Duration Milliseconds：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。


/////

////



///

# <!-- md:samp AddPaintingPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AddPaintingPacket -->数据包，数字ID是`22`。

## 结构

```viz
digraph AddPaintingPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		4	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		6	[comment="name: \"Vec3\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		8	[comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"AddPaintingPacket\", typeName: \"\", id: 0, branchId: 22, recurseId: -1, attributes: 0, notes: \"\"",
		label=AddPaintingPacket];
	1	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	0 -> 1;
	3	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 3;
	5	[comment="name: \"Position\", typeName: \"Vec3\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 5;
	7	[comment="name: \"Direction\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Direction];
	0 -> 7;
	9	[comment="name: \"Motif\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Motif];
	0 -> 9;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
}

```

## 字段

/// define
AddPaintingPacket

Target Actor ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/actoruniqueid.md)

- 类型：ActorUniqueID。

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Position：[<!-- md:samp Vec3 -->](refs/protocols/types/vec3.md)

- 类型：Vec3。

Direction：<!-- md:samp varint -->

- 类型：varint。

Motif：<!-- md:samp string -->

- 类型：string。


///

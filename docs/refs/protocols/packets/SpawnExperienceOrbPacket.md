# <!-- md:samp SpawnExperienceOrbPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SpawnExperienceOrbPacket -->数据包，数字ID是`66`。

## 结构

```dot
digraph SpawnExperienceOrbPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"Vec3\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"SpawnExperienceOrbPacket\", typeName: \"\", id: 0, branchId: 66, recurseId: -1, attributes: 0, notes: \"\"",
		label=SpawnExperienceOrbPacket];
	1	[comment="name: \"Position\", typeName: \"Vec3\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 1;
	3	[comment="name: \"XP Value\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="XP Value"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
SpawnExperienceOrbPacket

Position：[<!-- md:samp Vec3 -->](refs/protocols/types/Vec3.md)

- 类型：Vec3。

XP Value：<!-- md:samp varint -->

- 类型：varint。


///

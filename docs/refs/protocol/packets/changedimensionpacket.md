# <!-- md:samp ChangeDimensionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ChangeDimensionPacket -->数据包，数字ID是`61`。

## 结构

```viz
digraph ChangeDimensionPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"ChangeDimensionPacket\", typeName: \"\", id: 0, branchId: 61, recurseId: -1, attributes: 0, notes: \"\"",
		label=ChangeDimensionPacket];
	1	[comment="name: \"Dimension ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> Overworld, \
1 -> Nether, 2 -> The End, 3 -> Undefined)\"",
		label="Dimension ID"];
	0 -> 1;
	3	[comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 3;
	5	[comment="name: \"Respawn\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Respawn];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
ChangeDimensionPacket

Dimension ID：<!-- md:samp varint -->

- 类型：varint。Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)

Position：[<!-- md:samp Vec3 -->](refs/protocols/types/vec3.md)

- 类型：Vec3。

Respawn：<!-- md:samp bool -->

- 类型：bool。


///

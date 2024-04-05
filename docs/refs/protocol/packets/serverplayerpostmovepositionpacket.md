# <!-- md:samp ServerPlayerPostMovePositionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ServerPlayerPostMovePositionPacket -->数据包，数字ID是`16`。

## 结构

```viz
digraph ServerPlayerPostMovePositionPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"Vec3\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
	}
	0	[comment="name: \"ServerPlayerPostMovePositionPacket\", typeName: \"\", id: 0, branchId: 16, recurseId: -1, attributes: 0, notes: \"\"",
		label=ServerPlayerPostMovePositionPacket];
	1	[comment="name: \"Pos\", typeName: \"Vec3\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Pos];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
ServerPlayerPostMovePositionPacket

Pos：[<!-- md:samp Vec3 -->](refs/protocols/types/vec3.md)

- 类型：Vec3。


///

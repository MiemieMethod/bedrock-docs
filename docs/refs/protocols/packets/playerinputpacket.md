# <!-- md:samp PlayerInputPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerInputPacket -->数据包，数字ID是`57`。

## 结构

```viz
digraph PlayerInputPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"Vec2\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec2];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"PlayerInputPacket\", typeName: \"\", id: 0, branchId: 57, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerInputPacket];
	1	[comment="name: \"Move Vector\", typeName: \"Vec2\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Move Vector"];
	0 -> 1;
	3	[comment="name: \"Jumping\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Jumping];
	0 -> 3;
	5	[comment="name: \"Sneaking\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Sneaking];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
PlayerInputPacket

Move Vector：[<!-- md:samp Vec2 -->](refs/protocols/types/vec2.md)

- 类型：Vec2。

Jumping：<!-- md:samp bool -->

- 类型：bool。

Sneaking：<!-- md:samp bool -->

- 类型：bool。


///

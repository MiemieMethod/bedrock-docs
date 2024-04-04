# <!-- md:samp LessonProgressPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LessonProgressPacket -->数据包，数字ID是`183`。

## 结构

```dot
digraph LessonProgressPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"LessonProgressPacket\", typeName: \"\", id: 0, branchId: 183, recurseId: -1, attributes: 0, notes: \"\"",
		label=LessonProgressPacket];
	1	[comment="name: \"Lesson Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LessonAction\"",
		label="Lesson Action"];
	0 -> 1;
	3	[comment="name: \"Score\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Score];
	0 -> 3;
	5	[comment="name: \"Activity Id\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Activity Id"];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
LessonProgressPacket

Lesson Action：<!-- md:samp byte -->

- 类型：byte。enumeration: LessonAction

Score：<!-- md:samp varint -->

- 类型：varint。

Activity Id：<!-- md:samp string -->

- 类型：string。


///

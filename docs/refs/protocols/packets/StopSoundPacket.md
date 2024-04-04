# <!-- md:samp StopSoundPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StopSoundPacket -->数据包，数字ID是`87`。

## 结构

```dot
digraph StopSoundPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"StopSoundPacket\", typeName: \"\", id: 0, branchId: 87, recurseId: -1, attributes: 0, notes: \"\"",
		label=StopSoundPacket];
	1	[comment="name: \"Sound Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sound Name"];
	0 -> 1;
	3	[comment="name: \"Stop All Sounds?\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Stop All Sounds?"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
StopSoundPacket

Sound Name：<!-- md:samp string -->

- 类型：string。

Stop All Sounds?：<!-- md:samp bool -->

- 类型：bool。


///

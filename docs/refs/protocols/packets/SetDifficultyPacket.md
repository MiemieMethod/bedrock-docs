# <!-- md:samp SetDifficultyPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetDifficultyPacket -->数据包，数字ID是`60`。

## 结构

```viz
digraph SetDifficultyPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
	}
	0	[comment="name: \"SetDifficultyPacket\", typeName: \"\", id: 0, branchId: 60, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetDifficultyPacket];
	1	[comment="name: \"Difficulty\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Difficulty\"",
		label=Difficulty];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SetDifficultyPacket

Difficulty：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: Difficulty


///

# <!-- md:samp SetCommandsEnabledPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetCommandsEnabledPacket -->数据包，数字ID是`59`。

## 结构

```viz
digraph SetCommandsEnabledPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"SetCommandsEnabledPacket\", typeName: \"\", id: 0, branchId: 59, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetCommandsEnabledPacket];
	1	[comment="name: \"Commands Enabled\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Commands Enabled"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SetCommandsEnabledPacket

Commands Enabled：<!-- md:samp bool -->

- 类型：bool。


///

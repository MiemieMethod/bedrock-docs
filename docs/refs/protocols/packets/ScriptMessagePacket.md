# <!-- md:samp ScriptMessagePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ScriptMessagePacket -->数据包，数字ID是`177`。

## 结构

```viz
digraph ScriptMessagePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"ScriptMessagePacket\", typeName: \"\", id: 0, branchId: 177, recurseId: -1, attributes: 0, notes: \"\"",
		label=ScriptMessagePacket];
	1	[comment="name: \"Message Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Message Id"];
	0 -> 1;
	3	[comment="name: \"Message Value\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Message Value"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
ScriptMessagePacket

Message Id：<!-- md:samp string -->

- 类型：string。

Message Value：<!-- md:samp string -->

- 类型：string。


///

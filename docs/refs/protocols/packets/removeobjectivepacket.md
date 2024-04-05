# <!-- md:samp RemoveObjectivePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RemoveObjectivePacket -->数据包，数字ID是`106`。

## 结构

```viz
digraph RemoveObjectivePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"RemoveObjectivePacket\", typeName: \"\", id: 0, branchId: 106, recurseId: -1, attributes: 0, notes: \"\"",
		label=RemoveObjectivePacket];
	1	[comment="name: \"Objective Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Objective Name"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
RemoveObjectivePacket

Objective Name：<!-- md:samp string -->

- 类型：string。


///

# <!-- md:samp GameTestResultsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp GameTestResultsPacket -->数据包，数字ID是`195`。

## 结构

```dot
digraph GameTestResultsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"GameTestResultsPacket\", typeName: \"\", id: 0, branchId: 195, recurseId: -1, attributes: 0, notes: \"\"",
		label=GameTestResultsPacket];
	1	[comment="name: \"Succeeded\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Succeeded];
	0 -> 1;
	3	[comment="name: \"Error\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Error];
	0 -> 3;
	5	[comment="name: \"TestName\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=TestName];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
GameTestResultsPacket

Succeeded：<!-- md:samp bool -->

- 类型：bool。

Error：<!-- md:samp string -->

- 类型：string。

TestName：<!-- md:samp string -->

- 类型：string。


///

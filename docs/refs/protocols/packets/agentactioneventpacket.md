# <!-- md:samp AgentActionEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AgentActionEventPacket -->数据包，数字ID是`181`。

## 结构

```viz
digraph AgentActionEventPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"AgentActionEventPacket\", typeName: \"\", id: 0, branchId: 181, recurseId: -1, attributes: 0, notes: \"\"",
		label=AgentActionEventPacket];
	1	[comment="name: \"Request Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Request Id"];
	0 -> 1;
	3	[comment="name: \"Request Id\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: AgentActionType\"",
		label="Request Id"];
	0 -> 3;
	5	[comment="name: \"Response\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Response];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
AgentActionEventPacket

Request Id：<!-- md:samp string -->

- 类型：string。

Request Id：<!-- md:samp int -->

- 类型：int。enumeration: AgentActionType

Response：<!-- md:samp string -->

- 类型：string。


///

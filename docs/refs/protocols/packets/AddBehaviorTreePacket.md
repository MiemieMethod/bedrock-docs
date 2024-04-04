# <!-- md:samp AddBehaviorTreePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AddBehaviorTreePacket -->数据包，数字ID是`89`。

## 结构

```dot
digraph AddBehaviorTreePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"AddBehaviorTreePacket\", typeName: \"\", id: 0, branchId: 89, recurseId: -1, attributes: 0, notes: \"\"",
		label=AddBehaviorTreePacket];
	1	[comment="name: \"Behavior Tree Structure (JSON)\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Behavior Tree Structure (JSON)"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
AddBehaviorTreePacket

Behavior Tree Structure (JSON)：<!-- md:samp string -->

- 类型：string。


///

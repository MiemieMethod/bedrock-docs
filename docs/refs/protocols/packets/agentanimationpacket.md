# <!-- md:samp AgentAnimationPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AgentAnimationPacket -->数据包，数字ID是`304`。

## 结构

```viz
digraph AgentAnimationPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
	}
	0	[comment="name: \"AgentAnimationPacket\", typeName: \"\", id: 0, branchId: 304, recurseId: -1, attributes: 0, notes: \"\"",
		label=AgentAnimationPacket];
	1	[comment="name: \"Agent Animation\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Agent Animation"];
	0 -> 1;
	3	[comment="name: \"Runtime Id\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Runtime Id"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
AgentAnimationPacket

Agent Animation：<!-- md:samp byte -->

- 类型：byte。

Runtime Id：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。


///

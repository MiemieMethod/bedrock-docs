# <!-- md:samp SetLocalPlayerAsInitializedPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetLocalPlayerAsInitializedPacket -->数据包，数字ID是`113`。

## 结构

```viz
digraph SetLocalPlayerAsInitializedPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
	}
	0	[comment="name: \"SetLocalPlayerAsInitializedPacket\", typeName: \"\", id: 0, branchId: 113, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetLocalPlayerAsInitializedPacket];
	1	[comment="name: \"Player ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player ID"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SetLocalPlayerAsInitializedPacket

Player ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。


///

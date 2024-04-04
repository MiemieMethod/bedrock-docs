# <!-- md:samp PlayerStartItemCooldownPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerStartItemCooldownPacket -->数据包，数字ID是`176`。

## 结构

```dot
digraph PlayerStartItemCooldownPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"PlayerStartItemCooldownPacket\", typeName: \"\", id: 0, branchId: 176, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerStartItemCooldownPacket];
	1	[comment="name: \"Item Category\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Item Category"];
	0 -> 1;
	3	[comment="name: \"Duration Ticks\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Duration Ticks"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
PlayerStartItemCooldownPacket

Item Category：<!-- md:samp string -->

- 类型：string。

Duration Ticks：<!-- md:samp varint -->

- 类型：varint。


///

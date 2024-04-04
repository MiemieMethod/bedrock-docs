# <!-- md:samp ActorPickRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ActorPickRequestPacket -->数据包，数字ID是`35`。

## 结构

```dot
digraph ActorPickRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int64];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"ActorPickRequestPacket\", typeName: \"\", id: 0, branchId: 35, recurseId: -1, attributes: 0, notes: \"\"",
		label=ActorPickRequestPacket];
	1	[comment="name: \"Actor ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Target Actor ID\"",
		label="Actor ID"];
	0 -> 1;
	3	[comment="name: \"Max Slots\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"number of empty hotbar slots (to decide \
whether to overwrite a slot or add it to an empty one)\"",
		label="Max Slots"];
	0 -> 3;
	5	[comment="name: \"With Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"whether we want to store the NBT data \
along with the item\"",
		label="With Data"];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
ActorPickRequestPacket

Actor ID：<!-- md:samp int64 -->

- 类型：int64。Target Actor ID

Max Slots：<!-- md:samp byte -->

- 类型：byte。number of empty hotbar slots (to dec'id'e whether to overwrite a slot or add it to an empty one)

With Data：<!-- md:samp bool -->

- 类型：bool。whether we want to store the NBT data along with the item


///

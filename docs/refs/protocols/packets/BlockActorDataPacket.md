# <!-- md:samp BlockActorDataPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BlockActorDataPacket -->数据包，数字ID是`56`。

## 结构

```viz
digraph BlockActorDataPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		4	[comment="name: \"CompoundTag\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
	}
	0	[comment="name: \"BlockActorDataPacket\", typeName: \"\", id: 0, branchId: 56, recurseId: -1, attributes: 0, notes: \"\"",
		label=BlockActorDataPacket];
	1	[comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Block Position"];
	0 -> 1;
	3	[comment="name: \"Actor Data Tags\", typeName: \"CompoundTag\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Actor Data Tags"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
BlockActorDataPacket

Block Position：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Actor Data Tags：[<!-- md:samp CompoundTag -->](refs/protocols/types/compoundtag.md)

- 类型：CompoundTag。


///

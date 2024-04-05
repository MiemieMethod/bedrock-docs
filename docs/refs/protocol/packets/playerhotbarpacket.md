# <!-- md:samp PlayerHotbarPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerHotbarPacket -->数据包，数字ID是`48`。

## 结构

```viz
digraph PlayerHotbarPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"PlayerHotbarPacket\", typeName: \"\", id: 0, branchId: 48, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerHotbarPacket];
	1	[comment="name: \"Selected Slot\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Selected Slot"];
	0 -> 1;
	3	[comment="name: \"Container ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\"",
		label="Container ID"];
	0 -> 3;
	5	[comment="name: \"Should select slot?\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Should select slot?"];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
PlayerHotbarPacket

Selected Slot：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Container ID：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerID

Should select slot?：<!-- md:samp bool -->

- 类型：bool。


///

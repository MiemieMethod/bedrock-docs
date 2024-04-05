# <!-- md:samp CommandRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CommandRequestPacket -->数据包，数字ID是`77`。

## 结构

```viz
digraph CommandRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		22	[comment="name: \"CommandOriginData\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CommandOriginData];
		24	[comment="name: \"bool\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		26	[comment="name: \"varint\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"CommandRequestPacket\", typeName: \"\", id: 0, branchId: 77, recurseId: -1, attributes: 0, notes: \"\"",
		label=CommandRequestPacket];
	1	[comment="name: \"Command\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Command];
	0 -> 1;
	3	[comment="name: \"Command Origin\", typeName: \"CommandOriginData\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Command Origin"];
	0 -> 3;
	23	[comment="name: \"Is Internal Source?\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Internal Source?"];
	0 -> 23;
	25	[comment="name: \"Version\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Version];
	0 -> 25;
	1 -> 2;
	3 -> 22;
	23 -> 24;
	25 -> 26;
}

```

## 字段

/// define
CommandRequestPacket

Command：<!-- md:samp string -->

- 类型：string。

Command Origin：[<!-- md:samp CommandOriginData -->](refs/protocols/types/commandorigindata.md)

- 类型：CommandOriginData。

Is Internal Source?：<!-- md:samp bool -->

- 类型：bool。

Version：<!-- md:samp varint -->

- 类型：varint。


///

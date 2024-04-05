# <!-- md:samp PassengerJumpPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PassengerJumpPacket -->数据包，数字ID是`20`。

## 结构

```viz
digraph PassengerJumpPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"PassengerJumpPacket\", typeName: \"\", id: 0, branchId: 20, recurseId: -1, attributes: 0, notes: \"\"",
		label=PassengerJumpPacket];
	1	[comment="name: \"Jump Scale\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Jump Scale"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
PassengerJumpPacket

Jump Scale：<!-- md:samp varint -->

- 类型：varint。


///

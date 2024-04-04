# <!-- md:samp SetLastHurtByPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetLastHurtByPacket -->数据包，数字ID是`96`。

## 结构

```dot
digraph SetLastHurtByPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"SetLastHurtByPacket\", typeName: \"\", id: 0, branchId: 96, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetLastHurtByPacket];
	1	[comment="name: \"Last Hurt By\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorType\"",
		label="Last Hurt By"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SetLastHurtByPacket

Last Hurt By：<!-- md:samp varint -->

- 类型：varint。enumeration: ActorType


///

# <!-- md:samp SimpleEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SimpleEventPacket -->数据包，数字ID是`64`。

## 结构

```viz
digraph SimpleEventPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned short\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
	}
	0	[comment="name: \"SimpleEventPacket\", typeName: \"\", id: 0, branchId: 64, recurseId: -1, attributes: 0, notes: \"\"",
		label=SimpleEventPacket];
	1	[comment="name: \"Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SimpleEventPacket::Subtype\"",
		label=Type];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SimpleEventPacket

Type：<!-- md:samp unsigned short -->

- 类型：unsigned short。enumeration: SimpleEventPacket::Subtype


///

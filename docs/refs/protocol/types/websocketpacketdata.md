# <!-- md:samp WebSocketPacketData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp WebSocketPacketData -->类型。

## 结构

```viz
digraph WebSocketPacketData {
	graph [rankdir=LR];
	{
		graph [rank=max];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	2	[comment="name: \"WebSocketPacketData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=WebSocketPacketData];
	3	[comment="name: \"Websocket Server URI\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Websocket Server URI"];
	2 -> 3;
	3 -> 4;
}

```

## 字段

/// define
WebSocketPacketData

Websocket Server URI：<!-- md:samp string -->

- 类型：string。


///

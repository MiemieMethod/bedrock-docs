# <!-- md:samp SubClientLoginPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SubClientLoginPacket -->数据包，数字ID是`94`。

## 结构

```dot
digraph SubClientLoginPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"SubClientLoginPacket\", typeName: \"\", id: 0, branchId: 94, recurseId: -1, attributes: 0, notes: \"\"",
		label=SubClientLoginPacket];
	1	[comment="name: \"Sub Client Connection Request\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"see @subClientConnectionRequest.html#\
diagram@\"",
		label="Sub Client Connection Request"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SubClientLoginPacket

Sub Client Connection Request：<!-- md:samp string -->

- 类型：string。see @subClientConnectionRequest.html#diagram@


///

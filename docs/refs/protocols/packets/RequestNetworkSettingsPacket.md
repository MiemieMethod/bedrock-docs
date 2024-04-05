# <!-- md:samp RequestNetworkSettingsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RequestNetworkSettingsPacket -->数据包，数字ID是`193`。

## 结构

```viz
digraph RequestNetworkSettingsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"big endian int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="big endian int"];
	}
	0	[comment="name: \"RequestNetworkSettingsPacket\", typeName: \"\", id: 0, branchId: 193, recurseId: -1, attributes: 0, notes: \"\"",
		label=RequestNetworkSettingsPacket];
	1	[comment="name: \"ClientNetworkVersion\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ClientNetworkVersion];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
RequestNetworkSettingsPacket

ClientNetworkVersion：<!-- md:samp big endian int -->

- 类型：big endian int。


///

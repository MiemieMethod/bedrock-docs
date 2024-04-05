# <!-- md:samp UpdateAbilitiesPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateAbilitiesPacket -->数据包，数字ID是`187`。

## 结构

```viz
digraph UpdateAbilitiesPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"SerializedAbilitiesData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=SerializedAbilitiesData];
	}
	0	[comment="name: \"UpdateAbilitiesPacket\", typeName: \"\", id: 0, branchId: 187, recurseId: -1, attributes: 0, notes: \"\"",
		label=UpdateAbilitiesPacket];
	1	[comment="name: \"Data\", typeName: \"SerializedAbilitiesData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Data];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
UpdateAbilitiesPacket

Data：[<!-- md:samp SerializedAbilitiesData -->](refs/protocols/types/serializedabilitiesdata.md)

- 类型：SerializedAbilitiesData。


///

# <!-- md:samp EditorNetworkPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp EditorNetworkPacket -->数据包，数字ID是`190`。

## 结构

```viz
digraph EditorNetworkPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"CompoundTag\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
	}
	0	[comment="name: \"EditorNetworkPacket\", typeName: \"\", id: 0, branchId: 190, recurseId: -1, attributes: 0, notes: \"\"",
		label=EditorNetworkPacket];
	1	[comment="name: \"Binary Payload\", typeName: \"CompoundTag\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Binary Payload"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
EditorNetworkPacket

Binary Payload：[<!-- md:samp CompoundTag -->](refs/protocols/types/compoundtag.md)

- 类型：CompoundTag。


///

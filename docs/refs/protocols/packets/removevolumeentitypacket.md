# <!-- md:samp RemoveVolumeEntityPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RemoveVolumeEntityPacket -->数据包，数字ID是`167`。

## 结构

```viz
digraph RemoveVolumeEntityPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"EntityNetId\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=EntityNetId];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"RemoveVolumeEntityPacket\", typeName: \"\", id: 0, branchId: 167, recurseId: -1, attributes: 0, notes: \"\"",
		label=RemoveVolumeEntityPacket];
	1	[comment="name: \"Entity Network Id\", typeName: \"EntityNetId\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Entity Network Id"];
	0 -> 1;
	3	[comment="name: \"Dimension Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Dimension Type"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
RemoveVolumeEntityPacket

Entity Network Id：[<!-- md:samp EntityNetId -->](../types/entitynetid.md)

- 类型：EntityNetId。

Dimension Type：<!-- md:samp varint -->

- 类型：varint。


///

# <!-- md:samp ShowStoreOfferPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ShowStoreOfferPacket -->数据包，数字ID是`91`。

## 结构

```dot
digraph ShowStoreOfferPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"ShowStoreOfferPacket\", typeName: \"\", id: 0, branchId: 91, recurseId: -1, attributes: 0, notes: \"\"",
		label=ShowStoreOfferPacket];
	1	[comment="name: \"Product ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Product ID"];
	0 -> 1;
	3	[comment="name: \"Redirect Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ShowStoreOfferRedirectType\"",
		label="Redirect Type"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
ShowStoreOfferPacket

Product ID：<!-- md:samp string -->

- 类型：string。

Redirect Type：<!-- md:samp byte -->

- 类型：byte。enumeration: ShowStoreOfferRedirectType


///

# <!-- md:samp Vec3 -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp Vec3 -->类型。

## 结构

```viz
digraph Vec3 {
	graph [rankdir=LR];
	{
		graph [rank=max];
		10	[comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		12	[comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		14	[comment="name: \"float\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
	}
	8	[comment="name: \"Vec3\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Vec3];
	9	[comment="name: \"X\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=X];
	8 -> 9;
	11	[comment="name: \"Y\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Y];
	8 -> 11;
	13	[comment="name: \"Z\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Z];
	8 -> 13;
	9 -> 10;
	11 -> 12;
	13 -> 14;
}

```

## 字段

/// define
Vec3

X：<!-- md:samp float -->

- 类型：float。

Y：<!-- md:samp float -->

- 类型：float。

Z：<!-- md:samp float -->

- 类型：float。


///

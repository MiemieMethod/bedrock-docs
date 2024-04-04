# <!-- md:samp Fixed Float -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp Fixed Float -->类型。

## 结构

```dot
digraph "Fixed Float" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint64];
	}
	0	[comment="name: \"Fixed Float\", typeName: \"\", id: 0, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Fixed Float"];
	1	[comment="name: \"Modified float value\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Float value multiplied by \
32\"",
		label="Modified float value"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
Fixed Float

Modified float value：<!-- md:samp varint64 -->

- 类型：varint64。Float value multiplied by 32


///

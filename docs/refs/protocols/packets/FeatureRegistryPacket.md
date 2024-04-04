# <!-- md:samp FeatureRegistryPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp FeatureRegistryPacket -->数据包，数字ID是`191`。

## 结构

```viz
digraph FeatureRegistryPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"FeatureRegistryPacket\", typeName: \"\", id: 0, branchId: 191, recurseId: -1, attributes: 0, notes: \"\"",
		label=FeatureRegistryPacket];
	1	[comment="name: \"FeaturesDataList\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=FeaturesDataList];
	0 -> 1;
	2	[comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	1 -> 2;
	4	[comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	1 -> 4;
	2 -> 3;
	5	[comment="name: \"feature Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="feature Name"];
	4 -> 5;
	7	[comment="name: \"Binary Json Output\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Binary Json Output"];
	4 -> 7;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
FeatureRegistryPacket

FeaturesDataList

FeaturesDataList数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

FeaturesDataList的示例元素

feature Name：<!-- md:samp string -->

- 类型：string。

Binary Json Output：<!-- md:samp string -->

- 类型：string。


///

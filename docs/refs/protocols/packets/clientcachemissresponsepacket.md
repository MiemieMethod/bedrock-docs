# <!-- md:samp ClientCacheMissResponsePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ClientCacheMissResponsePacket -->数据包，数字ID是`136`。

## 结构

```viz
digraph ClientCacheMissResponsePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"unsigned int64\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"ClientCacheMissResponsePacket\", typeName: \"\", id: 0, branchId: 136, recurseId: -1, attributes: 0, notes: \"\"",
		label=ClientCacheMissResponsePacket];
	1	[comment="name: \"Missing Blobs\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Missing Blobs"];
	0 -> 1;
	2	[comment="name: \"Number of missing blobs\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Number of missing blobs"];
	1 -> 2;
	4	[comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	1 -> 4;
	2 -> 3;
	5	[comment="name: \"Blob Id\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Blob Id"];
	4 -> 5;
	7	[comment="name: \"Blob Data\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Subchunk data (see https://gist.github.com/\
Tomcc/a96af509e275b1af483b25c543cfbf37) plus biome data\"",
		label="Blob Data"];
	4 -> 7;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
ClientCacheMissResponsePacket

Missing Blobs

//// define
Number of missing blobs：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Missing Blobs的示例元素

Blob Id：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。

Blob Data：<!-- md:samp string -->

- 类型：string。Subchunk data (see https://gist.github.com/Tomcc/a96af509e275b1af483b25c543cfbf37) plus biome data


////



///

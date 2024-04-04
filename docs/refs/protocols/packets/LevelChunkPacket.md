# <!-- md:samp LevelChunkPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelChunkPacket -->数据包，数字ID是`58`。

## 结构

```viz
digraph LevelChunkPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		7	[comment="name: \"ChunkPos\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ChunkPos];
		9	[comment="name: \"varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		13	[comment="name: \"unsigned varint\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		18	[comment="name: \"unsigned varint\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		20	[comment="name: \"unsigned short\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		23	[comment="name: \"unsigned varint\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		25	[comment="name: \"bool\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		28	[comment="name: \"[No Data]\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		32	[comment="name: \"unsigned varint\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		35	[comment="name: \"unsigned int64\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		37	[comment="name: \"string\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"LevelChunkPacket\", typeName: \"\", id: 0, branchId: 58, recurseId: -1, attributes: 0, notes: \"\"",
		label=LevelChunkPacket];
	1	[comment="name: \"Chunk Position\", typeName: \"ChunkPos\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Chunk Position"];
	0 -> 1;
	8	[comment="name: \"Dimension Id\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Dimension Id"];
	0 -> 8;
	10	[comment="name: \"Dependency on 'Client Needs To Request Subchunks?'\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Client Needs To Request Subchunks?'",
		shape=note];
	0 -> 10;
	24	[comment="name: \"Cache Enabled\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"Lets the server turn off the cache \
for this chunk even if the Client signaled it supports it.\"",
		label="Cache Enabled"];
	0 -> 24;
	26	[comment="name: \"Dependency on 'Cache Enabled?'\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Cache Enabled?'",
		shape=note];
	0 -> 26;
	36	[comment="name: \"Serialized Chunk Data\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"See https://gist.github.com/\
Tomcc/a96af509e275b1af483b25c543cfbf37\"",
		label="Serialized Chunk Data"];
	0 -> 36;
	1 -> 7;
	8 -> 9;
	11	[comment="name: \"if (0)\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	10 -> 11;
	14	[comment="name: \"if (1)\", typeName: \"\", id: 14, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	10 -> 14;
	12	[comment="name: \"Sub-chunks Count\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sub-chunks Count"];
	11 -> 12;
	12 -> 13;
	15	[comment="name: \"Dependency on 'Client Request SubChunk Limit < 0?'\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Client Request SubChunk Limit < 0?'",
		shape=note];
	14 -> 15;
	16	[comment="name: \"if (0)\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	15 -> 16;
	21	[comment="name: \"if (1)\", typeName: \"\", id: 21, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	15 -> 21;
	17	[comment="name: \"Partial SubChunk Count When Client Requesting\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\
Currently max unsigned 32-bit int\"",
		label="Partial SubChunk Count When Client Requesting"];
	16 -> 17;
	19	[comment="name: \"Client Request SubChunk Limit\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Client Request SubChunk Limit"];
	16 -> 19;
	17 -> 18;
	19 -> 20;
	22	[comment="name: \"SubChunk Count When Client Requesting\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently \
max unsigned 32-bit int\"",
		label="SubChunk Count When Client Requesting"];
	21 -> 22;
	22 -> 23;
	24 -> 25;
	27	[comment="name: \"if (0)\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	26 -> 27;
	29	[comment="name: \"if (1)\", typeName: \"\", id: 29, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	26 -> 29;
	27 -> 28;
	30	[comment="name: \"Cache Blobs\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Cache Blobs"];
	29 -> 30;
	31	[comment="name: \"Blob Count\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"How many cache blobs make up this chunk.\"",
		label="Blob Count"];
	30 -> 31;
	33	[comment="name: \"example element\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	30 -> 33;
	31 -> 32;
	34	[comment="name: \"Blob Id\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 0, notes: \"See ClientCacheProtocol.md, included with \
the documentation for 1.12.0.2\"",
		label="Blob Id"];
	33 -> 34;
	34 -> 35;
	36 -> 37;
}

```

## 字段

/// define
LevelChunkPacket

Chunk Position：[<!-- md:samp ChunkPos -->](refs/protocols/types/ChunkPos.md)

- 类型：ChunkPos。

Dimension Id：<!-- md:samp varint -->

- 类型：varint。

Dependency on 'Client Needs To Request Subchunks?'

//// tab | if (0)
///// define
if (0)

Sub-chunks Count：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


/////

////

//// tab | if (1)
///// define
if (1)

Dependency on 'Client Request SubChunk Limit < 0?'

////// tab | if (0)
/////// define
if (0)

Partial SubChunk Count When Client Requesting：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。Currently max unsigned 32-bit int

Client Request SubChunk Limit：<!-- md:samp unsigned short -->

- 类型：unsigned short。


///////

//////

////// tab | if (1)
/////// define
if (1)

SubChunk Count When Client Requesting：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。Currently max unsigned 32-bit int


///////

//////



/////

////


Cache Enabled：<!-- md:samp bool -->

- 类型：bool。Lets the server turn off the cache for this chunk even if the Client signaled it supports it.

Dependency on 'Cache Enabled?'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Cache Blobs

Blob Count：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。How many cache blobs make up this chunk.

Cache Blobs的示例元素

Blob Id：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。See ClientCacheProtocol.md, included with the documentation for 1.12.0.2


/////

////


Serialized Chunk Data：<!-- md:samp string -->

- 类型：string。See https://gist.github.com/Tomcc/a96af509e275b1af483b25c543cfbf37


///

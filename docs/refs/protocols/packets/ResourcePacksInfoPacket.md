# <!-- md:samp ResourcePacksInfoPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ResourcePacksInfoPacket -->数据包，数字ID是`6`。

## 结构

```dot
digraph ResourcePacksInfoPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		8	[comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		11	[comment="name: \"unsigned short\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		14	[comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		16	[comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		18	[comment="name: \"unsigned int64\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		20	[comment="name: \"string\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		22	[comment="name: \"string\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		24	[comment="name: \"string\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		26	[comment="name: \"bool\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		29	[comment="name: \"unsigned short\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned short"];
		32	[comment="name: \"string\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		34	[comment="name: \"string\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		36	[comment="name: \"unsigned int64\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		38	[comment="name: \"string\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		40	[comment="name: \"string\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		42	[comment="name: \"string\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		44	[comment="name: \"bool\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		46	[comment="name: \"bool\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		49	[comment="name: \"unsigned varint\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		52	[comment="name: \"string\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		54	[comment="name: \"string\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"ResourcePacksInfoPacket\", typeName: \"\", id: 0, branchId: 6, recurseId: -1, attributes: 0, notes: \"\"",
		label=ResourcePacksInfoPacket];
	1	[comment="name: \"Resource Pack Required\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Resource Pack Required"];
	0 -> 1;
	3	[comment="name: \"Has Add-on Packs\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Has Add-on Packs"];
	0 -> 3;
	5	[comment="name: \"Has Scripts\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Has Scripts"];
	0 -> 5;
	7	[comment="name: \"Force Server Packs Enabled\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Force Server Packs Enabled"];
	0 -> 7;
	9	[comment="name: \"Behavior Packs\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Behavior Packs"];
	0 -> 9;
	27	[comment="name: \"Resource Packs\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Resource Packs"];
	0 -> 27;
	47	[comment="name: \"CDN URLs\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="CDN URLs"];
	0 -> 47;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	10	[comment="name: \"Array Size\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	9 -> 10;
	12	[comment="name: \"example element\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	9 -> 12;
	10 -> 11;
	13	[comment="name: \"ID\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ID];
	12 -> 13;
	15	[comment="name: \"Version\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Version];
	12 -> 15;
	17	[comment="name: \"Size\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Size];
	12 -> 17;
	19	[comment="name: \"Content Key\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Content Key"];
	12 -> 19;
	21	[comment="name: \"Sub Pack Name\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sub Pack Name"];
	12 -> 21;
	23	[comment="name: \"Content Identity\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Content Identity"];
	12 -> 23;
	25	[comment="name: \"Has Scripts\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Has Scripts"];
	12 -> 25;
	13 -> 14;
	15 -> 16;
	17 -> 18;
	19 -> 20;
	21 -> 22;
	23 -> 24;
	25 -> 26;
	28	[comment="name: \"Array Size\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	27 -> 28;
	30	[comment="name: \"example element\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	27 -> 30;
	28 -> 29;
	31	[comment="name: \"ID\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ID];
	30 -> 31;
	33	[comment="name: \"Version\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Version];
	30 -> 33;
	35	[comment="name: \"Size\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Size];
	30 -> 35;
	37	[comment="name: \"Content Key\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Content Key"];
	30 -> 37;
	39	[comment="name: \"Sub Pack Name\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sub Pack Name"];
	30 -> 39;
	41	[comment="name: \"Content Identity\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Content Identity"];
	30 -> 41;
	43	[comment="name: \"Has Scripts\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Has Scripts"];
	30 -> 43;
	45	[comment="name: \"Is Ray Tracing Capable\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Ray Tracing Capable"];
	30 -> 45;
	31 -> 32;
	33 -> 34;
	35 -> 36;
	37 -> 38;
	39 -> 40;
	41 -> 42;
	43 -> 44;
	45 -> 46;
	48	[comment="name: \"Array Size\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	47 -> 48;
	50	[comment="name: \"example element\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	47 -> 50;
	48 -> 49;
	51	[comment="name: \"First\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=First];
	50 -> 51;
	53	[comment="name: \"Second\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Second];
	50 -> 53;
	51 -> 52;
	53 -> 54;
}

```

## 字段

/// define
ResourcePacksInfoPacket

Resource Pack Required：<!-- md:samp bool -->

- 类型：bool。

Has Add-on Packs：<!-- md:samp bool -->

- 类型：bool。

Has Scripts：<!-- md:samp bool -->

- 类型：bool。

Force Server Packs Enabled：<!-- md:samp bool -->

- 类型：bool。

Behavior Packs

Behavior Packs数组的大小：<!-- md:samp unsigned short -->

- 类型：unsigned short。

Behavior Packs的示例元素

ID：<!-- md:samp string -->

- 类型：string。

Version：<!-- md:samp string -->

- 类型：string。

Size：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。

Content Key：<!-- md:samp string -->

- 类型：string。

Sub Pack Name：<!-- md:samp string -->

- 类型：string。

Content Identity：<!-- md:samp string -->

- 类型：string。

Resource Packs

Resource Packs数组的大小：<!-- md:samp unsigned short -->

- 类型：unsigned short。

Resource Packs的示例元素

Is Ray Tracing Capable：<!-- md:samp bool -->

- 类型：bool。

CDN URLs

CDN URLs数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

CDN URLs的示例元素

First：<!-- md:samp string -->

- 类型：string。

Second：<!-- md:samp string -->

- 类型：string。


///

# <!-- md:samp PlayerFogPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerFogPacket -->数据包，数字ID是`160`。

## 结构

```viz
digraph PlayerFogPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"PlayerFogPacket\", typeName: \"\", id: 0, branchId: 160, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerFogPacket];
	1	[comment="name: \"Fog Stack\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"Stack of fog effects created by /fog \
command\"",
		label="Fog Stack"];
	0 -> 1;
	2	[comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	1 -> 2;
	4	[comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	1 -> 4;
	2 -> 3;
	5	[comment="name: \"Fog Effect\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Fog effect string from /fog command\"",
		label="Fog Effect"];
	4 -> 5;
	5 -> 6;
}

```

## 字段

/// define
PlayerFogPacket

Fog Stack

//// define
Fog Stack数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Fog Stack的示例元素

Fog Effect：<!-- md:samp string -->

- 类型：string。Fog effect string from /fog command


////



///

# <!-- md:samp ItemComponentPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemComponentPacket -->数据包，数字ID是`162`。

## 结构

```viz
digraph ItemComponentPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"CompoundTag\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
	}
	0	[comment="name: \"ItemComponentPacket\", typeName: \"\", id: 0, branchId: 162, recurseId: -1, attributes: 0, notes: \"\"",
		label=ItemComponentPacket];
	1	[comment="name: \"Items\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"Array of component based items\"",
		label=Items];
	0 -> 1;
	2	[comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	1 -> 2;
	4	[comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	1 -> 4;
	2 -> 3;
	5	[comment="name: \"ComponentItem name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="ComponentItem name"];
	4 -> 5;
	7	[comment="name: \"Component data\", typeName: \"CompoundTag\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"Compound tag members \
- itemname: string, itemid: short, itemcomponents: {[componentkey:string]: { ...component definition here... } } }\"",
		label="Component data"];
	4 -> 7;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
ItemComponentPacket

Items

Items数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Items的示例元素

ComponentItem name：<!-- md:samp string -->

- 类型：string。

Component data：[<!-- md:samp CompoundTag -->](refs/protocols/types/CompoundTag.md)

- 类型：CompoundTag。Compound tag members - item'name': string, item'id': short, itemcomponents: {[componentkey:string]: { ...component definition here... } } }


///

# <!-- md:samp UpdateClientInputLocksPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateClientInputLocksPacket -->数据包，数字ID是`196`。

## 结构

```viz
digraph UpdateClientInputLocksPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		4	[comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
	}
	0	[comment="name: \"UpdateClientInputLocksPacket\", typeName: \"\", id: 0, branchId: 196, recurseId: -1, attributes: 0, notes: \"\"",
		label=UpdateClientInputLocksPacket];
	1	[comment="name: \"Input Lock ComponentData\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Input Lock ComponentData"];
	0 -> 1;
	3	[comment="name: \"Server Pos\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Server Pos"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
UpdateClientInputLocksPacket

Input Lock ComponentData：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Server Pos：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。


///

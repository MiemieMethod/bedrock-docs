# <!-- md:samp CorrectPlayerMovePredictionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CorrectPlayerMovePredictionPacket -->数据包，数字ID是`161`。

## 结构

```viz
digraph CorrectPlayerMovePredictionPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"Vec3\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		4	[comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		8	[comment="name: \"unsigned varint64\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint64"];
		10	[comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"CorrectPlayerMovePredictionPacket\", typeName: \"\", id: 0, branchId: 161, recurseId: -1, attributes: 0, notes: \"\"",
		label=CorrectPlayerMovePredictionPacket];
	1	[comment="name: \"Pos\", typeName: \"Vec3\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"Corrected position\"",
		label=Pos];
	0 -> 1;
	3	[comment="name: \"Pos Delta\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Corrected velocity\"",
		label="Pos Delta"];
	0 -> 3;
	5	[comment="name: \"On Ground\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Is on ground\"",
		label="On Ground"];
	0 -> 5;
	7	[comment="name: \"Tick\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Which frame we're correcting; should match \
the tick in the Player Auth Input packet\"",
		label=Tick];
	0 -> 7;
	9	[comment="name: \"PredictionType\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"Vehicle or Player Prediction\"",
		label=PredictionType];
	0 -> 9;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
}

```

## 字段

/// define
CorrectPlayerMovePredictionPacket

Pos：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。Corrected position

Pos Delta：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。Corrected velocity

On Ground：<!-- md:samp bool -->

- 类型：bool。Is on ground

Tick：<!-- md:samp unsigned varint64 -->

- 类型：unsigned varint64。Which frame we're correcting; should match the tick in the Player Auth Input packet

PredictionType：<!-- md:samp byte -->

- 类型：byte。Vehicle or Player Prediction


///

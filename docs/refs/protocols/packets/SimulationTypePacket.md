# <!-- md:samp SimulationTypePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SimulationTypePacket -->数据包，数字ID是`168`。

## 结构

```dot
digraph SimulationTypePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"SimulationTypePacket\", typeName: \"\", id: 0, branchId: 168, recurseId: -1, attributes: 0, notes: \"\"",
		label=SimulationTypePacket];
	1	[comment="name: \"Sim Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SimulationType\"",
		label="Sim Type"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SimulationTypePacket

Sim Type：<!-- md:samp byte -->

- 类型：byte。enumeration: SimulationType


///

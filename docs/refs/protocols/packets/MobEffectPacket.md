# <!-- md:samp MobEffectPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MobEffectPacket -->数据包，数字ID是`28`。

## 结构

```viz
digraph MobEffectPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		8	[comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		10	[comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		12	[comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		14	[comment="name: \"unsigned int64\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
	}
	0	[comment="name: \"MobEffectPacket\", typeName: \"\", id: 0, branchId: 28, recurseId: -1, attributes: 0, notes: \"\"",
		label=MobEffectPacket];
	1	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Event ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MobEffectPacket::Event\"",
		label="Event ID"];
	0 -> 3;
	5	[comment="name: \"Effect ID\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Effect ID"];
	0 -> 5;
	7	[comment="name: \"Effect Amplifier\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Effect Amplifier"];
	0 -> 7;
	9	[comment="name: \"Show Particles\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Show Particles"];
	0 -> 9;
	11	[comment="name: \"Effect Duration Ticks\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Effect Duration Ticks"];
	0 -> 11;
	13	[comment="name: \"Tick\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Tick];
	0 -> 13;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
}

```

## 字段

/// define
MobEffectPacket

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Event ID：<!-- md:samp byte -->

- 类型：byte。enumeration: MobEffectPacket::Event

Effect ID：<!-- md:samp varint -->

- 类型：varint。

Effect Amplifier：<!-- md:samp varint -->

- 类型：varint。

Show Particles：<!-- md:samp bool -->

- 类型：bool。

Effect Duration Ticks：<!-- md:samp varint -->

- 类型：varint。

Tick：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。


///

# <!-- md:samp SpawnParticleEffectPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SpawnParticleEffectPacket -->数据包，数字ID是`118`。

## 结构

```dot
digraph SpawnParticleEffectPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		6	[comment="name: \"Vec3\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		18	[comment="name: \"std::optional<class MolangVariableMap>\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<class MolangVariableMap>"];
	}
	0	[comment="name: \"SpawnParticleEffectPacket\", typeName: \"\", id: 0, branchId: 118, recurseId: -1, attributes: 0, notes: \"\"",
		label=SpawnParticleEffectPacket];
	1	[comment="name: \"Dimension Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Dimension Id"];
	0 -> 1;
	3	[comment="name: \"Actor Id\", typeName: \"ActorUniqueID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Actor Id"];
	0 -> 3;
	5	[comment="name: \"Position\", typeName: \"Vec3\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 5;
	7	[comment="name: \"Effect Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Should be an effect that exists on \
the client. No-op if the effect doesn't exist.\"",
		label="Effect Name"];
	0 -> 7;
	9	[comment="name: \"Molang Variables\", typeName: \"std::optional<class MolangVariableMap>\", id: 9, branchId: 0, recurseId: -1, attributes: 256, \
notes: \"\"",
		label="Molang Variables"];
	0 -> 9;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 18;
}

```

## 字段

/// define
SpawnParticleEffectPacket

Dimension Id：<!-- md:samp byte -->

- 类型：byte。

Actor Id：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。

Position：[<!-- md:samp Vec3 -->](refs/protocols/types/Vec3.md)

- 类型：Vec3。

Effect Name：<!-- md:samp string -->

- 类型：string。Should be an effect that exists on the client. No-op if the effect doesn't exist.

Molang Variables：[<!-- md:samp std::optional<class MolangVariableMap> -->](refs/protocols/types/std::optional<class MolangVariableMap>.md)

- 类型：std::optional<class MolangVariableMap>。


///

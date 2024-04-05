# <!-- md:samp SpawnParticleEffectPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SpawnParticleEffectPacket -->数据包，数字ID是`118`。

## 结构

```viz
digraph "SpawnParticleEffectPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 18

0 [label="SpawnParticleEffectPacket",comment="name: \"SpawnParticleEffectPacket\", typeName: \"\", id: 0, branchId: 118, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Dimension Id",comment="name: \"Dimension Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Actor Id",comment="name: \"Actor Id\", typeName: \"ActorUniqueID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Effect Name",comment="name: \"Effect Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Should be an effect that exists on the client. No-op if the effect doesn't exist.\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Molang Variables",comment="name: \"Molang Variables\", typeName: \"std::optional<class MolangVariableMap>\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
18 [label="std::optional<class MolangVariableMap>",comment="name: \"std::optional<class MolangVariableMap>\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;18}

}

```

## 字段

/// define
SpawnParticleEffectPacket

Dimension Id：<!-- md:samp byte -->

- 类型：byte。

Actor Id：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 类型：ActorUniqueID。

Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。

Effect Name：<!-- md:samp string -->

- 类型：string。Should be an effect that exists on the client. No-op if the effect doesn't exist.

Molang Variables：[<!-- md:samp std::optional<class MolangVariableMap> -->](../types/std::optional<class_molangvariablemap>.md)

- 类型：std::optional<class MolangVariableMap>。


///

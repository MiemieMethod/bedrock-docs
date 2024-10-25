# <!-- md:samp SpawnParticleEffectPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp SpawnParticleEffectPacket -->数据包，数字ID是`118`。该数据包用于protocol.packet.spawnparticleeffectpacket.description

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

```title='SpawnParticleEffectPacket'
[dimension_id][actor_id][position][effect_name][molang_variables]
```

/// html | div.result
//// define
Dimension Id：<!-- md:samp byte -->

- 基本类型。protocol.packet.spawnparticleeffectpacket.dimension_id.description


////
//// define
Actor Id：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.spawnparticleeffectpacket.actor_id.description


////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.spawnparticleeffectpacket.position.description


////
//// define
Effect Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.spawnparticleeffectpacket.effect_name.descriptionShould be an effect that exists on the client. No-op if the effect doesn't exist.


////
//// define
Molang Variables：[<!-- md:samp std::optional&lt;class MolangVariableMap&gt; -->](../types/std__optional_class_molangvariablemap_.md)

- 特殊类型。protocol.packet.spawnparticleeffectpacket.molang_variables.description


////

///


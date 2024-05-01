# <!-- md:samp AddVolumeEntityPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp AddVolumeEntityPacket -->数据包，数字ID是`166`。该数据包用于protocol.packet.addvolumeentitypacket.description

## 结构

```viz
digraph "AddVolumeEntityPacket" {
rankdir = LR
0
0 -> 1
1 -> 5
0 -> 6
6 -> 7
0 -> 8
8 -> 9
0 -> 10
10 -> 11
0 -> 12
12 -> 13
0 -> 14
14 -> 15
0 -> 16
16 -> 17
0 -> 18
18 -> 19

0 [label="AddVolumeEntityPacket",comment="name: \"AddVolumeEntityPacket\", typeName: \"\", id: 0, branchId: 166, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Entity Network Id",comment="name: \"Entity Network Id\", typeName: \"EntityNetId\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
5 [label="EntityNetId",comment="name: \"EntityNetId\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="Components",comment="name: \"Components\", typeName: \"CompoundTag\", id: 6, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
7 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="JSON Identifier",comment="name: \"JSON Identifier\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="string",comment="name: \"string\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="Instance Name",comment="name: \"Instance Name\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="string",comment="name: \"string\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="Min Bounds",comment="name: \"Min Bounds\", typeName: \"NetworkBlockPosition\", id: 12, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
13 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="Max Bounds",comment="name: \"Max Bounds\", typeName: \"NetworkBlockPosition\", id: 14, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
15 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="Dimension Type",comment="name: \"Dimension Type\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
17 [label="varint",comment="name: \"varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="Engine Version",comment="name: \"Engine Version\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"Semantic version string\""];
19 [label="string",comment="name: \"string\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;5;7;9;11;13;15;17;19}

}

```

## 字段

```title='AddVolumeEntityPacket'
[entity_network_id][components][json_identifier][instance_name][min_bounds][max_bounds][dimension_type][engine_version]
```

/// html | div.result
//// define
Entity Network Id：[<!-- md:samp EntityNetId -->](../types/entitynetid.md)

- 特殊类型。protocol.packet.addvolumeentitypacket.entity_network_id.description


////
//// define
Components：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.addvolumeentitypacket.components.description


////
//// define
JSON Identifier：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.addvolumeentitypacket.json_identifier.description


////
//// define
Instance Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.addvolumeentitypacket.instance_name.description


////
//// define
Min Bounds：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.addvolumeentitypacket.min_bounds.description


////
//// define
Max Bounds：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.addvolumeentitypacket.max_bounds.description


////
//// define
Dimension Type：<!-- md:samp varint -->

- 基本类型。protocol.packet.addvolumeentitypacket.dimension_type.description


////
//// define
Engine Version：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.addvolumeentitypacket.engine_version.descriptionSemantic version string


////

///


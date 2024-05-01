# <!-- md:samp PlayerSkinPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PlayerSkinPacket -->数据包，数字ID是`93`。该数据包用于protocol.packet.playerskinpacket.description

## 结构

```viz
digraph "PlayerSkinPacket" {
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
9 -> 10

0 [label="PlayerSkinPacket",comment="name: \"PlayerSkinPacket\", typeName: \"\", id: 0, branchId: 93, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="UUID",comment="name: \"UUID\", typeName: \"mce::UUID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Serialized Skin",comment="name: \"Serialized Skin\", typeName: \"SerializedSkin\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="SerializedSkin",comment="name: \"SerializedSkin\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="New Skin Name",comment="name: \"New Skin Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Old Skin Name",comment="name: \"Old Skin Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Whether skin is trusted marketplace content",comment="name: \"Whether skin is trusted marketplace content\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="bool",comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='PlayerSkinPacket'
[uuid][serialized_skin][new_skin_name][old_skin_name][whether_skin_is_trusted_marketplace_content]
```

/// html | div.result
//// define
UUID：[<!-- md:samp mce::UUID -->](../types/mce__uuid.md)

- 特殊类型。protocol.packet.playerskinpacket.uuid.description


////
//// define
Serialized Skin：[<!-- md:samp SerializedSkin -->](../types/serializedskin.md)

- 特殊类型。protocol.packet.playerskinpacket.serialized_skin.description


////
//// define
New Skin Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.playerskinpacket.new_skin_name.description


////
//// define
Old Skin Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.playerskinpacket.old_skin_name.description


////
//// define
Whether skin is trusted marketplace content：<!-- md:samp bool -->

- 基本类型。protocol.packet.playerskinpacket.whether_skin_is_trusted_marketplace_content.description


////

///


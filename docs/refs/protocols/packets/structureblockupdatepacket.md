# <!-- md:samp StructureBlockUpdatePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StructureBlockUpdatePacket -->数据包，数字ID是`90`。该数据包用于protocol.packet.structureblockupdatepacket.description

## 结构

```viz
digraph "StructureBlockUpdatePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 48
0 -> 49
49 -> 50
0 -> 51
51 -> 52

0 [label="StructureBlockUpdatePacket",comment="name: \"StructureBlockUpdatePacket\", typeName: \"\", id: 0, branchId: 90, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Block Position",comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Structure Data",comment="name: \"Structure Data\", typeName: \"StructureEditorData\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
48 [label="StructureEditorData",comment="name: \"StructureEditorData\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
49 [label="Trigger?",comment="name: \"Trigger?\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
50 [label="bool",comment="name: \"bool\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
51 [label="IsWaterlogged",comment="name: \"IsWaterlogged\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
52 [label="bool",comment="name: \"bool\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;48;50;52}

}

```

## 字段

```title='StructureBlockUpdatePacket'
[block_position][structure_data][trigger][iswaterlogged]
```

/// html | div.result
//// define
Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.structureblockupdatepacket.block_position.description


////
//// define
Structure Data：[<!-- md:samp StructureEditorData -->](../types/structureeditordata.md)

- 特殊类型。protocol.packet.structureblockupdatepacket.structure_data.description


////
//// define
Trigger?：<!-- md:samp bool -->

- 基本类型。protocol.packet.structureblockupdatepacket.trigger.description


////
//// define
IsWaterlogged：<!-- md:samp bool -->

- 基本类型。protocol.packet.structureblockupdatepacket.iswaterlogged.description


////

///


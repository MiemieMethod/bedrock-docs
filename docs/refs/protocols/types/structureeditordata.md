# <!-- md:samp StructureEditorData -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp StructureEditorData -->类型。该类型用于protocol.type.structureeditordata.description

## 结构

```viz
digraph "StructureEditorData" {
rankdir = LR
4
4 -> 5
5 -> 6
4 -> 7
7 -> 8
4 -> 9
9 -> 10
4 -> 11
11 -> 12
4 -> 13
13 -> 14
4 -> 15
15 -> 45
4 -> 46
46 -> 47

4 [label="StructureEditorData",comment="name: \"StructureEditorData\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="Structure Name",comment="name: \"Structure Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Data Field",comment="name: \"Data Field\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Used for structure blocks in data mode.\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Should players be included?",comment="name: \"Should players be included?\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="bool",comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Should show bounding box?",comment="name: \"Should show bounding box?\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="bool",comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Structure Block Type",comment="name: \"Structure Block Type\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="varint",comment="name: \"varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Structure Settings",comment="name: \"Structure Settings\", typeName: \"StructureSettings\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
45 [label="StructureSettings",comment="name: \"StructureSettings\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
46 [label="Redstone Save Mode",comment="name: \"Redstone Save Mode\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
47 [label="varint",comment="name: \"varint\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;6;8;10;12;14;45;47}

}

```

## 字段

```title='StructureEditorData'
[structure_name][data_field][should_players_be_included][should_show_bounding_box][structure_block_type][structure_settings][redstone_save_mode]
```

/// html | div.result
//// define
Structure Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.structureeditordata.structure_name.description


////
//// define
Data Field：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.structureeditordata.data_field.descriptionUsed for structure blocks in data mode.


////
//// define
Should players be included?：<!-- md:samp bool -->

- 基本类型。protocol.type.structureeditordata.should_players_be_included.description


////
//// define
Should show bounding box?：<!-- md:samp bool -->

- 基本类型。protocol.type.structureeditordata.should_show_bounding_box.description


////
//// define
Structure Block Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.structureeditordata.structure_block_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Data`|`0`|protocol.enum.data|
  |`Save`|`1`|protocol.enum.save|
  |`Load`|`2`|protocol.enum.load|
  |`Corner`|`3`|protocol.enum.corner|
  |`Invalid`|`4`|protocol.enum.invalid|
  |`Export`|`5`|protocol.enum.export|
  |`_count`|`6`|protocol.enum._count|



////
//// define
Structure Settings：[<!-- md:samp StructureSettings -->](../types/structuresettings.md)

- 特殊类型。protocol.type.structureeditordata.structure_settings.description


////
//// define
Redstone Save Mode：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.structureeditordata.redstone_save_mode.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`SavesToMemory`|`0`|protocol.enum.savestomemory|
  |`SavesToDisk`|`1`|protocol.enum.savestodisk|



////

///


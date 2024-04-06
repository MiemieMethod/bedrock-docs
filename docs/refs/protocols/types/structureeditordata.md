# <!-- md:samp StructureEditorData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StructureEditorData -->类型。

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
13 [label="Structure Block Type",comment="name: \"Structure Block Type\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: StructureBlockType\""];
14 [label="varint",comment="name: \"varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Structure Settings",comment="name: \"Structure Settings\", typeName: \"StructureSettings\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
45 [label="StructureSettings",comment="name: \"StructureSettings\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
46 [label="Redstone Save Mode",comment="name: \"Redstone Save Mode\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: StructureRedstoneSaveMode\""];
47 [label="varint",comment="name: \"varint\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;6;8;10;12;14;45;47}

}

```

## 字段

```title='StructureEditorData'
[structure_name][data_field][should_players_be_included?][should_show_bounding_box?][structure_block_type][structure_settings][redstone_save_mode]
```

/// html | div.result
//// define
Structure Name：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Data Field：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。Used for structure blocks in data mode.


////
//// define
Should players be included?：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。


////
//// define
Should show bounding box?：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。


////
//// define
Structure Block Type：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Data`|`0`||
  |`Save`|`1`||
  |`Load`|`2`||
  |`Corner`|`3`||
  |`Invalid`|`4`||
  |`Export`|`5`||
  |`_count`|`6`||



////
//// define
Structure Settings：[<!-- md:samp StructureSettings -->](../types/structuresettings.md)

- 类型：<!-- md:samp StructureSettings -->。


////
//// define
Redstone Save Mode：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`SavesToMemory`|`0`||
  |`SavesToDisk`|`1`||



////

///


# <!-- md:samp StructureTemplateDataRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp StructureTemplateDataRequestPacket -->数据包，数字ID是`132`。

## 结构

```viz
digraph "StructureTemplateDataRequestPacket" {
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

0 [label="StructureTemplateDataRequestPacket",comment="name: \"StructureTemplateDataRequestPacket\", typeName: \"\", id: 0, branchId: 132, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Structure Name",comment="name: \"Structure Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Structure Position",comment="name: \"Structure Position\", typeName: \"NetworkBlockPosition\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Structure Settings",comment="name: \"Structure Settings\", typeName: \"StructureSettings\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="StructureSettings",comment="name: \"StructureSettings\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Requested Operation",comment="name: \"Requested Operation\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: StructureTemplateRequestOperation\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='StructureTemplateDataRequestPacket'
[structure_name][structure_position][structure_settings][requested_operation]
```

/// html | div.result
//// define
Structure Name：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////
//// define
Structure Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- <!-- md:samp NetworkBlockPosition -->类型。


////
//// define
Structure Settings：[<!-- md:samp StructureSettings -->](../types/structuresettings.md)

- <!-- md:samp StructureSettings -->类型。


////
//// define
Requested Operation：<!-- md:samp byte -->

- <!-- md:samp byte -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`ExportFromSaveMode`|`1`||
  |`ExportFromLoadMode`|`2`||
  |`QuerySavedStructure`|`3`||
  |`Import`|`4`||



////

///


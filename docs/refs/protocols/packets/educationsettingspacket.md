# <!-- md:samp EducationSettingsPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp EducationSettingsPacket -->数据包，数字ID是`137`。该数据包用于protocol.packet.educationsettingspacket.description

## 结构

```viz
digraph "EducationSettingsPacket" {
rankdir = LR
0
0 -> 1
1 -> 32

0 [label="EducationSettingsPacket",comment="name: \"EducationSettingsPacket\", typeName: \"\", id: 0, branchId: 137, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Education Level Settings",comment="name: \"Education Level Settings\", typeName: \"EducationLevelSettings\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
32 [label="EducationLevelSettings",comment="name: \"EducationLevelSettings\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;32}

}

```

## 字段

```title='EducationSettingsPacket'
[education_level_settings]
```

/// html | div.result
//// define
Education Level Settings：[<!-- md:samp EducationLevelSettings -->](../types/educationlevelsettings.md)

- 特殊类型。protocol.packet.educationsettingspacket.education_level_settings.description


////

///


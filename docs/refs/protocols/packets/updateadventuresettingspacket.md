# <!-- md:samp UpdateAdventureSettingsPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp UpdateAdventureSettingsPacket -->数据包，数字ID是`188`。该数据包用于protocol.packet.updateadventuresettingspacket.description

## 结构

```viz
digraph "UpdateAdventureSettingsPacket" {
rankdir = LR
0
0 -> 1
1 -> 13

0 [label="UpdateAdventureSettingsPacket",comment="name: \"UpdateAdventureSettingsPacket\", typeName: \"\", id: 0, branchId: 188, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Adventure Settings",comment="name: \"Adventure Settings\", typeName: \"AdventureSettings\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
13 [label="AdventureSettings",comment="name: \"AdventureSettings\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;13}

}

```

## 字段

```title='UpdateAdventureSettingsPacket'
[adventure_settings]
```

/// html | div.result
//// define
Adventure Settings：[<!-- md:samp AdventureSettings -->](../types/adventuresettings.md)

- 特殊类型。protocol.packet.updateadventuresettingspacket.adventure_settings.description


////

///


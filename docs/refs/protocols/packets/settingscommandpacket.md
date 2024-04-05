# <!-- md:samp SettingsCommandPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SettingsCommandPacket -->数据包，数字ID是`140`。

## 结构

```viz
digraph "SettingsCommandPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="SettingsCommandPacket",comment="name: \"SettingsCommandPacket\", typeName: \"\", id: 0, branchId: 140, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Command",comment="name: \"Command\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Command to update setting.\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Suppress Output?",comment="name: \"Suppress Output?\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='SettingsCommandPacket'
[command][suppress_output?]
```

/// html | div.result
//// define
Command：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。Command to update setting.


////
//// define
Suppress Output?：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。


////

///


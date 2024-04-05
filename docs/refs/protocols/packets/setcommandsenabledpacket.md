# <!-- md:samp SetCommandsEnabledPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetCommandsEnabledPacket -->数据包，数字ID是`59`。

## 结构

```viz
digraph "SetCommandsEnabledPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetCommandsEnabledPacket",comment="name: \"SetCommandsEnabledPacket\", typeName: \"\", id: 0, branchId: 59, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Commands Enabled",comment="name: \"Commands Enabled\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="bool",comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

/// define
SetCommandsEnabledPacket

Commands Enabled：<!-- md:samp bool -->

- 类型：bool。


///

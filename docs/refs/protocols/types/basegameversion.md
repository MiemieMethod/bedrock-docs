# <!-- md:samp BaseGameVersion -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BaseGameVersion -->类型。

## 结构

```viz
digraph "BaseGameVersion" {
rankdir = LR
24
24 -> 25
25 -> 26

24 [label="BaseGameVersion",comment="name: \"BaseGameVersion\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
25 [label="Base Game Version",comment="name: \"Base Game Version\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"Format: 0.0.0 (i.e. Major.Minor.Patch)\""];
26 [label="string",comment="name: \"string\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;26}

}

```

## 字段

```title='BaseGameVersion'
[base_game_version]
```

/// html | div.result
//// define
Base Game Version：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。Format: 0.0.0 (i.e. Major.Minor.Patch)


////

///


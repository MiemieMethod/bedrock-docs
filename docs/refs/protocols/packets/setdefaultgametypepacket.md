# <!-- md:samp SetDefaultGameTypePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetDefaultGameTypePacket -->数据包，数字ID是`105`。

## 结构

```viz
digraph "SetDefaultGameTypePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetDefaultGameTypePacket",comment="name: \"SetDefaultGameTypePacket\", typeName: \"\", id: 0, branchId: 105, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Default Game Type",comment="name: \"Default Game Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GameType\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetDefaultGameTypePacket'
[default_game_type]
```

/// html | div.result
//// define
Default Game Type：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。enumeration: GameType


////

///


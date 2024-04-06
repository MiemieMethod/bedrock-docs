# <!-- md:samp SetDifficultyPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetDifficultyPacket -->数据包，数字ID是`60`。

## 结构

```viz
digraph "SetDifficultyPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetDifficultyPacket",comment="name: \"SetDifficultyPacket\", typeName: \"\", id: 0, branchId: 60, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Difficulty",comment="name: \"Difficulty\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Difficulty\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetDifficultyPacket'
[difficulty]
```

/// html | div.result
//// define
Difficulty：<!-- md:samp unsigned varint -->

- <!-- md:samp unsigned varint -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Peaceful`|`0`||
  |`Easy`|`1`||
  |`Normal`|`2`||
  |`Hard`|`3`||
  |`Count`|`4`||
  |`Unknown`|`5`||



////

///


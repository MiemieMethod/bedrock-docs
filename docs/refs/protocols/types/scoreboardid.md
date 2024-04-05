# <!-- md:samp ScoreboardId -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ScoreboardId -->类型。

## 结构

```viz
digraph "ScoreboardId" {
rankdir = LR
8
8 -> 9
9 -> 10

8 [label="ScoreboardId",comment="name: \"ScoreboardId\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="Id",comment="name: \"Id\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;10}

}

```

## 字段

/// define
ScoreboardId

Id：<!-- md:samp varint64 -->

- 类型：varint64。


///

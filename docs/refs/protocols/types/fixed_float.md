# <!-- md:samp Fixed Float -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp Fixed Float -->类型。

## 结构

```viz
digraph "Fixed Float" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="Fixed Float",comment="name: \"Fixed Float\", typeName: \"\", id: 0, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Modified float value",comment="name: \"Modified float value\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Float value multiplied by 32\""];
2 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

/// define
Fixed Float

Modified float value：<!-- md:samp varint64 -->

- 类型：varint64。Float value multiplied by 32


///

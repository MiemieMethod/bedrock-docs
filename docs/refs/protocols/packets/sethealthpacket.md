# <!-- md:samp SetHealthPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetHealthPacket -->数据包，数字ID是`42`。

## 结构

```viz
digraph "SetHealthPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetHealthPacket",comment="name: \"SetHealthPacket\", typeName: \"\", id: 0, branchId: 42, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Health",comment="name: \"Health\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetHealthPacket'
[health]
```

/// html | div.result
//// define
Health：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。


////

///


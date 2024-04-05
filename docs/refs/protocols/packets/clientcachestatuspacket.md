# <!-- md:samp ClientCacheStatusPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ClientCacheStatusPacket -->数据包，数字ID是`129`。

## 结构

```viz
digraph "ClientCacheStatusPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="ClientCacheStatusPacket",comment="name: \"ClientCacheStatusPacket\", typeName: \"\", id: 0, branchId: 129, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Is cache supported?",comment="name: \"Is cache supported?\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="bool",comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

/// define
ClientCacheStatusPacket

Is cache supported?：<!-- md:samp bool -->

- 类型：bool。


///

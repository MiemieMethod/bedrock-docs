# <!-- md:samp ClientCacheStatusPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ClientCacheStatusPacket -->数据包，数字ID是`129`。该数据包用于protocol.packet.clientcachestatuspacket.description

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

```title='ClientCacheStatusPacket'
[is_cache_supported]
```

/// html | div.result
//// define
Is cache supported?：<!-- md:samp bool -->

- 基本类型。protocol.packet.clientcachestatuspacket.is_cache_supported.description


////

///


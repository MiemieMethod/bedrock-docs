# <!-- md:samp SetLocalPlayerAsInitializedPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetLocalPlayerAsInitializedPacket -->数据包，数字ID是`113`。

## 结构

```viz
digraph "SetLocalPlayerAsInitializedPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetLocalPlayerAsInitializedPacket",comment="name: \"SetLocalPlayerAsInitializedPacket\", typeName: \"\", id: 0, branchId: 113, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Player ID",comment="name: \"Player ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetLocalPlayerAsInitializedPacket'
[player_id]
```

/// html | div.result
//// define
Player ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。


////

///


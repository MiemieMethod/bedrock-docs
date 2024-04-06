# <!-- md:samp BlockActorDataPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BlockActorDataPacket -->数据包，数字ID是`56`。

## 结构

```viz
digraph "BlockActorDataPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="BlockActorDataPacket",comment="name: \"BlockActorDataPacket\", typeName: \"\", id: 0, branchId: 56, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Block Position",comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Actor Data Tags",comment="name: \"Actor Data Tags\", typeName: \"CompoundTag\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='BlockActorDataPacket'
[block_position][actor_data_tags]
```

/// html | div.result
//// define
Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。


////
//// define
Actor Data Tags：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。


////

///


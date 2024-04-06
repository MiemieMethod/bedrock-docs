# <!-- md:samp SyncActorPropertyPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SyncActorPropertyPacket -->数据包，数字ID是`165`。

## 结构

```viz
digraph "SyncActorPropertyPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SyncActorPropertyPacket",comment="name: \"SyncActorPropertyPacket\", typeName: \"\", id: 0, branchId: 165, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Property Data",comment="name: \"Property Data\", typeName: \"CompoundTag\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"type: actor identifier hash; properties: properties of actor that have been flagged for client sync as a sub-compound tag\""];
2 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SyncActorPropertyPacket'
[property_data]
```

/// html | div.result
//// define
Property Data：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- <!-- md:samp CompoundTag -->类型。type: actor 'id'entifier hash; properties: properties of actor that have been flagged for client sync as a sub-compound tag


////

///


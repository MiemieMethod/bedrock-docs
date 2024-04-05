# <!-- md:samp RemoveVolumeEntityPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RemoveVolumeEntityPacket -->数据包，数字ID是`167`。

## 结构

```viz
digraph "RemoveVolumeEntityPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="RemoveVolumeEntityPacket",comment="name: \"RemoveVolumeEntityPacket\", typeName: \"\", id: 0, branchId: 167, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Entity Network Id",comment="name: \"Entity Network Id\", typeName: \"EntityNetId\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="EntityNetId",comment="name: \"EntityNetId\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Dimension Type",comment="name: \"Dimension Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='RemoveVolumeEntityPacket'
[entity_network_id][dimension_type]
```

/// html | div.result
//// define
Entity Network Id：[<!-- md:samp EntityNetId -->](../types/entitynetid.md)

- 类型：<!-- md:samp EntityNetId -->。


////
//// define
Dimension Type：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。


////

///


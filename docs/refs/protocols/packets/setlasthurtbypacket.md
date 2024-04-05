# <!-- md:samp SetLastHurtByPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetLastHurtByPacket -->数据包，数字ID是`96`。

## 结构

```viz
digraph "SetLastHurtByPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetLastHurtByPacket",comment="name: \"SetLastHurtByPacket\", typeName: \"\", id: 0, branchId: 96, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Last Hurt By",comment="name: \"Last Hurt By\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorType\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetLastHurtByPacket'
[last_hurt_by]
```

/// html | div.result
//// define
Last Hurt By：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。enumeration: ActorType


////

///


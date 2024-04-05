# <!-- md:samp SimpleEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SimpleEventPacket -->数据包，数字ID是`64`。

## 结构

```viz
digraph "SimpleEventPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SimpleEventPacket",comment="name: \"SimpleEventPacket\", typeName: \"\", id: 0, branchId: 64, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Type",comment="name: \"Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SimpleEventPacket::Subtype\""];
2 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SimpleEventPacket'
[type]
```

/// html | div.result
//// define
Type：<!-- md:samp unsigned short -->

- 类型：<!-- md:samp unsigned short -->。enumeration: SimpleEventPacket::Subtype


////

///


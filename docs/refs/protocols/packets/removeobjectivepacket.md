# <!-- md:samp RemoveObjectivePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp RemoveObjectivePacket -->数据包，数字ID是`106`。该数据包用于protocol.packet.removeobjectivepacket.description

## 结构

```viz
digraph "RemoveObjectivePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="RemoveObjectivePacket",comment="name: \"RemoveObjectivePacket\", typeName: \"\", id: 0, branchId: 106, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Objective Name",comment="name: \"Objective Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='RemoveObjectivePacket'
[objective_name]
```

/// html | div.result
//// define
Objective Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.removeobjectivepacket.objective_name.description


////

///


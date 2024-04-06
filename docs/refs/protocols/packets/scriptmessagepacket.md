# <!-- md:samp ScriptMessagePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ScriptMessagePacket -->数据包，数字ID是`177`。

## 结构

```viz
digraph "ScriptMessagePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="ScriptMessagePacket",comment="name: \"ScriptMessagePacket\", typeName: \"\", id: 0, branchId: 177, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Message Id",comment="name: \"Message Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Message Value",comment="name: \"Message Value\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='ScriptMessagePacket'
[message_id][message_value]
```

/// html | div.result
//// define
Message Id：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////
//// define
Message Value：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////

///


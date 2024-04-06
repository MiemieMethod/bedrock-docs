# <!-- md:samp SubClientLoginPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SubClientLoginPacket -->数据包，数字ID是`94`。

## 结构

```viz
digraph "SubClientLoginPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SubClientLoginPacket",comment="name: \"SubClientLoginPacket\", typeName: \"\", id: 0, branchId: 94, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Sub Client Connection Request",comment="name: \"Sub Client Connection Request\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"see @subClientConnectionRequest.html#diagram@\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SubClientLoginPacket'
[sub_client_connection_request]
```

/// html | div.result
//// define
Sub Client Connection Request：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。see @subClientConnectionRequest.html#diagram@


////

///


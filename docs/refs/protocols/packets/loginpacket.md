# <!-- md:samp LoginPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LoginPacket -->数据包，数字ID是`1`。

## 结构

```viz
digraph "LoginPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="LoginPacket",comment="name: \"LoginPacket\", typeName: \"\", id: 0, branchId: 1, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Client Network Version",comment="name: \"Client Network Version\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="big endian int",comment="name: \"big endian int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Connection Request",comment="name: \"Connection Request\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"see @connectionRequest.html#diagram@\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

/// define
LoginPacket

Client Network Version：<!-- md:samp big endian int -->

- 类型：big endian int。

Connection Request：<!-- md:samp string -->

- 类型：string。see @connectionRequest.html#diagram@


///

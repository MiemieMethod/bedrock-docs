# <!-- md:samp LoginPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp LoginPacket -->数据包，数字ID是`1`。该数据包用于protocol.packet.loginpacket.description

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

```title='LoginPacket'
[client_network_version][connection_request]
```

/// html | div.result
//// define
Client Network Version：<!-- md:samp big endian int -->

- 基本类型。protocol.packet.loginpacket.client_network_version.description


////
//// define
Connection Request：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.loginpacket.connection_request.descriptionsee @connectionRequest.html#diagram@


////

///


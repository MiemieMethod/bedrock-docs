# <!-- md:samp TransferPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp TransferPacket -->数据包，数字ID是`85`。该数据包用于protocol.packet.transferpacket.description

## 结构

```viz
digraph "TransferPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="TransferPacket",comment="name: \"TransferPacket\", typeName: \"\", id: 0, branchId: 85, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Server Address",comment="name: \"Server Address\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Server Port",comment="name: \"Server Port\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Reload World",comment="name: \"Reload World\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='TransferPacket'
[server_address][server_port][reload_world]
```

/// html | div.result
//// define
Server Address：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.transferpacket.server_address.description


////
//// define
Server Port：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.transferpacket.server_port.description


////
//// define
Reload World：<!-- md:samp bool -->

- 基本类型。protocol.packet.transferpacket.reload_world.description


////

///


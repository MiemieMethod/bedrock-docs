# <!-- md:samp ContainerClosePacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ContainerClosePacket -->数据包，数字ID是`47`。该数据包用于protocol.packet.containerclosepacket.description

## 结构

```viz
digraph "ContainerClosePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="ContainerClosePacket",comment="name: \"ContainerClosePacket\", typeName: \"\", id: 0, branchId: 47, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Server Initiated Close",comment="name: \"Server Initiated Close\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"True if the server initiated the closing\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='ContainerClosePacket'
[container_id][server_initiated_close]
```

/// html | div.result
//// define
Container ID：<!-- md:samp byte -->

- 基本类型。protocol.packet.containerclosepacket.container_id.description


////
//// define
Server Initiated Close：<!-- md:samp bool -->

- 基本类型。protocol.packet.containerclosepacket.server_initiated_close.descriptionTrue if the server initiated the closing


////

///


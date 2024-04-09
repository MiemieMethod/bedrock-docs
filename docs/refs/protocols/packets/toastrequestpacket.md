# <!-- md:samp ToastRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ToastRequestPacket -->数据包，数字ID是`186`。该数据包用于protocol.packet.toastrequestpacket.description

## 结构

```viz
digraph "ToastRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="ToastRequestPacket",comment="name: \"ToastRequestPacket\", typeName: \"\", id: 0, branchId: 186, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Title",comment="name: \"Title\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Content",comment="name: \"Content\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='ToastRequestPacket'
[title][content]
```

/// html | div.result
//// define
Title：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.toastrequestpacket.title.description


////
//// define
Content：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.toastrequestpacket.content.description


////

///


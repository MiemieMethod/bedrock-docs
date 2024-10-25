# <!-- md:samp ModalFormRequestPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ModalFormRequestPacket -->数据包，数字ID是`100`。该数据包用于protocol.packet.modalformrequestpacket.description

## 结构

```viz
digraph "ModalFormRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="ModalFormRequestPacket",comment="name: \"ModalFormRequestPacket\", typeName: \"\", id: 0, branchId: 100, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Form ID",comment="name: \"Form ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Form UI JSON",comment="name: \"Form UI JSON\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='ModalFormRequestPacket'
[form_id][form_ui_json]
```

/// html | div.result
//// define
Form ID：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.modalformrequestpacket.form_id.description


////
//// define
Form UI JSON：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.modalformrequestpacket.form_ui_json.description


////

///


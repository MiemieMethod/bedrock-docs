# <!-- md:samp ModalFormResponsePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ModalFormResponsePacket -->数据包，数字ID是`101`。该数据包用于protocol.packet.modalformresponsepacket.description

## 结构

```viz
digraph "ModalFormResponsePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 7
0 -> 8
8 -> 12

0 [label="ModalFormResponsePacket",comment="name: \"ModalFormResponsePacket\", typeName: \"\", id: 0, branchId: 101, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Form ID",comment="name: \"Form ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="JSON Response",comment="name: \"JSON Response\", typeName: \"std::optional<class Json::Value>\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
7 [label="std::optional<class Json::Value>",comment="name: \"std::optional<class Json::Value>\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="Form Cancel Reason",comment="name: \"Form Cancel Reason\", typeName: \"std::optional<enum ModalFormCancelReason>\", id: 8, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
12 [label="std::optional<enum ModalFormCancelReason>",comment="name: \"std::optional<enum ModalFormCancelReason>\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;7;12}

}

```

## 字段

```title='ModalFormResponsePacket'
[form_id][json_response][form_cancel_reason]
```

/// html | div.result
//// define
Form ID：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.modalformresponsepacket.form_id.description


////
//// define
JSON Response：[<!-- md:samp std::optional&lt;class Json::Value&gt; -->](../types/std__optional_class_json__value_.md)

- 特殊类型。protocol.packet.modalformresponsepacket.json_response.description


////
//// define
Form Cancel Reason：[<!-- md:samp std::optional&lt;enum ModalFormCancelReason&gt; -->](../types/std__optional_enum_modalformcancelreason_.md)

- 特殊类型。protocol.packet.modalformresponsepacket.form_cancel_reason.description


////

///


# <!-- md:samp ModalFormResponsePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ModalFormResponsePacket -->数据包，数字ID是`101`。

## 结构

```dot
digraph ModalFormResponsePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		7	[comment="name: \"std::optional<class Json::Value>\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<class Json::Value>"];
		12	[comment="name: \"std::optional<enum ModalFormCancelReason>\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<enum ModalFormCancelReason>"];
	}
	0	[comment="name: \"ModalFormResponsePacket\", typeName: \"\", id: 0, branchId: 101, recurseId: -1, attributes: 0, notes: \"\"",
		label=ModalFormResponsePacket];
	1	[comment="name: \"Form ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Form ID"];
	0 -> 1;
	3	[comment="name: \"JSON Response\", typeName: \"std::optional<class Json::Value>\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="JSON Response"];
	0 -> 3;
	8	[comment="name: \"Form Cancel Reason\", typeName: \"std::optional<enum ModalFormCancelReason>\", id: 8, branchId: 0, recurseId: -1, attributes: \
256, notes: \"\"",
		label="Form Cancel Reason"];
	0 -> 8;
	1 -> 2;
	3 -> 7;
	8 -> 12;
}

```

## 字段

/// define
ModalFormResponsePacket

Form ID：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

JSON Response：[<!-- md:samp std::optional<class Json::Value> -->](refs/protocols/types/std::optional<class Json::Value>.md)

- 类型：std::optional<class Json::Value>。

Form Cancel Reason：[<!-- md:samp std::optional<enum ModalFormCancelReason> -->](refs/protocols/types/std::optional<enum ModalFormCancelReason>.md)

- 类型：std::optional<enum ModalFormCancelReason>。


///

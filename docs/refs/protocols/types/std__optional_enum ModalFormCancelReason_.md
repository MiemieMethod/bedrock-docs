# <!-- md:samp std::optional<enum ModalFormCancelReason> -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional<enum ModalFormCancelReason> -->类型。

## 结构

```dot
digraph "std::optional<enum ModalFormCancelReason>" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		11	[comment="name: \"bool\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	9	[comment="name: \"std::optional<enum ModalFormCancelReason>\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="std::optional<enum ModalFormCancelReason>"];
	10	[comment="name: \"Has Value\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data \
type, otherwise nothing\"",
		label="Has Value"];
	9 -> 10;
	10 -> 11;
}

```

## 字段

/// define
std::optional<enum ModalFormCancelReason>

Has Value：<!-- md:samp bool -->

- 类型：bool。If true, follow with appropriate data type, otherwise nothing


///

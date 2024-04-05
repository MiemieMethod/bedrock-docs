# <!-- md:samp ItemStackResponsePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackResponsePacket -->数据包，数字ID是`148`。

## 结构

```viz
digraph "ItemStackResponsePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 46

0 [label="ItemStackResponsePacket",comment="name: \"ItemStackResponsePacket\", typeName: \"\", id: 0, branchId: 148, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Responses",comment="name: \"Responses\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Response Info",comment="name: \"Response Info\", typeName: \"ItemStackResponseInfo\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
46 [label="ItemStackResponseInfo",comment="name: \"ItemStackResponseInfo\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;46}

}

```

## 字段

/// define
ItemStackResponsePacket

Responses

//// define
Responses数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Responses的示例元素

Response Info：[<!-- md:samp ItemStackResponseInfo -->](../types/itemstackresponseinfo.md)

- 类型：ItemStackResponseInfo。


////



///

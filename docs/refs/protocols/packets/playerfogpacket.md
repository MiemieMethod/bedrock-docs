# <!-- md:samp PlayerFogPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerFogPacket -->数据包，数字ID是`160`。

## 结构

```viz
digraph "PlayerFogPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6

0 [label="PlayerFogPacket",comment="name: \"PlayerFogPacket\", typeName: \"\", id: 0, branchId: 160, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Fog Stack",comment="name: \"Fog Stack\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"Stack of fog effects created by /fog command\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Fog Effect",comment="name: \"Fog Effect\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Fog effect string from /fog command\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6}

}

```

## 字段

/// define
PlayerFogPacket

Fog Stack

//// define
Fog Stack数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Fog Stack的示例元素

Fog Effect：<!-- md:samp string -->

- 类型：string。Fog effect string from /fog command


////



///

# <!-- md:samp PassengerJumpPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PassengerJumpPacket -->数据包，数字ID是`20`。

## 结构

```viz
digraph "PassengerJumpPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="PassengerJumpPacket",comment="name: \"PassengerJumpPacket\", typeName: \"\", id: 0, branchId: 20, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Jump Scale",comment="name: \"Jump Scale\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='PassengerJumpPacket'
[jump_scale]
```

/// html | div.result
//// define
Jump Scale：<!-- md:samp varint -->

- 基本类型。


////

///


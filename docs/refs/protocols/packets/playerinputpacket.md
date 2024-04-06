# <!-- md:samp PlayerInputPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerInputPacket -->数据包，数字ID是`57`。

## 结构

```viz
digraph "PlayerInputPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="PlayerInputPacket",comment="name: \"PlayerInputPacket\", typeName: \"\", id: 0, branchId: 57, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Move Vector",comment="name: \"Move Vector\", typeName: \"Vec2\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="Vec2",comment="name: \"Vec2\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Jumping",comment="name: \"Jumping\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Sneaking",comment="name: \"Sneaking\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='PlayerInputPacket'
[move_vector][jumping][sneaking]
```

/// html | div.result
//// define
Move Vector：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 特殊类型。


////
//// define
Jumping：<!-- md:samp bool -->

- 基本类型。


////
//// define
Sneaking：<!-- md:samp bool -->

- 基本类型。


////

///


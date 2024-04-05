# <!-- md:samp EmoteListPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp EmoteListPacket -->数据包，数字ID是`152`。

## 结构

```viz
digraph "EmoteListPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
3 -> 6
6 -> 7
7 -> 8

0 [label="EmoteListPacket",comment="name: \"EmoteListPacket\", typeName: \"\", id: 0, branchId: 152, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Runtime id",comment="name: \"Runtime id\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Emote piece ids",comment="name: \"Emote piece ids\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Piece id",comment="name: \"Piece id\", typeName: \"mce::UUID\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
8 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8}

}

```

## 字段

/// define
EmoteListPacket

Runtime id：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Emote piece ids

//// define
Emote piece ids数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Emote piece ids的示例元素

Piece id：[<!-- md:samp mce::UUID -->](../types/mce::uuid.md)

- 类型：mce::UUID。


////



///

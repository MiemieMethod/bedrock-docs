# <!-- md:samp UpdateBlockSyncedPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateBlockSyncedPacket -->数据包，数字ID是`110`。

## 结构

```viz
digraph "UpdateBlockSyncedPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10
0 -> 11
11 -> 12

0 [label="UpdateBlockSyncedPacket",comment="name: \"UpdateBlockSyncedPacket\", typeName: \"\", id: 0, branchId: 110, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Block Position",comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Block Runtime ID",comment="name: \"Block Runtime ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Flags",comment="name: \"Flags\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Layer",comment="name: \"Layer\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Unique Actor Id",comment="name: \"Unique Actor Id\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id for the Moving Block Actor\""];
10 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Actor Sync Message",comment="name: \"Actor Sync Message\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorBlockSyncMessage::MessageId\""];
12 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12}

}

```

## 字段

/// define
UpdateBlockSyncedPacket

Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Block Runtime ID：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Flags：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Layer：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Unique Actor Id：<!-- md:samp varint64 -->

- 类型：varint64。Id for the Moving Block Actor

Actor Sync Message：<!-- md:samp varint64 -->

- 类型：varint64。enumeration: ActorBlockSyncMessage::MessageId


///

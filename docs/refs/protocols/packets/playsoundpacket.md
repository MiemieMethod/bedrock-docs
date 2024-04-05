# <!-- md:samp PlaySoundPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlaySoundPacket -->数据包，数字ID是`86`。

## 结构

```viz
digraph "PlaySoundPacket" {
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

0 [label="PlaySoundPacket",comment="name: \"PlaySoundPacket\", typeName: \"\", id: 0, branchId: 86, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Name",comment="name: \"Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Position",comment="name: \"Position\", typeName: \"NetworkBlockPosition\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Volume",comment="name: \"Volume\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="float",comment="name: \"float\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Pitch",comment="name: \"Pitch\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="float",comment="name: \"float\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

/// define
PlaySoundPacket

Name：<!-- md:samp string -->

- 类型：string。

Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Volume：<!-- md:samp float -->

- 类型：float。

Pitch：<!-- md:samp float -->

- 类型：float。


///

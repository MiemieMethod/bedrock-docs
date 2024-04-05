# <!-- md:samp SetDisplayObjectivePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetDisplayObjectivePacket -->数据包，数字ID是`107`。

## 结构

```viz
digraph "SetDisplayObjectivePacket" {
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

0 [label="SetDisplayObjectivePacket",comment="name: \"SetDisplayObjectivePacket\", typeName: \"\", id: 0, branchId: 107, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Display Slot Name",comment="name: \"Display Slot Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Objective Name",comment="name: \"Objective Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Objective Display Name",comment="name: \"Objective Display Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Criteria Name",comment="name: \"Criteria Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Sort Order",comment="name: \"Sort Order\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ObjectiveSortOrder\""];
10 [label="byte",comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

/// define
SetDisplayObjectivePacket

Display Slot Name：<!-- md:samp string -->

- 类型：string。

Objective Name：<!-- md:samp string -->

- 类型：string。

Objective Display Name：<!-- md:samp string -->

- 类型：string。

Criteria Name：<!-- md:samp string -->

- 类型：string。

Sort Order：<!-- md:samp byte -->

- 类型：byte。enumeration: ObjectiveSortOrder


///

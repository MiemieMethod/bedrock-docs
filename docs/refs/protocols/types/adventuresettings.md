# <!-- md:samp AdventureSettings -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp AdventureSettings -->类型。该类型用于protocol.type.adventuresettings.description

## 结构

```viz
digraph "AdventureSettings" {
rankdir = LR
2
2 -> 3
3 -> 4
2 -> 5
5 -> 6
2 -> 7
7 -> 8
2 -> 9
9 -> 10
2 -> 11
11 -> 12

2 [label="AdventureSettings",comment="name: \"AdventureSettings\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="no PvM",comment="name: \"no PvM\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="no MvP",comment="name: \"no MvP\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Immutable World",comment="name: \"Immutable World\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="bool",comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Show Name Tags",comment="name: \"Show Name Tags\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="bool",comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Auto Jump",comment="name: \"Auto Jump\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="bool",comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;4;6;8;10;12}

}

```

## 字段

```title='AdventureSettings'
[no_pvm][no_mvp][immutable_world][show_name_tags][auto_jump]
```

/// html | div.result
//// define
no PvM：<!-- md:samp bool -->

- 基本类型。protocol.type.adventuresettings.no_pvm.description


////
//// define
no MvP：<!-- md:samp bool -->

- 基本类型。protocol.type.adventuresettings.no_mvp.description


////
//// define
Immutable World：<!-- md:samp bool -->

- 基本类型。protocol.type.adventuresettings.immutable_world.description


////
//// define
Show Name Tags：<!-- md:samp bool -->

- 基本类型。protocol.type.adventuresettings.show_name_tags.description


////
//// define
Auto Jump：<!-- md:samp bool -->

- 基本类型。protocol.type.adventuresettings.auto_jump.description


////

///


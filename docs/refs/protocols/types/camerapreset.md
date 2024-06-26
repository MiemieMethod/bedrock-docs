# <!-- md:samp CameraPreset -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp CameraPreset -->类型。该类型用于protocol.type.camerapreset.description

## 结构

```viz
digraph "CameraPreset" {
rankdir = LR
8
8 -> 9
9 -> 10
8 -> 11
11 -> 12
8 -> 13
13 -> 17
8 -> 18
18 -> 19
8 -> 20
20 -> 21
8 -> 22
22 -> 23
8 -> 24
24 -> 25
8 -> 26
26 -> 30
8 -> 31
31 -> 35

8 [label="CameraPreset",comment="name: \"CameraPreset\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="Name",comment="name: \"Name\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Inherit From",comment="name: \"Inherit From\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="string",comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Pos X",comment="name: \"Pos X\", typeName: \"std::optional<float>\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
17 [label="std::optional<float>",comment="name: \"std::optional<float>\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="Pos Y",comment="name: \"Pos Y\", typeName: \"std::optional<float>\", id: 18, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
19 [label="std::optional<float>",comment="name: \"std::optional<float>\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="Pos Z",comment="name: \"Pos Z\", typeName: \"std::optional<float>\", id: 20, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
21 [label="std::optional<float>",comment="name: \"std::optional<float>\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="Rot X",comment="name: \"Rot X\", typeName: \"std::optional<float>\", id: 22, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
23 [label="std::optional<float>",comment="name: \"std::optional<float>\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
24 [label="Rot Y",comment="name: \"Rot Y\", typeName: \"std::optional<float>\", id: 24, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
25 [label="std::optional<float>",comment="name: \"std::optional<float>\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="Listener",comment="name: \"Listener\", typeName: \"std::optional<enum CameraPreset::AudioListener>\", id: 26, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
30 [label="std::optional<enum CameraPreset::AudioListener>",comment="name: \"std::optional<enum CameraPreset::AudioListener>\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="Player Effects",comment="name: \"Player Effects\", typeName: \"std::optional<bool>\", id: 31, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
35 [label="std::optional<bool>",comment="name: \"std::optional<bool>\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;10;12;17;19;21;23;25;30;35}

}

```

## 字段

```title='CameraPreset'
[name][inherit_from][pos_x][pos_y][pos_z][rot_x][rot_y][listener][player_effects]
```

/// html | div.result
//// define
Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.camerapreset.name.description


////
//// define
Inherit From：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.camerapreset.inherit_from.description


////
//// define
Pos X：[<!-- md:samp std::optional&lt;float&gt; -->](../types/std__optional_float_.md)

- 特殊类型。protocol.type.camerapreset.pos_x.description


////
//// define
Pos Y：[<!-- md:samp std::optional&lt;float&gt; -->](../types/std__optional_float_.md)

- 特殊类型。protocol.type.camerapreset.pos_y.description


////
//// define
Pos Z：[<!-- md:samp std::optional&lt;float&gt; -->](../types/std__optional_float_.md)

- 特殊类型。protocol.type.camerapreset.pos_z.description


////
//// define
Rot X：[<!-- md:samp std::optional&lt;float&gt; -->](../types/std__optional_float_.md)

- 特殊类型。protocol.type.camerapreset.rot_x.description


////
//// define
Rot Y：[<!-- md:samp std::optional&lt;float&gt; -->](../types/std__optional_float_.md)

- 特殊类型。protocol.type.camerapreset.rot_y.description


////
//// define
Listener：[<!-- md:samp std::optional&lt;enum CameraPreset::AudioListener&gt; -->](../types/std__optional_enum_camerapreset__audiolistener_.md)

- 特殊类型。protocol.type.camerapreset.listener.description


////
//// define
Player Effects：[<!-- md:samp std::optional&lt;bool&gt; -->](../types/std__optional_bool_.md)

- 特殊类型。protocol.type.camerapreset.player_effects.description


////

///


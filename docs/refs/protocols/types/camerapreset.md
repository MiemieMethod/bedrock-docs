# <!-- md:samp CameraPreset -->

> 文档版本：r/21_u3<br/>协议版本：729

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
26 -> 27
8 -> 28
28 -> 32
8 -> 33
33 -> 37
8 -> 38
38 -> 42
8 -> 43
43 -> 44
8 -> 45
45 -> 49
8 -> 50
50 -> 51

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
26 [label="Rotation Speed",comment="name: \"Rotation Speed\", typeName: \"std::optional<float>\", id: 26, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
27 [label="std::optional<float>",comment="name: \"std::optional<float>\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="Snap to Target",comment="name: \"Snap to Target\", typeName: \"std::optional<bool>\", id: 28, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
32 [label="std::optional<bool>",comment="name: \"std::optional<bool>\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="View Offset",comment="name: \"View Offset\", typeName: \"std::optional<class Vec2>\", id: 33, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
37 [label="std::optional<class Vec2>",comment="name: \"std::optional<class Vec2>\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
38 [label="Entity Offset",comment="name: \"Entity Offset\", typeName: \"std::optional<class Vec3>\", id: 38, branchId: 0, recurseId: -1, attributes: 256, notes: \"Changing the camera's pivot point from the center of the entity\""];
42 [label="std::optional<class Vec3>",comment="name: \"std::optional<class Vec3>\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
43 [label="Radius",comment="name: \"Radius\", typeName: \"std::optional<float>\", id: 43, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
44 [label="std::optional<float>",comment="name: \"std::optional<float>\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
45 [label="Listener",comment="name: \"Listener\", typeName: \"std::optional<enum CameraPreset::AudioListener>\", id: 45, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
49 [label="std::optional<enum CameraPreset::AudioListener>",comment="name: \"std::optional<enum CameraPreset::AudioListener>\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
50 [label="Player Effects",comment="name: \"Player Effects\", typeName: \"std::optional<bool>\", id: 50, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
51 [label="std::optional<bool>",comment="name: \"std::optional<bool>\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;10;12;17;19;21;23;25;27;32;37;42;44;49;51}

}

```

## 字段

```title='CameraPreset'
[name][inherit_from][pos_x][pos_y][pos_z][rot_x][rot_y][rotation_speed][snap_to_target][view_offset][entity_offset][radius][listener][player_effects]
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
Rotation Speed：[<!-- md:samp std::optional&lt;float&gt; -->](../types/std__optional_float_.md)

- 特殊类型。protocol.type.camerapreset.rotation_speed.description


////
//// define
Snap to Target：[<!-- md:samp std::optional&lt;bool&gt; -->](../types/std__optional_bool_.md)

- 特殊类型。protocol.type.camerapreset.snap_to_target.description


////
//// define
View Offset：[<!-- md:samp std::optional&lt;class Vec2&gt; -->](../types/std__optional_class_vec2_.md)

- 特殊类型。protocol.type.camerapreset.view_offset.description


////
//// define
Entity Offset：[<!-- md:samp std::optional&lt;class Vec3&gt; -->](../types/std__optional_class_vec3_.md)

- 特殊类型。protocol.type.camerapreset.entity_offset.descriptionChanging the camera's pivot point from the center of the entity


////
//// define
Radius：[<!-- md:samp std::optional&lt;float&gt; -->](../types/std__optional_float_.md)

- 特殊类型。protocol.type.camerapreset.radius.description


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


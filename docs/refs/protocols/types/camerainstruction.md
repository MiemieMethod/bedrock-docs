# <!-- md:samp CameraInstruction -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp CameraInstruction -->类型。该类型用于protocol.type.camerainstruction.description

## 结构

```viz
digraph "CameraInstruction" {
rankdir = LR
2
2 -> 3
3 -> 7
2 -> 8
8 -> 9
2 -> 10
10 -> 14
2 -> 15
15 -> 19
2 -> 20
20 -> 21

2 [label="CameraInstruction",comment="name: \"CameraInstruction\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="Set",comment="name: \"Set\", typeName: \"std::optional<struct CameraInstruction::SetInstruction>\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
7 [label="std::optional<struct CameraInstruction::SetInstruction>",comment="name: \"std::optional<struct CameraInstruction::SetInstruction>\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="Clear",comment="name: \"Clear\", typeName: \"std::optional<bool>\", id: 8, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
9 [label="std::optional<bool>",comment="name: \"std::optional<bool>\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="Fade",comment="name: \"Fade\", typeName: \"std::optional<struct CameraInstruction::FadeInstruction>\", id: 10, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
14 [label="std::optional<struct CameraInstruction::FadeInstruction>",comment="name: \"std::optional<struct CameraInstruction::FadeInstruction>\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Target",comment="name: \"Target\", typeName: \"std::optional<struct CameraInstruction::TargetInstruction>\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
19 [label="std::optional<struct CameraInstruction::TargetInstruction>",comment="name: \"std::optional<struct CameraInstruction::TargetInstruction>\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="RemoveTarget",comment="name: \"RemoveTarget\", typeName: \"std::optional<bool>\", id: 20, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
21 [label="std::optional<bool>",comment="name: \"std::optional<bool>\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;7;9;14;19;21}

}

```

## 字段

```title='CameraInstruction'
[set][clear][fade][target][removetarget]
```

/// html | div.result
//// define
Set：[<!-- md:samp std::optional&lt;struct CameraInstruction::SetInstruction&gt; -->](../types/std__optional_struct_camerainstruction__setinstruction_.md)

- 特殊类型。protocol.type.camerainstruction.set.description


////
//// define
Clear：[<!-- md:samp std::optional&lt;bool&gt; -->](../types/std__optional_bool_.md)

- 特殊类型。protocol.type.camerainstruction.clear.description


////
//// define
Fade：[<!-- md:samp std::optional&lt;struct CameraInstruction::FadeInstruction&gt; -->](../types/std__optional_struct_camerainstruction__fadeinstruction_.md)

- 特殊类型。protocol.type.camerainstruction.fade.description


////
//// define
Target：[<!-- md:samp std::optional&lt;struct CameraInstruction::TargetInstruction&gt; -->](../types/std__optional_struct_camerainstruction__targetinstruction_.md)

- 特殊类型。protocol.type.camerainstruction.target.description


////
//// define
RemoveTarget：[<!-- md:samp std::optional&lt;bool&gt; -->](../types/std__optional_bool_.md)

- 特殊类型。protocol.type.camerainstruction.removetarget.description


////

///


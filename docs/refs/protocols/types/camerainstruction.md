# <!-- md:samp CameraInstruction -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CameraInstruction -->类型。

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

2 [label="CameraInstruction",comment="name: \"CameraInstruction\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="Set",comment="name: \"Set\", typeName: \"std::optional<struct CameraInstruction::SetInstruction>\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
7 [label="std::optional<struct CameraInstruction::SetInstruction>",comment="name: \"std::optional<struct CameraInstruction::SetInstruction>\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="Clear",comment="name: \"Clear\", typeName: \"std::optional<bool>\", id: 8, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
9 [label="std::optional<bool>",comment="name: \"std::optional<bool>\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="Fade",comment="name: \"Fade\", typeName: \"std::optional<struct CameraInstruction::FadeInstruction>\", id: 10, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
14 [label="std::optional<struct CameraInstruction::FadeInstruction>",comment="name: \"std::optional<struct CameraInstruction::FadeInstruction>\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;7;9;14}

}

```

## 字段

```title='CameraInstruction'
[set][clear][fade]
```

/// html | div.result
//// define
Set：[<!-- md:samp std::optional&lt;struct CameraInstruction::SetInstruction&gt; -->](../types/std__optional_struct_camerainstruction__setinstruction_.md)

- 类型：<!-- md:samp std::optional&lt;struct CameraInstruction::SetInstruction&gt; -->。


////
//// define
Clear：[<!-- md:samp std::optional&lt;bool&gt; -->](../types/std__optional_bool_.md)

- 类型：<!-- md:samp std::optional&lt;bool&gt; -->。


////
//// define
Fade：[<!-- md:samp std::optional&lt;struct CameraInstruction::FadeInstruction&gt; -->](../types/std__optional_struct_camerainstruction__fadeinstruction_.md)

- 类型：<!-- md:samp std::optional&lt;struct CameraInstruction::FadeInstruction&gt; -->。


////

///


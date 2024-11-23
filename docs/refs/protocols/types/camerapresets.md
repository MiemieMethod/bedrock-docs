# <!-- md:samp CameraPresets -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp CameraPresets -->类型。该类型用于protocol.type.camerapresets.description

## 结构

```viz
digraph "CameraPresets" {
rankdir = LR
2
2 -> 3
3 -> 4
4 -> 5
3 -> 6
6 -> 7
7 -> 60

2 [label="CameraPresets",comment="name: \"CameraPresets\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="Presets",comment="name: \"Presets\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Camera Preset",comment="name: \"Camera Preset\", typeName: \"CameraPreset\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
60 [label="CameraPreset",comment="name: \"CameraPreset\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;5;60}

}

```

## 字段

```title='CameraPresets'
[presets]
```

/// html | div.result
```title='Presets'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.camerapresets.presets.array_size.description


/////
```title='示例元素'
[camera_preset]
```

///// html | div.result
////// define
Camera Preset：[<!-- md:samp CameraPreset -->](../types/camerapreset.md)

- 特殊类型。protocol.type.camerapresets.presets.example_element.camera_preset.description


//////

/////

////

///


# <!-- md:samp CameraPresetsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CameraPresetsPacket -->数据包，数字ID是`198`。

## 结构

```viz
digraph "CameraPresetsPacket" {
rankdir = LR
0
0 -> 1
1 -> 37

0 [label="CameraPresetsPacket",comment="name: \"CameraPresetsPacket\", typeName: \"\", id: 0, branchId: 198, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Camera Presets",comment="name: \"Camera Presets\", typeName: \"CameraPresets\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
37 [label="CameraPresets",comment="name: \"CameraPresets\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;37}

}

```

## 字段

```title='CameraPresetsPacket'
[camera_presets]
```

/// html | div.result
//// define
Camera Presets：[<!-- md:samp CameraPresets -->](../types/camerapresets.md)

- 特殊类型。


////

///


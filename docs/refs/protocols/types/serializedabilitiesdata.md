# <!-- md:samp SerializedAbilitiesData -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp SerializedAbilitiesData -->类型。该类型用于protocol.type.serializedabilitiesdata.description

## 结构

```viz
digraph "SerializedAbilitiesData" {
rankdir = LR
80
80 -> 81
81 -> 82
80 -> 83
83 -> 84
80 -> 85
85 -> 86
80 -> 87
87 -> 88
88 -> 89
87 -> 90
90 -> 91
91 -> 103

80 [label="SerializedAbilitiesData",comment="name: \"SerializedAbilitiesData\", typeName: \"\", id: 80, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
81 [label="TargetPlayer.rawID",comment="name: \"TargetPlayer.rawID\", typeName: \"\", id: 81, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
82 [label="int64",comment="name: \"int64\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
83 [label="mPlayerPermissions",comment="name: \"mPlayerPermissions\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
84 [label="byte",comment="name: \"byte\", typeName: \"\", id: 84, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
85 [label="mCommandPermissions",comment="name: \"mCommandPermissions\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
86 [label="byte",comment="name: \"byte\", typeName: \"\", id: 86, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
87 [label="Layers",comment="name: \"Layers\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
88 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 88, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
89 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
90 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 90, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
91 [label="layers",comment="name: \"layers\", typeName: \"SerializedAbilitiesData::SerializedLayer\", id: 91, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
103 [label="SerializedAbilitiesData::SerializedLayer",comment="name: \"SerializedAbilitiesData::SerializedLayer\", typeName: \"\", id: 103, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;82;84;86;89;103}

}

```

## 字段

```title='SerializedAbilitiesData'
[targetplayer.rawid][mplayerpermissions][mcommandpermissions][layers]
```

/// html | div.result
//// define
TargetPlayer.rawID：<!-- md:samp int64 -->

- 基本类型。protocol.type.serializedabilitiesdata.targetplayer.rawid.description


////
//// define
mPlayerPermissions：<!-- md:samp byte -->

- 基本类型。protocol.type.serializedabilitiesdata.mplayerpermissions.description


////
//// define
mCommandPermissions：<!-- md:samp byte -->

- 基本类型。protocol.type.serializedabilitiesdata.mcommandpermissions.description


////
```title='Layers'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.serializedabilitiesdata.数组大小.description


/////
```title='示例元素'
[layers]
```

///// html | div.result
////// define
layers：[<!-- md:samp SerializedAbilitiesData::SerializedLayer -->](../types/serializedabilitiesdata__serializedlayer.md)

- 特殊类型。protocol.type.serializedabilitiesdata.layers.description


//////

/////

////

///


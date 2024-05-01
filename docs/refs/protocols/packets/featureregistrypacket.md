# <!-- md:samp FeatureRegistryPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp FeatureRegistryPacket -->数据包，数字ID是`191`。该数据包用于protocol.packet.featureregistrypacket.description

## 结构

```viz
digraph "FeatureRegistryPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6
4 -> 7
7 -> 8

0 [label="FeatureRegistryPacket",comment="name: \"FeatureRegistryPacket\", typeName: \"\", id: 0, branchId: 191, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="FeaturesDataList",comment="name: \"FeaturesDataList\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="feature Name",comment="name: \"feature Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Binary Json Output",comment="name: \"Binary Json Output\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6;8}

}

```

## 字段

```title='FeatureRegistryPacket'
[featuresdatalist]
```

/// html | div.result
```title='FeaturesDataList'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.featureregistrypacket.featuresdatalist.array_size.description


/////
```title='示例元素'
[feature_name][binary_json_output]
```

///// html | div.result
////// define
feature Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.featureregistrypacket.featuresdatalist.example_element.feature_name.description


//////
////// define
Binary Json Output：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.featureregistrypacket.featuresdatalist.example_element.binary_json_output.description


//////

/////

////

///


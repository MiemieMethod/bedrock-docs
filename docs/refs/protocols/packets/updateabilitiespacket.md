# <!-- md:samp UpdateAbilitiesPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateAbilitiesPacket -->数据包，数字ID是`187`。

## 结构

```viz
digraph "UpdateAbilitiesPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="UpdateAbilitiesPacket",comment="name: \"UpdateAbilitiesPacket\", typeName: \"\", id: 0, branchId: 187, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Data",comment="name: \"Data\", typeName: \"SerializedAbilitiesData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="SerializedAbilitiesData",comment="name: \"SerializedAbilitiesData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='UpdateAbilitiesPacket'
[data]
```

/// html | div.result
//// define
Data：[<!-- md:samp SerializedAbilitiesData -->](../types/serializedabilitiesdata.md)

- 特殊类型。


////

///


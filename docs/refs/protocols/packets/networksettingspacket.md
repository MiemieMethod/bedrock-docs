# <!-- md:samp NetworkSettingsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NetworkSettingsPacket -->数据包，数字ID是`143`。该数据包用于protocol.packet.networksettingspacket.description

## 结构

```viz
digraph "NetworkSettingsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10

0 [label="NetworkSettingsPacket",comment="name: \"NetworkSettingsPacket\", typeName: \"\", id: 0, branchId: 143, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Compression Threshold",comment="name: \"Compression Threshold\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Determines the smallest size of raw network payload to compress. OTE: 0 is disable compression, 1 is compress everything 1 byte or larger (so everything)\""];
2 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="CompressionAlgorithm",comment="name: \"CompressionAlgorithm\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PacketCompressionAlgorithm\""];
4 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Client Throttle Enabled",comment="name: \"Client Throttle Enabled\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Client Throttle Threshold",comment="name: \"Client Throttle Threshold\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Client Throttle Scalar",comment="name: \"Client Throttle Scalar\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="float",comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='NetworkSettingsPacket'
[compression_threshold][compressionalgorithm][client_throttle_enabled][client_throttle_threshold][client_throttle_scalar]
```

/// html | div.result
//// define
Compression Threshold：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.networksettingspacket.compression_threshold.descriptionDetermines the smallest size of raw network payload to compress. OTE: 0 is disable compression, 1 is compress everything 1 byte or larger (so everything)


////
//// define
CompressionAlgorithm：<!-- md:samp unsigned short -->

- 基本类型枚举。protocol.packet.networksettingspacket.compressionalgorithm.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ZLib`|`0`|protocol.enum.zlib|
  |`Snappy`|`1`|protocol.enum.snappy|
  |`None`|`0xffff`|无|



////
//// define
Client Throttle Enabled：<!-- md:samp bool -->

- 基本类型。protocol.packet.networksettingspacket.client_throttle_enabled.description


////
//// define
Client Throttle Threshold：<!-- md:samp byte -->

- 基本类型。protocol.packet.networksettingspacket.client_throttle_threshold.description


////
//// define
Client Throttle Scalar：<!-- md:samp float -->

- 基本类型。protocol.packet.networksettingspacket.client_throttle_scalar.description


////

///


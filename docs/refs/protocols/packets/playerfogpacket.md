# <!-- md:samp PlayerFogPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PlayerFogPacket -->数据包，数字ID是`160`。该数据包用于protocol.packet.playerfogpacket.description

## 结构

```viz
digraph "PlayerFogPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6

0 [label="PlayerFogPacket",comment="name: \"PlayerFogPacket\", typeName: \"\", id: 0, branchId: 160, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Fog Stack",comment="name: \"Fog Stack\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"Stack of fog effects created by /fog command\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Fog Effect",comment="name: \"Fog Effect\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Fog effect string from /fog command\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6}

}

```

## 字段

```title='PlayerFogPacket'
[fog_stack]
```

/// html | div.result
```title='Fog Stack'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.playerfogpacket.数组大小.description


/////
```title='示例元素'
[fog_effect]
```

///// html | div.result
////// define
Fog Effect：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.playerfogpacket.fog_effect.descriptionFog effect string from /fog command


//////

/////

////

///


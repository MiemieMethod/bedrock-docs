# <!-- md:samp UpdateClientInputLocksPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp UpdateClientInputLocksPacket -->数据包，数字ID是`196`。该数据包用于protocol.packet.updateclientinputlockspacket.description

## 结构

```viz
digraph "UpdateClientInputLocksPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="UpdateClientInputLocksPacket",comment="name: \"UpdateClientInputLocksPacket\", typeName: \"\", id: 0, branchId: 196, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Input Lock ComponentData",comment="name: \"Input Lock ComponentData\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Server Pos",comment="name: \"Server Pos\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='UpdateClientInputLocksPacket'
[input_lock_componentdata][server_pos]
```

/// html | div.result
//// define
Input Lock ComponentData：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.updateclientinputlockspacket.input_lock_componentdata.description


////
//// define
Server Pos：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.updateclientinputlockspacket.server_pos.description


////

///


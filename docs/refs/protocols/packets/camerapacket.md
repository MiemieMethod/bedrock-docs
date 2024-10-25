# <!-- md:samp CameraPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp CameraPacket -->数据包，数字ID是`73`。该数据包用于protocol.packet.camerapacket.description

## 结构

```viz
digraph "CameraPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="CameraPacket",comment="name: \"CameraPacket\", typeName: \"\", id: 0, branchId: 73, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Camera ID",comment="name: \"Camera ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Target Player ID",comment="name: \"Target Player ID\", typeName: \"ActorUniqueID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='CameraPacket'
[camera_id][target_player_id]
```

/// html | div.result
//// define
Camera ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.camerapacket.camera_id.description


////
//// define
Target Player ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.camerapacket.target_player_id.description


////

///


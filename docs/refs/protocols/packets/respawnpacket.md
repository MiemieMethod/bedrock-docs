# <!-- md:samp RespawnPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp RespawnPacket -->数据包，数字ID是`45`。该数据包用于protocol.packet.respawnpacket.description

## 结构

```viz
digraph "RespawnPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="RespawnPacket",comment="name: \"RespawnPacket\", typeName: \"\", id: 0, branchId: 45, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="State",comment="name: \"State\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Player Runtime Id",comment="name: \"Player Runtime Id\", typeName: \"ActorRuntimeID\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='RespawnPacket'
[position][state][player_runtime_id]
```

/// html | div.result
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.respawnpacket.position.description


////
//// define
State：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.respawnpacket.state.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`SearchingForSpawn`|`0`|protocol.enum.searchingforspawn|
  |`ReadyToSpawn`|`1`|protocol.enum.readytospawn|
  |`ClientReadyToSpawn`|`2`|protocol.enum.clientreadytospawn|



////
//// define
Player Runtime Id：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.respawnpacket.player_runtime_id.description


////

///


# <!-- md:samp RespawnPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RespawnPacket -->数据包，数字ID是`45`。

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
3 [label="State",comment="name: \"State\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayerRespawnState\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Player Runtime Id",comment="name: \"Player Runtime Id\", typeName: \"ActorRuntimeID\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

/// define
RespawnPacket

Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。

State：<!-- md:samp byte -->

- 类型：byte。enumeration: PlayerRespawnState

Player Runtime Id：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。


///

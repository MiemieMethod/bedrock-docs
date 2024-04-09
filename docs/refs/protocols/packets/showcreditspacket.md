# <!-- md:samp ShowCreditsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ShowCreditsPacket -->数据包，数字ID是`75`。该数据包用于protocol.packet.showcreditspacket.description

## 结构

```viz
digraph "ShowCreditsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="ShowCreditsPacket",comment="name: \"ShowCreditsPacket\", typeName: \"\", id: 0, branchId: 75, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Player Runtime ID",comment="name: \"Player Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Credits State",comment="name: \"Credits State\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ShowCreditsPacket::CreditsState\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='ShowCreditsPacket'
[player_runtime_id][credits_state]
```

/// html | div.result
//// define
Player Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.showcreditspacket.player_runtime_id.description


////
//// define
Credits State：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.showcreditspacket.credits_state.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Start`|`0`|protocol.enum.start|
  |`Finished`|`1`|protocol.enum.finished|



////

///


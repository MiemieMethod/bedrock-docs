# <!-- md:samp ActorEventPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ActorEventPacket -->数据包，数字ID是`27`。该数据包用于通信活动对象事件。

## 结构

```viz
digraph "ActorEventPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="ActorEventPacket",comment="name: \"ActorEventPacket\", typeName: \"\", id: 0, branchId: 27, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Data",comment="name: \"Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='ActorEventPacket'
[target_runtime_id][event_id][data]
```

/// html | div.result
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。目标活动对象的运行时标识符。


////
//// define
Event ID：<!-- md:samp byte -->

- 基本类型。事件标识符。


////
//// define
Data：<!-- md:samp varint -->

- 基本类型。protocol.packet.actoreventpacket.data.description


////

///


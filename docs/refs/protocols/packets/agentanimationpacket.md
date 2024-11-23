# <!-- md:samp AgentAnimationPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp AgentAnimationPacket -->数据包，数字ID是`304`。该数据包用于protocol.packet.agentanimationpacket.description

## 结构

```viz
digraph "AgentAnimationPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="AgentAnimationPacket",comment="name: \"AgentAnimationPacket\", typeName: \"\", id: 0, branchId: 304, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Agent Animation",comment="name: \"Agent Animation\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Runtime Id",comment="name: \"Runtime Id\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='AgentAnimationPacket'
[agent_animation][runtime_id]
```

/// html | div.result
//// define
Agent Animation：<!-- md:samp byte -->

- 基本类型。protocol.packet.agentanimationpacket.agent_animation.description


////
//// define
Runtime Id：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.agentanimationpacket.runtime_id.description


////

///


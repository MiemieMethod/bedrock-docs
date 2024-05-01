# <!-- md:samp AgentActionEventPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp AgentActionEventPacket -->数据包，数字ID是`181`。该数据包用于protocol.packet.agentactioneventpacket.description

## 结构

```viz
digraph "AgentActionEventPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="AgentActionEventPacket",comment="name: \"AgentActionEventPacket\", typeName: \"\", id: 0, branchId: 181, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Request Id",comment="name: \"Request Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Action",comment="name: \"Action\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="int",comment="name: \"int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Response",comment="name: \"Response\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='AgentActionEventPacket'
[request_id][action][response]
```

/// html | div.result
//// define
Request Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.agentactioneventpacket.request_id.description


////
//// define
Action：<!-- md:samp int -->

- 基本类型。protocol.packet.agentactioneventpacket.action.description


////
//// define
Response：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.agentactioneventpacket.response.description


////

///


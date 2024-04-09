# <!-- md:samp AgentActionEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

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
3 [label="Request Id",comment="name: \"Request Id\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: AgentActionType\""];
4 [label="int",comment="name: \"int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Response",comment="name: \"Response\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='AgentActionEventPacket'
[request_id][request_id][response]
```

/// html | div.result
//// define
Request Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.agentactioneventpacket.request_id.description


////
//// define
Request Id：<!-- md:samp int -->

- 基本类型枚举。protocol.packet.agentactioneventpacket.request_id.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Attack`|`1`|protocol.enum.attack|
  |`Collect`|`2`|protocol.enum.collect|
  |`Destroy`|`3`|protocol.enum.destroy|
  |`DetectRedstone`|`4`|protocol.enum.detectredstone|
  |`DetectObstacle`|`5`|protocol.enum.detectobstacle|
  |`Drop`|`6`|protocol.enum.drop|
  |`DropAll`|`7`|protocol.enum.dropall|
  |`Inspect`|`8`|protocol.enum.inspect|
  |`InspectData`|`9`|protocol.enum.inspectdata|
  |`InspectItemCount`|`10`|protocol.enum.inspectitemcount|
  |`InspectItemDetail`|`11`|protocol.enum.inspectitemdetail|
  |`InspectItemSpace`|`12`|protocol.enum.inspectitemspace|
  |`Interact`|`13`|protocol.enum.interact|
  |`Move`|`14`|protocol.enum.move|
  |`PlaceBlock`|`15`|protocol.enum.placeblock|
  |`Till`|`16`|protocol.enum.till|
  |`TransferItemTo`|`17`|protocol.enum.transferitemto|
  |`Turn`|`18`|protocol.enum.turn|



////
//// define
Response：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.agentactioneventpacket.response.description


////

///


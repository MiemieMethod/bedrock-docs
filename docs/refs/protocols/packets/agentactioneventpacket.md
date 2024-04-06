# <!-- md:samp AgentActionEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AgentActionEventPacket -->数据包，数字ID是`181`。

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

- <!-- md:samp string -->类型。


////
//// define
Request Id：<!-- md:samp int -->

- <!-- md:samp int -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Attack`|`1`||
  |`Collect`|`2`||
  |`Destroy`|`3`||
  |`DetectRedstone`|`4`||
  |`DetectObstacle`|`5`||
  |`Drop`|`6`||
  |`DropAll`|`7`||
  |`Inspect`|`8`||
  |`InspectData`|`9`||
  |`InspectItemCount`|`10`||
  |`InspectItemDetail`|`11`||
  |`InspectItemSpace`|`12`||
  |`Interact`|`13`||
  |`Move`|`14`||
  |`PlaceBlock`|`15`||
  |`Till`|`16`||
  |`TransferItemTo`|`17`||
  |`Turn`|`18`||



////
//// define
Response：[<!-- md:samp string -->](../types/string.md)

- <!-- md:samp string -->类型。


////

///


# <!-- md:samp CodeBuilderSourcePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp CodeBuilderSourcePacket -->数据包，数字ID是`178`。该数据包用于protocol.packet.codebuildersourcepacket.description

## 结构

```viz
digraph "CodeBuilderSourcePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="CodeBuilderSourcePacket",comment="name: \"CodeBuilderSourcePacket\", typeName: \"\", id: 0, branchId: 178, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Operation",comment="name: \"Operation\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Category",comment="name: \"Category\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="CodeStatus",comment="name: \"CodeStatus\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='CodeBuilderSourcePacket'
[operation][category][codestatus]
```

/// html | div.result
//// define
Operation：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.codebuildersourcepacket.operation.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Get`|`1`|protocol.enum.get|
  |`Set`|`2`|protocol.enum.set|
  |`Reset`|`3`|protocol.enum.reset|



////
//// define
Category：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.codebuildersourcepacket.category.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`CodeStatus`|`1`|protocol.enum.codestatus|
  |`Instantiation`|`2`|protocol.enum.instantiation|



////
//// define
CodeStatus：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.codebuildersourcepacket.codestatus.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`NotStarted`|`1`|protocol.enum.notstarted|
  |`InProgress`|`2`|protocol.enum.inprogress|
  |`Paused`|`3`|protocol.enum.paused|
  |`Error`|`4`|protocol.enum.error|
  |`Succeeded`|`5`|protocol.enum.succeeded|



////

///


# <!-- md:samp CompletedUsingItemPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp CompletedUsingItemPacket -->数据包，数字ID是`142`。该数据包用于protocol.packet.completedusingitempacket.description

## 结构

```viz
digraph "CompletedUsingItemPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="CompletedUsingItemPacket",comment="name: \"CompletedUsingItemPacket\", typeName: \"\", id: 0, branchId: 142, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="short",comment="name: \"short\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Item Use Method",comment="name: \"Item Use Method\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="int",comment="name: \"int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='CompletedUsingItemPacket'
[item_id][item_use_method]
```

/// html | div.result
//// define
Item Id：<!-- md:samp short -->

- 基本类型。protocol.packet.completedusingitempacket.item_id.description


////
//// define
Item Use Method：<!-- md:samp int -->

- 基本类型枚举。protocol.packet.completedusingitempacket.item_use_method.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`-1`|protocol.enum.unknown|
  |`EquipArmor`|`0`|protocol.enum.equiparmor|
  |`Eat`|`1`|protocol.enum.eat|
  |`Attack`|`2`|protocol.enum.attack|
  |`Consume`|`3`|protocol.enum.consume|
  |`Throw`|`4`|protocol.enum.throw|
  |`Shoot`|`5`|protocol.enum.shoot|
  |`Place`|`6`|protocol.enum.place|
  |`FillBottle`|`7`|protocol.enum.fillbottle|
  |`FillBucket`|`8`|protocol.enum.fillbucket|
  |`PourBucket`|`9`|protocol.enum.pourbucket|
  |`UseTool`|`10`|protocol.enum.usetool|
  |`Interact`|`11`|protocol.enum.interact|
  |`Retrieved`|`12`|protocol.enum.retrieved|
  |`Dyed`|`13`|protocol.enum.dyed|
  |`Traded`|`14`|protocol.enum.traded|
  |`BrushingCompleted`|`15`|protocol.enum.brushingcompleted|
  |`OpenedVault`|`16`|protocol.enum.openedvault|
  |`_Count`|`17`|protocol.enum._count|



////

///


# <!-- md:samp AnimateEntityPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AnimateEntityPacket -->数据包，数字ID是`158`。该数据包用于protocol.packet.animateentitypacket.description

## 结构

```viz
digraph "AnimateEntityPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10
0 -> 11
11 -> 12
0 -> 13
13 -> 14
14 -> 15
13 -> 16
16 -> 17
17 -> 18

0 [label="AnimateEntityPacket",comment="name: \"AnimateEntityPacket\", typeName: \"\", id: 0, branchId: 158, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="mAnimation",comment="name: \"mAnimation\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"The name of the animation that the specified entities are to play.\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="mNextState",comment="name: \"mNextState\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"The next state to transition to once the specified animation is finished playing.\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="mStopExpression",comment="name: \"mStopExpression\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"The stop expression, the the condition that determines when to transition to the next state.\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Stop expression molang version",comment="name: \"Stop expression molang version\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MolangVersion\""];
8 [label="int",comment="name: \"int\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="mController",comment="name: \"mController\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"The name of an animation controller\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="mBlendOutTime",comment="name: \"mBlendOutTime\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"The amount of time to blend out of this animation\""];
12 [label="float",comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="mRuntimeIds",comment="name: \"mRuntimeIds\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"ActorRuntimeIDs of the entities that will play the specified animation\""];
14 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
17 [label="runtimeId",comment="name: \"runtimeId\", typeName: \"ActorRuntimeID\", id: 17, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
18 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;15;18}

}

```

## 字段

```title='AnimateEntityPacket'
[manimation][mnextstate][mstopexpression][stop_expression_molang_version][mcontroller][mblendouttime][mruntimeids]
```

/// html | div.result
//// define
mAnimation：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.animateentitypacket.manimation.descriptionThe 'name' of the animation that the specified entities are to play.


////
//// define
mNextState：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.animateentitypacket.mnextstate.descriptionThe next state to transition to once the specified animation is finished playing.


////
//// define
mStopExpression：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.animateentitypacket.mstopexpression.descriptionThe stop expression, the the condition that determines when to transition to the next state.


////
//// define
Stop expression molang version：<!-- md:samp int -->

- 基本类型枚举。protocol.packet.animateentitypacket.stop_expression_molang_version.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`-1`|protocol.enum.invalid|
  |`BeforeVersioning`|`0`|protocol.enum.beforeversioning|
  |`Initial`|`1`|protocol.enum.initial|
  |`FixedItemRemainingUseDurationQuery`|`2`|protocol.enum.fixeditemremainingusedurationquery|
  |`ExpressionErrorMessages`|`3`|protocol.enum.expressionerrormessages|
  |`UnexpectedOperatorErrors`|`4`|protocol.enum.unexpectedoperatorerrors|
  |`ConditionalOperatorAssociativity`|`5`|protocol.enum.conditionaloperatorassociativity|
  |`ComparisonAndLogicalOperatorPrecedence`|`6`|protocol.enum.comparisonandlogicaloperatorprecedence|
  |`DivideByNegativeValue`|`7`|protocol.enum.dividebynegativevalue|
  |`FixedCapeFlapAmountQuery`|`8`|protocol.enum.fixedcapeflapamountquery|
  |`QueryBlockPropertyRenamedToState`|`9`|protocol.enum.queryblockpropertyrenamedtostate|
  |`DeprecateOldBlockQueryNames`|`10`|protocol.enum.deprecateoldblockquerynames|
  |`DeprecatedSnifferAndCamelQueries`|`11`|protocol.enum.deprecatedsnifferandcamelqueries|
  |`LeafSupportingInFirstSolidBlockBelow`|`12`|protocol.enum.leafsupportinginfirstsolidblockbelow|
  |`NumValidVersions`|`13`|protocol.enum.numvalidversions|
  |`Latest`|`NumValidVersions - 1`|protocol.enum.latest|
  |`HardcodedMolang`|`Latest`|protocol.enum.hardcodedmolang|



////
//// define
mController：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.animateentitypacket.mcontroller.descriptionThe 'name' of an animation controller


////
//// define
mBlendOutTime：<!-- md:samp float -->

- 基本类型。protocol.packet.animateentitypacket.mblendouttime.descriptionThe amount of time to blend out of this animation


////
```title='mRuntimeIds'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.animateentitypacket.数组大小.description


/////
```title='示例元素'
[runtimeid]
```

///// html | div.result
////// define
runtimeId：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.animateentitypacket.runtimeid.description


//////

/////

////

///


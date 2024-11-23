# <!-- md:samp InteractPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp InteractPacket -->数据包，数字ID是`33`。该数据包用于protocol.packet.interactpacket.description

## 结构

```viz
digraph "InteractPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
6 -> 7
5 -> 8
8 -> 9
9 -> 10
8 -> 11
11 -> 12
8 -> 13
13 -> 14

0 [label="InteractPacket",comment="name: \"InteractPacket\", typeName: \"\", id: 0, branchId: 33, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Action",comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Action == InteractUpdate || Action == StopRiding'",shape=note,comment="name: \"Dependency on 'Action == InteractUpdate || Action == StopRiding'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 8, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
9 [label="Position X",comment="name: \"Position X\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="float",comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Position Y",comment="name: \"Position Y\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="float",comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Position Z",comment="name: \"Position Z\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="float",comment="name: \"float\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;7;10;12;14}

}

```

## 字段

```title='InteractPacket'
[action][target_runtime_id][dependency_on_action_is_interactupdate_or_action_is_stopriding]
```

/// html | div.result
//// define
Action：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.interactpacket.action.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Invalid`|`0`|protocol.enum.invalid|
  |`StopRiding`|`3`|protocol.enum.stopriding|
  |`InteractUpdate`|`4`|protocol.enum.interactupdate|
  |`NpcOpen`|`5`|protocol.enum.npcopen|
  |`OpenInventory`|`6`|protocol.enum.openinventory|



////
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.interactpacket.target_runtime_id.description


////
> 依赖于`Action == InteractUpdate || Action == StopRiding`

///// tab | `Action == InteractUpdate || Action == StopRiding`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Action == InteractUpdate || Action == StopRiding`如果为`1`
```title='if (1)'
[position_x][position_y][position_z]
```

////// html | div.result
/////// define
Position X：<!-- md:samp float -->

- 基本类型。protocol.packet.interactpacket.dependency_on_action_is_interactupdate_or_action_is_stopriding.if_1.position_x.description


///////
/////// define
Position Y：<!-- md:samp float -->

- 基本类型。protocol.packet.interactpacket.dependency_on_action_is_interactupdate_or_action_is_stopriding.if_1.position_y.description


///////
/////// define
Position Z：<!-- md:samp float -->

- 基本类型。protocol.packet.interactpacket.dependency_on_action_is_interactupdate_or_action_is_stopriding.if_1.position_z.description


///////

//////

/////

///


# <!-- md:samp AnimatePacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp AnimatePacket -->数据包，数字ID是`44`。该数据包用于protocol.packet.animatepacket.description

## 结构

```viz
digraph "AnimatePacket" {
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

0 [label="AnimatePacket",comment="name: \"AnimatePacket\", typeName: \"\", id: 0, branchId: 44, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Action",comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Action'",shape=note,comment="name: \"Dependency on 'Action'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 8, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
9 [label="Rowing Time",comment="name: \"Rowing Time\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"Only written for rowing actions\""];
10 [label="float",comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;7;10}

}

```

## 字段

```title='AnimatePacket'
[action][target_runtime_id][dependency_on_action]
```

/// html | div.result
//// define
Action：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.animatepacket.action.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NoAction`|`0`|protocol.enum.noaction|
  |`Swing`|`1`|protocol.enum.swing|
  |`WakeUp`|`3`|protocol.enum.wakeup|
  |`CriticalHit`|`4`|protocol.enum.criticalhit|
  |`MagicCriticalHit`|`5`|protocol.enum.magiccriticalhit|
  |`RowRight`|`128`|protocol.enum.rowright|
  |`RowLeft`|`129`|protocol.enum.rowleft|



////
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.animatepacket.target_runtime_id.description


////
> 依赖于`Action`

///// tab | `Action`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Action`如果为`1`
```title='if (1)'
[rowing_time]
```

////// html | div.result
/////// define
Rowing Time：<!-- md:samp float -->

- 基本类型。protocol.packet.animatepacket.dependency_on_action.if_1.rowing_time.descriptionOnly written for rowing actions


///////

//////

/////

///


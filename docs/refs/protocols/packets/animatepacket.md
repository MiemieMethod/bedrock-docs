# <!-- md:samp AnimatePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AnimatePacket -->数据包，数字ID是`44`。

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
5 -> 10
10 -> 11
5 -> 12
12 -> 13
5 -> 14
14 -> 15
5 -> 16
16 -> 17
17 -> 18
5 -> 19
19 -> 20
20 -> 21

0 [label="AnimatePacket",comment="name: \"AnimatePacket\", typeName: \"\", id: 0, branchId: 44, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Action",comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: AnimatePacket::Action\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Action'",shape=note,comment="name: \"Dependency on 'Action'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 8, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
9 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 10, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
11 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 12, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
13 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="if (5)",shape=diamond,comment="name: \"if (5)\", typeName: \"\", id: 14, branchId: 5, recurseId: -1, attributes: 4, notes: \"\""];
15 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="if (128)",shape=diamond,comment="name: \"if (128)\", typeName: \"\", id: 16, branchId: 128, recurseId: -1, attributes: 4, notes: \"\""];
17 [label="Rowing Time",comment="name: \"Rowing Time\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="float",comment="name: \"float\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="if (129)",shape=diamond,comment="name: \"if (129)\", typeName: \"\", id: 19, branchId: 129, recurseId: -1, attributes: 4, notes: \"\""];
20 [label="Rowing Time",comment="name: \"Rowing Time\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
21 [label="float",comment="name: \"float\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;7;9;11;13;15;18;21}

}

```

## 字段

```title='AnimatePacket'
[action][target_runtime_id][dependency_on_action]
```

/// html | div.result
//// define
Action：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NoAction`|`0`||
  |`Swing`|`1`||
  |`WakeUp`|`3`||
  |`CriticalHit`|`4`||
  |`MagicCriticalHit`|`5`||
  |`RowRight`|`128`||
  |`RowLeft`|`129`||



////
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。


////
> 依赖于`Action`

///// tab | `Action`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Action`如果为`1`
////// define
if (1)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Action`如果为`3`
////// define
if (3)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Action`如果为`4`
////// define
if (4)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Action`如果为`5`
////// define
if (5)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Action`如果为`128`
```title='if (128)'
[rowing_time]
```

////// html | div.result
/////// define
Rowing Time：<!-- md:samp float -->

- 基本类型。


///////

//////

/////

///// tab | `Action`如果为`129`
```title='if (129)'
[rowing_time]
```

////// html | div.result
/////// define
Rowing Time：<!-- md:samp float -->

- 基本类型。


///////

//////

/////

///

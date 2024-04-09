# <!-- md:samp MapItemTrackedActor::UniqueId -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MapItemTrackedActor::UniqueId -->类型。该类型用于protocol.type.mapitemtrackedactor::uniqueid.description

## 结构

```viz
digraph "MapItemTrackedActor::UniqueId" {
rankdir = LR
42
42 -> 43
43 -> 44
42 -> 45
45 -> 46
46 -> 47
47 -> 48
45 -> 49
49 -> 50
50 -> 51
45 -> 52
52 -> 53

42 [label="MapItemTrackedActor::UniqueId",comment="name: \"MapItemTrackedActor::UniqueId\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
43 [label="Type",comment="name: \"Type\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MapItemTrackedActor::Type\""];
44 [label="int",comment="name: \"int\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
45 [label="Dependency on 'Type'",shape=note,comment="name: \"Dependency on 'Type'\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
46 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
47 [label="Unique ID",comment="name: \"Unique ID\", typeName: \"ActorUniqueID\", id: 47, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
48 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
49 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 49, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
50 [label="Block position",comment="name: \"Block position\", typeName: \"NetworkBlockPosition\", id: 50, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
51 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
52 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 52, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
53 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;44;48;51;53}

}

```

## 字段

```title='MapItemTrackedActor::UniqueId'
[type][dependency_on_type]
```

/// html | div.result
//// define
Type：<!-- md:samp int -->

- 基本类型枚举。protocol.type.mapitemtrackedactor::uniqueid.type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Entity`|`0`|protocol.enum.entity|
  |`BlockEntity`|`1`|protocol.enum.blockentity|
  |`Other`|`2`|protocol.enum.other|
  |`COUNT`|`3`|protocol.enum.count|



////
> 依赖于`Type`

///// tab | `Type`如果为`0`
```title='if (0)'
[unique_id]
```

////// html | div.result
/////// define
Unique ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.type.mapitemtrackedactor::uniqueid.unique_id.description


///////

//////

/////

///// tab | `Type`如果为`1`
```title='if (1)'
[block_position]
```

////// html | div.result
/////// define
Block position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.type.mapitemtrackedactor::uniqueid.block_position.description


///////

//////

/////

///// tab | `Type`如果为`2`
////// define
if (2)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///


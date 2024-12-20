# <!-- md:samp InventorySource -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp InventorySource -->类型。该类型用于protocol.type.inventorysource.description

## 结构

```viz
digraph "InventorySource" {
rankdir = LR
30
30 -> 31
31 -> 32
30 -> 33
33 -> 34
34 -> 35
35 -> 36
33 -> 37
37 -> 38
33 -> 39
39 -> 40
40 -> 41
33 -> 42
42 -> 43

30 [label="InventorySource",comment="name: \"InventorySource\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
31 [label="Source Type",comment="name: \"Source Type\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Dependency on 'Source Type'",shape=note,comment="name: \"Dependency on 'Source Type'\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
34 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
35 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
36 [label="varint",comment="name: \"varint\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 37, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
38 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
39 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 39, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
40 [label="Bit Flags",comment="name: \"Bit Flags\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
41 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
42 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 42, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
43 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;32;36;38;41;43}

}

```

## 字段

```title='InventorySource'
[source_type][dependency_on_source_type]
```

/// html | div.result
//// define
Source Type：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.type.inventorysource.source_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`InvalidInventory`|`std::numeric_limits<uint32_t>::max()`|protocol.enum.invalidinventory|
  |`ContainerInventory`|`0`|protocol.enum.containerinventory|
  |`GlobalInventory`|`1`|protocol.enum.globalinventory|
  |`WorldInteraction`|`2`|protocol.enum.worldinteraction|
  |`CreativeInventory`|`3`|protocol.enum.creativeinventory|
  |`NonImplementedFeatureTODO`|`99999`|protocol.enum.nonimplementedfeaturetodo|



////
> 依赖于`Source Type`

///// tab | `Source Type`如果为`0`
```title='if (0)'
[container_id]
```

////// html | div.result
/////// define
Container ID：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.inventorysource.dependency_on_source_type.if_0.container_id.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`CONTAINER_ID_NONE`|`-1`|protocol.enum.container_id_none|
  |`CONTAINER_ID_INVENTORY`|`0`|protocol.enum.container_id_inventory|
  |`CONTAINER_ID_FIRST`|`1`|protocol.enum.container_id_first|
  |`CONTAINER_ID_LAST`|`100`|protocol.enum.container_id_last|
  |`CONTAINER_ID_OFFHAND`|`119`|protocol.enum.container_id_offhand|
  |`CONTAINER_ID_ARMOR`|`120`|protocol.enum.container_id_armor|
  |`CONTAINER_ID_SELECTION_SLOTS`|`122`|protocol.enum.container_id_selection_slots|
  |`CONTAINER_ID_PLAYER_ONLY_UI`|`124`|protocol.enum.container_id_player_only_ui|
  |`CONTAINER_ID_REGISTRY`|`125`|protocol.enum.container_id_registry|



///////

//////

/////

///// tab | `Source Type`如果为`1`
////// define
if (1)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Source Type`如果为`2`
```title='if (2)'
[bit_flags]
```

////// html | div.result
/////// define
Bit Flags：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.type.inventorysource.dependency_on_source_type.if_2.bit_flags.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NoFlag`|`0`|protocol.enum.noflag|
  |`WorldInteraction_Random`|`1`|protocol.enum.worldinteraction_random|



///////

//////

/////

///// tab | `Source Type`如果为`3`
////// define
if (3)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///


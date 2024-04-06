# <!-- md:samp ContainerSetDataPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ContainerSetDataPacket -->数据包，数字ID是`51`。

## 结构

```viz
digraph "ContainerSetDataPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="ContainerSetDataPacket",comment="name: \"ContainerSetDataPacket\", typeName: \"\", id: 0, branchId: 51, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="ID",comment="name: \"ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Value",comment="name: \"Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='ContainerSetDataPacket'
[container_id][id][value]
```

/// html | div.result
//// define
Container ID：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`CONTAINER_ID_NONE`|`-1`||
  |`CONTAINER_ID_INVENTORY`|`0`||
  |`CONTAINER_ID_FIRST`|`1`||
  |`CONTAINER_ID_LAST`|`100`||
  |`CONTAINER_ID_OFFHAND`|`119`||
  |`CONTAINER_ID_ARMOR`|`120`||
  |`CONTAINER_ID_SELECTION_SLOTS`|`122`||
  |`CONTAINER_ID_PLAYER_ONLY_UI`|`124`||



////
//// define
ID：<!-- md:samp varint -->

- 基本类型。


////
//// define
Value：<!-- md:samp varint -->

- 基本类型。


////

///

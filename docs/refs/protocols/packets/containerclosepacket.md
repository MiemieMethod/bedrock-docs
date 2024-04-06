# <!-- md:samp ContainerClosePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ContainerClosePacket -->数据包，数字ID是`47`。

## 结构

```viz
digraph "ContainerClosePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="ContainerClosePacket",comment="name: \"ContainerClosePacket\", typeName: \"\", id: 0, branchId: 47, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Server Initiated Close",comment="name: \"Server Initiated Close\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"True if the server initiated the closing\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='ContainerClosePacket'
[container_id][server_initiated_close]
```

/// html | div.result
//// define
Container ID：<!-- md:samp byte -->

- 类型：<!-- md:samp byte -->。枚举值如下：

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
Server Initiated Close：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。True if the server initiated the closing


////

///


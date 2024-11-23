# <!-- md:samp ContainerClosePacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ContainerClosePacket -->数据包，数字ID是`47`。该数据包用于protocol.packet.containerclosepacket.description

## 结构

```viz
digraph "ContainerClosePacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="ContainerClosePacket",comment="name: \"ContainerClosePacket\", typeName: \"\", id: 0, branchId: 47, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Container ID",comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Container Type",comment="name: \"Container Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Server Initiated Close",comment="name: \"Server Initiated Close\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"True if the server initiated the closing\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='ContainerClosePacket'
[container_id][container_type][server_initiated_close]
```

/// html | div.result
//// define
Container ID：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.containerclosepacket.container_id.description枚举值如下：

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



////
//// define
Container Type：<!-- md:samp byte -->

- 基本类型。protocol.packet.containerclosepacket.container_type.description


////
//// define
Server Initiated Close：<!-- md:samp bool -->

- 基本类型。protocol.packet.containerclosepacket.server_initiated_close.descriptionTrue if the server initiated the closing


////

///


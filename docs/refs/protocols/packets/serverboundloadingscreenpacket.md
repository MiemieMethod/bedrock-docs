# <!-- md:samp ServerboundLoadingScreenPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ServerboundLoadingScreenPacket -->数据包，数字ID是`312`。该数据包用于protocol.packet.serverboundloadingscreenpacket.description

## 结构

```viz
digraph "ServerboundLoadingScreenPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="ServerboundLoadingScreenPacket",comment="name: \"ServerboundLoadingScreenPacket\", typeName: \"\", id: 0, branchId: 312, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Loading Screen Packet Type",comment="name: \"Loading Screen Packet Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Loading Screen Id",comment="name: \"Loading Screen Id\", typeName: \"std::optional<unsigned int>\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"This will be set if the server gives us a value. If the server doesn't expect this value, then the client will get disconnected.\""];
4 [label="std::optional<unsigned int>",comment="name: \"std::optional<unsigned int>\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='ServerboundLoadingScreenPacket'
[loading_screen_packet_type][loading_screen_id]
```

/// html | div.result
//// define
Loading Screen Packet Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.serverboundloadingscreenpacket.loading_screen_packet_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Unknown`|`0`|protocol.enum.unknown|
  |`StartLoadingScreen`|`1`|protocol.enum.startloadingscreen|
  |`EndLoadingScreen`|`2`|protocol.enum.endloadingscreen|



////
//// define
Loading Screen Id：[<!-- md:samp std::optional&lt;unsigned int&gt; -->](../types/std__optional_unsigned_int_.md)

- 特殊类型。protocol.packet.serverboundloadingscreenpacket.loading_screen_id.descriptionThis will be set if the server gives us a value. If the server doesn't expect this value, then the client will get disconnected.


////

///


# <!-- md:samp ShowStoreOfferPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ShowStoreOfferPacket -->数据包，数字ID是`91`。该数据包用于protocol.packet.showstoreofferpacket.description

## 结构

```viz
digraph "ShowStoreOfferPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="ShowStoreOfferPacket",comment="name: \"ShowStoreOfferPacket\", typeName: \"\", id: 0, branchId: 91, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Product ID",comment="name: \"Product ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Redirect Type",comment="name: \"Redirect Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='ShowStoreOfferPacket'
[product_id][redirect_type]
```

/// html | div.result
//// define
Product ID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.showstoreofferpacket.product_id.description


////
//// define
Redirect Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.showstoreofferpacket.redirect_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`MarketplaceOffer`|`0`|protocol.enum.marketplaceoffer|
  |`DressingRoomOffer`|`1`|protocol.enum.dressingroomoffer|
  |`ThirdPartyServerPage`|`2`|protocol.enum.thirdpartyserverpage|
  |`Count`|`3`|protocol.enum.count|



////

///


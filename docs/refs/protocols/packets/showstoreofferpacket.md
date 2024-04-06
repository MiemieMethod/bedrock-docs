# <!-- md:samp ShowStoreOfferPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ShowStoreOfferPacket -->数据包，数字ID是`91`。

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
3 [label="Redirect Type",comment="name: \"Redirect Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ShowStoreOfferRedirectType\""];
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
Product ID：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Redirect Type：<!-- md:samp byte -->

- 类型：<!-- md:samp byte -->。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`MarketplaceOffer`|`0`||
  |`DressingRoomOffer`|`1`||
  |`ThirdPartyServerPage`|`2`||
  |`Count`|`3`||



////

///


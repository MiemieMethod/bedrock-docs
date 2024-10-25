# <!-- md:samp ItemData -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ItemData -->类型。该类型用于protocol.type.itemdata.description

## 结构

```viz
digraph "ItemData" {
rankdir = LR
180
180 -> 181
181 -> 182
180 -> 183
183 -> 184
180 -> 185
185 -> 186

180 [label="ItemData",comment="name: \"ItemData\", typeName: \"\", id: 180, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
181 [label="Item Name",comment="name: \"Item Name\", typeName: \"\", id: 181, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
182 [label="string",comment="name: \"string\", typeName: \"\", id: 182, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
183 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 183, branchId: 0, recurseId: -1, attributes: 0, notes: \"Block id's < 256 (can be negative); Item id's > 257\""];
184 [label="short",comment="name: \"short\", typeName: \"\", id: 184, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
185 [label="Is Component Based",comment="name: \"Is Component Based\", typeName: \"\", id: 185, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
186 [label="bool",comment="name: \"bool\", typeName: \"\", id: 186, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;182;184;186}

}

```

## 字段

```title='ItemData'
[item_name][item_id][is_component_based]
```

/// html | div.result
//// define
Item Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.itemdata.item_name.description


////
//// define
Item Id：<!-- md:samp short -->

- 基本类型。protocol.type.itemdata.item_id.descriptionBlock 'id''s < 256 (can be negative); Item 'id''s > 257


////
//// define
Is Component Based：<!-- md:samp bool -->

- 基本类型。protocol.type.itemdata.is_component_based.description


////

///


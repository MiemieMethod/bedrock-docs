# <!-- md:samp ItemData -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ItemData -->类型。该类型用于protocol.type.itemdata.description

## 结构

```viz
digraph "ItemData" {
rankdir = LR
174
174 -> 175
175 -> 176
174 -> 177
177 -> 178
174 -> 179
179 -> 180

174 [label="ItemData",comment="name: \"ItemData\", typeName: \"\", id: 174, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
175 [label="Item Name",comment="name: \"Item Name\", typeName: \"\", id: 175, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
176 [label="string",comment="name: \"string\", typeName: \"\", id: 176, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
177 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 177, branchId: 0, recurseId: -1, attributes: 0, notes: \"Block id's < 256 (can be negative); Item id's > 257\""];
178 [label="short",comment="name: \"short\", typeName: \"\", id: 178, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
179 [label="Is Component Based",comment="name: \"Is Component Based\", typeName: \"\", id: 179, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
180 [label="bool",comment="name: \"bool\", typeName: \"\", id: 180, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;176;178;180}

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


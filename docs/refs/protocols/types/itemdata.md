# <!-- md:samp ItemData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemData -->类型。

## 结构

```viz
digraph "ItemData" {
rankdir = LR
172
172 -> 173
173 -> 174
172 -> 175
175 -> 176
172 -> 177
177 -> 178

172 [label="ItemData",comment="name: \"ItemData\", typeName: \"\", id: 172, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
173 [label="Item Name",comment="name: \"Item Name\", typeName: \"\", id: 173, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
174 [label="string",comment="name: \"string\", typeName: \"\", id: 174, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
175 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 175, branchId: 0, recurseId: -1, attributes: 0, notes: \"Block id's < 256 (can be negative); Item id's > 257\""];
176 [label="short",comment="name: \"short\", typeName: \"\", id: 176, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
177 [label="Is Component Based",comment="name: \"Is Component Based\", typeName: \"\", id: 177, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
178 [label="bool",comment="name: \"bool\", typeName: \"\", id: 178, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;174;176;178}

}

```

## 字段

```title='ItemData'
[item_name][item_id][is_component_based]
```

/// html | div.result
//// define
Item Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////
//// define
Item Id：<!-- md:samp short -->

- 基本类型。Block 'id''s < 256 (can be negative); Item 'id''s > 257


////
//// define
Is Component Based：<!-- md:samp bool -->

- 基本类型。


////

///

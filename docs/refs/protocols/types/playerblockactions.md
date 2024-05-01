# <!-- md:samp PlayerBlockActions -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp PlayerBlockActions -->类型。该类型用于protocol.type.playerblockactions.description

## 结构

```viz
digraph "PlayerBlockActions" {
rankdir = LR
118
118 -> 119
119 -> 120
120 -> 121
119 -> 122
122 -> 123
123 -> 158

118 [label="PlayerBlockActions",comment="name: \"PlayerBlockActions\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
119 [label="Player Block Actions",comment="name: \"Player Block Actions\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
120 [label="Player Block Actions count",comment="name: \"Player Block Actions count\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
121 [label="varint",comment="name: \"varint\", typeName: \"\", id: 121, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
122 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 122, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
123 [label="Player Block Action",comment="name: \"Player Block Action\", typeName: \"PlayerBlockActionData\", id: 123, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
158 [label="PlayerBlockActionData",comment="name: \"PlayerBlockActionData\", typeName: \"\", id: 158, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;121;158}

}

```

## 字段

```title='PlayerBlockActions'
[player_block_actions]
```

/// html | div.result
```title='Player Block Actions'
[player_block_actions_count][[example_element]..]
```

//// html | div.result
///// define
Player Block Actions count：<!-- md:samp varint -->

- 基本类型。protocol.type.playerblockactions.player_block_actions_count.description


/////
```title='示例元素'
[player_block_action]
```

///// html | div.result
////// define
Player Block Action：[<!-- md:samp PlayerBlockActionData -->](../types/playerblockactiondata.md)

- 特殊类型。protocol.type.playerblockactions.player_block_action.description


//////

/////

////

///


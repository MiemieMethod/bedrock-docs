# <!-- md:samp PlayerBlockActionData -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp PlayerBlockActionData -->类型。该类型用于protocol.type.playerblockactiondata.description

## 结构

```viz
digraph "PlayerBlockActionData" {
rankdir = LR
124
124 -> 125
125 -> 126
124 -> 127
127 -> 128
128 -> 129
129 -> 130
128 -> 131
131 -> 132
127 -> 133
133 -> 134
134 -> 135
133 -> 136
136 -> 137
127 -> 138
138 -> 139
139 -> 140
138 -> 141
141 -> 142
127 -> 143
143 -> 144
144 -> 145
143 -> 146
146 -> 147
127 -> 148
148 -> 149
149 -> 150
148 -> 151
151 -> 152
127 -> 153
153 -> 154
154 -> 155
153 -> 156
156 -> 157

124 [label="PlayerBlockActionData",comment="name: \"PlayerBlockActionData\", typeName: \"\", id: 124, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
125 [label="Player Action Type",comment="name: \"Player Action Type\", typeName: \"\", id: 125, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
126 [label="varint",comment="name: \"varint\", typeName: \"\", id: 126, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
127 [label="Dependency on 'Player Action Type'",shape=note,comment="name: \"Dependency on 'Player Action Type'\", typeName: \"\", id: 127, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
128 [label="if (26)",shape=diamond,comment="name: \"if (26)\", typeName: \"\", id: 128, branchId: 26, recurseId: -1, attributes: 4, notes: \"\""];
129 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 129, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
130 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 130, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
131 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 131, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
132 [label="varint",comment="name: \"varint\", typeName: \"\", id: 132, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
133 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 133, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
134 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 134, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
135 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 135, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
136 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 136, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
137 [label="varint",comment="name: \"varint\", typeName: \"\", id: 137, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
138 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 138, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
139 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 139, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
140 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 140, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
141 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 141, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
142 [label="varint",comment="name: \"varint\", typeName: \"\", id: 142, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
143 [label="if (18)",shape=diamond,comment="name: \"if (18)\", typeName: \"\", id: 143, branchId: 18, recurseId: -1, attributes: 4, notes: \"\""];
144 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 144, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
145 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 145, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
146 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 146, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
147 [label="varint",comment="name: \"varint\", typeName: \"\", id: 147, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
148 [label="if (27)",shape=diamond,comment="name: \"if (27)\", typeName: \"\", id: 148, branchId: 27, recurseId: -1, attributes: 4, notes: \"\""];
149 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 149, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
150 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 150, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
151 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 151, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
152 [label="varint",comment="name: \"varint\", typeName: \"\", id: 152, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
153 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 153, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
154 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 154, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
155 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 155, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
156 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 156, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
157 [label="varint",comment="name: \"varint\", typeName: \"\", id: 157, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;126;130;132;135;137;140;142;145;147;150;152;155;157}

}

```

## 字段

```title='PlayerBlockActionData'
[player_action_type][dependency_on_player_action_type]
```

/// html | div.result
//// define
Player Action Type：<!-- md:samp varint -->

- 基本类型。protocol.type.playerblockactiondata.player_action_type.description


////
> 依赖于`Player Action Type`

///// tab | `Player Action Type`如果为`26`
```title='if (26)'
[position][facing]
```

////// html | div.result
/////// define
Position：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_26.position.description


///////
/////// define
Facing：<!-- md:samp varint -->

- 基本类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_26.facing.description


///////

//////

/////

///// tab | `Player Action Type`如果为`0`
```title='if (0)'
[position][facing]
```

////// html | div.result
/////// define
Position：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_0.position.description


///////
/////// define
Facing：<!-- md:samp varint -->

- 基本类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_0.facing.description


///////

//////

/////

///// tab | `Player Action Type`如果为`1`
```title='if (1)'
[position][facing]
```

////// html | div.result
/////// define
Position：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_1.position.description


///////
/////// define
Facing：<!-- md:samp varint -->

- 基本类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_1.facing.description


///////

//////

/////

///// tab | `Player Action Type`如果为`18`
```title='if (18)'
[position][facing]
```

////// html | div.result
/////// define
Position：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_18.position.description


///////
/////// define
Facing：<!-- md:samp varint -->

- 基本类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_18.facing.description


///////

//////

/////

///// tab | `Player Action Type`如果为`27`
```title='if (27)'
[position][facing]
```

////// html | div.result
/////// define
Position：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_27.position.description


///////
/////// define
Facing：<!-- md:samp varint -->

- 基本类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_27.facing.description


///////

//////

/////

///// tab | `Player Action Type`如果为`2`
```title='if (2)'
[position][facing]
```

////// html | div.result
/////// define
Position：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_2.position.description


///////
/////// define
Facing：<!-- md:samp varint -->

- 基本类型。protocol.type.playerblockactiondata.dependency_on_player_action_type.if_2.facing.description


///////

//////

/////

///


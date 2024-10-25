# <!-- md:samp PlayerBlockActionData -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp PlayerBlockActionData -->类型。该类型用于protocol.type.playerblockactiondata.description

## 结构

```viz
digraph "PlayerBlockActionData" {
rankdir = LR
128
128 -> 129
129 -> 130
128 -> 131
131 -> 132
132 -> 133
133 -> 134
132 -> 135
135 -> 136
131 -> 137
137 -> 138
138 -> 139
137 -> 140
140 -> 141
131 -> 142
142 -> 143
143 -> 144
142 -> 145
145 -> 146
131 -> 147
147 -> 148
148 -> 149
147 -> 150
150 -> 151
131 -> 152
152 -> 153
153 -> 154
152 -> 155
155 -> 156
131 -> 157
157 -> 158
158 -> 159
157 -> 160
160 -> 161

128 [label="PlayerBlockActionData",comment="name: \"PlayerBlockActionData\", typeName: \"\", id: 128, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
129 [label="Player Action Type",comment="name: \"Player Action Type\", typeName: \"\", id: 129, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
130 [label="varint",comment="name: \"varint\", typeName: \"\", id: 130, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
131 [label="Dependency on 'Player Action Type'",shape=note,comment="name: \"Dependency on 'Player Action Type'\", typeName: \"\", id: 131, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
132 [label="if (26)",shape=diamond,comment="name: \"if (26)\", typeName: \"\", id: 132, branchId: 26, recurseId: -1, attributes: 4, notes: \"\""];
133 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 133, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
134 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 134, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
135 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 135, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
136 [label="varint",comment="name: \"varint\", typeName: \"\", id: 136, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
137 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 137, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
138 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 138, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
139 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 139, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
140 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 140, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
141 [label="varint",comment="name: \"varint\", typeName: \"\", id: 141, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
142 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 142, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
143 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 143, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
144 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 144, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
145 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 145, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
146 [label="varint",comment="name: \"varint\", typeName: \"\", id: 146, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
147 [label="if (18)",shape=diamond,comment="name: \"if (18)\", typeName: \"\", id: 147, branchId: 18, recurseId: -1, attributes: 4, notes: \"\""];
148 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 148, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
149 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 149, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
150 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 150, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
151 [label="varint",comment="name: \"varint\", typeName: \"\", id: 151, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
152 [label="if (27)",shape=diamond,comment="name: \"if (27)\", typeName: \"\", id: 152, branchId: 27, recurseId: -1, attributes: 4, notes: \"\""];
153 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 153, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
154 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 154, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
155 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 155, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
156 [label="varint",comment="name: \"varint\", typeName: \"\", id: 156, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
157 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 157, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
158 [label="Position",comment="name: \"Position\", typeName: \"BlockPos\", id: 158, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
159 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 159, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
160 [label="Facing",comment="name: \"Facing\", typeName: \"\", id: 160, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
161 [label="varint",comment="name: \"varint\", typeName: \"\", id: 161, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;130;134;136;139;141;144;146;149;151;154;156;159;161}

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


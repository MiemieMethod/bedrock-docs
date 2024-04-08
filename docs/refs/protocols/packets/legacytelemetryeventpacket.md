# <!-- md:samp LegacyTelemetryEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LegacyTelemetryEventPacket -->数据包，数字ID是`65`。

## 结构

```viz
digraph "LegacyTelemetryEventPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
8 -> 9
9 -> 10
7 -> 11
11 -> 12
12 -> 13
11 -> 14
14 -> 15
11 -> 16
16 -> 17
11 -> 18
18 -> 19
7 -> 20
20 -> 21
21 -> 22
7 -> 23
23 -> 24
24 -> 25
23 -> 26
26 -> 27
7 -> 28
28 -> 29
29 -> 30
28 -> 31
31 -> 32
28 -> 33
33 -> 34
28 -> 35
35 -> 36
28 -> 37
37 -> 38
28 -> 39
39 -> 40
7 -> 41
41 -> 42
42 -> 43
41 -> 44
44 -> 45
41 -> 46
46 -> 47
7 -> 48
48 -> 49
49 -> 50
48 -> 51
51 -> 52
48 -> 53
53 -> 54
48 -> 55
55 -> 56
7 -> 57
57 -> 58
58 -> 59
57 -> 60
60 -> 61
57 -> 62
62 -> 63
7 -> 64
64 -> 65
65 -> 66
64 -> 67
67 -> 68
64 -> 69
69 -> 70
64 -> 71
71 -> 72
64 -> 73
73 -> 74
7 -> 75
75 -> 76
7 -> 77
77 -> 78
7 -> 79
79 -> 80
80 -> 81
79 -> 82
82 -> 83
79 -> 84
84 -> 85
79 -> 86
86 -> 87
7 -> 88
88 -> 89
7 -> 90
90 -> 91
91 -> 92
90 -> 93
93 -> 94
90 -> 95
95 -> 96
7 -> 97
97 -> 98
7 -> 99
99 -> 100
100 -> 101
99 -> 102
102 -> 103
7 -> 104
104 -> 105
105 -> 106
104 -> 107
107 -> 108
7 -> 109
109 -> 110
110 -> 111
7 -> 112
112 -> 113
113 -> 114
7 -> 115
115 -> 116
116 -> 117
115 -> 118
118 -> 119
115 -> 120
120 -> 121
7 -> 122
122 -> 123
7 -> 124
124 -> 125
7 -> 126
126 -> 127
7 -> 128
128 -> 129
129 -> 130
7 -> 131
131 -> 132
132 -> 133
131 -> 134
134 -> 135
7 -> 136
136 -> 137
137 -> 138
7 -> 139
139 -> 140
140 -> 141
7 -> 142
142 -> 143
143 -> 144
142 -> 145
145 -> 146
7 -> 147
147 -> 148
7 -> 149
149 -> 150
7 -> 151
151 -> 152

0 [label="LegacyTelemetryEventPacket",comment="name: \"LegacyTelemetryEventPacket\", typeName: \"\", id: 0, branchId: 65, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Event Type",comment="name: \"Event Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LegacyTelemetryEventPacket::Type\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Use Player ID",comment="name: \"Use Player ID\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Dependency on 'Event Type'",shape=note,comment="name: \"Dependency on 'Event Type'\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
8 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
9 [label="Achievement ID",comment="name: \"Achievement ID\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="varint",comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 11, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
12 [label="Interaction Type",comment="name: \"Interaction Type\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MinecraftEventing::InteractionType\""];
13 [label="varint",comment="name: \"varint\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="Interaction Actor Type",comment="name: \"Interaction Actor Type\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorType\""];
15 [label="varint",comment="name: \"varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="Interaction Actor Variant",comment="name: \"Interaction Actor Variant\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
17 [label="varint",comment="name: \"varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="Interaction Actor Color",comment="name: \"Interaction Actor Color\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
19 [label="byte",comment="name: \"byte\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 20, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
21 [label="Dimension ID",comment="name: \"Dimension ID\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)\""];
22 [label="varint",comment="name: \"varint\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 23, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
24 [label="Source Dimension ID",comment="name: \"Source Dimension ID\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)\""];
25 [label="varint",comment="name: \"varint\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="Target Dimension ID",comment="name: \"Target Dimension ID\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)\""];
27 [label="varint",comment="name: \"varint\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 28, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
29 [label="Instigator Actor ID",comment="name: \"Instigator Actor ID\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
30 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Instigator's Child Actor Type",comment="name: \"Instigator's Child Actor Type\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorType\""];
34 [label="varint",comment="name: \"varint\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="Damage Source",comment="name: \"Damage Source\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorDamageCause\""];
36 [label="varint",comment="name: \"varint\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="Trade Tier",comment="name: \"Trade Tier\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"-1 if not a trading actor.\""];
38 [label="varint",comment="name: \"varint\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
39 [label="Trader Name",comment="name: \"Trader Name\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"Empty if not a trading actor.\""];
40 [label="string",comment="name: \"string\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="if (5)",shape=diamond,comment="name: \"if (5)\", typeName: \"\", id: 41, branchId: 5, recurseId: -1, attributes: 4, notes: \"\""];
42 [label="Contents Color",comment="name: \"Contents Color\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
43 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
44 [label="Contents Type",comment="name: \"Contents Type\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
45 [label="varint",comment="name: \"varint\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
46 [label="Fill Level",comment="name: \"Fill Level\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
47 [label="varint",comment="name: \"varint\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
48 [label="if (6)",shape=diamond,comment="name: \"if (6)\", typeName: \"\", id: 48, branchId: 6, recurseId: -1, attributes: 4, notes: \"\""];
49 [label="Instigator Actor ID",comment="name: \"Instigator Actor ID\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
50 [label="varint",comment="name: \"varint\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
51 [label="Instigator Mob Variant",comment="name: \"Instigator Mob Variant\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
52 [label="varint",comment="name: \"varint\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
53 [label="Damage Source",comment="name: \"Damage Source\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorDamageCause\""];
54 [label="varint",comment="name: \"varint\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
55 [label="Died in Raid?",comment="name: \"Died in Raid?\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
56 [label="bool",comment="name: \"bool\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
57 [label="if (7)",shape=diamond,comment="name: \"if (7)\", typeName: \"\", id: 57, branchId: 7, recurseId: -1, attributes: 4, notes: \"\""];
58 [label="Boss Actor ID",comment="name: \"Boss Actor ID\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
59 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
60 [label="Party Size",comment="name: \"Party Size\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
61 [label="varint",comment="name: \"varint\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
62 [label="Boss Type",comment="name: \"Boss Type\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorType\""];
63 [label="varint",comment="name: \"varint\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
64 [label="if (8)",shape=diamond,comment="name: \"if (8)\", typeName: \"\", id: 64, branchId: 8, recurseId: -1, attributes: 4, notes: \"\""];
65 [label="Result",comment="name: \"Result\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LegacyTelemetryEventPacket::AgentResult\""];
66 [label="varint",comment="name: \"varint\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
67 [label="Result Number",comment="name: \"Result Number\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
68 [label="varint",comment="name: \"varint\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
69 [label="Command Name",comment="name: \"Command Name\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
70 [label="string",comment="name: \"string\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
71 [label="Result Key",comment="name: \"Result Key\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
72 [label="string",comment="name: \"string\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
73 [label="Result String",comment="name: \"Result String\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
74 [label="string",comment="name: \"string\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
75 [label="if (9)",shape=diamond,comment="name: \"if (9)\", typeName: \"\", id: 75, branchId: 9, recurseId: -1, attributes: 4, notes: \"\""];
76 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
77 [label="if (10)",shape=diamond,comment="name: \"if (10)\", typeName: \"\", id: 77, branchId: 10, recurseId: -1, attributes: 4, notes: \"\""];
78 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
79 [label="if (11)",shape=diamond,comment="name: \"if (11)\", typeName: \"\", id: 79, branchId: 11, recurseId: -1, attributes: 4, notes: \"\""];
80 [label="Success Count",comment="name: \"Success Count\", typeName: \"\", id: 80, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
81 [label="varint",comment="name: \"varint\", typeName: \"\", id: 81, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
82 [label="Error Count",comment="name: \"Error Count\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
83 [label="varint",comment="name: \"varint\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
84 [label="Command Name",comment="name: \"Command Name\", typeName: \"\", id: 84, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
85 [label="string",comment="name: \"string\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
86 [label="Error List",comment="name: \"Error List\", typeName: \"\", id: 86, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
87 [label="string",comment="name: \"string\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
88 [label="if (12)",shape=diamond,comment="name: \"if (12)\", typeName: \"\", id: 88, branchId: 12, recurseId: -1, attributes: 4, notes: \"\""];
89 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
90 [label="if (13)",shape=diamond,comment="name: \"if (13)\", typeName: \"\", id: 90, branchId: 13, recurseId: -1, attributes: 4, notes: \"\""];
91 [label="Born Baby: Entity Type",comment="name: \"Born Baby: Entity Type\", typeName: \"\", id: 91, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
92 [label="varint",comment="name: \"varint\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
93 [label="Born Baby: Entity Variant",comment="name: \"Born Baby: Entity Variant\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
94 [label="varint",comment="name: \"varint\", typeName: \"\", id: 94, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
95 [label="Born Baby: Color",comment="name: \"Born Baby: Color\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
96 [label="byte",comment="name: \"byte\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
97 [label="if (14)",shape=diamond,comment="name: \"if (14)\", typeName: \"\", id: 97, branchId: 14, recurseId: -1, attributes: 4, notes: \"\""];
98 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
99 [label="if (15)",shape=diamond,comment="name: \"if (15)\", typeName: \"\", id: 99, branchId: 15, recurseId: -1, attributes: 4, notes: \"\""];
100 [label="Block Interaction Type",comment="name: \"Block Interaction Type\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MinecraftEventing::POIBlockInteractionType\""];
101 [label="varint",comment="name: \"varint\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
102 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the relevant item used in the interaction.\""];
103 [label="varint",comment="name: \"varint\", typeName: \"\", id: 103, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
104 [label="if (16)",shape=diamond,comment="name: \"if (16)\", typeName: \"\", id: 104, branchId: 16, recurseId: -1, attributes: 4, notes: \"\""];
105 [label="Block Interaction Type",comment="name: \"Block Interaction Type\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MinecraftEventing::POIBlockInteractionType\""];
106 [label="varint",comment="name: \"varint\", typeName: \"\", id: 106, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
107 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 107, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the relevant item used in the interaction.\""];
108 [label="varint",comment="name: \"varint\", typeName: \"\", id: 108, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
109 [label="if (17)",shape=diamond,comment="name: \"if (17)\", typeName: \"\", id: 109, branchId: 17, recurseId: -1, attributes: 4, notes: \"\""];
110 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the relevant item used in the interaction.\""];
111 [label="varint",comment="name: \"varint\", typeName: \"\", id: 111, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
112 [label="if (18)",shape=diamond,comment="name: \"if (18)\", typeName: \"\", id: 112, branchId: 18, recurseId: -1, attributes: 4, notes: \"\""];
113 [label="Event Name",comment="name: \"Event Name\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
114 [label="string",comment="name: \"string\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
115 [label="if (19)",shape=diamond,comment="name: \"if (19)\", typeName: \"\", id: 115, branchId: 19, recurseId: -1, attributes: 4, notes: \"\""];
116 [label="Current Raid Wave",comment="name: \"Current Raid Wave\", typeName: \"\", id: 116, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
117 [label="varint",comment="name: \"varint\", typeName: \"\", id: 117, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
118 [label="Total Raid Waves",comment="name: \"Total Raid Waves\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
119 [label="varint",comment="name: \"varint\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
120 [label="Won Raid",comment="name: \"Won Raid\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
121 [label="bool",comment="name: \"bool\", typeName: \"\", id: 121, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
122 [label="if (20)",shape=diamond,comment="name: \"if (20)\", typeName: \"\", id: 122, branchId: 20, recurseId: -1, attributes: 4, notes: \"\""];
123 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 123, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
124 [label="if (21)",shape=diamond,comment="name: \"if (21)\", typeName: \"\", id: 124, branchId: 21, recurseId: -1, attributes: 4, notes: \"\""];
125 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 125, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
126 [label="if (22)",shape=diamond,comment="name: \"if (22)\", typeName: \"\", id: 126, branchId: 22, recurseId: -1, attributes: 4, notes: \"\""];
127 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 127, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
128 [label="if (23)",shape=diamond,comment="name: \"if (23)\", typeName: \"\", id: 128, branchId: 23, recurseId: -1, attributes: 4, notes: \"\""];
129 [label="Redstone Level",comment="name: \"Redstone Level\", typeName: \"\", id: 129, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
130 [label="varint",comment="name: \"varint\", typeName: \"\", id: 130, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
131 [label="if (24)",shape=diamond,comment="name: \"if (24)\", typeName: \"\", id: 131, branchId: 24, recurseId: -1, attributes: 4, notes: \"\""];
132 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 132, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
133 [label="varint",comment="name: \"varint\", typeName: \"\", id: 133, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
134 [label="Was targeting bartering player",comment="name: \"Was targeting bartering player\", typeName: \"\", id: 134, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
135 [label="bool",comment="name: \"bool\", typeName: \"\", id: 135, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
136 [label="if (25)",shape=diamond,comment="name: \"if (25)\", typeName: \"\", id: 136, branchId: 25, recurseId: -1, attributes: 4, notes: \"\""];
137 [label="Player Waxed or Unwaxed Copper Block ID",comment="name: \"Player Waxed or Unwaxed Copper Block ID\", typeName: \"\", id: 137, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
138 [label="varint",comment="name: \"varint\", typeName: \"\", id: 138, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
139 [label="if (26)",shape=diamond,comment="name: \"if (26)\", typeName: \"\", id: 139, branchId: 26, recurseId: -1, attributes: 4, notes: \"\""];
140 [label="Code builder runtime action",comment="name: \"Code builder runtime action\", typeName: \"\", id: 140, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
141 [label="string",comment="name: \"string\", typeName: \"\", id: 141, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
142 [label="if (27)",shape=diamond,comment="name: \"if (27)\", typeName: \"\", id: 142, branchId: 27, recurseId: -1, attributes: 4, notes: \"\""];
143 [label="Objective Name",comment="name: \"Objective Name\", typeName: \"\", id: 143, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
144 [label="string",comment="name: \"string\", typeName: \"\", id: 144, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
145 [label="Code Builder Scoreboard Score",comment="name: \"Code Builder Scoreboard Score\", typeName: \"\", id: 145, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
146 [label="varint",comment="name: \"varint\", typeName: \"\", id: 146, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
147 [label="if (28)",shape=diamond,comment="name: \"if (28)\", typeName: \"\", id: 147, branchId: 28, recurseId: -1, attributes: 4, notes: \"\""];
148 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 148, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
149 [label="if (29)",shape=diamond,comment="name: \"if (29)\", typeName: \"\", id: 149, branchId: 29, recurseId: -1, attributes: 4, notes: \"\""];
150 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 150, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
151 [label="if (30)",shape=diamond,comment="name: \"if (30)\", typeName: \"\", id: 151, branchId: 30, recurseId: -1, attributes: 4, notes: \"\""];
152 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 152, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;10;13;15;17;19;22;25;27;30;32;34;36;38;40;43;45;47;50;52;54;56;59;61;63;66;68;70;72;74;76;78;81;83;85;87;89;92;94;96;98;101;103;106;108;111;114;117;119;121;123;125;127;130;133;135;138;141;144;146;148;150;152}

}

```

## 字段

```title='LegacyTelemetryEventPacket'
[target_actor_id][event_type][use_player_id][dependency_on_event_type]
```

/// html | div.result
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。


////
//// define
Event Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Achievement`|`0`||
  |`Interaction`|`1`||
  |`PortalCreated`|`2`||
  |`PortalUsed`|`3`||
  |`MobKilled`|`4`||
  |`CauldronUsed`|`5`||
  |`PlayerDied`|`6`||
  |`BossKilled`|`7`||
  |`AgentCommand_OBSOLETE`|`8`||
  |`AgentCreated`|`9`||
  |`PatternRemoved_OBSOLETE`|`10`||
  |`SlashCommand`|`11`||
  |`Deprecated_FishBucketed`|`12`||
  |`MobBorn`|`13`||
  |`PetDied_OBSOLETE`|`14`||
  |`POICauldronUsed`|`15`||
  |`ComposterUsed`|`16`||
  |`BellUsed`|`17`||
  |`ActorDefinition`|`18`||
  |`RaidUpdate`|`19`||
  |`PlayerMovementAnomaly_OBSOLETE`|`20`||
  |`PlayerMovementCorrected_OBSOLETE`|`21`||
  |`HoneyHarvested`|`22`||
  |`TargetBlockHit`|`23`||
  |`PiglinBarter`|`24`||
  |`PlayerWaxedOrUnwaxedCopper`|`25`||
  |`CodeBuilderRuntimeAction`|`26`||
  |`CodeBuilderScoreboard`|`27`||
  |`StriderRiddenInLavaInOverworld`|`28`||
  |`SneakCloseToSculkSensor`|`29`||
  |`CarefulRestoration`|`30`||



////
//// define
Use Player ID：<!-- md:samp byte -->

- 基本类型。


////
> 依赖于`Event Type`

///// tab | `Event Type`如果为`0`
```title='if (0)'
[achievement_id]
```

////// html | div.result
/////// define
Achievement ID：<!-- md:samp varint -->

- 基本类型。


///////

//////

/////

///// tab | `Event Type`如果为`1`
```title='if (1)'
[interaction_type][interaction_actor_type][interaction_actor_variant][interaction_actor_color]
```

////// html | div.result
/////// define
Interaction Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Breeding`|`1`||
  |`Taming`|`2`||
  |`Curing`|`3`||
  |`Crafted`|`4`||
  |`Shearing`|`5`||
  |`Milking`|`6`||
  |`Trading`|`7`||
  |`Feeding`|`8`||
  |`Igniting`|`9`||
  |`Coloring`|`10`||
  |`Naming`|`11`||
  |`Leashing`|`12`||
  |`Unleashing`|`13`||
  |`PetSleep`|`14`||
  |`Trusting`|`15`||
  |`Commanding`|`16`||



///////
/////// define
Interaction Actor Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`1`||
  |`TypeMask`|`0x000000ff`||
  |`Mob`|`0x00000100`||
  |`PathfinderMob`|`0x00000200 | Mob`||
  |`Monster`|`0x00000800 | PathfinderMob`||
  |`Animal`|`0x00001000 | PathfinderMob`||
  |`TamableAnimal`|`0x00004000 | Animal`||
  |`Ambient`|`0x00008000 | Mob`||
  |`UndeadMob`|`0x00010000 | Monster`||
  |`ZombieMonster`|`0x00020000 | UndeadMob`||
  |`Arthropod`|`0x00040000 | Monster`||
  |`Minecart`|`0x00080000`||
  |`SkeletonMonster`|`0x00100000 | UndeadMob`||
  |`EquineAnimal`|`0x00200000 | TamableAnimal`||
  |`Projectile`|`0x00400000`||
  |`AbstractArrow`|`0x00800000`||
  |`WaterAnimal`|`0x00002000 | PathfinderMob`||
  |`VillagerBase`|`0x01000000 | PathfinderMob`||
  |`Chicken`|`10 | Animal`||
  |`Cow`|`11 | Animal`||
  |`Pig`|`12 | Animal`||
  |`Sheep`|`13 | Animal`||
  |`Wolf`|`14 | TamableAnimal`||
  |`Villager`|`15 | VillagerBase`||
  |`MushroomCow`|`16 | Animal`||
  |`Squid`|`17 | WaterAnimal`||
  |`Rabbit`|`18 | Animal`||
  |`Bat`|`19 | Ambient`||
  |`IronGolem`|`20 | PathfinderMob`||
  |`SnowGolem`|`21 | PathfinderMob`||
  |`Ocelot`|`22 | TamableAnimal`||
  |`Horse`|`23 | EquineAnimal`||
  |`PolarBear`|`28 | Animal`||
  |`Llama`|`29 | Animal`||
  |`Parrot`|`30 | TamableAnimal`||
  |`Dolphin`|`31 | WaterAnimal`||
  |`Donkey`|`24 | EquineAnimal`||
  |`Mule`|`25 | EquineAnimal`||
  |`SkeletonHorse`|`26 | EquineAnimal | UndeadMob`||
  |`ZombieHorse`|`27 | EquineAnimal | UndeadMob`||
  |`Zombie`|`32 | ZombieMonster`||
  |`Creeper`|`33 | Monster`||
  |`Skeleton`|`34 | SkeletonMonster`||
  |`Spider`|`35 | Arthropod`||
  |`PigZombie`|`36 | UndeadMob`||
  |`Slime`|`37 | Monster`||
  |`EnderMan`|`38 | Monster`||
  |`Silverfish`|`39 | Arthropod`||
  |`CaveSpider`|`40 | Arthropod`||
  |`Ghast`|`41 | Monster`||
  |`LavaSlime`|`42 | Monster`||
  |`Blaze`|`43 | Monster`||
  |`ZombieVillager`|`44 | ZombieMonster`||
  |`Witch`|`45 | Monster`||
  |`Stray`|`46 | SkeletonMonster`||
  |`Husk`|`47 | ZombieMonster`||
  |`WitherSkeleton`|`48 | SkeletonMonster`||
  |`Guardian`|`49 | Monster`||
  |`ElderGuardian`|`50 | Monster`||
  |`Npc`|`51 | Mob`||
  |`WitherBoss`|`52 | UndeadMob`||
  |`Dragon`|`53 | Monster`||
  |`Shulker`|`54 | Monster`||
  |`Endermite`|`55 | Arthropod`||
  |`Agent`|`56 | Mob`||
  |`Vindicator`|`57 | Monster`||
  |`Phantom`|`58 | UndeadMob`||
  |`IllagerBeast`|`59 | Monster`||
  |`ArmorStand`|`61 | Mob`||
  |`TripodCamera`|`62 | Mob`||
  |`Player`|`63 | Mob`||
  |`ItemEntity`|`64`||
  |`PrimedTnt`|`65`||
  |`FallingBlock`|`66`||
  |`MovingBlock`|`67`||
  |`ExperiencePotion`|`68 | Projectile`||
  |`Experience`|`69`||
  |`EyeOfEnder`|`70`||
  |`EnderCrystal`|`71`||
  |`FireworksRocket`|`72`||
  |`Trident`|`73 | Projectile | AbstractArrow`||
  |`Turtle`|`74 | Animal`||
  |`Cat`|`75 | TamableAnimal`||
  |`ShulkerBullet`|`76 | Projectile`||
  |`FishingHook`|`77`||
  |`Chalkboard`|`78`||
  |`DragonFireball`|`79 | Projectile`||
  |`Arrow`|`80 | Projectile | AbstractArrow`||
  |`Snowball`|`81 | Projectile`||
  |`ThrownEgg`|`82 | Projectile`||
  |`Painting`|`83`||
  |`LargeFireball`|`85 | Projectile`||
  |`ThrownPotion`|`86 | Projectile`||
  |`Enderpearl`|`87 | Projectile`||
  |`LeashKnot`|`88`||
  |`WitherSkull`|`89 | Projectile`||
  |`BoatRideable`|`90`||
  |`WitherSkullDangerous`|`91 | Projectile`||
  |`LightningBolt`|`93`||
  |`SmallFireball`|`94 | Projectile`||
  |`AreaEffectCloud`|`95`||
  |`LingeringPotion`|`101 | Projectile`||
  |`LlamaSpit`|`102 | Projectile`||
  |`EvocationFang`|`103 | Projectile`||
  |`EvocationIllager`|`104 | Monster`||
  |`Vex`|`105 | Monster`||
  |`MinecartRideable`|`84 | Minecart`||
  |`MinecartHopper`|`96 | Minecart`||
  |`MinecartTNT`|`97 | Minecart`||
  |`MinecartChest`|`98 | Minecart`||
  |`MinecartFurnace`|`99 | Minecart`||
  |`MinecartCommandBlock`|`100 | Minecart`||
  |`IceBomb`|`106 | Projectile`||
  |`Balloon`|`107`||
  |`Pufferfish`|`108 | WaterAnimal`||
  |`Salmon`|`109 | WaterAnimal`||
  |`Drowned`|`110 | ZombieMonster`||
  |`Tropicalfish`|`111 | WaterAnimal`||
  |`Fish`|`112 | WaterAnimal`||
  |`Panda`|`113 | Animal`||
  |`Pillager`|`114 | Monster`||
  |`VillagerV2`|`115 | VillagerBase`||
  |`ZombieVillagerV2`|`116 | ZombieMonster`||
  |`Shield`|`117`||
  |`WanderingTrader`|`118 | PathfinderMob`||
  |`Lectern`|`119`||
  |`ElderGuardianGhost`|`120 | Monster`||
  |`Fox`|`121 | Animal`||
  |`Bee`|`122 | Mob`||
  |`Piglin`|`123 | Mob`||
  |`Hoglin`|`124 | Animal`||
  |`Strider`|`125 | Animal`||
  |`Zoglin`|`126 | UndeadMob`||
  |`PiglinBrute`|`127 | Mob`||
  |`Goat`|`128 | Animal`||
  |`GlowSquid`|`129 | WaterAnimal`||
  |`Axolotl`|`130 | Animal`||
  |`Warden`|`131 | Monster`||
  |`Frog`|`132 | Animal`||
  |`Tadpole`|`133 | WaterAnimal`||
  |`Allay`|`134 | Mob`||
  |`ChestBoatRideable`|`136 | BoatRideable`||
  |`TraderLlama`|`137 | Llama`||
  |`Camel`|`138 | Animal`||
  |`Sniffer`|`139 | Animal`||
  |`Breeze`|`140 | Monster`||
  |`BreezeWindChargeProjectile`|`141 | Projectile`||
  |`Armadillo`|`142 | Animal`||
  |`WindChargeProjectile`|`143 | Projectile`||
  |`Bogged`|`144| SkeletonMonster`||



///////
/////// define
Interaction Actor Variant：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Interaction Actor Color：<!-- md:samp byte -->

- 基本类型。


///////

//////

/////

///// tab | `Event Type`如果为`2`
```title='if (2)'
[dimension_id]
```

////// html | div.result
/////// define
Dimension ID：<!-- md:samp varint -->

- 基本类型。Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)


///////

//////

/////

///// tab | `Event Type`如果为`3`
```title='if (3)'
[source_dimension_id][target_dimension_id]
```

////// html | div.result
/////// define
Source Dimension ID：<!-- md:samp varint -->

- 基本类型。Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)


///////
/////// define
Target Dimension ID：<!-- md:samp varint -->

- 基本类型。Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)


///////

//////

/////

///// tab | `Event Type`如果为`4`
```title='if (4)'
[instigator_actor_id][target_actor_id][instigators_child_actor_type][damage_source][trade_tier][trader_name]
```

////// html | div.result
/////// define
Instigator Actor ID：<!-- md:samp varint64 -->

- 基本类型。


///////
/////// define
Target Actor ID：<!-- md:samp varint64 -->

- 基本类型。


///////
/////// define
Instigator's Child Actor Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`1`||
  |`TypeMask`|`0x000000ff`||
  |`Mob`|`0x00000100`||
  |`PathfinderMob`|`0x00000200 | Mob`||
  |`Monster`|`0x00000800 | PathfinderMob`||
  |`Animal`|`0x00001000 | PathfinderMob`||
  |`TamableAnimal`|`0x00004000 | Animal`||
  |`Ambient`|`0x00008000 | Mob`||
  |`UndeadMob`|`0x00010000 | Monster`||
  |`ZombieMonster`|`0x00020000 | UndeadMob`||
  |`Arthropod`|`0x00040000 | Monster`||
  |`Minecart`|`0x00080000`||
  |`SkeletonMonster`|`0x00100000 | UndeadMob`||
  |`EquineAnimal`|`0x00200000 | TamableAnimal`||
  |`Projectile`|`0x00400000`||
  |`AbstractArrow`|`0x00800000`||
  |`WaterAnimal`|`0x00002000 | PathfinderMob`||
  |`VillagerBase`|`0x01000000 | PathfinderMob`||
  |`Chicken`|`10 | Animal`||
  |`Cow`|`11 | Animal`||
  |`Pig`|`12 | Animal`||
  |`Sheep`|`13 | Animal`||
  |`Wolf`|`14 | TamableAnimal`||
  |`Villager`|`15 | VillagerBase`||
  |`MushroomCow`|`16 | Animal`||
  |`Squid`|`17 | WaterAnimal`||
  |`Rabbit`|`18 | Animal`||
  |`Bat`|`19 | Ambient`||
  |`IronGolem`|`20 | PathfinderMob`||
  |`SnowGolem`|`21 | PathfinderMob`||
  |`Ocelot`|`22 | TamableAnimal`||
  |`Horse`|`23 | EquineAnimal`||
  |`PolarBear`|`28 | Animal`||
  |`Llama`|`29 | Animal`||
  |`Parrot`|`30 | TamableAnimal`||
  |`Dolphin`|`31 | WaterAnimal`||
  |`Donkey`|`24 | EquineAnimal`||
  |`Mule`|`25 | EquineAnimal`||
  |`SkeletonHorse`|`26 | EquineAnimal | UndeadMob`||
  |`ZombieHorse`|`27 | EquineAnimal | UndeadMob`||
  |`Zombie`|`32 | ZombieMonster`||
  |`Creeper`|`33 | Monster`||
  |`Skeleton`|`34 | SkeletonMonster`||
  |`Spider`|`35 | Arthropod`||
  |`PigZombie`|`36 | UndeadMob`||
  |`Slime`|`37 | Monster`||
  |`EnderMan`|`38 | Monster`||
  |`Silverfish`|`39 | Arthropod`||
  |`CaveSpider`|`40 | Arthropod`||
  |`Ghast`|`41 | Monster`||
  |`LavaSlime`|`42 | Monster`||
  |`Blaze`|`43 | Monster`||
  |`ZombieVillager`|`44 | ZombieMonster`||
  |`Witch`|`45 | Monster`||
  |`Stray`|`46 | SkeletonMonster`||
  |`Husk`|`47 | ZombieMonster`||
  |`WitherSkeleton`|`48 | SkeletonMonster`||
  |`Guardian`|`49 | Monster`||
  |`ElderGuardian`|`50 | Monster`||
  |`Npc`|`51 | Mob`||
  |`WitherBoss`|`52 | UndeadMob`||
  |`Dragon`|`53 | Monster`||
  |`Shulker`|`54 | Monster`||
  |`Endermite`|`55 | Arthropod`||
  |`Agent`|`56 | Mob`||
  |`Vindicator`|`57 | Monster`||
  |`Phantom`|`58 | UndeadMob`||
  |`IllagerBeast`|`59 | Monster`||
  |`ArmorStand`|`61 | Mob`||
  |`TripodCamera`|`62 | Mob`||
  |`Player`|`63 | Mob`||
  |`ItemEntity`|`64`||
  |`PrimedTnt`|`65`||
  |`FallingBlock`|`66`||
  |`MovingBlock`|`67`||
  |`ExperiencePotion`|`68 | Projectile`||
  |`Experience`|`69`||
  |`EyeOfEnder`|`70`||
  |`EnderCrystal`|`71`||
  |`FireworksRocket`|`72`||
  |`Trident`|`73 | Projectile | AbstractArrow`||
  |`Turtle`|`74 | Animal`||
  |`Cat`|`75 | TamableAnimal`||
  |`ShulkerBullet`|`76 | Projectile`||
  |`FishingHook`|`77`||
  |`Chalkboard`|`78`||
  |`DragonFireball`|`79 | Projectile`||
  |`Arrow`|`80 | Projectile | AbstractArrow`||
  |`Snowball`|`81 | Projectile`||
  |`ThrownEgg`|`82 | Projectile`||
  |`Painting`|`83`||
  |`LargeFireball`|`85 | Projectile`||
  |`ThrownPotion`|`86 | Projectile`||
  |`Enderpearl`|`87 | Projectile`||
  |`LeashKnot`|`88`||
  |`WitherSkull`|`89 | Projectile`||
  |`BoatRideable`|`90`||
  |`WitherSkullDangerous`|`91 | Projectile`||
  |`LightningBolt`|`93`||
  |`SmallFireball`|`94 | Projectile`||
  |`AreaEffectCloud`|`95`||
  |`LingeringPotion`|`101 | Projectile`||
  |`LlamaSpit`|`102 | Projectile`||
  |`EvocationFang`|`103 | Projectile`||
  |`EvocationIllager`|`104 | Monster`||
  |`Vex`|`105 | Monster`||
  |`MinecartRideable`|`84 | Minecart`||
  |`MinecartHopper`|`96 | Minecart`||
  |`MinecartTNT`|`97 | Minecart`||
  |`MinecartChest`|`98 | Minecart`||
  |`MinecartFurnace`|`99 | Minecart`||
  |`MinecartCommandBlock`|`100 | Minecart`||
  |`IceBomb`|`106 | Projectile`||
  |`Balloon`|`107`||
  |`Pufferfish`|`108 | WaterAnimal`||
  |`Salmon`|`109 | WaterAnimal`||
  |`Drowned`|`110 | ZombieMonster`||
  |`Tropicalfish`|`111 | WaterAnimal`||
  |`Fish`|`112 | WaterAnimal`||
  |`Panda`|`113 | Animal`||
  |`Pillager`|`114 | Monster`||
  |`VillagerV2`|`115 | VillagerBase`||
  |`ZombieVillagerV2`|`116 | ZombieMonster`||
  |`Shield`|`117`||
  |`WanderingTrader`|`118 | PathfinderMob`||
  |`Lectern`|`119`||
  |`ElderGuardianGhost`|`120 | Monster`||
  |`Fox`|`121 | Animal`||
  |`Bee`|`122 | Mob`||
  |`Piglin`|`123 | Mob`||
  |`Hoglin`|`124 | Animal`||
  |`Strider`|`125 | Animal`||
  |`Zoglin`|`126 | UndeadMob`||
  |`PiglinBrute`|`127 | Mob`||
  |`Goat`|`128 | Animal`||
  |`GlowSquid`|`129 | WaterAnimal`||
  |`Axolotl`|`130 | Animal`||
  |`Warden`|`131 | Monster`||
  |`Frog`|`132 | Animal`||
  |`Tadpole`|`133 | WaterAnimal`||
  |`Allay`|`134 | Mob`||
  |`ChestBoatRideable`|`136 | BoatRideable`||
  |`TraderLlama`|`137 | Llama`||
  |`Camel`|`138 | Animal`||
  |`Sniffer`|`139 | Animal`||
  |`Breeze`|`140 | Monster`||
  |`BreezeWindChargeProjectile`|`141 | Projectile`||
  |`Armadillo`|`142 | Animal`||
  |`WindChargeProjectile`|`143 | Projectile`||
  |`Bogged`|`144| SkeletonMonster`||



///////
/////// define
Damage Source：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`-1`||
  |`Override`|`0`||
  |`Contact`|`1`||
  |`EntityAttack`|`2`||
  |`Projectile`|`3`||
  |`Suffocation`|`4`||
  |`Fall`|`5`||
  |`Fire`|`6`||
  |`FireTick`|`7`||
  |`Lava`|`8`||
  |`Drowning`|`9`||
  |`BlockExplosion`|`10`||
  |`EntityExplosion`|`11`||
  |`Void`|`12`||
  |`SelfDestruct`|`13`||
  |`Magic`|`14`||
  |`Wither`|`15`||
  |`Starve`|`16`||
  |`Anvil`|`17`||
  |`Thorns`|`18`||
  |`FallingBlock`|`19`||
  |`Piston`|`20`||
  |`FlyIntoWall`|`21`||
  |`Magma`|`22`||
  |`Fireworks`|`23`||
  |`Lightning`|`24`||
  |`Charging`|`25`||
  |`Temperature`|`26`||
  |`Freezing`|`27`||
  |`Stalactite`|`28`||
  |`Stalagmite`|`29`||
  |`RamAttack`|`30`||
  |`SonicBoom`|`31`||
  |`Campfire`|`32`||
  |`SoulCampfire`|`33`||
  |`All`|`34`||



///////
/////// define
Trade Tier：<!-- md:samp varint -->

- 基本类型。-1 if not a trading actor.


///////
/////// define
Trader Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。Empty if not a trading actor.


///////

//////

/////

///// tab | `Event Type`如果为`5`
```title='if (5)'
[contents_color][contents_type][fill_level]
```

////// html | div.result
/////// define
Contents Color：<!-- md:samp unsigned varint -->

- 基本类型。


///////
/////// define
Contents Type：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Fill Level：<!-- md:samp varint -->

- 基本类型。


///////

//////

/////

///// tab | `Event Type`如果为`6`
```title='if (6)'
[instigator_actor_id][instigator_mob_variant][damage_source][died_in_raid]
```

////// html | div.result
/////// define
Instigator Actor ID：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Instigator Mob Variant：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Damage Source：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`-1`||
  |`Override`|`0`||
  |`Contact`|`1`||
  |`EntityAttack`|`2`||
  |`Projectile`|`3`||
  |`Suffocation`|`4`||
  |`Fall`|`5`||
  |`Fire`|`6`||
  |`FireTick`|`7`||
  |`Lava`|`8`||
  |`Drowning`|`9`||
  |`BlockExplosion`|`10`||
  |`EntityExplosion`|`11`||
  |`Void`|`12`||
  |`SelfDestruct`|`13`||
  |`Magic`|`14`||
  |`Wither`|`15`||
  |`Starve`|`16`||
  |`Anvil`|`17`||
  |`Thorns`|`18`||
  |`FallingBlock`|`19`||
  |`Piston`|`20`||
  |`FlyIntoWall`|`21`||
  |`Magma`|`22`||
  |`Fireworks`|`23`||
  |`Lightning`|`24`||
  |`Charging`|`25`||
  |`Temperature`|`26`||
  |`Freezing`|`27`||
  |`Stalactite`|`28`||
  |`Stalagmite`|`29`||
  |`RamAttack`|`30`||
  |`SonicBoom`|`31`||
  |`Campfire`|`32`||
  |`SoulCampfire`|`33`||
  |`All`|`34`||



///////
/////// define
Died in Raid?：<!-- md:samp bool -->

- 基本类型。


///////

//////

/////

///// tab | `Event Type`如果为`7`
```title='if (7)'
[boss_actor_id][party_size][boss_type]
```

////// html | div.result
/////// define
Boss Actor ID：<!-- md:samp varint64 -->

- 基本类型。


///////
/////// define
Party Size：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Boss Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`1`||
  |`TypeMask`|`0x000000ff`||
  |`Mob`|`0x00000100`||
  |`PathfinderMob`|`0x00000200 | Mob`||
  |`Monster`|`0x00000800 | PathfinderMob`||
  |`Animal`|`0x00001000 | PathfinderMob`||
  |`TamableAnimal`|`0x00004000 | Animal`||
  |`Ambient`|`0x00008000 | Mob`||
  |`UndeadMob`|`0x00010000 | Monster`||
  |`ZombieMonster`|`0x00020000 | UndeadMob`||
  |`Arthropod`|`0x00040000 | Monster`||
  |`Minecart`|`0x00080000`||
  |`SkeletonMonster`|`0x00100000 | UndeadMob`||
  |`EquineAnimal`|`0x00200000 | TamableAnimal`||
  |`Projectile`|`0x00400000`||
  |`AbstractArrow`|`0x00800000`||
  |`WaterAnimal`|`0x00002000 | PathfinderMob`||
  |`VillagerBase`|`0x01000000 | PathfinderMob`||
  |`Chicken`|`10 | Animal`||
  |`Cow`|`11 | Animal`||
  |`Pig`|`12 | Animal`||
  |`Sheep`|`13 | Animal`||
  |`Wolf`|`14 | TamableAnimal`||
  |`Villager`|`15 | VillagerBase`||
  |`MushroomCow`|`16 | Animal`||
  |`Squid`|`17 | WaterAnimal`||
  |`Rabbit`|`18 | Animal`||
  |`Bat`|`19 | Ambient`||
  |`IronGolem`|`20 | PathfinderMob`||
  |`SnowGolem`|`21 | PathfinderMob`||
  |`Ocelot`|`22 | TamableAnimal`||
  |`Horse`|`23 | EquineAnimal`||
  |`PolarBear`|`28 | Animal`||
  |`Llama`|`29 | Animal`||
  |`Parrot`|`30 | TamableAnimal`||
  |`Dolphin`|`31 | WaterAnimal`||
  |`Donkey`|`24 | EquineAnimal`||
  |`Mule`|`25 | EquineAnimal`||
  |`SkeletonHorse`|`26 | EquineAnimal | UndeadMob`||
  |`ZombieHorse`|`27 | EquineAnimal | UndeadMob`||
  |`Zombie`|`32 | ZombieMonster`||
  |`Creeper`|`33 | Monster`||
  |`Skeleton`|`34 | SkeletonMonster`||
  |`Spider`|`35 | Arthropod`||
  |`PigZombie`|`36 | UndeadMob`||
  |`Slime`|`37 | Monster`||
  |`EnderMan`|`38 | Monster`||
  |`Silverfish`|`39 | Arthropod`||
  |`CaveSpider`|`40 | Arthropod`||
  |`Ghast`|`41 | Monster`||
  |`LavaSlime`|`42 | Monster`||
  |`Blaze`|`43 | Monster`||
  |`ZombieVillager`|`44 | ZombieMonster`||
  |`Witch`|`45 | Monster`||
  |`Stray`|`46 | SkeletonMonster`||
  |`Husk`|`47 | ZombieMonster`||
  |`WitherSkeleton`|`48 | SkeletonMonster`||
  |`Guardian`|`49 | Monster`||
  |`ElderGuardian`|`50 | Monster`||
  |`Npc`|`51 | Mob`||
  |`WitherBoss`|`52 | UndeadMob`||
  |`Dragon`|`53 | Monster`||
  |`Shulker`|`54 | Monster`||
  |`Endermite`|`55 | Arthropod`||
  |`Agent`|`56 | Mob`||
  |`Vindicator`|`57 | Monster`||
  |`Phantom`|`58 | UndeadMob`||
  |`IllagerBeast`|`59 | Monster`||
  |`ArmorStand`|`61 | Mob`||
  |`TripodCamera`|`62 | Mob`||
  |`Player`|`63 | Mob`||
  |`ItemEntity`|`64`||
  |`PrimedTnt`|`65`||
  |`FallingBlock`|`66`||
  |`MovingBlock`|`67`||
  |`ExperiencePotion`|`68 | Projectile`||
  |`Experience`|`69`||
  |`EyeOfEnder`|`70`||
  |`EnderCrystal`|`71`||
  |`FireworksRocket`|`72`||
  |`Trident`|`73 | Projectile | AbstractArrow`||
  |`Turtle`|`74 | Animal`||
  |`Cat`|`75 | TamableAnimal`||
  |`ShulkerBullet`|`76 | Projectile`||
  |`FishingHook`|`77`||
  |`Chalkboard`|`78`||
  |`DragonFireball`|`79 | Projectile`||
  |`Arrow`|`80 | Projectile | AbstractArrow`||
  |`Snowball`|`81 | Projectile`||
  |`ThrownEgg`|`82 | Projectile`||
  |`Painting`|`83`||
  |`LargeFireball`|`85 | Projectile`||
  |`ThrownPotion`|`86 | Projectile`||
  |`Enderpearl`|`87 | Projectile`||
  |`LeashKnot`|`88`||
  |`WitherSkull`|`89 | Projectile`||
  |`BoatRideable`|`90`||
  |`WitherSkullDangerous`|`91 | Projectile`||
  |`LightningBolt`|`93`||
  |`SmallFireball`|`94 | Projectile`||
  |`AreaEffectCloud`|`95`||
  |`LingeringPotion`|`101 | Projectile`||
  |`LlamaSpit`|`102 | Projectile`||
  |`EvocationFang`|`103 | Projectile`||
  |`EvocationIllager`|`104 | Monster`||
  |`Vex`|`105 | Monster`||
  |`MinecartRideable`|`84 | Minecart`||
  |`MinecartHopper`|`96 | Minecart`||
  |`MinecartTNT`|`97 | Minecart`||
  |`MinecartChest`|`98 | Minecart`||
  |`MinecartFurnace`|`99 | Minecart`||
  |`MinecartCommandBlock`|`100 | Minecart`||
  |`IceBomb`|`106 | Projectile`||
  |`Balloon`|`107`||
  |`Pufferfish`|`108 | WaterAnimal`||
  |`Salmon`|`109 | WaterAnimal`||
  |`Drowned`|`110 | ZombieMonster`||
  |`Tropicalfish`|`111 | WaterAnimal`||
  |`Fish`|`112 | WaterAnimal`||
  |`Panda`|`113 | Animal`||
  |`Pillager`|`114 | Monster`||
  |`VillagerV2`|`115 | VillagerBase`||
  |`ZombieVillagerV2`|`116 | ZombieMonster`||
  |`Shield`|`117`||
  |`WanderingTrader`|`118 | PathfinderMob`||
  |`Lectern`|`119`||
  |`ElderGuardianGhost`|`120 | Monster`||
  |`Fox`|`121 | Animal`||
  |`Bee`|`122 | Mob`||
  |`Piglin`|`123 | Mob`||
  |`Hoglin`|`124 | Animal`||
  |`Strider`|`125 | Animal`||
  |`Zoglin`|`126 | UndeadMob`||
  |`PiglinBrute`|`127 | Mob`||
  |`Goat`|`128 | Animal`||
  |`GlowSquid`|`129 | WaterAnimal`||
  |`Axolotl`|`130 | Animal`||
  |`Warden`|`131 | Monster`||
  |`Frog`|`132 | Animal`||
  |`Tadpole`|`133 | WaterAnimal`||
  |`Allay`|`134 | Mob`||
  |`ChestBoatRideable`|`136 | BoatRideable`||
  |`TraderLlama`|`137 | Llama`||
  |`Camel`|`138 | Animal`||
  |`Sniffer`|`139 | Animal`||
  |`Breeze`|`140 | Monster`||
  |`BreezeWindChargeProjectile`|`141 | Projectile`||
  |`Armadillo`|`142 | Animal`||
  |`WindChargeProjectile`|`143 | Projectile`||
  |`Bogged`|`144| SkeletonMonster`||



///////

//////

/////

///// tab | `Event Type`如果为`8`
```title='if (8)'
[result][result_number][command_name][result_key][result_string]
```

////// html | div.result
/////// define
Result：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ActionFail`|`0`||
  |`ActionSuccess`|`1`||
  |`QueryResultFalse`|`2`||
  |`QueryResultTrue`|`3`||



///////
/////// define
Result Number：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Command Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


///////
/////// define
Result Key：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


///////
/////// define
Result String：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


///////

//////

/////

///// tab | `Event Type`如果为`9`
////// define
if (9)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Event Type`如果为`10`
////// define
if (10)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Event Type`如果为`11`
```title='if (11)'
[success_count][error_count][command_name][error_list]
```

////// html | div.result
/////// define
Success Count：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Error Count：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Command Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


///////
/////// define
Error List：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


///////

//////

/////

///// tab | `Event Type`如果为`12`
////// define
if (12)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Event Type`如果为`13`
```title='if (13)'
[born_baby:_entity_type][born_baby:_entity_variant][born_baby:_color]
```

////// html | div.result
/////// define
Born Baby: Entity Type：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Born Baby: Entity Variant：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Born Baby: Color：<!-- md:samp byte -->

- 基本类型。


///////

//////

/////

///// tab | `Event Type`如果为`14`
////// define
if (14)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Event Type`如果为`15`
```title='if (15)'
[block_interaction_type][item_id]
```

////// html | div.result
/////// define
Block Interaction Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`Extend`|`1`||
  |`Clone`|`2`||
  |`Lock`|`3`||
  |`Create`|`4`||
  |`CreateLocator`|`5`||
  |`Rename`|`6`||
  |`ItemPlaced`|`7`||
  |`ItemRemoved`|`8`||
  |`Cooking`|`9`||
  |`Dousing`|`10`||
  |`Lighting`|`11`||
  |`Haystack`|`12`||
  |`Filled`|`13`||
  |`Emptied`|`14`||
  |`AddDye`|`15`||
  |`DyeItem`|`16`||
  |`ClearItem`|`17`||
  |`EnchantArrow`|`18`||
  |`CompostItemPlaced`|`19`||
  |`RecoveredBonemeal`|`20`||
  |`BookPlaced`|`21`||
  |`BookOpened`|`22`||
  |`Disenchant`|`23`||
  |`Repair`|`24`||
  |`DisenchantAndRepair`|`25`||



///////
/////// define
Item Id：<!-- md:samp varint -->

- 基本类型。Id of the relevant item used in the interaction.


///////

//////

/////

///// tab | `Event Type`如果为`16`
```title='if (16)'
[block_interaction_type][item_id]
```

////// html | div.result
/////// define
Block Interaction Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`Extend`|`1`||
  |`Clone`|`2`||
  |`Lock`|`3`||
  |`Create`|`4`||
  |`CreateLocator`|`5`||
  |`Rename`|`6`||
  |`ItemPlaced`|`7`||
  |`ItemRemoved`|`8`||
  |`Cooking`|`9`||
  |`Dousing`|`10`||
  |`Lighting`|`11`||
  |`Haystack`|`12`||
  |`Filled`|`13`||
  |`Emptied`|`14`||
  |`AddDye`|`15`||
  |`DyeItem`|`16`||
  |`ClearItem`|`17`||
  |`EnchantArrow`|`18`||
  |`CompostItemPlaced`|`19`||
  |`RecoveredBonemeal`|`20`||
  |`BookPlaced`|`21`||
  |`BookOpened`|`22`||
  |`Disenchant`|`23`||
  |`Repair`|`24`||
  |`DisenchantAndRepair`|`25`||



///////
/////// define
Item Id：<!-- md:samp varint -->

- 基本类型。Id of the relevant item used in the interaction.


///////

//////

/////

///// tab | `Event Type`如果为`17`
```title='if (17)'
[item_id]
```

////// html | div.result
/////// define
Item Id：<!-- md:samp varint -->

- 基本类型。Id of the relevant item used in the interaction.


///////

//////

/////

///// tab | `Event Type`如果为`18`
```title='if (18)'
[event_name]
```

////// html | div.result
/////// define
Event Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


///////

//////

/////

///// tab | `Event Type`如果为`19`
```title='if (19)'
[current_raid_wave][total_raid_waves][won_raid]
```

////// html | div.result
/////// define
Current Raid Wave：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Total Raid Waves：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Won Raid：<!-- md:samp bool -->

- 基本类型。


///////

//////

/////

///// tab | `Event Type`如果为`20`
////// define
if (20)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Event Type`如果为`21`
////// define
if (21)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Event Type`如果为`22`
////// define
if (22)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Event Type`如果为`23`
```title='if (23)'
[redstone_level]
```

////// html | div.result
/////// define
Redstone Level：<!-- md:samp varint -->

- 基本类型。


///////

//////

/////

///// tab | `Event Type`如果为`24`
```title='if (24)'
[item_id][was_targeting_bartering_player]
```

////// html | div.result
/////// define
Item Id：<!-- md:samp varint -->

- 基本类型。


///////
/////// define
Was targeting bartering player：<!-- md:samp bool -->

- 基本类型。


///////

//////

/////

///// tab | `Event Type`如果为`25`
```title='if (25)'
[player_waxed_or_unwaxed_copper_block_id]
```

////// html | div.result
/////// define
Player Waxed or Unwaxed Copper Block ID：<!-- md:samp varint -->

- 基本类型。


///////

//////

/////

///// tab | `Event Type`如果为`26`
```title='if (26)'
[code_builder_runtime_action]
```

////// html | div.result
/////// define
Code builder runtime action：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


///////

//////

/////

///// tab | `Event Type`如果为`27`
```title='if (27)'
[objective_name][code_builder_scoreboard_score]
```

////// html | div.result
/////// define
Objective Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


///////
/////// define
Code Builder Scoreboard Score：<!-- md:samp varint -->

- 基本类型。


///////

//////

/////

///// tab | `Event Type`如果为`28`
////// define
if (28)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Event Type`如果为`29`
////// define
if (29)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///// tab | `Event Type`如果为`30`
////// define
if (30)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///

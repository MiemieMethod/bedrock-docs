# <!-- md:samp LegacyTelemetryEventPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp LegacyTelemetryEventPacket -->数据包，数字ID是`65`。该数据包用于protocol.packet.legacytelemetryeventpacket.description

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
11 -> 20
20 -> 21
7 -> 22
22 -> 23
23 -> 24
7 -> 25
25 -> 26
26 -> 27
25 -> 28
28 -> 29
7 -> 30
30 -> 31
31 -> 32
30 -> 33
33 -> 34
30 -> 35
35 -> 36
30 -> 37
37 -> 38
30 -> 39
39 -> 40
30 -> 41
41 -> 42
7 -> 43
43 -> 44
44 -> 45
43 -> 46
46 -> 47
43 -> 48
48 -> 49
7 -> 50
50 -> 51
51 -> 52
50 -> 53
53 -> 54
50 -> 55
55 -> 56
50 -> 57
57 -> 58
7 -> 59
59 -> 60
60 -> 61
59 -> 62
62 -> 63
59 -> 64
64 -> 65
7 -> 66
66 -> 67
67 -> 68
66 -> 69
69 -> 70
66 -> 71
71 -> 72
66 -> 73
73 -> 74
66 -> 75
75 -> 76
7 -> 77
77 -> 78
7 -> 79
79 -> 80
7 -> 81
81 -> 82
82 -> 83
81 -> 84
84 -> 85
81 -> 86
86 -> 87
81 -> 88
88 -> 89
7 -> 90
90 -> 91
7 -> 92
92 -> 93
93 -> 94
92 -> 95
95 -> 96
92 -> 97
97 -> 98
7 -> 99
99 -> 100
7 -> 101
101 -> 102
102 -> 103
101 -> 104
104 -> 105
7 -> 106
106 -> 107
107 -> 108
106 -> 109
109 -> 110
7 -> 111
111 -> 112
112 -> 113
7 -> 114
114 -> 115
115 -> 116
7 -> 117
117 -> 118
118 -> 119
117 -> 120
120 -> 121
117 -> 122
122 -> 123
7 -> 124
124 -> 125
7 -> 126
126 -> 127
7 -> 128
128 -> 129
7 -> 130
130 -> 131
131 -> 132
7 -> 133
133 -> 134
134 -> 135
133 -> 136
136 -> 137
7 -> 138
138 -> 139
139 -> 140
7 -> 141
141 -> 142
142 -> 143
7 -> 144
144 -> 145
145 -> 146
144 -> 147
147 -> 148
7 -> 149
149 -> 150
7 -> 151
151 -> 152
7 -> 153
153 -> 154
7 -> 155
155 -> 156
156 -> 157
155 -> 158
158 -> 159
155 -> 160
160 -> 161
155 -> 162
162 -> 163

0 [label="LegacyTelemetryEventPacket",comment="name: \"LegacyTelemetryEventPacket\", typeName: \"\", id: 0, branchId: 65, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Event Type",comment="name: \"Event Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Use Player ID",comment="name: \"Use Player ID\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Dependency on 'Event Type'",shape=note,comment="name: \"Dependency on 'Event Type'\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
8 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
9 [label="Achievement ID",comment="name: \"Achievement ID\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="varint",comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 11, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
12 [label="Interacted Entity ID",comment="name: \"Interacted Entity ID\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
13 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="Interaction Type",comment="name: \"Interaction Type\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="varint",comment="name: \"varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="Interaction Actor Type",comment="name: \"Interaction Actor Type\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
17 [label="varint",comment="name: \"varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="Interaction Actor Variant",comment="name: \"Interaction Actor Variant\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
19 [label="varint",comment="name: \"varint\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="Interaction Actor Color",comment="name: \"Interaction Actor Color\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
21 [label="byte",comment="name: \"byte\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 22, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
23 [label="Dimension ID",comment="name: \"Dimension ID\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)\""];
24 [label="varint",comment="name: \"varint\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 25, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
26 [label="Source Dimension ID",comment="name: \"Source Dimension ID\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)\""];
27 [label="varint",comment="name: \"varint\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="Target Dimension ID",comment="name: \"Target Dimension ID\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)\""];
29 [label="varint",comment="name: \"varint\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 30, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
31 [label="Instigator Actor ID",comment="name: \"Instigator Actor ID\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="Instigator's Child Actor Type",comment="name: \"Instigator's Child Actor Type\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
36 [label="varint",comment="name: \"varint\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="Damage Source",comment="name: \"Damage Source\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
38 [label="varint",comment="name: \"varint\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
39 [label="Trade Tier",comment="name: \"Trade Tier\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"-1 if not a trading actor.\""];
40 [label="varint",comment="name: \"varint\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="Trader Name",comment="name: \"Trader Name\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"Empty if not a trading actor.\""];
42 [label="string",comment="name: \"string\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
43 [label="if (5)",shape=diamond,comment="name: \"if (5)\", typeName: \"\", id: 43, branchId: 5, recurseId: -1, attributes: 4, notes: \"\""];
44 [label="Contents Color",comment="name: \"Contents Color\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
45 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
46 [label="Contents Type",comment="name: \"Contents Type\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
47 [label="varint",comment="name: \"varint\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
48 [label="Fill Level",comment="name: \"Fill Level\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
49 [label="varint",comment="name: \"varint\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
50 [label="if (6)",shape=diamond,comment="name: \"if (6)\", typeName: \"\", id: 50, branchId: 6, recurseId: -1, attributes: 4, notes: \"\""];
51 [label="Instigator Actor ID",comment="name: \"Instigator Actor ID\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
52 [label="varint",comment="name: \"varint\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
53 [label="Instigator Mob Variant",comment="name: \"Instigator Mob Variant\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
54 [label="varint",comment="name: \"varint\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
55 [label="Damage Source",comment="name: \"Damage Source\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
56 [label="varint",comment="name: \"varint\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
57 [label="Died in Raid?",comment="name: \"Died in Raid?\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
58 [label="bool",comment="name: \"bool\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
59 [label="if (7)",shape=diamond,comment="name: \"if (7)\", typeName: \"\", id: 59, branchId: 7, recurseId: -1, attributes: 4, notes: \"\""];
60 [label="Boss Actor ID",comment="name: \"Boss Actor ID\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
61 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
62 [label="Party Size",comment="name: \"Party Size\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
63 [label="varint",comment="name: \"varint\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
64 [label="Boss Type",comment="name: \"Boss Type\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
65 [label="varint",comment="name: \"varint\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
66 [label="if (8)",shape=diamond,comment="name: \"if (8)\", typeName: \"\", id: 66, branchId: 8, recurseId: -1, attributes: 4, notes: \"\""];
67 [label="Result",comment="name: \"Result\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
68 [label="varint",comment="name: \"varint\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
69 [label="Result Number",comment="name: \"Result Number\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
70 [label="varint",comment="name: \"varint\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
71 [label="Command Name",comment="name: \"Command Name\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
72 [label="string",comment="name: \"string\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
73 [label="Result Key",comment="name: \"Result Key\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
74 [label="string",comment="name: \"string\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
75 [label="Result String",comment="name: \"Result String\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
76 [label="string",comment="name: \"string\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
77 [label="if (9)",shape=diamond,comment="name: \"if (9)\", typeName: \"\", id: 77, branchId: 9, recurseId: -1, attributes: 4, notes: \"\""];
78 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
79 [label="if (10)",shape=diamond,comment="name: \"if (10)\", typeName: \"\", id: 79, branchId: 10, recurseId: -1, attributes: 4, notes: \"\""];
80 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 80, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
81 [label="if (11)",shape=diamond,comment="name: \"if (11)\", typeName: \"\", id: 81, branchId: 11, recurseId: -1, attributes: 4, notes: \"\""];
82 [label="Success Count",comment="name: \"Success Count\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
83 [label="varint",comment="name: \"varint\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
84 [label="Error Count",comment="name: \"Error Count\", typeName: \"\", id: 84, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
85 [label="varint",comment="name: \"varint\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
86 [label="Command Name",comment="name: \"Command Name\", typeName: \"\", id: 86, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
87 [label="string",comment="name: \"string\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
88 [label="Error List",comment="name: \"Error List\", typeName: \"\", id: 88, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
89 [label="string",comment="name: \"string\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
90 [label="if (12)",shape=diamond,comment="name: \"if (12)\", typeName: \"\", id: 90, branchId: 12, recurseId: -1, attributes: 4, notes: \"\""];
91 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 91, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
92 [label="if (13)",shape=diamond,comment="name: \"if (13)\", typeName: \"\", id: 92, branchId: 13, recurseId: -1, attributes: 4, notes: \"\""];
93 [label="Born Baby: Entity Type",comment="name: \"Born Baby: Entity Type\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
94 [label="varint",comment="name: \"varint\", typeName: \"\", id: 94, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
95 [label="Born Baby: Entity Variant",comment="name: \"Born Baby: Entity Variant\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
96 [label="varint",comment="name: \"varint\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
97 [label="Born Baby: Color",comment="name: \"Born Baby: Color\", typeName: \"\", id: 97, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
98 [label="byte",comment="name: \"byte\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
99 [label="if (14)",shape=diamond,comment="name: \"if (14)\", typeName: \"\", id: 99, branchId: 14, recurseId: -1, attributes: 4, notes: \"\""];
100 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
101 [label="if (15)",shape=diamond,comment="name: \"if (15)\", typeName: \"\", id: 101, branchId: 15, recurseId: -1, attributes: 4, notes: \"\""];
102 [label="Block Interaction Type",comment="name: \"Block Interaction Type\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
103 [label="varint",comment="name: \"varint\", typeName: \"\", id: 103, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
104 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 104, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the relevant item used in the interaction.\""];
105 [label="varint",comment="name: \"varint\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
106 [label="if (16)",shape=diamond,comment="name: \"if (16)\", typeName: \"\", id: 106, branchId: 16, recurseId: -1, attributes: 4, notes: \"\""];
107 [label="Block Interaction Type",comment="name: \"Block Interaction Type\", typeName: \"\", id: 107, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
108 [label="varint",comment="name: \"varint\", typeName: \"\", id: 108, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
109 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 109, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the relevant item used in the interaction.\""];
110 [label="varint",comment="name: \"varint\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
111 [label="if (17)",shape=diamond,comment="name: \"if (17)\", typeName: \"\", id: 111, branchId: 17, recurseId: -1, attributes: 4, notes: \"\""];
112 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 112, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the relevant item used in the interaction.\""];
113 [label="varint",comment="name: \"varint\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
114 [label="if (18)",shape=diamond,comment="name: \"if (18)\", typeName: \"\", id: 114, branchId: 18, recurseId: -1, attributes: 4, notes: \"\""];
115 [label="Event Name",comment="name: \"Event Name\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
116 [label="string",comment="name: \"string\", typeName: \"\", id: 116, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
117 [label="if (19)",shape=diamond,comment="name: \"if (19)\", typeName: \"\", id: 117, branchId: 19, recurseId: -1, attributes: 4, notes: \"\""];
118 [label="Current Raid Wave",comment="name: \"Current Raid Wave\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
119 [label="varint",comment="name: \"varint\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
120 [label="Total Raid Waves",comment="name: \"Total Raid Waves\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
121 [label="varint",comment="name: \"varint\", typeName: \"\", id: 121, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
122 [label="Won Raid",comment="name: \"Won Raid\", typeName: \"\", id: 122, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
123 [label="bool",comment="name: \"bool\", typeName: \"\", id: 123, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
124 [label="if (20)",shape=diamond,comment="name: \"if (20)\", typeName: \"\", id: 124, branchId: 20, recurseId: -1, attributes: 4, notes: \"\""];
125 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 125, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
126 [label="if (21)",shape=diamond,comment="name: \"if (21)\", typeName: \"\", id: 126, branchId: 21, recurseId: -1, attributes: 4, notes: \"\""];
127 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 127, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
128 [label="if (22)",shape=diamond,comment="name: \"if (22)\", typeName: \"\", id: 128, branchId: 22, recurseId: -1, attributes: 4, notes: \"\""];
129 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 129, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
130 [label="if (23)",shape=diamond,comment="name: \"if (23)\", typeName: \"\", id: 130, branchId: 23, recurseId: -1, attributes: 4, notes: \"\""];
131 [label="Redstone Level",comment="name: \"Redstone Level\", typeName: \"\", id: 131, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
132 [label="varint",comment="name: \"varint\", typeName: \"\", id: 132, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
133 [label="if (24)",shape=diamond,comment="name: \"if (24)\", typeName: \"\", id: 133, branchId: 24, recurseId: -1, attributes: 4, notes: \"\""];
134 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 134, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
135 [label="varint",comment="name: \"varint\", typeName: \"\", id: 135, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
136 [label="Was targeting bartering player",comment="name: \"Was targeting bartering player\", typeName: \"\", id: 136, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
137 [label="bool",comment="name: \"bool\", typeName: \"\", id: 137, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
138 [label="if (25)",shape=diamond,comment="name: \"if (25)\", typeName: \"\", id: 138, branchId: 25, recurseId: -1, attributes: 4, notes: \"\""];
139 [label="Player Waxed or Unwaxed Copper Block ID",comment="name: \"Player Waxed or Unwaxed Copper Block ID\", typeName: \"\", id: 139, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
140 [label="varint",comment="name: \"varint\", typeName: \"\", id: 140, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
141 [label="if (26)",shape=diamond,comment="name: \"if (26)\", typeName: \"\", id: 141, branchId: 26, recurseId: -1, attributes: 4, notes: \"\""];
142 [label="Code builder runtime action",comment="name: \"Code builder runtime action\", typeName: \"\", id: 142, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
143 [label="string",comment="name: \"string\", typeName: \"\", id: 143, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
144 [label="if (27)",shape=diamond,comment="name: \"if (27)\", typeName: \"\", id: 144, branchId: 27, recurseId: -1, attributes: 4, notes: \"\""];
145 [label="Objective Name",comment="name: \"Objective Name\", typeName: \"\", id: 145, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
146 [label="string",comment="name: \"string\", typeName: \"\", id: 146, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
147 [label="Code Builder Scoreboard Score",comment="name: \"Code Builder Scoreboard Score\", typeName: \"\", id: 147, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
148 [label="varint",comment="name: \"varint\", typeName: \"\", id: 148, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
149 [label="if (28)",shape=diamond,comment="name: \"if (28)\", typeName: \"\", id: 149, branchId: 28, recurseId: -1, attributes: 4, notes: \"\""];
150 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 150, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
151 [label="if (29)",shape=diamond,comment="name: \"if (29)\", typeName: \"\", id: 151, branchId: 29, recurseId: -1, attributes: 4, notes: \"\""];
152 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 152, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
153 [label="if (30)",shape=diamond,comment="name: \"if (30)\", typeName: \"\", id: 153, branchId: 30, recurseId: -1, attributes: 4, notes: \"\""];
154 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 154, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
155 [label="if (31)",shape=diamond,comment="name: \"if (31)\", typeName: \"\", id: 155, branchId: 31, recurseId: -1, attributes: 4, notes: \"\""];
156 [label="Item Id",comment="name: \"Item Id\", typeName: \"\", id: 156, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
157 [label="short",comment="name: \"short\", typeName: \"\", id: 157, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
158 [label="Item Aux",comment="name: \"Item Aux\", typeName: \"\", id: 158, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
159 [label="int",comment="name: \"int\", typeName: \"\", id: 159, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
160 [label="Use Method",comment="name: \"Use Method\", typeName: \"\", id: 160, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
161 [label="int",comment="name: \"int\", typeName: \"\", id: 161, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
162 [label="Use Count",comment="name: \"Use Count\", typeName: \"\", id: 162, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
163 [label="int",comment="name: \"int\", typeName: \"\", id: 163, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;10;13;15;17;19;21;24;27;29;32;34;36;38;40;42;45;47;49;52;54;56;58;61;63;65;68;70;72;74;76;78;80;83;85;87;89;91;94;96;98;100;103;105;108;110;113;116;119;121;123;125;127;129;132;135;137;140;143;146;148;150;152;154;157;159;161;163}

}

```

## 字段

```title='LegacyTelemetryEventPacket'
[target_actor_id][event_type][use_player_id][dependency_on_event_type]
```

/// html | div.result
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.legacytelemetryeventpacket.target_actor_id.description


////
//// define
Event Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.legacytelemetryeventpacket.event_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Achievement`|`0`|protocol.enum.achievement|
  |`Interaction`|`1`|protocol.enum.interaction|
  |`PortalCreated`|`2`|protocol.enum.portalcreated|
  |`PortalUsed`|`3`|protocol.enum.portalused|
  |`MobKilled`|`4`|protocol.enum.mobkilled|
  |`CauldronUsed`|`5`|protocol.enum.cauldronused|
  |`PlayerDied`|`6`|protocol.enum.playerdied|
  |`BossKilled`|`7`|protocol.enum.bosskilled|
  |`AgentCommand_OBSOLETE`|`8`|protocol.enum.agentcommand_obsolete|
  |`AgentCreated`|`9`|protocol.enum.agentcreated|
  |`PatternRemoved_OBSOLETE`|`10`|protocol.enum.patternremoved_obsolete|
  |`SlashCommand`|`11`|protocol.enum.slashcommand|
  |`Deprecated_FishBucketed`|`12`|protocol.enum.deprecated_fishbucketed|
  |`MobBorn`|`13`|protocol.enum.mobborn|
  |`PetDied_OBSOLETE`|`14`|protocol.enum.petdied_obsolete|
  |`POICauldronUsed`|`15`|protocol.enum.poicauldronused|
  |`ComposterUsed`|`16`|protocol.enum.composterused|
  |`BellUsed`|`17`|protocol.enum.bellused|
  |`ActorDefinition`|`18`|protocol.enum.actordefinition|
  |`RaidUpdate`|`19`|protocol.enum.raidupdate|
  |`PlayerMovementAnomaly_OBSOLETE`|`20`|protocol.enum.playermovementanomaly_obsolete|
  |`PlayerMovementCorrected_OBSOLETE`|`21`|protocol.enum.playermovementcorrected_obsolete|
  |`HoneyHarvested`|`22`|protocol.enum.honeyharvested|
  |`TargetBlockHit`|`23`|protocol.enum.targetblockhit|
  |`PiglinBarter`|`24`|protocol.enum.piglinbarter|
  |`PlayerWaxedOrUnwaxedCopper`|`25`|protocol.enum.playerwaxedorunwaxedcopper|
  |`CodeBuilderRuntimeAction`|`26`|protocol.enum.codebuilderruntimeaction|
  |`CodeBuilderScoreboard`|`27`|protocol.enum.codebuilderscoreboard|
  |`StriderRiddenInLavaInOverworld`|`28`|protocol.enum.striderriddeninlavainoverworld|
  |`SneakCloseToSculkSensor`|`29`|protocol.enum.sneakclosetosculksensor|
  |`CarefulRestoration`|`30`|protocol.enum.carefulrestoration|
  |`ItemUsedEvent`|`31`|protocol.enum.itemusedevent|



////
//// define
Use Player ID：<!-- md:samp byte -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.use_player_id.description


////
> 依赖于`Event Type`

///// tab | `Event Type`如果为`0`
```title='if (0)'
[achievement_id]
```

////// html | div.result
/////// define
Achievement ID：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_0.achievement_id.description


///////

//////

/////

///// tab | `Event Type`如果为`1`
```title='if (1)'
[interacted_entity_id][interaction_type][interaction_actor_type][interaction_actor_variant][interaction_actor_color]
```

////// html | div.result
/////// define
Interacted Entity ID：<!-- md:samp varint64 -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_1.interacted_entity_id.description


///////
/////// define
Interaction Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_1.interaction_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Breeding`|`1`|protocol.enum.breeding|
  |`Taming`|`2`|protocol.enum.taming|
  |`Curing`|`3`|protocol.enum.curing|
  |`Crafted`|`4`|protocol.enum.crafted|
  |`Shearing`|`5`|protocol.enum.shearing|
  |`Milking`|`6`|protocol.enum.milking|
  |`Trading`|`7`|protocol.enum.trading|
  |`Feeding`|`8`|protocol.enum.feeding|
  |`Igniting`|`9`|protocol.enum.igniting|
  |`Coloring`|`10`|protocol.enum.coloring|
  |`Naming`|`11`|protocol.enum.naming|
  |`Leashing`|`12`|protocol.enum.leashing|
  |`Unleashing`|`13`|protocol.enum.unleashing|
  |`PetSleep`|`14`|protocol.enum.petsleep|
  |`Trusting`|`15`|protocol.enum.trusting|
  |`Commanding`|`16`|protocol.enum.commanding|



///////
/////// define
Interaction Actor Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_1.interaction_actor_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`1`|protocol.enum.undefined|
  |`TypeMask`|`0x000000ff`|protocol.enum.typemask|
  |`Mob`|`0x00000100`|protocol.enum.mob|
  |`PathfinderMob`|`0x00000200 | Mob`|protocol.enum.pathfindermob|
  |`Monster`|`0x00000800 | PathfinderMob`|protocol.enum.monster|
  |`Animal`|`0x00001000 | PathfinderMob`|protocol.enum.animal|
  |`TamableAnimal`|`0x00004000 | Animal`|protocol.enum.tamableanimal|
  |`Ambient`|`0x00008000 | Mob`|protocol.enum.ambient|
  |`UndeadMob`|`0x00010000 | Monster`|protocol.enum.undeadmob|
  |`ZombieMonster`|`0x00020000 | UndeadMob`|protocol.enum.zombiemonster|
  |`Arthropod`|`0x00040000 | Monster`|protocol.enum.arthropod|
  |`Minecart`|`0x00080000`|protocol.enum.minecart|
  |`SkeletonMonster`|`0x00100000 | UndeadMob`|protocol.enum.skeletonmonster|
  |`EquineAnimal`|`0x00200000 | TamableAnimal`|protocol.enum.equineanimal|
  |`Projectile`|`0x00400000`|protocol.enum.projectile|
  |`AbstractArrow`|`0x00800000`|protocol.enum.abstractarrow|
  |`WaterAnimal`|`0x00002000 | PathfinderMob`|protocol.enum.wateranimal|
  |`VillagerBase`|`0x01000000 | PathfinderMob`|protocol.enum.villagerbase|
  |`Chicken`|`10 | Animal`|protocol.enum.chicken|
  |`Cow`|`11 | Animal`|protocol.enum.cow|
  |`Pig`|`12 | Animal`|protocol.enum.pig|
  |`Sheep`|`13 | Animal`|protocol.enum.sheep|
  |`Wolf`|`14 | TamableAnimal`|protocol.enum.wolf|
  |`Villager`|`15 | VillagerBase`|protocol.enum.villager|
  |`MushroomCow`|`16 | Animal`|protocol.enum.mushroomcow|
  |`Squid`|`17 | WaterAnimal`|protocol.enum.squid|
  |`Rabbit`|`18 | Animal`|protocol.enum.rabbit|
  |`Bat`|`19 | Ambient`|protocol.enum.bat|
  |`IronGolem`|`20 | PathfinderMob`|protocol.enum.irongolem|
  |`SnowGolem`|`21 | PathfinderMob`|protocol.enum.snowgolem|
  |`Ocelot`|`22 | TamableAnimal`|protocol.enum.ocelot|
  |`Horse`|`23 | EquineAnimal`|protocol.enum.horse|
  |`PolarBear`|`28 | Animal`|protocol.enum.polarbear|
  |`Llama`|`29 | Animal`|protocol.enum.llama|
  |`Parrot`|`30 | TamableAnimal`|protocol.enum.parrot|
  |`Dolphin`|`31 | WaterAnimal`|protocol.enum.dolphin|
  |`Donkey`|`24 | EquineAnimal`|protocol.enum.donkey|
  |`Mule`|`25 | EquineAnimal`|protocol.enum.mule|
  |`SkeletonHorse`|`26 | EquineAnimal | UndeadMob`|protocol.enum.skeletonhorse|
  |`ZombieHorse`|`27 | EquineAnimal | UndeadMob`|protocol.enum.zombiehorse|
  |`Zombie`|`32 | ZombieMonster`|protocol.enum.zombie|
  |`Creeper`|`33 | Monster`|protocol.enum.creeper|
  |`Skeleton`|`34 | SkeletonMonster`|protocol.enum.skeleton|
  |`Spider`|`35 | Arthropod`|protocol.enum.spider|
  |`PigZombie`|`36 | UndeadMob`|protocol.enum.pigzombie|
  |`Slime`|`37 | Monster`|protocol.enum.slime|
  |`EnderMan`|`38 | Monster`|protocol.enum.enderman|
  |`Silverfish`|`39 | Arthropod`|protocol.enum.silverfish|
  |`CaveSpider`|`40 | Arthropod`|protocol.enum.cavespider|
  |`Ghast`|`41 | Monster`|protocol.enum.ghast|
  |`LavaSlime`|`42 | Monster`|protocol.enum.lavaslime|
  |`Blaze`|`43 | Monster`|protocol.enum.blaze|
  |`ZombieVillager`|`44 | ZombieMonster`|protocol.enum.zombievillager|
  |`Witch`|`45 | Monster`|protocol.enum.witch|
  |`Stray`|`46 | SkeletonMonster`|protocol.enum.stray|
  |`Husk`|`47 | ZombieMonster`|protocol.enum.husk|
  |`WitherSkeleton`|`48 | SkeletonMonster`|protocol.enum.witherskeleton|
  |`Guardian`|`49 | Monster`|protocol.enum.guardian|
  |`ElderGuardian`|`50 | Monster`|protocol.enum.elderguardian|
  |`Npc`|`51 | Mob`|protocol.enum.npc|
  |`WitherBoss`|`52 | UndeadMob`|protocol.enum.witherboss|
  |`Dragon`|`53 | Monster`|protocol.enum.dragon|
  |`Shulker`|`54 | Monster`|protocol.enum.shulker|
  |`Endermite`|`55 | Arthropod`|protocol.enum.endermite|
  |`Agent`|`56 | Mob`|protocol.enum.agent|
  |`Vindicator`|`57 | Monster`|protocol.enum.vindicator|
  |`Phantom`|`58 | UndeadMob`|protocol.enum.phantom|
  |`IllagerBeast`|`59 | Monster`|protocol.enum.illagerbeast|
  |`ArmorStand`|`61 | Mob`|protocol.enum.armorstand|
  |`TripodCamera`|`62 | Mob`|protocol.enum.tripodcamera|
  |`Player`|`63 | Mob`|protocol.enum.player|
  |`ItemEntity`|`64`|protocol.enum.itementity|
  |`PrimedTnt`|`65`|protocol.enum.primedtnt|
  |`FallingBlock`|`66`|protocol.enum.fallingblock|
  |`MovingBlock`|`67`|protocol.enum.movingblock|
  |`ExperiencePotion`|`68 | Projectile`|protocol.enum.experiencepotion|
  |`Experience`|`69`|protocol.enum.experience|
  |`EyeOfEnder`|`70`|protocol.enum.eyeofender|
  |`EnderCrystal`|`71`|protocol.enum.endercrystal|
  |`FireworksRocket`|`72`|protocol.enum.fireworksrocket|
  |`Trident`|`73 | Projectile | AbstractArrow`|protocol.enum.trident|
  |`Turtle`|`74 | Animal`|protocol.enum.turtle|
  |`Cat`|`75 | TamableAnimal`|protocol.enum.cat|
  |`ShulkerBullet`|`76 | Projectile`|protocol.enum.shulkerbullet|
  |`FishingHook`|`77`|protocol.enum.fishinghook|
  |`Chalkboard`|`78`|protocol.enum.chalkboard|
  |`DragonFireball`|`79 | Projectile`|protocol.enum.dragonfireball|
  |`Arrow`|`80 | Projectile | AbstractArrow`|protocol.enum.arrow|
  |`Snowball`|`81 | Projectile`|protocol.enum.snowball|
  |`ThrownEgg`|`82 | Projectile`|protocol.enum.thrownegg|
  |`Painting`|`83`|protocol.enum.painting|
  |`LargeFireball`|`85 | Projectile`|protocol.enum.largefireball|
  |`ThrownPotion`|`86 | Projectile`|protocol.enum.thrownpotion|
  |`Enderpearl`|`87 | Projectile`|protocol.enum.enderpearl|
  |`LeashKnot`|`88`|protocol.enum.leashknot|
  |`WitherSkull`|`89 | Projectile`|protocol.enum.witherskull|
  |`BoatRideable`|`90`|protocol.enum.boatrideable|
  |`WitherSkullDangerous`|`91 | Projectile`|protocol.enum.witherskulldangerous|
  |`LightningBolt`|`93`|protocol.enum.lightningbolt|
  |`SmallFireball`|`94 | Projectile`|protocol.enum.smallfireball|
  |`AreaEffectCloud`|`95`|protocol.enum.areaeffectcloud|
  |`LingeringPotion`|`101 | Projectile`|protocol.enum.lingeringpotion|
  |`LlamaSpit`|`102 | Projectile`|protocol.enum.llamaspit|
  |`EvocationFang`|`103 | Projectile`|protocol.enum.evocationfang|
  |`EvocationIllager`|`104 | Monster`|protocol.enum.evocationillager|
  |`Vex`|`105 | Monster`|protocol.enum.vex|
  |`MinecartRideable`|`84 | Minecart`|protocol.enum.minecartrideable|
  |`MinecartHopper`|`96 | Minecart`|protocol.enum.minecarthopper|
  |`MinecartTNT`|`97 | Minecart`|protocol.enum.minecarttnt|
  |`MinecartChest`|`98 | Minecart`|protocol.enum.minecartchest|
  |`MinecartFurnace`|`99 | Minecart`|protocol.enum.minecartfurnace|
  |`MinecartCommandBlock`|`100 | Minecart`|protocol.enum.minecartcommandblock|
  |`IceBomb`|`106 | Projectile`|protocol.enum.icebomb|
  |`Balloon`|`107`|protocol.enum.balloon|
  |`Pufferfish`|`108 | WaterAnimal`|protocol.enum.pufferfish|
  |`Salmon`|`109 | WaterAnimal`|protocol.enum.salmon|
  |`Drowned`|`110 | ZombieMonster`|protocol.enum.drowned|
  |`Tropicalfish`|`111 | WaterAnimal`|protocol.enum.tropicalfish|
  |`Fish`|`112 | WaterAnimal`|protocol.enum.fish|
  |`Panda`|`113 | Animal`|protocol.enum.panda|
  |`Pillager`|`114 | Monster`|protocol.enum.pillager|
  |`VillagerV2`|`115 | VillagerBase`|protocol.enum.villagerv2|
  |`ZombieVillagerV2`|`116 | ZombieMonster`|protocol.enum.zombievillagerv2|
  |`Shield`|`117`|protocol.enum.shield|
  |`WanderingTrader`|`118 | PathfinderMob`|protocol.enum.wanderingtrader|
  |`Lectern`|`119`|protocol.enum.lectern|
  |`ElderGuardianGhost`|`120 | Monster`|protocol.enum.elderguardianghost|
  |`Fox`|`121 | Animal`|protocol.enum.fox|
  |`Bee`|`122 | Mob`|protocol.enum.bee|
  |`Piglin`|`123 | Mob`|protocol.enum.piglin|
  |`Hoglin`|`124 | Animal`|protocol.enum.hoglin|
  |`Strider`|`125 | Animal`|protocol.enum.strider|
  |`Zoglin`|`126 | UndeadMob`|protocol.enum.zoglin|
  |`PiglinBrute`|`127 | Mob`|protocol.enum.piglinbrute|
  |`Goat`|`128 | Animal`|protocol.enum.goat|
  |`GlowSquid`|`129 | WaterAnimal`|protocol.enum.glowsquid|
  |`Axolotl`|`130 | Animal`|protocol.enum.axolotl|
  |`Warden`|`131 | Monster`|protocol.enum.warden|
  |`Frog`|`132 | Animal`|protocol.enum.frog|
  |`Tadpole`|`133 | WaterAnimal`|protocol.enum.tadpole|
  |`Allay`|`134 | Mob`|protocol.enum.allay|
  |`ChestBoatRideable`|`136 | BoatRideable`|protocol.enum.chestboatrideable|
  |`TraderLlama`|`137 | Llama`|protocol.enum.traderllama|
  |`Camel`|`138 | Animal`|protocol.enum.camel|
  |`Sniffer`|`139 | Animal`|protocol.enum.sniffer|
  |`Breeze`|`140 | Monster`|protocol.enum.breeze|
  |`BreezeWindChargeProjectile`|`141 | Projectile`|protocol.enum.breezewindchargeprojectile|
  |`Armadillo`|`142 | Animal`|protocol.enum.armadillo|
  |`WindChargeProjectile`|`143 | Projectile`|protocol.enum.windchargeprojectile|
  |`Bogged`|`144 | SkeletonMonster`|protocol.enum.bogged|
  |`OminousItemSpawner`|`145`|protocol.enum.ominousitemspawner|



///////
/////// define
Interaction Actor Variant：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_1.interaction_actor_variant.description


///////
/////// define
Interaction Actor Color：<!-- md:samp byte -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_1.interaction_actor_color.description


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

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_2.dimension_id.descriptionCurrently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)


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

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_3.source_dimension_id.descriptionCurrently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)


///////
/////// define
Target Dimension ID：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_3.target_dimension_id.descriptionCurrently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)


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

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_4.instigator_actor_id.description


///////
/////// define
Target Actor ID：<!-- md:samp varint64 -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_4.target_actor_id.description


///////
/////// define
Instigator's Child Actor Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_4.instigators_child_actor_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`1`|protocol.enum.undefined|
  |`TypeMask`|`0x000000ff`|protocol.enum.typemask|
  |`Mob`|`0x00000100`|protocol.enum.mob|
  |`PathfinderMob`|`0x00000200 | Mob`|protocol.enum.pathfindermob|
  |`Monster`|`0x00000800 | PathfinderMob`|protocol.enum.monster|
  |`Animal`|`0x00001000 | PathfinderMob`|protocol.enum.animal|
  |`TamableAnimal`|`0x00004000 | Animal`|protocol.enum.tamableanimal|
  |`Ambient`|`0x00008000 | Mob`|protocol.enum.ambient|
  |`UndeadMob`|`0x00010000 | Monster`|protocol.enum.undeadmob|
  |`ZombieMonster`|`0x00020000 | UndeadMob`|protocol.enum.zombiemonster|
  |`Arthropod`|`0x00040000 | Monster`|protocol.enum.arthropod|
  |`Minecart`|`0x00080000`|protocol.enum.minecart|
  |`SkeletonMonster`|`0x00100000 | UndeadMob`|protocol.enum.skeletonmonster|
  |`EquineAnimal`|`0x00200000 | TamableAnimal`|protocol.enum.equineanimal|
  |`Projectile`|`0x00400000`|protocol.enum.projectile|
  |`AbstractArrow`|`0x00800000`|protocol.enum.abstractarrow|
  |`WaterAnimal`|`0x00002000 | PathfinderMob`|protocol.enum.wateranimal|
  |`VillagerBase`|`0x01000000 | PathfinderMob`|protocol.enum.villagerbase|
  |`Chicken`|`10 | Animal`|protocol.enum.chicken|
  |`Cow`|`11 | Animal`|protocol.enum.cow|
  |`Pig`|`12 | Animal`|protocol.enum.pig|
  |`Sheep`|`13 | Animal`|protocol.enum.sheep|
  |`Wolf`|`14 | TamableAnimal`|protocol.enum.wolf|
  |`Villager`|`15 | VillagerBase`|protocol.enum.villager|
  |`MushroomCow`|`16 | Animal`|protocol.enum.mushroomcow|
  |`Squid`|`17 | WaterAnimal`|protocol.enum.squid|
  |`Rabbit`|`18 | Animal`|protocol.enum.rabbit|
  |`Bat`|`19 | Ambient`|protocol.enum.bat|
  |`IronGolem`|`20 | PathfinderMob`|protocol.enum.irongolem|
  |`SnowGolem`|`21 | PathfinderMob`|protocol.enum.snowgolem|
  |`Ocelot`|`22 | TamableAnimal`|protocol.enum.ocelot|
  |`Horse`|`23 | EquineAnimal`|protocol.enum.horse|
  |`PolarBear`|`28 | Animal`|protocol.enum.polarbear|
  |`Llama`|`29 | Animal`|protocol.enum.llama|
  |`Parrot`|`30 | TamableAnimal`|protocol.enum.parrot|
  |`Dolphin`|`31 | WaterAnimal`|protocol.enum.dolphin|
  |`Donkey`|`24 | EquineAnimal`|protocol.enum.donkey|
  |`Mule`|`25 | EquineAnimal`|protocol.enum.mule|
  |`SkeletonHorse`|`26 | EquineAnimal | UndeadMob`|protocol.enum.skeletonhorse|
  |`ZombieHorse`|`27 | EquineAnimal | UndeadMob`|protocol.enum.zombiehorse|
  |`Zombie`|`32 | ZombieMonster`|protocol.enum.zombie|
  |`Creeper`|`33 | Monster`|protocol.enum.creeper|
  |`Skeleton`|`34 | SkeletonMonster`|protocol.enum.skeleton|
  |`Spider`|`35 | Arthropod`|protocol.enum.spider|
  |`PigZombie`|`36 | UndeadMob`|protocol.enum.pigzombie|
  |`Slime`|`37 | Monster`|protocol.enum.slime|
  |`EnderMan`|`38 | Monster`|protocol.enum.enderman|
  |`Silverfish`|`39 | Arthropod`|protocol.enum.silverfish|
  |`CaveSpider`|`40 | Arthropod`|protocol.enum.cavespider|
  |`Ghast`|`41 | Monster`|protocol.enum.ghast|
  |`LavaSlime`|`42 | Monster`|protocol.enum.lavaslime|
  |`Blaze`|`43 | Monster`|protocol.enum.blaze|
  |`ZombieVillager`|`44 | ZombieMonster`|protocol.enum.zombievillager|
  |`Witch`|`45 | Monster`|protocol.enum.witch|
  |`Stray`|`46 | SkeletonMonster`|protocol.enum.stray|
  |`Husk`|`47 | ZombieMonster`|protocol.enum.husk|
  |`WitherSkeleton`|`48 | SkeletonMonster`|protocol.enum.witherskeleton|
  |`Guardian`|`49 | Monster`|protocol.enum.guardian|
  |`ElderGuardian`|`50 | Monster`|protocol.enum.elderguardian|
  |`Npc`|`51 | Mob`|protocol.enum.npc|
  |`WitherBoss`|`52 | UndeadMob`|protocol.enum.witherboss|
  |`Dragon`|`53 | Monster`|protocol.enum.dragon|
  |`Shulker`|`54 | Monster`|protocol.enum.shulker|
  |`Endermite`|`55 | Arthropod`|protocol.enum.endermite|
  |`Agent`|`56 | Mob`|protocol.enum.agent|
  |`Vindicator`|`57 | Monster`|protocol.enum.vindicator|
  |`Phantom`|`58 | UndeadMob`|protocol.enum.phantom|
  |`IllagerBeast`|`59 | Monster`|protocol.enum.illagerbeast|
  |`ArmorStand`|`61 | Mob`|protocol.enum.armorstand|
  |`TripodCamera`|`62 | Mob`|protocol.enum.tripodcamera|
  |`Player`|`63 | Mob`|protocol.enum.player|
  |`ItemEntity`|`64`|protocol.enum.itementity|
  |`PrimedTnt`|`65`|protocol.enum.primedtnt|
  |`FallingBlock`|`66`|protocol.enum.fallingblock|
  |`MovingBlock`|`67`|protocol.enum.movingblock|
  |`ExperiencePotion`|`68 | Projectile`|protocol.enum.experiencepotion|
  |`Experience`|`69`|protocol.enum.experience|
  |`EyeOfEnder`|`70`|protocol.enum.eyeofender|
  |`EnderCrystal`|`71`|protocol.enum.endercrystal|
  |`FireworksRocket`|`72`|protocol.enum.fireworksrocket|
  |`Trident`|`73 | Projectile | AbstractArrow`|protocol.enum.trident|
  |`Turtle`|`74 | Animal`|protocol.enum.turtle|
  |`Cat`|`75 | TamableAnimal`|protocol.enum.cat|
  |`ShulkerBullet`|`76 | Projectile`|protocol.enum.shulkerbullet|
  |`FishingHook`|`77`|protocol.enum.fishinghook|
  |`Chalkboard`|`78`|protocol.enum.chalkboard|
  |`DragonFireball`|`79 | Projectile`|protocol.enum.dragonfireball|
  |`Arrow`|`80 | Projectile | AbstractArrow`|protocol.enum.arrow|
  |`Snowball`|`81 | Projectile`|protocol.enum.snowball|
  |`ThrownEgg`|`82 | Projectile`|protocol.enum.thrownegg|
  |`Painting`|`83`|protocol.enum.painting|
  |`LargeFireball`|`85 | Projectile`|protocol.enum.largefireball|
  |`ThrownPotion`|`86 | Projectile`|protocol.enum.thrownpotion|
  |`Enderpearl`|`87 | Projectile`|protocol.enum.enderpearl|
  |`LeashKnot`|`88`|protocol.enum.leashknot|
  |`WitherSkull`|`89 | Projectile`|protocol.enum.witherskull|
  |`BoatRideable`|`90`|protocol.enum.boatrideable|
  |`WitherSkullDangerous`|`91 | Projectile`|protocol.enum.witherskulldangerous|
  |`LightningBolt`|`93`|protocol.enum.lightningbolt|
  |`SmallFireball`|`94 | Projectile`|protocol.enum.smallfireball|
  |`AreaEffectCloud`|`95`|protocol.enum.areaeffectcloud|
  |`LingeringPotion`|`101 | Projectile`|protocol.enum.lingeringpotion|
  |`LlamaSpit`|`102 | Projectile`|protocol.enum.llamaspit|
  |`EvocationFang`|`103 | Projectile`|protocol.enum.evocationfang|
  |`EvocationIllager`|`104 | Monster`|protocol.enum.evocationillager|
  |`Vex`|`105 | Monster`|protocol.enum.vex|
  |`MinecartRideable`|`84 | Minecart`|protocol.enum.minecartrideable|
  |`MinecartHopper`|`96 | Minecart`|protocol.enum.minecarthopper|
  |`MinecartTNT`|`97 | Minecart`|protocol.enum.minecarttnt|
  |`MinecartChest`|`98 | Minecart`|protocol.enum.minecartchest|
  |`MinecartFurnace`|`99 | Minecart`|protocol.enum.minecartfurnace|
  |`MinecartCommandBlock`|`100 | Minecart`|protocol.enum.minecartcommandblock|
  |`IceBomb`|`106 | Projectile`|protocol.enum.icebomb|
  |`Balloon`|`107`|protocol.enum.balloon|
  |`Pufferfish`|`108 | WaterAnimal`|protocol.enum.pufferfish|
  |`Salmon`|`109 | WaterAnimal`|protocol.enum.salmon|
  |`Drowned`|`110 | ZombieMonster`|protocol.enum.drowned|
  |`Tropicalfish`|`111 | WaterAnimal`|protocol.enum.tropicalfish|
  |`Fish`|`112 | WaterAnimal`|protocol.enum.fish|
  |`Panda`|`113 | Animal`|protocol.enum.panda|
  |`Pillager`|`114 | Monster`|protocol.enum.pillager|
  |`VillagerV2`|`115 | VillagerBase`|protocol.enum.villagerv2|
  |`ZombieVillagerV2`|`116 | ZombieMonster`|protocol.enum.zombievillagerv2|
  |`Shield`|`117`|protocol.enum.shield|
  |`WanderingTrader`|`118 | PathfinderMob`|protocol.enum.wanderingtrader|
  |`Lectern`|`119`|protocol.enum.lectern|
  |`ElderGuardianGhost`|`120 | Monster`|protocol.enum.elderguardianghost|
  |`Fox`|`121 | Animal`|protocol.enum.fox|
  |`Bee`|`122 | Mob`|protocol.enum.bee|
  |`Piglin`|`123 | Mob`|protocol.enum.piglin|
  |`Hoglin`|`124 | Animal`|protocol.enum.hoglin|
  |`Strider`|`125 | Animal`|protocol.enum.strider|
  |`Zoglin`|`126 | UndeadMob`|protocol.enum.zoglin|
  |`PiglinBrute`|`127 | Mob`|protocol.enum.piglinbrute|
  |`Goat`|`128 | Animal`|protocol.enum.goat|
  |`GlowSquid`|`129 | WaterAnimal`|protocol.enum.glowsquid|
  |`Axolotl`|`130 | Animal`|protocol.enum.axolotl|
  |`Warden`|`131 | Monster`|protocol.enum.warden|
  |`Frog`|`132 | Animal`|protocol.enum.frog|
  |`Tadpole`|`133 | WaterAnimal`|protocol.enum.tadpole|
  |`Allay`|`134 | Mob`|protocol.enum.allay|
  |`ChestBoatRideable`|`136 | BoatRideable`|protocol.enum.chestboatrideable|
  |`TraderLlama`|`137 | Llama`|protocol.enum.traderllama|
  |`Camel`|`138 | Animal`|protocol.enum.camel|
  |`Sniffer`|`139 | Animal`|protocol.enum.sniffer|
  |`Breeze`|`140 | Monster`|protocol.enum.breeze|
  |`BreezeWindChargeProjectile`|`141 | Projectile`|protocol.enum.breezewindchargeprojectile|
  |`Armadillo`|`142 | Animal`|protocol.enum.armadillo|
  |`WindChargeProjectile`|`143 | Projectile`|protocol.enum.windchargeprojectile|
  |`Bogged`|`144 | SkeletonMonster`|protocol.enum.bogged|
  |`OminousItemSpawner`|`145`|protocol.enum.ominousitemspawner|



///////
/////// define
Damage Source：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_4.damage_source.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`-1`|无|
  |`Override`|`0`|protocol.enum.override|
  |`Contact`|`1`|protocol.enum.contact|
  |`EntityAttack`|`2`|protocol.enum.entityattack|
  |`Projectile`|`3`|protocol.enum.projectile|
  |`Suffocation`|`4`|protocol.enum.suffocation|
  |`Fall`|`5`|protocol.enum.fall|
  |`Fire`|`6`|protocol.enum.fire|
  |`FireTick`|`7`|protocol.enum.firetick|
  |`Lava`|`8`|protocol.enum.lava|
  |`Drowning`|`9`|protocol.enum.drowning|
  |`BlockExplosion`|`10`|protocol.enum.blockexplosion|
  |`EntityExplosion`|`11`|protocol.enum.entityexplosion|
  |`Void`|`12`|protocol.enum.void|
  |`SelfDestruct`|`13`|protocol.enum.selfdestruct|
  |`Magic`|`14`|protocol.enum.magic|
  |`Wither`|`15`|protocol.enum.wither|
  |`Starve`|`16`|protocol.enum.starve|
  |`Anvil`|`17`|protocol.enum.anvil|
  |`Thorns`|`18`|protocol.enum.thorns|
  |`FallingBlock`|`19`|protocol.enum.fallingblock|
  |`Piston`|`20`|protocol.enum.piston|
  |`FlyIntoWall`|`21`|protocol.enum.flyintowall|
  |`Magma`|`22`|protocol.enum.magma|
  |`Fireworks`|`23`|protocol.enum.fireworks|
  |`Lightning`|`24`|protocol.enum.lightning|
  |`Charging`|`25`|protocol.enum.charging|
  |`Temperature`|`26`|protocol.enum.temperature|
  |`Freezing`|`27`|protocol.enum.freezing|
  |`Stalactite`|`28`|protocol.enum.stalactite|
  |`Stalagmite`|`29`|protocol.enum.stalagmite|
  |`RamAttack`|`30`|protocol.enum.ramattack|
  |`SonicBoom`|`31`|protocol.enum.sonicboom|
  |`Campfire`|`32`|protocol.enum.campfire|
  |`SoulCampfire`|`33`|protocol.enum.soulcampfire|
  |`MaceSmash`|`34`|protocol.enum.macesmash|
  |`All`|`35`|protocol.enum.all|



///////
/////// define
Trade Tier：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_4.trade_tier.description-1 if not a trading actor.


///////
/////// define
Trader Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_4.trader_name.descriptionEmpty if not a trading actor.


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

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_5.contents_color.description


///////
/////// define
Contents Type：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_5.contents_type.description


///////
/////// define
Fill Level：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_5.fill_level.description


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

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_6.instigator_actor_id.description


///////
/////// define
Instigator Mob Variant：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_6.instigator_mob_variant.description


///////
/////// define
Damage Source：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_6.damage_source.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`-1`|无|
  |`Override`|`0`|protocol.enum.override|
  |`Contact`|`1`|protocol.enum.contact|
  |`EntityAttack`|`2`|protocol.enum.entityattack|
  |`Projectile`|`3`|protocol.enum.projectile|
  |`Suffocation`|`4`|protocol.enum.suffocation|
  |`Fall`|`5`|protocol.enum.fall|
  |`Fire`|`6`|protocol.enum.fire|
  |`FireTick`|`7`|protocol.enum.firetick|
  |`Lava`|`8`|protocol.enum.lava|
  |`Drowning`|`9`|protocol.enum.drowning|
  |`BlockExplosion`|`10`|protocol.enum.blockexplosion|
  |`EntityExplosion`|`11`|protocol.enum.entityexplosion|
  |`Void`|`12`|protocol.enum.void|
  |`SelfDestruct`|`13`|protocol.enum.selfdestruct|
  |`Magic`|`14`|protocol.enum.magic|
  |`Wither`|`15`|protocol.enum.wither|
  |`Starve`|`16`|protocol.enum.starve|
  |`Anvil`|`17`|protocol.enum.anvil|
  |`Thorns`|`18`|protocol.enum.thorns|
  |`FallingBlock`|`19`|protocol.enum.fallingblock|
  |`Piston`|`20`|protocol.enum.piston|
  |`FlyIntoWall`|`21`|protocol.enum.flyintowall|
  |`Magma`|`22`|protocol.enum.magma|
  |`Fireworks`|`23`|protocol.enum.fireworks|
  |`Lightning`|`24`|protocol.enum.lightning|
  |`Charging`|`25`|protocol.enum.charging|
  |`Temperature`|`26`|protocol.enum.temperature|
  |`Freezing`|`27`|protocol.enum.freezing|
  |`Stalactite`|`28`|protocol.enum.stalactite|
  |`Stalagmite`|`29`|protocol.enum.stalagmite|
  |`RamAttack`|`30`|protocol.enum.ramattack|
  |`SonicBoom`|`31`|protocol.enum.sonicboom|
  |`Campfire`|`32`|protocol.enum.campfire|
  |`SoulCampfire`|`33`|protocol.enum.soulcampfire|
  |`MaceSmash`|`34`|protocol.enum.macesmash|
  |`All`|`35`|protocol.enum.all|



///////
/////// define
Died in Raid?：<!-- md:samp bool -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_6.died_in_raid.description


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

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_7.boss_actor_id.description


///////
/////// define
Party Size：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_7.party_size.description


///////
/////// define
Boss Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_7.boss_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`1`|protocol.enum.undefined|
  |`TypeMask`|`0x000000ff`|protocol.enum.typemask|
  |`Mob`|`0x00000100`|protocol.enum.mob|
  |`PathfinderMob`|`0x00000200 | Mob`|protocol.enum.pathfindermob|
  |`Monster`|`0x00000800 | PathfinderMob`|protocol.enum.monster|
  |`Animal`|`0x00001000 | PathfinderMob`|protocol.enum.animal|
  |`TamableAnimal`|`0x00004000 | Animal`|protocol.enum.tamableanimal|
  |`Ambient`|`0x00008000 | Mob`|protocol.enum.ambient|
  |`UndeadMob`|`0x00010000 | Monster`|protocol.enum.undeadmob|
  |`ZombieMonster`|`0x00020000 | UndeadMob`|protocol.enum.zombiemonster|
  |`Arthropod`|`0x00040000 | Monster`|protocol.enum.arthropod|
  |`Minecart`|`0x00080000`|protocol.enum.minecart|
  |`SkeletonMonster`|`0x00100000 | UndeadMob`|protocol.enum.skeletonmonster|
  |`EquineAnimal`|`0x00200000 | TamableAnimal`|protocol.enum.equineanimal|
  |`Projectile`|`0x00400000`|protocol.enum.projectile|
  |`AbstractArrow`|`0x00800000`|protocol.enum.abstractarrow|
  |`WaterAnimal`|`0x00002000 | PathfinderMob`|protocol.enum.wateranimal|
  |`VillagerBase`|`0x01000000 | PathfinderMob`|protocol.enum.villagerbase|
  |`Chicken`|`10 | Animal`|protocol.enum.chicken|
  |`Cow`|`11 | Animal`|protocol.enum.cow|
  |`Pig`|`12 | Animal`|protocol.enum.pig|
  |`Sheep`|`13 | Animal`|protocol.enum.sheep|
  |`Wolf`|`14 | TamableAnimal`|protocol.enum.wolf|
  |`Villager`|`15 | VillagerBase`|protocol.enum.villager|
  |`MushroomCow`|`16 | Animal`|protocol.enum.mushroomcow|
  |`Squid`|`17 | WaterAnimal`|protocol.enum.squid|
  |`Rabbit`|`18 | Animal`|protocol.enum.rabbit|
  |`Bat`|`19 | Ambient`|protocol.enum.bat|
  |`IronGolem`|`20 | PathfinderMob`|protocol.enum.irongolem|
  |`SnowGolem`|`21 | PathfinderMob`|protocol.enum.snowgolem|
  |`Ocelot`|`22 | TamableAnimal`|protocol.enum.ocelot|
  |`Horse`|`23 | EquineAnimal`|protocol.enum.horse|
  |`PolarBear`|`28 | Animal`|protocol.enum.polarbear|
  |`Llama`|`29 | Animal`|protocol.enum.llama|
  |`Parrot`|`30 | TamableAnimal`|protocol.enum.parrot|
  |`Dolphin`|`31 | WaterAnimal`|protocol.enum.dolphin|
  |`Donkey`|`24 | EquineAnimal`|protocol.enum.donkey|
  |`Mule`|`25 | EquineAnimal`|protocol.enum.mule|
  |`SkeletonHorse`|`26 | EquineAnimal | UndeadMob`|protocol.enum.skeletonhorse|
  |`ZombieHorse`|`27 | EquineAnimal | UndeadMob`|protocol.enum.zombiehorse|
  |`Zombie`|`32 | ZombieMonster`|protocol.enum.zombie|
  |`Creeper`|`33 | Monster`|protocol.enum.creeper|
  |`Skeleton`|`34 | SkeletonMonster`|protocol.enum.skeleton|
  |`Spider`|`35 | Arthropod`|protocol.enum.spider|
  |`PigZombie`|`36 | UndeadMob`|protocol.enum.pigzombie|
  |`Slime`|`37 | Monster`|protocol.enum.slime|
  |`EnderMan`|`38 | Monster`|protocol.enum.enderman|
  |`Silverfish`|`39 | Arthropod`|protocol.enum.silverfish|
  |`CaveSpider`|`40 | Arthropod`|protocol.enum.cavespider|
  |`Ghast`|`41 | Monster`|protocol.enum.ghast|
  |`LavaSlime`|`42 | Monster`|protocol.enum.lavaslime|
  |`Blaze`|`43 | Monster`|protocol.enum.blaze|
  |`ZombieVillager`|`44 | ZombieMonster`|protocol.enum.zombievillager|
  |`Witch`|`45 | Monster`|protocol.enum.witch|
  |`Stray`|`46 | SkeletonMonster`|protocol.enum.stray|
  |`Husk`|`47 | ZombieMonster`|protocol.enum.husk|
  |`WitherSkeleton`|`48 | SkeletonMonster`|protocol.enum.witherskeleton|
  |`Guardian`|`49 | Monster`|protocol.enum.guardian|
  |`ElderGuardian`|`50 | Monster`|protocol.enum.elderguardian|
  |`Npc`|`51 | Mob`|protocol.enum.npc|
  |`WitherBoss`|`52 | UndeadMob`|protocol.enum.witherboss|
  |`Dragon`|`53 | Monster`|protocol.enum.dragon|
  |`Shulker`|`54 | Monster`|protocol.enum.shulker|
  |`Endermite`|`55 | Arthropod`|protocol.enum.endermite|
  |`Agent`|`56 | Mob`|protocol.enum.agent|
  |`Vindicator`|`57 | Monster`|protocol.enum.vindicator|
  |`Phantom`|`58 | UndeadMob`|protocol.enum.phantom|
  |`IllagerBeast`|`59 | Monster`|protocol.enum.illagerbeast|
  |`ArmorStand`|`61 | Mob`|protocol.enum.armorstand|
  |`TripodCamera`|`62 | Mob`|protocol.enum.tripodcamera|
  |`Player`|`63 | Mob`|protocol.enum.player|
  |`ItemEntity`|`64`|protocol.enum.itementity|
  |`PrimedTnt`|`65`|protocol.enum.primedtnt|
  |`FallingBlock`|`66`|protocol.enum.fallingblock|
  |`MovingBlock`|`67`|protocol.enum.movingblock|
  |`ExperiencePotion`|`68 | Projectile`|protocol.enum.experiencepotion|
  |`Experience`|`69`|protocol.enum.experience|
  |`EyeOfEnder`|`70`|protocol.enum.eyeofender|
  |`EnderCrystal`|`71`|protocol.enum.endercrystal|
  |`FireworksRocket`|`72`|protocol.enum.fireworksrocket|
  |`Trident`|`73 | Projectile | AbstractArrow`|protocol.enum.trident|
  |`Turtle`|`74 | Animal`|protocol.enum.turtle|
  |`Cat`|`75 | TamableAnimal`|protocol.enum.cat|
  |`ShulkerBullet`|`76 | Projectile`|protocol.enum.shulkerbullet|
  |`FishingHook`|`77`|protocol.enum.fishinghook|
  |`Chalkboard`|`78`|protocol.enum.chalkboard|
  |`DragonFireball`|`79 | Projectile`|protocol.enum.dragonfireball|
  |`Arrow`|`80 | Projectile | AbstractArrow`|protocol.enum.arrow|
  |`Snowball`|`81 | Projectile`|protocol.enum.snowball|
  |`ThrownEgg`|`82 | Projectile`|protocol.enum.thrownegg|
  |`Painting`|`83`|protocol.enum.painting|
  |`LargeFireball`|`85 | Projectile`|protocol.enum.largefireball|
  |`ThrownPotion`|`86 | Projectile`|protocol.enum.thrownpotion|
  |`Enderpearl`|`87 | Projectile`|protocol.enum.enderpearl|
  |`LeashKnot`|`88`|protocol.enum.leashknot|
  |`WitherSkull`|`89 | Projectile`|protocol.enum.witherskull|
  |`BoatRideable`|`90`|protocol.enum.boatrideable|
  |`WitherSkullDangerous`|`91 | Projectile`|protocol.enum.witherskulldangerous|
  |`LightningBolt`|`93`|protocol.enum.lightningbolt|
  |`SmallFireball`|`94 | Projectile`|protocol.enum.smallfireball|
  |`AreaEffectCloud`|`95`|protocol.enum.areaeffectcloud|
  |`LingeringPotion`|`101 | Projectile`|protocol.enum.lingeringpotion|
  |`LlamaSpit`|`102 | Projectile`|protocol.enum.llamaspit|
  |`EvocationFang`|`103 | Projectile`|protocol.enum.evocationfang|
  |`EvocationIllager`|`104 | Monster`|protocol.enum.evocationillager|
  |`Vex`|`105 | Monster`|protocol.enum.vex|
  |`MinecartRideable`|`84 | Minecart`|protocol.enum.minecartrideable|
  |`MinecartHopper`|`96 | Minecart`|protocol.enum.minecarthopper|
  |`MinecartTNT`|`97 | Minecart`|protocol.enum.minecarttnt|
  |`MinecartChest`|`98 | Minecart`|protocol.enum.minecartchest|
  |`MinecartFurnace`|`99 | Minecart`|protocol.enum.minecartfurnace|
  |`MinecartCommandBlock`|`100 | Minecart`|protocol.enum.minecartcommandblock|
  |`IceBomb`|`106 | Projectile`|protocol.enum.icebomb|
  |`Balloon`|`107`|protocol.enum.balloon|
  |`Pufferfish`|`108 | WaterAnimal`|protocol.enum.pufferfish|
  |`Salmon`|`109 | WaterAnimal`|protocol.enum.salmon|
  |`Drowned`|`110 | ZombieMonster`|protocol.enum.drowned|
  |`Tropicalfish`|`111 | WaterAnimal`|protocol.enum.tropicalfish|
  |`Fish`|`112 | WaterAnimal`|protocol.enum.fish|
  |`Panda`|`113 | Animal`|protocol.enum.panda|
  |`Pillager`|`114 | Monster`|protocol.enum.pillager|
  |`VillagerV2`|`115 | VillagerBase`|protocol.enum.villagerv2|
  |`ZombieVillagerV2`|`116 | ZombieMonster`|protocol.enum.zombievillagerv2|
  |`Shield`|`117`|protocol.enum.shield|
  |`WanderingTrader`|`118 | PathfinderMob`|protocol.enum.wanderingtrader|
  |`Lectern`|`119`|protocol.enum.lectern|
  |`ElderGuardianGhost`|`120 | Monster`|protocol.enum.elderguardianghost|
  |`Fox`|`121 | Animal`|protocol.enum.fox|
  |`Bee`|`122 | Mob`|protocol.enum.bee|
  |`Piglin`|`123 | Mob`|protocol.enum.piglin|
  |`Hoglin`|`124 | Animal`|protocol.enum.hoglin|
  |`Strider`|`125 | Animal`|protocol.enum.strider|
  |`Zoglin`|`126 | UndeadMob`|protocol.enum.zoglin|
  |`PiglinBrute`|`127 | Mob`|protocol.enum.piglinbrute|
  |`Goat`|`128 | Animal`|protocol.enum.goat|
  |`GlowSquid`|`129 | WaterAnimal`|protocol.enum.glowsquid|
  |`Axolotl`|`130 | Animal`|protocol.enum.axolotl|
  |`Warden`|`131 | Monster`|protocol.enum.warden|
  |`Frog`|`132 | Animal`|protocol.enum.frog|
  |`Tadpole`|`133 | WaterAnimal`|protocol.enum.tadpole|
  |`Allay`|`134 | Mob`|protocol.enum.allay|
  |`ChestBoatRideable`|`136 | BoatRideable`|protocol.enum.chestboatrideable|
  |`TraderLlama`|`137 | Llama`|protocol.enum.traderllama|
  |`Camel`|`138 | Animal`|protocol.enum.camel|
  |`Sniffer`|`139 | Animal`|protocol.enum.sniffer|
  |`Breeze`|`140 | Monster`|protocol.enum.breeze|
  |`BreezeWindChargeProjectile`|`141 | Projectile`|protocol.enum.breezewindchargeprojectile|
  |`Armadillo`|`142 | Animal`|protocol.enum.armadillo|
  |`WindChargeProjectile`|`143 | Projectile`|protocol.enum.windchargeprojectile|
  |`Bogged`|`144 | SkeletonMonster`|protocol.enum.bogged|
  |`OminousItemSpawner`|`145`|protocol.enum.ominousitemspawner|



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

- 基本类型枚举。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_8.result.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ActionFail`|`0`|protocol.enum.actionfail|
  |`ActionSuccess`|`1`|protocol.enum.actionsuccess|
  |`QueryResultFalse`|`2`|protocol.enum.queryresultfalse|
  |`QueryResultTrue`|`3`|protocol.enum.queryresulttrue|



///////
/////// define
Result Number：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_8.result_number.description


///////
/////// define
Command Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_8.command_name.description


///////
/////// define
Result Key：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_8.result_key.description


///////
/////// define
Result String：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_8.result_string.description


///////

//////

/////

///// tab | `Event Type`如果为`9`
////// define
if (9)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`10`
////// define
if (10)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`11`
```title='if (11)'
[success_count][error_count][command_name][error_list]
```

////// html | div.result
/////// define
Success Count：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_11.success_count.description


///////
/////// define
Error Count：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_11.error_count.description


///////
/////// define
Command Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_11.command_name.description


///////
/////// define
Error List：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_11.error_list.description


///////

//////

/////

///// tab | `Event Type`如果为`12`
////// define
if (12)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`13`
```title='if (13)'
[born_baby:_entity_type][born_baby:_entity_variant][born_baby:_color]
```

////// html | div.result
/////// define
Born Baby: Entity Type：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_13.born_baby:_entity_type.description


///////
/////// define
Born Baby: Entity Variant：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_13.born_baby:_entity_variant.description


///////
/////// define
Born Baby: Color：<!-- md:samp byte -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_13.born_baby:_color.description


///////

//////

/////

///// tab | `Event Type`如果为`14`
////// define
if (14)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`15`
```title='if (15)'
[block_interaction_type][item_id]
```

////// html | div.result
/////// define
Block Interaction Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_15.block_interaction_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Extend`|`1`|protocol.enum.extend|
  |`Clone`|`2`|protocol.enum.clone|
  |`Lock`|`3`|protocol.enum.lock|
  |`Create`|`4`|protocol.enum.create|
  |`CreateLocator`|`5`|protocol.enum.createlocator|
  |`Rename`|`6`|protocol.enum.rename|
  |`ItemPlaced`|`7`|protocol.enum.itemplaced|
  |`ItemRemoved`|`8`|protocol.enum.itemremoved|
  |`Cooking`|`9`|protocol.enum.cooking|
  |`Dousing`|`10`|protocol.enum.dousing|
  |`Lighting`|`11`|protocol.enum.lighting|
  |`Haystack`|`12`|protocol.enum.haystack|
  |`Filled`|`13`|protocol.enum.filled|
  |`Emptied`|`14`|protocol.enum.emptied|
  |`AddDye`|`15`|protocol.enum.adddye|
  |`DyeItem`|`16`|protocol.enum.dyeitem|
  |`ClearItem`|`17`|protocol.enum.clearitem|
  |`EnchantArrow`|`18`|protocol.enum.enchantarrow|
  |`CompostItemPlaced`|`19`|protocol.enum.compostitemplaced|
  |`RecoveredBonemeal`|`20`|protocol.enum.recoveredbonemeal|
  |`BookPlaced`|`21`|protocol.enum.bookplaced|
  |`BookOpened`|`22`|protocol.enum.bookopened|
  |`Disenchant`|`23`|protocol.enum.disenchant|
  |`Repair`|`24`|protocol.enum.repair|
  |`DisenchantAndRepair`|`25`|protocol.enum.disenchantandrepair|



///////
/////// define
Item Id：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_15.item_id.descriptionId of the relevant item used in the interaction.


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

- 基本类型枚举。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_16.block_interaction_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Extend`|`1`|protocol.enum.extend|
  |`Clone`|`2`|protocol.enum.clone|
  |`Lock`|`3`|protocol.enum.lock|
  |`Create`|`4`|protocol.enum.create|
  |`CreateLocator`|`5`|protocol.enum.createlocator|
  |`Rename`|`6`|protocol.enum.rename|
  |`ItemPlaced`|`7`|protocol.enum.itemplaced|
  |`ItemRemoved`|`8`|protocol.enum.itemremoved|
  |`Cooking`|`9`|protocol.enum.cooking|
  |`Dousing`|`10`|protocol.enum.dousing|
  |`Lighting`|`11`|protocol.enum.lighting|
  |`Haystack`|`12`|protocol.enum.haystack|
  |`Filled`|`13`|protocol.enum.filled|
  |`Emptied`|`14`|protocol.enum.emptied|
  |`AddDye`|`15`|protocol.enum.adddye|
  |`DyeItem`|`16`|protocol.enum.dyeitem|
  |`ClearItem`|`17`|protocol.enum.clearitem|
  |`EnchantArrow`|`18`|protocol.enum.enchantarrow|
  |`CompostItemPlaced`|`19`|protocol.enum.compostitemplaced|
  |`RecoveredBonemeal`|`20`|protocol.enum.recoveredbonemeal|
  |`BookPlaced`|`21`|protocol.enum.bookplaced|
  |`BookOpened`|`22`|protocol.enum.bookopened|
  |`Disenchant`|`23`|protocol.enum.disenchant|
  |`Repair`|`24`|protocol.enum.repair|
  |`DisenchantAndRepair`|`25`|protocol.enum.disenchantandrepair|



///////
/////// define
Item Id：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_16.item_id.descriptionId of the relevant item used in the interaction.


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

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_17.item_id.descriptionId of the relevant item used in the interaction.


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

- 特殊类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_18.event_name.description


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

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_19.current_raid_wave.description


///////
/////// define
Total Raid Waves：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_19.total_raid_waves.description


///////
/////// define
Won Raid：<!-- md:samp bool -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_19.won_raid.description


///////

//////

/////

///// tab | `Event Type`如果为`20`
////// define
if (20)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`21`
////// define
if (21)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`22`
////// define
if (22)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`23`
```title='if (23)'
[redstone_level]
```

////// html | div.result
/////// define
Redstone Level：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_23.redstone_level.description


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

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_24.item_id.description


///////
/////// define
Was targeting bartering player：<!-- md:samp bool -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_24.was_targeting_bartering_player.description


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

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_25.player_waxed_or_unwaxed_copper_block_id.description


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

- 特殊类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_26.code_builder_runtime_action.description


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

- 特殊类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_27.objective_name.description


///////
/////// define
Code Builder Scoreboard Score：<!-- md:samp varint -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_27.code_builder_scoreboard_score.description


///////

//////

/////

///// tab | `Event Type`如果为`28`
////// define
if (28)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`29`
////// define
if (29)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`30`
////// define
if (30)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Event Type`如果为`31`
```title='if (31)'
[item_id][item_aux][use_method][use_count]
```

////// html | div.result
/////// define
Item Id：<!-- md:samp short -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_31.item_id.description


///////
/////// define
Item Aux：<!-- md:samp int -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_31.item_aux.description


///////
/////// define
Use Method：<!-- md:samp int -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_31.use_method.description


///////
/////// define
Use Count：<!-- md:samp int -->

- 基本类型。protocol.packet.legacytelemetryeventpacket.dependency_on_event_type.if_31.use_count.description


///////

//////

/////

///


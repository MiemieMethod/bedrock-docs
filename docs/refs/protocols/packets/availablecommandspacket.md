# <!-- md:samp AvailableCommandsPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp AvailableCommandsPacket -->数据包，数字ID是`76`。该数据包用于protocol.packet.availablecommandspacket.description

## 结构

```viz
digraph "AvailableCommandsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6
0 -> 7
7 -> 8
8 -> 9
7 -> 10
10 -> 11
11 -> 12
0 -> 13
13 -> 14
14 -> 15
13 -> 16
16 -> 17
17 -> 18
0 -> 19
19 -> 20
20 -> 21
19 -> 22
22 -> 23
23 -> 24
22 -> 25
25 -> 26
26 -> 27
25 -> 28
28 -> 29
29 -> 30
30 -> 31
31 -> 32
32 -> 33
33 -> 34
31 -> 35
35 -> 36
36 -> 37
29 -> 38
38 -> 39
39 -> 40
0 -> 41
41 -> 42
42 -> 43
41 -> 44
44 -> 45
45 -> 46
44 -> 47
47 -> 48
48 -> 49
47 -> 50
50 -> 51
51 -> 52
50 -> 53
53 -> 54
0 -> 55
55 -> 56
56 -> 57
55 -> 58
58 -> 59
59 -> 60
58 -> 61
61 -> 62
58 -> 63
63 -> 64
58 -> 65
65 -> 66
58 -> 67
67 -> 68
58 -> 69
69 -> 70
70 -> 71
69 -> 72
72 -> 73
73 -> 74
58 -> 75
75 -> 76
76 -> 77
75 -> 78
78 -> 79
79 -> 80
78 -> 81
81 -> 82
82 -> 83
81 -> 84
84 -> 85
85 -> 86
84 -> 87
87 -> 88
84 -> 89
89 -> 90
84 -> 91
91 -> 92
0 -> 93
93 -> 94
94 -> 95
93 -> 96
96 -> 97
97 -> 98
96 -> 99
99 -> 100
100 -> 101
99 -> 102
102 -> 103
103 -> 104
0 -> 105
105 -> 106
106 -> 107
105 -> 108
108 -> 109
109 -> 110
108 -> 111
111 -> 112
108 -> 113
113 -> 114
114 -> 115
113 -> 116
116 -> 117
117 -> 118

0 [label="AvailableCommandsPacket",comment="name: \"AvailableCommandsPacket\", typeName: \"\", id: 0, branchId: 76, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Enum Values",comment="name: \"Enum Values\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Value",comment="name: \"Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Enum Values",comment="name: \"Enum Values\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
8 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
9 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
11 [label="Chained Subcommand Values",comment="name: \"Chained Subcommand Values\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="string",comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Post Fixes",comment="name: \"Post Fixes\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
14 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
17 [label="Post Fix",comment="name: \"Post Fix\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="string",comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="Enum Data",comment="name: \"Enum Data\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
20 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
21 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
22 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
23 [label="Name",comment="name: \"Name\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="string",comment="name: \"string\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Values",comment="name: \"Values\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
26 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
27 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
29 [label="Dependency on 'Enum Values Size <= 256'",shape=note,comment="name: \"Dependency on 'Enum Values Size <= 256'\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
30 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
31 [label="Dependency on 'Enum Values Size <= 65536'",shape=note,comment="name: \"Dependency on 'Enum Values Size <= 65536'\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
32 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
33 [label="Enum Value",comment="name: \"Enum Value\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 35, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
36 [label="Enum Value",comment="name: \"Enum Value\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
37 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
38 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 38, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
39 [label="Enum Value",comment="name: \"Enum Value\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
40 [label="byte",comment="name: \"byte\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="Chained Subcommand Data",comment="name: \"Chained Subcommand Data\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
42 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
43 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
44 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
45 [label="SubCommand Name",comment="name: \"SubCommand Name\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
46 [label="string",comment="name: \"string\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
47 [label="SubCommand values",comment="name: \"SubCommand values\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
48 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
49 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
50 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
51 [label="SubCommand First Value",comment="name: \"SubCommand First Value\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
52 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
53 [label="SubCommand Second Value",comment="name: \"SubCommand Second Value\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
54 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
55 [label="Commands",comment="name: \"Commands\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
56 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
57 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
58 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
59 [label="Name",comment="name: \"Name\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
60 [label="string",comment="name: \"string\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
61 [label="Description",comment="name: \"Description\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
62 [label="string",comment="name: \"string\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
63 [label="Flags",comment="name: \"Flags\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
64 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
65 [label="Permission Level",comment="name: \"Permission Level\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
66 [label="byte",comment="name: \"byte\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
67 [label="Alias Enum",comment="name: \"Alias Enum\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
68 [label="int",comment="name: \"int\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
69 [label="CommandData Chained Subcommand Indexes",comment="name: \"CommandData Chained Subcommand Indexes\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
70 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
71 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
72 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
73 [label="Index",comment="name: \"Index\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
74 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
75 [label="Overloads",comment="name: \"Overloads\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
76 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
77 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 77, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
78 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
79 [label="isChaining",comment="name: \"isChaining\", typeName: \"\", id: 79, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
80 [label="bool",comment="name: \"bool\", typeName: \"\", id: 80, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
81 [label="Parameter Data",comment="name: \"Parameter Data\", typeName: \"\", id: 81, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
82 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
83 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
84 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 84, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
85 [label="Name",comment="name: \"Name\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
86 [label="string",comment="name: \"string\", typeName: \"\", id: 86, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
87 [label="Parse Symbol",comment="name: \"Parse Symbol\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
88 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 88, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
89 [label="Is Optional?",comment="name: \"Is Optional?\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
90 [label="bool",comment="name: \"bool\", typeName: \"\", id: 90, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
91 [label="Options",comment="name: \"Options\", typeName: \"\", id: 91, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
92 [label="byte",comment="name: \"byte\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
93 [label="Soft Enums",comment="name: \"Soft Enums\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
94 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 94, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
95 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
96 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
97 [label="Enum Name",comment="name: \"Enum Name\", typeName: \"\", id: 97, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
98 [label="string",comment="name: \"string\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
99 [label="Enum Options",comment="name: \"Enum Options\", typeName: \"\", id: 99, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
100 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
101 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
102 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
103 [label="Value",comment="name: \"Value\", typeName: \"\", id: 103, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
104 [label="string",comment="name: \"string\", typeName: \"\", id: 104, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
105 [label="Constraints",comment="name: \"Constraints\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
106 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 106, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
107 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 107, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
108 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 108, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
109 [label="Enum Value Symbol",comment="name: \"Enum Value Symbol\", typeName: \"\", id: 109, branchId: 0, recurseId: -1, attributes: 0, notes: \"Symbol in the command parser representing this enum's value.\""];
110 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
111 [label="Enum Symbol",comment="name: \"Enum Symbol\", typeName: \"\", id: 111, branchId: 0, recurseId: -1, attributes: 0, notes: \"Symbol in the command parser representing this enum.\""];
112 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 112, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
113 [label="Constraint Indices",comment="name: \"Constraint Indices\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
114 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
115 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
116 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 116, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
117 [label="Semantic Constraint Index",comment="name: \"Semantic Constraint Index\", typeName: \"\", id: 117, branchId: 0, recurseId: -1, attributes: 0, notes: \"Index of the semantic constraint within the command parser.\""];
118 [label="byte",comment="name: \"byte\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6;9;12;15;18;21;24;27;34;37;40;43;46;49;52;54;57;60;62;64;66;68;71;74;77;80;83;86;88;90;92;95;98;101;104;107;110;112;115;118}

}

```

## 字段

```title='AvailableCommandsPacket'
[enum_values][enum_values][post_fixes][enum_data][chained_subcommand_data][commands][soft_enums][constraints]
```

/// html | div.result
```title='Enum Values'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.enum_values.array_size.description


/////
```title='示例元素'
[value]
```

///// html | div.result
////// define
Value：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.availablecommandspacket.enum_values.example_element.value.description


//////

/////

////
```title='Enum Values'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.enum_values.array_size.description


/////
```title='示例元素'
[chained_subcommand_values]
```

///// html | div.result
////// define
Chained Subcommand Values：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.availablecommandspacket.enum_values.example_element.chained_subcommand_values.description


//////

/////

////
```title='Post Fixes'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.post_fixes.array_size.description


/////
```title='示例元素'
[post_fix]
```

///// html | div.result
////// define
Post Fix：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.availablecommandspacket.post_fixes.example_element.post_fix.description


//////

/////

////
```title='Enum Data'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.enum_data.array_size.description


/////
```title='示例元素'
[name][values]
```

///// html | div.result
////// define
Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.availablecommandspacket.enum_data.example_element.name.description


//////
```title='Values'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.enum_data.example_element.values.array_size.description


///////
```title='示例元素'
[dependency_on_enum_values_size_le_256]
```

/////// html | div.result
> 依赖于`Enum Values Size <= 256`

///////// tab | `Enum Values Size <= 256`如果为`0`
```title='if (0)'
[dependency_on_enum_values_size_le_65536]
```

////////// html | div.result
> 依赖于`Enum Values Size <= 65536`

//////////// tab | `Enum Values Size <= 65536`如果为`0`
```title='if (0)'
[enum_value]
```

///////////// html | div.result
////////////// define
Enum Value：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.availablecommandspacket.enum_data.example_element.values.example_element.dependency_on_enum_values_size_le_256.if_0.dependency_on_enum_values_size_le_65536.if_0.enum_value.description


//////////////

/////////////

////////////

//////////// tab | `Enum Values Size <= 65536`如果为`1`
```title='if (1)'
[enum_value]
```

///////////// html | div.result
////////////// define
Enum Value：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.availablecommandspacket.enum_data.example_element.values.example_element.dependency_on_enum_values_size_le_256.if_0.dependency_on_enum_values_size_le_65536.if_1.enum_value.description


//////////////

/////////////

////////////

//////////

/////////

///////// tab | `Enum Values Size <= 256`如果为`1`
```title='if (1)'
[enum_value]
```

////////// html | div.result
/////////// define
Enum Value：<!-- md:samp byte -->

- 基本类型。protocol.packet.availablecommandspacket.enum_data.example_element.values.example_element.dependency_on_enum_values_size_le_256.if_1.enum_value.description


///////////

//////////

/////////

///////

//////

/////

////
```title='Chained Subcommand Data'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.chained_subcommand_data.array_size.description


/////
```title='示例元素'
[subcommand_name][subcommand_values]
```

///// html | div.result
////// define
SubCommand Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.availablecommandspacket.chained_subcommand_data.example_element.subcommand_name.description


//////
```title='SubCommand values'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.chained_subcommand_data.example_element.subcommand_values.array_size.description


///////
```title='示例元素'
[subcommand_first_value][subcommand_second_value]
```

/////// html | div.result
//////// define
SubCommand First Value：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.availablecommandspacket.chained_subcommand_data.example_element.subcommand_values.example_element.subcommand_first_value.description


////////
//////// define
SubCommand Second Value：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.availablecommandspacket.chained_subcommand_data.example_element.subcommand_values.example_element.subcommand_second_value.description


////////

///////

//////

/////

////
```title='Commands'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.commands.array_size.description


/////
```title='示例元素'
[name][description][flags][permission_level][alias_enum][commanddata_chained_subcommand_indexes][overloads]
```

///// html | div.result
////// define
Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.availablecommandspacket.commands.example_element.name.description


//////
////// define
Description：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.availablecommandspacket.commands.example_element.description.description


//////
////// define
Flags：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.availablecommandspacket.commands.example_element.flags.description


//////
////// define
Permission Level：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.availablecommandspacket.commands.example_element.permission_level.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Any`|`0`|protocol.enum.any|
  |`GameDirectors`|`1`|protocol.enum.gamedirectors|
  |`Admin`|`2`|protocol.enum.admin|
  |`Host`|`3`|protocol.enum.host|
  |`Owner`|`4`|protocol.enum.owner|
  |`Internal`|`5`|protocol.enum.internal|



//////
////// define
Alias Enum：<!-- md:samp int -->

- 基本类型。protocol.packet.availablecommandspacket.commands.example_element.alias_enum.description


//////
```title='CommandData Chained Subcommand Indexes'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.commands.example_element.commanddata_chained_subcommand_indexes.array_size.description


///////
```title='示例元素'
[index]
```

/////// html | div.result
//////// define
Index：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.availablecommandspacket.commands.example_element.commanddata_chained_subcommand_indexes.example_element.index.description


////////

///////

//////
```title='Overloads'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.commands.example_element.overloads.array_size.description


///////
```title='示例元素'
[ischaining][parameter_data]
```

/////// html | div.result
//////// define
isChaining：<!-- md:samp bool -->

- 基本类型。protocol.packet.availablecommandspacket.commands.example_element.overloads.example_element.ischaining.description


////////
```title='Parameter Data'
[array_size][[example_element]..]
```

//////// html | div.result
///////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.commands.example_element.overloads.example_element.parameter_data.array_size.description


/////////
```title='示例元素'
[name][parse_symbol][is_optional][options]
```

///////// html | div.result
////////// define
Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.availablecommandspacket.commands.example_element.overloads.example_element.parameter_data.example_element.name.description


//////////
////////// define
Parse Symbol：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.availablecommandspacket.commands.example_element.overloads.example_element.parameter_data.example_element.parse_symbol.description


//////////
////////// define
Is Optional?：<!-- md:samp bool -->

- 基本类型。protocol.packet.availablecommandspacket.commands.example_element.overloads.example_element.parameter_data.example_element.is_optional.description


//////////
////////// define
Options：<!-- md:samp byte -->

- 基本类型。protocol.packet.availablecommandspacket.commands.example_element.overloads.example_element.parameter_data.example_element.options.description


//////////

/////////

////////

///////

//////

/////

////
```title='Soft Enums'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.soft_enums.array_size.description


/////
```title='示例元素'
[enum_name][enum_options]
```

///// html | div.result
////// define
Enum Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.availablecommandspacket.soft_enums.example_element.enum_name.description


//////
```title='Enum Options'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.soft_enums.example_element.enum_options.array_size.description


///////
```title='示例元素'
[value]
```

/////// html | div.result
//////// define
Value：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.availablecommandspacket.soft_enums.example_element.enum_options.example_element.value.description


////////

///////

//////

/////

////
```title='Constraints'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.constraints.array_size.description


/////
```title='示例元素'
[enum_value_symbol][enum_symbol][constraint_indices]
```

///// html | div.result
////// define
Enum Value Symbol：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.availablecommandspacket.constraints.example_element.enum_value_symbol.descriptionSymbol in the command parser representing this enum's value.


//////
////// define
Enum Symbol：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.availablecommandspacket.constraints.example_element.enum_symbol.descriptionSymbol in the command parser representing this enum.


//////
```title='Constraint Indices'
[array_size][[example_element]..]
```

////// html | div.result
/////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.availablecommandspacket.constraints.example_element.constraint_indices.array_size.description


///////
```title='示例元素'
[semantic_constraint_index]
```

/////// html | div.result
//////// define
Semantic Constraint Index：<!-- md:samp byte -->

- 基本类型。protocol.packet.availablecommandspacket.constraints.example_element.constraint_indices.example_element.semantic_constraint_index.descriptionIndex of the semantic constraint within the command parser.


////////

///////

//////

/////

////

///


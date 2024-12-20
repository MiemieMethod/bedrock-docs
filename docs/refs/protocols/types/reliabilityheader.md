# <!-- md:samp Reliability Header -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp Reliability Header -->类型。该类型用于protocol.type.reliability_header.description

## 结构

```viz
digraph "Reliability Header" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
6 -> 7
5 -> 8
8 -> 9
9 -> 10
8 -> 11
11 -> 12
8 -> 13
13 -> 14
5 -> 15
15 -> 16
16 -> 17
5 -> 18
18 -> 19
19 -> 20
18 -> 21
21 -> 22
18 -> 23
23 -> 24
5 -> 25
25 -> 26
26 -> 27
25 -> 28
28 -> 29
25 -> 30
30 -> 31
25 -> 32
32 -> 33
0 -> 34
34 -> 35
35 -> 36
34 -> 37
37 -> 38
38 -> 39
37 -> 40
40 -> 41
37 -> 42
42 -> 43

0 [label="Reliability Header",comment="name: \"Reliability Header\", typeName: \"\", id: 0, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Reliability Type (3 bits), is packet split? (1 bit)",comment="name: \"Reliability Type (3 bits), is packet split? (1 bit)\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Payload Bit Length",comment="name: \"Payload Bit Length\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Reliability Type'",shape=note,comment="name: \"Dependency on 'Reliability Type'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
8 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 8, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
9 [label="Sequenced Index",comment="name: \"Sequenced Index\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="unsigned int24",comment="name: \"unsigned int24\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Ordering Index",comment="name: \"Ordering Index\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="unsigned int24",comment="name: \"unsigned int24\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Ordering Channel",comment="name: \"Ordering Channel\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="byte",comment="name: \"byte\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 15, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
16 [label="Reliable Message",comment="name: \"Reliable Message\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
17 [label="unsigned int24",comment="name: \"unsigned int24\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 18, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
19 [label="Reliable Message",comment="name: \"Reliable Message\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
20 [label="unsigned int24",comment="name: \"unsigned int24\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
21 [label="Ordering Index",comment="name: \"Ordering Index\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="unsigned int24",comment="name: \"unsigned int24\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Ordering Channel",comment="name: \"Ordering Channel\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="byte",comment="name: \"byte\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 25, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
26 [label="Reliable Message",comment="name: \"Reliable Message\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
27 [label="unsigned int24",comment="name: \"unsigned int24\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="Sequenced Index",comment="name: \"Sequenced Index\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
29 [label="unsigned int24",comment="name: \"unsigned int24\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="Ordering Index",comment="name: \"Ordering Index\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
31 [label="unsigned int24",comment="name: \"unsigned int24\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
32 [label="Ordering Channel",comment="name: \"Ordering Channel\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
33 [label="byte",comment="name: \"byte\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
34 [label="Dependency on 'Is Packet Split?'",shape=note,comment="name: \"Dependency on 'Is Packet Split?'\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
35 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
36 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 37, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
38 [label="Split Packet Count",comment="name: \"Split Packet Count\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
39 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
40 [label="Split Packet Id",comment="name: \"Split Packet Id\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
41 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
42 [label="Split Packet Index",comment="name: \"Split Packet Index\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
43 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;7;10;12;14;17;20;22;24;27;29;31;33;36;39;41;43}

}

```

## 字段

```title='Reliability Header'
[reliability_type_is_packet_split][payload_bit_length][dependency_on_reliability_type][dependency_on_is_packet_split]
```

/// html | div.result
//// define
Reliability Type (3 bits), is packet split? (1 bit)：<!-- md:samp byte -->

- 基本类型。protocol.type.reliability_header.reliability_type_is_packet_split.description


////
//// define
Payload Bit Length：<!-- md:samp unsigned short -->

- 基本类型。protocol.type.reliability_header.payload_bit_length.description


////
> 依赖于`Reliability Type`

///// tab | `Reliability Type`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Reliability Type`如果为`1`
```title='if (1)'
[sequenced_index][ordering_index][ordering_channel]
```

////// html | div.result
/////// define
Sequenced Index：<!-- md:samp unsigned int24 -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_1.sequenced_index.description


///////
/////// define
Ordering Index：<!-- md:samp unsigned int24 -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_1.ordering_index.description


///////
/////// define
Ordering Channel：<!-- md:samp byte -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_1.ordering_channel.description


///////

//////

/////

///// tab | `Reliability Type`如果为`2`
```title='if (2)'
[reliable_message]
```

////// html | div.result
/////// define
Reliable Message：<!-- md:samp unsigned int24 -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_2.reliable_message.description


///////

//////

/////

///// tab | `Reliability Type`如果为`3`
```title='if (3)'
[reliable_message][ordering_index][ordering_channel]
```

////// html | div.result
/////// define
Reliable Message：<!-- md:samp unsigned int24 -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_3.reliable_message.description


///////
/////// define
Ordering Index：<!-- md:samp unsigned int24 -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_3.ordering_index.description


///////
/////// define
Ordering Channel：<!-- md:samp byte -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_3.ordering_channel.description


///////

//////

/////

///// tab | `Reliability Type`如果为`4`
```title='if (4)'
[reliable_message][sequenced_index][ordering_index][ordering_channel]
```

////// html | div.result
/////// define
Reliable Message：<!-- md:samp unsigned int24 -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_4.reliable_message.description


///////
/////// define
Sequenced Index：<!-- md:samp unsigned int24 -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_4.sequenced_index.description


///////
/////// define
Ordering Index：<!-- md:samp unsigned int24 -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_4.ordering_index.description


///////
/////// define
Ordering Channel：<!-- md:samp byte -->

- 基本类型。protocol.type.reliability_header.dependency_on_reliability_type.if_4.ordering_channel.description


///////

//////

/////
> 依赖于`Is Packet Split?`

///// tab | `Is Packet Split?`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Is Packet Split?`如果为`1`
```title='if (1)'
[split_packet_count][split_packet_id][split_packet_index]
```

////// html | div.result
/////// define
Split Packet Count：<!-- md:samp unsigned int -->

- 基本类型。protocol.type.reliability_header.dependency_on_is_packet_split.if_1.split_packet_count.description


///////
/////// define
Split Packet Id：<!-- md:samp unsigned short -->

- 基本类型。protocol.type.reliability_header.dependency_on_is_packet_split.if_1.split_packet_id.description


///////
/////// define
Split Packet Index：<!-- md:samp unsigned int -->

- 基本类型。protocol.type.reliability_header.dependency_on_is_packet_split.if_1.split_packet_index.description


///////

//////

/////

///


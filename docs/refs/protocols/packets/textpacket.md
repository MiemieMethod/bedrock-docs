# <!-- md:samp TextPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp TextPacket -->数据包，数字ID是`9`。该数据包用于protocol.packet.textpacket.description

## 结构

```viz
digraph "TextPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
6 -> 7
7 -> 8
5 -> 9
9 -> 10
10 -> 11
9 -> 12
12 -> 13
5 -> 14
14 -> 15
15 -> 16
14 -> 17
17 -> 18
18 -> 19
17 -> 20
20 -> 21
21 -> 22
5 -> 23
23 -> 24
24 -> 25
23 -> 26
26 -> 27
27 -> 28
26 -> 29
29 -> 30
30 -> 31
5 -> 32
32 -> 33
33 -> 34
32 -> 35
35 -> 36
36 -> 37
35 -> 38
38 -> 39
39 -> 40
5 -> 41
41 -> 42
42 -> 43
5 -> 44
44 -> 45
45 -> 46
5 -> 47
47 -> 48
48 -> 49
47 -> 50
50 -> 51
5 -> 52
52 -> 53
53 -> 54
52 -> 55
55 -> 56
5 -> 57
57 -> 58
58 -> 59
5 -> 60
60 -> 61
61 -> 62
5 -> 63
63 -> 64
64 -> 65
0 -> 66
66 -> 67
0 -> 68
68 -> 69
0 -> 70
70 -> 71

0 [label="TextPacket",comment="name: \"TextPacket\", typeName: \"\", id: 0, branchId: 9, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Message Type",comment="name: \"Message Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Localize?",comment="name: \"Localize?\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Message Type'",shape=note,comment="name: \"Dependency on 'Message Type'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="Message",comment="name: \"Message\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 9, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
10 [label="Player Name",comment="name: \"Player Name\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="string",comment="name: \"string\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
12 [label="Message",comment="name: \"Message\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
13 [label="string",comment="name: \"string\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 14, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
15 [label="Message",comment="name: \"Message\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="string",comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="Parameter List",comment="name: \"Parameter List\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
18 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
19 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
21 [label="Parameter",comment="name: \"Parameter\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="string",comment="name: \"string\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 23, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
24 [label="Message",comment="name: \"Message\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
25 [label="string",comment="name: \"string\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="Parameter List",comment="name: \"Parameter List\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
27 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
28 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
29 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
30 [label="Parameter",comment="name: \"Parameter\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
31 [label="string",comment="name: \"string\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
32 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 32, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
33 [label="Message",comment="name: \"Message\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="string",comment="name: \"string\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="Parameter List",comment="name: \"Parameter List\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
36 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
37 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
38 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
39 [label="Parameter",comment="name: \"Parameter\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
40 [label="string",comment="name: \"string\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="if (5)",shape=diamond,comment="name: \"if (5)\", typeName: \"\", id: 41, branchId: 5, recurseId: -1, attributes: 4, notes: \"\""];
42 [label="Message",comment="name: \"Message\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
43 [label="string",comment="name: \"string\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
44 [label="if (6)",shape=diamond,comment="name: \"if (6)\", typeName: \"\", id: 44, branchId: 6, recurseId: -1, attributes: 4, notes: \"\""];
45 [label="Message",comment="name: \"Message\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
46 [label="string",comment="name: \"string\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
47 [label="if (7)",shape=diamond,comment="name: \"if (7)\", typeName: \"\", id: 47, branchId: 7, recurseId: -1, attributes: 4, notes: \"\""];
48 [label="Player Name",comment="name: \"Player Name\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
49 [label="string",comment="name: \"string\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
50 [label="Message",comment="name: \"Message\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
51 [label="string",comment="name: \"string\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
52 [label="if (8)",shape=diamond,comment="name: \"if (8)\", typeName: \"\", id: 52, branchId: 8, recurseId: -1, attributes: 4, notes: \"\""];
53 [label="Player Name",comment="name: \"Player Name\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
54 [label="string",comment="name: \"string\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
55 [label="Message",comment="name: \"Message\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
56 [label="string",comment="name: \"string\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
57 [label="if (9)",shape=diamond,comment="name: \"if (9)\", typeName: \"\", id: 57, branchId: 9, recurseId: -1, attributes: 4, notes: \"\""];
58 [label="Message",comment="name: \"Message\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
59 [label="string",comment="name: \"string\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
60 [label="if (10)",shape=diamond,comment="name: \"if (10)\", typeName: \"\", id: 60, branchId: 10, recurseId: -1, attributes: 4, notes: \"\""];
61 [label="Message",comment="name: \"Message\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
62 [label="string",comment="name: \"string\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
63 [label="if (11)",shape=diamond,comment="name: \"if (11)\", typeName: \"\", id: 63, branchId: 11, recurseId: -1, attributes: 4, notes: \"\""];
64 [label="Message",comment="name: \"Message\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
65 [label="string",comment="name: \"string\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
66 [label="Sender's XUID",comment="name: \"Sender's XUID\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
67 [label="string",comment="name: \"string\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
68 [label="Platform Id",comment="name: \"Platform Id\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
69 [label="string",comment="name: \"string\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
70 [label="Filtered Message",comment="name: \"Filtered Message\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
71 [label="string",comment="name: \"string\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;8;11;13;16;19;22;25;28;31;34;37;40;43;46;49;51;54;56;59;62;65;67;69;71}

}

```

## 字段

```title='TextPacket'
[message_type][localize][dependency_on_message_type][senders_xuid][platform_id][filtered_message]
```

/// html | div.result
//// define
Message Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.textpacket.message_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Raw`|`0`|protocol.enum.raw|
  |`Chat`|`1`|protocol.enum.chat|
  |`Translate`|`2`|protocol.enum.translate|
  |`Popup`|`3`|protocol.enum.popup|
  |`JukeboxPopup`|`4`|protocol.enum.jukeboxpopup|
  |`Tip`|`5`|protocol.enum.tip|
  |`SystemMessage`|`6`|protocol.enum.systemmessage|
  |`Whisper`|`7`|protocol.enum.whisper|
  |`Announcement`|`8`|protocol.enum.announcement|
  |`TextObjectWhisper`|`9`|protocol.enum.textobjectwhisper|
  |`TextObject`|`10`|protocol.enum.textobject|
  |`TextObjectAnnouncement`|`11`|protocol.enum.textobjectannouncement|



////
//// define
Localize?：<!-- md:samp bool -->

- 基本类型。protocol.packet.textpacket.localize.description


////
> 依赖于`Message Type`

///// tab | `Message Type`如果为`0`
```title='if (0)'
[message]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_0.message.description


///////

//////

/////

///// tab | `Message Type`如果为`1`
```title='if (1)'
[player_name][message]
```

////// html | div.result
/////// define
Player Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_1.player_name.description


///////
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_1.message.description


///////

//////

/////

///// tab | `Message Type`如果为`2`
```title='if (2)'
[message][parameter_list]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_2.message.description


///////
```title='Parameter List'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.textpacket.dependency_on_message_type.if_2.parameter_list.array_size.description


////////
```title='示例元素'
[parameter]
```

//////// html | div.result
///////// define
Parameter：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_2.parameter_list.example_element.parameter.description


/////////

////////

///////

//////

/////

///// tab | `Message Type`如果为`3`
```title='if (3)'
[message][parameter_list]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_3.message.description


///////
```title='Parameter List'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.textpacket.dependency_on_message_type.if_3.parameter_list.array_size.description


////////
```title='示例元素'
[parameter]
```

//////// html | div.result
///////// define
Parameter：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_3.parameter_list.example_element.parameter.description


/////////

////////

///////

//////

/////

///// tab | `Message Type`如果为`4`
```title='if (4)'
[message][parameter_list]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_4.message.description


///////
```title='Parameter List'
[array_size][[example_element]..]
```

/////// html | div.result
//////// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.textpacket.dependency_on_message_type.if_4.parameter_list.array_size.description


////////
```title='示例元素'
[parameter]
```

//////// html | div.result
///////// define
Parameter：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_4.parameter_list.example_element.parameter.description


/////////

////////

///////

//////

/////

///// tab | `Message Type`如果为`5`
```title='if (5)'
[message]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_5.message.description


///////

//////

/////

///// tab | `Message Type`如果为`6`
```title='if (6)'
[message]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_6.message.description


///////

//////

/////

///// tab | `Message Type`如果为`7`
```title='if (7)'
[player_name][message]
```

////// html | div.result
/////// define
Player Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_7.player_name.description


///////
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_7.message.description


///////

//////

/////

///// tab | `Message Type`如果为`8`
```title='if (8)'
[player_name][message]
```

////// html | div.result
/////// define
Player Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_8.player_name.description


///////
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_8.message.description


///////

//////

/////

///// tab | `Message Type`如果为`9`
```title='if (9)'
[message]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_9.message.description


///////

//////

/////

///// tab | `Message Type`如果为`10`
```title='if (10)'
[message]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_10.message.description


///////

//////

/////

///// tab | `Message Type`如果为`11`
```title='if (11)'
[message]
```

////// html | div.result
/////// define
Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.dependency_on_message_type.if_11.message.description


///////

//////

/////
//// define
Sender's XUID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.senders_xuid.description


////
//// define
Platform Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.platform_id.description


////
//// define
Filtered Message：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.textpacket.filtered_message.description


////

///


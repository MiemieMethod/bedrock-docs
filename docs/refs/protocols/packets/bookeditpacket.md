# <!-- md:samp BookEditPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp BookEditPacket -->数据包，数字ID是`97`。该数据包用于protocol.packet.bookeditpacket.description

## 结构

```viz
digraph "BookEditPacket" {
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
6 -> 9
9 -> 10
6 -> 11
11 -> 12
5 -> 13
13 -> 14
14 -> 15
13 -> 16
16 -> 17
13 -> 18
18 -> 19
5 -> 20
20 -> 21
21 -> 22
5 -> 23
23 -> 24
24 -> 25
23 -> 26
26 -> 27
5 -> 28
28 -> 29
29 -> 30
28 -> 31
31 -> 32
28 -> 33
33 -> 34

0 [label="BookEditPacket",comment="name: \"BookEditPacket\", typeName: \"\", id: 0, branchId: 97, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Action",comment="name: \"Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Book Slot",comment="name: \"Book Slot\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Action'",shape=note,comment="name: \"Dependency on 'Action'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="Page Index",comment="name: \"Page Index\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Text A",comment="name: \"Text A\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Text B",comment="name: \"Text B\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="string",comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 13, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
14 [label="Page Index",comment="name: \"Page Index\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="byte",comment="name: \"byte\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="Text A",comment="name: \"Text A\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
17 [label="string",comment="name: \"string\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
18 [label="Text B",comment="name: \"Text B\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
19 [label="string",comment="name: \"string\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="if (2)",shape=diamond,comment="name: \"if (2)\", typeName: \"\", id: 20, branchId: 2, recurseId: -1, attributes: 4, notes: \"\""];
21 [label="Page Index",comment="name: \"Page Index\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
22 [label="byte",comment="name: \"byte\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 23, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
24 [label="Page Index A",comment="name: \"Page Index A\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
25 [label="byte",comment="name: \"byte\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="Page Index B",comment="name: \"Page Index B\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
27 [label="byte",comment="name: \"byte\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 28, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
29 [label="Text A",comment="name: \"Text A\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
30 [label="string",comment="name: \"string\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
31 [label="Text B",comment="name: \"Text B\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="string",comment="name: \"string\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="XUID",comment="name: \"XUID\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="string",comment="name: \"string\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;8;10;12;15;17;19;22;25;27;30;32;34}

}

```

## 字段

```title='BookEditPacket'
[action][book_slot][dependency_on_action]
```

/// html | div.result
//// define
Action：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.bookeditpacket.action.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ReplacePage`|`0`|protocol.enum.replacepage|
  |`AddPage`|`1`|protocol.enum.addpage|
  |`DeletePage`|`2`|protocol.enum.deletepage|
  |`SwapPages`|`3`|protocol.enum.swappages|
  |`Finalize`|`4`|protocol.enum.finalize|



////
//// define
Book Slot：<!-- md:samp byte -->

- 基本类型。protocol.packet.bookeditpacket.book_slot.description


////
> 依赖于`Action`

///// tab | `Action`如果为`0`
```title='if (0)'
[page_index][text_a][text_b]
```

////// html | div.result
/////// define
Page Index：<!-- md:samp byte -->

- 基本类型。protocol.packet.bookeditpacket.dependency_on_action.if_0.page_index.description


///////
/////// define
Text A：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.bookeditpacket.dependency_on_action.if_0.text_a.description


///////
/////// define
Text B：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.bookeditpacket.dependency_on_action.if_0.text_b.description


///////

//////

/////

///// tab | `Action`如果为`1`
```title='if (1)'
[page_index][text_a][text_b]
```

////// html | div.result
/////// define
Page Index：<!-- md:samp byte -->

- 基本类型。protocol.packet.bookeditpacket.dependency_on_action.if_1.page_index.description


///////
/////// define
Text A：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.bookeditpacket.dependency_on_action.if_1.text_a.description


///////
/////// define
Text B：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.bookeditpacket.dependency_on_action.if_1.text_b.description


///////

//////

/////

///// tab | `Action`如果为`2`
```title='if (2)'
[page_index]
```

////// html | div.result
/////// define
Page Index：<!-- md:samp byte -->

- 基本类型。protocol.packet.bookeditpacket.dependency_on_action.if_2.page_index.description


///////

//////

/////

///// tab | `Action`如果为`3`
```title='if (3)'
[page_index_a][page_index_b]
```

////// html | div.result
/////// define
Page Index A：<!-- md:samp byte -->

- 基本类型。protocol.packet.bookeditpacket.dependency_on_action.if_3.page_index_a.description


///////
/////// define
Page Index B：<!-- md:samp byte -->

- 基本类型。protocol.packet.bookeditpacket.dependency_on_action.if_3.page_index_b.description


///////

//////

/////

///// tab | `Action`如果为`4`
```title='if (4)'
[text_a][text_b][xuid]
```

////// html | div.result
/////// define
Text A：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.bookeditpacket.dependency_on_action.if_4.text_a.description


///////
/////// define
Text B：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.bookeditpacket.dependency_on_action.if_4.text_b.description


///////
/////// define
XUID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.bookeditpacket.dependency_on_action.if_4.xuid.description


///////

//////

/////

///


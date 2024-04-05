# <!-- md:samp DisconnectPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp DisconnectPacket -->数据包，数字ID是`5`。

## 结构

```viz
digraph "DisconnectPacket" {
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

0 [label="DisconnectPacket",comment="name: \"DisconnectPacket\", typeName: \"\", id: 0, branchId: 5, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Reason",comment="name: \"Reason\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Connection::DisconnectFailReason\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Skip Message",comment="name: \"Skip Message\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dependency on 'Skip Message'",shape=note,comment="name: \"Dependency on 'Skip Message'\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
6 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
7 [label="Message",comment="name: \"Message\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 9, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
10 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;8;10}

}

```

## 字段

```title='DisconnectPacket'
[reason][skip_message][dependency_on_'skip_message']
```

/// html | div.result
//// define
Reason：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。enumeration: Connection::DisconnectFailReason


////
//// define
Skip Message：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。


////
> 依赖于`Skip Message`

///// tab | `Skip Message`如果为`0`
```title='if (0)'
[message]
```

////// html | div.result
/////// define
Message：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


///////

//////

/////

///// tab | `Skip Message`如果为`1`
////// define
if (1)：<!-- md:samp [No Data] -->

- 无数据。


//////

/////

///


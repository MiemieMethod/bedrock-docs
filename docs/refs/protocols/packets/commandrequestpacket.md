# <!-- md:samp CommandRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CommandRequestPacket -->数据包，数字ID是`77`。

## 结构

```viz
digraph "CommandRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 22
0 -> 23
23 -> 24
0 -> 25
25 -> 26

0 [label="CommandRequestPacket",comment="name: \"CommandRequestPacket\", typeName: \"\", id: 0, branchId: 77, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Command",comment="name: \"Command\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Command Origin",comment="name: \"Command Origin\", typeName: \"CommandOriginData\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
22 [label="CommandOriginData",comment="name: \"CommandOriginData\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="Is Internal Source?",comment="name: \"Is Internal Source?\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="bool",comment="name: \"bool\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Version",comment="name: \"Version\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="varint",comment="name: \"varint\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;22;24;26}

}

```

## 字段

/// define
CommandRequestPacket

Command：<!-- md:samp string -->

- 类型：string。

Command Origin：[<!-- md:samp CommandOriginData -->](../types/commandorigindata.md)

- 类型：CommandOriginData。

Is Internal Source?：<!-- md:samp bool -->

- 类型：bool。

Version：<!-- md:samp varint -->

- 类型：varint。


///

# <!-- md:samp CodeBuilderPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp CodeBuilderPacket -->数据包，数字ID是`150`。该数据包用于protocol.packet.codebuilderpacket.description

## 结构

```viz
digraph "CodeBuilderPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="CodeBuilderPacket",comment="name: \"CodeBuilderPacket\", typeName: \"\", id: 0, branchId: 150, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="URL",comment="name: \"URL\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Should open code builder",comment="name: \"Should open code builder\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='CodeBuilderPacket'
[url][should_open_code_builder]
```

/// html | div.result
//// define
URL：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.codebuilderpacket.url.description


////
//// define
Should open code builder：<!-- md:samp bool -->

- 基本类型。protocol.packet.codebuilderpacket.should_open_code_builder.description


////

///


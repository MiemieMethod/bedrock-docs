# <!-- md:samp GameTestResultsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp GameTestResultsPacket -->数据包，数字ID是`195`。

## 结构

```viz
digraph "GameTestResultsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="GameTestResultsPacket",comment="name: \"GameTestResultsPacket\", typeName: \"\", id: 0, branchId: 195, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Succeeded",comment="name: \"Succeeded\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="bool",comment="name: \"bool\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Error",comment="name: \"Error\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="TestName",comment="name: \"TestName\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

/// define
GameTestResultsPacket

Succeeded：<!-- md:samp bool -->

- 类型：bool。

Error：<!-- md:samp string -->

- 类型：string。

TestName：<!-- md:samp string -->

- 类型：string。


///

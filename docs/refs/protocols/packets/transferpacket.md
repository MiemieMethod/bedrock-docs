# <!-- md:samp TransferPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp TransferPacket -->数据包，数字ID是`85`。

## 结构

```viz
digraph "TransferPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="TransferPacket",comment="name: \"TransferPacket\", typeName: \"\", id: 0, branchId: 85, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Server Address",comment="name: \"Server Address\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Server Port",comment="name: \"Server Port\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='TransferPacket'
[server_address][server_port]
```

/// html | div.result
//// define
Server Address：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Server Port：<!-- md:samp unsigned short -->

- 类型：<!-- md:samp unsigned short -->。


////

///


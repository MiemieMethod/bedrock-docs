# <!-- md:samp TickSyncPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp TickSyncPacket -->数据包，数字ID是`23`。

## 结构

```viz
digraph "TickSyncPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="TickSyncPacket",comment="name: \"TickSyncPacket\", typeName: \"\", id: 0, branchId: 23, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Client Request Timestamp",comment="name: \"Client Request Timestamp\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="int64",comment="name: \"int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Server Reception Response Timestamp",comment="name: \"Server Reception Response Timestamp\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="int64",comment="name: \"int64\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='TickSyncPacket'
[client_request_timestamp][server_reception_response_timestamp]
```

/// html | div.result
//// define
Client Request Timestamp：<!-- md:samp int64 -->

- 类型：<!-- md:samp int64 -->。


////
//// define
Server Reception Response Timestamp：<!-- md:samp int64 -->

- 类型：<!-- md:samp int64 -->。


////

///


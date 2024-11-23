# <!-- md:samp WebSocketPacketData -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp WebSocketPacketData -->类型。该类型用于protocol.type.websocketpacketdata.description

## 结构

```viz
digraph "WebSocketPacketData" {
rankdir = LR
2
2 -> 3
3 -> 4

2 [label="WebSocketPacketData",comment="name: \"WebSocketPacketData\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="Websocket Server URI",comment="name: \"Websocket Server URI\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;4}

}

```

## 字段

```title='WebSocketPacketData'
[websocket_server_uri]
```

/// html | div.result
//// define
Websocket Server URI：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.websocketpacketdata.websocket_server_uri.description


////

///


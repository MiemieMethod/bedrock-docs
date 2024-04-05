# <!-- md:samp AutomationClientConnectPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AutomationClientConnectPacket -->数据包，数字ID是`95`。

## 结构

```viz
digraph "AutomationClientConnectPacket" {
rankdir = LR
0
0 -> 1
1 -> 5

0 [label="AutomationClientConnectPacket",comment="name: \"AutomationClientConnectPacket\", typeName: \"\", id: 0, branchId: 95, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Web Socket Data",comment="name: \"Web Socket Data\", typeName: \"WebSocketPacketData\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
5 [label="WebSocketPacketData",comment="name: \"WebSocketPacketData\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;5}

}

```

## 字段

/// define
AutomationClientConnectPacket

Web Socket Data：[<!-- md:samp WebSocketPacketData -->](../types/websocketpacketdata.md)

- 类型：WebSocketPacketData。


///

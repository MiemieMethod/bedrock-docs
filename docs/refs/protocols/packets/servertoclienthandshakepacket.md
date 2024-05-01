# <!-- md:samp ServerToClientHandshakePacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ServerToClientHandshakePacket -->数据包，数字ID是`3`。该数据包用于protocol.packet.servertoclienthandshakepacket.description

## 结构

```viz
digraph "ServerToClientHandshakePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="ServerToClientHandshakePacket",comment="name: \"ServerToClientHandshakePacket\", typeName: \"\", id: 0, branchId: 3, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Handshake WebToken",comment="name: \"Handshake WebToken\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Base64 encoded JSON Web Token that contains the other relevant client properties. roperties Include: salt' = (for use in encryption) he public key used to compute the shared secret for encryption is embedded in the header of the token. It's the signer public key (json value of 'x5u')\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='ServerToClientHandshakePacket'
[handshake_webtoken]
```

/// html | div.result
//// define
Handshake WebToken：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.servertoclienthandshakepacket.handshake_webtoken.descriptionBase64 encoded JSON Web Token that contains the other relevant client properties. roperties Include: salt' = (for use in encryption) he public key used to compute the shared secret for encryption is embedded in the header of the token. It's the signer public key (json value of 'x5u')


////

///


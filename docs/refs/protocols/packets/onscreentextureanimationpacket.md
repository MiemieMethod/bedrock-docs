# <!-- md:samp OnScreenTextureAnimationPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp OnScreenTextureAnimationPacket -->数据包，数字ID是`130`。该数据包用于protocol.packet.onscreentextureanimationpacket.description

## 结构

```viz
digraph "OnScreenTextureAnimationPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="OnScreenTextureAnimationPacket",comment="name: \"OnScreenTextureAnimationPacket\", typeName: \"\", id: 0, branchId: 130, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Effect Id",comment="name: \"Effect Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the effect whose icon should be shown on-screen.\""];
2 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='OnScreenTextureAnimationPacket'
[effect_id]
```

/// html | div.result
//// define
Effect Id：<!-- md:samp unsigned int -->

- 基本类型。protocol.packet.onscreentextureanimationpacket.effect_id.descriptionId of the effect whose icon should be shown on-screen.


////

///


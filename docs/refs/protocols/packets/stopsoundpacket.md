# <!-- md:samp StopSoundPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp StopSoundPacket -->数据包，数字ID是`87`。该数据包用于protocol.packet.stopsoundpacket.description

## 结构

```viz
digraph "StopSoundPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="StopSoundPacket",comment="name: \"StopSoundPacket\", typeName: \"\", id: 0, branchId: 87, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Sound Name",comment="name: \"Sound Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Stop All Sounds?",comment="name: \"Stop All Sounds?\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="bool",comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Stop Music (Legacy)",comment="name: \"Stop Music (Legacy)\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='StopSoundPacket'
[sound_name][stop_all_sounds][stop_music]
```

/// html | div.result
//// define
Sound Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.stopsoundpacket.sound_name.description


////
//// define
Stop All Sounds?：<!-- md:samp bool -->

- 基本类型。protocol.packet.stopsoundpacket.stop_all_sounds.description


////
//// define
Stop Music (Legacy)：<!-- md:samp bool -->

- 基本类型。protocol.packet.stopsoundpacket.stop_music.description


////

///


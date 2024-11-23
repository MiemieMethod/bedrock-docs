# <!-- md:samp AvailableActorIdentifiersPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp AvailableActorIdentifiersPacket -->数据包，数字ID是`119`。该数据包用于protocol.packet.availableactoridentifierspacket.description

## 结构

```viz
digraph "AvailableActorIdentifiersPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="AvailableActorIdentifiersPacket",comment="name: \"AvailableActorIdentifiersPacket\", typeName: \"\", id: 0, branchId: 119, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Actor Info List",comment="name: \"Actor Info List\", typeName: \"CompoundTag\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"CompoundTag containing a list of ActorInfo:rid (RuntimeId - Int),id (string),bid (BaseId - string),hasspawnegg (bool),summonable (bool)\""];
2 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='AvailableActorIdentifiersPacket'
[actor_info_list]
```

/// html | div.result
//// define
Actor Info List：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.availableactoridentifierspacket.actor_info_list.descriptionCompoundTag containing a list of ActorInfo:r'id' (RuntimeId - Int),'id' (string),b'id' (BaseId - string),hasspawnegg (bool),summonable (bool)


////

///


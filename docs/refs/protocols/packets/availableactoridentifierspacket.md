# <!-- md:samp AvailableActorIdentifiersPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AvailableActorIdentifiersPacket -->数据包，数字ID是`119`。

## 结构

```viz
digraph AvailableActorIdentifiersPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"CompoundTag\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
	}
	0	[comment="name: \"AvailableActorIdentifiersPacket\", typeName: \"\", id: 0, branchId: 119, recurseId: -1, attributes: 0, notes: \"\"",
		label=AvailableActorIdentifiersPacket];
	1	[comment="name: \"Actor Info List\", typeName: \"CompoundTag\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"CompoundTag containing \
a list of ActorInfo:rid (RuntimeId - Int),id (string),bid (BaseId - string),hasspawnegg (bool),summonable (bool)\"",
		label="Actor Info List"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
AvailableActorIdentifiersPacket

Actor Info List：[<!-- md:samp CompoundTag -->](refs/protocols/types/compoundtag.md)

- 类型：CompoundTag。CompoundTag containing a list of ActorInfo:r'id' (RuntimeId - Int),'id' (string),b'id' (BaseId - string),hasspawnegg (bool),summonable (bool)


///

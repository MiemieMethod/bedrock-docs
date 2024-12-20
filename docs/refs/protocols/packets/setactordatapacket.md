# <!-- md:samp SetActorDataPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp SetActorDataPacket -->数据包，数字ID是`39`。该数据包用于protocol.packet.setactordatapacket.description

## 结构

```viz
digraph "SetActorDataPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8

0 [label="SetActorDataPacket",comment="name: \"SetActorDataPacket\", typeName: \"\", id: 0, branchId: 39, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Actor Data",comment="name: \"Actor Data\", typeName: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >",comment="name: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Synched Properties",comment="name: \"Synched Properties\", typeName: \"PropertySyncData\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="PropertySyncData",comment="name: \"PropertySyncData\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Tick",comment="name: \"Tick\", typeName: \"PlayerInputTick\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"If this packet is referring to the player or a client predicted vehicle they are in control of, this should be the most recently processed PlayerInputTick from their PlayerAuthInputPacket. Otherwise zero.\""];
8 [label="PlayerInputTick",comment="name: \"PlayerInputTick\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='SetActorDataPacket'
[target_runtime_id][actor_data][synched_properties][tick]
```

/// html | div.result
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.setactordatapacket.target_runtime_id.description


////
//// define
Actor Data：[<!-- md:samp std::vector&lt;std::unique_ptr&lt;DataItem&gt;&gt; -->](../types/std__vector_class_std__unique_ptr_class_dataitem,struct_std__default_delete_class_dataitem___,class_std__allocator_class_std__u.md)

- 特殊类型。protocol.packet.setactordatapacket.actor_data.description


////
//// define
Synched Properties：[<!-- md:samp PropertySyncData -->](../types/propertysyncdata.md)

- 特殊类型。protocol.packet.setactordatapacket.synched_properties.description


////
//// define
Tick：[<!-- md:samp PlayerInputTick -->](../types/playerinputtick.md)

- 特殊类型。protocol.packet.setactordatapacket.tick.descriptionIf this packet is referring to the player or a client predicted vehicle they are in control of, this should be the most recently processed PlayerInputTick from their PlayerAuthInputPacket. Otherwise zero.


////

///


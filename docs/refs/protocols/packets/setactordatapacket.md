# <!-- md:samp SetActorDataPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetActorDataPacket -->数据包，数字ID是`39`。

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
7 [label="Tick",comment="name: \"Tick\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Which frame we're correcting; should match the tick in the Player Auth Input packet. (Can be 0 if not doing server auth movement.)\""];
8 [label="unsigned varint64",comment="name: \"unsigned varint64\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
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

- <!-- md:samp ActorRuntimeID -->类型。


////
//// define
Actor Data：[<!-- md:samp std::vector&lt;class std::unique_ptr&lt;class DataItem,struct std::default_delete&lt;class DataItem&gt; &gt;,class std::allocator&lt;class std::unique_ptr&lt;class DataItem,struct std::default_delete&lt;class DataItem&gt; &gt; &gt; &gt; -->](../types/std__vector_class_std__unique_ptr_class_dataitem,struct_std__default_delete_class_dataitem___,class_std__allocator_class_std__u.md)

- <!-- md:samp std::vector&lt;class std::unique_ptr&lt;class DataItem,struct std::default_delete&lt;class DataItem&gt; &gt;,class std::allocator&lt;class std::unique_ptr&lt;class DataItem,struct std::default_delete&lt;class DataItem&gt; &gt; &gt; &gt; -->类型。


////
//// define
Synched Properties：[<!-- md:samp PropertySyncData -->](../types/propertysyncdata.md)

- <!-- md:samp PropertySyncData -->类型。


////
//// define
Tick：<!-- md:samp unsigned varint64 -->

- <!-- md:samp unsigned varint64 -->类型。Which frame we're correcting; should match the tick in the Player Auth Input packet. (Can be 0 if not doing server auth movement.)


////

///


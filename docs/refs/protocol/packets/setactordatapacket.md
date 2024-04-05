# <!-- md:samp SetActorDataPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetActorDataPacket -->数据包，数字ID是`39`。

## 结构

```viz
digraph SetActorDataPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class \
std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, \
attributes: 512, notes: \"\"",
			label="std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_\
ptr<class DataItem,struct std::default_delete<class DataItem> > > >"];
		6	[comment="name: \"PropertySyncData\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=PropertySyncData];
		8	[comment="name: \"unsigned varint64\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint64"];
	}
	0	[comment="name: \"SetActorDataPacket\", typeName: \"\", id: 0, branchId: 39, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetActorDataPacket];
	1	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Actor Data\", typeName: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class \
std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", id: 3, branchId: 0, recurseId: \
-1, attributes: 256, notes: \"\"",
		label="Actor Data"];
	0 -> 3;
	5	[comment="name: \"Synched Properties\", typeName: \"PropertySyncData\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Synched Properties"];
	0 -> 5;
	7	[comment="name: \"Tick\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Which frame we're correcting; should match \
the tick in the Player Auth Input packet. (Can be 0 if not doing server auth movement.)\"",
		label=Tick];
	0 -> 7;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
SetActorDataPacket

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Actor Data：[<!-- md:samp std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > > -->](refs/protocols/types/std::vector<class_std::unique_ptr<class_dataitem,struct_std::default_delete<class_dataitem>_>,class_std::allocator<class_std::unique_ptr<class_dataitem,struct_std::default_delete<class_dataitem>_>_>_>.md)

- 类型：std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >。

Synched Properties：[<!-- md:samp PropertySyncData -->](refs/protocols/types/propertysyncdata.md)

- 类型：PropertySyncData。

Tick：<!-- md:samp unsigned varint64 -->

- 类型：unsigned varint64。Which frame we're correcting; should match the tick in the Player Auth Input packet. (Can be 0 if not doing server auth movement.)


///

# <!-- md:samp AddItemActorPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AddItemActorPacket -->数据包，数字ID是`15`。

## 结构

```viz
digraph AddItemActorPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		4	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		6	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
		8	[comment="name: \"Vec3\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		10	[comment="name: \"Vec3\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		12	[comment="name: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class \
std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", typeName: \"\", id: 12, branchId: 0, recurseId: \
-1, attributes: 512, notes: \"\"",
			label="std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_\
ptr<class DataItem,struct std::default_delete<class DataItem> > > >"];
		14	[comment="name: \"bool\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"AddItemActorPacket\", typeName: \"\", id: 0, branchId: 15, recurseId: -1, attributes: 0, notes: \"\"",
		label=AddItemActorPacket];
	1	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	0 -> 1;
	3	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 3;
	5	[comment="name: \"Item\", typeName: \"NetworkItemStackDescriptor\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Item];
	0 -> 5;
	7	[comment="name: \"Position\", typeName: \"Vec3\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 7;
	9	[comment="name: \"Velocity\", typeName: \"Vec3\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Velocity];
	0 -> 9;
	11	[comment="name: \"Entity Data\", typeName: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class \
std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", id: 11, branchId: 0, recurseId: \
-1, attributes: 256, notes: \"\"",
		label="Entity Data"];
	0 -> 11;
	13	[comment="name: \"From Fishing?\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="From Fishing?"];
	0 -> 13;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
}

```

## 字段

/// define
AddItemActorPacket

Target Actor ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/ActorRuntimeID.md)

- 类型：ActorRuntimeID。

Item：[<!-- md:samp NetworkItemStackDescriptor -->](refs/protocols/types/NetworkItemStackDescriptor.md)

- 类型：NetworkItemStackDescriptor。

Position：[<!-- md:samp Vec3 -->](refs/protocols/types/Vec3.md)

- 类型：Vec3。

Velocity：[<!-- md:samp Vec3 -->](refs/protocols/types/Vec3.md)

- 类型：Vec3。

Entity Data：[<!-- md:samp std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > > -->](refs/protocols/types/std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >.md)

- 类型：std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >。

From Fishing?：<!-- md:samp bool -->

- 类型：bool。


///

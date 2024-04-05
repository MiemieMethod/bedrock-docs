# <!-- md:samp std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > > -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > > -->类型。

## 结构

```viz
digraph "std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_\
ptr<class DataItem,struct std::default_delete<class DataItem> > > >" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		53	[comment="name: \"unsigned varint\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		55	[comment="name: \"DataItem\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=DataItem];
	}
	51	[comment="name: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class \
std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", typeName: \"\", id: 51, branchId: 0, recurseId: \
-1, attributes: 0, notes: \"\"",
		label="std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_\
ptr<class DataItem,struct std::default_delete<class DataItem> > > >"];
	52	[comment="name: \"Count\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Count];
	51 -> 52;
	54	[comment="name: \"Item\", typeName: \"DataItem\", id: 54, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Item];
	51 -> 54;
	52 -> 53;
	54 -> 55;
}

```

## 字段

/// define
std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >

Count：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Item：[<!-- md:samp DataItem -->](refs/protocols/types/dataitem.md)

- 类型：DataItem。


///

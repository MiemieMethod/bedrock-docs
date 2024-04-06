# <!-- md:samp std::vector&lt;std::unique_ptr&lt;DataItem&gt;&gt; -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::vector&lt;std::unique_ptr&lt;DataItem&gt;&gt; -->类型。

## 结构

```viz
digraph "std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >" {
rankdir = LR
51
51 -> 52
52 -> 53
51 -> 54
54 -> 55

51 [label="std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >",comment="name: \"std::vector<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> >,class std::allocator<class std::unique_ptr<class DataItem,struct std::default_delete<class DataItem> > > >\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
52 [label="Count",comment="name: \"Count\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
53 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
54 [label="Item",comment="name: \"Item\", typeName: \"DataItem\", id: 54, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
55 [label="DataItem",comment="name: \"DataItem\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;53;55}

}

```

## 字段

```title='std::vector&lt;std::unique_ptr&lt;DataItem&gt;&gt;'
[count][item]
```

/// html | div.result
//// define
Count：<!-- md:samp unsigned varint -->

- 基本类型。


////
//// define
Item：[<!-- md:samp DataItem -->](../types/dataitem.md)

- 特殊类型。


////

///


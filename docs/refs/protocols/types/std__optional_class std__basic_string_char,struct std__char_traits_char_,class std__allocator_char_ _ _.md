# <!-- md:samp std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > > -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > > -->类型。

## 结构

```viz
digraph "std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		23	[comment="name: \"bool\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	21	[comment="name: \"std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >\", typeName: \"\", id: \
21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >"];
	22	[comment="name: \"Has Value\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data \
type, otherwise nothing\"",
		label="Has Value"];
	21 -> 22;
	22 -> 23;
}

```

## 字段

/// define
std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >

Has Value：<!-- md:samp bool -->

- 类型：bool。If true, follow with appropriate data type, otherwise nothing


///

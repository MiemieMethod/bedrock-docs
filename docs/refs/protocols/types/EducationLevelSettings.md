# <!-- md:samp EducationLevelSettings -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp EducationLevelSettings -->类型。

## 结构

```viz
digraph EducationLevelSettings {
	graph [rankdir=LR];
	{
		graph [rank=max];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		10	[comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		12	[comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		14	[comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		19	[comment="name: \"std::optional<struct AgentCapabilities>\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<struct AgentCapabilities>"];
		24	[comment="name: \"std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >\", typeName: \"\", id: \
24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >"];
		26	[comment="name: \"bool\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		31	[comment="name: \"std::optional<struct ExternalLinkSettings>\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<struct ExternalLinkSettings>"];
	}
	2	[comment="name: \"EducationLevelSettings\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=EducationLevelSettings];
	3	[comment="name: \"Code Builder Default URI\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Code Builder Default URI"];
	2 -> 3;
	5	[comment="name: \"Code Builder Title\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Code Builder Title"];
	2 -> 5;
	7	[comment="name: \"Can resize Code Builder\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Can resize Code Builder"];
	2 -> 7;
	9	[comment="name: \"Disable legacy title bar\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Disable legacy title bar"];
	2 -> 9;
	11	[comment="name: \"Post Process Filter\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Post Process Filter"];
	2 -> 11;
	13	[comment="name: \"Screenshot Border Resource Path\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Screenshot Border Resource Path"];
	2 -> 13;
	15	[comment="name: \"Agent Capabilities\", typeName: \"std::optional<struct AgentCapabilities>\", id: 15, branchId: 0, recurseId: -1, attributes: \
256, notes: \"\"",
		label="Agent Capabilities"];
	2 -> 15;
	20	[comment="name: \"Code Builder Override Uri\", typeName: \"std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::\
allocator<char> > >\", id: 20, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Code Builder Override Uri"];
	2 -> 20;
	25	[comment="name: \"Indiciates if the world has a quiz attached to it\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\
hasQuiz was only used by old JD China EDU and has been removed\"",
		label="Indiciates if the world has a quiz attached to it"];
	2 -> 25;
	27	[comment="name: \"External Link Settings\", typeName: \"std::optional<struct ExternalLinkSettings>\", id: 27, branchId: 0, recurseId: -1, attributes: \
256, notes: \"\"",
		label="External Link Settings"];
	2 -> 27;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 19;
	20 -> 24;
	25 -> 26;
	27 -> 31;
}

```

## 字段

/// define
EducationLevelSettings

Code Builder Default URI：<!-- md:samp string -->

- 类型：string。

Code Builder Title：<!-- md:samp string -->

- 类型：string。

Can resize Code Builder：<!-- md:samp bool -->

- 类型：bool。

Disable legacy title bar：<!-- md:samp bool -->

- 类型：bool。

Post Process Filter：<!-- md:samp string -->

- 类型：string。

Screenshot Border Resource Path：<!-- md:samp string -->

- 类型：string。

Agent Capabilities：[<!-- md:samp std::optional<struct AgentCapabilities> -->](refs/protocols/types/std::optional<struct AgentCapabilities>.md)

- 类型：std::optional<struct AgentCapabilities>。

Code Builder Override Uri：[<!-- md:samp std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > > -->](refs/protocols/types/std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >.md)

- 类型：std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >。

Indiciates if the world has a quiz attached to it：<!-- md:samp bool -->

- 类型：bool。hasQuiz was only used by old JD China EDU and has been removed

External Link Settings：[<!-- md:samp std::optional<struct ExternalLinkSettings> -->](refs/protocols/types/std::optional<struct ExternalLinkSettings>.md)

- 类型：std::optional<struct ExternalLinkSettings>。


///

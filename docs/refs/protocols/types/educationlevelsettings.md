# <!-- md:samp EducationLevelSettings -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp EducationLevelSettings -->类型。

## 结构

```viz
digraph "EducationLevelSettings" {
rankdir = LR
2
2 -> 3
3 -> 4
2 -> 5
5 -> 6
2 -> 7
7 -> 8
2 -> 9
9 -> 10
2 -> 11
11 -> 12
2 -> 13
13 -> 14
2 -> 15
15 -> 19
2 -> 20
20 -> 24
2 -> 25
25 -> 26
2 -> 27
27 -> 31

2 [label="EducationLevelSettings",comment="name: \"EducationLevelSettings\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="Code Builder Default URI",comment="name: \"Code Builder Default URI\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Code Builder Title",comment="name: \"Code Builder Title\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Can resize Code Builder",comment="name: \"Can resize Code Builder\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="bool",comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Disable legacy title bar",comment="name: \"Disable legacy title bar\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="bool",comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Post Process Filter",comment="name: \"Post Process Filter\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="string",comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Screenshot Border Resource Path",comment="name: \"Screenshot Border Resource Path\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="Agent Capabilities",comment="name: \"Agent Capabilities\", typeName: \"std::optional<struct AgentCapabilities>\", id: 15, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
19 [label="std::optional<struct AgentCapabilities>",comment="name: \"std::optional<struct AgentCapabilities>\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
20 [label="Code Builder Override Uri",comment="name: \"Code Builder Override Uri\", typeName: \"std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >\", id: 20, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
24 [label="std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >",comment="name: \"std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
25 [label="Indiciates if the world has a quiz attached to it",comment="name: \"Indiciates if the world has a quiz attached to it\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"hasQuiz was only used by old JD China EDU and has been removed\""];
26 [label="bool",comment="name: \"bool\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
27 [label="External Link Settings",comment="name: \"External Link Settings\", typeName: \"std::optional<struct ExternalLinkSettings>\", id: 27, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
31 [label="std::optional<struct ExternalLinkSettings>",comment="name: \"std::optional<struct ExternalLinkSettings>\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;4;6;8;10;12;14;19;24;26;31}

}

```

## 字段

```title='EducationLevelSettings'
[code_builder_default_uri][code_builder_title][can_resize_code_builder][disable_legacy_title_bar][post_process_filter][screenshot_border_resource_path][agent_capabilities][code_builder_override_uri][indiciates_if_the_world_has_a_quiz_attached_to_it][external_link_settings]
```

/// html | div.result
//// define
Code Builder Default URI：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Code Builder Title：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Can resize Code Builder：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。


////
//// define
Disable legacy title bar：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。


////
//// define
Post Process Filter：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Screenshot Border Resource Path：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Agent Capabilities：[<!-- md:samp std::optional<struct AgentCapabilities> -->](../types/std__optional_struct_agentcapabilities_.md)

- 类型：<!-- md:samp std::optional<struct AgentCapabilities> -->。


////
//// define
Code Builder Override Uri：[<!-- md:samp std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > > -->](../types/std__optional_class_std__basic_string_char,struct_std__char_traits_char_,class_std__allocator_char_____.md)

- 类型：<!-- md:samp std::optional<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > > -->。


////
//// define
Indiciates if the world has a quiz attached to it：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。hasQuiz was only used by old JD China EDU and has been removed


////
//// define
External Link Settings：[<!-- md:samp std::optional<struct ExternalLinkSettings> -->](../types/std__optional_struct_externallinksettings_.md)

- 类型：<!-- md:samp std::optional<struct ExternalLinkSettings> -->。


////

///


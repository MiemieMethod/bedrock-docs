# <!-- md:samp Experiments -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp Experiments -->类型。该类型用于protocol.type.experiments.description

## 结构

```viz
digraph "Experiments" {
rankdir = LR
29
29 -> 30
30 -> 31
31 -> 32
30 -> 33
33 -> 34
34 -> 35
33 -> 36
36 -> 37
33 -> 38
38 -> 39
33 -> 40
40 -> 41
29 -> 42
42 -> 43

29 [label="Experiments",comment="name: \"Experiments\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
30 [label="Experiments array",comment="name: \"Experiments array\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 8, notes: \"List of currently enabled experiments\""];
31 [label="Streamed Experiment Names Size",comment="name: \"Streamed Experiment Names Size\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
34 [label="Toggle Name",comment="name: \"Toggle Name\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
35 [label="string",comment="name: \"string\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
36 [label="Enabled",comment="name: \"Enabled\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
37 [label="bool",comment="name: \"bool\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
38 [label="Always On Name",comment="name: \"Always On Name\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
39 [label="string",comment="name: \"string\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
40 [label="Enabled",comment="name: \"Enabled\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
41 [label="bool",comment="name: \"bool\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
42 [label="Were Any Experiments Ever Toggled",comment="name: \"Were Any Experiments Ever Toggled\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
43 [label="bool",comment="name: \"bool\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;32;35;37;39;41;43}

}

```

## 字段

```title='Experiments'
[experiments_array][were_any_experiments_ever_toggled]
```

/// html | div.result
```title='Experiments array'
[streamed_experiment_names_size][[example_element]..]
```

//// html | div.result
///// define
Streamed Experiment Names Size：<!-- md:samp unsigned int -->

- 基本类型。protocol.type.experiments.experiments_array.streamed_experiment_names_size.description


/////
```title='示例元素'
[toggle_name][enabled][always_on_name][enabled]
```

///// html | div.result
////// define
Toggle Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.experiments.experiments_array.example_element.toggle_name.description


//////
////// define
Enabled：<!-- md:samp bool -->

- 基本类型。protocol.type.experiments.experiments_array.example_element.enabled.description


//////
////// define
Always On Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.experiments.experiments_array.example_element.always_on_name.description


//////
////// define
Enabled：<!-- md:samp bool -->

- 基本类型。protocol.type.experiments.experiments_array.example_element.enabled.description


//////

/////

////
//// define
Were Any Experiments Ever Toggled：<!-- md:samp bool -->

- 基本类型。protocol.type.experiments.were_any_experiments_ever_toggled.description


////

///


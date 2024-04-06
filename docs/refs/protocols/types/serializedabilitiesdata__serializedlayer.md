# <!-- md:samp SerializedAbilitiesData::SerializedLayer -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SerializedAbilitiesData::SerializedLayer -->类型。

## 结构

```viz
digraph "SerializedAbilitiesData::SerializedLayer" {
rankdir = LR
92
92 -> 93
93 -> 94
92 -> 95
95 -> 96
92 -> 97
97 -> 98
92 -> 99
99 -> 100
92 -> 101
101 -> 102

92 [label="SerializedAbilitiesData::SerializedLayer",comment="name: \"SerializedAbilitiesData::SerializedLayer\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
93 [label="SerializedLayer",comment="name: \"SerializedLayer\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SerializedAbilitiesData::SerializedAbilitiesLayer\""];
94 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 94, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
95 [label="AbilitiesSet",comment="name: \"AbilitiesSet\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
96 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
97 [label="AbilityValues",comment="name: \"AbilityValues\", typeName: \"\", id: 97, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
98 [label="unsigned int",comment="name: \"unsigned int\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
99 [label="FlySpeed",comment="name: \"FlySpeed\", typeName: \"\", id: 99, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
100 [label="float",comment="name: \"float\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
101 [label="WalkSpeed",comment="name: \"WalkSpeed\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
102 [label="float",comment="name: \"float\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;94;96;98;100;102}

}

```

## 字段

```title='SerializedAbilitiesData::SerializedLayer'
[serializedlayer][abilitiesset][abilityvalues][flyspeed][walkspeed]
```

/// html | div.result
//// define
SerializedLayer：<!-- md:samp unsigned short -->

- 类型：<!-- md:samp unsigned short -->。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`CustomCache`|`0`||
  |`Base`|`1`||
  |`Spectator`|`2`||
  |`Commands`|`3`||
  |`Editor`|`4`||



////
//// define
AbilitiesSet：<!-- md:samp unsigned int -->

- 类型：<!-- md:samp unsigned int -->。


////
//// define
AbilityValues：<!-- md:samp unsigned int -->

- 类型：<!-- md:samp unsigned int -->。


////
//// define
FlySpeed：<!-- md:samp float -->

- 类型：<!-- md:samp float -->。


////
//// define
WalkSpeed：<!-- md:samp float -->

- 类型：<!-- md:samp float -->。


////

///


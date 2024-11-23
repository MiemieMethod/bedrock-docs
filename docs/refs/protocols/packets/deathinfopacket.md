# <!-- md:samp DeathInfoPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp DeathInfoPacket -->数据包，数字ID是`189`。该数据包用于protocol.packet.deathinfopacket.description

## 结构

```viz
digraph "DeathInfoPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
4 -> 5
3 -> 6
6 -> 7
7 -> 8
6 -> 9
9 -> 10

0 [label="DeathInfoPacket",comment="name: \"DeathInfoPacket\", typeName: \"\", id: 0, branchId: 189, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Death Cause Attack Name",comment="name: \"Death Cause Attack Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="string",comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Death Cause Message List",comment="name: \"Death Cause Message List\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Death Cause Entity Name",comment="name: \"Death Cause Entity Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Death Cause Entity Name",comment="name: \"Death Cause Entity Name\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8;10}

}

```

## 字段

```title='DeathInfoPacket'
[death_cause_attack_name][death_cause_message_list]
```

/// html | div.result
//// define
Death Cause Attack Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.deathinfopacket.death_cause_attack_name.description


////
```title='Death Cause Message List'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.deathinfopacket.death_cause_message_list.array_size.description


/////
```title='示例元素'
[death_cause_entity_name][death_cause_entity_name]
```

///// html | div.result
////// define
Death Cause Entity Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.deathinfopacket.death_cause_message_list.example_element.death_cause_entity_name.description


//////
////// define
Death Cause Entity Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.deathinfopacket.death_cause_message_list.example_element.death_cause_entity_name.description


//////

/////

////

///


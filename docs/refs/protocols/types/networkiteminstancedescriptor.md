# <!-- md:samp NetworkItemInstanceDescriptor -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NetworkItemInstanceDescriptor -->类型。该类型用于protocol.type.networkiteminstancedescriptor.description

## 结构

```viz
digraph "NetworkItemInstanceDescriptor" {
rankdir = LR
25
25 -> 26
26 -> 27
27 -> 28
28 -> 29
26 -> 30
30 -> 31
31 -> 32
30 -> 33
33 -> 34
30 -> 35
35 -> 36
30 -> 37
37 -> 38
30 -> 39
39 -> 40

25 [label="NetworkItemInstanceDescriptor",comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
26 [label="Dependency on 'Valid item'",shape=note,comment="name: \"Dependency on 'Valid item'\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
27 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
28 [label="Id",comment="name: \"Id\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"Send fixed Id of 0 for invalid item\""];
29 [label="varint",comment="name: \"varint\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 30, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
31 [label="Id",comment="name: \"Id\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="varint",comment="name: \"varint\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
33 [label="Stack size",comment="name: \"Stack size\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
34 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="Aux value",comment="name: \"Aux value\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
36 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="Block Runtime Id",comment="name: \"Block Runtime Id\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
38 [label="varint",comment="name: \"varint\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
39 [label="User Data Buffer",comment="name: \"User Data Buffer\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"The @ItemInstanceUserData.html#ItemInstanceUserData@  binary blob encoded as a String, so it's unsigned varint length prefixed. Get all your nbt+property bytes, calculate the length, write that length, THEN write the data.\""];
40 [label="string",comment="name: \"string\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;29;32;34;36;38;40}

}

```

## 字段

```title='NetworkItemInstanceDescriptor'
[dependency_on_valid_item]
```

/// html | div.result
> 依赖于`Valid item`

///// tab | `Valid item`如果为`0`
```title='if (0)'
[id]
```

////// html | div.result
/////// define
Id：<!-- md:samp varint -->

- 基本类型。protocol.type.networkiteminstancedescriptor.id.descriptionSend fixed Id of 0 for inval'id' item


///////

//////

/////

///// tab | `Valid item`如果为`1`
```title='if (1)'
[id][stack_size][aux_value][block_runtime_id][user_data_buffer]
```

////// html | div.result
/////// define
Id：<!-- md:samp varint -->

- 基本类型。protocol.type.networkiteminstancedescriptor.id.description


///////
/////// define
Stack size：<!-- md:samp unsigned short -->

- 基本类型。protocol.type.networkiteminstancedescriptor.stack_size.description


///////
/////// define
Aux value：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.networkiteminstancedescriptor.aux_value.description


///////
/////// define
Block Runtime Id：<!-- md:samp varint -->

- 基本类型。protocol.type.networkiteminstancedescriptor.block_runtime_id.description


///////
/////// define
User Data Buffer：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.networkiteminstancedescriptor.user_data_buffer.descriptionThe @ItemInstanceUserData.html#ItemInstanceUserData@  binary blob encoded as a String, so it's unsigned varint length prefixed. Get all your nbt+property bytes, calculate the length, write that length, THEN write the data.


///////

//////

/////

///


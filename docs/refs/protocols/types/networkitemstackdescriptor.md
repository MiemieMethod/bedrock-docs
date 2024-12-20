# <!-- md:samp NetworkItemStackDescriptor -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp NetworkItemStackDescriptor -->类型。该类型用于protocol.type.networkitemstackdescriptor.description

## 结构

```viz
digraph "NetworkItemStackDescriptor" {
rankdir = LR
18
18 -> 19
19 -> 20
20 -> 21
21 -> 22
19 -> 23
23 -> 24
24 -> 25
23 -> 26
26 -> 27
23 -> 28
28 -> 29
23 -> 30
30 -> 31
23 -> 32
32 -> 33
33 -> 34
32 -> 35
35 -> 36
36 -> 40
23 -> 41
41 -> 42
23 -> 43
43 -> 44

18 [label="NetworkItemStackDescriptor",comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
19 [label="Dependency on 'Valid item'",shape=note,comment="name: \"Dependency on 'Valid item'\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
20 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
21 [label="Id",comment="name: \"Id\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"Send fixed Id of 0 for invalid item\""];
22 [label="varint",comment="name: \"varint\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
23 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 23, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
24 [label="Id",comment="name: \"Id\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
25 [label="varint",comment="name: \"varint\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="Stack size",comment="name: \"Stack size\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
27 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
28 [label="Aux value",comment="name: \"Aux value\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
29 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
30 [label="Include Net Id",comment="name: \"Include Net Id\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
31 [label="bool",comment="name: \"bool\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
32 [label="Dependency on 'Include Net Id'",shape=note,comment="name: \"Dependency on 'Include Net Id'\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
33 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
34 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="if (1)",shape=diamond,comment="name: \"if (1)\", typeName: \"\", id: 35, branchId: 1, recurseId: -1, attributes: 4, notes: \"\""];
36 [label="Net Id Variant",comment="name: \"Net Id Variant\", typeName: \"ItemStackNetIdVariant\", id: 36, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
40 [label="ItemStackNetIdVariant",comment="name: \"ItemStackNetIdVariant\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="Block Runtime Id",comment="name: \"Block Runtime Id\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
42 [label="varint",comment="name: \"varint\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
43 [label="User Data Buffer",comment="name: \"User Data Buffer\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"The @ItemInstanceUserData.html#ItemInstanceUserData@  binary blob encoded as a String, so it's unsigned varint length prefixed. Get all your nbt+property bytes, calculate the length, write that length, THEN write the data.\""];
44 [label="string",comment="name: \"string\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;22;25;27;29;31;34;40;42;44}

}

```

## 字段

```title='NetworkItemStackDescriptor'
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

- 基本类型。protocol.type.networkitemstackdescriptor.dependency_on_valid_item.if_0.id.descriptionSend fixed Id of 0 for inval'id' item


///////

//////

/////

///// tab | `Valid item`如果为`1`
```title='if (1)'
[id][stack_size][aux_value][include_net_id][dependency_on_include_net_id][block_runtime_id][user_data_buffer]
```

////// html | div.result
/////// define
Id：<!-- md:samp varint -->

- 基本类型。protocol.type.networkitemstackdescriptor.dependency_on_valid_item.if_1.id.description


///////
/////// define
Stack size：<!-- md:samp unsigned short -->

- 基本类型。protocol.type.networkitemstackdescriptor.dependency_on_valid_item.if_1.stack_size.description


///////
/////// define
Aux value：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.networkitemstackdescriptor.dependency_on_valid_item.if_1.aux_value.description


///////
/////// define
Include Net Id：<!-- md:samp bool -->

- 基本类型。protocol.type.networkitemstackdescriptor.dependency_on_valid_item.if_1.include_net_id.description


///////
> 依赖于`Include Net Id`

//////// tab | `Include Net Id`如果为`0`
///////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


/////////

////////

//////// tab | `Include Net Id`如果为`1`
```title='if (1)'
[net_id_variant]
```

///////// html | div.result
////////// define
Net Id Variant：[<!-- md:samp ItemStackNetIdVariant -->](../types/itemstacknetidvariant.md)

- 特殊类型。protocol.type.networkitemstackdescriptor.dependency_on_valid_item.if_1.dependency_on_include_net_id.if_1.net_id_variant.description


//////////

/////////

////////
/////// define
Block Runtime Id：<!-- md:samp varint -->

- 基本类型。protocol.type.networkitemstackdescriptor.dependency_on_valid_item.if_1.block_runtime_id.description


///////
/////// define
User Data Buffer：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.networkitemstackdescriptor.dependency_on_valid_item.if_1.user_data_buffer.descriptionThe @ItemInstanceUserData.html#ItemInstanceUserData@  binary blob encoded as a String, so it's unsigned varint length prefixed. Get all your nbt+property bytes, calculate the length, write that length, THEN write the data.


///////

//////

/////

///


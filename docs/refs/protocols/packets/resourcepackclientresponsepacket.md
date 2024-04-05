# <!-- md:samp ResourcePackClientResponsePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ResourcePackClientResponsePacket -->数据包，数字ID是`8`。

## 结构

```viz
digraph "ResourcePackClientResponsePacket" {
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

0 [label="ResourcePackClientResponsePacket",comment="name: \"ResourcePackClientResponsePacket\", typeName: \"\", id: 0, branchId: 8, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Response",comment="name: \"Response\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ResourcePackResponse\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Downloading Packs",comment="name: \"Downloading Packs\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
4 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="unsigned short",comment="name: \"unsigned short\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
6 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
7 [label="Pack Name",comment="name: \"Pack Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;5;8}

}

```

## 字段

```title='ResourcePackClientResponsePacket'
[response][downloading_packs]
```

/// html | div.result
//// define
Response：<!-- md:samp byte -->

- 类型：<!-- md:samp byte -->。enumeration: ResourcePackResponse


////
```title='Downloading Packs'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned short -->

- 类型：<!-- md:samp unsigned short -->。


/////
```title='示例元素'
[pack_name]
```

///// html | div.result
////// define
Pack Name：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


//////

/////

////

///


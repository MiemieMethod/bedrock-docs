# <!-- md:samp ResourcePackClientResponsePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ResourcePackClientResponsePacket -->数据包，数字ID是`8`。该数据包用于protocol.packet.resourcepackclientresponsepacket.description

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
1 [label="Response",comment="name: \"Response\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 基本类型枚举。protocol.packet.resourcepackclientresponsepacket.response.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Cancel`|`1`|protocol.enum.cancel|
  |`Downloading`|`2`|protocol.enum.downloading|
  |`DownloadingFinished`|`3`|protocol.enum.downloadingfinished|
  |`ResourcePackStackFinished`|`4`|protocol.enum.resourcepackstackfinished|



////
```title='Downloading Packs'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned short -->

- 基本类型。protocol.packet.resourcepackclientresponsepacket.downloading_packs.array_size.description


/////
```title='示例元素'
[pack_name]
```

///// html | div.result
////// define
Pack Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.resourcepackclientresponsepacket.downloading_packs.example_element.pack_name.description


//////

/////

////

///

